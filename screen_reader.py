# screen_reader.py
# Dictionary holding all translations for different languages
translations = {
    'English': {
    # system
        'system_on': "Power On.",
        'system_off': "Power Off.",
        'system_armed': "System armed.\nPlease enter the PIN or look at the webcam for Face ID.",
        'system_disarmed': "System disarmed.\nAccess granted.",
    # face ID
        'user_recognised': "You are recognised.\nPlease enter the PIN to disarm the system.",
        'user_not_recognised': "You are not recognised.\nPlease enter the PIN to disarm the system.",
    # pin
        'pin_correct': "You entered the PIN correctly.",
        'pin_incorrect': "PIN is incorrect. Try again.",
    # menu 
        'menu': "Menu: Please select an option.\n The options are Arm and Schedule Activation, Settings, Languages, Change Password, or Add Face ID.",
    # menu arm
        'menu_arm_and_schedule_activation': "You have selected Arm and Schedule Activation. \nSelect Arm or Schedule Activation to proceed and select back to return to the menu.",
        'menu_arm': "You have selected Arm. Press the button to arm the system.\nOr select close to go back to the menu.",
        'menu_schedule_activation': "You have selected Schedule Activation.\nEnter a time between 1 and 5 minutes to schedule the activation.\nOr select close to go back to the menu.",
    # menu settings
        'menu_settings_screen_reader': "You have selected Screen Reader.\nPlease press the button to enable the screen reader. Or select close to go back to the menu.",
        'menu_settings_record_log': "You have selected Record Log.\nPlease scroll to see information about previous alarm activations\n Click the video button to view the recording.",
        'menu_settings': "You have selected Settings. Please select an option to proceed or select back to return to the menu. The options are Troubleshoot and Maintenance, Record Log, Screen Reader, Font Size.",
        'menu_settings_troubleshoot_and_maintenance': "You have selected Troubleshoot and Maintenance.\nSelect Troubleshoot to perform a quick scan, select Maintenance to see contact information for your nearest branch,\nor select close to go back to the menu.",
        'menu_settings_troubleshoot': "You have selected Troubleshoot.\nPlease wait while we perform a quick scan, this usually takes around 5 minutes. \nSelect cancel to stop the scan.",
        'menu_settings_maintenance': "You have selected Maintenance.\nThese are the following details for your closest branch.\nSelect back to return to Settings.",
        'menu_font_size': "You have selected Font Size.This is the current font size.\n\nPlease enter a number between 16 to 24 to change the font size.\nSelect Enter to proceed and Exit to return to Settings.",
    # Menu Change Password/ add face id
        'menu_edit_face_id': "You have selected Edit Face ID.\nSelect proceed to carry on and select exit to return to the menu.",
        'menu_change_password': "You have selected Change Password.\nSelect proceed to carry on and select exit to return to the menu.",
        'menu_after_check_change_password': "Enter the new PIN using the keys on the keypad.",
        'menu_check_new_password': "This is the new PIN you entered.\n\nPlease confirm that you want to proceed or enter a different PIN.",
        'menu_check_efi': "You have selected Edit FaceID.\nSelect proceed to carry on and select exit to return to the menu.",
    # menu languages
        'menu_languages': "You have selected Languages.\nSelect English, Welsh, or Punjabi.",
    # alarm:
        'alarm_active': "Alarm activated.",
        'alarm_disactive': "Alarm deactivated.",
        'record': "Recording Started.",
        'security': "Security Notified.",
    },

    'Welsh': {
    # system
        'system_on': "Pŵer Ymlaen.",
        'system_off': "Pŵer Ffwrdd.",
        'system_armed': "System wedi'i arfogi.\nRhowch y PIN neu edrychwch ar y gwe-gamera am ID Wyneb.",
        'system_disarmed': "System wedi'i ddadranu.\nMynediad wedi'i ganiatáu.",
    # face ID
        'user_recognised': "Rydych chi'n cael eich adnabod.\nRhowch y PIN i ddadrfogi'r system.",
        'user_not_recognised': "Nid ydych chi'n cael eich adnabod.\nRhowch y PIN i ddadrfogi'r system.",
    # pin
        'pin_correct': "Rydych wedi nodi'r PIN yn gywir.",
        'pin_incorrect': "Mae'r PIN yn anghywir. Rhowch gynnig arall.",
    # menu 
        'menu': "Dewislen: Dewiswch opsiwn.\n Y opsiynau yw Arfogi ac Activasiwn Amserlen, Gosodiadau, Ieithoedd, Newid Cyfrinair, neu Ychwanegu ID Wyneb.",
    # menu arm
        'menu_arm_and_schedule_activation': "Rydych wedi dewis Arfogi ac Activasiwn Amserlen. Dewiswch Arfogi neu Activasiwn Amserlen i fynd ymlaen a dewiswch yn ôl i fynd yn ôl i'r ddewislen.",
        'menu_arm': "Rydych wedi dewis Arfogi. Pwyswch y botwm i arfogi'r system.\nNeu dewiswch cau i fynd yn ôl i'r ddewislen.",
        'menu_schedule_activation': "Rydych wedi dewis Activasiwn Amserlen.\nRhowch amser rhwng 1 a 5 munud i drefnu'r gweithrediad.\nNeu dewiswch cau i fynd yn ôl i'r ddewislen.",
    # menu settings
        'menu_settings_screen_reader': "Rydych wedi dewis Darllenwr Sgrin.\nPwyswch y botwm i alluogi'r darllenwr sgrin. Neu dewiswch cau i fynd yn ôl i'r ddewislen.",
        'menu_settings_record_log': "Rydych wedi dewis Logio Record.\nSgroliwch i weld gwybodaeth am ymyriadau larwm blaenorol.\nCliciwch ar y botwm fideo i weld y recordiad.",
        'menu_settings': "Rydych wedi dewis Gosodiadau. Dewiswch opsiwn i fynd ymlaen neu ddewiswch yn ôl i fynd yn ôl i'r ddewislen. Mae'r opsiynau'n cynnwys Ymyrraeth a Chynnal, Logio Record, Darllenwr Sgrin, Maint Ffont.",
        'menu_settings_troubleshoot_and_maintenance': "Rydych wedi dewis Ymyrraeth a Chynnal.\nDewiswch Ymyrraeth i gynnal sgan cyflym, dewiswch Gynnal i weld gwybodaeth gyswllt ar gyfer eich cangen agosaf,\nneu dewiswch cau i fynd yn ôl i'r ddewislen.",
        'menu_settings_troubleshoot': "Rydych wedi dewis Ymyrraeth.\nArhoswch tra byddwn yn cynnal sgan cyflym, mae hyn fel arfer yn cymryd tua 5 munud.\nDewiswch canslo i atal y sgan.",
        'menu_settings_maintenance': "Rydych wedi dewis Cynnal.\nDyma'r manylion ar gyfer eich cangen agosaf.\nDewiswch yn ôl i fynd yn ôl i Gosodiadau.",
        'menu_font_size': "Rydych wedi dewis Maint Ffont. Dyma faint y ffont presennol.\n\nRhowch rif rhwng 16 a 24 i newid maint y ffont.\nDewiswch Enter i fynd ymlaen a Chau i fynd yn ôl i Gosodiadau.",
    # Menu Change Password/ add face id
        'menu_edit_face_id': "Rydych wedi dewis Golygu ID Wyneb.\nDewiswch bwrw ymlaen i fynd yn ôl a dewiswch allan i fynd yn ôl i'r ddewislen.",
        'menu_change_password': "Rydych wedi dewis Newid Cyfrinair.\nDewiswch bwrw ymlaen i fynd yn ôl a dewiswch allan i fynd yn ôl i'r ddewislen.",
        'menu_after_check_change_password': "Rhowch y PIN newydd gan ddefnyddio'r eiriau ar y bysellfwrdd.",
        'menu_check_new_password': "Dyma'r PIN newydd a nodwyd gennych.\nCadarnhewch eich bod am fynd ymlaen neu nodwch PIN gwahanol.",
        'menu_check_efi': "Rydych wedi dewis Golygu ID Wyneb.\nDewiswch bwrw ymlaen i fynd yn ôl a dewiswch allan i fynd yn ôl i'r ddewislen.",
    # menu languages
        'menu_languages': "Rydych wedi dewis Ieithoedd.\nDewiswch Saesneg, Cymraeg, neu Punjabi.",
    # alarm:
        'alarm_active': "Llais trydanol wedi'i gweithredu.",
        'alarm_disactive': "Llais trydanol wedi'i dadyrchu."
    },

    'Punjabi': {
    # system
        'system_on': "ਪਾਵਰ ਚਾਲੂ",
        'system_off': "ਪਾਵਰ ਬੰਦ",
        'system_armed': "ਸਿਸਟਮ ਅਸਲਾਹ.\nਪਿਨ ਦਰਜ ਕਰੋ ਜਾਂ ਚਿਹਰੇ ਦੀ ਪਛਾਣ ਲਈ ਵੈਬਕੈਮ ਵੇਖੋ।",
        'system_disarmed': "ਸਿਸਟਮ ਅਸਲਾਹ ਰਹਿਤ ਹੋ ਗਿਆ ਹੈ।\nਪਹੁੰਚ ਮਨਜ਼ੂਰ ਹੈ",
    # face id 
        'user_recognised': "ਤੁਸੀਂ ਪਛਾਣੇ ਗਏ ਹੋ।\nਸਿਸਟਮ ਨੂੰ ਅਨਲੌਕ ਕਰਨ ਲਈ ਪਿਨ ਦਰਜ ਕਰੋ।",
        'user_not_recognised': "ਤੁਹਾਨੂੰ ਪਛਾਣਿਆ ਨਹੀਂ ਗਿਆ ਹੈ।\nਸਿਸਟਮ ਨੂੰ ਅਨਲੌਕ ਕਰਨ ਲਈ ਪਿਨ ਦਰਜ ਕਰੋ।",
    # pin
        'pin_correct': "ਤੁਸੀਂ ਪਿਨ ਸਹੀ ਦਰਜ ਕੀਤਾ ਹੈ।",
        'pin_incorrect': "ਪਿਨ ਗਲਤ ਹੈ। ਮੁਆਫ ਕਰੋ।",
    # menu 
        'menu': "ਮੀਨੂ: ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ ਚੋਣ ਚੁਣੋ। ਚੋਣ ਅਰਮ ਕਰੋ ਅਤੇ ਸ਼ੈੱਡਿਊਲ ਕਾਰਜ, ਸੈਟਿੰਗਸ, ਭਾਸ਼ਾਵਾਂ, ਪਾਸਵਰਡ ਬਦਲੋ ਜਾਂ ਚਿਹਰਾ ID ਸ਼ਾਮਲ ਕਰੋ।",
    # menu arm
        'menu_arm_and_schedule_activation': "ਤੁਸੀਂ ਅਰਮ ਅਤੇ ਸ਼ੈੱਡਿਊਲ ਕਾਰਜ ਚੁਣਿਆ ਹੈ। ਅਰਮ ਜਾਂ ਸ਼ੈੱਡਿਊਲ ਕਰਨ ਲਈ ਅੱਗੇ ਬਢੋ ਅਤੇ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਪਿੱਛੇ ਚੁਣੋ।",
        'menu_arm': "ਤੁਸੀਂ ਅਰਮ ਚੁਣਿਆ ਹੈ। ਸਿਸਟਮ ਅਰਮ ਕਰਨ ਲਈ ਬਟਨ ਨੂੰ ਦਬਾਓ। ਜਾਂ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਬੰਦ ਕਰੋ।",
        'menu_schedule_activation': "ਤੁਸੀਂ ਸ਼ੈੱਡਿਊਲ ਕਾਰਜ ਚੁਣਿਆ ਹੈ। ਕਾਰਜ ਸ਼ੈੱਡਿਊਲ ਕਰਨ ਲਈ 1 ਅਤੇ 5 ਮਿੰਟ ਦਰਮਿਆਨ ਸਮਾਂ ਦਾਖਲ ਕਰੋ। ਜਾਂ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਬੰਦ ਕਰੋ।",
    # menu settings
        'menu_settings_screen_reader': "ਤੁਸੀਂ ਸਕ੍ਰੀਨ ਪੜ੍ਹਨ ਵਾਲਾ ਚੁਣਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਬਟਨ ਦਬਾਓ ਤਾਂ ਸਕ੍ਰੀਨ ਪੜ੍ਹਨ ਵਾਲੀ ਸਮੱਗਰੀ ਨੂੰ ਸਮਰੱਥ ਕਰੋ। ਜਾਂ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਬੰਦ ਕਰੋ।",
        'menu_settings_record_log': "ਤੁਸੀਂ ਰਿਕਾਰਡ ਲੌਗ ਚੁਣਿਆ ਹੈ। ਕ੍ਰਿਪਾ ਕਰਕੇ ਪਿਛਲੇ ਅਲਾਰਮ ਸਰਗਰਮੀ ਬਾਰੇ ਜਾਣਕਾਰੀ ਵੇਖਣ ਲਈ ਸਕਰੋ। ਰਿਕਾਰਡਿੰਗ ਵੇਖਣ ਲਈ ਵੀਡੀਓ ਬਟਨ ਨੂੰ ਕਲਿੱਕ ਕਰੋ।",
        'menu_settings': "ਤੁਸੀਂ ਸੈਟਿੰਗ ਚੁਣਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਜਾਰੀ ਕਰਨ ਲਈ ਇੱਕ ਚੋਣ ਚੁਣੋ ਜਾਂ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਪਿੱਛੇ ਚੁਣੋ। ਚੋਣ ਹਨ: ਅਸੁਧਾ ਦੇ ਸੁਧਾਰ, ਰਿਕਾਰਡ ਲੌਗ, ਸਕ੍ਰੀਨ ਪੜ੍ਹਨ ਵਾਲਾ, ਫ੉ਂਟ ਆਕਾਰ।",
        'menu_settings_troubleshoot_and_maintenance': "ਤੁਸੀਂ ਅਸੁਧਾ ਅਤੇ ਮੈਨਟੀਨੈਂਸ ਚੁਣਿਆ ਹੈ। ਅਸੁਧਾ ਪੂਰਾ ਕਰਨ ਲਈ ਅਸੁਧਾ ਚੁਣੋ, ਆਪਣੇ ਨੇੜੇ ਸੰਚਾਰ ਸ਼ਾਖਾ ਲਈ ਸੰਪਰਕ ਜਾਣਕਾਰੀ ਵੇਖਣ ਲਈ ਮੈਨਟੀਨੈਂਸ ਚੁਣੋ,\nਜਾਂ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਪਿੱਛੇ ਚੁਣੋ।",
        'menu_settings_troubleshoot': "ਤੁਸੀਂ ਅਸੁਧਾ ਚੁਣਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਅਸੁਧਾ ਨੂੰ ਪੂਰਾ ਕਰਨ ਦੇ ਪਹਿਲੇ ਸਕਨ ਲਈ ਰੁਕੋ, ਇਹ ਅਮੋਮਾਨੇ 5 ਮਿੰਟ ਲੈਂਦਾ ਹੈ।\nਸਕੈਨ ਬੰਦ ਕਰਨ ਲਈ ਰੱਦ ਕਰੋ।",
        'menu_settings_maintenance': "ਤੁਸੀਂ ਮੈਨਟੀਨੈਂਸ ਚੁਣਿਆ ਹੈ। ਤੁਹਾਡੇ ਨੇੜੇ ਸ਼ਾਖਾ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਗਏ ਵੇਰਵੇ।\nਸੈਟਿੰਗਸ ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਪਿੱਛੇ ਚੁਣੋ।",
        'menu_font_size': "ਤੁਸੀਂ ਫ੉ਂਟ ਆਕਾਰ ਚੁਣਿਆ ਹੈ। ਹਾਲੇ ਵਰਤੋਂ ਹੋ ਰਿਹਾ ਫ੉ਂਟ ਆਕਾਰ।\n\n16 ਤੋਂ 24 ਵਿਚ ਨੰਬਰ ਦਾਖਲ ਕਰੋ ਫ੉ਂਟ ਆਕਾਰ ਬਦਲਣ ਲਈ।\nਅੱਗੇ ਬਢੋ ਅਤੇ ਸੈਟਿੰਗਸ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਦਬਾਓ।",
    # Menu Change Password/ add face id
        'menu_edit_face_id': "ਤੁਸੀਂ ਚਿਹਰਾ ID ਸੋਧਣ ਚੁਣਿਆ ਹੈ। ਅੱਗੇ ਬਢਣ ਲਈ ਚੁਣੋ ਅਤੇ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਬੰਦ ਕਰੋ।",
        'menu_change_password': "ਤੁਸੀਂ ਪਾਸਵਰਡ ਬਦਲਣ ਚੁਣਿਆ ਹੈ। ਅੱਗੇ ਬਢਣ ਲਈ ਚੁਣੋ ਅਤੇ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਬੰਦ ਕਰੋ।",
        'menu_after_check_change_password': "ਕੀਪੈਡ ਤੇ ਕੀਜ਼ ਦੀ ਮਦਦ ਨਾਲ ਨਵਾਂ ਪਿੰਨ ਦਰਜ ਕਰੋ।",
        'menu_check_new_password': "ਇਹ ਨਵੀਂ ਪਿੰਨ ਜੋ ਤੁਸੀਂ ਦਰਜ ਕੀਤੀ ਹੈ।\nਕਿਰਪਾ ਕਰਕੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਤੁਸੀਂ ਆਗੇ ਬਢਣ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਵੱਖਰਾ ਪਿੰਨ ਦਰਜ ਕਰੋ।",
        'menu_check_efi': "ਤੁਸੀਂ ਚਿਹਰਾ ID ਸੋਧਣ ਚੁਣਿਆ ਹੈ। ਅੱਗੇ ਬਢਣ ਲਈ ਚੁਣੋ ਅਤੇ ਮੀਨੂ 'ਤੇ ਵਾਪਸ ਜਾਣ ਲਈ ਬੰਦ ਕਰੋ।",
    # menu languages
        'menu_languages': "ਤੁਸੀਂ ਭਾਸ਼ਾਵਾਂ ਚੁਣਿਆ ਹੈ। ਅੰਗਰੇਜ਼ੀ, ਵੈਲਸ, ਜਾਂ ਪੰਜਾਬੀ ਚੁਣੋ।",
    # alarm:
        'alarm_active': "ਅਲਾਰਮ ਸਰਗਰਮ ਹੈ।",
        'alarm_disactive': "ਅਲਾਰਮ ਬੰਦ ਹੈ।"
    }
}
def get_translation(language, key):
    return translations.get(language, {}).get(key, "")
# Audio files corresponding to each message
audio_files = {
    'English': {
        # system
        'system_on': "audio/english/eng_system_on.mp3",
        'system_off': "audio/english/eng_system_off.mp3",
        'system_armed': "audio/english/eng_system_armed.mp3",
        'system_disarmed': "audio/english/eng_system_disarmed.mp3",
        # face ID
        'user_recognised': "audio/english/eng_user_recognised.mp3",
        'user_not_recognised': "audio/english/eng_user_not_recognised.mp3",
        # pin
        'pin_correct': "audio/english/eng_pin_correct.mp3",
        'pin_incorrect': "audio/english/eng_pin_incorrect.mp3",
        # menu
        'menu': "audio/english/eng_menu.mp3",
        'menu_arm_and_schedule_activation': "audio/english/eng_menu_arm_and_schedule_activation.mp3",
        'menu_arm': "audio/english/eng_menu_arm.mp3",
        'menu_schedule_activation': "audio/english/eng_menu_schedule_activation.mp3",
        'menu_settings': "audio/english/eng_menu_settings.mp3",
        'menu_settings_screen_reader': "audio/english/eng_menu_settings_screen_reader.mp3",
        'menu_settings_record_log': "audio/english/eng_menu_settings_record_log.mp3",
        'menu_settings_troubleshoot_and_maintenance': "audio/english/eng_menu_settings_troubleshoot_and_maintenance.mp3",
        'menu_settings_troubleshoot': "audio/english/eng_menu_settings_troubleshoot.mp3",
        'menu_settings_maintenance': "audio/english/eng_menu_settings_maintenance.mp3",
        'menu_font_size': "audio/english/eng_menu_font_size.mp3",
        'menu_edit_face_id': "audio/english/eng_menu_edit_face_id.mp3",
        'menu_change_password': "audio/english/eng_menu_change_password.mp3",
        'menu_after_check_change_password': "audio/english/eng_menu_after_check_change_password.mp3",
        'menu_check_new_password': "audio/english/eng_menu_check_new_password.mp3",
        'menu_check_efi': "audio/english/eng_menu_check_efi.mp3",
        # menu languages
        'menu_languages': "audio/english/eng_menu_languages.mp3",
        # alarm
        'alarm_active': "audio/english/eng_alarm_active.mp3",
        'alarm_disactive': "audio/english/eng_alarm_disactive.mp3",
        'record': "audio/english/eng_record.mp3",
        'security': "audio/english/eng_security.mp3"
    },
    'Welsh': {
        # system
        'system_on': "audio/welsh/welsh_system_on.mp3",
        'system_off': "audio/welsh/welsh_system_off.mp3",
        'system_armed': "audio/welsh/welsh_system_armed.mp3",
        'system_disarmed': "audio/welsh/welsh_system_disarmed.mp3",
        # face ID
        'user_recognised': "audio/welsh/welsh_user_recognised.mp3",
        'user_not_recognised': "audio/welsh/welsh_user_not_recognised.mp3",
        # pin
        'pin_correct': "audio/welsh/welsh_pin_correct.mp3",
        'pin_incorrect': "audio/welsh/welsh_pin_incorrect.mp3",
        # menu
        'menu': "audio/welsh/welsh_menu.mp3",
        'menu_arm_and_schedule_activation': "audio/welsh/welsh_menu_arm_and_schedule_activation.mp3",
        'menu_arm': "audio/welsh/welsh_menu_arm.mp3",
        'menu_schedule_activation': "audio/welsh/welsh_menu_schedule_activation.mp3",
        'menu_settings': "audio/welsh/welsh_menu_settings.mp3",
        'menu_settings_screen_reader': "audio/welsh/welsh_menu_settings_screen_reader.mp3",
        'menu_settings_record_log': "audio/welsh/welsh_menu_settings_record_log.mp3",
        'menu_settings_troubleshoot_and_maintenance': "audio/welsh/welsh_menu_settings_troubleshoot_and_maintenance.mp3",
        'menu_settings_troubleshoot': "audio/welsh/welsh_menu_settings_troubleshoot.mp3",
        'menu_settings_maintenance': "audio/welsh/welsh_menu_settings_maintenance.mp3",
        'menu_font_size': "audio/welsh/welsh_menu_font_size.mp3",
        'menu_edit_face_id': "audio/welsh/welsh_menu_edit_face_id.mp3",
        'menu_change_password': "audio/welsh/welsh_menu_change_password.mp3",
        'menu_after_check_change_password': "audio/welsh/welsh_menu_after_check_change_password.mp3",
        'menu_check_new_password': "audio/welsh/welsh_menu_check_new_password.mp3",
        'menu_check_efi': "audio/welsh/welsh_menu_check_efi.mp3",
        # menu languages
        'menu_languages': "audio/welsh/welsh_menu_languages.mp3",
        # alarm
        'alarm_active': "audio/welsh/welsh_alarm_active.mp3",
        'alarm_disactive': "audio/welsh/welsh_alarm_disactive.mp3",
        'record': "audio/welsh/welsh_record_started.mp3",
        'security': "audio/welsh/welsh_security_notified.mp3"
    },
    'Punjabi': {
        # system
        'system_on': "audio/punjabi/pun_system_on.mp3",
        'system_off': "audio/punjabi/pun_system_off.mp3",
        'system_armed': "audio/punjabi/pun_system_armed.mp3",
        'system_disarmed': "audio/punjabi/pun_system_disarmed.mp3",
        # face ID
        'user_recognised': "audio/punjabi/pun_user_recognised.mp3",
        'user_not_recognised': "audio/punjabi/pun_user_not_recognised.mp3",
        # pin
        'pin_correct': "audio/punjabi/pun_pin_correct.mp3",
        'pin_incorrect': "audio/punjabi/pun_pin_incorrect.mp3",
        # menu
        'menu': "audio/punjabi/pun_menu.mp3",
        'menu_arm_and_schedule_activation': "audio/punjabi/pun_menu_arm_and_schedule_activation.mp3",
        'menu_arm': "audio/punjabi/pun_menu_arm.mp3",
        'menu_schedule_activation': "audio/punjabi/pun_menu_schedule_activation.mp3",
        'menu_settings': "audio/punjabi/pun_menu_settings.mp3",
        'menu_settings_screen_reader': "audio/punjabi/pun_menu_settings_screen_reader.mp3",
        'menu_settings_record_log': "audio/punjabi/pun_menu_settings_record_log.mp3",
        'menu_settings_troubleshoot_and_maintenance': "audio/punjabi/pun_menu_settings_troubleshoot_and_maintenance.mp3",
        'menu_settings_troubleshoot': "audio/punjabi/pun_menu_settings_troubleshoot.mp3",
        'menu_settings_maintenance': "audio/punjabi/pun_menu_settings_maintenance.mp3",
        'menu_font_size': "audio/punjabi/pun_menu_font_size.mp3",
        'menu_edit_face_id': "audio/punjabi/pun_menu_edit_face_id.mp3",
        'menu_change_password': "audio/punjabi/pun_menu_change_password.mp3",
        'menu_after_check_change_password': "audio/punjabi/pun_menu_after_check_change_password.mp3",
        'menu_check_new_password': "audio/punjabi/pun_menu_check_new_password.mp3",
        'menu_check_efi': "audio/punjabi/pun_menu_check_efi.mp3",
        # menu languages
        'menu_languages': "audio/punjabi/pun_menu_languages.mp3",
        # alarm
        'alarm_active': "audio/punjabi/pun_alarm_active.mp3",
        'alarm_disactive': "audio/punjabi/pun_alarm_disactive.mp3",
        'record': "audio/punjabi/pun_record_started.mp3",
        'security': "audio/punjabi/pun_security_notified.mp3"
    }
}

