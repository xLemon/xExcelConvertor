#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os

from core.base_processor import xBaseProcessor

from utilities.export_helper import xExportHelper
from utilities.file_utility import xFileUtility

from definitions.constant_data import xConstantData

class xProcessorIni(xBaseProcessor) :
	def __init__(self, p_strSuffix, p_strConfig) :
		return super(xProcessorIni, self).__init__('INI', p_strSuffix, p_strConfig)
	
	def ProcessExport(self, p_strWorkbookName, p_cWorkbook, p_cWorkSheet, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel) :
		print('>>>>> 正在处理 工作表 [{0}] => [{1}]'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))

		strExportDirectory = self.GetExportDirectory(p_mapExportConfigs)

		self.PrepareExportDirectory(strExportDirectory)
		
		mapGenerateControl                = { }
		mapGenerateControl['level_index'] = 0
		mapGenerateControl['ident']       = '\t'
		
		strContent  = ''
		strContent += self.__ConvertIniHead(p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs)
		strContent += '\n'
		strContent += self.__ConvertIniContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel, mapGenerateControl)
		strContent += '\n'

		strFileName = '{0}.{1}'.format(p_mapIndexSheetConfigs['DATA_FILE_NAME'], self.Suffix.lower())
		strFilePath = os.path.join(strExportDirectory, strFileName)

		xFileUtility.DeleteFile(strFilePath)
		
		bSuccess = xFileUtility.WriteDataToFile(strFilePath, 'w', strContent)

		if bSuccess :
			print('>>>>> 工作表 [{0}] => [{1}] 处理成功！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
		else :
			print('>>>>> 工作表 [{0}] => [{1}] 处理失败！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
	
		return bSuccess
	
	def __ConvertIniHead(self, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs) :
		nFirstColumnIndex = p_mapDataSheetConfigs.keys()[0]
		nLastColumnIndex  = p_mapDataSheetConfigs.keys()[-1]

		lstPrimaryKeys = []
		lstUniqueKeys  = []

		strContent  = ''

		nIndex = 0

		for nColumnIndex in p_mapDataSheetConfigs :
			if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs) :
				continue

			if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Config, p_mapExportConfigs) :
				continue

			# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
				# continue

			strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs)

			if nIndex > 0 :
				strContent += ','

			strContent += '"{0}"'.format(strFieldName)

			nIndex += 1

		return strContent
	
	
	def __ConvertIniContent(self, p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas, p_nCategoryLevel, p_mapGenerateControl) :
		if type(p_mixPreloadDatas) == dict and p_mixPreloadDatas.has_key('datas') :
			return self.__ConvertIniContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas['datas'], p_nCategoryLevel, p_mapGenerateControl)

		if type(p_mixPreloadDatas) == dict :
			strContent = ''

			for mixKey in p_mixPreloadDatas :
				strContent += self.__ConvertIniContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas[mixKey], p_nCategoryLevel, p_mapGenerateControl)
			
			return strContent

		if type(p_mixPreloadDatas) == list :
			strContent = ''

			for mapLineDatas in p_mixPreloadDatas :
				if self.IsEmptyLine(mapLineDatas) :
					continue

				if p_mapGenerateControl['level_index'] > 0 :
					strContent += '\n'

				nDataColumnIndex = 0

				for nColumnIndex in p_mapDataSheetConfigs :
					if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs) :
						continue

					if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Config, p_mapExportConfigs) :
						continue

					# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
						# continue

					if nDataColumnIndex > 0 :
						strContent += ','

					strCellValue = ''
					strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs)
					
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

					strCellValue = strCellValue.replace('"', '\"')

					strContent += '"{0}"'.format(strCellValue)

					nDataColumnIndex += 1
				
				p_mapGenerateControl['level_index'] += 1

			return strContent