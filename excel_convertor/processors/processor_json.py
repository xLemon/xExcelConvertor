#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os

from core.base_processor import xBaseProcessor

from utilities.export_helper import xExportHelper
from utilities.file_utility import xFileUtility

from definitions.constant_data import xConstantData

class xProcessorJson(xBaseProcessor) :
	def __init__(self) :
		return super(xProcessorJson, self).__init__('JSON')
	
	def ProcessExport(self, p_strWorkbookName, p_cWorkbook, p_cWorkSheet, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel) :
		print('>>>>> 正在处理 工作表 [{0}] => [{1}]'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))

		strExportDirectory = self.GetExportDirectory(p_mapExportConfigs)

		self.PrepareExportDirectory(strExportDirectory)
		
		lstCategoryLevelColumnIndexIndexs = self.GetCategoryLevelColumnIndexList(p_nCategoryLevel, self.Type, p_mapExportConfigs, p_mapDataSheetConfigs)
		
		mapGenerateControl                = { }
		mapGenerateControl['level_index'] = 0
		mapGenerateControl['ident']       = '\t'
		
		strContent  = ''
		strContent += '{'
		strContent += self.__ConvertJsonContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, mapGenerateControl)
		
		if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] :
			strContent += '\n'

		strContent += '}\n'

		strFileName = '{0}.{1}'.format(p_mapIndexSheetConfigs['DATA_FILE_NAME'], self.Type.lower())
		strFilePath = os.path.join(strExportDirectory, strFileName)

		xFileUtility.DeleteFile(strFilePath)
		
		bSuccess = xFileUtility.WriteDataToFile(strFilePath, 'w', strContent)

		if bSuccess :
			print('>>>>> 工作表 [{0}] => [{1}] 处理成功！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
		else :
			print('>>>>> 工作表 [{0}] => [{1}] 处理失败！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
	
		return bSuccess
	
	def __ConvertJsonContent(self, p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas, p_lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, p_mapGenerateControl) :
		if type(p_mixPreloadDatas) == dict and p_mixPreloadDatas.has_key('datas') :
			return self.__ConvertJsonContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas['datas'], p_lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, p_mapGenerateControl)

		if type(p_mixPreloadDatas) == dict :
			strContent = ''

			p_mapGenerateControl['level_index'] += 1

			for mixKey in p_mixPreloadDatas :
				if mixKey is None :
					continue
				
				if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] :
					strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'], p_mapGenerateControl['ident']))
				
				strKey = '{0}'.format(mixKey)
				strKey = strKey.replace('"', '\\"')

				strContent += '"{0}"'.format(strKey)
				
				if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] :
					strContent += ' : '
				else :
					strContent += ':'

				if type(p_mixPreloadDatas[mixKey]) == list and len(p_mixPreloadDatas[mixKey]) > 1 :
					strContent += '['
				else :
					strContent += '{'

				strContent += self.__ConvertJsonContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas[mixKey], p_lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, p_mapGenerateControl)
				
				if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] and p_mapGenerateControl['level_index'] < len(p_lstCategoryLevelColumnIndexIndexs) :
					strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'], p_mapGenerateControl['ident']))
				
				if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] and type(p_mixPreloadDatas[mixKey]) == list and len(p_mixPreloadDatas[mixKey]) > 1 :
					strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'], p_mapGenerateControl['ident']))
					
				if type(p_mixPreloadDatas[mixKey]) == list and len(p_mixPreloadDatas[mixKey]) > 1 :
					strContent += '],'
				else :
					strContent += '},'

			p_mapGenerateControl['level_index'] -= 1

			return strContent[0:-1]

		if type(p_mixPreloadDatas) == list :
			nPreloadDataSize = len(p_mixPreloadDatas)

			strContent = ''

			nDataBlock = 0

			for mapLineDatas in p_mixPreloadDatas :
				nDataColumnIndex = 0

				if self.IsEmptyLine(mapLineDatas) :
					nPreloadDataSize -= 1
					continue

				if nPreloadDataSize > 1 :
					if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] :
						strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'] + 1, p_mapGenerateControl['ident']))
					strContent += '{'

				for nColumnIndex in p_mapDataSheetConfigs :
					if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs) :
						continue

					if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Type, p_mapExportConfigs) :
						continue

					# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
						# continue

					strCellValue = ''
					strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs)

					if mapLineDatas[strFieldName] is None :
						if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DEFAULT_VALUE] is not None :
							strCellValue = '{0}'.format(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DEFAULT_VALUE])
						else :
							if xConstantData.MYSQL_DATA_DEFINITIONS[p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()]['IS_STRING'] :
								strCellValue = ''
							else :
								strCellValue = '0'
					else :
						strCellValue = '{0}'.format(mapLineDatas[strFieldName])

					strCellValue = strCellValue.replace('"', '\\"')

					if nDataColumnIndex > 0 :
						strContent += ','
	
					if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] :
						strContent += ' '

					strContent += '"{0}"'.format(strFieldName)

					if p_mapExportConfigs['EXPORTS'][self.Type]['FORMAT_DATA'] :
						strContent += ' : '
					else :
						strContent += ':'

					if xConstantData.MYSQL_DATA_DEFINITIONS[p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()]['IS_STRING'] :
						strContent += '"{0}"'.format(strCellValue)
					else :
						strContent += '{0}'.format(strCellValue)

					nDataColumnIndex += 1

				if nPreloadDataSize > 1 :
					strContent += '},'

				nDataBlock += 1

			if nDataBlock >= 2 :
				return strContent[0:-1]
			else :
				return strContent
