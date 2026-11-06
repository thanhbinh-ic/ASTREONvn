define persistent.chapter_act0 = False
define persistent.chapter_act1 = False
define persistent.chapter_act2 = False
define persistent.chapter_act3 = False
define persistent.chapter_act4 = False

default chapters_adj = ui.adjustment()

screen chapter_choice():
    
    tag menu

    add "gui/Chapter/Prologuerender.png"
    # add "gui/Chapter/chapter_menu_1.png"
    
    
    imagemap:

        idle "gui/Chapter/chapter_menu_1.png"
        hover "gui/Chapter/chapter_menu_2.png"


        hotspot (36,962,296,65):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
        hotspot (782,950,354,99):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/buttonsounds1.mp3"), Start()]
        hotspot (1519,960,367,71):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("choice_scene_prologue")]
        hotspot (1556,88,300,73):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("cheat_input")]

    add "gui/Chapter/chapter_menu_prologue.png"
    add "gui/Chapter/eq.png"

    frame:

        xalign 0.5
        yalign 0.8
        xsize 1540
        ysize 320
        
        viewport:

            xadjustment chapters_adj
            mousewheel True
            draggable True
            xmaximum 1540
            # scrollbars "horisontal"

            hbox:
                
                key 'e' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'E' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'У' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'у' action SetField(chapters_adj, "value", chapters_adj.value + 510)

                key 'q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'й' action SetField(chapters_adj, "value", chapters_adj.value - 510)

                imagebutton:
                    idle "gui/Chapter/Prologue1.png" hover "gui/Chapter/Prologue2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"


                if persistent.chapter_act1 == True:
                    imagebutton:
                        idle "gui/Chapter/Act1_chapter.png" hover "gui/Chapter/Act1_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act1")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"
                
                if persistent.chapter_act2 == True:
                    imagebutton:
                        idle "gui/Chapter/Act2_1_chapter.png" hover "gui/Chapter/Act2_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act2")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act3 == True:
                    imagebutton:
                        idle "gui/Chapter/Act3_1_chapter.png" hover "gui/Chapter/Act3_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act3")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act4 == True:
                    imagebutton:
                        idle "gui/Chapter/Act4_1_chapter.png" hover "gui/Chapter/Act4_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act4")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

    frame:

        xpos 50
        ypos 160
        xsize 535
        ysize 255

        vbox:
            spacing 10
            xalign 0.5
            xysize (535, 255)

            text _("A little journey.") size 45 font "font/NotoSansSC-Black.ttf" 
            text _("")
            text _("{color=#ffffff}“End what began. Reclaim what was lost.“.") size 35 font "DejaVuSans.ttf" color (0,246,255)
            text _("")
            text _("[mc]") size 35 font "font/NotoSansSC-Black.ttf" 
            text _("")



screen chapter_choice_act1():
    
    tag menu

    add "gui/Chapter/Act1render.png"
    # add "gui/Chapter/chapter_menu_1.png"
    
    
    imagemap:

        idle "gui/Chapter/chapter_menu_1.png"
        hover "gui/Chapter/chapter_menu_2.png"


        hotspot (36,962,296,65):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
        hotspot (782,950,354,99):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story02")]
        hotspot (1519,960,367,71):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("choice_scene_act1")]
        hotspot (1556,88,300,73):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("cheat_input")]

    add "gui/Chapter/chapter_menu_act1.png"
    add "gui/Chapter/eq.png"

    frame:

        xalign 0.5
        yalign 0.8
        xsize 1540
        ysize 320
        
        viewport:

            xadjustment chapters_adj
            mousewheel True
            draggable True
            xmaximum 1540
            # scrollbars "horisontal"

            hbox:
                
                key 'e' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'E' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'У' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'у' action SetField(chapters_adj, "value", chapters_adj.value + 510)

                key 'q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'й' action SetField(chapters_adj, "value", chapters_adj.value - 510)

                imagebutton:
                    idle "gui/Chapter/Prologue1.png" hover "gui/Chapter/Prologue2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"


                if persistent.chapter_act1 == True:
                    imagebutton:
                        idle "gui/Chapter/Act1_chapter.png" hover "gui/Chapter/Act1_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act1")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"
                
                if persistent.chapter_act2 == True:
                    imagebutton:
                        idle "gui/Chapter/Act2_1_chapter.png" hover "gui/Chapter/Act2_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act2")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act3 == True:
                    imagebutton:
                        idle "gui/Chapter/Act3_1_chapter.png" hover "gui/Chapter/Act3_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act3")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act4 == True:
                    imagebutton:
                        idle "gui/Chapter/Act4_1_chapter.png" hover "gui/Chapter/Act4_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act4")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

    frame:

        xpos 50
        ypos 160
        xsize 535
        ysize 255

        vbox:
            spacing 10
            xalign 0.5
            xysize (535, 255)

            text _("New Beginning.") size 45 font "font/NotoSansSC-Black.ttf" 
            text _("")
            text _("{color=#ffffff}“Beginnings aren’t where life gets easier. They’re where we decide to move forward, no matter the cost.“") size 35 font "DejaVuSans.ttf" color (0,246,255)
            text _("")
            text _("Flora") size 35 font "font/NotoSansSC-Black.ttf" 

screen chapter_choice_act2():
    
    tag menu

    add "gui/Chapter/Act2render.png"
    # add "gui/Chapter/chapter_menu_1.png"
    
    
    imagemap:

        idle "gui/Chapter/chapter_menu_1.png"
        hover "gui/Chapter/chapter_menu_2.png"


        hotspot (36,962,296,65):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
        hotspot (782,950,354,99):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story03")]
        hotspot (1519,960,367,71):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("choice_scene_act2")]
        hotspot (1556,88,300,73):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("cheat_input")]

    add "gui/Chapter/chapter_menu_act2.png"
    add "gui/Chapter/eq.png"

    frame:

        xalign 0.5
        yalign 0.8
        xsize 1540
        ysize 320
        
        viewport:

            xadjustment chapters_adj
            mousewheel True
            draggable True
            xmaximum 1540
            # scrollbars "horisontal"

            hbox:
                
                key 'e' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'E' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'У' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'у' action SetField(chapters_adj, "value", chapters_adj.value + 510)

                key 'q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                

                imagebutton:
                    idle "gui/Chapter/Prologue1.png" hover "gui/Chapter/Prologue2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"


                if persistent.chapter_act1 == True:
                    imagebutton:
                        idle "gui/Chapter/Act1_chapter.png" hover "gui/Chapter/Act1_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act1")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"
                
                if persistent.chapter_act2 == True:
                    imagebutton:
                        idle "gui/Chapter/Act2_1_chapter.png" hover "gui/Chapter/Act2_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act2")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act3 == True:
                    imagebutton:
                        idle "gui/Chapter/Act3_1_chapter.png" hover "gui/Chapter/Act3_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act3")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act4 == True:
                    imagebutton:
                        idle "gui/Chapter/Act4_1_chapter.png" hover "gui/Chapter/Act4_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act4")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

    frame:

        xpos 50
        ypos 160
        xsize 535
        ysize 255

        vbox:
            spacing 10
            xalign 0.5
            xysize (535, 255)

            text _("Forgotten wounds.") size 45 font "font/NotoSansSC-Black.ttf" 
            text _("")
            text _("{color=#ffffff}“Time cannot erase pain. It only teaches us the art of carrying it.“") size 35 font "DejaVuSans.ttf" color (0,246,255)
            text _("")
            text _("Miriel") size 35 font "font/NotoSansSC-Black.ttf" 

screen chapter_choice_act3():
    
    tag menu

    add "gui/Chapter/Act3render.png"
    # add "gui/Chapter/chapter_menu_1.png"
    
    
    imagemap:

        idle "gui/Chapter/chapter_menu_1.png"
        hover "gui/Chapter/chapter_menu_2.png"


        hotspot (36,962,296,65):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
        hotspot (782,950,354,99):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story04")]
        hotspot (1519,960,367,71):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("choice_scene_act3")]
        hotspot (1556,88,300,73):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("cheat_input")]

    add "gui/Chapter/chapter_menu_act3.png"
    add "gui/Chapter/eq.png"

    frame:

        xalign 0.5
        yalign 0.8
        xsize 1540
        ysize 320
        
        viewport:

            xadjustment chapters_adj
            mousewheel True
            draggable True
            xmaximum 1540
            # scrollbars "horisontal"

            hbox:
                
                key 'e' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'E' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'У' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'у' action SetField(chapters_adj, "value", chapters_adj.value + 510)

                key 'q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                

                imagebutton:
                    idle "gui/Chapter/Prologue1.png" hover "gui/Chapter/Prologue2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"


                if persistent.chapter_act1 == True:
                    imagebutton:
                        idle "gui/Chapter/Act1_chapter.png" hover "gui/Chapter/Act1_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act1")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"
                
                if persistent.chapter_act2 == True:
                    imagebutton:
                        idle "gui/Chapter/Act2_1_chapter.png" hover "gui/Chapter/Act2_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act2")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act3 == True:
                    imagebutton:
                        idle "gui/Chapter/Act3_1_chapter.png" hover "gui/Chapter/Act3_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act3")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act4 == True:
                    imagebutton:
                        idle "gui/Chapter/Act4_1_chapter.png" hover "gui/Chapter/Act4_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act4")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

    frame:

        xpos 50
        ypos 160
        xsize 535
        ysize 255

        vbox:
            spacing 10
            xalign 0.5
            xysize (535, 255)

            text _("Betrayal?") size 45 font "font/NotoSansSC-Black.ttf" 
            text _("")
            text _("{color=#ffffff}“Betrayal isn’t forgiven. It’s merely postponed… until the moment they realize how cheap their life truly is.“") size 35 font "DejaVuSans.ttf" color (0,246,255)
            text _("")
            text _("Kalestra") size 35 font "font/NotoSansSC-Black.ttf" 

screen chapter_choice_act4():
    
    tag menu

    add "gui/Chapter/Act4render.png"
    # add "gui/Chapter/chapter_menu_1.png"
    
    
    imagemap:

        idle "gui/Chapter/chapter_menu_1.png"
        hover "gui/Chapter/chapter_menu_2.png"


        hotspot (36,962,296,65):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), Return()]
        hotspot (782,950,354,99):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story05")]
        hotspot (1519,960,367,71):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("choice_scene_act4")]
        hotspot (1556,88,300,73):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("cheat_input")]

    add "gui/Chapter/chapter_menu_act4.png"
    add "gui/Chapter/eq.png"

    frame:

        xalign 0.5
        yalign 0.8
        xsize 1540
        ysize 320
        
        viewport:

            xadjustment chapters_adj
            mousewheel True
            draggable True
            xmaximum 1540
            # scrollbars "horisontal"

            hbox:
                
                key 'e' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'E' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'У' action SetField(chapters_adj, "value", chapters_adj.value + 510)
                key 'у' action SetField(chapters_adj, "value", chapters_adj.value + 510)

                key 'q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Q' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'Й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                key 'й' action SetField(chapters_adj, "value", chapters_adj.value - 510)
                

                imagebutton:
                    idle "gui/Chapter/Prologue1.png" hover "gui/Chapter/Prologue2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"


                if persistent.chapter_act1 == True:
                    imagebutton:
                        idle "gui/Chapter/Act1_chapter.png" hover "gui/Chapter/Act1_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act1")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"
                
                if persistent.chapter_act2 == True:
                    imagebutton:
                        idle "gui/Chapter/Act2_1_chapter.png" hover "gui/Chapter/Act2_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act2")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act3 == True:
                    imagebutton:
                        idle "gui/Chapter/Act3_1_chapter.png" hover "gui/Chapter/Act3_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act3")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

                if persistent.chapter_act4 == True:
                    imagebutton:
                        idle "gui/Chapter/Act4_1_chapter.png" hover "gui/Chapter/Act4_2_chapter.png"
                        action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act4")]
                        focus_mask True
                        style "navigation_button"
                        hover_sound "audio/CLS.ogg"

                else: 
                    imagebutton:
                        idle "gui/Chapter/blackprologue.png"
                        style "navigation_button"

    frame:

        xpos 50
        ypos 160
        xsize 535
        ysize 255

        vbox:
            spacing 10
            xalign 0.5
            xysize (535, 255)

            text _("Truth.") size 45 font "font/NotoSansSC-Black.ttf" 
            text _("")
            text _("{color=#ffffff}“Truth whispers in the quiet moments, but its echo can roar louder than any war.“") size 35 font "DejaVuSans.ttf" color (0,246,255)
            text _("")
            text _("Evrelia") size 35 font "font/NotoSansSC-Black.ttf" 