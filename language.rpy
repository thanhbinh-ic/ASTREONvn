define dropbox_popup_xsize = config.screen_width // 8

init -1:
    style dropbox_vbox is vbox:
        spacing 0

    style dropbox_button is button:
        background "#1d1d1d86"
        hover_background gui.hover_color

    style dropbox_button_text is button_text:
        color gui.idle_color
        hover_color gui.text_color

    style dropbox_frame is frame:
        background "#1d1d1d86"

init -1 python:
    @renpy.pure
    class DropDown(Action):
        def __init__(self, *args, **kwargs):
            labels = args[0::2]
            actions = args[1::2]
            self.entries = list(zip(labels, actions))

            if kwargs.get("mouse", False) and not(kwargs.get("width", None) or kwargs.get("xsize", None)):
                kwargs["width"] = dropbox_popup_xsize

            self.kwargs = kwargs

        def __call__(self):
            renpy.capture_focus("dropdown")
            renpy.show_screen("dropdown", entries=self.entries, **self.kwargs)
            renpy.restart_interaction()

    def dropbox_pos(**kwargs):
        if kwargs.get("mouse", False):
            x, y = renpy.get_mouse_pos()
            x, y = int(x), int(y)

        else:
            if kwargs.get("pos", None):
                x, y = kwargs.get("pos")

            else:
                x, y = kwargs.get("xpos", None), kwargs.get("ypos", None)

        return x, y

    def focus():
        x, y, w, h = renpy.focus_coordinates()

        if None in (x, y, w, h):
            return 0, 0, 0, 0

        return int(x), int(y), int(w), int(h)

    def dropbox_xsize(**kwargs):
        return focus()[2] or kwargs.get("xsize", None) or kwargs.get("width", None)

screen dropdown_container(**kwargs):
    default pos = dropbox_pos(**kwargs)

    if pos == (None, None):
        nearrect:
            transclude

            focus "dropdown"

    else:
        frame style "empty":
            if pos:
                pos pos

            focus "dropdown"

            transclude

screen dropdown(entries, **kwargs):
    zorder 99

    dismiss:
        action Hide()

    use dropdown_container(**kwargs):
        style_prefix "dropbox"

        frame:
            has vbox

            for i in range(len(entries)):
                $ label, action = entries[i]

                textbutton label:
                    xsize dropbox_xsize(**kwargs)
                    action [ Hide(), action ]

screen language1():

    key 'e' action ShowMenu("other1")
    key 'E' action ShowMenu("other1")
    key 'У' action ShowMenu("other1")
    key 'у' action ShowMenu("other1")

    key 'q' action ShowMenu("help1")
    key 'Q' action ShowMenu("help1")
    key 'Й' action ShowMenu("help1")
    key 'й' action ShowMenu("help1")

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

    add "gui/game_menu_settings3.png" 

    frame: 
        xpos 1250
        ypos 300

        use tooltip1()

                    
                
    button:
        vbox:
            xpos 55
            ypos 322

            frame:
                background "gui/test_2.png"
                hover_background "gui/test_hover.png"
            

                padding (0, 0)
                xysize (1120, 80)

                text "Change language" align (0.03, 0.4) font "font/NotoSansSC-Black.ttf" size 30

                hbox:
                    spacing 15
                    align (0.65, 0.4)

                    

                    textbutton "Language ▼":
                        action DropDown(
                            _("English"), Language(None),
                            _("Russian"), Show("russian_screen"),
                            _("Chinese"), Show("chinese_screen"),
                            _("Spanish"), Show("spanish_screen"),
                            _("Vietnamese"), Language("vietnamese"),
                            mouse=True
                        )

                        hovered SetVariable("tooltip_text", "Select the language of all text in the game.")
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


screen russian_screen():

    tag russian_screen
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 400

        style_prefix "confirm"

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            text _("Включить Русский перевод?") size 45 font "font/NotoSansSC-Black.ttf" xalign 0.5

            text _("Несколько моментов, начиная с 4 акта, и до конца текущего контента перевод был сделан вручную переводчиком. Все что до этого, было переведено с помощью ИИ, в качестве временной мери. (P.S. Ваш Безславный разработчик.)"):
                size 22
                font "font/NotoSansSC-Black.ttf"
                xalign 0.5
                text_align 0.5
                xmaximum 620

            hbox:
                spacing 60
                xalign 0.5

                textbutton _("Enable"):
                    text_size 40
                    action [
                        Play("menu_click", "audio/buttonsounds3.mp3"),
                        Language("russian"),
                        Hide("russian_screen")
                    ]

                textbutton _("Disable"):
                    text_size 40
                    action [
                        Play("menu_click", "audio/buttonsounds3.mp3"),
                        Hide("russian_screen")
                    ]


screen chinese_screen():

    tag chinese_screen
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 400

        style_prefix "confirm"

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            text _("Enable Chinese translation?") size 45 font "font/NotoSansSC-Black.ttf" xalign 0.5

            # text _("The Chinese translation was made with AI as a temporary measure. By continuing, you agree to use it."):
                # size 22
                # font "font/NotoSansSC-Black.ttf"
                # xalign 0.5
                # text_align 0.5
                # xmaximum 620

            hbox:
                spacing 60
                xalign 0.5

                textbutton _("Enable"):
                    text_size 40
                    action [
                        Play("menu_click", "audio/buttonsounds3.mp3"),
                        Language("chinese"),
                        Hide("chinese_screen")
                    ]

                textbutton _("Disable"):
                    text_size 40
                    action [
                        Play("menu_click", "audio/buttonsounds3.mp3"),
                        Hide("chinese_screen")
                    ]


screen spanish_screen():

    tag spanish_screen
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 400

        style_prefix "confirm"

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            text _("Enable Spanish translation?") size 45 font "font/NotoSansSC-Black.ttf" xalign 0.5

            text _("The Spanish translation was made with AI as a temporary measure. By continuing, you agree to use it."):
                size 22
                font "font/NotoSansSC-Black.ttf"
                xalign 0.5
                text_align 0.5
                xmaximum 620

            hbox:
                spacing 60
                xalign 0.5

                textbutton _("Enable"):
                    text_size 40
                    action [
                        Play("menu_click", "audio/buttonsounds3.mp3"),
                        Language("spanish"),
                        Hide("spanish_screen")
                    ]

                textbutton _("Disable"):
                    text_size 40
                    action [
                        Play("menu_click", "audio/buttonsounds3.mp3"),
                        Hide("spanish_screen")
                    ]
