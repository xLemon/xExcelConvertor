#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import codecs
import os
import sys
import traceback

class xFileUtility :
	@staticmethod
	def GetDirectoryFiles(p_strDirectoryPath, p_bRecursion) :
		
		setDirectoryFiles = set()
		lstDirectoryFiles = os.listdir(p_strDirectoryPath)

		for strFileName in lstDirectoryFiles :
			strFilePath = os.path.join(p_strDirectoryPath, strFileName)
			if os.path.isdir(strFilePath) :
				if p_bRecursion :
					setDirectoryFiles |= xFileUtility.GetDirectoryFiles(strFilePath, p_bRecursion)
			else :
				setDirectoryFiles.add(strFilePath)

		return setDirectoryFiles

	@staticmethod
	def IsFileOrDirectoryExist(p_strPath) :
		if not p_strPath is None :
			return os.path.exists(p_strPath)
		return False

	@staticmethod
	def DeleteFile(p_strFilePath) :
		if os.path.isfile(p_strFilePath) :
			os.remove(p_strFilePath)
			return True
		return False

	@staticmethod
	def CreateDirectory(p_strDirectoryPath) :
		if not p_strDirectoryPath is None :
			os.makedirs(p_strDirectoryPath)
			return True
		return False

	@staticmethod
	def GetFileSuffixByName(p_strFileName) :
		strFileSuffix = ''

		if p_strFileName is None :
			return strFileSuffix

		lstFileNameParts = p_strFileName.split(".")

		return lstFileNameParts[1]

	@staticmethod
	def GetFileNameFromPath(p_strFilePath, p_bWithoutSuffix = False) :
		strFileName = ''

		if p_strFilePath is None :
			return strFileName

		lstFilePathParts = p_strFilePath.split(os.sep)

		strFileName = lstFilePathParts[-1]

		if p_bWithoutSuffix :
			lstFileNameParts = strFileName.split(".")
			strFileName = lstFileNameParts[0]

		return strFileName

	@staticmethod
	def WriteDataToFile(p_strFilePath, p_strMode, p_strData) :
		# "a+": read, write, append
		# "w" : clear before, then write
		cFile = codecs.open(p_strFilePath, p_strMode)

		if p_strMode == "a+" :
			cFile.seek(0, os.SEEK_END)

		cFile.write(p_strData)
		cFile.flush()

		cFile.close()

		return True
