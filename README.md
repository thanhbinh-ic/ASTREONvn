# Astreon — Vietnamese Translation (Fan-made)

**Current version: v0.4.5**

[![Version](https://img.shields.io/badge/version-v0.4.5-blue)](https://github.com/thanhbinh-ic/ASTREONvn/releases/tag/v0.4.5)
[![Platform](https://img.shields.io/badge/platform-Android-green)](https://github.com/thanhbinh-ic/ASTREONvn/releases/tag/v0.4.5)
[![Language](https://img.shields.io/badge/language-Vietnamese-red)](https://github.com/thanhbinh-ic/ASTREONvn/releases/tag/v0.4.5)

A fan-made Vietnamese translation pack for **Astreon**, an adult visual novel by NoGlory.

> ⚠️ **Adults only (18+).** This game contains explicit adult content.

## About the Game

In the year 2032, humanity stands on the brink of a technological breakthrough. A new material, developed by a group of scientists, possesses not only extraordinary strength, hyper-elasticity, and energy-saving properties, but also a unique, or rather exceptional, ability to self-repair. This capability turned the material into a regenerative pill, allowing people with limited abilities to become fully functional humans, while also making them stronger, smarter, and even extending their lifespan.

However, fearing the consequences of such power, the scientists decide to destroy the records, reports, and everything related to their research. They scattered, each going their own way. But as is often the case, someone found the remnants of this work. Ignoring the dangers, they decided to complete it, which eventually led to the formation of a globally banned terrorist organization called "Masquerade." In response, leaders of major corporations launched a large-scale operation to eliminate the individual responsible and eradicate everything related to the research.

You are a former soldier, unable to bear the guilt of the atrocities committed during the operation. You retreat to a remote location on the edge of the world, a small town cut off from the rest of civilization, where you planned to live a peaceful life with your wife and children, far removed from all the troubles of the past.

But, as often happens, things do not go according to plan. One day, when your wife goes on a business trip to a certain research institute, she suddenly stops contacting you. In an attempt to find out what happened, you embark on a journey. Days, weeks, months, and years pass... Eventually, you come to terms with the fact that you may never see your wife again, burying all your emotions deep inside. Then, one day, your son arrives, asking for your help and with a glimmer of hope that not all is lost, that there is still a small chance to restore your peaceful life.

### Game Info

| | |
| --- | --- |
| **Published** | Sep 13, 2024 |
| **Status** | In development |
| **Platforms** | Windows, macOS, Linux, Android |
| **Rating** | ★ 4.5 out of 5 stars (561 total ratings) |
| **Author** | NoGlory |
| **Genre** | Visual Novel |
| **Tags** | 3D, Adult, Cyberpunk, Erotic, harem, NSFW, Porn, Ren'Py, Sci-fi |
| **Content** | No generative AI was used |
| **Current version** | v0.4.5 |

### Original Game

This is a fan translation. The original game is made by **NoGlory**. Please support the author on the official page:

[![Play Astreon on itch.io](https://img.shields.io/badge/itch.io-Astreon-fa5c5c?style=for-the-badge)](https://noglory.itch.io/astreon)

🔗 **Official page:** https://noglory.itch.io/astreon

## What's in This Repository

- The `main` branch contains the **full Android game data** for Astreon v0.4.5.
- The **Releases** page contains the files you need to play on Android:
  - `Astreon.0.4.5.apk` (~278 MB) — the Android installer.
  - `Patch_Vietnamese_v0.4.5.zip` (~135 MB) — the Vietnamese translation patch. **The APK on its own is not yet translated.**
  - `Source code (zip)` — the full game data, also available from the Releases page.

## Languages

The game already includes **English, Chinese, Russian, and Spanish**.

**Vietnamese is optional.** If you don't install the patch, the game will still work in one of the built-in languages. Install the Vietnamese patch only if you want to play in Vietnamese.

## What's Translated

The Vietnamese patch includes:

- All story dialogue and narration — over **20,000 translated entries** in total
- The user interface, menus, settings, and credits
- The codex and help screens
- In-game images with text, including the main menu, chapter cards, and UI buttons
- The two subtitled cutscene videos (`loading1.webm` and `spmoment.webm`), with Vietnamese subtitles
- A fix for the character-name font, so Vietnamese names display correctly
- A fix for the missing History screen (`history_screen` crash)

## Installation (Android)

### What you need

- An Android device (Android 5.0 or later)
- At least 1 GB of free storage
- A file manager app that can extract ZIP files

### Steps

**1. Download the files**

From the [**Releases**](../../releases) page, download these three files:

- `Astreon.0.4.5.apk`
- `Patch_Vietnamese_v0.4.5.zip`
- `Source code (zip)`

**2. Install the APK**

Install `Astreon.0.4.5.apk` on your Android device. You may need to allow installation from unknown sources.

Then **run the game once and close it**. This creates the game's data folder on your device.

**3. Copy the game data**

Extract `Source code (zip)` into the game's data folder on your Android device:

```
/Documents/NoGlory/astreon.noglory/game
```

Make sure the game files (such as `script.rpy`, `tl/`, `video/`, and `audio/`) are placed **directly** inside the `game` folder, not inside an extra nested subfolder.

**4. Install the Vietnamese patch (optional)**

Extract `Patch_Vietnamese_v0.4.5.zip` into the **same** data folder:

```
/Documents/NoGlory/astreon.noglory/game
```

When asked, choose **Replace / Overwrite** for any files with the same name. This adds the Vietnamese translation (`game/tl/vietnamese/`) and the language menu entry.

**5. Play in Vietnamese**

Launch the game, open **LANGUAGE** from the main menu, and select **Vietnamese**.

If you skip step 4, the game will still work — just in English, Chinese, Russian, or Spanish.

## Troubleshooting

| Problem | Solution |
| --- | --- |
| The `game` folder does not exist | Run the game once first (step 2), then check the path again. |
| Vietnamese does not appear in the language menu | Make sure the patch was extracted into the same `game` folder, with **Replace / Overwrite** enabled, and that `game/tl/vietnamese/` exists. |
| The app asks to reinstall or won't install | Uninstall the old version of the app first, then install the new APK. |
| The game is in English after installing the patch | Open **LANGUAGE** in the main menu and select **Vietnamese**. |
| Text shows as `?` or boxes | Make sure the patch was fully extracted, including `game/tl/vietnamese/fonts/`. |

## Version History

### v0.4.5 — Current

- Full Android game data for Astreon v0.4.5.
- Vietnamese translation patch (`Patch_Vietnamese_v0.4.5.zip`), including translated text, images, UI, and subtitled videos.
- History screen fix included in the patch.

## Disclaimer

This is an **unofficial, fan-made translation**. It is not affiliated with, endorsed by, or connected to NoGlory, the author of Astreon.

- The game **Astreon** and all of its original content belong to **NoGlory**.
- This translation pack is shared for free, for fans who want to play the game in Vietnamese.
- If you enjoy the game, please support the author on the [official itch.io page](https://noglory.itch.io/astreon).

## Credits

- **Original game:** [NoGlory](https://noglory.itch.io/astreon)
- **Vietnamese translation:** Thanh Bình ([@thanhbinh-ic](https://github.com/thanhbinh-ic))
