import sys, os
import shutil
import subprocess

arg=''
if len(sys.argv) > 1:
	arg = sys.argv[1]

def run(script):
	subprocess.call("python %s.py" % script)

def make_loads():
	wd = os.getcwd()
	os.chdir(os.path.join(wd, 'loads'))
	for x in ['cdf_2009', 'marines_2009']:
		run(x)
	sys.path.pop(0)
	os.chdir(wd)

def make_core():
	shutil.copy2("KingsHorses_core.Chernarus_Summer/mission.sqm", "./KingsHorses.Chernarus_Summer/")

if arg == 'core':
	make_core()
elif arg == '3d':
	run("make_3d")
elif arg == 'slots':
	run("make_slots")
elif arg == 'loads':
	make_loads()
else:
	make_core()
	make_loads()
	run("make_3d")
	run("make_slots")

