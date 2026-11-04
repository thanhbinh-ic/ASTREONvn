init:
    default Lora_path = False
    default Olivia_path = False
    default Anya_path = False
    default Shiya_path = False
    default Anya_path_replay = False

    default Lora_love = True
    default Olivia_love = True
    default Anya_love = True
    default Shiya_love = True

define unlock_anya = 0
define unlock_lora = 0
define unlock_olivia = 0
define unlock_shiya = 0
define unlock_ivy = 0
define unlock_flora = 0
define unlock_miriel = 0
define unlock_ember = 0
define unlock_astoria = 0
define unlock_aisha = 0
define unlock_kalestra = 0
define unlock_zoya = 0
define unlock_riya = 0
define unlock_elaena = 0
define mc_powerup = 0


define death_anya = 0
define death_lora = 1
define death_olivia = 0
define death_shiya = 0
define death_ivy = 0
define death_flora = 0
define death_miriel = 0
define death_ember = 0
define death_astoria = 0


transform fade_in:
    alpha 0.0
    linear 0.6 alpha 1.0

transform fade_out:
    alpha 1.0
    linear 0.3 alpha 0.0

default character_count = 10



label profile_menu_context:
    call screen profile_menu
    return

screen profile_menu:
    

    tag profile_menu

    modal False
    style_prefix "ground"

    button:
        background "gui/characters/profile_menu.png"
        xysize (1920, 1080)

    

    imagemap:
        ground "gui/MainMenu/codex1.png"
        hover "gui/MainMenu/codex.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    frame:
            
            background None
            has vbox

            if persistent.preview:
                add persistent.preview at fade_in



    frame:

        xalign 0.94
        yalign 0.5

        xsize 580
        ysize 630
        
        
        
        has viewport
        scrollbars "vertical" 
        mousewheel True



        vbox:


            
            # if mc_powerup == 0:
            #     imagebutton:
                                
            #             idle "gui/characters/mc1button.png"
            #             hover "gui/characters/mc2button.png"
            #             action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("mc1")]
            #             xpos 92
            #             focus_mask True
            #             style "navigation_button"
            #             hover_sound "audio/CLS.ogg"
            #             hovered [SetVariable("persistent.preview", "gui/characters/mc1_preview.png")]
            #             unhovered [SetVariable("persistent.preview", None)]

            # elif mc_powerup == 1: 
            #     imagebutton:
                                
            #             idle "gui/characters/mc1button.png"
            #             hover "gui/characters/mc2button.png"
            #             action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("mc1")]
            #             xpos 92
            #             focus_mask True
            #             style "navigation_button"
            #             hover_sound "audio/CLS.ogg"
            #             hovered [SetVariable("persistent.preview", "gui/characters/mc3.png")]
            #             unhovered [SetVariable("persistent.preview", None)]

            # elif mc_powerup == 2: 
            #     imagebutton:
                                
            #             idle "gui/characters/mc1button.png"
            #             hover "gui/characters/mc2button.png"
            #             action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("mc1")]
            #             xpos 92
            #             focus_mask True
            #             style "navigation_button"
            #             hover_sound "audio/CLS.ogg"
            #             hovered [SetVariable("persistent.preview", "gui/characters/mc5.png")]
            #             unhovered [SetVariable("persistent.preview", None)]

            if unlock_anya == 1:
                
                imagebutton:
                            
                    idle "gui/characters/anya1button.png"
                    hover "gui/characters/anya2button.png"
                    action [SetVariable("persistent.preview", None), Play("menu_click", "audio/UItaps.mp3"), ShowMenu("anya1")]
                    xpos 0
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    hovered [SetVariable("persistent.preview", "gui/characters/anya2.png")]
                    unhovered [SetVariable("persistent.preview", None)]

            else:
                
                imagebutton:
                            
                    idle "gui/characters/anya3button.png"
                    

            if unlock_lora == 1:
                
                imagebutton:
                            
                    idle "gui/characters/lora1button.png"
                    hover "gui/characters/lora2button.png"
                    action [SetVariable("persistent.preview", None), Play("menu_click", "audio/UItaps.mp3"), ShowMenu("lora1")]
                    xpos 0
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    hovered [SetVariable("persistent.preview", "gui/characters/lora1.png")]
                    unhovered [SetVariable("persistent.preview", None)]

            if unlock_olivia == 1:

                imagebutton:
                            
                    idle "gui/characters/olivia1button.png"
                    hover "gui/characters/olivia2button.png"
                    action [SetVariable("persistent.preview", None), Play("menu_click", "audio/UItaps.mp3"), ShowMenu("olivia1")]
                    xpos 0
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    hovered [SetVariable("persistent.preview", "gui/characters/olivia1.png")]
                    unhovered [SetVariable("persistent.preview", None)]

            else:

                imagebutton:
                            
                    idle "gui/characters/olivia3button.png"


            if unlock_miriel == 1:

                imagebutton:
                            
                    idle "gui/characters/miriel1button.png"
                    hover "gui/characters/miriel2button.png"
                    action [SetVariable("persistent.preview", None), Play("menu_click", "audio/UItaps.mp3"), ShowMenu("miriel1")]
                    xpos 0
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    hovered [SetVariable("persistent.preview", "gui/characters/miriel1.png")]
                    unhovered [SetVariable("persistent.preview", None)]
            

            else:

                imagebutton:
                            
                    idle "gui/characters/miriel3button.png"


            if unlock_flora == 1:

                imagebutton:
                            
                    idle "gui/characters/flora1button.png"
                    hover "gui/characters/flora2button.png"
                    action [SetVariable("persistent.preview", None), Play("menu_click", "audio/UItaps.mp3"), ShowMenu("flora1")]
                    xpos 0
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    hovered [SetVariable("persistent.preview", "gui/characters/flora1.png")]
                    unhovered [SetVariable("persistent.preview", None)]

            else:

                imagebutton:
                            
                    idle "gui/characters/flora3button.png"
                    

            if unlock_kalestra == 1:

                imagebutton:
                            
                    idle "gui/characters/kalestra1button.png"
                    hover "gui/characters/kalestra2button.png"
                    action [SetVariable("persistent.preview", None), Play("menu_click", "audio/UItaps.mp3"), ShowMenu("kalestra1")]
                    xpos 0
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    hovered [SetVariable("persistent.preview", "gui/characters/kalestra1.png")]
                    unhovered [SetVariable("persistent.preview", None)]

            else:

                imagebutton:
                            
                    idle "gui/characters/kalestra3button.png"

    
            

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


# screen mc1:

#     modal False
#     style_prefix "ground"

#     if mc_powerup == 0:
#         button:
#             background "gui/characters/mc2.png"
#             xysize (1920, 1080)

#     elif mc_powerup == 1:
#         button:
#             background "gui/characters/mc4.png"
#             xysize (1920, 1080)

#     elif mc_powerup == 2:
#         button:
#             background "gui/characters/mc6.png"
#             xysize (1920, 1080)

#     frame:
#         xpos 1120
#         xsize 520
#         ysize 180
#         padding (0, 0)
#         vbox:
#             xpos 50
#             yalign 0.5
#             text _("Character") size 60 font "font/DAGGERSQUARE.otf" color (0, 246, 255)

#         vbox:
#             xpos 60
#             yalign 1.2
#             text _("Name [mc]") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

#         vbox:
#             xpos 60
#             yalign 1.9
#             text _("Age - 41") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

#         vbox:
#             xpos 60
#             yalign 2.6
#             text _("Height - 190 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

#         vbox:
#             xpos 60
#             yalign 3.3
#             text _("Weight - 90 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

#         vbox:
#             xpos 60
#             yalign 4.0
#             text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

#         #32

#         # vbox:
#         #     xpos 60
#         #     ypos 590
#         #     xsize 100

#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
#         #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            

#     imagebutton:
#         idle "gui/ANEXT.png" hover "gui/BNEXT.png"
#         action [Play("menu_click", "audio/UItaps.mp3"),Hide("mc1"), ShowMenu("profile_menu")]
#         at test_anim_not
#         xpos 30
#         ypos 760
#         focus_mask True
#         style "navigation_button"
#         hover_sound "audio/CLS.ogg"

screen anya1:

    tag profile_menu 

    imagemap:
        ground "gui/characters/Anya2.png"
        hover "gui/characters/anya1_preview.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    modal False
    style_prefix "ground"

    frame:
        add "gui/characters/profile_menu2.png" 

    vbox:
        xpos 1320
        ypos 180
        text _("Character") size 60 font "font/DAGGERSQUARE.otf" color "#6f542c"


    frame:

        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара


        xpos 1320
        ypos 270
        xsize 530
        ysize 670

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Anya") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Age - 33") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Height - 173 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weight - 64 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if death_anya == 0:
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

            else:
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("It doesn`t matter what`s") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("going on around you, it") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("matters how you feel") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("about it.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)


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
            action [Play("menu_click", "audio/UItaps.mp3"), Return("")]
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



screen anya2:

    modal False
    style_prefix "ground"

    button:
        background "gui/characters/AnyaNumber1.png"
        xysize (1920, 1080)

    frame:
        xpos 1120
        xsize 520
        ysize 180
        padding (0, 0)
        vbox:
            xpos 50
            yalign 0.5
            text _("Character") size 60 font "font/DAGGERSQUARE.otf" color (0, 246, 255)

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Anya?") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            yalign 1.9
            text _("Age - ??") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            yalign 2.6
            text _("Height - 173 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            yalign 3.3
            text _("Weight - 64 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        if death_anya == 0:
            vbox:
                xpos 60
                yalign 4.0
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        else:
            vbox:
                xpos 60
                yalign 4.0
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        # vbox:
        #     xpos 60
        #     ypos 590


        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            

    imagebutton:
        idle "gui/ANEXT.png" hover "gui/BNEXT.png"
        action [Play("menu_click", "audio/UItaps.mp3"),Hide("anya2"), ShowMenu("anya1")]
        at test_anim_not
        xpos 30
        ypos 760
        focus_mask True
        style "navigation_button"
        hover_sound "audio/CLS.ogg"

screen olivia1:

    modal False
    style_prefix "ground"

    tag profile_menu 

    imagemap:
        ground "gui/characters/olivia1.png"
        hover "gui/characters/olivia2.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 
    

    frame:
        add "gui/characters/profile_menu2.png" 

    vbox:
        xpos 1320
        ypos 180
        text _("Character") size 60 font "font/DAGGERSQUARE.otf" color "#6f542c"


    frame:

        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара


        xpos 1320
        ypos 270
        xsize 530
        ysize 670

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Olivia") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Age - 39") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Height - 159 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weight - 54 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if death_olivia == 0:
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

            else:
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("If you can`t fly - run, if") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("you can`t run - walk, if") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("you can`t walk - crawl,") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("but whatever you do -") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("keep moving forward") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)


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


    
            


screen lora1:

    modal False
    style_prefix "ground"

    tag profile_menu 

    imagemap:
        ground "gui/characters/lora1.png"
        hover "gui/characters/lora2.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    frame:
        add "gui/characters/profile_menu2.png" 

    vbox:
        xpos 1320
        ypos 180
        text _("Character") size 60 font "font/DAGGERSQUARE.otf" color "#6f542c"


    frame:

        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара


        xpos 1320
        ypos 270
        xsize 530
        ysize 670

        
        

    
        vbox:
            xpos 60
            yalign 1.2
            text _("Name Lora") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Age - 41") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Height - 165 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weight - 57 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if death_lora == 1:
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            else:
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Live like gonna die tomorrow.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("Study as if you`ll live") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("forever. Love as if you`ll") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("never know disappointment.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        # vbox:
        #     xpos 60
        #     yalign 1.9
        #     

        # vbox:
        #     xpos 60
        #     yalign 2.6
        #     

        # vbox:
        #     xpos 60
        #     yalign 3.3
        #     

        # if death_lora == 1:
        #     vbox:
        #         xpos 60
        #         yalign 4.0
        #         

        # else:
        #     vbox:
        #         xpos 60
        #         yalign 4.0
        #         

        # vbox:
        #     xpos 60
        #     ypos 590

        #     
        #     
        #     
        #     

            
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


screen shiya1:

    modal False
    style_prefix "ground"

    frame:
        add "gui/characters/profile_menu2.png" 

    frame:

        

        xpos 1260
        ypos 120
        xsize 520
        ysize 180
        padding (0, 0)
        vbox:
            xpos 50
            yalign 0.5
            text _("Character") size 60 font "font/DAGGERSQUARE.otf" color (0, 246, 255)

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Shiya") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            yalign 1.9
            text _("Age - 31") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            yalign 2.6
            text _("Height - 167 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            yalign 3.3
            text _("Weight - 59 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        
        if death_shiya == 0:
            vbox:
                xpos 60
                yalign 4.0
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        else:
            vbox:
                xpos 60
                yalign 4.0
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        vbox:
            xpos 60
            ypos 590

            text _("Don`t let anyone tell you") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("that you can`t. No one") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("can limit your dreams") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("but yourself") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            

    imagebutton:
        idle "gui/ANEXT.png" hover "gui/BNEXT.png"
        action [Play("menu_click", "audio/UItaps.mp3"),Hide("shiya1"), ShowMenu("profile_menu")]
        at test_anim_not
        xpos 30
        ypos 760
        focus_mask True
        style "navigation_button"
        hover_sound "audio/CLS.ogg"

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



screen miriel1:

    modal False
    style_prefix "ground"

    tag profile_menu 

    imagemap:
        ground "gui/characters/miriel1.png"
        hover "gui/characters/miriel2.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    frame:
        add "gui/characters/profile_menu2.png" 

    vbox:
            xpos 1320
            ypos 180
            text _("Character") size 60 font "font/DAGGERSQUARE.otf" color "#6f542c"


    frame:

        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара


        xpos 1320
        ypos 270
        xsize 530
        ysize 670

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Miriel") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Age - 160") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("(27 by human standards)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Height - 160 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weight - ?? kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if death_miriel == 0:
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            else:
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("A home built on love and understanding is stronger than any fortress.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            
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


screen flora1:

    modal False
    style_prefix "ground"

    tag profile_menu 

    imagemap:
        ground "gui/characters/flora1.png"
        hover "gui/characters/flora2.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    frame:
        add "gui/characters/profile_menu2.png" 

    vbox:
            xpos 1320
            ypos 180
            text _("Character") size 60 font "font/DAGGERSQUARE.otf" color "#6f542c"


    frame:

        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара


        xpos 1320
        ypos 270
        xsize 530
        ysize 670

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Flora") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Age - 26") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Height - 178 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weight - 78 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        
            if death_flora == 0:
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            else:
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Oh, the human mind is a marvelous thing!") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("It allows one to find excuses for any stupidity they consider genius.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            

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



screen kalestra1:

    modal False
    style_prefix "ground"

    tag profile_menu 

    imagemap:
        ground "gui/characters/kalestra1.png"
        hover "gui/characters/kalestra2.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")] 

    frame:
        add "gui/characters/profile_menu2.png" 

    vbox:
            xpos 1320
            ypos 180
            text _("Character") size 60 font "font/DAGGERSQUARE.otf" color "#6f542c"


    frame:

        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара


        xpos 1320
        ypos 270
        xsize 530
        ysize 670

        vbox:
            xpos 60
            yalign 1.2
            text _("Name Kalestra") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Age - 35") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Height - 178 cm") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weight - 82 kg") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        
            if death_flora == 0:
                text _("Status - Alive") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

            else:
                text _("Status - (???)") size 50 font "font/DAGGERSQUARE.otf" color (255, 255, 255)

            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Mercy is a luxury for the weak.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            text _("I was forged in fire, and I will rule with it.") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
        #     text _("SSSSSSSSSSSSSSSSSSSSSSSSS") size 40 font "font/DAGGERSQUARE.otf" color (255, 255, 255)
            
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
