import os
from loads.cdf_2009 import *
from loads.marines_2009 import *

os.chdir(os.path.join('KingsHorses.Chernarus_Summer', 'loads'))

cdf_sl().write()
cdf_crew().write()
cdf_asl_gunner().write()
cdf_rifleman().write()
cdf_grenadier().write()
cdf_mg().write()
cdf_medic().write()

marine_sl().write()
marine_tl().write()
marine_rifleman().write()
marine_ar().write()
marine_aar().write()
