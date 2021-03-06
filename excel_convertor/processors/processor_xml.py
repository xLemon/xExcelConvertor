#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os

from core.base_processor import xBaseProcessor

from utilities.export_helper import xExportHelper
from utilities.file_utility import xFileUtility

from definitions.constant_data import xConstantData

class xProcessorXml(xBaseProcessor) :
	def __init__(self, p_strSuffix, p_strConfig) :
		return super(xProcessorXml, self).__init__('XML', p_strSuffix, p_strConfig)

	def ProcessExport(self, p_strWorkbookName, p_cWorkbook, p_cWorkSheet, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel) :
		print('>>>>> 正在处理 工作表 [{0}] => [{1}]'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
		
		lstExportDirectories = self.GetExportDirectories(p_mapExportConfigs)

		self.PrepareExportDirectories(lstExportDirectories)
		
		lstCategoryLevelColumnIndexIndexs = self.GetCategoryLevelColumnIndexList(p_nCategoryLevel, self.Config, p_mapExportConfigs, p_mapDataSheetConfigs)
		
		mapGenerateControl                = { }
		mapGenerateControl['level_index'] = 0
		mapGenerateControl['ident']       = '\t'
		
		nAdditionIdents = 0

		bFirstChildSheet = False

		if 'FIRST_CHILD_SHEET' in p_mapExportConfigs['EXPORTS'][self.Config] :
			bFirstChildSheet = p_mapExportConfigs['EXPORTS'][self.Config]['FIRST_CHILD_SHEET']

		strDocumentRoot = 'items'

		if 'DOCUMENT_ROOT' in p_mapExportConfigs['EXPORTS'][self.Config] :
			strDocumentRoot = p_mapExportConfigs['EXPORTS'][self.Config]['DOCUMENT_ROOT']

		strContent = ''

		if 'DOCUMENT_HEADER' in p_mapExportConfigs['EXPORTS'][self.Config] :
			strContent += '{0}\n'.format(p_mapExportConfigs['EXPORTS'][self.Config]['DOCUMENT_HEADER'])
		else :
			strContent += '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'

		strContent += '\n'
		strContent += '<!--\n'
		strContent += '\n'
		strContent += '!!! DO NOT EDIT THIS FILE !!!\n'
		strContent += '\n'
		strContent += '{0}\n'.format(self.GetCopyrightString(p_mapExportConfigs['COPYRIGHT']['ORGANIZATION'], p_mapExportConfigs['COPYRIGHT']['SINCE_YEAR']))
		strContent += '\n'
		strContent += 'Create By   : {0}\n'.format(self.GetAuthorString())
		strContent += '\n'
		strContent += 'Description : {0}\n'.format(p_cWorkSheet.title)
		strContent += '\n'
		strContent += '-->\n'
		strContent += '\n'
		strContent += '<{0}'.format(strDocumentRoot)

		if 'DOCUMENT_ROOT_ATTR' in p_mapExportConfigs['EXPORTS'][self.Config] :
			strContent += ' '
			strContent += p_mapExportConfigs['EXPORTS'][self.Config]['DOCUMENT_ROOT_ATTR']

		strContent += '>'

		###########################################

		if bFirstChildSheet :
			nAdditionIdents = 1

			if p_mapExportConfigs['EXPORTS'][self.Config]['FORMAT_DATA'] :
				strContent += '\n{0}'.format(self.GenerateIdentIdentifier(mapGenerateControl['level_index'] + 1, mapGenerateControl['ident']))
			
			strContent += '<Group id="{0}">'.format(p_mapIndexSheetConfigs['DATA_FILE_NAME'])

		###########################################

		strContent += self.__ConvertXMLContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, mapGenerateControl, nAdditionIdents, p_mapIndexSheetConfigs['EXPORT_EMPTY_DATA_ITEM'])
		
		###########################################

		if bFirstChildSheet :
			if p_mapExportConfigs['EXPORTS'][self.Config]['FORMAT_DATA'] :
				strContent += '\n{0}'.format(self.GenerateIdentIdentifier(mapGenerateControl['level_index'] + 1, mapGenerateControl['ident']))
			
			strContent += '</Group>'

		###########################################

		if p_mapExportConfigs['EXPORTS'][self.Config]['FORMAT_DATA'] :
			strContent += '\n'

		strContent += '</{0}>\n'.format(strDocumentRoot)
		
		strFileName = '{0}.{1}'.format(p_mapIndexSheetConfigs['DATA_FILE_NAME'], self.Suffix.lower())

		for strExportDirectory in lstExportDirectories :
			strFilePath = os.path.join(strExportDirectory, strFileName)

			xFileUtility.DeleteFile(strFilePath)
			
			bSuccess = xFileUtility.WriteDataToFile(strFilePath, 'w', strContent)

			if not bSuccess :
				break

		if bSuccess :
			print('>>>>> 工作表 [{0}] => [{1}] 处理成功！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
		else :
			print('>>>>> 工作表 [{0}] => [{1}] 处理失败！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
	
		return bSuccess
	
	def __ConvertXMLContent(self, p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas, p_lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, p_mapGenerateControl, p_nAdditionIdents, p_bExportEmptyDataItem) :
		if type(p_mixPreloadDatas) == dict and p_mixPreloadDatas.has_key('datas') :
			return self.__ConvertXMLContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas['datas'], p_lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, p_mapGenerateControl, p_nAdditionIdents, p_bExportEmptyDataItem)

		if type(p_mixPreloadDatas) == dict :
			strContent = ''

			p_mapGenerateControl['level_index'] += 1

			for mixKey in p_mixPreloadDatas :
				nColumnIndex = p_lstCategoryLevelColumnIndexIndexs[p_mapGenerateControl['level_index'] - 1]

				strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs)

				if p_mapExportConfigs['EXPORTS'][self.Config]['FORMAT_DATA'] :
					strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'] + p_nAdditionIdents, p_mapGenerateControl['ident']))

				strContent += '<{0} value="{1}">'.format(strFieldName, mixKey)
				strContent += self.__ConvertXMLContent(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas[mixKey], p_lstCategoryLevelColumnIndexIndexs, p_nCategoryLevel, p_mapGenerateControl, p_nAdditionIdents, p_bExportEmptyDataItem)
				
				if p_mapExportConfigs['EXPORTS'][self.Config]['FORMAT_DATA'] :
					strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'] + p_nAdditionIdents, p_mapGenerateControl['ident']))

				strContent += '</{0}>'.format(strFieldName)
			
			p_mapGenerateControl['level_index'] -= 1

			return strContent

		if type(p_mixPreloadDatas) == list :
			strContent = ''

			for mapLineDatas in p_mixPreloadDatas :
				if self.IsEmptyLine(mapLineDatas) :
					continue

				if p_mapExportConfigs['EXPORTS'][self.Config]['FORMAT_DATA'] :
					strContent += '\n{0}'.format(self.GenerateIdentIdentifier(p_mapGenerateControl['level_index'] + p_nAdditionIdents + 1, p_mapGenerateControl['ident']))

				strContent += '<'

				if 'DOCUMENT_ITEM' in p_mapExportConfigs['EXPORTS'][self.Config] :
					strContent += p_mapExportConfigs['EXPORTS'][self.Config]['DOCUMENT_ITEM']
				else :
					strContent += 'item'

				strContent += ' '

				for nColumnIndex in p_mapDataSheetConfigs :
					if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs) :
						continue

					if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Config, p_mapExportConfigs) :
						continue

					# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
						# continue

					strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Config, p_mapExportConfigs)

					if mapLineDatas[strFieldName] is None and not p_bExportEmptyDataItem :
						continue

					strDefaultValue = p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DEFAULT_VALUE]
					strDataType     = p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()

					strCellValue = self.GetCellValue(mapLineDatas[strFieldName], strDefaultValue, strDataType, p_bExportEmptyDataItem)
					strCellValue = strCellValue.replace('<', '&lt;')
					strCellValue = strCellValue.replace('>', '&gt;')
					strCellValue = strCellValue.replace('"', '&quot;')

					if len(strCellValue) > 0 or p_bExportEmptyDataItem :
						strContent += '{0}="{1}" '.format(strFieldName, strCellValue)

				strContent += '/>'

			return strContent
