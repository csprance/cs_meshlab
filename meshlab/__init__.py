import os
import subprocess

import lx

dir_path = os.path.dirname(os.path.realpath(__file__))
TEMP_FBX_PATH_INPUT = os.path.join(dir_path, 'temp_lod_file_in.fbx')
TEMP_FBX_PATH_OUTPUT = os.path.join(dir_path, 'temp_lod_file_out.fbx')


def get_user_values():
	return {
		"optimizationRatio": lx.eval('user.value pc_optimizationRatio ?'),
		"progressiveRatio": lx.eval('user.value pc_progressiveRatio ?'),
		"borderMode": lx.eval('user.value pc_borderMode ?'),
		"cornerMode": lx.eval('user.value pc_cornerMode ?'),
		"keepMaterialBoundaries": lx.eval('user.value pc_keepMaterialBoundaries ?'),
		"materialBoundaryMode": lx.eval('user.value pc_materialBoundaryMode ?'),
		"keepTextures": lx.eval('user.value pc_keepTextures ?'),
		"uvMode": lx.eval('user.value pc_uvMode ?'),
		"uvTolerance": lx.eval('user.value pc_uvTolerance ?'),
		"keepVertexColors": lx.eval('user.value pc_keepVertexColors ?'),
		"vcMode": lx.eval('user.value pc_vcMode ?'),
		"vcTolerance": lx.eval('user.value pc_vcTolerance ?'),
		"keepNormals": lx.eval('user.value pc_keepNormals ?'),
		"normalMode": lx.eval('user.value pc_normalMode ?'),
		"thresholdAngle": lx.eval('user.value pc_thresholdAngle ?'),
		"favorCompactFaces": lx.eval('user.value pc_favorCompactFaces ?'),
		"preventFlippedNormals": lx.eval('user.value pc_preventFlippedNormals ?'),
		"stopAutomatically": lx.eval('user.value pc_stopAutomatically ?'),
		"lockVertexPosition": lx.eval('user.value pc_lockVertexPosition ?'),
		"appPath": os.path.normpath(lx.eval('user.value pc_appPath ?'))
	}


def start_meshlabserver_with_flags(app_path, flags):
	"""Start Polygon Cruncher with a set of flags waits until it exits and report any failures"""
	try:
		process = subprocess.Popen(app_path + ' ' + flags)
		process.wait()
	except Exception, e:
		lx.out("meshlabserver application launch failed check app path and try again!")
		print e


def format_user_values_to_flags(user_values):
	flags = [
		'-license-serial bd8b0a3db967a3c280'
		'-i ' + TEMP_FBX_PATH_INPUT,
		'-levelnbr 1',
		'-level1 ' + str(int(user_values['optimizationRatio'])),
		# '-progressive ' + str(int(user_values['progressiveRatio'])),  # not sure what this is
		'-' + user_values['borderMode'],
		'-' + user_values['cornerMode'],
		'-' + user_values['materialBoundaryMode'],
		# uv
		'-' + user_values['uvMode'],
		'-uv-tolerance ' + str(user_values['uvTolerance']),
		# vertex colors
		'-' + user_values['vcMode'],
		'-vc-tolerance ' + str(user_values['vcTolerance']),
		# normals
		'-' + user_values['normalMode'],
		'-normal-tolerance ' + str(user_values['thresholdAngle']),
		# output
		'-ouput-nameprefix "_out"'
	]
	print ' '.join(flags)
	return ' '.join(flags)


def set_fbx_export_preset_values():
	"""set the fbx presets and export the fbx temp file"""
	print 'setting scripts fbx preset values'
	lx.eval('user.value sceneio.fbx.save.exportToASCII true')
	lx.eval('user.value sceneio.fbx.save.exportType FBXExportSelection')
	lx.eval('user.value sceneio.fbx.save.animationOnly false')
	lx.eval('user.value sceneio.fbx.save.geometry true')
	lx.eval('user.value sceneio.fbx.save.materials true')
	lx.eval('user.value sceneio.fbx.save.cameras false')
	lx.eval('user.value sceneio.fbx.save.lights false')
	lx.eval('user.value sceneio.fbx.save.animation false')
	lx.eval('user.value sceneio.fbx.save.surfaceRefining FBXExportPolygons')
	lx.eval('user.value sceneio.fbx.save.polygonParts true')
	lx.eval('user.value sceneio.fbx.save.selectionSets false')
	lx.eval('user.value sceneio.fbx.save.smoothingGroups true')
	lx.eval('user.value sceneio.fbx.save.morphMaps false')
	lx.eval('user.value sceneio.fbx.save.tangentsBitangents true')
	lx.eval('user.value sceneio.fbx.save.units default')
	lx.eval('user.value sceneio.fbx.save.scale 1.0')
	lx.eval('user.value sceneio.fbx.save.exportRgbaAsDiffCol false')
	lx.eval('user.value sceneio.fbx.save.pbrMaterials false')
	lx.eval('user.value sceneio.fbx.save.sampleAnimation false')
	lx.eval('user.value sceneio.fbx.save.sampleAnimFpsMultiplier FBXAnimSampleRate_x1')
	lx.eval('user.value sceneio.fbx.save.exportActionType FBXExportNoActions')


def store_fbx_preset_user_values():
	"""store the users current FBX preset values"""
	print 'storing user fbx preset values'
	return {
		"exportToASCII": lx.eval('user.value sceneio.fbx.save.exportToASCII ?'),
		"exportType": lx.eval('user.value sceneio.fbx.save.exportType ?'),
		"animationOnly": lx.eval('user.value sceneio.fbx.save.animationOnly ?'),
		"geometry": lx.eval('user.value sceneio.fbx.save.geometry ?'),
		"materials": lx.eval('user.value sceneio.fbx.save.materials ?'),
		"cameras": lx.eval('user.value sceneio.fbx.save.cameras ?'),
		"lights": lx.eval('user.value sceneio.fbx.save.lights ?'),
		"animation": lx.eval('user.value sceneio.fbx.save.animation ?'),
		"surfaceRefining": lx.eval('user.value sceneio.fbx.save.surfaceRefining ?'),
		"polygonParts": lx.eval('user.value sceneio.fbx.save.polygonParts ?'),
		"selectionSets": lx.eval('user.value sceneio.fbx.save.selectionSets ?'),
		"smoothingGroups": lx.eval('user.value sceneio.fbx.save.smoothingGroups ?'),
		"morphMaps": lx.eval('user.value sceneio.fbx.save.morphMaps ?'),
		"tangentsBitangents": lx.eval('user.value sceneio.fbx.save.tangentsBitangents ?'),
		"units": lx.eval('user.value sceneio.fbx.save.units ?'),
		"scale": lx.eval('user.value sceneio.fbx.save.scale ?'),
		"exportRgbaAsDiffCol": lx.eval('user.value sceneio.fbx.save.exportRgbaAsDiffCol ?'),
		"pbrMaterials": lx.eval('user.value sceneio.fbx.save.pbrMaterials ?'),
		"sampleAnimation": lx.eval('user.value sceneio.fbx.save.sampleAnimation ?'),
		"sampleAnimFpsMultiplier": lx.eval('user.value sceneio.fbx.save.sampleAnimFpsMultiplier ?'),
		"exportActionType": lx.eval('user.value sceneio.fbx.save.exportActionType ?'),
	}


def export_mesh():
	# store the export presets
	fbx_values = store_fbx_preset_user_values()
	
	# set the export presets
	set_fbx_export_preset_values()
	
	# export the mesh
	lx.eval('game.export exportPath:' + TEMP_FBX_PATH_INPUT)
	print 'exporting mesh to temp file at' + TEMP_FBX_PATH_INPUT
	
	# restore the users FBX preset values
	print 'resstoring user fbx preset values'
	for key, val in fbx_values.items():
		lx.eval('user.value sceneio.fbx.save.' + key + ' ' + str(val))


def import_lod_mesh(name):
	print 'importing FBX as: ' + str(int(name))


def execute():
	# export the current mesh with the correct FBX presets and path
	export_mesh()
	
	# get user values from the form UI
	user_values = get_user_values()
	
	# convert user values to flags
	flags = format_user_values_to_flags(user_values)
	
	# run meshlab using the user values
	start_meshlabserver_with_flags(user_values['appPath'], flags)
	
	# reimport the mesh as mesh_name_lod_N
	import_lod_mesh(user_values['optimizationRatio'])
