#!/usr/bin/env python
################################################################################
#
# cs_MeshLab_command_class.py
# Description: The class used for creating cs_meshlab
# Usage:
# PolygonCruncher - Shows the form
# Author: Chris Sprance Entrada Interactive
#
################################################################################
import lx
import lxu.command

import meshlab


class cs_MeshLab(lxu.command.BasicCommand):
	def __init__(self):
		print 'Running cs_meshlab'
		lxu.command.BasicCommand.__init__(self)
	
	def cmd_Flags(self):
		return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO
	
	def basic_Enable(self, msg):
		return True
	
	def cmd_Interact(self):
		pass
	
	def basic_Execute(self, msg, flags):
		reload(meshlab)
		meshlab.execute()
	
	def cmd_Query(self, index, vaQuery):
		lx.notimpl()


lx.bless(cs_MeshLab, "cs_MeshLab")
