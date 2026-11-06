
define persistent.inquisitor_access = 1

screen codex_menu:
    

    tag profile_menu

    modal False
    style_prefix "ground"

    imagemap:
        ground "gui/MainMenu/codex1.png"
        hover "gui/MainMenu/codex.png"

        hotspot (710,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"),  ShowMenu("replay")]
        hotspot (873,47,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("profile_menu")]
        hotspot (1038,50,165,90) action [Play("menu_click", "audio/UItaps.mp3"), Hide("codex_men"), Hide ("menu_codex"), ShowMenu("codex_menu")]  

    frame:
        add "gui/MainMenu/codexfram1.png" 

    vbox:
        xpos 190
        ypos 270
            
        if persistent.inquisitor_access == 1:
            text _("Clearance Levels: I") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        elif persistent.inquisitor_access == 2:
            text _("Clearance Levels: II") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        elif persistent.inquisitor_access == 3:
            text _("Clearance Levels: III") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        elif persistent.inquisitor_access == 4:
            text _("Clearance Levels: IV") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        elif persistent.inquisitor_access == 5:
            text _("Clearance Levels: V") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        elif persistent.inquisitor_access == 6:
            text _("Clearance Levels: VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"



    frame:
        xalign 0.058
        yalign 0.6

        has viewport
        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 650
        ysize 400

        

        grid 2 8:
            
            xspacing 0
            
            fixed:
                xysize (320, 174)
                imagebutton:
                    idle "gui/MainMenu/ranksystem_A.png"
                    hover "gui/MainMenu/ranksystem_B.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("inqisition_rank_")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            # Это в прологе
            if persistent.energy_c == True:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/energysmall_A.png"
                        hover "gui/MainMenu/energysmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("supplything")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"

            # Это в прологе
            if persistent.warpdrive_memory == True:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/warpdrivesmall_A.png"
                        hover "gui/MainMenu/warpdrivesmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("warp_drive_screen")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"


            
            # Это в Акте 1
            if persistent.tomb_screen_ == True:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/tombsmall_A.png"
                        hover "gui/MainMenu/tombsmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("tomb_screen")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"

            # Это в Акте 1
            if persistent.ark_origin_ == True:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/arksmall_A.png"
                        hover "gui/MainMenu/arksmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("ark_origin")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"
                
            # # Это в акте 1
            if persistent.mutants_screen_ == True:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/mutantsmall_A.png"
                        hover "gui/MainMenu/mutantsmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("mutants_screen")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"
            
            # # Это в акте 1
            if persistent.parallel_threads_ == True:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/parallelthreadsmall_A.png"
                        hover "gui/MainMenu/parallelthreadsmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("parallel_threads_")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"

            # # Это в Акте 2

            if persistent.ancient_blood_ == True:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/ancientsmall_A.png"
                        hover "gui/MainMenu/ancientsmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("ancient_blood")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"

            

            # # Это в акте 4
            if persistent.inquisitor_screen_ == True:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/inqusitionsmall_A.png"
                        hover "gui/MainMenu/inqusitionsmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Inquisition")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"


            # # Это в акте 4
            if persistent.keepers_screen_ == True:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/keepersmall_A.png"
                        hover "gui/MainMenu/keepersmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Keepers_1")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"

            # # Это в акте 4

            if persistent.abyss_screen_ == True:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/abyssmall_A.png"
                        hover "gui/MainMenu/abyssmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Abyss")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"

            # # Это в акте 3

            if persistent.gate_screen_ == True:
                
                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/gatesmall_A.png"
                        hover "gui/MainMenu/gatesmall_B.png"
                        action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Gate")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

            else:

                fixed:
                    xysize (320, 174)
                    imagebutton:
                        idle "gui/MainMenu/nnsmall_A.png"
                        style "navigation_button"


            # # Это в акте 5
            fixed:
                xysize (320, 174)
                imagebutton:
                    idle "gui/MainMenu/nnsmall_A.png"
                    # hover "gui/MainMenu/keepersmall_B.png"
                    # action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Keepers_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            fixed:
                xysize (320, 174)
                imagebutton:
                    idle "gui/MainMenu/nnsmall_A.png"
                    # hover "gui/MainMenu/keepersmall_B.png"
                    # action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Keepers_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            fixed:
                xysize (320, 174)
                imagebutton:
                    idle "gui/MainMenu/nnsmall_A.png"
                    # hover "gui/MainMenu/keepersmall_B.png"
                    # action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Keepers_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            fixed:
                xysize (320, 174)
                imagebutton:
                    idle "gui/MainMenu/nnsmall_A.png"
                    # hover "gui/MainMenu/keepersmall_B.png"
                    # action [Play("menu_click", "audio/buttonsounds1.mp3"), ShowMenu("Keepers_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"




    # frame:
            
    #         background None
    #         has vbox

    #         if persistent.preview:
    #             add persistent.preview at fade_in

    # imagebutton:
                                
    #     idle "gui/codex/FRACTIONA.png"
    #     hover "gui/codex/FRACTIONB.png"
    #     action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("fraction"), Hide("race")]
    #     ypos 270
    #     xpos 20
    #     focus_mask True
    #     style "navigation_button"
    #     hover_sound "audio/CLS.ogg"

    # imagebutton:
                                
    #     idle "gui/codex/RACEA.png"
    #     hover "gui/codex/RACEAB.png"
    #     action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("race"), Hide("fraction")]
    #     ypos 370
    #     xpos 20
    #     focus_mask True
    #     style "navigation_button"
    #     hover_sound "audio/CLS.ogg"

    # imagebutton:
                                
    #     idle "gui/codex/MAPA.png"
    #     hover "gui/codex/MAPB.png"
    #     action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("maps_screen"), Hide("fraction")]
    #     ypos 470
    #     xpos 20
    #     focus_mask True
    #     style "navigation_button"
    #     hover_sound "audio/CLS.ogg"

    # imagebutton:
                                
    #     idle "gui/codex/RANKSYSTEMA.png"
    #     hover "gui/codex/RANKSYSTEMB.png"
    #     action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("rank_system"), Hide("fraction")]
    #     ypos 570
    #     xpos 20
    #     focus_mask True
    #     style "navigation_button"
    #     hover_sound "audio/CLS.ogg"

    # imagebutton:
                                
    #     idle "gui/codex/OTHERA.png"
    #     hover "gui/codex/OTHERB.png"
    #     action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("mc_info"), Hide("fraction")]
    #     ypos 670
    #     xpos 20
    #     focus_mask True
    #     style "navigation_button"
    #     hover_sound "audio/CLS.ogg"

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



    
            




define mc_knowledge = 0
define arkconf = 0
define persistent.arkoflight = 0
define persistent.astraldominion = 0
define persistent.ominionsyndycate = 0
define persistent.reliccoalition = 0
define persistent.freelegion = 0
# define vara_cloud = 1
# define phalanx_of_eridanus = 1
# define zeta_prime_hegemony = 1
# define the_phobos_triumvirate = 1
# define aratan_dynasty = 1
# define light_of_the_abyss = 1
# define order_of_aurelius = 1

screen fraction:
    tag codex_men
    frame:


        ypos 270
        xpos 350

        xsize 350
        ysize 630
        
        has viewport
        scrollbars "vertical" 
        mousewheel True
        vbox:

            if persistent.arkconf == 2:
                imagebutton:
                                        
                    idle "gui/codex/ARKCONFA.png"
                    hover "gui/codex/ARKCONFB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("arkconfederation")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                
            else:

                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                

            if persistent.arkoflight == 2:

                imagebutton:
                                        
                    idle "gui/codex/ARKOFLIGHTA.png"
                    hover "gui/codex/ARKOFLIGHTB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("arkoflight_example")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                
            else:
                

                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                    
            if persistent.astraldominion == 2:

                imagebutton:
                                        
                    idle "gui/codex/ASTRALDOMINIONA.png"
                    hover "gui/codex/ASTRALDOMINIONB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("astraldominion_example")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                
            else:

                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if persistent.ominionsyndycate == 2:

                imagebutton:
                                        
                    idle "gui/codex/OMINIONSYNDICATEA.png"
                    hover "gui/codex/OMINIONSYNDICATEB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("ominionsyndycate_example")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                
            else:

                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                

            if persistent.reliccoalition == 2:

                imagebutton:
                                        
                    idle "gui/codex/RELICCOALITIONA.png"
                    hover "gui/codex/RELICCOALITIONB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("mc1")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                
                    
            else:

                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                

            if persistent.freelegion == 2:

                imagebutton:
                                        
                    idle "gui/codex/FREELEGIONSA.png"
                    hover "gui/codex/FREELEGIONSB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("mc1")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                
                    
            else:

                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
                

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            

screen arkconfederation:
    tag menu_codex
    frame:
        add "gui/codex/ARKCONF_EXAMPLE.png" 

    vbox:
        spacing 10
        xpos 830
        ypos 250
            
        text _("Arks Confederation") size 45 font "font/DAGGERSQUARE.otf" color (0,246,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("Human Federation") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("4# in technology") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("8# in military") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 830
        ypos 520
        xsize 970
        ysize 400

        vbox:
            
            text _("Political System:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Confederation of Arks is a federal alliance of multiple star systems, each retaining partial autonomy while adhering to a common democratic council.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The governing body is the Confederate Senate, where representatives from various systems debate laws, diplomatic relations, and military strategies.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

            text _("Economy:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Confederation has a mixed economy, where corporate conglomerates interact with state institutions.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("With its highly developed infrastructure and advanced technologies, Arks plays a crucial role in interstellar trade.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            
            text _("Military and Security:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("While the Confederation upholds democratic values, it maintains a powerful fleet and a sophisticated security network.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Due to its openness, it is vulnerable to espionage and internal conflicts, making intelligence agencies and special forces highly influential.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

            text _("Ideology and Culture:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Confederation prides itself on freedom, equality, and the right to vote, but disputes among different worlds often lead to political struggles and even localized crises.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Unlike totalitarian empires, Arks relies on diplomatic solutions, though it does not always avoid armed conflicts.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

screen ominionsyndycate_example:
    tag menu_codex
    frame:
        add "gui/codex/OMINIONSYNDICATE_EXAMPLE.png" 

    vbox:
        spacing 10
        xpos 830
        ypos 250
            
        text _("Omnion Syndicate") size 45 font "font/DAGGERSQUARE.otf" color (0,246,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("Mutant Federation") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("9# in technology") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("6# in military") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 830
        ypos 520
        xsize 970
        ysize 400

        vbox:
            
            text _("Political System:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("At the top of the organization is the mysterious Omnion Council, a group of powerful figures whose identities are hidden even from their most loyal operatives.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Beneath them, the Syndicate operates through a {b}clan{/b} system, where different groups specialize in various criminal enterprises:") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Smugglers – Handle the transportation of illegal goods, weapons, narcotics, and rare technology.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Assassins & Special Ops – Eliminate rivals, engage in blackmail, and conduct hostile takeovers.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Hackers & Information Brokers – Control financial flows, conduct cyber-espionage, and manipulate data.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Corrupt Officials & {b}White-Collar{/b} Operatives – Influence politics, lobby for Syndicate interests, and launder money through legal fronts.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)


            text _("Economy:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Omnion functions as a shadow economy, moving vast amounts of illicit credits through hidden financial networks.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("They invest in legal businesses, laundering their wealth through banks, tech corporations, and even political organizations.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Beyond finances, the Syndicate controls entire planets and space stations, where official governments are either bribed, compromised, or completely absent. In these territories, only Omnion’s law applies.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)


            text _("Ideology and Culture:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Despite its criminal nature, Omnion operates under strict hierarchy and internal codes:") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}Power is greater than law{/b} – Anyone cunning, ruthless, and ambitious enough can rise through the ranks.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}Money rules all{/b} – The Syndicate has no ideology; profit matters more than morality.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}No friends, only interests{/b} – Loyalty is temporary, and betrayal is part of the game.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

screen astraldominion_example:
    tag menu_codex
    frame:
        add "gui/codex/ASTRALDOMINION_EXAMPLE.png" 

    vbox:
        spacing 10
        xpos 830
        ypos 250
            
        text _("Astral Dominion") size 45 font "font/DAGGERSQUARE.otf" color (0,246,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("Elf Federation") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("3# in technology") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("1# in military") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 830
        ypos 520
        xsize 970
        ysize 400

        vbox:
            
            text _("Political System:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The empire is ruled by the Supreme Emperor, an absolute dictator who is worshiped as a divine figure.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("His rule is enforced by the Astral Council, composed of high-ranking military leaders, administrators, and high priests of the state ideology.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Dominion operates under a strict military hierarchy and demands unquestioning loyalty:") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Legions of Conquest – Elite armies that push the empire’s borders forward.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Orders of Control – Secret police and intelligence agencies that eliminate internal threats.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Caste System – Citizens are divided into rigid social classes, where the higher castes rule, and the lower castes serve.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)


            text _("Economy:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The economy of the Astral Dominion is built on resource exploitation, colonization, and forced labor.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Conquered worlds are turned into production hubs, feeding the empire’s war machine.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Beyond military strength, the Dominion wields propaganda and religious doctrine to maintain control.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The population is taught that expansion is a divine mandate, and resistance is heresy and treason.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)



            text _("Ideology and Culture:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Dominion views democracies, criminal syndicates, and independent systems as chaos — a disorder that must be destroyed or assimilated.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}Might makes right{/b} – The weak must submit to the strong.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}The galaxy must be united{/b} – But only under the Dominion’s iron rule.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}The Emperor is perfection incarnate{/b} – A cult of personality that justifies any conquest.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

screen arkoflight_example:
    tag menu_codex
    frame:
        add "gui/codex/ARKOFLIGHT_EXAMPLE.png" 

    vbox:
        spacing 10
        xpos 830
        ypos 250
            
        text _("Ark of Light") size 45 font "font/DAGGERSQUARE.otf" color (0,246,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("Orks Federation") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("5# in technology") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("7# in military") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 830
        ypos 520
        xsize 970
        ysize 400

        vbox:
            
            text _("Political System:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("At the head of the cult is the Grand Seer, a spiritual leader who claims to receive divine revelations.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Beneath them is the Council of Prophets, who interpret sacred texts and direct the cult’s actions.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Ark is organized into hierarchical orders, each with a specific role:") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Pilgrims of Light – Ordinary believers who serve the cult, spread its teachings, and participate in rituals.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Hosts of Purity – Fanatical warriors willing to die for the Ark’s ideals, leading {b}holy crusades{/b} to exterminate heretics.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Flames of Cleansing – Inquisitors and priests who judge and purge nonbelievers and defectors.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Heralds of Revelation – Missionaries and diplomats who spread the Ark’s word, often using deception and bribery.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)



            text _("Economy:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Ark of Light does not seek wealth, but it thrives on conquest, plunder, and donations from fervent followers.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("They seize technology, resources, and even captives, all repurposed for their {b}holy mission.{/b}") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Their influence spreads like a plague, infiltrating societies through hidden cults, sermons, and ideological subversion.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("On many worlds, the Ark corrupts from within, converting populations before launching full-scale {b}purification{/b} campaigns.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)



            text _("Ideology and Culture:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Ark of Light believes that only their doctrine can save the galaxy. They despise democracies, criminals, and even empires, seeing them as manifestations of chaos and corruption.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}Light must banish darkness{/b} – Any society that does not follow their path must be {b}cleansed.{b}") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}Heresy is a disease{/b} – Even the slightest doubt or deviation is punishable by death.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("{b}The Path of Revelation is the only truth{/b} – All other ideologies, religions, and governments are false.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)




screen race:
    tag codex_men
    frame:


        ypos 270
        xpos 350

        xsize 350
        ysize 630
        
        has viewport
        scrollbars "vertical" 
        mousewheel True
        vbox:

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

screen maps_screen:
    tag codex_men
    frame:


        ypos 270
        xpos 350

        xsize 350
        ysize 630

        vbox:

            imagebutton:
                                        
                    idle "gui/codex/GALAXYMAPA.png"
                    hover "gui/codex/GALAXYMAPB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("map_screen")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

define galaxymapupdated = 1

screen Inquisition():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Classified Section. Clearance Level: I–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Document: Report № INQ–0/II") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subject: The Federation Inquisition") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Active") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("I. General Provisions") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Federation Inquisition is an elite, specialized unit of galactic scale, tasked with functions of protection, strategic intelligence, scientific research operations, counterterrorism, and the elimination of exceptionally dangerous entities posing an existential threat to the Federation and its interests.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Inquisition possesses extended authorities approaching absolute scope and holds recognized authority both within the Federation and beyond its borders. The unit is formally incorporated into the structure of the Galactic Special Forces Bureau, while retaining full autonomy in decision-making.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("II. Origin and Status") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Inquisition was established by personal initiative and under the direct patronage of Lady Evrelia.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Its doctrine, structure, and operational principles are codified as a direct reflection of the Foundress’s will and are not subject to revision without authorization of the highest level.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The formal strength of the unit is 20,000 active operatives, which by galactic standards is classified as a strategically insignificant contingent. The actual operational effectiveness of the Inquisition fully compensates for its numerical limitations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("III. Personnel Composition") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Each inquisitor is the result of multi-stage selection and bioengineering modification.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Personnel are equipped with a full spectrum of implant systems, including but not limited to:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("neurosensory modules for reading and analyzing cognitive patterns;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("regenerative and self-repairing systems;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("combat enhancers of physical performance and reactive capabilities;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("integration with analytical AI clusters.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("A single inquisitor is classified as an autonomous suppression unit, capable of independently neutralizing from several hundred to several thousand hostile targets, depending on operational conditions.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Funding and Service Status") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Inquisitors constitute the most expensive assets of the Federation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Funding includes:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("exceptional remuneration;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("full material provision;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("priority access to resources, technologies, and medical support.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Actual use of monetary resources by personnel is minimal.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Reason: service in the Inquisition is lifelong.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Inquisitors are prohibited from:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("forming families;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("entering hereditary or kinship obligations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("developing unauthorized personal attachments.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Thus, all invested resources de facto remain within the Federation system.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. Terms and Conditions of Service") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Service in the Inquisition begins at the moment of activation and ends exclusively with the death of the subject.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Voluntary withdrawal, retirement, or refusal to fulfill duties is impossible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Given the clearance level, responsibility, and potential risks, the Inquisition classifies each of its members as a non-recoverable resource.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Conclusion") size 32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Federation Inquisition is neither an army nor a law enforcement agency.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("It is an instrument of final resolution, intended for situations in which other mechanisms lose effectiveness.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The existence of the Inquisition guarantees the stability of the Federation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("At the same time, its presence serves as a reminder:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the limits of permissibility are defined not by law, but by the necessity of system survival.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
screen Abyss():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Classified Archive. Clearance Level: III–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        vbox:

            text _("Document: Report № ABYSS–II/13") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subject: Object «The Abyss»") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Official existence unrecognized") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("I. General Overview") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The object, provisionally designated as «The Abyss», is classified in the public domain as myth, folklore horror, or a component of conspiracy theories.  ") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Among the general population, belief in the existence of The Abyss is entirely absent.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("A different situation exists within higher echelons of power. Heads of federations and representatives of the upper strata possess fragmentary knowledge regarding The Abyss and consider it a potential source of unique information.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("II. Level of Awareness") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("A widely circulated rumor among elites asserts that The Abyss contains knowledge capable of sustaining continuity of consciousness, erroneously interpreted as immortality.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Consequently, numerous attempts have been documented to:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("identify access pathways;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("restore lost navigational data;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("activate ancient gates of unknown origin.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Accurate information regarding the true nature of The Abyss is known to an extremely limited number of individuals (see Appendix VI).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("III. Spatial Nature of the Object") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Abyss represents an isolated fragment of a star system, consisting of 13 planets, each containing remnants of the Ancient Empire's civilization.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Structurally, the object is analogous to the Solar System, but it exists in a distant future stage of its evolutionary cycle:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the central star is absent;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("planets lack a light source;;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the system's thermal equilibrium is stable and does not conform to known physical models.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The object is isolated from the galaxy at large, evades standard observation, and disrupts cause-and-effect temporal sequences.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Effectively, The Abyss is classified as a separate world, localized within a closed sector of the galaxy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Access is only possible through the use of Ancient Gates (success is not guaranteed).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Origin") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Abyss is the result of a failed experiment by the Ancient Empire, related to temporal manipulation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("According to reconstructed data:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the experiment was sanctioned by the empire's highest authority;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("its objective was to overcome the finiteness of existence;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the experiment utilized the Astreon System to manipulate time;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the outcome was the collapse of the entire civilization.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ancient Empire ceased to exist entirely.  ") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("No subject survived or exited the experimental zone.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Abyss is classified as a failure caused by greedy ambition and the transgression of permissible limits.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. Principle of So-Called «Immortality»") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The key mechanism, erroneously interpreted as a path to eternal life, is designated as the «Resurrection Point.»") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("upon the death of a subject, physical form is restored;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("each subsequent activation shifts the Resurrection Point closer to the moment of final collapse (Death);") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the process is irreversible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Therefore:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("immortality is a limited and diminishing resource;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("ultimate death is inevitable;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the mechanism is ineffective for achieving true eternal life.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("This fact is concealed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Verified information on the nature of the Resurrection Point is known to no more than a few subjects galaxy-wide.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Each activation of the Resurrection Point consumes energy equivalent to a concentration of Ancient Blood, limiting the number of possible restorations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Conclusion") size 32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Abyss is not a repository of knowledge and does not represent an evolutionary advancement.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("It is the vestige of a catastrophe left behind by a civilization that decided limits could be ignored.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Dissemination of information regarding the true nature of The Abyss is classified as a threat to systemic stability.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Codex Recommendations:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("maintain myth status;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("control access to gates;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("eliminate attempts at unauthorized investigation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


screen Keepers_1():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Closed Archive. Clearance Level: IV–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Document: Report № KEEP–ORIGIN/II") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subject: Class «Keeper» Entities") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Active. Origin Classified") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("I. General Overview") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Keepers are autonomous high-order entities tasked with overseeing the stability of the galactic system and enforcing the preservation of the so-called Balance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Their activity is not directed toward the protection of individual states,species, or civilizations, but toward maintaining the long-term structural integrity of the galaxy as a whole.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("II. Nature and Limitations") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Keepers possess significant resources and power, granting them substantial influence over galaxy-level political processes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("However:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the Keepers are not an absolute force;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("they are mortal;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("their physical destruction is possible, though it requires expenditures deemed strategically unjustified.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The presence of vulnerability is documented and considered acceptable within the framework of Balance preservation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("III. Principles of Intervention") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Intervention by the Keepers is strictly limited in nature.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("They:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("do not participate in local conflicts;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("do not prevent wars or mass casualties;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("do not interfere in confrontations that possess internal, self-sustaining causes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The criterion for intervention is not the scale of violence, but the degree of threat posed to the integrity of the Balance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            if persistent.fallen_empire_ == True:

                text _("IV. Origin (Restricted Classification)") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The Keepers are former members of the fallen Ancient Empire.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("This fact is:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("not officially confirmed;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("prohibited from dissemination;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("recorded within the closed Codex archives as critically significant.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their continued existence is regarded as a consequence of the catastrophe that led to the disappearanceof the Ancient Empire.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
            else:

                text _("IV. Origin (Restricted Classification)") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens at the end of the fifth act.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The Keepers are former members of the fallen Ancient Empire.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("This fact is:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("not officially confirmed;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("prohibited from dissemination;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("recorded within the closed Codex archives as critically significant.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their continued existence is regarded as a consequence of the catastrophe that led to the disappearanceof the Ancient Empire.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            text _("V. Stance Toward the Ancient Legacy") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any activity associated with:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("research into the Ancient Empire;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("restoration of its technologies;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("reference to or study of its legacy, is suppressed by the Keepers immediately and without deliberation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("This protocol requires no justification and is executed automatically.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Interaction with Federations") size 32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Keepers exercise heightened caution toward:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("heads of federations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("major political conglomerates;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("federations as systemic nodes of the Balance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The destruction of an entire federation is classified as an event with excessive consequences capable of destabilizing galactic equilibrium.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In isolated cases, the Keepers permit:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("individual breaches of prohibitions;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("personal research of Ancient Empire ruins by heads of federations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("provided that such actions do not exceed the acceptable risk threshold.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VII. Threshold of Acceptability") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("A critical boundary exists, beyond which:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("preservation of a federation becomes less significant than restoration of Balance;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("its destruction is deemed justified.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The exact formulation of this threshold is unknown.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("No warning is issued prior to intervention.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
            if persistent.fallen_empire_ == True:

                text _("VIII. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The Keepers are not judges, saviors, nor rulers of the galaxy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("They are remnants of a civilization that outlived its own end, acting as regulators seeking to prevent the recurrence of catastrophe.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Balance, to the Keepers, is not an ideal.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("It is a form of atonement.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            else: 

                text _("VIII. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens at the end of the fifth act.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The Keepers are not judges, saviors, nor rulers of the galaxy.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("They are remnants of a civilization that outlived its own end, acting as regulators seeking to prevent the recurrence of catastrophe.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Balance, to the Keepers, is not an ideal.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("It is a form of atonement.") size  28 font "Cybertron.otf" color (255,255,255)


    
screen Gate():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Closed Archive. Clearance Level: V–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Document: Report № GATE–AST/14") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subject: Object «Ancient Gates»") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Prohibited from Operation") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. Purpose and Origin") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ancient Gates are entry mechanisms to the Astreon System, designed for instantaneous transfer of matter, military units, and resources across intergalactic distances.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The technology was developed by the Ancient Empire for the purposes of:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("strategic deployment of armed forces;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("transport of mineral and industrial resources from remote regions of the galaxy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Due to the extreme complexity of construction and exceptional energy requirements, the use of the Gates has been strictly limited since their creation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. Portal Network Structure") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Within the galaxy, fourteen primary portals have been recorded, interconnected into a single closed network.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("These primary portals served as the basis for secondary, lower-capacity connectors.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Each federation possesses at least one primary portal within its jurisdiction.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Certain federations maintain multiple objects of this type.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III. Legal Status") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Despite their strategic value, the operation of the Ancient Gates is categorically prohibited by:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("resolution of the Galactic Council;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("direct decree of the Keepers.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Threat Classification: galactic scale.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any attempt at activation is considered a crime against the stability of the entire galactic system.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Energy Principle") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Gates are powered by a substance provisionally designated as the “Blood of the Ancients.”") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("produced exclusively from living organisms;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("requires sacrifices in quantities classified as absurd even by the standards of eras defined by continuous warfare;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("lacks alternative sources or substitutes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Use of the Gates entails mass and purposeful extermination of living beings, which constitutes the primary reason for the total prohibition of the technology.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. Connection to the Object “Abyss”") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("It has been established that the Ancient Gates provide access to the object “Abyss.”") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Access Conditions:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("proper portal configuration;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("knowledge of the approximate temporal period of the Abyss’s existence, or") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("prior personal presence of the subject within the Abyss.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Activation of the Gates requires an immense and instantaneous release of energy, surpassing any standard galactic energy protocols.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The magnitude of consumption directly correlates with the size and mass of transferred matter.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Mismanagement or insufficient energy supply results in immediate catastrophic failure of the portal and surrounding systems.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Accidental or unqualified activation is impossible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Conclusion") size 32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ancient Gates constitute:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the legacy of the Ancient Empire’s expansionist policy;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("a mechanism based on the direct conversion of life into energy;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the key to an object responsible for the disappearance of an entire civilization.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Their existence is acknowledged as unavoidable, but their operation is impermissible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Codex Recommendation:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("maintain strict prohibition;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("limit dissemination of information;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("assign control and oversight to specialized structures (see section INQ).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

# persistent.warpdrive_memory
# persistent.energy_c
define persistent.ancient_blood_ = False
define persistent.tomb_screen_ = False
define persistent.mutants_screen_ = False
define persistent.inquisitor_screen_ = False
define persistent.abyss_screen_ = False
define persistent.gate_screen_ = False
define persistent.keepers_screen_ = False
define persistent.fallen_empire_ = False
define persistent.parallel_threads_ = False
define persistent.ark_origin_ = False

screen supplything():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Closed Archive. Clearance Level: II–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: Legacy of the Ancient Empire") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subsection: Energy Cells of the Ancients") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Extremely Classified / Inquisition Control") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. General Overview") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("During the era of the Ancient Empire, a series of mechanisms were developed for the accumulation, containment, and utilization of colossal volumes of energy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("These mechanisms, collectively designated as Energy Cells of the Ancients, are considered assets of exceptional value to the modern galaxy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("It must be emphasized:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the value of the cells is determined not by their storage capacity, but by their contents.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. Technological Context") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Contemporary galactic technologies have long surpassed the theoretical limits of energy storage achievable during the era of the Ancient Empire.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("However, the Energy Cells of the Ancients remain unique due to the resource they contain, which cannot be reproducednor safely substituted by any known means.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if persistent.ancient_blood_ == True:
                text _("III. Cell Contents") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Energy Cells contain the Blood of the Ancients (see separate Codex Article: “Blood of the Ancients”).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The Blood of the Ancients is classified as:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a prohibited biotechnological resource;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a source of energy of anomalous origin;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a critical component in the operation of multiple Ancient Empire technologies.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Utilization of this resource enables:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("activation of Ancient Gates;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("power supply for galaxy-scale systems;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("circumvention of standard energetic model limitations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("IV. Strategic Significance") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Energy Cells of the Ancients are classified as a resource posing a galactic-level threat.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Primary factors include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the impossibility of lawful reproduction of the Blood of the Ancients;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the colossal volume of sacrifices required for its creation;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("direct violation of fundamental galactic ethical and legal frameworks.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Even by the standards of a galaxy where war and mass extermination have become commonplace, the quantities required to fill a single cell are deemed absurd and unacceptable.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            else: 
                text _("III. Cell Contents") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens at the end of the second act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Energy Cells contain the Blood of the Ancients (see separate Codex Article: “Blood of the Ancients”).") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The Blood of the Ancients is classified as:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("a prohibited biotechnological resource;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("a source of energy of anomalous origin;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("a critical component in the operation of multiple Ancient Empire technologies.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Utilization of this resource enables:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("activation of Ancient Gates;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("power supply for galaxy-scale systems;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("circumvention of standard energetic model limitations.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("IV. Strategic Significance") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens at the end of the second act.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Energy Cells of the Ancients are classified as a resource posing a galactic-level threat.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Primary factors include:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("the impossibility of lawful reproduction of the Blood of the Ancients;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("the colossal volume of sacrifices required for its creation;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("direct violation of fundamental galactic ethical and legal frameworks.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Even by the standards of a galaxy where war and mass extermination have become commonplace, the quantities required to fill a single cell are deemed absurd and unacceptable.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
           
            if persistent.inquisitor_screen_ == True:
                text _("V. Restrictions and Oversight") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Production of the Blood of the Ancients is strictly prohibited.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Utilization of Energy Cells is permitted only under exceptional circumstances, specifically in response to threats of galactic scale.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Any unauthorized storage, possession, or transportation of Energy Cells is classified as a crime against galactic balance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("КOversight is conducted by:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the Inquisition;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the Keepers;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("under direct mandate of the Galactic Council.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VI. Conclusion") size 32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Energy Cells of the Ancients represent:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the legacy of a civilization that exceeded all permissible boundaries;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a source of forbidden energy;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a potential catalyst for catastrophic events.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their continued existence is tolerated solely as an unavoidable consequence of the past, while any attempt to replicate or revive the technologies of the Ancient Empireis classified as unacceptable.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            else:
                text _("V. Restrictions and Oversight") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Production of the Blood of the Ancients is strictly prohibited.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Utilization of Energy Cells is permitted only under exceptional circumstances, specifically in response to threats of galactic scale.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Any unauthorized storage, possession, or transportation of Energy Cells is classified as a crime against galactic balance.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("КOversight is conducted by:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("the Inquisition;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("the Keepers;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("under direct mandate of the Galactic Council.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VI. Conclusion") size 32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Energy Cells of the Ancients represent:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the legacy of a civilization that exceeded all permissible boundaries;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a source of forbidden energy;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a potential catalyst for catastrophic events.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their continued existence is tolerated solely as an unavoidable consequence of the past, while any attempt to replicate or revive the technologies of the Ancient Empireis classified as unacceptable.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

screen tomb_screen():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Classified Archive. Clearance Level: II-VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: Legacy of the Ancient Empire") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subsection: Abandoned Complexes (Unauthorized Designation: «Tombs»)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Inquisition Control / Overseen by the Keepers") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. General Overview") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The abandoned complexes of the Ancient Empire are isolated zones of research, experimentation, and technological development, established during the existence of the Ancient Empire.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("These sites possess exceptional value due to:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("lost knowledge;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("artifacts from the era of the Ancient Empire;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("technologies irreproducible by contemporary civilizations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In the current chronological period, the discovery of a fully intact and unplundered complex is considered an event of extreme rarity and strategic significance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if persistent.inquisitor_screen_ == True:
                text _("II. Classification of Complexes") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("All discovered sites are provisionally divided into three categories:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("1. Lost Complexes") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Sites for which access has been permanently lost.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Causes of loss include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("structural collapse;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("spatial or temporal instability;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("degradation of entry mechanisms.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Practical value: none.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Interest exists solely for theoretical research and archival hypotheses.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("2. Open Complexes") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Complexes previously accessed and studied.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("In the overwhelming majority of cases, they contain no unique technologies.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("All significant findings have either been lost or thoroughly examined.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Note:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Open complexes may hold limited value for:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("minor organizations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("local militias;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("small-scale corporations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The majority of surviving sites to date fall into this category.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("3. Sealed Complexes") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Fully isolated sites, never accessed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Possess enormous strategic and scientific value.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The primary challenge lies not in discovery, but in the process of unsealing.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("III. Unsealing Procedure") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The unsealing of a complex is not an act of access, but an operation to neutralize a potential threat.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("A sealed complex is not a passive object. In most cases, it represents:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("an autonomous ecosystem;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a closed city of the Ancient Empire;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("an environment governed by its own operational, security, and self-maintenance laws.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Potential threats within complexes include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("biological mutations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("uncontrolled viruses;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("degraded lifeforms;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("active defense systems;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("consequences of failed experiments.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Certain complexes are recorded as zones showing signs of extremely cruel or forbidden research.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("IV. Restrictions and Prohibitions") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Unauthorized unsealing of Sealed Complexes is strictly prohibited.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Any actions taken without the sanction of the Keepers are classified as a threat to the galactic balance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Information regarding the discovery of a Sealed Complex must be immediately suppressed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Violations of these provisions will result in:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Inquisition intervention;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("enforced destruction of data;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("elimination of involved personnel.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("V. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The abandoned complexes of the Ancient Empire constitute:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a source of lost knowledge;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("potential epicenters of catastrophic events;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the legacy of a civilization that destroyed itself.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their study is permissible only under conditions of complete control, with priority given to galactic safety over any potential gain.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
            else: 

                text _("II. Classification of Complexes") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("All discovered sites are provisionally divided into three categories:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("1. Lost Complexes") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Sites for which access has been permanently lost.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Causes of loss include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("structural collapse;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("spatial or temporal instability;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("degradation of entry mechanisms.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Practical value: none.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Interest exists solely for theoretical research and archival hypotheses.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("2. Open Complexes") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Complexes previously accessed and studied.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("In the overwhelming majority of cases, they contain no unique technologies.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("All significant findings have either been lost or thoroughly examined.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Note:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Open complexes may hold limited value for:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("minor organizations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("local militias;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("small-scale corporations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The majority of surviving sites to date fall into this category.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("3. Sealed Complexes") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Fully isolated sites, never accessed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Possess enormous strategic and scientific value.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The primary challenge lies not in discovery, but in the process of unsealing.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("III. Unsealing Procedure") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The unsealing of a complex is not an act of access, but an operation to neutralize a potential threat.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("A sealed complex is not a passive object. In most cases, it represents:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("an autonomous ecosystem;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a closed city of the Ancient Empire;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("an environment governed by its own operational, security, and self-maintenance laws.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Potential threats within complexes include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("biological mutations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("uncontrolled viruses;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("degraded lifeforms;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("active defense systems;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("consequences of failed experiments.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Certain complexes are recorded as zones showing signs of extremely cruel or forbidden research.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("IV. Restrictions and Prohibitions") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Unauthorized unsealing of Sealed Complexes is strictly prohibited.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Any actions taken without the sanction of the Keepers are classified as a threat to the galactic balance.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Information regarding the discovery of a Sealed Complex must be immediately suppressed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Violations of these provisions will result in:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Inquisition intervention;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("enforced destruction of data;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("elimination of involved personnel.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("V. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The abandoned complexes of the Ancient Empire constitute:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("a source of lost knowledge;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("potential epicenters of catastrophic events;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the legacy of a civilization that destroyed itself.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their study is permissible only under conditions of complete control, with priority given to galactic safety over any potential gain.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

screen inqisition_rank_():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Rank system.") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. Clearance Levels") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Clearance levels are designated by Greek letters ranging from I to VI.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Each record specifies the minimum and maximum level of access permitted to an object.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I - base level, accessible to the majority of personnel;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II - high-level clearance, accessible to senior officers;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III - very high clearance, restricted access, quarantine or hazardous objects;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV - high clearance, comparable to III, commonly assigned to strategic assets;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V - near-maximum clearance, extremely classified, access limited to a small number of authorized subjects;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI - maximum clearance, absolute restriction, access granted only to special supervisory structures.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Clearance Range Designation") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Entries formatted as “from… to…” define the permitted clearance range.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Example:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II–VI — access permitted from level II to VI (including officers and the Inquisition);") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III–VI — strictly restricted access; lower boundary III, upper boundary VI;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Absolutely Restricted / VI — access fully prohibited, reserved exclusively for supervisory entities.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any interaction with an object outside the established clearance level is classified as a violation of the Galactic Codex and may result in sanctions imposed by the Inquisition.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


screen parallel_threads_():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Classified Archive. Clearance Level: Δ–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: Chronological and Ontological Structures") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subsection: Ontological Deviation") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Observable Phenomenon") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. Definition") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Parallel Threads are autonomous branches of reality that have diverged from the Main Thread of the World.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("By their nature, each thread constitutes:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("an independent universe;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("with its own chain of causality;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("with variations of history, outcomes, and states of matter.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("All threads exist simultaneously and are interconnected within a single ontological system.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. Principle of Divergence") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The formation of parallel threads occurs at moments of critical probability, when reality allows more than one admissible outcome.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("An analogy deemed acceptable for explanatory purposes to lower ranks:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the principle of multiple observational states (see: Astreon paradox).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Each thread records one realized outcome, while all remaining possibilities form separate branches of existence.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III. Degree of World Similarity") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("At early stages of divergence, parallel threads may:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("almost entirely replicate the Main Thread;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("differ only by minor events;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("possess identical territories, individuals, and power structures.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("As temporal distance increases, differences accumulate, leading to radical divergences:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("cultural;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("biological;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("technological;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("existential.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Thread Interconnectivity") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("All threads:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("are not fully isolated;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("exist within a shared chronological framework;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("are subject to indirect influence upon one another.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Destabilization of a single thread may trigger:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("resonant fluctuations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("thinning of boundaries;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("localized temporal ruptures.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. THREAD WEAVERS") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The existence of subjects capable of influencing parallel threads has been recorded.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Official designation: Weavers.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Capabilities") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weavers are capable of:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("perceiving the structure of threads;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("shifting event probabilities;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("strengthening or weakening individual branches;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("in rare cases, initiating divergence.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VII. Limitations") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Weavers do not create threads ex nihilo.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("They operate exclusively within already permissible variants of reality.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Direct intervention:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("requires colossal resources;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("results in degradation of the bearer;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("significantly increases the risk of ontological collapse.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VIII. Weaver Status") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("All Weavers are classified as:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subjects of Elevated Existential Risk.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Observation - mandatory.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Isolation - permissible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Elimination - authorized in the event of a threat to the integrity of the Main Thread.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IX. Codex Warning") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("There is no “better” thread.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("There exists only the one that endured the pressure of time.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any attempt to impose an “ideal outcome” upon reality results in the disintegration of the structure of existence.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("X. Final Provision") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Parallel threads are not an error of creation. They are a consequence of probabilistic freedom.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("However, interference with them is equivalent to interference with the foundation of reality.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The cost of error, the erasure of a world.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)





screen warp_drive_screen():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Closed Archive. Clearance Level: II–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: Technologies of the Ancient Empire / Legacy of Hyperspatial Mechanisms") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subsection: Warp Drive") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Inquisition Oversight / Keeper Surveillance") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. General Description") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("A Warp Drive is a high-technology mechanism capable of transporting objects across vast interstellar distances.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Functionally, it serves as an analogue to the Gates, but on the scale of an individual spacecraft.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Each drive is an autonomous unit and is not integrated into the Astreon System.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Primary limitations include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("restricted operational range;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("high resource consumption, including the Blood of the Ancients;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("a severely limited number of operational units within the galaxy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if persistent.inquisitor_screen_ == True:
                text _("II. History and Purpose") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("A total of approximately one hundred Warp Drives were constructed. Their production was justified by:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the potential necessity to replace the Gate network in the event of system failure;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the strategic value of autonomous interstellar mobility for spacefaring units.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Each vessel requires a variable number of drives depending on its class and dimensions:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("small vessels (single-operator class), up to 3 drives;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("large cruisers or Citadel-class structures, up to one thousand drives per unit.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Despite limited practical application, long-term viability was ensured by comparatively low operational costs relative to alternative technologies.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                
            else:
                text _("II. History and Purpose") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("A total of approximately one hundred Warp Drives were constructed. Their production was justified by:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the potential necessity to replace the Gate network in the event of system failure;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("the strategic value of autonomous interstellar mobility for spacefaring units.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Each vessel requires a variable number of drives depending on its class and dimensions:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("small vessels (single-operator class), up to 3 drives;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("large cruisers or Citadel-class structures, up to one thousand drives per unit.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Despite limited practical application, long-term viability was ensured by comparatively low operational costs relative to alternative technologies.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            if persistent.tomb_screen_ == True:

                text _("III. Current Strategic Relevance") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("In the modern galaxy, Warp Drives possess exceptional strategic value for two primary reasons:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("1. Minimal energy requirements for warpspace transition;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("2. The ability to reconfigure the system for alternative energy sources while preserving warpspace jump functionality, at the cost of reduced output.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            else:   

                text _("III. Current Strategic Relevance") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the first act") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("In the modern galaxy, Warp Drives possess exceptional strategic value for two primary reasons:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("1. Minimal energy requirements for warpspace transition;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("2. The ability to reconfigure the system for alternative energy sources while preserving warpspace jump functionality, at the cost of reduced output.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
            if persistent.inquisitor_screen_ == True:
                text _("IV. Limitations and Hazards") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Operation of Warp Drives involves significant risks:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("navigational precision, required to prevent planetary collision;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("sufficient fuel reserves, depletion during transit results in total structural disintegration;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("probability of entering anomalous zones or Hidden Galaxies, return probability is effectively zero.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Additional data:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("only 37 drives are currently confirmed operational within the galaxy;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("the remaining units are of unknown location;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("each confirmed drive is under continuous surveillance by the Keepers, rendering their use for covert operations or espionage largely ineffective.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("V. Social and Political Status") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Possession of Warp Drives is regarded as a symbol of prestige and technological superiority within the Federation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Any unauthorized use, transfer, or modification of Warp Drives without Keeper authorization is classified as a threat to galactic security and may result in direct Inquisition sanctions.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VI. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Warp Drives are rare and strategically critical mechanisms, combining immense technological value with substantial inherent risk.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their operation is permitted only under full oversight, with galactic security prioritized over tactical or economic advantage.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
            else:
            
                text _("IV. Limitations and Hazards") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Operation of Warp Drives involves significant risks:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("navigational precision, required to prevent planetary collision;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("sufficient fuel reserves, depletion during transit results in total structural disintegration;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("probability of entering anomalous zones or Hidden Galaxies, return probability is effectively zero.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Additional data:") size  28 font "Cybertron.otf" color (255,255,255)
                text _("only 37 drives are currently confirmed operational within the galaxy;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("the remaining units are of unknown location;") size  28 font "Cybertron.otf" color (255,255,255)
                text _("each confirmed drive is under continuous surveillance by the Keepers, rendering their use for covert operations or espionage largely ineffective.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "Cybertron.otf" color (255,255,255)
                text _("V. Social and Political Status") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the fourth act.") size  45 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Possession of Warp Drives is regarded as a symbol of prestige and technological superiority within the Federation.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Any unauthorized use, transfer, or modification of Warp Drives without Keeper authorization is classified as a threat to galactic security and may result in direct Inquisition sanctions.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VI. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Warp Drives are rare and strategically critical mechanisms, combining immense technological value with substantial inherent risk.") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Their operation is permitted only under full oversight, with galactic security prioritized over tactical or economic advantage.") size  28 font "Cybertron.otf" color (255,255,255)




screen the_fallen_empire():
    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Closed Archive. Clearance Level: V–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Document: Report № ANCIENT–HIST/13K") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Subject: The Ancient Empire") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Classified / Extremely Restricted Access") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. General Information") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ancient Empire was a federative entity that governed the galactic system approximately 13,000 years prior to the current chronological reference.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Exact dates and detailed chronology remain unknown.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Existing data is extremely limited and subject to strict classification.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Empire possessed:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("absolute power;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("technologies capable of violating the fundamental laws of the galaxy;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("ambitions extending beyond the natural constraints of life and time.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. Collapse and Catastrophe") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Attempts by the Ancient Empire to develop technology capable of altering or distorting space-time culminated in a catastrophic event.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The implemented device was designated as the Astreon System (internal designation: “time machine”).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Objective: to overcome galactic cyclicity and achieve immortality for the Empire’s population.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Consequence: a massive detonation that divided the galaxy into two distinct regions:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Visible Galaxy, a relatively stable zone, accessible for exploration.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Hidden Galaxy, an anomalous region characterized by temporal distortions, accessible only via Ancient Gates or through possession of specialized knowledge and technologies.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The anomalous region contains “fragments of time from the Terran system” coexisting simultaneously, forming unique chronological conditions.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III. Theories and Restrictions") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("A hypothesis exists suggesting that the catastrophe may have been triggered by military conflict with an external adversary.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("No verified evidence supporting this theory has been recovered.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any research, verification, or attempts to reconstruct or reactivate the system are strictly prohibited and are actively suppressed by the Keepers and the Inquisition.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Consequences for the Modern Galaxy") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Hidden portion of the galaxy generates anomalous zones in which temporal flow differs from standard reference:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Terran-origin entities and objects within the Hidden Zone exist on a decelerated temporal scale relative to the external galaxy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any expedition into anomalous regions requires advanced technologies and access to Ancient Gates.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("All information concerning the Ancient Empire and the Astreon System is classified under the category “Extreme Secrecy.”") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Unauthorized dissemination of information is punishable by data erasure and Inquisition-imposed sanctions.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The impact of the catastrophe persists to the present era:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("anomalies in gravitational and temporal fields;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("residual effects of space-time experimentation;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("persistent risk of renewed activation of the Astreon System.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ancient Empire and the Astreon System constitute:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the origin of multiple galactic anomalies;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("a documented example of civilization-ending ambition;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("objects of maximum secrecy and continuous surveillance by the Keepers and the Inquisition.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any interference with technologies or research related to the Ancient Empire or the Astreon System is strictly prohibited and classified as a direct threat to galactic stability.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)



screen ancient_blood():

    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Closed Archive. Clearance Level IV") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: Prohibited Substances and Existential Threats") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Article: BLOOD OF THE ANCIENTS") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Absolutely Restricted") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. General Description") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Blood of the Ancients is a high-energy processed substance, erroneously referred to as “blood.”") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("By its nature, it is not a biological fluid in the classical sense.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The substance was created during the era of the Ancient Empire and represents a viral-type energy carrier capable of briefly releasing colossal amounts of energy.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Due to the complexity of extraction, instability, and severe side effects, it is classified as a top-tier strategic resource and is employed exclusively under exceptional circumstances.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. Storage and Active Lifespan") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Blood of the Ancients is inherently unstable and possesses a limited active lifespan.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("To prolong storage viability, the substance must be contained within specialized isolating capsules (see: Energy Cells of the Ancient Empire).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Violation of storage conditions results in:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("structural degradation;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("spontaneous energy release;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("contamination of the surrounding environment.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III. Principle of Operation") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Upon application, the Blood of the Ancients integrates into a host object (living organism, mechanism, structure, or artifact — distinctions are non-critical).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In essence, the substance functions as a viral energy form, causing:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("formation of internal microorganisms;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("temporary extreme amplification of the host’s energy potential;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("initiation of irreversible mutational processes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In the short term, the effect may be perceived as enhancement.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In the long term, it results in degradation, destruction, or complete transformation of the host.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Miasma and Mutational Processes") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("During activation, the Blood of the Ancients generates miasma, energy-biological clouds that propagate through living organisms.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Miasma:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("consumes the life force of all biological forms (from microorganisms to sapient species);") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("restructures absorbed matter according to its own framework;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("initiates mutational transformations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The outcome of these processes is the emergence of mutated entities designated as Soulless (see: Soulless and Mutants).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. Military Mutations") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Controlled military mutations utilizing the Blood of the Ancients are:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("extremely rare;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("characterized by a low stabilization success rate;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("incapable of sustaining long-term host survival.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Even a “successful” mutation extends the subject’s existence only for a limited duration (typically from several hours to several days).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Within galactic military practice, such mutations are employed exclusively:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("as a measure of last resort;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("primarily on convicted criminals.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Standard tactical application:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the infected subject is deployed into enemy-controlled territory;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the subject’s direct combat role is secondary;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("the primary effect is produced by miasma propagation following contact.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Countermeasure Methods") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Complete destruction of the Blood of the Ancients is classified as extremely difficult, though not impossible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Effective countermeasures include:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("exposure to extremely low temperatures;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("cryogenic isolation;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("total elimination of viable biological environments.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In the absence of life-energy sources, the substance undergoes autonomous degradation upon expiration of its active lifespan.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VII. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Blood of the Ancients is not a tool of immortality nor a source of absolute power.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("It constitutes a self-propagating weapon of mass destruction, posing an equal threat to both the target and the party attempting to employ it.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Any unauthorized use is classified as a galactic-scale threat and mandates immediate intervention (see: Keeper Protocols).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)

screen mutants_screen():

    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Clearance Level I–VI") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: Biological and Existential Threats") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Article: SOULLESS AND MIASMATIC MUTANTS") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Quarantine Objec") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. Origin") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Soulless entities and related forms are organisms that emerge as a result of miasma exposure, generated by the Blood of the Ancient Empire, acting upon living matter.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The original host is irrelevant:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("humans, other sapient species, animals, microorganisms —") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("all are subject to transformation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The process is irreversible.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. General Functional Principle") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Miasma:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("restructures biological matter;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("consumes vital energy;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("forms a self-sustaining ecosystem independent of the host’s original physiology.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The base behavioral pattern of most mutants resembles primitive predatory lifeforms (commonly and incorrectly classified as “zombies”).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Key distinctions:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("increased physical strength;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("accelerated reaction speed;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("high resistance to damage;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("probability of secondary mutations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III. Mutation Factors") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The probability and type of mutation depend on the following parameters:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("biological nature of the host;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("duration of miasma exposure;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("concentration of miasma within the infected zone.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("As a result, a hierarchical mutant structure is formed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("IV. Soulless Entities") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Soulless entities are not individual organisms, but manifestations of the miasmatic ecosystem itself.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("elimination of one Soulless entity increases the probability of multiple new manifestations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("death of allied organisms accelerates miasma propagation;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("conventional military tactics are classified as ineffective.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Expansion of infected zones occurs exponentially in the presence of viable biological environments.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("V. Classification and Threat Levels") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("1. Soulless (Base Type)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Threat Level: I") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The most widespread form.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("minimal cognitive function;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("primitive behavioral responses;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("primary threat to civilian populations.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Standard military units are capable of neutralization using conventional means.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("2. Ghostclaw") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Threat Level: II") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Mutated form with partial cognitive development.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("limited intelligence;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("high mobility;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("capability for optical camouflage (invisibility).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Primary dangers:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("sudden assaults;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("disruption of defensive formations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("extreme difficulty of detection.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("3. Mimics") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Threat Level: III") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("High-intelligence mutation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("advanced understanding of sapient behavior;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("ability to replicate the external appearance of intelligent beings.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Replication limitations:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("direct visual contact required;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("personal interaction with the copied subject is necessary.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Primary dangers:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("infiltration;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("erosion of trust;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("internal collapse of organized structures.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("4. Strikers") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Threat Level: III") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Heavy mutation class.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("massive physical structure;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("height ranging from 4 to 6 meters;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("reinforced, armored tissue.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Standard small arms are ineffective.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Recommended neutralization measures:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("heavy weaponry;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("grenade launchers (against smaller specimens);") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("armored vehicles (against larger entities).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("5. Distorted Ones") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Threat Level: IV (Maximum)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: Priority Target") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Command-class mutant entities.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Characteristics:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("intelligence comparable to sapient species;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("speech capability;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("control over groups of Soulless entities;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("coordination of miasma expansion.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Distinctive trait:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("all miasmatic resources are redirected to cerebral support;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("loss of extreme physical strength in exchange for strategic capabilities.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Distorted Ones are typically located at the core of infected zones and function as central control nodes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VI. Existential Threat Assessment") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("At early stages, infection may appear to be a localized incident.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The emergence of a Distorted One:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("transitions the situation into an uncontrollable expansion phase;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("renders standard containment measures ineffective;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("requires full-scale military or quarantine intervention.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Delay is unacceptable.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("VII. Conclusion") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Soulless entities and related mutations constitute a self-evolving biological ecosystem, not isolated hostile organisms.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Failure to suppress early-stage outbreaks results in:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("loss of star systems;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("collapse of federations;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("intervention by higher supervisory structures (see: Keeper Protocols).") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            

screen ark_origin():

    tag menu_codex

    vbox:
        spacing 10
        xpos 780
        ypos 250
            
        text _("Clearance Level: III–VI (Absolute)") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
        text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
        

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 780
        ypos 340
        xsize 1000
        ysize 460

        
        vbox:

            text _("Section: ProExistential Anomalies and Lost Objects") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Article: THE ARK") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Status: ⚠️ Prohibited Knowledge") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("I. General Classification") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ark is an object of mythological and existential nature, presumed to have been created by the Ancient Empire in the period preceding the Galactic Schism.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("No confirmed data regarding the existence of the object has been identified.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("All available information is derived from fragmented references, distorted legends, and prohibited archives.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Official status:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Existence unconfirmed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("II. Commonly Accepted Theory") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("(Accessible to civilian and academic institutions)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("According to the prevailing version:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("The Ark was a unique vessel constructed by the Ancient Empire as a means of survival in the event of an apocalypse;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Equipped with a superluminal drive enabling travel at velocities approaching the speed of light;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Classified as a lost relic posing no practical threat.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("This version is acknowledged as incomplete, yet deemed unsuitable for further public investigation.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("III. Forbidden Attribute") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("(Information fragmentary, clearance level IV+)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            if persistent.inquisitor_screen_ == True:
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Certain sources indicate that the Ark’s true uniqueness lay not in the vessel itself, but in the object it carried:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Autonomous Ancient Gates;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Directly integrated into the hull of the ship;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Allowing the Ark alone to interface with the Astreon system outside stationary nodes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("If accurate, the Ark functioned as a mobile node of the Astreon system.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("IV. The Dragonkind Legend") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("(Unverified, classified as myth)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Among ancient draconic clans, the following legend is recorded:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("“When the final hidden Gates are found, from them shall emerge that which will bring an end to the Galaxy.”") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The credibility of this legend remains unconfirmed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Modern historians classify it as an eschatological fear of ancient species.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("V. The Error of Empires") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("(Classified, clearance level VI)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Opens in the middle of the sixth act") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Access denied") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VI. The Truth of the Ancient Empire") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("Opens in the middle of the seventh act") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Access denied") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("{font=font/NotoSansSC-Black.ttf}VII.{/font} The Abyss as a Seal") size  32 font "Cybertron.otf" color "#6f542c"
                text _("Opens at the end of the eighth act") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Access denied") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            
            else: 

                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Certain sources indicate that the Ark’s true uniqueness lay not in the vessel itself, but in the object it carried:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Autonomous Ancient Gates;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Directly integrated into the hull of the ship;") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Allowing the Ark alone to interface with the Astreon system outside stationary nodes.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("If accurate, the Ark functioned as a mobile node of the Astreon system.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("IV. The Dragonkind Legend") size  32 font "font/NotoSansSC-Black.ttf" color "#6f542c"
                text _("(Unverified, classified as myth)") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Among ancient draconic clans, the following legend is recorded:") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("“When the final hidden Gates are found, from them shall emerge that which will bring an end to the Galaxy.”") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("The credibility of this legend remains unconfirmed.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Modern historians classify it as an eschatological fear of ancient species.") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("V. The Error of Empires") size  32 font "Cybertron.otf" color "#6f542c"
                text _("(Classified, clearance level VI)") size  28 font "Cybertron.otf" color (255,255,255)
                text _("Opens in the middle of the sixth act") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Access denied") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VI. The Truth of the Ancient Empire") size  32 font "Cybertron.otf" color "#6f542c"
                text _("Opens in the middle of the seventh act") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Access denied") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("VII. The Abyss as a Seal") size  28 font "Cybertron.otf" color (255,255,255)
                text _("Opens at the end of the eighth act") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)
                text _("Access denied") size  28 font "Cybertron.otf" color (255,255,255)
                text _("") size  28 font "font/NotoSansSC-Black.ttf" color (255,255,255)













screen map_screen():
    tag menu_codex
    frame:
        add "gui/codex/galaxyframe.png" 

    default zoom = 1.0  # Начальный масштаб
    default x_offset = 0
    default y_offset = 0


    frame:
        xpos 783
        ypos 170
        xsize 1070
        ysize 780
        background "#222"  # Цвет фона (можно убрать)
        
        viewport id "map_view":
            child_size (2000, 2000)  # Размер самой карты
            draggable True
            mousewheel True

            # Ограничиваем перемещение внутри окна
            xmaximum 1070
            ymaximum 780

            if galaxymapupdated == 1:
                add Transform("gui/codex/Galaxymap2.png", zoom=zoom)
            
            elif galaxymapupdated == 2:
                add Transform("gui/codex/Galaxymap.png", zoom=zoom)
            
            elif galaxymapupdated == 3:
                add Transform("gui/codex/Galaxymap1.png", zoom=zoom)

    frame:
        add "gui/codex/galaxyframe1.png" 


    # Кнопки управления
    textbutton "Zoom In":
        action SetScreenVariable("zoom", min(zoom + 0.1, 3.0))
        xpos 1050
        ypos 980

    textbutton "Zoom Out":
        action SetScreenVariable("zoom", max(zoom - 0.1, 0.5))
        xpos 1450
        ypos 980


screen popup_image():
    modal False  # Позволяет взаимодействовать с игрой во время показа окна

    image "gui/codex/memoryupdatedtext.png":
        xpos 1200  # Позиция в углу (можно изменить)
        ypos 50
        at popup_animation

    timer 1.0 action Hide("gui/codex/memoryupdatedtext.png")  # Исчезнет через 60 секунд

transform popup_animation:
    alpha 0.0
    easein 0.5 alpha 1.0  # Плавное появление
    pause 59.0
    easeout 0.5 alpha 0.0  # Плавное исчезновение

screen rank_system:
    tag codex_men
    frame:


        ypos 270
        xpos 350

        xsize 350
        ysize 630
        
        has viewport
        scrollbars "vertical" 
        mousewheel True
        vbox:

            if arkconf == 1:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            else:
                imagebutton:
                                        
                    idle "gui/codex/ARKCONFA.png"
                    hover "gui/codex/ARKCONFB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("arkconfederationrank")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

screen arkconfederationrank:
    tag menu_codex
    frame:
        add "gui/codex/ARKCONF_EXAMPLE.png" 

    vbox:
        spacing 10
        xpos 830
        ypos 250
            
        text _("Arks Confederation") size 45 font "font/DAGGERSQUARE.otf" color (0,246,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("Human Federation") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("4# in technology") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("8# in military") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
        text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

    frame:
    
        has viewport  # Первое выражение в блоке frame
        mousewheel True  # Прокрутка колесиком мыши
        draggable True  # Возможность перетаскивания содержимого
        scrollbars "vertical"  # Добавление вертикального скроллбара
        xpos 830
        ypos 520
        xsize 970
        ysize 400
        vbox:
            
            text _("Ranks:") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)

            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("I. Общие положения") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The official leader and face of the Confederation, serving as the highest authority in political and diplomatic affairs.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Oversees the execution of laws and policies across the Confederation.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Represents the Confederation in interstellar diplomacy and negotiations.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Acts as the commander-in-chief during times of war or crisis.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Can veto major decisions but is kept in check by the Council and other branches of power.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

            
            text _("#2 - Left and Right Hands") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The two most powerful advisors to the Representative, often embodying different ideological or political approaches.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Right Hand: Oversees military strategy, security, and law enforcement.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Left Hand: Focuses on economics, diplomacy, and internal affairs.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Both act as executive officers capable of making critical decisions when the Representative is unavailable.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Frequently at odds with each other, ensuring a balance of power.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)


            text _("#3 - The Council") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("A governing body made up of representatives from different systems, acting as the legislative and judicial authority.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Debates and passes laws that affect the entire Confederation.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Balances the power of the Representative and the Left & Right Hands.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Ensures that individual systems retain autonomy while remaining unified.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Controls the allocation of resources and military actions.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Composition:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Includes members from different factions and backgrounds, ensuring that all voices are heard.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Decisions are made through voting and debates.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

            text _("#4 - Scientists") size  28 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The Confederation values scientific progress as one of its pillars, giving scientists considerable influence.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Develop advanced technology, medicine, and infrastructure.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Serve as advisors to the government on technological policies.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Oversee terraforming, AI development, and space exploration.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Often at odds with Religious Fanatics, who resist certain scientific advancements.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Status & Influence:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("While they do not have direct political power, their research impacts almost every aspect of the Confederation’s growth.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The military often relies on scientific breakthroughs for weapons and defense systems.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

            text _("#5 - Religious Fanatics") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Though the Confederation is largely secular, various religious movements hold power within their own domains.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Maintain cultural traditions and spiritual well-being among citizens.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Influence moral and ethical policies, sometimes clashing with scientists over issues like cloning, AI rights, or genetic engineering.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Act as mediators in conflicts between different factions.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Power Struggles:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Some religious groups advocate for peace and unity, while others are more radical, seeking to impose their vision of order.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Constantly debating with scientists and politicians over the future of the Confederation.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)

            text _("#6 - Military Forces") size  28 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The backbone of the Confederation’s defense and expansion, ensuring security from external and internal threats.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Protect the Confederation from external aggressors like the Astral Dominion or Omnion Syndicate.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Maintain law and order in unstable systems.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Conduct covert operations against threats before they escalate.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Structure:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Fleet Command: Oversees interstellar navy and ship deployments.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Ground Forces Command: Manages planetary security and counterinsurgency.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Intelligence Division: Engages in espionage, cyberwarfare, and black ops.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            
            text _("#7 - Administrators") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The unsung heroes (or villains) of the Confederation, ensuring that laws, economies, and societies function smoothly.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Manage interplanetary trade, infrastructure, and logistics.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Enforce taxation, laws, and regulations.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Often hold hidden power, as corruption and political maneuvering are common.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            
            text _("#8 - Criminal Syndicates") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Though the Confederation fights against crime, organized syndicates still hold immense influence in the shadows.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties (or Crimes):") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Control smuggling, black-market trade, and illegal technology.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Bribe politicians, military officers, and even council members.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Act as unofficial power brokers, sometimes more efficient than legal authorities.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Influence & Conflicts:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("While some Syndicates work against the Confederation, others secretly collaborate with high-ranking officials.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("They are a necessary evil, sometimes offering {b}services{/b} that the government cannot officially acknowledge.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)



            text _("#9 - The People") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("The largest and most diverse group, consisting of all ordinary citizens who are not part of the elite classes.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Duties & Rights:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Have the right to vote, protest, and participate in governance.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Consist of workers, traders, explorers, and settlers expanding the frontier.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Are the foundation of the Confederation’s strength, but also the most vulnerable to manipulation by those in power.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Struggles & Movements:") size  28 font "font/DAGGERSQUARE.otf" color (0,240,240)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Some advocate for more power to the people, while others fall under the influence of corporations, cults, or criminal syndicates.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("Periodic uprisings and strikes occur, forcing the government to respond to their demands.") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)


            text _("#Special - Inquisition") size  32 font "font/DAGGERSQUARE.otf" color (0,246,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("??????????????????????????????????????????????????") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("??????????????????????????????????????????????????") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)
            text _("") size  28 font "font/DAGGERSQUARE.otf" color (255,255,255)


screen mc_info:

    
    tag codex_men
    frame:


        ypos 270
        xpos 350

        xsize 350
        ysize 630
        
        has viewport
        scrollbars "vertical" 
        mousewheel True
        vbox:
            
            if mc_knowledge >= 1:
                imagebutton:
                                        
                    idle "gui/codex/KNOWLEDGE1A.png"
                    hover "gui/codex/KNOWLEDGE1B.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 2:
                imagebutton:
                                        
                    idle "gui/codex/MIASMASA.png"
                    hover "gui/codex/MIASMASB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 3:
                imagebutton:
                                        
                    idle "gui/codex/SHARDSA.png"
                    hover "gui/codex/SHARDSB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 4:
                imagebutton:
                                        
                    idle "gui/codex/SLEPISSUEA.png"
                    hover "gui/codex/SLEPISSUEB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 5:
                imagebutton:
                                        
                    idle "gui/codex/SYNDICATEsA.png"
                    hover "gui/codex/SYNDICATEsB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 6:
                imagebutton:
                                        
                    idle "gui/codex/DOWNTOWNA.png"
                    hover "gui/codex/DOWNTOWNB.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 7:
                imagebutton:
                                        
                    idle "gui/codex/KNOWLEDGE1A.png"
                    hover "gui/codex/KNOWLEDGE1B.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            if mc_knowledge >= 8:
                imagebutton:
                                        
                    idle "gui/codex/KNOWLEDGE1A.png"
                    hover "gui/codex/KNOWLEDGE1B.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("war_maiden")]

                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif mc_knowledge >= 0:
                imagebutton:
                                            
                    idle "gui/codex/EMPTYANSWERA.png"
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

