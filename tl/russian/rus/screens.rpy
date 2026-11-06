define -1 persistent.dialogueBoxOpacity = 0.5
define -1 first_start = True
define -1 persistent.textbox_width = 1400
define -1 persistent.textbox_height = 200

# Диалоговое окно в игре.
init -501 screen say(who, what):

    zorder -1

    style_prefix "say"

    window:
        id "window"
        background Frame (im.Alpha ("gui/textbox.png", persistent.dialogueBoxOpacity), 0, 0)
        xsize persistent.textbox_width + 274
        ysize persistent.textbox_height + 110

        has vbox
        xpos gui.name_xpos
        ypos 10
        xsize persistent.textbox_width
        spacing -80

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what":
            xpos 120

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

# Диалоговое окно в меню.
init -501 screen dialogue_preview(who, what, scale=1.0):

    zorder -1

    frame:

        xalign 0.5
        yalign 0.5

        window:
            id "window"
            background Frame (im.Alpha ("gui/textbox.png", persistent.dialogueBoxOpacity), 0, 0)
            xsize persistent.textbox_width + 510
            ysize persistent.textbox_height + 150
            align (0.5, 0.6)

        vbox:
            xpos gui.name_xpos
            ypos 110
            xsize persistent.textbox_width
            ysize persistent.textbox_height
            spacing 15

            if who is not None:

                window:

                    style "namebox"
                    text who:
                        size 70


                    text what:
                        xpos 120
                        ypos 90
                        size 50

        at transform:
            zoom scale

init -1 python:
    config.character_id_prefixes.append('namebox')

# Экран ввода имени
init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xanchor gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

# Экран выборов
init -501 screen choice(items):
    style_prefix "choice"

    vbox:
         for i in items:
             if (renpy.showing("s1dd7") or renpy.showing("s1dd6")) and preferences.language == "russian":
                 if i.caption == "Help":
                     $ i.caption = "Помочь"
                 if i.caption == "Refuse":
                     $ i.caption = "Не вмешиваться"
             if (renpy.showing("s1dd2") or renpy.showing("s1dd3")) and preferences.language == "russian":
                 if i.caption == "Lora":
                     $ i.caption = "Лора."
             if renpy.showing("s2g9") and preferences.language == "russian":
                 if i.caption == "No":
                     $ i.caption = "Нет."
             textbutton i.caption action i.action

# Нижняя менюшка во время игры
init -501 screen quick_menu:
    zorder 1000

    if persistent.profmenu == True:
        vbox:
            style_prefix "quick"
            xalign 0.01
            yalign 0.01

            imagebutton:
                idle "gui/ASETING.png" hover "gui/BSETING.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("profile_menu",_transition=linearblur)]
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

    if quick_menu_orientation == "vbox":
        imagemap:

            idle "gui/bar/qmenu_idle.png"
            hover "gui/bar/qmenu_hover.png"

            hotspot (370, 1000,150,100) action Rollback() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (510, 1000, 150, 100) action Preference("auto-forward", "toggle") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (650, 1000, 150, 100) action [Hide("qmenutextdisplay"), Skip()] alternate Skip(fast=True, confirm=True)
            hotspot (800, 1000, 150, 100) action ShowMenu('history') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (950, 1000, 150, 100) action ShowMenu('save') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1110, 1000, 150, 100) action QuickSave() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1250, 1000, 150, 100) action QuickLoad() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1400, 1000, 150, 100) action ShowMenu('navigation') hovered [ Play ("hover_load", "audio/CLS.ogg") ]

    elif quick_menu_orientation   == "hbox":
        imagemap:

            idle "gui/bar/qmenu_idle1.png"
            hover "gui/bar/qmenu_hover1.png"

            hotspot (1800, 340,120, 50) action Rollback() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800,  400, 120, 50) action Preference("auto-forward", "toggle") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 450, 120, 50) action [Hide("qmenutextdisplay"), Skip()] alternate Skip(fast=True, confirm=True)
            hotspot (1800, 510, 120, 50) action ShowMenu('history') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 570, 120, 50) action ShowMenu('save') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 630, 120, 50) action QuickSave() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 680, 120, 50) action QuickLoad() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 740, 120, 50) action ShowMenu('navigation') hovered [ Play ("hover_load", "audio/CLS.ogg") ]

init -1 python:
    config.overlay_screens.append("quick_menu")

init -501 screen navigation():
    if renpy.get_screen("main_menu"):
        imagemap:

            idle "gui/game_menu1.png"
            hover "gui/game_menu11.png"


            hotspot (1617,861,107,111) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://www.patreon.com/NoGloryx") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1495,861,116,109) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://discord.gg/cmF9ayjYUq") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1380,861,109,109) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://subscribestar.adult/Astreon") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1715,394,125,140) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://noglory.itch.io/astreon") hovered [ Play ("hover_load", "audio/CLS.ogg")]


        vbox:
            style_prefix "navigation_MM"

            xalign 0.1
            yalign 0.1

            # spacing gui.navigation_spacing

            imagebutton:
                idle "images/MainMenu/ASTART.png" hover "images/MainMenu/BSTART.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                at slide_from_left
                xpos 100
                ypos 1
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "images/MainMenu/ALOAD.png" hover "images/MainMenu/BLOAD.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("load")]
                at slide_from_left1
                xpos 120
                ypos 1
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "images/MainMenu/APREF.png" hover "images/MainMenu/BPREF.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("preferences")]
                at slide_from_left2
                xpos 140
                ypos 1
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

            if _in_replay:

                imagebutton:
                    idle "gui/return-replay.png" hover "gui/return-replay1.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), EndReplay(confirm=True)]
                    at slide_from_left22
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"



            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()








            if renpy.variant("pc"):

                imagebutton:
                    idle "images/MainMenu/AQUIT.png" hover "images/MainMenu/BQUIT.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Quit(confirm=not main_menu)]
                    at slide_from_left3
                    xpos 160
                    ypos 1
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

    else:
        add "images/part8/pause.png"
        vbox:

            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                imagebutton:
                    idle "gui/ASTART.png" hover "gui/BSTART.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Start()]
                    at slide_from_leftM3
                    focus_mask True
                    hover_sound "audio/CLS.ogg"

            else:

                imagebutton:
                    idle "gui/AHISTORY.png" hover "gui/BHISTORY.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("history")]
                    at slide_from_leftM2
                    focus_mask True
                    hover_sound "audio/CLS.ogg"

                imagebutton:
                    idle "gui/ASAVE2.png" hover "gui/BSAVE2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("save")]
                    at slide_from_leftM3
                    focus_mask True
                    hover_sound "audio/CLS.ogg"


            imagebutton:
                idle "gui/ALOAD2.png" hover "gui/BLOAD2.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("load")]
                at slide_from_leftM4
                focus_mask True
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/AOPTION2.png" hover "gui/BOPTION2.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("preferences")]
                at slide_from_leftM5
                focus_mask True
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "gui/ACREDITS2.png" hover "gui/BCREDITS2.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("credits1")]
                at slide_from_leftM6
                focus_mask True
                hover_sound "audio/CLS.ogg"

            if _in_replay:

                imagebutton:
                    idle "gui/return-replay.png" hover "gui/return-replay1.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), EndReplay(confirm=True)]
                    at slide_from_left22
                    focus_mask True
                    xpos 200
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif not main_menu:

                imagebutton:
                    idle "gui/AMAINMENU2.png" hover "gui/BMAINMENU2.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), MainMenu()]
                    at slide_from_leftM7 focus_mask True hover_sound "audio/CLS.ogg"

init -501 screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    if renpy.variant("pc"):

        style_prefix "game_menu"

    else:

        add "gui/game_menu_pref.png"

        style_prefix "game_menu"

        frame:
            ypos (-70)


            has hbox

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        has vbox
                        spacing spacing

                        transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude


        imagebutton:
            idle "gui/ASAVE.png" hover "gui/BSAVE.png"
            action ShowMenu('save')
            at test_anim_not
            xpos 1240
            ypos 950
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/ALOAD.png" hover "gui/BLOAD.png"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("load")]
            at test_anim_not
            xpos 1540
            ypos 950
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/AOPTION.png" hover "gui/BOPTION.png"
            action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("preferences")]
            at test_anim_not
            xpos 940
            ypos 950
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/return-pref.png" hover "gui/return-pref1.png"
            if main_menu:
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("main_menu")]
            else:
                action [Play("menu_click", "audio/UItaps.mp3"), Return()]

            at test_anim_not
            xpos 340
            ypos 950
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"

        imagebutton:
            idle "gui/AMAINMENU.png" hover "gui/BMAINMENU.png"
            action [Play("menu_click", "audio/UItaps.mp3"), MainMenu()]
            at test_anim_not
            xpos 40
            ypos 950
            focus_mask True
            style "navigation_button"
            hover_sound "audio/CLS.ogg"


        label title

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")

init -501 screen save():
    tag menu
    use file_slots(_(""))

init -501 screen load():
    tag menu
    use file_slots(_(""))

init -1 style page_label_text:
    font "font/NotoSansSC-Black.ttf"
    size 40
    color (255,255,255)

init -501 screen file_slots(title):


    key 'e' action ShowMenu("preferences")
    key 'E' action ShowMenu("preferences")
    key 'У' action ShowMenu("preferences")
    key 'у' action ShowMenu("preferences")

    key 'q' action ShowMenu("other1")
    key 'Q' action ShowMenu("other1")
    key 'Й' action ShowMenu("other1")
    key 'й' action ShowMenu("other1")

    key 'd' action FilePageNext()
    key 'D' action FilePageNext()
    key 'в' action FilePageNext()
    key 'В' action FilePageNext()

    key 'a' action FilePagePrevious()
    key 'A' action FilePagePrevious()
    key 'ф' action FilePagePrevious()
    key 'Ф' action FilePagePrevious()

    key 'K_ESCAPE' action Return()

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

    add "gui/game_menu_frame13.png"

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

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    fixed:



        order_reverse True



        frame:

            vbox:
                xalign 0.95
                yalign 0.25
                text _("LOAD/SAVE SCREEN") size 40 font "font/NotoSansSC-Black.ttf" color (0,246,255)



            button:
                style "page_label"

                key_events True
                xpos 1380
                ypos 445
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value




            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.1
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1


                    button:
                        if renpy.current_screen().screen_name[0] == "load":
                            action FileAction(slot)
                        else:

                            selected (str(persistent._file_page) + "-" + str(slot) == renpy.newest_slot("[0-9]"))
                            if persistent.save_naming:
                                action SetVariable("save_name", FileSaveName(slot)), Show("screen_save_name", slot=slot)
                            else:
                                action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot).replace("[","[[").replace("{","{{"):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

            frame:



                xsize 435
                xpos 1760
                ypos 345

                if persistent.save_naming:
                    textbutton _("ON") action ToggleField(persistent, "save_naming"):
                        style "save_button"
                        hovered SetVariable("hover_color", "#0a0")
                        unhovered SetVariable("hover1_color", "#0f0")
                        at hover_transform

                        text_font "font/NotoSansSC-Black.ttf"
                        text_size 40

                else:
                    textbutton _("OFF") action ToggleField(persistent, "save_naming"):
                        style "save_button"
                        hovered SetVariable("hover_color", "#a00")
                        unhovered SetVariable("hover1_color", "#f00")
                        at hover_transform

                        text_font "font/NotoSansSC-Black.ttf"
                        text_size 40

            frame:
                has vbox
                xpos 1460
                ypos 350
                text _("Save name") size 40 font "font/NotoSansSC-Black.ttf" color (255,255,255)


            vbox:
                xpos 1440
                ypos 760
                text "Note: You can move between" size 24
                text "saves using the A - D keys." size 24

            frame:

                padding (0,0)
                xpos (150)
                ypos (800)
                xysize (1860, 350)

                has hbox
                ypos (10)

                style_prefix "page"

                spacing gui.page_spacing

                textbutton _("<<") action FilePagePrevious(decrement=10)

                null width 25

                textbutton _("<") action FilePagePrevious()

                null width 10

                if config.has_autosave:
                    textbutton _("{#auto_page}A" ) xminimum 66 text_size 35 text_xalign 0.1 action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") xminimum 66 text_size 35 text_xalign 0.1 action FilePage("quick")


                for page in range( (persistent.pages_range * 10) + 1 , (persistent.pages_range * 10) + 11 ):
                    textbutton "[page]" xminimum 66 text_size 35 text_xalign 0.1 action FilePage(page)

                null width 10

                textbutton _(">") action FilePageNext()

                null width 25

                textbutton _(">>") action FilePageNext(increment=10)

init -501 screen replay_screen():
    tag menu
    use navigation

define persistent.main_menu_choice = 1

init -501 screen main_menu():
    tag menu
    if persistent.main_menu_choice == 1:

        frame at test_anim_not:
            padding (0, 0)
            background None

            add Movie(play="images/mainmenu/MainMenu.webm")
            imagemap:

                idle "gui/game_menu1.png"
                hover "gui/game_menu11.png"


                hotspot (1713,866,137,140) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://www.patreon.com/NoGloryx") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (1715,716,131,133) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://discord.gg/cmF9ayjYUq") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (1713,555,133,138) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://subscribestar.adult/Astreon") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (1715,394,125,140) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://noglory.itch.io/astreon") hovered [ Play ("hover_load", "audio/CLS.ogg")]

            imagebutton:
                idle "images/MainMenu/ASTART.png" hover "images/MainMenu/BSTART.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("chapter_choice")]
                at slide_from_left
                xpos 100
                ypos 100
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "images/MainMenu/ALOAD.png" hover "images/MainMenu/BLOAD.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("load")]
                at slide_from_left1
                xpos 120
                ypos 200
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

            imagebutton:
                idle "images/MainMenu/APREF.png" hover "images/MainMenu/BPREF.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("preferences")]
                at slide_from_left2
                xpos 140
                ypos 300
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

            if _in_replay:

                imagebutton:
                    idle "gui/return-replay.png" hover "gui/return-replay1.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), EndReplay(confirm=True)]
                    xpos 122260
                    ypos 400
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()








            if renpy.variant("pc"):

                imagebutton:
                    idle "images/MainMenu/AQUIT.png" hover "images/MainMenu/BQUIT.png"
                    action [Play("menu_click", "audio/UItaps.mp3"), Quit(confirm=not main_menu)]
                    at slide_from_left3
                    xpos 160
                    ypos 400
                    focus_mask True
                    style "navigation_button"
                    hover_sound "audio/CLS.ogg"

    elif persistent.main_menu_choice == 2:

        frame at test_anim_not:
            padding (0, 0)
            background None

            add Movie(play="images/mainmenu/MainMenu1.webm")

            imagemap:

                idle "gui/MainMenu/mainmenus2_1.png"
                hover "gui/MainMenu/mainmenus2_2.png"


                hotspot (96,639,393,48) action [ Play ("menu_click","audio/UItaps.mp3") ], ShowMenu("chapter_choice") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (96,687,393,45) action [ Play ("menu_click","audio/UItaps.mp3") ], ShowMenu("load") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (96,733,393,45) action [ Play ("menu_click","audio/UItaps.mp3") ], ShowMenu("preferences") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (96,777,393,45) action [ Play ("menu_click","audio/UItaps.mp3") ], Quit(confirm=not main_menu) hovered [ Play ("hover_load", "audio/CLS.ogg")]

                hotspot (1703,866,167,140) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://www.patreon.com/NoGloryx") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (1715,716,151,133) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://discord.gg/cmF9ayjYUq") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (1713,540,151,158) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://subscribestar.adult/Astreon") hovered [ Play ("hover_load", "audio/CLS.ogg")]
                hotspot (1715,374,155,163) action [ Play ("menu_click","audio/UItaps.mp3") ], OpenURL("https://noglory.itch.io/astreon") hovered [ Play ("hover_load", "audio/CLS.ogg")]

define persistent.text_sctp = True

init -501 screen preferences():

    key 'e' action ShowMenu("music_screen")
    key 'E' action ShowMenu("music_screen")
    key 'У' action ShowMenu("music_screen")
    key 'у' action ShowMenu("music_screen")

    key 'q' action ShowMenu("load")
    key 'Q' action ShowMenu("load")
    key 'Й' action ShowMenu("load")
    key 'й' action ShowMenu("load")

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

    add "gui/game_menu_settings.png"

    if Language(None):

        frame:

            has viewport  # Первое выражение в блоке frame
            mousewheel True  # Прокрутка колесиком мыши
            draggable True
            scrollbars "vertical"  # Добавление вертикального скроллбара
            xpos 55
            ypos 322
            xsize 1140
            ysize 530

            vbox:

                spacing 30



                frame:
                    background "gui/test_1.png"
                    hover_background "gui/test_hover.png"

                    padding (0,0)
                    xysize (1120, 80)
                    text "Screen" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30


                    hbox:
                        spacing 15
                        align (0.9, 0.4)

                        if _preferences.fullscreen:
                            textbutton _("Window"):
                                text_size 32
                                text_font "font/NotoSansSC-Black.ttf"
                                action Preference("display", "window")

                        else:
                            textbutton _("Full Screen"):
                                text_size 32
                                text_font "font/NotoSansSC-Black.ttf"
                                action Preference("display", "fullscreen")


                frame:
                    background "gui/test_1.png"
                    padding (0,0)
                    xysize (1120,80)
                    text "Dialogue transparency: [int(persistent.dialogueBoxOpacity * 100)]%" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                    bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider"):
                        left_bar "gui/bar-hover2.png"
                        right_bar "gui/bar-idle.png"
                        thumb "gui/barsth.png"
                        xysize (566, 40)
                        xalign 0.9 yalign 0.2
                        at hover_transform
                        hovered SetVariable("tooltip_text", "Allows you to change the transparency of the text, you can see the result in the example above.")
                        unhovered SetVariable("tooltip_text", None)


                frame:
                    background "gui/test_1.png"
                    padding (0,0)
                    xysize (1120,80)
                    text "Textbox Width: ([persistent.textbox_width] /1650)" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                    bar value FieldValue(persistent, "textbox_width", offset=1100, range=550, style="slider"):
                        left_bar "gui/bar-hover2.png"
                        right_bar "gui/bar-idle.png"
                        thumb "gui/barsth.png"
                        xysize (566, 40)
                        xalign 0.9 yalign 0.2
                        at hover_transform
                        hovered SetVariable("tooltip_text", "Allows you to change the width of the textbox.")
                        unhovered SetVariable("tooltip_text", None)


                frame:
                    background "gui/test_1.png"
                    padding (0,0)
                    xysize (1120,80)
                    text "Textbox Height: ([persistent.textbox_height] /300)" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                    bar value FieldValue(persistent, "textbox_height", offset=150, range=150, style="slider"):
                        left_bar "gui/bar-hover2.png"
                        right_bar "gui/bar-idle.png"
                        thumb "gui/barsth.png"
                        xysize (566, 40)
                        xalign 0.9 yalign 0.2
                        at hover_transform
                        hovered SetVariable("tooltip_text", "Allows you to change the height of the textbox.")
                        unhovered SetVariable("tooltip_text", None)



                frame:
                    background "gui/test_1.png"
                    padding (0,0)
                    xysize (1120,80)
                    text "Skip" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                    hbox:
                        spacing 15
                        align (0.9, 0.4)

                        textbutton _("All Text"):
                            text_size 30
                            text_font "font/NotoSansSC-Black.ttf"
                            action Preference("skip", "toggle")
                            hovered SetVariable("tooltip_text", "Skips all text, even text you haven't read yet.")
                            unhovered SetVariable("tooltip_text", None)

                        add "gui/button/check_selected_foreground.png" ypos 12

                        textbutton _("Selection"):
                            text_size 30
                            text_font "font/NotoSansSC-Black.ttf"
                            action Preference("after choices", "toggle")
                            hovered SetVariable("tooltip_text", "Skips only the text that has been read.")
                            unhovered SetVariable("tooltip_text", None)


                        add "gui/button/check_selected_foreground.png" ypos 12

                        textbutton _("Transitions"):
                            text_size 30
                            text_font "font/NotoSansSC-Black.ttf"
                            action InvertSelected(Preference("transitions", "toggle"))
                            hovered SetVariable("tooltip_text", "Enable or disable transitions between scenes, such as animations or screen changer effects.")
                            unhovered SetVariable("tooltip_text", None)





                if persistent.text_sctp == True:
                    frame:
                        background "gui/test_1.png"
                        hover_background "gui/test_hover.png"

                        padding (0,0)
                        xysize (1120, 80)
                        text "Text speed: ([preferences.text_cps] /300" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30


                        bar value FieldValue(preferences, "text_cps", offset=0, range=300, style="slider"):
                            left_bar "gui/bar-hover2.png"
                            right_bar "gui/bar-idle.png"
                            thumb "gui/barsth.png"
                            xysize (566, 40)
                            xalign 0.9 yalign 0.2
                            at hover_transform
                            hovered SetVariable("tooltip_text", "Changes the speed text appears.")
                            unhovered SetVariable("tooltip_text", None)

                frame:
                    background "gui/test_1.png"
                    padding (0,0)
                    xysize (1120,80)
                    text "Text speed" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                    hbox:
                        spacing 15
                        align (0.9, 0.45)

                        if persistent.text_sctp == True:
                            textbutton _("On"):
                                text_size 32
                                text_font "font/NotoSansSC-Black.ttf"
                                action [ToggleVariable("persistent.text_sctp", True), SetField(preferences, "text_cps", 0), With(dissolve)]
                                hovered SetVariable("tooltip_text", "Text typing effect - enabled.")
                                unhovered SetVariable("tooltip_text", None)


                        else:
                            textbutton _("Off"):
                                text_size 32
                                text_font "font/NotoSansSC-Black.ttf"
                                action [ToggleVariable("persistent.text_sctp", True), With(dissolve)]
                                hovered SetVariable("tooltip_text", "Text typing effect - disabled.")
                                unhovered SetVariable("tooltip_text", None)


        frame:
            xpos 1210
            ypos 315
            xysize (1418, 574)
            background None
            add "gui/alpha-back.png"

            frame:
                xalign 0.136
                yalign 0.32
                has hbox

                use dialogue_preview(who="{color=#20ADA3}Jacob{/color}", what="I Am Gay", scale=0.32)

        frame:
            xpos 1250
            ypos 600

            use tooltip1()


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

define -1 gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

#default cheat_code_input = ""

init python:

    def check_cheat_code():

        code = cheat_code_input.lower()

        if code == "srsmg%235@1":
            renpy.notify("Scenes up to the latest update have been activated.")
            persistent.chapter_act0 = True
            persistent.chapter_act1 = True
            persistent.chapter_act2 = True
            persistent.chapter_act3 = True
            persistent.chapter_act4 = True
            persistent.chapter_act0_scene += 30
            persistent.chapter_act1_scene += 30
            persistent.chapter_act1_lewd_scene += 30
            persistent.chapter_act3_scene += 30
            persistent.chapter_act4_scene += 30
            persistent.ancient_blood_ = True
            persistent.tomb_screen_ = True
            persistent.mutants_screen_ = True
            persistent.inquisitor_screen_ = True
            persistent.abyss_screen_ = True
            persistent.gate_screen_ = True
            persistent.keepers_screen_ = True
            persistent.fallen_empire_ = True
            persistent.parallel_threads_ = True
            persistent.ark_origin_ = True
            persistent.mc_name = "Kael"

        elif code == "yourstorysucks":
            renpy.notify("Gallery unlocked.")
            persistent.Anya_path_replay = True
            persistent.Olivia_path_replay = True
            persistent.Ivy_replay = True
            persistent.Flora_replay = True
            persistent.lora_First_scene = True
            persistent.lora_Second_scene = True
            persistent.olivia_Second_scene = True
            persistent.Miriel_replay = True
            persistent.Ivy_Second_scene = True
            persistent.Kalestra_replay = True
            persistent.Olivia_second_replay = True
            persistent.mc_name = "Kael"

        else:
            renpy.notify("Invalid code")

        renpy.hide_screen("cheat_input")


screen cheat_input():

    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 45

        label "Enter code":
            xalign 0.5

        input value VariableInputValue("cheat_code_input") length 32

        hbox:
            xalign 0.5
            spacing 100

            textbutton "OK" action Function(check_cheat_code)
            textbutton "Cancel" action Hide("cheat_input")

init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action

init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

init -501 screen nvl(dialogue, items):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id

define -1 config.nvl_list_length = gui.nvl_list_length

init -501 screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

init -501 screen first_start:
    imagebutton:
        idle "images/MainMenu/WarningNOA.png"
        hover "images/MainMenu/WarningNOB.png"
        xalign 0.65
        yalign 0.92
        action [OpenURL("https://www.youtube.com/watch?v=RgKAFK5djSk"), Function(renpy.quit)]
        focus_mask True

    imagebutton:
        idle "images/MainMenu/WarningYESA.png"
        hover "images/MainMenu/WarningYESB.png"
        xalign 0.34
        yalign 0.92
        action [SetVariable("persistent.first_start", False), Jump('splashscreen')]
        focus_mask True

# Движение в 0.1 и прологе.
init -501 screen path_first:
    imagebutton:
        idle "gui/button/LNAV1.png"
        hover "gui/button/LNAV.png"
        xalign 0.648
        yalign 0.795
        action Jump('path_first_left')
        focus_mask True

    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('first_right')
        focus_mask True

init -501 screen dodgebut:
    imagebutton:
        idle "gui/dodgebutton.png"
        hover "gui/dodgebutton1.png"
        xalign 0.9
        yalign 0.4
        action Jump("dodgebut2")
        focus_mask True

    timer 3.0 action Jump("dodgebut")

    bar:
        align (0.5, 0.95)
        xysize (500, 5)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 3.0, 1)

init -501 screen shooting:
    imagebutton:
        idle "images/buttons/s1g24_1.png"
        hover "images/buttons/s1g24_2.png"
        action Jump("shoot2")
        focus_mask True

    imagebutton:
        idle "images/buttons/s1g24_3.png"
        hover "images/buttons/s1g24_4.png"
        action Jump("shoot4")
        focus_mask True

    timer 3.0 action Jump("shoot3")

    bar:
        align (0.5, 0.95)
        xysize (500, 5)
        left_bar "#FFFFFF"
        right_bar "#696969"
        value AnimatedValue(0, 1, 3.0, 1)

init -501 screen shoot1:
    imagebutton:
        idle "images/buttons/SPIs 43.png"
        hover "images/S9.2D/SPIs 44.png"
        action Jump('shoot')
        focus_mask True

init -501 screen path_first_left_next:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left_next_2')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('path_first_left_back')
        focus_mask True

init -501 screen path_first_left_back:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('first_right')
        focus_mask True

init -501 screen path_door_back:
    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('path_front_next2')
        focus_mask True

init -501 screen path_front_back:

    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('path_first_left')
        focus_mask True

    imagebutton:
        idle "gui/button/LNAV1.png"
        hover "gui/button/LNAV.png"
        xalign 0.648
        yalign 0.795
        action Jump('first_right')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('front')
        focus_mask True

init -501 screen path_front_next:

    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('door_space_ship')
        focus_mask True

init -501 screen path_front_next1:

    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_front_next2')
        focus_mask True

    imagebutton:
        idle "gui/button/RNAV1.png"
        hover "gui/button/RNAV.png"
        xalign 0.73
        yalign 0.795
        action Jump('door_space_ship')
        focus_mask True

    imagebutton:
        idle "gui/button/DNAV1.png"
        hover "gui/button/DNAV.png"
        xalign 0.697
        yalign 0.85
        action Jump('front_back')
        focus_mask True

init -501 screen path_right_back1:
    imagebutton:
        idle "gui/button/UNAV1.png"
        hover "gui/button/UNAV.png"
        xalign 0.697
        yalign 0.696
        action Jump('path_first_left')
        focus_mask True

init -501 screen shoot:
    imagebutton:
        idle "images/S9.2D/SPIs 43.png"
        hover "images/S9.2D/SPIs 44.png"
        action Jump('shoot')
        focus_mask True

define -1 bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define -1 bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define -1 bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define -1 bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

init -501 screen quick_menu:
    zorder 1000

    if persistent.profmenu == True:
        vbox:
            style_prefix "quick"
            xalign 0.01
            yalign 0.01

            imagebutton:
                idle "gui/ASETING.png" hover "gui/BSETING.png"
                action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("profile_menu",_transition=linearblur)]
                focus_mask True
                style "navigation_button"
                hover_sound "audio/CLS.ogg"

    if quick_menu_orientation == "vbox":
        imagemap:

            idle "gui/bar/qmenu_idle.png"
            hover "gui/bar/qmenu_hover.png"

            hotspot (370, 1000,150,100) action Rollback() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (510, 1000, 150, 100) action Preference("auto-forward", "toggle") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (650, 1000, 150, 100) action [Hide("qmenutextdisplay"), Skip()] alternate Skip(fast=True, confirm=True)
            hotspot (800, 1000, 150, 100) action ShowMenu('history') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (950, 1000, 150, 100) action ShowMenu('save') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1110, 1000, 150, 100) action QuickSave() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1250, 1000, 150, 100) action QuickLoad() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1400, 1000, 150, 100) action ShowMenu('navigation') hovered [ Play ("hover_load", "audio/CLS.ogg") ]

    elif quick_menu_orientation   == "hbox":
        imagemap:

            idle "gui/bar/qmenu_idle1.png"
            hover "gui/bar/qmenu_hover1.png"

            hotspot (1800, 340,120, 50) action Rollback() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800,  400, 120, 50) action Preference("auto-forward", "toggle") hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 450, 120, 50) action [Hide("qmenutextdisplay"), Skip()] alternate Skip(fast=True, confirm=True)
            hotspot (1800, 510, 120, 50) action ShowMenu('history') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 570, 120, 50) action ShowMenu('save') hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 630, 120, 50) action QuickSave() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 680, 120, 50) action QuickLoad() hovered [ Play ("hover_load", "audio/CLS.ogg")]
            hotspot (1800, 740, 120, 50) action ShowMenu('navigation') hovered [ Play ("hover_load", "audio/CLS.ogg") ]

init python:

    def dialogue_gesture(gesture):

        # Работает только во время диалога
        if not renpy.get_screen("say"):
            return None

        renpy.notify(gesture)

        # Свайп влево
        if gesture == "e":
            if renpy.can_rollback():
                renpy.rollback()
                return True

        if gesture == "n":
            renpy.call_in_new_context("_game_menu", "preferences")
            return True

        if gesture == "s":
            renpy.call_in_new_context("profile_menu_context")
            return True

        return None

define config.dispatch_gesture = dialogue_gesture

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
