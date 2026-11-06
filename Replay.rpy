image closevideo = Movie(loop = True, play="gui/Characters/closevideo.webm")

    

screen replay:
    
    tag profile_menu

    modal False
    style_prefix "ground"

    imagemap:
        ground "gui/MainMenu/codex1.png"
        hover "gui/MainMenu/codex.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    viewport:
        xalign 0.5
        yalign 0.5

        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 1690
        ysize 700

        

        grid 3 4:

            # xalign 1.0  # выравнивание сетки справа
            # yalign 0.0
            
            
            # Это в прологе
            if persistent.Ivy_replay == True:

                imagebutton:
                    idle "gui/Characters/ivyfirstscene_A.png"
                    hover "gui/Characters/ivyfirstscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("ivy_replay", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.Ivy_replay == False:

                add "gui/Characters/nn_BA.png" 

            if persistent.Flora_replay == True:

                imagebutton:
                    idle "gui/Characters/florafirstscene_A.png"
                    hover "gui/Characters/florafirstscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("Flora_replay1", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.Flora_replay == False:

                add "gui/Characters/nn_BA.png" 

            if persistent.lora_First_scene == True:

                imagebutton:
                    idle "gui/Characters/lorafirstscene_A.png"
                    hover "gui/Characters/lorafirstscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("Lora_replay1", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.lora_First_scene == False:

                add "gui/Characters/nn_BA.png" 

            if persistent.lora_Second_scene == True:

                imagebutton:
                    idle "gui/Characters/lorasecondscene_A.png"
                    hover "gui/Characters/lorasecondscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("Lora_replay2", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.lora_Second_scene == False:

                add "gui/Characters/nn_BA.png" 

            if persistent.olivia_Second_scene == True:

                imagebutton:
                    idle "gui/Characters/oliviasecondscene_A.png"
                    hover "gui/Characters/oliviasecondscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("Olivia_replay2", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.olivia_Second_scene == False:

                add "gui/Characters/nn_BA.png" 

            if persistent.Ivy_Second_scene == True:

                imagebutton:
                    idle "gui/Characters/ivysecondscene_A.png"
                    hover "gui/Characters/ivysecondscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("Ivy_replay_second_scene", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.Ivy_Second_scene == False:

                add "gui/Characters/nn_BA.png" 

            if persistent.Miriel_replay == True:

                imagebutton:
                    idle "gui/Characters/mirielfirstscene_A.png"
                    hover "gui/Characters/mirielfirstscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("Miriel_replay", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.Miriel_replay == False:

                add "gui/Characters/nn_BA.png" 


            if persistent.Kalestra_replay == True:

                imagebutton:
                    idle "gui/Characters/kalifirstscene_A.png"
                    hover "gui/Characters/kalifirstscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("kali_scene_replay", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.Miriel_replay == False:

                add "gui/Characters/nn_BA.png" 


            if persistent.olivia_Third_scene == True:
                
                imagebutton:
                    idle "gui/Characters/oliviathirdscene_A.png"
                    hover "gui/Characters/oliviathirdscene_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Replay("olivia_Third_scene_replay", scope={}, locked=False)]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            elif persistent.Miriel_replay == False:

                add "gui/Characters/nn_BA.png" 

    
    if _in_replay:
        imagebutton:
            idle "gui/return-replay1.png" hover "gui/return-replay2.png"
            action [Play("menu_click", "audio/UItaps.mp3"), EndReplay(confirm=True)]
            at test_anim_not
            xpos 540
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/AMAP.png" hover "gui/BMAP.png"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("map_screen")]
            at test_anim_not
            xpos 1660
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

    if main_menu:
        imagebutton:
            idle "gui/AESC.png" hover "gui/BESC.png"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
            at test_anim_not
            xpos 40
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/AMAP.png" hover "gui/BMAP.png"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("map_screen")]
            at test_anim_not
            xpos 1660
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

    else:

        imagebutton:
            idle "gui/AESC.png" hover "gui/BESC.png"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
            at test_anim_not
            xpos 40
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"
            
        imagebutton:
            idle "gui/AMAINMENU4.png" hover "gui/BMAINMENU4.png"
            action [Play("menu_click", "audio/UItaps.mp3"), MainMenu()]
            at test_anim_not
            xpos 240
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/AMAP.png" hover "gui/BMAP.png"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("map_screen")]
            at test_anim_not
            xpos 1660
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

