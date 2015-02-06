from p4a.loadout import Crate
 
class cdfsf_explosives(Crate):
        title = 'CDFSF Explosives'
        magazines = [
               
                ['rhs_mag_rgd5', 100],
                ['rhs_mag_rdg2_white', 100],
                ['rhs_mag_rdg2_black', 100],
                ['rhs_mag_nspn_yellow', 100],
                ['rhs_mag_nspn_red', 100],
                ['rhs_mag_nspn_green', 100],
                ['rhs_mine_tm62m', 100],

                ['DemoCharge_Remote_Mag', 100],
                ['rhs_VOG25', 100],
                ['rhs_VOG25p', 100],
                ['rhs_vg40op_white', 100],
                ['rhs_vg40op_green', 100],
                ['rhs_vg40op_red', 100],
                ['rhs_GRD40_white', 100],
                ['rhs_GRD40_green', 100],
                ['rhs_GRD40_red', 100],
        ]
 
class cdfsf_launchers(Crate):
        title = 'CDFSF Launchers and Warheads'
        weapons = [
                ['rhs_weap_rpg7', 10],
                ['rhs_weap_rpg26', 100],
                ['rhs_weap_rshg2', 50],
        ]
        magazines = [
                ['rhs_rpg7_PG7VL_mag', 100],
                ['rhs_rpg7_PG7VR_mag', 100],
                ['rhs_rpg7_OG7V_mag', 100],
        ]
 
class cdfsf_weapons(Crate):
        title = 'CDFSF Rifles and Ammo'
        weapons = [
                ['rhs_weap_ak74m', 5],
                ['rhs_weap_ak74m_folded', 5],
                ['rhs_weap_pkp', 5],
                ['rhs_weap_svdp', 3],
                ['rhs_weap_ak74m_camo', 5],
                ['rhs_weap_ak74m_gp25', 5],
        ]
        magazines = [
                ['rhs_30Rnd_545x39_AK', 100],
                ['rhs_30Rnd_545x39_AK_green', 100],
                ['rhs_100Rnd_762x54mmR', 100],
                ['RH_8Rnd_762_tt33', 85],
                ['rhs_10Rnd_762x54mmR_7N1', 100],
        ]

class cdfsf_radios(Crate):
        title = 'CDFSF Radios'
        items = [
               
                ['tf_rf7800str_1', 75],
                ['tf_anprc152_2', 45],
                ['tf_anprc148jem', 65],

        ]
