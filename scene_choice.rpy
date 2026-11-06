define persistent.chapter_act0_scene = 0
define persistent.chapter_act1_scene = 0
define persistent.chapter_act1_secret_scene = 0
define persistent.chapter_act1_lewd_scene = 0
define persistent.chapter_act2_scene = 0
define persistent.chapter_act3_scene = 0
define persistent.chapter_act3_5_scene = 0
define persistent.chapter_act3_5_lewd_scene = 0
define persistent.chapter_act4_scene = 0
define persistent.chapter_act4_5_scene = 0

screen choice_scene_prologue():

    tag menu 

    add "gui/Chapter/Prologuerender.png"
    # add "gui/prologue1.png"
    # add "gui/Chapter/prologue_choice_chapter/blackscreen1.png"

    imagemap:

        idle "gui/scene_choice_1.png"
        hover "gui/scene_choice_2.png"


        hotspot (36,962,296,66):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
    
    frame:
        xalign 0.5
        yalign 0.5

        has viewport
        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 1550
        ysize 720

        

        grid 3 3:
            xalign 1.0  # выравнивание сетки справа
            yalign 0.0

            if persistent.chapter_act0_scene >= 0:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene1_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene1_on.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Start()]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

                    

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene2_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene2_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("homedinner")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene3_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene3_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("anna")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene4_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene4_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("bar_olivica")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene5_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene5_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("norman_home")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/Prologue1.png"
                    hover "gui/Chapter/Prologue2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("jungle")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 6:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene7_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene7_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("spaceship")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act0_scene >= 7:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene8_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene8_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("spaceship_into")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act0_scene >= 8:
                imagebutton:
                    idle "gui/Chapter/prologue_choice_chapter/scene9_off.png"
                    hover "gui/Chapter/prologue_choice_chapter/scene9_on.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("endoftheporolgue")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

screen choice_scene_act1():

    tag menu 

    add "gui/Chapter/Act1render.png"
    # add "gui/prologue1.png"
    # add "gui/Chapter/prologue_choice_chapter/blackscreen1.png"

    imagemap:

        idle "gui/scene_choice_1.png"
        hover "gui/scene_choice_2.png"


        hotspot (36,962,296,66):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act1")]
    
    frame:
        xalign 0.5
        yalign 0.5

        has viewport
        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 1550
        ysize 720

        

        grid 3 4:
            xalign 1.0  # выравнивание сетки справа
            yalign 0.0

            if persistent.chapter_act1_scene >= 0:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_1_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_1_off.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story02")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

                    

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_2_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_2_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("firstanswernext")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_secret_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_11_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_11_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("eye")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_3_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_3_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("taxi")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"


            if persistent.chapter_act1_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_4_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_4_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("street3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_5_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_5_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("bar_cyber")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_6_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_6_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("bar_cyber1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 6:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_7_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_7_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("cyberstreet1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 7:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_8_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_8_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("gate2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_scene >= 8:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_9_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_9_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("gate4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act1_lewd_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_12_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_12_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("olivia_fr_scene")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"


            if persistent.chapter_act1_scene >= 9:
                imagebutton:
                    idle "gui/Chapter/act1_choice_chapter/act1_sceme_10_on.png"
                    hover "gui/Chapter/act1_choice_chapter/act1_sceme_10_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("final2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

screen choice_scene_act2():

    tag menu 

    add "gui/Chapter/Act2render.png"
    # add "gui/prologue1.png"
    # add "gui/Chapter/prologue_choice_chapter/blackscreen1.png"

    imagemap:

        idle "gui/scene_choice_1.png"
        hover "gui/scene_choice_2.png"


        hotspot (36,962,296,66):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act2")]
    
    frame:
        xalign 0.5
        yalign 0.5

        has viewport
        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 1550
        ysize 720

        

        grid 3 4:
            xalign 1.0  # выравнивание сетки справа
            yalign 0.0

            if persistent.chapter_act2_scene >= 0:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_1_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_1_off.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story03")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

                    

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_2_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_2_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_3_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_3_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"


            if persistent.chapter_act2_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_4_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_4_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_5_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_5_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter5")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_6_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_6_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter5_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 6:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_8_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_8_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter5_5")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 7:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_9_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_9_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter6")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 8:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_7_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_7_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt2chapter7")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act2_scene >= 9:
                imagebutton:
                    idle "gui/Chapter/act2_choice_chapter/act2_sceme_9_on.png"
                    hover "gui/Chapter/act2_choice_chapter/act2_sceme_9_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("mirielhome")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

screen choice_scene_act3():

    tag menu 

    add "gui/Chapter/Act3render.png"
    # add "gui/prologue1.png"
    # add "gui/Chapter/prologue_choice_chapter/blackscreen1.png"

    imagemap:

        idle "gui/scene_choice_1.png"
        hover "gui/scene_choice_2.png"


        hotspot (36,962,296,66):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act3")]
    
    frame:
        xalign 0.5
        yalign 0.5

        has viewport
        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 1550
        ysize 720

        

        grid 3 9:
            xalign 1.0  # выравнивание сетки справа
            yalign 0.0

            if persistent.chapter_act3_scene >= 0:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_1_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_1_off.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story04")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"



            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_2_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_2_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter1_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_3_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_3_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter1_3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"


            if persistent.chapter_act3_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_4_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_4_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_5_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_5_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter2_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_6_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_6_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter2_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 6:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_7_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_7_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 7:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_8_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_8_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter3_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 8:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_9_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_9_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter3_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act3_scene >= 9:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_10_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_10_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter3_3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"


            if persistent.chapter_act3_scene >= 10:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_11_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_11_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter3_4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"


            if persistent.chapter_act3_scene >= 11:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_12_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_12_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_scene >= 12:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_13_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_13_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter5")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_scene >= 13:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_14_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_14_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter5_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_scene >= 14:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_15_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_15_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter5_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_scene >= 15:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_16_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_16_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("akt3chapter6")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_17_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_17_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_18_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_18_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter1_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_19_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_19_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_20_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_20_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter2_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_21_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_21_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter2_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 6:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_22_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_22_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter2_3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 7:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_23_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_23_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 8:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_24_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_24_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("next_kalestra_meeting")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_scene >= 9:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_25_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_25_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("act3_5chapter4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"



            if persistent.chapter_act3_5_lewd_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_26_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_26_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("ivy_meetings")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"


            if persistent.chapter_act3_5_scene >= 10:
                imagebutton:
                    idle "gui/Chapter/act3_choice_chapter/act3_sceme_27_on.png"
                    hover "gui/Chapter/act3_choice_chapter/act3_sceme_27_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("endof3_5chapter")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

screen choice_scene_act4():

    tag menu 

    add "gui/Chapter/Act4render.png"
    # add "gui/prologue1.png"
    # add "gui/Chapter/prologue_choice_chapter/blackscreen1.png"

    imagemap:

        idle "gui/scene_choice_1.png"
        hover "gui/scene_choice_2.png"


        hotspot (36,962,296,66):
            hover_sound "audio/CLS.ogg"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice_act4")]
    
    

    frame:
        xalign 0.5
        yalign 0.5

        has viewport
        mousewheel True
        draggable True
        scrollbars "vertical"
        xsize 1550
        ysize 720

        

        grid 3 6:
            xalign 1.0  # выравнивание сетки справа
            yalign 0.0

            if persistent.chapter_act4_scene >= 0:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_1_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_1_off.png"
                    action [Play("menu_click", "audio/buttonsounds1.mp3"), Start("story05")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"



            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_2_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_2_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_3_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_3_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"
            
            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    focus_mask True
                    style "navigation_button"


            if persistent.chapter_act4_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_4_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_4_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_2_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_5_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_5_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_6_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_6_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"
            if persistent.chapter_act4_scene >= 6:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_7_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_7_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"
            if persistent.chapter_act4_scene >= 7:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_8_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_8_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_6")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"
            if persistent.chapter_act4_scene >= 8:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_9_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_9_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_7")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"
            

            if persistent.chapter_act4_scene >= 9:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_10_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_10_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_8")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"
                    

            if persistent.chapter_act4_scene >= 10:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_sceme_11_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_sceme_11_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_9")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"


            if persistent.chapter_act4_5_scene >= 0:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_5_sceme_1_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_5_sceme_1_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5_1")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_5_scene >= 1:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_5_sceme_2_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_5_sceme_2_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5_2")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_5_scene >= 2:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_5_sceme_3_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_5_sceme_3_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5_3")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_5_scene >= 3:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_5_sceme_4_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_5_sceme_4_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5_4")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_5_scene >= 4:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_5_sceme_5_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_5_sceme_5_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5_5")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            if persistent.chapter_act4_5_scene >= 5:
                imagebutton:
                    idle "gui/Chapter/act4_choice_chapter/act4_5_sceme_6_on.png"
                    hover "gui/Chapter/act4_choice_chapter/act4_5_sceme_6_off.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start("story05_5_6")]
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            else: 
                imagebutton:
                    idle "gui/Chapter/blackprologue.png"
                    style "navigation_button"

            