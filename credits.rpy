screen credits1():

    key 'e' action ShowMenu("help1")
    key 'E' action ShowMenu("help1")
    key 'У' action ShowMenu("help1")
    key 'у' action ShowMenu("help1")

    key 'q' action ShowMenu("music_screen")
    key 'Q' action ShowMenu("music_screen")
    key 'Й' action ShowMenu("music_screen")
    key 'й' action ShowMenu("music_screen")

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

    add "gui/game_menu_settings1.png" 
    add "gui/game_menu_frame12.png" 

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара

        xpos 76
        ypos 235
        xsize 1110
        ysize 610

    
        
    
        vbox:
            spacing 10
            xalign 0.5
            text _("[config.name!t]") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Version 0.4.5") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            text ""
            text _("Game Developer") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("{a=https://www.patreon.com/c/NoGloryx}{color=#03befc}https://www.patreon.com/c/NoGloryx{/a}{/color}") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)   

            text ""
            text _("Music by") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("{color=#ffffff}https://pixabay.com{/color}") size 25 font "font/Montserrat-Medium.ttf" 
            text _("{color=#ffffff}https://aimusicfactory.ai{/color}") size 25 font "font/Montserrat-Medium.ttf" 
            text _("{color=#ffffff}https://suno.com{/color}") size 25 font "font/Montserrat-Medium.ttf" 
            text ""

            text _("Music by") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Scott Buckley") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("{a=http://creativecommons.org/licenses/by/3.0/}{color=#03befc}Licensed under Creative Commons: By Attribution 3.0{/a}{/color}") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)   
            text ""

            text _("Music by") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Kevin MacLeod") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("{a=http://creativecommons.org/licenses/by/3.0/}{color=#03befc}Licensed under Creative Commons: By Attribution 3.0{/a}{/color}") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)   
            text ""

            text _("Translations") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("CH Translation - Z&H") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("RU Translation - Debios") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("{a=https://boosty.to/debios}{color=#03befc}Благодарность переводчику, за его труд!{/a}{/color}") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)   
            text ""
            text _("Special thanks to") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("W.M, Duve, JazzPourer, D-san, TheRock, AsTc3r, and all other dev who help me.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("A huge thank you to my discord moderators.") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("NoSharzii, Dr.Nobody.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            
            text _("")
            text _("I would like to say a special thanks to") size 35 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("To my testers who helped to improve and fix bugs in this game, thank you.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Illusion Soft{color=#ffffff} for making HS2 and Studio NEO.") size 25 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("The Illusion Soft and HS2 Discord communities{color=#ffffff}") size 25 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("{color=#ffffff}If it wasn't for these guys, this game might not have happened.")  size 25  color "#6f542c"

            text _("")
            text _("{color=#ffffff}{font=font/NotoSansSC-Black.ttf}And to everyone else who helped me but who I forgot to mention...")

            if gui.about:
                text "[gui.about!t]\n"

            text _("{color=#6f542c}{font=font/NotoSansSC-Black.ttf}Made with {font=font/NotoSansSC-Black.ttf}{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]{/color}. {color=#ffffff}{font=font/NotoSansSC-Black.ttf}\n\n[renpy.license!t]")  size 25  color (0,246,255)


    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара

        xpos 1296
        ypos 235
        xsize 570
        ysize 610

        vbox:
            spacing 10
            xalign 0.5
            text _("PATRONS/SUBSCRIBERS") size 40 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text ""
            text _("{color=#6f542c}A huge thank to my {color=#ffffff}Deathwatch Captain:") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
            text _("Dr.NoBody, NoGKN, Notpro, Dead.hunter, Flak, YuKa.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("{color=#6f542c}A huge thank to my {color=#ffffff}Interrogator:") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
            text _("Than, Mr.Lonely, hailstromz, TripleNiple333.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("{color=#6f542c}A huge thank to my {color=#ffffff}Guardsman:") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
            text _("Nooby Nick, Dean, madox84109, Vilesh Darothar, son, Calothora.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("{color=#6f542c}Special thanks: {color=#ffffff} ") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
            text _("Léo, Unknown.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("{color=#6f542c}{size=30}And a huge thanks for my other{color=#ffffff} {size=35}Acolyte, Scribe, {color=#6f542c}{size=30}YOU ALL GUYS THE BEST.") size 35 font "font/DAGGERSQUARE.otf" color (0,246,255)

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
    #             xalign 0.24
    #             yalign 0.4

    #             text _("Preferences") size 60 font "font/NotoSansSC-Black.ttf" color (0,246,255)

    #         vbox:
    #             xalign 0.24
    #             yalign 0.8

    #             text _("Credits screen") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    #     button:
    #         background "gui/preference_frame.png"
    #         xysize (1920, 1080)
    #         xpos 0 ypos 180
    #         vbox:
    #             spacing 10
    #             align (0.5, 0.95)
    #             text _("{color=#A9A9A9}Screen{/color}") font "font/DAGGERSQUARE.otf" size 30


    #     frame:
    #         add "gui/MenuFrame1.png" 
    #         xpos 50
    #         ypos 340
    #         style_prefix "about"
            
    #     frame:
    #         add "gui/MenuFrame4.png" 
    #         xpos (770)
    #         ypos (340)

    #     frame:
        
    #         has viewport  # Первое выражение в блоке frame
    #         mousewheel True  # Прокрутка колесиком мыши
    #         draggable True  # Возможность перетаскивания содержимого
    #         scrollbars "vertical"  # Добавление вертикального скроллбара

    #         xpos 76
    #         ypos 350
    #         xsize 1070
    #         ysize 550

        
            
        
    #         vbox:
    #             spacing 10
    #             xalign 0.5
    #             text _("[config.name!t]") size 45 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("Version 0.2") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)

    #             text ""
    #             text _("Game Developer") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("{a=https://www.patreon.com/Astreon}{color=#03befc}https://www.patreon.com/Astreon{/a}{/color}") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)   

    #             text ""
    #             text _("Music by") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("{color=#ffffff}https://pixabay.com{/color}") size 25 font "font/Montserrat-Medium.ttf" 
    #             text _("{color=#ffffff}https://aimusicfactory.ai{/color}") size 25 font "font/Montserrat-Medium.ttf" 
    #             text ""

    #             text _("Music by") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("Scott Buckley") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("{a=http://creativecommons.org/licenses/by/3.0/}{color=#03befc}Licensed under Creative Commons: By Attribution 3.0{/a}{/color}") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)   
    #             text ""

    #             text _("Music by") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("Kevin MacLeod") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("{a=http://creativecommons.org/licenses/by/3.0/}{color=#03befc}Licensed under Creative Commons: By Attribution 3.0{/a}{/color}") size 30 font "font/NotoSansSC-Black.ttf" color (255,255,255)   
    #             text ""

    #             text _("Translations") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("CH Translation - xxm---xxm") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("RU Translation - Noglory") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text ""
    #             text _("Special thanks to") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("Chainz, JazzPourer, Sienna, YaL, TheRock, AsTc3r, and all other dev who help me.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("")
    #             text _("A huge thank you to my discord moderators.") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("NoSharzii.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("")
                
    #             text _("")
    #             text _("I would like to say a special thanks to") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("To my testers who helped to improve and fix bugs in this game, thank you.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("")
    #             text _("Illusion Soft{color=#ffffff} for making HS2 and Studio NEO.") size 25 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("The Illusion Soft and HS2 Discord communities{color=#ffffff}") size 25 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("{color=#ffffff}If it wasn't for these guys, this game might not have happened.")  size 25  color (0,246,255)

    #             text _("")
    #             text _("{color=#ffffff}{font=font/NotoSansSC-Black.ttf}And to everyone else who helped me but who I forgot to mention...")

    #             if gui.about:
    #                 text "[gui.about!t]\n"

    #             text _("{color=#a40000}{font=font/NotoSansSC-Black.ttf}Made with {font=font/NotoSansSC-Black.ttf}{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]{/color}. {color=#ffffff}{font=font/NotoSansSC-Black.ttf}\n\n[renpy.license!t]")  size 25  color (0,246,255)


        
            


    #     frame:
        
    #         has viewport  # Первое выражение в блоке frame
    #         mousewheel True  # Прокрутка колесиком мыши
    #         draggable True  # Возможность перетаскивания содержимого
    #         scrollbars "vertical"  # Добавление вертикального скроллбара

    #         xpos 1346
    #         ypos 350
    #         xsize 530
    #         ysize 560

    #         vbox:
    #             spacing 10
    #             xalign 0.5
    #             text _("PATRONS/SUBSCRIBERS") size 40 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text ""
    #             text _("A huge thank to my {color=#ffffff}Deathwatch Captain:") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("Dr.NoBody, Робин.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("")
    #             text _("A huge thank to my {color=#ffffff}Interrogator:") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("PayPao, DoomChicken.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("")
    #             text _("A huge thank you to my {color=#ffffff}Guardsman:") size 35 font "font/NotoSansSC-Black.ttf" color (0,246,255)
    #             text _("Léo, Nooby Nick, Dean.") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #             text _("")
    #             text _("{size=30}And a huge thanks for my other{color=#ffffff} {size=35}Acolyte, Scribe, {color=#00f6ff}{size=30}YOU ALL GUYS THE BEST.") size 35 font "font/DAGGERSQUARE.otf" color (0,246,255)


            

        


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