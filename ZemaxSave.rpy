init offset = 99

default persistent.save_naming = True


init -999 python:

    def pages_range():
        page = int(persistent._file_page)

        if page % 10 == 0:
            return (page // 10) - 1
        else:
            return page // 10


    if persistent.pages_range is None:
        if unicode(persistent._file_page).isnumeric():
            persistent.pages_range = pages_range()
        else:
            persistent.pages_range = 0

    class FilePage(Action, DictEquality):
        """
         :doc: file_action

         Sets the file page to `page`, which should be one of "auto", "quick",
         or an integer.
         """

        def __init__(self, page):
            self.page = str(page)

            if page == "auto":
                self.alt = _("File page auto")
            elif page == "quick":
                self.alt = _("File page quick")
            else:
                self.alt = _("File page [text]")

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_selected(self):
            return self.page == persistent._file_page

        def predict(self):
            _predict_file_page(self.page)


    class FilePageNext(Action, DictEquality):
        """
        :doc: file_action

        Goes to the next file page.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to.

        `wrap`
            If true, we can go to the first page when on the
            last file page if `max` is set.

        `auto`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.

        `quick`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.
        """

        alt = _("Next file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, increment=1):

            page = persistent._file_page

            if page == "auto":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                elif config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"

            elif page == "quick":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                else:
                    page = "1"

            else:
                page = int(page) + increment

                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None

                if page is not None:
                    page = str(page)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None

        def predict(self):
            _predict_file_page(self.page)


    class FilePagePrevious(Action, DictEquality):
        """
         :doc: file_action

         Goes to the previous file page, if possible.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to. This is required to enable
            wrap.

        `wrap`
            If true, we can go to the last page when on the first file page if max is set.

        `auto`
            If true, this can bring the player to
            the page of automatic saves.

        `quick`
            If true, this can bring the player to
            the page of automatic saves.

         """

        alt = _("Previous file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, decrement=1):

            if wrap and max is not None:
                max = str(max)
            else:
                max = None

            page = persistent._file_page

            if page == "auto":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                else:
                    page = max

            elif page == "quick":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            elif page == "1":
                if decrement == 1 and config.has_quicksave and quick:
                    page = "quick"
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            else:
                if int(page) <= decrement:
                    page = max
                else:
                    page = str(int(page) - decrement)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page

        def predict(self):
            _predict_file_page(self.page)



screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            spacing 25
            xsize 650

            if FileLoadable(slot):
                label _("Save name ({color=#f00}Overwrite{/color}):") style "confirm_prompt"
            else:
                label _("Save name ({color=#0f0}New{/color}):") style "confirm_prompt"

            input:
                value VariableInputValue('save_name')
                length 30
                xalign 0.5
                exclude "\\[{"

            hbox:
                xfill True
                textbutton _("Yes") action FileAction(slot, confirm=False), Hide("screen_save_name") xalign 0.5
                textbutton _("No") action Hide("screen_save_name") xalign 0.5

    ## Right-click and escape answer "no".
    key "game_menu" action Hide("screen_save_name")

    ## Return of Enter answer "yes".
    key "K_RETURN" action FileAction(slot, confirm=False), Hide("screen_save_name")
    key "K_KP_ENTER" action FileAction(slot, confirm=False), Hide("screen_save_name")



