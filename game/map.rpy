default map_zoom = 1.0
default map_x = 0.0
default map_y = 0.0
define MAP_W = 6316
define MAP_H = 4148
default dragging = False
default drag_started = False
default drag_moved = False

init python:

    def start_drag():
        global dragging, last_mouse_x, last_mouse_y, drag_started, drag_moved

        dragging = True
        drag_started = True
        drag_moved = False

        last_mouse_x, last_mouse_y = renpy.get_mouse_pos()

    def stop_drag():
        global dragging
        dragging = False


    def drag_move():
        global map_x, map_y, last_mouse_x, last_mouse_y, dragging, drag_moved

        if not dragging:
            return

        mx, my = renpy.get_mouse_pos()

        dx = mx - last_mouse_x
        dy = my - last_mouse_y

        if abs(dx) > 3 or abs(dy) > 3:
            drag_moved = True

            map_x += dx
            map_y += dy

            clamp_offset()

        last_mouse_x = mx
        last_mouse_y = my
        
    def zoom_at(mx, my, factor):
        global map_zoom, map_x, map_y

        sw = renpy.config.screen_width
        sh = renpy.config.screen_height

        mx -= sw / 2
        my -= sh / 2

        old_zoom = map_zoom
        new_zoom = max(0.3, min(2.0, map_zoom * factor))

        if new_zoom == old_zoom:
            return

        scale = new_zoom / old_zoom

        map_x = mx - (mx - map_x) * scale
        map_y = my - (my - map_y) * scale

        map_zoom = new_zoom

        clamp_offset()

    def clamp_offset():
        global map_x, map_y, map_zoom

        sw = renpy.config.screen_width
        sh = renpy.config.screen_height

        half_w = (MAP_W * map_zoom) / 2
        half_h = (MAP_H * map_zoom) / 2

        min_x = sw/2 - half_w
        max_x = half_w - sw/2

        min_y = sh/2 - half_h
        max_y = half_h - sh/2

        map_x = max(min_x, min(max_x, map_x))
        map_y = max(min_y, min(max_y, map_y))


        
screen map_screen:

    tag profile_menu

    modal True
    style_prefix "ground"
    
    key 'K_ESCAPE' action Return()
    key 'K_TAB' action Hide("map_screen"), ShowMenu("Galaxymap")
    
    key "mouseup_4" action Function(zoom_at, renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1], 1.1)
    key "mouseup_5" action Function(zoom_at, renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1], 0.9)

    if persistent.chapter_act1 == True:

        

        key "mousedown_1" action Function(start_drag)
        key "mouseup_1" action Function(stop_drag)

        timer 0.01 action Function(drag_move) repeat True

        add Solid("#000")
        
        fixed:
            xysize (config.screen_width, config.screen_height)

        fixed:
            xfill True
            yfill True

            add "gui/map/map.png" at Transform(
                zoom=map_zoom,
                xpos=0.5,
                ypos=0.5,
                anchor=(0.5, 0.5),
                xoffset=map_x,
                yoffset=map_y
            )
            

            
            imagebutton:
                idle "gui/map/sector0.png"
                hover "gui/map/sector0b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector0")]
                hover_sound "audio/CLS.ogg"
        
            imagebutton:
                idle "gui/map/sector1.png"
                hover "gui/map/sector1b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector0")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector2.png"
                hover "gui/map/sector2b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector2")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector3.png"
                hover "gui/map/sector3b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector3")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector4.png"
                hover "gui/map/sector4b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector0")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector5.png"
                hover "gui/map/sector5b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector5")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector6.png"
                hover "gui/map/sector6b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector6")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector7.png"
                hover "gui/map/sector7b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector7")]
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/map/sector8.png"
                hover "gui/map/sector8b.png"
                focus_mask True
                at Transform(zoom=map_zoom, xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), xoffset=map_x, yoffset=map_y)
                action [Play("menu_click", "audio/UItaps.mp3"), Show("sector8")]
                hover_sound "audio/CLS.ogg"

        
        imagemap:
            ground "gui/map/mapFrame.png"
            hover "gui/map/mapFrame2.png"

            hotspot (171,919,159,50) action Return()
            hotspot (1380,919,184,50) action Hide("map_screen"), ShowMenu("Galaxymap")
            # hotspot (1611,921,198,47) action Return()
            hotspot (1258,109,150,52) action Function(zoom_at, config.screen_width/2, config.screen_height/2, 0.9)
            hotspot (1414,107,135,52) action Function(zoom_at, config.screen_width/2, config.screen_height/2, 1.1)
            hotspot (1661,109,143,52) action Hide("map_screen"), ShowMenu("Galaxymap")

        add "gui/map/arkf.png"

    else:

        add "gui/map/closemap1.png"

        imagebutton:
            idle "gui/AESC.png" hover "gui/BESC.png"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
            at test_anim_not
            xpos 40
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

    # viewport:
    #     draggable True
    #     mousewheel False

    #     add "gui/map/map.png" at Transform(zoom=map_zoom)

    # if _in_replay:
    #         imagebutton:
    #             idle "gui/return-replay1.png" hover "gui/return-replay2.png"
    #             action [Play("menu_click", "audio/UItaps.mp3"), EndReplay(confirm=True)]
    #             at test_anim_not
    #             xpos 540
    #             ypos 900
    #             focus_mask True
    #             style "navigation_button"
    #             hover_sound "audio/CLS.ogg"

    # if main_menu:
    #     imagebutton:
    #         idle "gui/AESC.png" hover "gui/BESC.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), Return()]
    #         at test_anim_not
    #         xpos 40
    #         ypos 900
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    # else:

    #     imagebutton:
    #         idle "gui/AESC.png" hover "gui/BESC.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), Return()]
    #         at test_anim_not
    #         xpos 40
    #         ypos 900
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

    #     imagebutton:
    #         idle "gui/AMAINMENU4.png" hover "gui/BMAINMENU4.png"
    #         action [Play("menu_click", "audio/UItaps.mp3"), MainMenu()]
    #         at test_anim_not
    #         xpos 240
    #         ypos 900
    #         focus_mask True
    #         style "navigation_button"
    #         hover_sound "audio/CLS.ogg"

        


screen sector0:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 0") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Tower") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)

            text _("")
            text _("Type: Unique. The Tower, the heart of the entire Federation.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("It oversees everything that happens within the Federation, from minor clashes in the slums to massive intergalactic corporations.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: aristocrats, governors, high-ranking officers.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Clean air (advanced filtration).") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Artificial gardens and grand cathedrals.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Almost no noise or crime.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255) 
            text _("To govern the entire Federation.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("True purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Intergalactic gateway.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("") 


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
            add "gui/map/sector_0_1.png"
            add "gui/map/sector_0_2.png"
            add "gui/map/sector_0_3.png"
            add "gui/map/sector_0_4.png"
            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector0"), ShowMenu("map_screen")

screen sector6:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 6") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Frontier Zone") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Type: Industrial-Military.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: officers, peacekeepers, the Inquisition.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Half-ruined lower levels.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Frequent conflicts.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Constant noise.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Defending the city from the Soulless.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Note: A buffer zone between the civilized sectors and the infected regions.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)



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
            add "gui/map/sector_6_1.png"
            add "gui/map/sector_6_2.png"
            add "gui/map/sector_6_3.png"
            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector6"), ShowMenu("map_screen")


screen sector5:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 5") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("The Slums") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Type: Industrial-Residential.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: workers, civilians, maintenance personnel.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Constant noise.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Polluted air.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Severe overpopulation.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Production of weapons, machinery, and resources.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Maintaining the Federation’s economy.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Note: Gunfights between patrol units and unidentified groups occur daily.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)




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
            add "gui/map/sector_5_1.png"
            add "gui/map/sector_5_2.png"
            add "gui/map/sector_5_3.png"
            add "gui/map/sector_5_4.png"
            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector5"), ShowMenu("map_screen")



screen sector7:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 7") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("The Ruins / Tombs") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Type: Ruins.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: the poor, gangs, mutants, and the Soulless.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Half-collapsed levels.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Frequent violence.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Little to no law enforcement.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Black market operations.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Cheap labor.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)



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
            add "gui/map/sector_7_1.png"
            add "gui/map/sector_7_2.png"
            add "gui/map/sector_7_3.png"
            add "gui/map/sector_7_4.png"
            add "gui/map/sector_7_5.png"
            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector7"), ShowMenu("map_screen")


screen sector8:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 8") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("The Ruins / Tombs") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Type: Ruins.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: the Soulless.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Half-collapsed levels.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Polluted air.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Destroyed infrastructure.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Complete anarchy.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Officially: none.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("In reality: a source of constant threat — the Soulless.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)


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
            add "gui/map/sector_8_1.png"
            add "gui/map/sector_8_2.png"
            add "gui/map/sector_8_3.png"
            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector8"), ShowMenu("map_screen")


screen sector3:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 3") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Administrative Districts") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Type: Wealthy Residential / Administrative.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: middle-class citizens, weapons dealers, corporate elites.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Clean air (advanced filtration).")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Crime kept under control.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Restricted access.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Propaganda and the Cult of Astoria.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Administration of Sectors 4–6.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)


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
            add "gui/map/sector_3_1.png"
            add "gui/map/sector_3_2.png"
            add "gui/map/sector_3_3.png"
            add "gui/map/sector_3_4.png"
            add "gui/map/sector_3_5.png"
            add "gui/map/sector_3_6.png"
            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector3"), ShowMenu("map_screen")



screen sector2:

    tag sector_menu

    modal True
    style_prefix "ground"

    add "gui/game_menu_frame14.png" 

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
            text _("Sector 2") size 45 font "font/NotoSansSC-Black.ttf" color "#6f542c"
            text _("Elite Districts") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Type: Wealthy Residential / Administrative.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Residents: upper middle class, government officials, officers.") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Environment:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Well-maintained infrastructure.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Minimal noise and crime.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Private businesses and services.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("")
            text _("Purpose:") size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Bureaucratic administration.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Oversight of industrial production.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)
            text _("Serving the elite.")  size 25 font "font/NotoSansSC-Black.ttf" color (255,255,255)


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
            add "gui/map/sector_2_1.png"
            add "gui/map/sector_2_2.png"
            add "gui/map/sector_2_3.png"
            add "gui/map/sector_2_4.png"

            

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("sector2"), ShowMenu("map_screen")


screen Galaxymap:

    tag profile_menu

    modal True
    style_prefix "ground"
    
    key 'K_ESCAPE' action Return()

    add "gui/map/galaxymap.png" 

    imagebutton:
        idle "gui/map/arkfederation1.png" hover "gui/map/arkfederation2.png"
        action [Play("menu_click", "audio/UItaps.mp3"), Hide("Galaxymap"), ShowMenu("map_screen")]
        focus_mask True
        xpos -10 
        ypos -10 
        style "navigation_button"
        hover_sound "audio/CLS.ogg"

    imagebutton:
        idle "gui/map/elfemp1.png" hover "gui/map/elfemp2.png"
        action [Play("menu_click", "audio/UItaps.mp3"), Hide("Galaxymap"), ShowMenu("elf_empire")]
        focus_mask True
        xpos -10 
        ypos -10 
        style "navigation_button"
        hover_sound "audio/CLS.ogg"

    imagemap:
        ground "gui/map/escmap.png"
        hover "gui/map/mapFrame2.png"

        hotspot (171,919,159,50) action Hide("Galaxymap"), ShowMenu("map_screen")





screen elf_empire:

    if persistent.chapter_act5 == True:

        add "gui/map/closemap2.png"

        imagebutton:
            idle "gui/AESC.png" hover "gui/BESC.png"
            action [Play("menu_click", "audio/UItaps.mp3"), Hide("elf_empire"), ShowMenu("Galaxymap")]
            at test_anim_not
            xpos 40
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"


    else: 

        add "gui/map/closemap2.png"

        imagebutton:
            idle "gui/AESC.png" hover "gui/BESC.png"
            action [Play("menu_click", "audio/UItaps.mp3"), Hide("elf_empire"), ShowMenu("Galaxymap")]
            at test_anim_not
            xpos 40
            ypos 900
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"
