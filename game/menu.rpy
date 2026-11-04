default persistent.audio = False

default tooltip_text = None



screen tooltip():
    if tooltip_text:
        frame:
            style "tooltip_frame"
            text tooltip_text style "tooltip_text"


style tooltip_frame:
    background "#25252500"  # Полупрозрачный черный фон
    # padding (10, 100)
    xalign 0.97 # Выравнивание по горизонтали
    ypos 1  # Подсказка над элементом

    xsize 600
    ysize 550

if Language(None):
    style tooltip_text:
        color "#fff"
        font "font/NotoSansSC-Black.ttf" size 40

screen tooltip():
    if tooltip_text:
        frame:
            style "tooltip_frame"
            text tooltip_text style "tooltip_text"

# второй тул 

screen tooltip1():
    if tooltip_text:
        frame:
            style "tooltip_frame1"
            text tooltip_text style "tooltip_text"


style tooltip_frame1:
    background "#25252500"  # Полупрозрачный черный фон
    # padding (10, 100)
    xalign 0.99 # Выравнивание по горизонтали
    ypos 10   # Подсказка над элементом

    xsize 600
    ysize 550


screen tooltip1():
    if tooltip_text:
        frame:
            style "tooltip_frame1"
            text tooltip_text style "tooltip_text"

transform hover_transform:
    on hover:
        parallel:

            linear 0.1 alpha 1.0
            
    on idle:
        parallel:
            linear 0.1 alpha 0.7

screen music_screen():

    key 'e' action ShowMenu("credits1")
    key 'E' action ShowMenu("credits1")
    key 'У' action ShowMenu("credits1")
    key 'у' action ShowMenu("credits1")

    key 'q' action ShowMenu("preferences")
    key 'Q' action ShowMenu("preferences")
    key 'Й' action ShowMenu("preferences")
    key 'й' action ShowMenu("preferences")

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
    
    add "gui/game_menu_music.png" 

    frame: 
        xpos 1250
        ypos 300

        use tooltip1()

    frame:
            
        has viewport  # Первое выражение в блоке frame
        xpos 55
        ypos 322
        xsize 1140
        ysize 330

        vbox:

            spacing 30

            frame:
                background "gui/test_1.png"
                padding (0,0)
                xysize (1120, 80)
                text "Music Volume: [int(preferences.get_mixer('music') * 100)]%" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                bar value Preference("Music Volume"): 
                    left_bar "gui/bar-hover2.png" 
                    right_bar "gui/bar-idle.png" 
                    thumb "gui/barsth.png"
                    xysize (566, 40)  
                    xalign 0.9 yalign 0.2
                    at hover_transform
                    hovered SetVariable("tooltip_text", "Adjust the music volume.    P.S. Sometimes even moan.")  # Текст подсказки
                    unhovered SetVariable("tooltip_text", None)

            


                

            frame:
                background "gui/test_1.png"
                padding (0,0)
                xysize (1120, 80)
                text "Sound Volume: [int(preferences.get_mixer('sfx') * 100)]%" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                bar value Preference("Sound Volume"): 
                    left_bar "gui/bar-hover2.png"
                    right_bar "gui/bar-idle.png"
                    thumb "gui/barsth.png"
                    xysize (566, 40)  
                    xalign 0.9 yalign 0.2
                    at hover_transform
                    hovered SetVariable("tooltip_text", "Adjust the sound volume.")  # Текст подсказки
                    unhovered SetVariable("tooltip_text", None)

    

            vbox:
                    


                frame:
                    background "gui/test_1.png"
                    hover_background "gui/test_hover.png"

                    padding (0,0)
                    xysize (1120, 80)
                    text "Music" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30


                    hbox:
                        spacing 15
                        align (0.9, 0.4)

                        if persistent.audio:
                            textbutton _("Unmute all"):
                                text_size 32
                                text_font "font/NotoSansSC-Black.ttf"
                                action [Preference("all mute", "toggle"), ToggleVariable("persistent.audio", False), With(dissolve)]
                                hovered SetVariable("tooltip_text", "Disables all music in the game, including sounds.")  # Текст подсказки
                                unhovered SetVariable("tooltip_text", None)
                        else:
                            textbutton _("Mute all"):
                                text_size 32
                                text_font "font/NotoSansSC-Black.ttf"
                                action [Preference("all mute", "toggle"), ToggleVariable("persistent.audio", True), With(dissolve)]
                                hovered SetVariable("tooltip_text", "Disables all music in the game, including sounds.")  # Текст подсказки
                                unhovered SetVariable("tooltip_text", None)


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


    # else:

        

    #     frame:
    #         add "gui/game_menu_pref.png" 
    #         xsize 520
    #         ysize 180
    #         padding (0,0)
    #         vbox:
    #             xalign 0.5 
    #             yalign 0.4

    #             text _("Preferences") size 60 font "font/NotoSansSC-Black.ttf" color (0,246,255)

    #         vbox:
    #             xalign 0.28
    #             yalign 0.8
    #             text _("Settings screen") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            
    #     button:
    #         background "gui/preference_frame.png"
    #         xysize (1920, 1080)
    #         xpos 0 ypos 180

    #     if Language("chinese"):

    #         vbox:
    #             spacing -230
    #             align (0.91, 0.336)
                

    #             frame:
    #                 background "gui/test.png"
    #                 padding (0,0)
    #                 xysize (1860,80)
    #                 text "Music Volume: [int(preferences.get_mixer('music') * 100)]%" align (0.03, 0.5) font "font/NotoSansSC-Black.ttf" size 30

    #                 bar value Preference("Music Volume"): 
    #                     left_bar "gui/bar-hover.png" 
    #                     right_bar "gui/bar-idle.png" 
    #                     thumb "gui/barsth.png"
    #                     xysize (566, 40)  
    #                     xalign 0.4 yalign 0.2
    #                     at hover_transform
    #                     hovered SetVariable("tooltip_text", "Adjust the music volume")  # Текст подсказки
    #                     unhovered SetVariable("tooltip_text", None)

    #                 use tooltip1()


                    

    #             frame:
    #                 background "gui/test.png"
    #                 padding (0,0)
    #                 ypos (235)
    #                 xysize (1860,80)
    #                 text "Sound Volume: [int(preferences.get_mixer('sfx') * 100)]%" align (0.03, 0.5) font "font/NotoSansSC-Black.ttf" size 30

    #                 bar value Preference("Sound Volume"): 
    #                     left_bar "gui/bar-hover.png"
    #                     right_bar "gui/bar-idle.png"
    #                     thumb "gui/barsth.png"
    #                     xysize (566, 40)  
    #                     xalign 0.4 yalign 0.2
    #                     at hover_transform
    #                     hovered SetVariable("tooltip_text", "Adjust the sound volume")  # Текст подсказки
    #                     unhovered SetVariable("tooltip_text", None)

    #         vbox:
    #             spacing -230
    #             xpos (50)
    #             ypos (606)
                    


    #             frame:
    #                 background "gui/test.png"
    #                 hover_background "gui/test_hover.png"

    #                 padding (0,0)
    #                 xysize (1860, 350)
    #                 text "Music" align (0.03, 0.06) font "font/NotoSansSC-Black.ttf" size 30


    #                 hbox:
    #                     spacing 15
    #                     align (0.5, 0.04)

    #                     if persistent.audio:
    #                         textbutton _("Unmute all"):
    #                             text_size 32
    #                             text_font "font/NotoSansSC-Black.ttf"
    #                             action [Preference("all mute", "toggle"), ToggleVariable("persistent.audio", False), With(dissolve)]
    #                             hovered SetVariable("tooltip_text", "Disables all music in the game, including sounds.")  # Текст подсказки
    #                             unhovered SetVariable("tooltip_text", None)
    #                     else:
    #                         textbutton _("Mute all"):
    #                             text_size 32
    #                             text_font "font/NotoSansSC-Black.ttf"
    #                             action [Preference("all mute", "toggle"), ToggleVariable("persistent.audio", True), With(dissolve)]
    #                             hovered SetVariable("tooltip_text", "Disables all music in the game, including sounds.")  # Текст подсказки
    #                             unhovered SetVariable("tooltip_text", None)

    #     elif Language(None):

    #         vbox:
    #             spacing -230
    #             align (0.91, 0.336)
                

    #             frame:
    #                 background "gui/test.png"
    #                 padding (0,0)
    #                 xysize (1860,80)
    #                 text "Music Volume" align (0.03, 0.5) font "font/DAGGERSQUARE.otf" size 30

    #                 bar value Preference("Music Volume"): 
    #                     left_bar "gui/bar-hover.png" 
    #                     right_bar "gui/bar-idle.png" 
    #                     thumb "gui/barsth.png"
    #                     xysize (566, 40)  
    #                     xalign 0.4 yalign 0.2
    #                     at hover_transform
    #                     hovered SetVariable("tooltip_text", "Adjust the music volume")  # Текст подсказки
    #                     unhovered SetVariable("tooltip_text", None)

    #                 use tooltip1()


                    

    #             frame:
    #                 background "gui/test.png"
    #                 padding (0,0)
    #                 ypos (235)
    #                 xysize (1860,80)
    #                 text "Sound Volume" align (0.03, 0.5) font "font/DAGGERSQUARE.otf" size 30

    #                 bar value Preference("Sound Volume"): 
    #                     left_bar "gui/bar-hover.png"
    #                     right_bar "gui/bar-idle.png"
    #                     thumb "gui/barsth.png"
    #                     xysize (566, 40)  
    #                     xalign 0.4 yalign 0.2
    #                     at hover_transform
    #                     hovered SetVariable("tooltip_text", "Adjust the sound volume")  # Текст подсказки
    #                     unhovered SetVariable("tooltip_text", None)

        

    #         vbox:
    #             spacing -230
    #             xpos (50)
    #             ypos (606)
                    


    #             frame:
    #                 background "gui/test.png"
    #                 hover_background "gui/test_hover.png"

    #                 padding (0,0)
    #                 xysize (1860, 350)
    #                 text "Music" align (0.03, 0.06) font "font/DAGGERSQUARE.otf" size 30


    #                 hbox:
    #                     spacing 15
    #                     align (0.5, 0.04)

    #                     if persistent.audio:
    #                         textbutton _("Unmute all"):
    #                             text_size 32
    #                             text_font "font/DAGGERSQUARE.otf"
    #                             action [Preference("all mute", "toggle"), ToggleVariable("persistent.audio", False), With(dissolve)]
    #                             hovered SetVariable("tooltip_text", "Disables all music in the game, including sounds.")  # Текст подсказки
    #                             unhovered SetVariable("tooltip_text", None)
    #                     else:
    #                         textbutton _("Mute all"):
    #                             text_size 32
    #                             text_font "font/DAGGERSQUARE.otf"
    #                             action [Preference("all mute", "toggle"), ToggleVariable("persistent.audio", True), With(dissolve)]
    #                             hovered SetVariable("tooltip_text", "Disables all music in the game, including sounds.")  # Текст подсказки
    #                             unhovered SetVariable("tooltip_text", None)

        

    #     imagebutton:
    #         idle "gui/AOPTION1.png" hover "gui/BOPTION1.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("preferences")]
    #         at test_anim_not
    #         xpos 60
    #         ypos 190
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/AMUSIC1.png" hover "gui/BMUSIC1.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("music")]
    #         at test_anim_not
    #         xpos 360
    #         ypos 190
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/ACREDITS.png" hover "gui/BCREDITS.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("credits1")]
    #         at test_anim_not
    #         xpos 660
    #         ypos 190
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/AHELP.png" hover "gui/BHELP.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("help1")]
    #         at test_anim_not
    #         xpos 960
    #         ypos 190
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/ALANGUAGE.png" hover "gui/BLANGUAGE.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("language1")]
    #         at test_anim_not
    #         xpos 1260
    #         ypos 190
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/AOTHER.png" hover "gui/BOTHER.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("other1")]
    #         at test_anim_not
    #         xpos 1560
    #         ypos 190
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/ASAVE.png" hover "gui/BSAVE.png"
    #         action ShowMenu('save')
    #         at test_anim_not
    #         xpos 1240
    #         ypos 950
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/ALOAD.png" hover "gui/BLOAD.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("load")]
    #         at test_anim_not
    #         xpos 1540
    #         ypos 950
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     if _in_replay:
    #         imagebutton:
    #             idle "gui/return-replayx.png" hover "gui/return-replayx1.png"
    #             action [Play("menu_click", "audio/UItaps.mp3"), EndReplay(confirm=True)]
    #             at test_anim_not
    #             xpos 640
    #             ypos 950
    #             focus_mask True
    #             style "navigation_button"
    #             hover_sound "audio/CLS.ogg"

    #     if main_menu:
    #         imagebutton:
    #             idle "gui/return-pref.png" hover "gui/return-pref1.png"
    #             action [Play("menu_click", "audio/UItaps.mp3"), Return()]
    #             at test_anim_not
    #             xpos 40
    #             ypos 950
    #             focus_mask True
    #             style "navigation_button"
    #             hover_sound "audio/CLS.ogg"
    #     else:
    #         imagebutton:
    #             idle "gui/AMAINMENU.png" hover "gui/BMAINMENU.png"
    #             action [Play("menu_click", "audio/UItaps.mp3"), MainMenu()]
    #             at test_anim_not
    #             xpos 40
    #             ypos 950
    #             focus_mask True
    #             style "navigation_button"
    #             hover_sound "audio/CLS.ogg"

    #         imagebutton:
    #             idle "gui/return-pref.png" hover "gui/return-pref1.png"
    #             action [Play("menu_click", "audio/UItaps.mp3"), Return()]
    #             at test_anim_not
    #             xpos 340
    #             ypos 950
    #             focus_mask True
    #             style "navigation_button"
    #             hover_sound "audio/CLS.ogg"