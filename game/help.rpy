screen help1():

    key 'e' action ShowMenu("language1")
    key 'E' action ShowMenu("language1")
    key 'У' action ShowMenu("language1")
    key 'у' action ShowMenu("language1")

    key 'q' action ShowMenu("credits1")
    key 'Q' action ShowMenu("credits1")
    key 'Й' action ShowMenu("credits1")
    key 'й' action ShowMenu("credits1")

    key 'K_ESCAPE' action Return()

    tag menu

    # if renpy.variant("pc"):
    imagemap:
        ground "gui/game_menu_pref1.png" 
        hover "gui/game_menu_pref2.png" 
        
        hotspot (1410,105,219,73) action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("other1")]
        hotspot (1185,105,225,73) action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("language1")]
        hotspot (964,105,219,75) action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("help1")]
        hotspot (739,105,225,73) action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("credits1")]
        hotspot (514,105,225,73) action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("music_screen")]
        hotspot (292,105,224,73) action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("preferences")]

    add "gui/game_menu_settings2.png" 
        
    vbox:
        spacing 30
        xpos 55
        ypos 322
            


        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)
            

            text "Advances diaolgue" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30
                
            text "Space" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Access the game menu" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "Escape" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Skip dialogues" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "Ctrl" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Toggles dialogue skipping" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "Tab" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Hides the user interface" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "H" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 
    
    vbox:
        spacing 30
        xpos (970)
        ypos 322
            


        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Rolls back" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30


            text "Page Up" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Rolls forward" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "Page down" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Takes a screenshot" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "S" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Toggles assistive self-voicing" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "V" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

        frame:
            background "gui/test_2.png"
            hover_background "gui/test_hover.png"

            padding (0,0)
            xysize (1120, 80)

            text "Open the accessibility menu" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

            text "Shift+A" align (0.7, 0.4) font "font/NotoSansSC-Black.ttf" size 30 

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
        idle "gui/ASAVE22.png" hover "gui/BSAVE22.png"
        action ShowMenu('save')
        at test_anim_not
        xpos 1320
        ypos 900
        focus_mask True
        style "navigation_button"
        hover_sound "audio/CLS.ogg"

    imagebutton:
        idle "gui/BLOAD22.png" hover "gui/BLOAD23.png"
        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("load")]
        at test_anim_not
        xpos 1620
        ypos 900
        focus_mask True
        style "navigation_button"
        hover_sound "audio/CLS.ogg"


