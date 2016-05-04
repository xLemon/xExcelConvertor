#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os

from utilities.file_utility import xFileUtility

class xProcessorManager(object) :
	@staticmethod
	def GetProcessorPath() :
		return os.path.join(os.path.abspath('.'), 'processors')

	@staticmethod
	def IsProcessorExist(p_strExportType) :
		if len(p_strExportType) <= 0 :
			return False

		strProcessorFilePath = os.path.join(xProcessorManager.GetProcessorPath(), 'processor_{0}.py'.format(p_strExportType.lower()))

		return xFileUtility.IsFileOrDirectoryExist(strProcessorFilePath)
	
	@staticmethod
	def GetProcessorInstance(p_strType) :
		cProcessor = None

		strProcessorPath = 'processors.processor_{0}'.format(p_strType.lower())

		try :
			cProcessor = __import__(strProcessorPath, None, None, ('xProcessor{0}'.format(p_strType.lower().capitalize())))
		except Exception as cException :
			raise Exception('Processor : "{0}" Import Fail!'.format(strProcessorPath))
		
		cProcessorClass = getattr(cProcessor, 'xProcessor{0}'.format(p_strType.lower().capitalize()))

		return cProcessorClass()
