/**
 * Passe la variable R3F_LOG_joueur_deplace_objet à objNull pour informer le script "deplacer" d'arrêter de déplacer l'objet
 */

if (R3F_LOG_mutex_local_verrou) then
{
	hintC STR_R3F_LOG_mutex_action_en_cours;
}
else
{
	R3F_LOG_mutex_local_verrou = true;
	[kh_alive_required,"updateObject",[R3F_LOG_joueur_deplace_objet]] call ALIVE_fnc_logistics;
	R3F_LOG_joueur_deplace_objet = objNull;
	sleep 0.25;
	
	R3F_LOG_mutex_local_verrou = false;
};