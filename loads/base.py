from p4a.loadout import LoadOut

class Base(LoadOut):
	class NoWrite: pass
	def __init__(self):
		super(Base, self).__init__()
		self.remove('all')
		self.clear('all')

	items = [
		'ItemWatch',
		'ItemMap',
		'ItemCompass',
		'NVGoggles_BLUFOR',
	]
	
	class Uniform:
		items = [
			['AGM_MapTools', 1],
			['AGM_EarBuds', 1],
			['cse_bandage_basic', 5],
			['cse_bandageElastic', 3],
			['cse_packing_bandage', 3],
			['cse_quikclot', 3],
			['cse_tourniquet', 1],
			['cse_nasopharyngeal_tube', 1],
		]
