
mish = "KingsHorses.Chernarus_Summer"

try:
    from local_settings import *
except ImportError:
    pass

###############################################################################
# Create a file in this folder called local_settings.py and paste the following
# into it.  Change the path so that it points to your A3 profile folder.
#
# profile_folder = r'C:\Users\sux\Documents\Arma 3 - Other Profiles\Moore'
#
# Make sure to uncomment the line as well. duh
###############################################################################

missions_folder = profile_folder + r'\missions'
mpmissions_folder = profile_folder + r'\mpmissions'
