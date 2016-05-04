#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

class xExcelHelper :
	@staticmethod
	def ConvertColumnNameToColumnIndex(p_strColumnName) :
		if type(p_strColumnName) is not str :
			return p_strColumnName

		nColumn = 0
		nPower  = 1
		
		print len(p_strColumnName)
		
		for i in xrange(len(p_strColumnName) - 1, -1, -1) :
			szChar = p_strColumnName[i]
			nColumn += (ord(szChar) - ord('A') +  1 ) * nPower
			nPower  *= 26
		
		return nColumn - 1

	@staticmethod
	def ConvertColumnIndexToColumnName(p_nColumnIndex) :
		if type(p_nColumnIndex) != int :
			return p_nColumnIndex

		if p_nColumnIndex > 25 :
			szChar1 = chr(p_nColumnIndex % 26 + 65)
			szChar2 = chr(p_nColumnIndex / 26 + 64)
			return szChar2 + szChar1
		else :
			return chr(p_nColumnIndex % 26 + 65)
