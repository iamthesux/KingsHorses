import os
import inspect
import importlib
import settings as cfg

os.chdir(os.path.join(cfg.mish, 'loads'))

for grp in ['cdf_2009', 'marines_2009', 'det5_2009', 'det5_crates', 'soar_2009']:
	lib = importlib.import_module('loads.' + grp)
	for name, obj in inspect.getmembers(lib):
		if inspect.isclass(obj) and 'NoWrite' not in obj.__dict__:
			obj().write()
