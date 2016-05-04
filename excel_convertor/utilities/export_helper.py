#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

from definitions.constant_data import xConstantData

class xExportHelper :
	@staticmethod
	def IsDataSheetColumnLanguageAvailable(p_strDataSheetColumnLanguage, p_strExportType, p_mapExportConfigs) :
		# 指定导出的语言类型没填的话当成all处理

		if p_strDataSheetColumnLanguage is None or len(p_strDataSheetColumnLanguage) <= 0 :
			return True

		strDataSheetColumnLanguage = p_strDataSheetColumnLanguage.lower()
		strExportLanguage          = p_mapExportConfigs['EXPORTS'][p_strExportType]['EXPORT_LANGUAGE'].lower()

		# 如果导出配置中配置的是要导出所有类型的语言，那么无论数据表中配置的是什么语言，都导出

		if 0 == cmp(strExportLanguage, xConstantData.EXPORT_IDENTIFIER_ALL) :
			return True

		# 如果导出配置中配置的是要导出特定类型的语言，那么只导出匹配的语言

		if 0 == cmp(strExportLanguage, strDataSheetColumnLanguage) :
			return True
		
		# 到这里，我也不知道为神马失败了- -#

		return False
	
	@staticmethod
	def IsDataSheetColumnExportTypeAvailable(p_strDataSheetColumnExportType, p_strExportType, p_mapExportConfigs) :
		# 指定导出的格式类型没填的话当成all处理

		if p_strDataSheetColumnExportType is None or len(p_strDataSheetColumnExportType) <= 0 :
			return True

		strDataSheetColumnExportType = p_strDataSheetColumnExportType.lower()

		if 0 == cmp(strDataSheetColumnExportType, xConstantData.EXPORT_IDENTIFIER_ALL) :
			return True

		if 0 != cmp(strDataSheetColumnExportType, xConstantData.EXPORT_IDENTIFIER_NONE) :
			return p_strExportType.lower() in strDataSheetColumnExportType.split(',')

		# 这里是none的话，就是没有要导出的了

		return False
	
	@staticmethod
	def GetFieldNameAsI18N(p_strFieldName, p_strLanguageCode, p_strExportType, p_mapExportConfigs) :
		# 全局导出配置中配置的语言类型不为all，那么这里仅返回原始字段名

		if 0 != cmp(p_mapExportConfigs['EXPORTS'][p_strExportType]['EXPORT_LANGUAGE'].lower(), xConstantData.EXPORT_IDENTIFIER_ALL) :
			return p_strFieldName

		# 如果导出配置中没有配置要导出的语言，或导出配置中配置的导出语言为all，那么直接返回原始字段名

		if p_strLanguageCode is None or 0 == cmp(p_strLanguageCode, '') or 0 == cmp(p_strLanguageCode, xConstantData.EXPORT_IDENTIFIER_ALL) :
			return p_strFieldName

		# 否则返回的格式为 : 原始字段名_语言代码

		return '{0}_{1}'.format(p_strFieldName, p_strLanguageCode)
