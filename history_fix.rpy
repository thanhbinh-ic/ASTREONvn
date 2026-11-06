# history_fix.rpy
# Fix cho loi: renpy.script.LabelNotFound: could not find label 'history_screen'.
#
# Nguyen nhan goc:
#   Astreon xoa mat man hinh History mac dinh cua Ren'Py (screen history),
#   nhung Ren'Py van goi ShowMenu('history') khi mo lich su hoi thoai.
#   ShowMenu khong tim thay screen 'history' nen doi thanh 'history_screen'
#   roi nhay toi label do, ma label nay cung khong ton tai -> crash.
#
# Cach sua:
#   File nay khoi phuc lai screen history() theo mau chuan cua Ren'Py,
#   dung cac gia tri gui.history_* va style history_* san co trong game
#   (gui.rpy, stylescreen.rpy), va them label history_screen lam du phong.
#   Khong sua file nao khac, chi can chep file nay vao game/ roi chay lai.
#
# Luu y: nut History trong menu tam dung (screens.rpy, nut AHISTORY.png)
#   hien chi phat tieng click, khong co lenh mo lich su. De nut do mo duoc
#   lich su thi sua 1 dong trong screens.rpy (xem cuoi file nay).

screen history():

    tag menu

    # Man hinh lich su co the rat dai, khong doan truoc.
    predict False

    add "gui/game_menu_pref.png"

    key "K_ESCAPE" action Return()
    key "game_menu" action Return()

    text _("History") size 40 font "font/NotoSansSC-Black.ttf" color (0, 246, 255) xpos 100 ypos 40

    viewport:
        xpos 100
        ypos 110
        xsize 1720
        ysize 760
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox:
            # QUAN TRONG: style_prefix "history" de moi dong lich su dung
            # dung style cua game: ten o cot trai (history_name, ket thuc o
            # x=233), loi thoai o cot phai (history_text, bat dau o x=255).
            # Thieu dong nay, text se dung style mac dinh, bat dau o x=0
            # va de len ten nhan vat.
            style_prefix "history"
            spacing 10

            for h in _history_list:

                window:
                    has fixed:
                        yfit True

                    if h.who:
                        label h.who:
                            style "history_name"
                            substitute False

                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        style "history_text"
                        substitute False

            if not _history_list:
                label _("The dialogue history is empty.")

    imagebutton:
        idle "gui/AESC.png" hover "gui/BESC.png"
        action Return()
        at test_anim_not
        xpos 40
        ypos 900
        focus_mask True
        style "navigation_button"
        hover_sound "audio/CLS.ogg"


label history_screen:
    call screen history
    return


# --- Sua nut History trong menu tam dung (tuy chon, de nut mo duoc lich su) ---
# Trong game/screens.rpy, tim doan:
#     imagebutton:
#         idle "gui/AHISTORY.png" hover "gui/BHISTORY.png"
#         action [Play("menu_click", "audio/UItaps.mp3")]
# Doi dong action thanh:
#         action [Play("menu_click", "audio/UItaps.mp3"), ShowMenu("history")]
# Luu file, xoa game/screens.rpyc, Force Recompile, chay lai game.
