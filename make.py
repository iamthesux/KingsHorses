import sys, os, shutil
import shutil
import subprocess

import settings as cfg

from p4a.formats.rap import Klass
from p4a.formats.rap.text import Reader, Writer

arg=''
if len(sys.argv) > 1:
	arg = sys.argv[1]

def run(script):
	subprocess.call("python %s.py" % script)

def make_core():
	shutil.copy2(os.path.join(cfg.mish_core, "mission.sqm"), cfg.mish)

def pull():
	shutil.copy2(os.path.join(cfg.mpmissions_folder, cfg.mish_core, "mission.sqm"), cfg.mish_core)
	shutil.copy2(os.path.join(cfg.missions_folder, cfg.mish_3d, "mission.biedi"), cfg.mish_3d)
def install():
	dest = os.path.join(cfg.mpmissions_folder, cfg.mish)
	#TODO make this check safer
	if os.path.isdir(dest) and dest != cfg.mpmissions_folder:
		shutil.rmtree(dest)
	shutil.copytree(cfg.mish, dest)

def test():
	run("make_loads")
	dest = os.path.join(cfg.mpmissions_folder, 'test.Chernarus_Summer')
	dest2 = os.path.join(cfg.missions_folder, 'test.VR')

	#print dest
	#TODO make this check safer
	if os.path.isdir(dest) and dest != 'test.Chernarus_Summer':
		shutil.rmtree(dest)
	shutil.copytree('test.Chernarus_Summer', dest)
	shutil.copytree(os.path.join(cfg.mish, 'loads'), os.path.join(dest, 'loads'))
	if os.path.isdir(dest2) and dest2 != 'test.VR':
		shutil.rmtree(dest2)
	shutil.copytree(os.path.join(cfg.mish, 'loads'), os.path.join(dest2, 'loads'))
	shutil.copytree(os.path.join(cfg.mish, 'sux_load'), os.path.join(dest, 'sux_load'))
# def debug():
	# mish = Reader('KingsHorses.Chernarus_Summer/mission.sqm').read()
	# cs = mish('Mission')('Groups').filter(lambda x: x('Vehicles')('Item0')('args')('Item0') == "LOGIC")
	# print len(cs)
	
if arg == 'core':
	make_core()
elif arg == '3d':
	run("make_3d")
elif arg == 'slots':
	run("make_slots")
elif arg == 'crates':
	run("make_crates")
elif arg == 'loads':
	run("make_loads")
elif arg == 'install':
	install()
elif arg == 'pull':
	pull()
elif arg == 'test':
	test()
else:
	make_core()
	run("make_loads")
	run("make_crates")
	run("make_3d")
	run("make_slots")
	install()
