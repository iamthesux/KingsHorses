from p4a.loadout import LoadOut

class Base(LoadOut):
	class NoWrite: pass
	def __init__(self):
		super(Base, self).__init__()
		self.remove('all')
		self.clear('all')

	items = [
		'ItemGPS',
		'ItemMap',
		'ItemCompass',
		'tf_microdagr',
	]
	
	class Uniform:
		items = [
			['cw_item_notepad', 1],
			['AGM_MapTools', 1],
			['cse_bandage_basic', 5],
			['cse_bandageElastic', 3],
			['cse_packing_bandage', 3],
			['cse_quikclot', 3],
			['cse_tourniquet', 4],
		]

MedicSupplies = [
	['cse_bandage_basic', 16],
	['cse_packing_bandage', 16],
	['cse_tourniquet', 8],
	['cse_morphine', 4],
	['cse_epinephrine', 4],
	['cse_atropine', 4],
	['cse_saline_iv_250', 4],
	['cse_quikclot', 16],
	['cse_surgical_kit', 1],
	['cse_personal_aid_kit', 1],
]