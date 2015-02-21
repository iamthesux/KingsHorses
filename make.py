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
	shutil.copy2("KingsHorses_core.Chernarus_Summer/mission.sqm", "./KingsHorses.Chernarus_Summer/")

def pull():
	shutil.copy2(os.path.join(cfg.mpmissions_folder, "KingsHorses_core.Chernarus_Summer/mission.sqm"), "./KingsHorses_core.Chernarus_Summer/")
def install():
	dest = os.path.join(cfg.mpmissions_folder, cfg.mish)
	if os.path.isdir(dest):
		shutil.rmtree(dest)
	shutil.copytree(cfg.mish, dest)


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
else:
	make_core()
	run("make_loads")
	run("make_crates")
	run("make_3d")
	run("make_slots")
	install()
