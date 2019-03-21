#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import abc
import time

from utilities.export_helper import xExportHelper
from utilities.file_utility import xFileUtility

from definitions.constant_data import xConstantData

class xBaseProcessor(object) :
	__metaclass__ = abc.ABCMeta

	__strType   = None
	__strSuffix = None
	__strConfig = None

	def __init__(self, p_strType = None, p_strSuffix = None, p_strConfig = None) :
		self.__strType   = p_strType
		self.__strSuffix = p_strSuffix
		self.__strConfig = p_strConfig
		# print('{0}__{1}__{2}'.format(p_strType, p_strSuffix, p_strConfig))
		return super(xBaseProcessor, self).__init__()

	@property
	def Type(self) :
		return self.__strType

	@property
	def Suffix(self) :
		return self.__strSuffix

	@property
	def Config(self) :
		return self.__strConfig

	def ProcessGlobalFile(self, p_strWorkbookName, p_mapExportConfigs, p_mapDatabaseConfigs) :
		return True

	@abc.abstractmethod
	def ProcessExport(self, p_strWorkbookName, p_cWorkbook, p_cWorkSheet, p_mapExportConfigs, p_mapDatabaseConfigs, p_mapIndexSheetConfigs, p_mapDataSheetConfigs, p_mapPreloadDataMaps, p_nCategoryLevel) :
		pass

	def PrepareExportDirectory(self, p_strExportDirectory) :
		if xFileUtility.IsFileOrDirectoryExist(p_strExportDirectory) :
			return True

		if not xFileUtility.CreateDirectory(p_strExportDirectory) :
			raise Exception('创建目录失败 : {0}'.format(p_strExportDirectory))

		return True

	def PrepareExportDirectories(self, p_lstExportDirectory) :
		for strExportDirectory in p_lstExportDirectory :
			self.PrepareExportDirectory(strExportDirectory)

	def IsEmptyLine(self, p_mapLineDatas) :
		nLineItems = len(p_mapLineDatas)

		if nLineItems <= 0 :
			return True

		lstNoneValueItems = []

		for mixKey in p_mapLineDatas :
			if p_mapLineDatas[mixKey] is None :
				lstNoneValueItems.append(mixKey)

		return len(lstNoneValueItems) >= nLineItems
	
	def GetCategoryLevelColumnIndexList(self, p_nCategoryLevel, p_strExportType, p_mapExportConfigs, p_mapDataSheetConfigs) :
		if p_nCategoryLevel <= 0 :
			return []

		lstTierColumnIndexs = []

		nTierIndex = 0
		nCellIndex = 0

		for nColumnIndex in p_mapDataSheetConfigs :
			if nTierIndex >= p_nCategoryLevel :
				break

			if not xExportHelper.IsDataSheetColumnLanguageAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_LANGUAGE_CODE], p_strExportType, p_mapExportConfigs) :
				continue

			if not xExportHelper.IsDataSheetColumnExportTypeAvailable(p_mapDataSheetConfigs[nColumnIndex][xConstantData.DATA_SHEET_ROW_EXPORT_IDENTIFIER], p_strExportType, p_mapExportConfigs) :
				continue

			lstTierColumnIndexs.append(nColumnIndex)

			nTierIndex += 1

		return lstTierColumnIndexs
	
	def GenerateIdentIdentifier(self, p_nCount, p_strIdentIdentifier) :
		if p_nCount == 1 :
			return p_strIdentIdentifier

		if p_nCount <= 0 :
			return ''

		strIdentIdentifier = ''

		for i in xrange(0, p_nCount) :
			strIdentIdentifier += p_strIdentIdentifier

		return strIdentIdentifier

	def GetCopyrightString(self, p_strOrganization, p_nSinceYear) :
		nTime = time.time()

		cLocalTime = time.localtime(nTime)

		strYear = ''

#		if cLocalTime.tm_year <= int(p_nSinceYear) :
#			strYear = '{0}'.format(p_nSinceYear)
#		else :
#			strYear = '{0} - {1}'.format(p_nSinceYear, cLocalTime.tm_year)

		strYear = 'Since {0}'.format(p_nSinceYear)

		return 'Copyright (c) {0}, {1}, All Rights Reserved.'.format(strYear, p_strOrganization)
	
	def GetAuthorString(self) :
		return '{0}({1})'.format(xConstantData.EC_NAME, 'https://github.com/xLemon/xExcelConvertor')

	def GetExportDirectory(self, p_mapExportConfigs) :
		strExportDirectory = p_mapExportConfigs['EXPORTS'][self.Config]['EXPORT_DIRECTORY']

		if not xFileUtility.IsFileOrDirectoryExist(strExportDirectory) :
			xFileUtility.CreateDirectory(strExportDirectory)

		return strExportDirectory

	def GetExportDirectories(self, p_mapExportConfigs) :
		lstExportDirectories = p_mapExportConfigs['EXPORTS'][self.Config]['EXPORT_DIRECTORY'].split(xConstantData.PATH_SEPARATOR)

		for strExportDirectory in lstExportDirectories :
			if not xFileUtility.IsFileOrDirectoryExist(strExportDirectory) :
				xFileUtility.CreateDirectory(strExportDirectory)

		return lstExportDirectories

	def GetCellValue(self, p_strValue, p_strDefaultValue, p_strDataType, p_bExportEmptyDataItem) :
		if p_strValue is not None :
			return self.FixCellValue('{0}'.format(p_strValue), p_strDataType)

		if p_strDefaultValue is not None:
			return self.FixCellValue('{0}'.format(p_strDefaultValue), p_strDataType)

		if xConstantData.MYSQL_DATA_DEFINITIONS[p_strDataType]['IS_STRING'] :
			return self.FixCellValue('', p_strDataType)

		return self.FixCellValue('0', p_strDataType)

	def FixCellValue(self, p_strValue, p_strDataType) :
		if not xConstantData.MYSQL_DATA_DEFINITIONS[p_strDataType]['IS_NUMERIC'] :
			return p_strValue

		if not xExportHelper.IsNumeric(p_strValue) :
			return p_strValue # TODO::

		if xConstantData.MYSQL_DATA_DEFINITIONS[p_strDataType]['IS_INTEGER'] :
			if xExportHelper.IsInteger(p_strValue) :
				return p_strValue
			else :
				return p_strValue[0:p_strValue.find('.')]

		return p_strValue
