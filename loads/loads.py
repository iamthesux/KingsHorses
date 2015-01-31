from p4a.loadout import LoadOut, Writer

from base import *
from pubs import *
from onesix import *

class sasr_base(ClassyNshit):
	def __init__(self):
		super(sasr_base, self).__init__()
	
	headgear = 'H_SOC_MARITIME_MCM'
	
	class Primary:
		weapon = 'RHARD_M4DDRD_B_F'
		optic = 'CUP_optic_ACOG'
		supressor = 'muzzle_MK18D_L'
		rail = 'PEQ15_A3_Top'
		mags = [['30Rnd_556x45_Stanag', 30]]

	class Uniform(ClassyNshit.Uniform):
		type = 'LOP_U_ISIS_Fatigue_05'

	class Vest:
		type = 'bink_vest_4'
		items = [
			['30Rnd_556x45_Stanag', 5],
		]
	class Backpack:
		type = 'B_Kitbag_mcamo'
		items = [
			['30Rnd_556x45_Stanag', 5],
		]

#wrtr = Writer('loads.sqf')
#wrtr.write(sasr_base())
#wrtr.write(one6_command())

one6_command().write()

class SOARPilot(ClassyNshit):
	name = 'soar_pilot'
	headgear = 'U_B_HeliPilotCoveralls'
	binoc = 'Binocular'
	class Primary:
		weapon = 'CUP_arifle_M4A1_black'
		optic = 'CUP_optic_CompM4'
		rail = 'acc_pointer_IR'
		mags = [['30Rnd_556x45_Stanag', 30]]

	class Uniform(ClassyNshit.Uniform):
		type = 'U_B_HeliPilotCoveralls'

	class Vest:
		type = 'V_TacVest_blk'
		items = [
			['30Rnd_556x45_Stanag', 5],
		]
	class Backpack:
		type = 'tf_rt1523g_green'
		items = [
			['30Rnd_556x45_Stanag', 5],
		]

class MCRU(Base):
	name = 'mcru_base'
	headgear = 'U_B_HeliPilotCoveralls'
	class Uniform(ClassyNshit.Uniform):
		type = 'U_B_HeliPilotCoveralls'

		
