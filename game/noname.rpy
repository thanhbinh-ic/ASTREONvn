init -666:
    if renpy.loadable("anchous"):
        $ rparequired = True
    else:
        $ rparequired = False
    $ rpainstalled = False


define Astreon = Character(_("NoGlory"), color="#0a43ff")
label presplash:
    $ GameName = os.path.basename(os.path.dirname(renpy.config.basedir))

    if renpy.loadable("archive.rpa"):
        $ rpainstalled = True

    if (rparequired == True ) and (rpainstalled == False ):

        menu:
            "Quit. (Must restart to load rpa file)":
                Astreon "[config.name]"
                Astreon "[gamename]"
                Astreon "You need to add {b}archive.rpa{/b} to the {b}/Documents/Astreon/game{/b} directory"
                $ renpy.quit(relaunch=False, status=0, save=False)



    python:
        config.label_overrides.pop("splashscreen")
    if renpy.has_label("splashscreen"):
        call splashscreen from _call_splashscreen
    return

init 10001 python:
    config.label_overrides["splashscreen"] = "presplash"

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
