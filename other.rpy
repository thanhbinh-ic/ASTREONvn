screen other1():

    key 'e' action ShowMenu("load")
    key 'E' action ShowMenu("load")
    key 'У' action ShowMenu("load")
    key 'у' action ShowMenu("load")

    key 'q' action ShowMenu("language1")
    key 'Q' action ShowMenu("language1")
    key 'Й' action ShowMenu("language1")
    key 'й' action ShowMenu("language1")

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

    add "gui/game_menu_settings4.png"

    # frame:
    
    #     has viewport  


    #     xpos 0
    #     ypos 220
    #     xsize 920
    #     ysize 750 

        

    #     vbox:
    #         xalign 0.5

    #         frame:
    #             add "gui/FreindlyDev/CrossRealm1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)
    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4 
    #                 text _("Cross Realms") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://duskduck.itch.io/cross-realms}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)  
            
    #         frame:
    #             add "gui/FreindlyDev/WildCats1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)
                
    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4
    #                 text _("Wild Cats") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://lopaphi.itch.io/wild-cats}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)  

    #         frame:
    #             add "gui/FreindlyDev/Dogma1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)

    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4 
    #                 text _("Dogma") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://whitemasq.itch.io/dogma/devlog/897044/dogma-04-s1-100-release-pc}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)  

    #         frame:
    #             add "gui/FreindlyDev/Reconstruction1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)

    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4
    #                 text _("Reconstruction") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://yui-yal.itch.io/reconstruction}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)  

    # frame:
    
    #     has viewport  


    #     xpos 900
    #     ypos 220
    #     xsize 920
    #     ysize 650 

    #     vbox:
    #         xalign 0.5

    #         frame:
    #             add "gui/FreindlyDev/Gay1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)

    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4
    #                 text _("Artifice") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://duve-dev.itch.io/artifice}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)  


            

            
    #         frame:
    #             add "gui/FreindlyDev/DrivenByDesire1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)
    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4
    #                 text _("Driven By Desire") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://kloppstyle.itch.io/driven-by-desire}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)

    #         frame:
    #             add "gui/FreindlyDev/Profiler1.png" 
    #             xpos (100)
    #             ypos (10)
    #             xsize 520
    #             ysize 168
    #             padding (0,0)
    #             vbox:
    #                 xalign 0.4 
    #                 yalign 0.4
    #                 text _("Profiler") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
    #                 text _("{a=https://divebar-studio.itch.io/profiler}{color=#03befc}Link to the game{/a}{/color}") size 35 font "font/NotoSansSC-Black.ttf" color (255,255,255)  


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
