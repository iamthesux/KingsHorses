import os
import inspect
import importlib

os.chdir(os.path.join('KingsHorses.Chernarus_Summer', 'loads'))

for grp in ['cdf_2009', 'marines_2009']:
	lib = importlib.import_module('loads.' + grp)
	for name, obj in inspect.getmembers(lib):
		if inspect.isclass(obj) and 'NoWrite' not in obj.__dict__:
			obj().write()
