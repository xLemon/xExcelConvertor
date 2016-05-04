#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os

from core.base_processor import xBaseProcessor

from utilities.export_helper import xExportHelper
from utilities.file_utility import xFileUtility

from definitions.constant_data import xConstantData

class xProcessorSql(xBaseProcessor) :
	def __init__(self) :
		return super(xProcessorSql, self).__init__('SQL')

	def ProcessGlobalFile(self, p_strWorkbookName, p_mapExportConfigs, p_mapDatabaseConfigs) :
		strExportDirectory = self.GetExportDirectory(p_mapExportConfigs)

		self.PrepareExportDirectory(strExportDirectory)

		strFileName = '{0}.{1}'.format(p_strWorkbookName, self.Type.lower())

		xFileUtility.DeleteFile(os.path.join(strExportDirectory, strFileName))

		strContent  = '\n'
		strContent += '-- Database - {0}\n'.format(p_mapDatabaseConfigs['DATABASE_NAME'])
		strContent += '\n'
		strContent += 'CREATE DATABASE IF NOT EXISTS `{0}` DEFAULT CHARACTER SET {1} COLLATE {2};\n\n'.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATABASE_CHARSET'], p_mapDatabaseConfigs['DATABASE_COLLATE'])
				
		if not xFileUtility.WriteDataToFile(os.path.join(strExportDirectory, strFileName), 'a+', strContent) :
			raise Exception('文件{0}写入失败！'.format(os.path.join(strExportDirectory, strFileName)))

		return True

	def ProcessExport(self, p_strWorkbookName, p_cWorkbook, p_cWorkSheet, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel) :
		print('>>>>> 正在处理 工作表 [{0}] => [{1}]'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))

		strContent  = ''
		strContent += '-- Table structure for table `{0}`.`{1}{2}`\n\n'.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATA_TABLE_PREFIX'], p_mapIndexSheetConfigs['DATA_FILE_NAME'])
		strContent += self.__ConvertCreateTableSQL(p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs)
		strContent += '\n\n'

		strContent += '-- Dumping data for table `{0}`.`{1}{2}`\n\n'.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATA_TABLE_PREFIX'], p_mapIndexSheetConfigs['DATA_FILE_NAME'])
		strContent += self.__ConvertTableDataSQL(p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel)
		strContent += '\n\n'
		
		strFileName = '{0}.{1}'.format(p_strWorkbookName, self.Type.lower())
		strFilePath = os.path.join(self.GetExportDirectory(p_mapExportConfigs), strFileName)

		bSuccess = xFileUtility.WriteDataToFile(strFilePath, 'a+', strContent)

		if bSuccess :
			print('>>>>> 工作表 [{0}] => [{1}] 处理成功！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
		else :
			print('>>>>> 工作表 [{0}] => [{1}] 处理失败！'.format(p_mapIndexSheetConfigs['DATA_SHEET'], self.Type.lower()))
	
		return bSuccess
	
	def __ConvertCreateTableSQL(self, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs) :
		nFirstColumnIndex = p_mapDataSheetConfigs.keys()[0]
		nLastColumnIndex  = p_mapDataSheetConfigs.keys()[-1]

		lstPrimaryKeys = []
		lstUniqueKeys  = []

		strContent  = ''
		strContent += 'DROP TABLE IF EXISTS `{0}`.`{1}{2}`;'.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATA_TABLE_PREFIX'], p_mapIndexSheetConfigs['DATA_FILE_NAME'])
		strContent += '\n\n'
		strContent += 'CREATE TABLE `{0}`.`{1}{2}` (\n'.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATA_TABLE_PREFIX'], p_mapIndexSheetConfigs['DATA_FILE_NAME'])

		nIndex = 0

		for nColumnIndex in p_mapDataSheetConfigs :
			if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs) :
				continue

			if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Type, p_mapExportConfigs) :
				continue

			# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
				# continue

			strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs)

			if nIndex > 0 :
				strContent += ',\n'

			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_LENGTH] > 0 :
				strContent += '\t`{0}` {1}({2})'.format(strFieldName, p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper(), p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_LENGTH])
			else :
				strContent += '\t`{0}` {1}'.format(strFieldName, p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper())

			if xConstantData.MYSQL_DATA_DEFINITIONS[p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()]['COLLATE'] :
				strContent += ' COLLATE {0}'.format(p_mapIndexSheetConfigs['DATA_TABLE_COLLATE'])

			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_PRIMARY_KEY_IDENTIFIER] is not None :
				lstPrimaryKeys.append(strFieldName)

			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_UNIQUE_IDENTIFIER] is not None :
				lstUniqueKeys.append(strFieldName)
				
			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_UNSIGNED_IDENTIFIER] is not None and not xConstantData.MYSQL_DATA_DEFINITIONS[p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()]['IS_STRING'] :
				strContent += ' UNSIGNED'

			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_NULL_IDENTIFIER] is not None :
				strContent += ' NOT NULL'

			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
				strContent += ' AUTO_INCREMENT'
			else :
				if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DEFAULT_VALUE] is not None :
					if xConstantData.MYSQL_DATA_DEFINITIONS[p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()]['IS_STRING'] :
						strContent += ' DEFAULT \'{0}\''.format(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DEFAULT_VALUE])
					else :
						strContent += ' DEFAULT {0}'.format(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DEFAULT_VALUE])

			if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_COMMENT] is not None :
				strContent += ' COMMENT \'{0}\''.format(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_COMMENT])

			nIndex += 1

		nPrimaryKeys = len(lstPrimaryKeys)

		if nPrimaryKeys > 0 :
			nPrimaryKeyIndex = 0

			strContent += ',\n\tPRIMARY KEY ('

			for strPrimaryKey in lstPrimaryKeys :
				if strPrimaryKey in lstUniqueKeys :
					lstUniqueKeys.pop(lstUniqueKeys.index(strPrimaryKey))

				if nPrimaryKeyIndex > 0 :
					strContent += ', '

				strContent += '`{0}`'.format(strPrimaryKey)

				nPrimaryKeyIndex += 1

			strContent += ')'

		nUniqueKeys = len(lstUniqueKeys)

		if nUniqueKeys > 0 :
			nUniqueKeyIndex = 0

			strContent += ',\n\tUNIQUE KEY ('

			for strUniqueKey in lstUniqueKeys :
				if nUniqueKeyIndex > 0 :
					strContent += ', '

				strContent += '`{0}`'.format(strUniqueKey)

				nUniqueKeyIndex += 1

			strContent += ')'
		
		strContent += '\n) ENGINE = {0} DEFAULT CHARSET = {1} COLLATE = {2} COMMENT \'{3}\';'.format(p_mapIndexSheetConfigs['DATA_TABLE_ENGINE'], p_mapIndexSheetConfigs['DATA_TABLE_CHARSET'], p_mapIndexSheetConfigs['DATA_TABLE_COLLATE'], p_mapIndexSheetConfigs['DATA_SHEET'])

		return strContent
	
	def __ConvertTableDataSQL(self, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel) :
		nFirstColumnIndex = p_mapDataSheetConfigs.keys()[0]
		nLastColumnIndex  = p_mapDataSheetConfigs.keys()[-1]

		strContent  = ''
		strContent += 'TRUNCATE TABLE `{0}`.`{1}{2}`;'.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATA_TABLE_PREFIX'], p_mapIndexSheetConfigs['DATA_FILE_NAME'])
		strContent += '\n\n'
		strContent += 'INSERT INTO `{0}`.`{1}{2}` ('.format(p_mapDatabaseConfigs['DATABASE_NAME'], p_mapDatabaseConfigs['DATA_TABLE_PREFIX'], p_mapIndexSheetConfigs['DATA_FILE_NAME'])

		nIndex = 0

		for nColumnIndex in p_mapDataSheetConfigs :
			if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs) :
				continue

			if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Type, p_mapExportConfigs) :
				continue

			strFieldName = xExportHelper.GetFieldNameAsI18N(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_FIELD], p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs)

			# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
				# continue

			if nIndex > 0 :
				strContent += ', '

			strContent += '`{0}`'.format(strFieldName)

			nIndex += 1

		strContent += ')\nVALUES\n'
		
		mapGenerateControl = {}
		mapGenerateControl['line_index'] = 0

		strDataSQL = self.__ConvertTableDataValueSQL(p_mapExportConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel, mapGenerateControl)

		if len(strDataSQL) > 0 :
			strContent += strDataSQL
			strContent += ';'
		else :
			strContent = ''

		return strContent
	
	def __ConvertTableDataValueSQL(self, p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas, p_nCategoryLevel, p_mapGenerateControl) :
		if type(p_mixPreloadDatas) == dict and p_mixPreloadDatas.has_key('datas') :
			return self.__ConvertTableDataValueSQL(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas['datas'], p_nCategoryLevel, p_mapGenerateControl)

		if type(p_mixPreloadDatas) == dict :
			strContent = ''

			for mixKey in p_mixPreloadDatas :
				strContent += self.__ConvertTableDataValueSQL(p_mapExportConfigs, p_mapDataSheetConfigs, p_mixPreloadDatas[mixKey], p_nCategoryLevel, p_mapGenerateControl)
			
			return strContent

		if type(p_mixPreloadDatas) == list :
			strContent = ''

			for mapLineDatas in p_mixPreloadDatas :
				if self.IsEmptyLine(mapLineDatas) :
					continue

				if p_mapGenerateControl['line_index'] > 0 :
					strContent += ',\n'

				strContent += '('

				nDataColumnIndex = 0

				for nColumnIndex in p_mapDataSheetConfigs :
					if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], self.Type, p_mapExportConfigs) :
						continue

					if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], self.Type, p_mapExportConfigs) :
						continue

					# if p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER] is not None :
						# continue

					if nDataColumnIndex > 0 :
						strContent += ', '

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

					strCellValue = strCellValue.replace('\'', '\'\'')

					if xConstantData.MYSQL_DATA_DEFINITIONS[p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_DATA_TYPE].upper()]['IS_STRING'] :
						strContent += '\'{0}\''.format(strCellValue)
					else :
						strContent += '{0}'.format(strCellValue)

					nDataColumnIndex += 1

				strContent += ')'
				
				p_mapGenerateControl['line_index'] += 1

			return strContent
