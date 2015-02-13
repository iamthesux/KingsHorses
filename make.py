import sys, os, shutil
import shutil
import subprocess

import settings as cfg

arg=''
if len(sys.argv) > 1:
	arg = sys.argv[1]

def run(script):
	subprocess.call("python %s.py" % script)

def make_core():
	shutil.copy2("KingsHorses_core.Chernarus_Summer/mission.sqm", "./KingsHorses.Chernarus_Summer/")

def install():
	dest = os.path.join(cfg.mpmissions_folder, cfg.mish)
	if os.path.isdir(dest):
		shutil.rmtree(dest)
	shutil.copytree(cfg.mish, dest)

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
else:
	make_core()
	run("make_loads")
	run("make_crates")
	run("make_3d")
	run("make_slots")
	install()
