init  python:
    config.interact_callbacks.append(lambda: set_replace_text())

    def set_replace_text():
        if _preferences.language == "chinese":
            def replace_text(t):
                t = t.replace("Kael", "凯尔")
              
                return t
            config.replace_text = replace_text
        else:
            config.replace_text = None
return
