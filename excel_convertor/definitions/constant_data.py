#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

class xConstantData :
	EC_NAME = 'xExcelConvertor'

	SUPPORTED_EXCEL_FORMATS = ('xlsx', 'xlsm', 'xltx', 'xltm')

	MYSQL_DATA_DEFINITIONS              = { }
	MYSQL_DATA_DEFINITIONS['TINYINT']   = { 'NAME' : 'TINYINT',   'LENGTH' : 4,   'IS_STRING' : False, 'IS_NUMERIC' : True,  'IS_INTEGER' : True,  'IS_FLOAT' : False, 'COLLATE' : False }
	MYSQL_DATA_DEFINITIONS['SMALLINT']  = { 'NAME' : 'SMALLINT',  'LENGTH' : 6,   'IS_STRING' : False, 'IS_NUMERIC' : True,  'IS_INTEGER' : True,  'IS_FLOAT' : False, 'COLLATE' : False }
	MYSQL_DATA_DEFINITIONS['MEDIUMINT'] = { 'NAME' : 'MEDIUMINT', 'LENGTH' : 9,   'IS_STRING' : False, 'IS_NUMERIC' : True,  'IS_INTEGER' : True,  'IS_FLOAT' : False, 'COLLATE' : False }
	MYSQL_DATA_DEFINITIONS['INT']       = { 'NAME' : 'INT',       'LENGTH' : 11,  'IS_STRING' : False, 'IS_NUMERIC' : True,  'IS_INTEGER' : True,  'IS_FLOAT' : False, 'COLLATE' : False }
	MYSQL_DATA_DEFINITIONS['BIGINT']    = { 'NAME' : 'BIGINT',    'LENGTH' : 20,  'IS_STRING' : False, 'IS_NUMERIC' : True,  'IS_INTEGER' : True,  'IS_FLOAT' : False, 'COLLATE' : False }
	MYSQL_DATA_DEFINITIONS['CHAR']      = { 'NAME' : 'CHAR',      'LENGTH' : 40,  'IS_STRING' : True,  'IS_NUMERIC' : False, 'IS_INTEGER' : False, 'IS_FLOAT' : False, 'COLLATE' : True  }
	MYSQL_DATA_DEFINITIONS['VARCHAR']   = { 'NAME' : 'VARCHAR',   'LENGTH' : 255, 'IS_STRING' : True,  'IS_NUMERIC' : False, 'IS_INTEGER' : False, 'IS_FLOAT' : False, 'COLLATE' : True  }
	MYSQL_DATA_DEFINITIONS['TINYTEXT']  = { 'NAME' : 'TINYTEXT',  'LENGTH' : 0,   'IS_STRING' : True,  'IS_NUMERIC' : False, 'IS_INTEGER' : False, 'IS_FLOAT' : False, 'COLLATE' : True  }
	MYSQL_DATA_DEFINITIONS['TEXT']      = { 'NAME' : 'TEXT',      'LENGTH' : 0,   'IS_STRING' : True,  'IS_NUMERIC' : False, 'IS_INTEGER' : False, 'IS_FLOAT' : False, 'COLLATE' : True  }
	MYSQL_DATA_DEFINITIONS['LONGTEXT']  = { 'NAME' : 'LONGTEXT',  'LENGTH' : 0,   'IS_STRING' : True,  'IS_NUMERIC' : False, 'IS_INTEGER' : False, 'IS_FLOAT' : False, 'COLLATE' : True  }

	PATH_SEPARATOR  = '|'
	PATH_IDENTIFIER = '${SCRIPT_PATH}'

	EXPORT_IDENTIFIER_ALL   = 'all'
	EXPORT_IDENTIFIER_NONE  = 'none'
	EXPORT_IDENTIFIER_TRUE  = 'true'
	EXPORT_IDENTIFIER_FALSE = 'false'
	EXPORT_IDENTIFIER_YES   = 'yes'
	EXPORT_IDENTIFIER_NO    = 'no'

	DEFAULT_DATA_TABLE_ENGINE  = 'InnoDB'          # 默认数据表引擎
	DEFAULT_DATA_TABLE_CHARSET = 'utf8'            # 默认数据表字符集
	DEFAULT_DATA_TABLE_COLLATE = 'utf8_unicode_ci' # 默认数据表校对规则
	
	# ##################################################################################
	# INDEX_SHEET
	# ##################################################################################

	INDEX_SHEET_GLOBAL_COLUMN_DATABASE_NAME     = 1 # 数据库名
	INDEX_SHEET_GLOBAL_COLUMN_DATABASE_CHARSET  = 3 # 数据库字符集
	INDEX_SHEET_GLOBAL_COLUMN_DATABASE_COLLATE  = 5 # 数据库校对规则
	INDEX_SHEET_GLOBAL_COLUMN_DATA_TABLE_PREFIX = 7 # 数据表前缀

	INDEX_SHEET_DATA_COLUMN_NAME                   = 0 # 所在Sheet
	INDEX_SHEET_DATA_COLUMN_ALIAS                  = 1 # 资源名称
	INDEX_SHEET_DATA_COLUMN_TABLE_ENGINE           = 2 # 数据表引擎
	INDEX_SHEET_DATA_COLUMN_TABLE_CHARSET          = 3 # 数据表字符集
	INDEX_SHEET_DATA_COLUMN_TABLE_COLLATE          = 4 # 数据表校对规则
	INDEX_SHEET_DATA_COLUMN_ENABLE                 = 5 # 导出类型
	INDEX_SHEET_DATA_COLUMN_STRUCTURE_ONLY         = 6 # 仅结构（仅对sql有效）
	INDEX_SHEET_DATA_COLUMN_EXPORT_EMPTY_DATA_ITEM = 7 # 是否导出空数据项（默认 True）

	# ##################################################################################
	# DATA_SHEET
	# ##################################################################################

	DATA_SHEET_NAVIGATION_COLUMN_CATEGORY_LEVEL = 3 # 分类层级所在列

	DATA_SHEET_ROW_NAVIGATION                =  1 # 导航，在此无具体用处
	DATA_SHEET_ROW_FIELD                     =  2 # 字段名
	DATA_SHEET_ROW_DATA_TYPE                 =  3 # 数据类型，导出SQL时使用
	DATA_SHEET_ROW_DATA_LENGTH               =  4 # 数据长度，导出SQL时使用
	DATA_SHEET_ROW_DEFAULT_VALUE             =  5 # 默认值
	DATA_SHEET_ROW_PRIMARY_KEY_IDENTIFIER    =  6 # 是否主键，导出SQL时使用
	DATA_SHEET_ROW_NULL_IDENTIFIER           =  7 # 是否非空，导出SQL时使用
	DATA_SHEET_ROW_AUTO_INCREMENT_IDENTIFIER =  8 # 是否自增，导出SQL时使用
	DATA_SHEET_ROW_UNSIGNED_IDENTIFIER       =  9 # 是否无符号，导出SQL时使用
	DATA_SHEET_ROW_UNIQUE_IDENTIFIER         = 10 # 是否唯一，导出SQL时使用
	DATA_SHEET_ROW_EXPORT_IDENTIFIER         = 11 # 导出类型标记
	DATA_SHEET_ROW_LANGUAGE_CODE             = 12 # 语言代码
	DATA_SHEET_ROW_COMMENT                   = 13 # 注释

	DATA_SHEET_ROW_MIN = DATA_SHEET_ROW_FIELD
	DATA_SHEET_ROW_MAX = DATA_SHEET_ROW_COMMENT
