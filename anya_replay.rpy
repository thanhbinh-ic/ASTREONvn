label ivy_replay:
    play sound ntsound loop 
    scene black with dissolve
    pause 3.0
    scene s1ee19 with dissolve 
    pause 1.0
    scene s1ee20 with dissolve 
    i "And how do you like it here? Are you enjoying yourself?"
    scene s1ee21 with dissolve 
    i "I hope I won’t disappoint your expectations."
    scene s1ee15 with dissolve 
    mc1 "..."
    scene s1ee17 with dissolve 
    mc1 "Let’s cut to it."
    scene s1ee18 with dissolve 
    i "Why so tense?"
    scene s1ee17 with dissolve 
    mc1 "..."
    scene s1ee18 with dissolve 
    i "Relax a little…"
    i "You look like you’re about to interrogate me."
    scene s1ee17 with dissolve 
    mc1 "Maybe I am."
    i "..."

    scene s1ee22 with dissolve 
    i "You know…"
    scene s1ee23 with dissolve 
    i "People are much more honest when they’re comfortable."
    i "Or… when they’re distracted."

    scene s1ee24 with dissolve 
    pause 1.0

    image Ivy1 = Movie(channel="movie_dp", loop = False, play="video/s1/ivyy1.webm")
    show Ivy1 with dissolve
    $ renpy.pause(2.9, hard=True)
    
    play music unfelt fadein 2.9
    scene s1ee26 with dissolve 
    mc1 "I didn’t come here for that."

    scene s1ee29 with dissolve 
    i "Oh, really?"
    i "Then why did you say yes?"

    scene s1ee30 with dissolve 
    mc1 "We both want the same thing."
    mc1 "Or you think I don’t see what you’re doing?"


    scene s1ee31 with dissolve 
    i "You’re not wrong… but only halfway."
    i "I am curious about you, that’s true… but—"

    scene s1ee34 with dissolve 
    i "This is actually my first time doing something like this…"
    i "In a setting like this."
    scene s1ee35 with dissolve 
    mc1 "Who’s Ember?"
    scene s1ee36 with dissolve 
    i "Persistent, aren’t you…"
    i "You know what, let’s make it a game."
    i "If I win, you get your information."
    i "If you win—"
    scene s1ee35 with dissolve 
    mc1 "Same deal."
    mc1 "Rules?"

    scene black with dissolve
    pause 1.5
    scene s1ee37 with dissolve 
    mc1 "What, getting shy now?"
    mc1 "You didn’t seem the type earlier."
    mc1 "So what changed?"
    scene s1ee38 with dissolve 
    mc1 "..."
    scene s1ee39 with dissolve 
    mc1 "…And?"
    scene s1ee40 with dissolve 
    i "If I hadn’t seen your reaction downstairs… I might’ve thought you weren’t interested."
    i "But then again…"
    scene s1ee41 with dissolve 
    i "I’ve always wondered what it feels… with a real person."
    i "You help me, I help you."
    i "That’s all there is to it."
    scene s1ee42 with dissolve 
    i "..."
    jump ivy1_replay

label ivy1_replay:
    scene s1ee43 with dissolve 
    i "Or do you need a personal invitation?"

    window hide
    image Ivyy3 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy1.webm")
    show Ivyy3 with dissolve
    $ renpy.pause(18.9, hard=True)

    image Ivyy4 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy2.webm")
    show Ivyy4 with dissolve

    i "I… ah…"
    i "(N-no… that’s too much…)"
    mc1 "Who… is Ember?"
    i "(I need to… pull it together—)"
    mc1 "I’m waiting."
    i "Ember…"
    
    i "She’s not just the head…"
    i "She’s the one holding this whole place together."
    i "(Breathing heavier.)"
    i "Ah~"
    i "(N-no… focus. I have to—)"
    mc1 "Arch—…"
    i "H-how are you connected to that scho—"
    i "Ahh—!"
    mc1 "She’s…"
    mc1 "(Hold it together…)"
    mc1 "..."
    i "You keep asking questions…"
    i "But you don’t answer anything yourself."

    mc1 "...someone close to me."
    i "C-close… how close are we talk—"
    pause 1.1

    menu: 
        "Continue.":
            jump ivy2_replay

        "Change angle.":
            jump ivy1_1_replay


label ivy1_1_replay:
    hide Ivyy4
    image Ivyy9 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy3.webm")
    show Ivyy9 with dissolve
    pause 

    menu: 
        "Continue.":
            jump ivy2_replay

        "Change angle.":
            jump ivy1_2_replay

label ivy2_replay:
    image Ivyy5 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy5.webm")
    show Ivyy5 with dissolve
    $ renpy.pause(13.9, hard=True)
    
    image Ivyy6 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy6.webm")
    show Ivyy6 with dissolve
    
    mc1 "What..."
    mc1 "did Lora do?"
    i "(No… I… have to hold—)"
    i "...keep my mouth shut."
    i "Lora…"
    i "She…"
    pause 0.8
    i "..."
    mc1 "Don’t dodge it."
    i "...you already know this isn’t a simple question."
    mc1 "Answer."
    i "Ah… I don’t know…"
    mc1 "(…Not enough.)"
    mc1 "I don’t need fragments."
    i "Hey… what’s gotten into you…"
    mc1 "Finish it."
    i "N-no! A-another ques—"

    pause 1.1

    menu: 
        "Continue.":
            jump ivy3_replay

        "Change angle.":
            jump ivy2_1_replay

label ivy2_2_replay:
    image Ivyy6 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy6.webm")
    show Ivyy6 with dissolve
    pause 
    menu: 
        "Continue.":
            jump ivy3_replay

        "Change angle.":
            jump ivy2_1_replay

label ivy2_1_replay:
    hide Ivyy6
    image Ivyy10 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy8.webm")
    show Ivyy10 with dissolve
    pause 

    menu: 
        "Continue.":
            jump ivy3_replay

        "Change angle.":
            jump ivy2_2_replay

label ivy3_replay:

    image Ivyy7 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy10.webm")
    show Ivyy7 with dissolve
    pause 

    menu: 
        "End.":
            jump ivy4_replay

label ivy4_replay:

    image Ivyy8 = Movie(channel="movie_dp", loop = False, play="video/s1/ivy11.webm")
    show Ivyy8 with dissolve
    $ renpy.pause(5.7, hard=True)

    window show

    
    scene s1ee44 with dissolve 
    pause 1.0
    i "(My first time…)"
    scene s1ee45 with dissolve 
    i "You… still haven’t… answered."
    mc1 "…Yeah."
    scene s1ee46 with dissolve 
    mc1 "(Catches his breath.)"
    mc1 "I don’t know."
    i "..."
    scene s1ee47 with dissolve 
    i "...A debt…"
    i "I hope this isn’t…"
    i "our last meeting."
    scene s1ee48 with dissolve 
    pause 0.5
    scene s1ee49 with dissolve 
    pause 0.5
    scene s1ee50 with dissolve 
    pause 0.5

    stop music fadeout 3.2
    scene black with dissolve 
    pause 5.4

    $ renpy.end_replay()
    return

label Flora_replay1:
    scene s2h40 with dissolve
    mc1 "Fine."
    Fl "(W-wait... seriously?)"
    Fl "(Now what...?)"

    window hide
    image flora8 = Movie(channel="movie_dp", loop = False, play="video/s2/Flora8.webm")
    show flora8 with dissolve
    $ renpy.pause(21.5, hard=True)

    image flora1 = Movie(channel="movie_dp", loop = True, play="video/s2/Flora1.webm")
    show flora1 with dissolve
    Fl "(H-he's huge...)"
    Fl "(And... it's actually throbbing.)"
    pause 0.9
    Fl "(Am... am I doing this right?)"
    Fl "(His face... damn it, I can't tell what he's thinking!)"
    mc1 "Never took you for the type to waste time on pointless foreplay."
    Fl "And you're not the type to deny yourself what you want."
    mc1 "(Her first time? She's a little clumsy...)"
    Fl "Admit it. You like this."
    mc1 "..."
    mc1 "(Still, she's giving it everything she's got. Gotta give her that.)"
    Fl "(He's still getting bigger...)"
    Fl "(M-my whole body keeps trembling.)"
    "Soft moans begin to slip from Flora's lips."
    mc1 "From the sound of it, you're enjoying this more than I am."
    Fl "(W-what?)"
    "She catches her breath."
    Fl "Well, look who's talking."
    Fl "Don't tell me you're already at your limit?"
    mc1 "..."
    Fl "Or are you seriously going to pretend you aren't?"
    mc1 "Keep pushing me and find out."
    Fl "(...His voice changed?)"
    Fl "(It's rougher now... so why is my heart...)"
    pause 0.9
    "Flora's heart began to race, anticipation building as she waited to see what he'd do next."
    Fl "(I shouldn't provoke him...)"
    Fl "(But that voice...)"
    Fl "Or what?"
    Fl "(...why is that so unbelievably hot?)"
    

    image flora2 = Movie(channel="movie_dp", loop = False, play="video/s2/Flora2.webm")
    show flora2 with dissolve
    $ renpy.pause(13.1, hard=True)

    
    
    image flora3 = Movie(channel="movie_dp", loop = False, play="video/s2/Flora3.webm")
    show flora3 with dissolve
    $ renpy.pause(4.8, hard=True)



    image flora4 = Movie(channel="movie_dp", loop = True, play="video/s2/Flora4.webm")
    show flora4 with dissolve
    Fl "(What am I even doing?)"
    Fl "(He didn't ask for this...)"
    Fl "(My hand just... moved on its own.)"
    Fl "(No, no, no! He's going to think I'm some kind of pervert!)"
    Fl "(Throwing myself at him the first chance I get...)"
    mc1 "...Not bad."
    pause 0.8
    "Your thoughts begin to drift, pulling you further away from the moment."
    mc1 "(I have a wife...)"
    mc1 "(And I still went along with this.)"
    pause 0.8
    mc1 "(That makes me a terrible man... {w}An even worse husband.)"
    "Noticing the distant look on [mc1]'s face, Flora quickens her pace, as if desperate to draw his attention back to her."
    Fl "(Y-you idiot...)"
    Fl "(How dare you make that face?)"
    Fl "(...Don't tell me you're not enjoying this.)"
    Fl "(I know I saw this work in those magazines...)"
    Fl "(Y-yeah... he's just pretending.)"
    "Flora's soft moans slip out more and more often, each one harder to hold back than the last."
    mc1 "Something bothering you? Your eyes keep darting around."
    Fl "...You don't exactly look like you're enjoying yourself."
    Fl "You know..."
    Fl "That's surprisingly demotivating."
    mc1 "What, you need me to moan for you?"
    mc1 "That desperate to hear it?"
    Fl "(You smug jerk...)"
    Fl "(Are you seriously messing with me?)"
    Fl "(Fine then.)"
    Fl "(I'll make you regret saying that.)"
    

    image flora5 = Movie(channel="movie_dp", loop = False, play="video/s2/Flora5.webm")
    show flora5 with dissolve
    $ renpy.pause(11.0, hard=True)



    image flora6 = Movie(channel="movie_dp", loop = True, play="video/s2/Flora6.webm")
    show flora6 with dissolve
    mc1 "(She's getting more forceful... Did I strike a nerve?)"
    mc1 "Easy watch the teeth, Flora."
    Fl "(R-right...)"
    Fl "(That'll teach you to keep your head in the clouds.)"
    mc1 "You know... you're a beautiful woman, Flora."
    "For a brief moment, Flora seems to freeze, then she resumes with even greater intensity."
    Fl "(T-this idiot...)"
    Fl "(I almost came just from hearing that.)"
    Fl "(B-but...)"
    Fl "(Hearing something like that actually feels... nice.)"
    Fl "(N-no! Focus! I still have to...)"
    "[mc1]'s breathing grows heavier."
    mc1 "(She's clumsy... but that tongue of hers wraps around me like she's trying to drain every last drop.)"
    mc1 "Ah..."
    "At the sound, Flora's eyes light up with sudden excitement."
    Fl "(Hehe...)"
    Fl "(...That sound isn't bad at all.)"
    Fl "(...What would it feel like to have him... inside me?)"
    "The mere thought sends a wave of desire through her entire body, every part of her aching for [mc]."
    Fl "(P-pull yourself together, Flora!)"
    Fl "(You're stronger than this!)"
    mc1 "I'm close..."
    "As [mc1] tries to pull free from her lips, Flora suddenly draws him back in with all her strength."
    Fl "(NO!)"

    image flora7 = Movie(channel="movie_dp", loop = False, play="video/s2/Flora7.webm")
    show flora7 with dissolve
    $ renpy.pause(13.5, hard=True)

    stop sounds2
    stop music fadeout 5.4
    scene black with dissolve
    pause 3.5

    $ renpy.end_replay()
    return

label Lora_replay1:
    scene black with dissolve
    pause 1.5
    play sounds2 scifidooropen2
    stop sounds1 fadeout 1.0
    play music lora01 fadein 6.2 volume 0.2
    show s3cc6 with dissolve
    "Her hands trembling slightly, she gathers her courage and lets the towel fall away."
    L "...How do I look?"
    mc1 "Beautiful."
    "His words send her heart racing, each beat thundering louder in her chest."
    L "(After dying so many times... hearing you say that again...)"
    "She bites down on her lip, trying to keep her emotions from showing."
    L "(Don’t you dare start crying now.)"
    L "You look wonderful too, darling!"
    show s3cc7 with dissolve
    "Her gaze lingers on him, catching even the slightest tremble that runs through his body."
    mc1 "You're not exactly being subtle."
    L "I’m just... gathering my thoughts!"
    mc1 "You're trembling..."
    L "Because I can hardly wait to feel your warmth again."
    mc1 "(Is that really all it is...?)"
    mc1 "Lora?"
    L "(...You still see right through me.)"
    show s3cc8 with dissolve
    L "I don’t know what I’m supposed to do..." 
    L "Part of me wants to tell you everything..." 
    L "To finally unload this burden, but..."
    show s3cc11 with dissolve
    pause 0.5
    play sounds2 clench
    show s3cc12 with dissolve
    L "...I’m afraid."
    "A sudden shiver courses through her, leaving her entire body trembling with anticipation."
    L "I only... wanted to protect you."
    L "(But I watched you die again and again. Olivia, Norman, Mina... Everyone I ever loved...)"
    pause 1.1
    show s3cc14 with dissolve
    L "Aren’t you going to say anything?"
    show s3cc13 with dissolve
    "An uneasy silence hangs between them, heavy with everything neither of them dares to say."
    mc1 "Just one thing."
    pause 0.9
    mc1 "You did well, darling."
    show s3cc15 with dissolve
    L "(You’re so...)"
    L "(One word. Just one word from you, and I’m already floating somewhere beyond the seventh heaven.)"
    show s3cc16 with dissolve
    L "(Whispering) I love you."
    L "God, how I love you!"
    mc1 "I love you too, darling."
    "Slowly, he closes the distance between them."

    image Lora01 = Movie(channel="movie_dp", loop = False, play="video/s3/Lora01.webm")
    show Lora01 with dissolve
    $ renpy.pause(24.6, hard=True)
    
    image Lora02 = Movie(channel="movie_dp", loop = True, play="video/s3/Lora02.webm")
    show Lora02 with dissolve

    "He slips inside her with surprising ease, drawing a sharp breath from her lips."
    mc1 "(S-she's still so tight...)"
    mc1 "How I've missed you..."
    mc1 "All those years... all that pain..."
    mc1 "And now, finally... you're here."
    "His grip around her tightens, holding her even closer."
    mc1 "I thought I'd lose my mind without you..."
    "Trying to hold back her moans, she struggles to force out a few words."
    L "(It feels so good... The way he pulses inside me... the way he moves...)"
    L "(I don’t want to let him go ever again... Never.)"
    L "What do you... feel?"
    "Her hips begin to sway beneath him, slowly searching for the rhythm."
    L "Do you like it?"
    mc1 "You have no idea..."
    mc1 "And from the sound of it, I'm not the only one enjoying this."
    mc1 "The way your body answers me... those soft moans..."
    mc1 "They tell me everything."
    mc1 "Don't hold back."
    L "I-I just didn’t want anyone to hear us."
    L "...I still have to look Olivia in the eye after this."
    mc1 "Thinking about someone else while you're with me?"
    "With one shallow thrust, he brushes against a particularly sensitive spot."
    L "AAAHH~!"
    "As though something inside her finally breaks free, her moans burst from her all at once, filling the entire room."
    L "AAAHHHHH~~"
    L "Th-that was dirty!"
    mc1 "But you liked it."
    L "...Very much."
    L "But you know, darling... two can play that game."
    mc1 "(Finally got her out of her own head...)"
    mc1 "(Though I may have pushed her a little too far—)"

    image Lora03 = Movie(channel="movie_dp", loop = True, play="video/s3/Lora03.webm")
    show Lora03 with dissolve

    "She tightens around him with every movement, each thrust drawing an even firmer embrace from her body."
    mc1 "Ah... easy, darling."
    mc1 "Loosen your grip a little."
    L "Mmm... I don’t want to let go, darling."
    L "Besides... I know how good it feels."
    mc1 "At this rate, I won't last much longer."
    "She leans closer, her warm breath brushing against [mc]'s ear."
    L "(Whispering) Then fill me to the brim."
    L "(Whispering) We’ve always wanted a baby... haven’t we?"
    mc1 "Y-you fight dirty..."
    "A strained groan slips through [mc]'s clenched teeth."
    mc1 "You know we were never able to—"
    L "Exactly. So don’t you dare deny yourself now."
    L "We are... husband and wife, after all."
    mc1 "You asked for it!"
    L "(So warm...)" 
    L "(If only... we hadn’t been infertile, perhaps...)" 
    L "(Perhaps our entire life would’ve turned out differently.)"
    mc1 "Darling—!"


    image Lora04 = Movie(channel="movie_dp", loop = False, play="video/s3/Lora04.webm")
    show Lora04 with dissolve
    $ renpy.pause(20.4, hard=True)
    stop music fadeout 2.1

    scene black 
    pause 1.5
    $ renpy.end_replay()
    return

label Lora_replay2:
    play music lora02 fadein 2.2 volume 0.5
    show s3cc16 with dissolve
    L "(Whispering) I love you."
    L "God, how I love you!"
    mc1 "I love you too, darling."
    "Slowly, he closes the distance between them."

    image Lora01 = Movie(channel="movie_dp", loop = False, play="video/s3/Lora01.webm")
    show Lora01 with dissolve
    $ renpy.pause(24.6, hard=True)
    
    image Lora02 = Movie(channel="movie_dp", loop = True, play="video/s3/Lora02.webm")
    show Lora02 with dissolve

    "He slips inside her with surprising ease, drawing a sharp breath from her lips."
    mc1 "(S-she's still so tight...)"
    mc1 "How I've missed you..."
    mc1 "All those years... all that pain..."
    mc1 "And now, finally... you're here."
    "His grip around her tightens, holding her even closer."
    mc1 "I thought I'd lose my mind without you..."
    "Trying to hold back her moans, she struggles to force out a few words."
    L "(It feels so good... The way he pulses inside me... the way he moves...)"
    L "(I don’t want to let him go ever again... Never.)"
    L "What do you... feel?"
    "Her hips begin to sway beneath him, slowly searching for the rhythm."
    L "Do you like it?"
    mc1 "You have no idea..."
    mc1 "And from the sound of it, I'm not the only one enjoying this."
    mc1 "The way your body answers me... those soft moans..."
    mc1 "They tell me everything."
    mc1 "Don't hold back."
    L "I-I just didn’t want anyone to hear us."
    L "...I still have to look Olivia in the eye after this."
    mc1 "Thinking about someone else while you're with me?"
    "With one shallow thrust, he brushes against a particularly sensitive spot."
    L "AAAHH~!"
    "As though something inside her finally breaks free, her moans burst from her all at once, filling the entire room."
    L "AAAHHHHH~~"
    L "Th-that was dirty!"
    mc1 "But you liked it."
    L "...Very much."
    L "But you know, darling... two can play that game."
    mc1 "(Finally got her out of her own head...)"
    mc1 "(Though I may have pushed her a little too far—)"

    image Lora03 = Movie(channel="movie_dp", loop = True, play="video/s3/Lora03.webm")
    show Lora03 with dissolve

    "She tightens around him with every movement, each thrust drawing an even firmer embrace from her body."
    mc1 "Ah... easy, darling."
    mc1 "Loosen your grip a little."
    L "Mmm... I don’t want to let go, darling."
    L "Besides... I know how good it feels."
    mc1 "At this rate, I won't last much longer."
    "She leans closer, her warm breath brushing against [mc]'s ear."
    L "(Whispering) Then fill me to the brim."
    L "(Whispering) We’ve always wanted a baby... haven’t we?"
    mc1 "Y-you fight dirty..."
    "A strained groan slips through [mc]'s clenched teeth."
    mc1 "You know we were never able to—"
    L "Exactly. So don’t you dare deny yourself now."
    L "We are... husband and wife, after all."
    mc1 "You asked for it!"
    L "(So warm...)" 
    L "(If only... we hadn’t been infertile, perhaps...)" 
    L "(Perhaps our entire life would’ve turned out differently.)"
    mc1 "Darling—!"


    image Lora04 = Movie(channel="movie_dp", loop = False, play="video/s3/Lora04.webm")
    show Lora04 with dissolve
    $ renpy.pause(20.4, hard=True)
    stop music fadeout 2.1

    stop music fadeout 2.2
    show black with dissolve
    pause 2.2
    $ renpy.end_replay()
    return

label Olivia_replay2:
    play music olivia03 fadein 3.2
    show s3p54 with dissolve
    mc1 "Aren’t you afraid of the consequences?"
    h "Hmm..."
    show s3p55 with dissolve
    h "Not sure what I should fear more—"
    h "An unfaithful man... {w}Or his furious wife."
    show s3p56 with dissolve
    mc1 "Don’t worry. I’ll talk to her about it."
    show s3p57 with dissolve
    h "I don’t doubt that. And if you don’t— I will."
    show s3p58 with dissolve
    h "You know, I thought about it... and honestly, I don’t really want to ruin your marriage."
    show s3p59 with dissolve
    mc1 "(That... didn’t sound convincing at all...)"
    show s3p60 with dissolve
    h "Part of me says — this is wrong."
    show s3p61 with dissolve
    h "But these desires... inside me, they're screaming, craving—"
    mc1 "(Someone’s fighting with herself...)"
    show s3p62 with dissolve
    h "I’m gonna go take a sho—"
    show s3p63 with vpunch
    h "EEEK—!"
    show s3p64 with dissolve
    h "Wait! I’m all dirty..."
    show s3p65 with dissolve
    mc1 "And who said I wanted you clean?"
    show s3p66 with dissolve
    h "Ha, you pervert..."
    h "UGHH♥"
    h "...You're crazy."
    show s3p67 with dissolve
    h "You're... being way too intense today."
    h "I'm seriously gonna lose my mind."
    mc1 "We’re just getting started."
    show s3p68 with dissolve
    h "Hey, wait, what are you—"
    show s3p69 with dissolve
    h "Ha... cocky bastard..."
    mc1 "Admit it, you’re enjoying this."
    h "I... don’t have to admit anything."
    mc1 "But you’re already trembling. And that fiery look in your eyes? It’s fading."
    show s3p70 with dissolve
    h "...You’re just playing dirty."
    mc1 "This isn’t a game. You're the one who asked for heat."
    show s3p71 with dissolve
    h "Heat? Don’t make me laugh."
    h "Tell me — do you still think you're in control here?"
    show s3p72 with dissolve
    mc1 "Control’s not what I need to handle someone like you."
    show s3p73 with dissolve
    h "Oh really? Then what?"
    show s3p74 with dissolve
    mc1 "Just putting you in your place."
    show s3p73 with dissolve
    h "H-ha. Bold of you..."
    show s3p75 with dissolve
    h "Well then... time to prove it."
    show s3p76 with dissolve
    h "So... what’s your move?"

    image olivia3 = Movie(channel="movie_dp", loop = True, play="video/s3/Olivia3.webm")
    show olivia3 with dissolve

    mc1 "My move?"
    mc1 "Tch. You’re already on the edge, and I haven’t even tried yet."
    h "Tried? This... this isn't trying?"
    mc1 "You keep teasing like you’ve got the upper hand... but your body’s honest."
    h "Shut up... you think you’ve figured me out?"
    mc1 "(Those trembling fingers, that shaky breath... You’re barely holding it together.)"

    image olivia4 = Movie(channel="movie_dp", loop = False, play="video/s3/Olivia4.webm")
    show olivia4 with dissolve
    $ renpy.pause(9.7, hard=True)

    image olivia5 = Movie(channel="movie_dp", loop = True, play="video/s3/Olivia5.webm")
    show olivia5 with dissolve

    h "You think I’ll just give in? That easy?"
    mc1 "You already have. You’re just too proud to say it."
    h "Tch... You arrogant...!"
    h "Fine. Then stop talking—"
    h "And *show* me."
    mc1 "Heh. Don’t say I didn’t warn you."
    h "Bring it on."
    mc1 "(She’s fire and thorns... but even fire can melt.)"
    h "(I hate how much I want this... How much I want *him.*)"
    mc1 "Still think you’re in charge?"
    h "No. But I know how to take it back."
    mc1 "Then try. I dare you."
    h "You’ll regret asking for that."
    mc1 "I doubt it. In fact—"
    mc1 "I’m counting on it."

    stop music fadeout 2.2
    show black with dissolve
    pause 2.2
    $ renpy.end_replay()
    return

label Miriel_replay:

    play music mirielscene1 fadein 5.4 
    play sounds1 rustling2
    play sounds3 mmove
    show s3_5ee88 with dissolve
    Mi "(How awkward...)"
    play sounds2 footstep1
    show s3_5ee89 with dissolve
    mc1 "Ready to continue?"
    show s3_5ee90 with dissolve
    Mi "Mhm."
    play sounds3 mmove
    play sounds1 puttable
    play sounds2 tablesq
    show s3_5ee91 with vpunch
    mc1 "Miriel... you’re shaking."
    play sounds1 rustling2
    show s3_5ee92 with dissolve
    mc1 "You’re burning up..."
    Mi "I can’t control it... my whole body feels strange."
    play sounds1 rustling2
    show s3_5ee93 with dissolve
    image Miriel1 = Movie(channel="movie_dp", loop = True, play="video/s3/Miriel1.webm")
    show Miriel1 with dissolve
    mc1 "Miriel... Why are you so...?"
    Mi "I don`t know why my body became like this either..."
    Mi "I was definitely happy to see you there..."
    Mi "But at the same time, my chest started to hurt and-"
    Mi "It woudn`t stop tingling down there..."
    mc1 "You’ve been carrying this alone the whole time, haven’t you?"
    Mi "Even if it`s just for a moment..."
    Mi "Let`s enjoy this, a little bit."
    Mi "Please, fill me up with your love..."
    mc1 "If this is what you want then… I won’t hold back."


    
    show s3_5ee94 with dissolve
    Mi "Ahh...! W-wait! The way you move..."
    play sounds zippis 
    show s3_5ee95 with dissolve
    Mi "Deeper... please, I want more..."
    show s3_5e52 with dissolve

    image Miriel2 = Movie(channel="movie_dp", loop = True, play="video/s3/Miriel2.webm")
    show Miriel2 with dissolve
    Mi "It feels so good! Ah..."
    Mi "Th-this was what I wanted."
    Mi "Because of this I..."
    Mi "Ahn!!!"
    Mi "Ever since that day..."
    Mi "After your words... I coudn`t sleep properly."
    Mi "This is all I could think about..."
    Mi "Until your..."
    Mi "I thought this is why so many girls are hanging around you."
    Mi "And it... Turned me on."
    Mi "Ahn!"
    mc1 "(She’s getting carried away... almost too much.)"
    mc1 "Easy, Miriel. I hear you."
    mc1 "Just breathe — we don’t need to rush."
    Mi "Aren`t you happy that a twenty-year-old elf..."
    Mi "Is throwing herself at you?"
    mc1 ""
    Mi "Don`t you find it thrilling that you`re having sex..."
    Mi "With your protector? Be honest..."
    mc1 "But Miriel, it isn`t sex..."
    mc1 "(Even with my tongue... The inside of her pussy keeps getting tighter.)"
    Mi "Wait [mc1], sth... Coming..."
    Mi "I..."
    scene s3_5e54 with dreamyzoom
    pause 1.1
    scene s3_5e53 with dreamyzoom
    Mi "I`m... Cumming!"
    scene s3_5e53 with dreamyzoom
    pause 0.5
    scene s3_5e53 with dreamyzoom
    pause 0.9
    play sounds1 mirfall
    show s3_5e55 with dissolve
    Mi "That was simply wonderful, thank you for—"
    mc1 "Hold on— you’re not done yet."
    play sounds1 rustling2
    show s3_5e56 with dissolve
    Mi "Wait, wha—"
    mc1 "You didn’t really think I’d stop now, did you?"
    play sounds1 rustling2
    play sounds2 mmove
    show s3_5e57 with dissolve
    Mi "I just cu—"
    show s3_5e58 with dissolve

    image Miriel3 = Movie(channel="movie_dp", loop = True, play="video/s3/Miriel3.webm")
    show Miriel3 with dissolve

    Mi "Huh? It feels a lot deeper all of a sudden!"
    Mi "I might end up cumming too quicly if you keep this up!"
    mc1 "That`s fine."
    mc1 "Remember? We don`t have much time."
    mc1 "Let`s hurry, and wrap it up."
    Mi "Right..."
    Mi "But don’t stop... not yet... Please..."
    Mi "I can feel every bit of you... it’s-"
    scene s3_5e59 with dreamyzoom
    pause 0.5
    scene s3_5e59 with dreamyzoom
    pause 0.9
    scene s3_5e59 with dreamyzoom
    Mi "Cumming!"

    stop music fadeout 6.2
    scene black 
    pause 1.5
    $ renpy.end_replay()
    return

label Ivy_replay_second_scene:

    play music1 ivyscene2 fadein 6.5
    scene s3_5ff33 with dissolve
    i "To be honest, I`m.... A little wet there."
    i "And... It`s come out."
    scene s3_5ff34 with dissolve
    mc1 "The current situation aside..."
    mc1 "(Her unique scent and the odor of her sweat.)"
    mc1 "(Keep clouding my mind.)"
    scene s3_5ff35 with dissolve
    mc1 "(I don`t even know if I shoud be doing this right now.)"
    play sounds3 zippis
    scene s3_5ff36 with dissolve
    mc1 "(But...)"

    image ivyscene2_1 = Movie(channel="movie_dp", loop = False, play="video/s3/Ivyscene1.webm")
    show ivyscene2_1 with dissolve
    $ renpy.pause(7.1, hard=True)
    
    image ivyscene2_2 = Movie(channel="movie_dp", loop = True, play="video/s3/Ivyscene2.webm")
    show ivyscene2_2 with dissolve
    b "I don`t think I can just sit there and do nothing."
    mc1 "Even if they looks not that big. I can admit..."
    mc1 "They heavy."
    i "Mmm… you really don’t waste time, do you?"
    mc1 "Hard to resist when you’re this close."
    i "Ahh… careful— the way you touch me… it makes my head spin."
    mc1 "Then I’ll be gentle… for now."
    i "Don’t tease me like that. Every little move— I can feel it."
    mc1 "You’re trembling. Do you like it this much?"
    i "...More than I’d ever admit. Just… keep going."
    mc1 "Tell me what you want, Ivy."
    i "I want… all of you. Right here, right now."
    i "Mmh… you’re making it hard to think straight."
    mc1 "Then don’t think. Just feel."
    i "Easy for you to say… I’m the one melting here."
    mc1 "Good. That means I’m doing something right."
    i "You know, sitting like this… it almost feels like you’re claiming me."
    mc1 "Almost?"
    i "Tch, don’t get cocky. I didn’t say I mind."
    mc1 "I can tell."
    i "Hah… damn you. Every time I think I’ve got the upper hand, you flip it back on me."
    mc1 "Maybe you never had it to begin with."
    i "Oh really? Then hold me tighter… and prove it."
    i "Mmh… careful, if you keep teasing me like that, I might actually forget how to breathe."
    mc1 "Then I guess I’ll just have to remind you."
    i "Hah… cocky as ever."
    i "You… you don’t play fair."
    mc1 "Neither do you."
    i "Touché…"

    scene s3_5ff37 with dissolve
    i "If we’re doing this… we’re doing it my way."
    i "You’re staring…"
    scene s3_5ff38 with dissolve
    i "Don’t tell me you’re already losing patience."
    mc1 "You’re doing it on purpose."
    scene s3_5ff39 with dissolve
    i "Guilty as charged."
    scene s3_5ff40 with dissolve
    i "Mmh… can you blame me? It’s not every day I get to make you look this… restless."
    scene s3_5ff41 with dissolve
    i "See? I like watching you squirm almost as much as you like watching me."
    i "So… should I keep teasing you, or are you going to beg for more?"
    scene s3_5ff40 with dissolve
    mc1 "You really enjoy tormenting me, don’t you?"
    scene s3_5ff42 with dissolve
    i "Torment? Oh, please… I call it anticipation."
    scene s3_5ff43 with dissolve
    i "You know what makes this fun? Watching your eyes follow every move. Like you can’t decide if you want to grab me, or just sit there and suffer."
    scene s3_5ff44 with dissolve
    mc1 "You’re dangerous."
    i "And you love it."
    i "Patience, [mc1]. I’m not done enjoying this yet."
    mc1 "You really think I’m just gonna sit here and let you run the show?"
    scene s3_5ff45 with dissolve
    i "Mm, I don’t think, I know."
    i "So…"
    i "Like the view?"
    i "Mm… this feels better."
    mc1 "You’re really not planning to give me a choice, are you?"
    i "What can I say… I like the view from here."

    scene s3_5ff47 with dissolve
    mc1 "You’re playing with fire, Ivy."
    i "Good thing I don’t mind getting burned."
    scene s3_5ff48 with dissolve
    i "Mmh… just like that. Don’t stop—"
    i "Mmh… god, I can feel every bit of you…"
    scene s3_5ff46 with dissolve
    i "You don’t know what you’re doing to me right now."
    image ivyscene2_3 = Movie(channel="movie_dp", loop = True, play="video/s3/Ivyscene3.webm")
    show ivyscene2_3 with dissolve
    mc1 "Oh, I think I do."
    i "You’re so unfair… ngh… making me feel like this…"
    mc1 "Says the girl who’s been teasing me all night."
    i "Touché…"
    i "Don’t… don’t slow down now. Please—"
    i "I want it all. Every last drop of you— all of it."
    mc1 "Then take it, Ivy. It’s yours."
    i "Yes… yes… just like that…! Ahh—"
    i "Mmh… you’re staring too hard. You know what happens when you do that, right?"
    mc1 "And what happens?"
    i "I start thinking… maybe I should move… or maybe just… stay right here and make you wait."
    i "Don’t be so eager… patience, remember? Every second counts."
    i "God… I can feel how tense you are. Every muscle, every heartbeat… it’s delicious."
    mc1 "You really enjoy me like this, huh?"
    i "Maybe… or maybe I just like the game. Seeing how far I can push you… before you beg."
    i "Feel that? Every move, every touch… you like it, don’t you?"
    mc1 "Yes… but you’re killing me with this slow torture."
    image ivyscene2_4 = Movie(channel="movie_dp", loop = True, play="video/s3/Ivyscene4.webm")
    show ivyscene2_4 with dissolve
    i "Mmm… good. Then I’ll keep going… enjoy it all. You deserve it."
    i "Don’t even think about rushing… I’m the one setting the pace here."
    i "Feeling good yet? Or do I need to move a little… closer?"
    mc1 "(She’s… she’s driving me insane… every move, every pause… I can’t tell if I should pull her closer or just… stay still.)"
    mc1 "You know, this slow torture… it’s… almost too much."
    i "Almost? Oh, we’re just getting started. I like watching you squirm… feel every second stretch out."
    i "You feel that? Every little twitch… your hands, your chest… I can feel how much you want me."
    mc1 "I… I do… but you’re enjoying this too much."
    i "Of course I am… it’s fun seeing you like this… helpless, tense… completely mine… almost."
    i "Not too fast… savor it. I want to see every reaction… every shiver."
    mc1 "(Every touch… every glance… she’s in complete control… and I can’t look away.)"
    mc1 "You’re unbelievable…"
    i "Mmh… almost there… can you feel it? Every bit of me…"
    i "Mmh… yes… right there… don’t stop…"
    mc1 "(She’s… she’s incredible. Every shiver, every breath… I can feel how much she wants this, and it’s driving me mad.)"
    mc1 "Ivy… you’re… amazing."
    i "Don’t… don’t stop… I need… I need all of you…"
    mc1 "Ivy… you’re driving me insane…"
    i "Almost… almost there… can you feel it? Every bit of us… connected…"
    i "There… yes… I… ahhh…"
    scene s3_5ff49 with dreamyzoom
    i "C-CUMMING!"
    scene s3_5ff49 with dreamyzoom
    pause 0.8
    scene s3_5ff49 with dreamyzoom
    pause 0.5
    
    scene black with dissolve
    i "So… tell me…"
    i "Do you like the view?"
    pause 1.5
    $ renpy.end_replay()
    return

label kali_scene_replay:


    play sounds2 hit
    play sounds3 punch1
    stop music fadeout 0.5
    scene s4_e62 with vpunch
    mc1 "(whispering) bingo..."
    k "Hmph. Congrats."
    k "Now you can go brag to your mommy about beating up a girl."
    mc1 "You really know how to get under my skin."
    k "Enough talking."
    k "If you’re not gonna do anything with me, let go."
    scene s4_e60 with dissolve 
    mc1 "I want an apology."
    k "Huh? And why exactly would I do that?"
    mc1 "(whispering) I’m waiting."
    scene s4_e61 with dissolve 
    k "*Spits*"
    play music1 kali_scene1 fadein 11.4
    scene s4_e60 with dissolve 
    mc1 "..."
    mc1 "(So that’s your answer?)"
    play sounds2 mmove 
    scene s4_e64 with vpunch 
    mc1 "(Fine. Time to put you in your place.)"
    k "..."
    play sounds3 mmove 
    scene s4_e65 with dissolve 
    k "(Took you long enough, idiot.)"
    scene s4_e66 with dissolve 
    "(Her heavy breathing, her eyes roaming over [mc]’s body, as if waiting for his next move.)"
    "([mc] reaches out, grabs her by the waist, and pulls her closer, feeling the heat of her body against his.)"
    k "Finally decided to take control?"
    scene s4_e67 with dissolve 
    mc1 "Before we start… tell me. Do you have any experience?"
    k "And why, does that matter to you?"  
    mc1 "I’m a bad husband, but I try to be an attentive partner."  
    mc1 "If I fail to please you, it’s going to bruise my ego."
    play sounds2 mmove 
    scene s4_e70 with dissolve 
    pause 0.6
    scene s4_e71 with dissolve 
    "(She doesn’t hesitate. A snap of her fingers, and her clothes vanish, leaving her completely exposed before me.)"
    k "You’re thoughtful… cute."
    k "But I don’t give a damn about being careful."
    k "I just want to lose myself."
    play sounds2 clothess 
    scene s4_e72 with dissolve 
    k "Make me forget everything else. Just this moment. Just us."  
    k "I don’t care how."
    k "Rough, gentle, break me if you want."
    k "Just make me forget, about everything."
    scene s4_e74 with dissolve 
    mc1 "(That arrogant smile… strange thing is, I want to make her beg.)"
    mc1 "I can see you’re impatient. But then I thought…"
    "[mc] grinds his cock against her pussy, soaked in her juices, feeling how wet she is."
    k "Hey, hey. Don’t tease. Put it in already."
    scene s4_e73 with dissolve 
    mc1 "..."
    mc1 "What do good girls do?"
    k "Oh, I see…"
    k "So that’s what you’re into? Like it when they beg, huh?"
    scene s4_e72 with dissolve 
    k "Fine."
    k "(whisper) I don’t give a shit about these games. But if it strokes your ego…"
    k "(whisper) Then please. Put that huge cock inside me-"
    k "(whisper) and wreck me."
    
    play sounds2 whoosh     
    image s4_kali_1 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_1.webm")
    show s4_kali_1 with CropMove(time=0.1, mode='slideup')

    "(With one confident thrust, his drill pierced her heavens.)"
    k "Fuuuck… that feels so good…" 
    k "Tell me…"
    k "Mmmmmmh..."
    k "Where the hell were you… all my life?"
    mc1 "You’re… incredible."
    k "Mmmm... Are you enjoying the way my pussy squeezes around your dick?"
    mc1 "(Her pussy grips me like a living thing, pulling me in deeper every time…)"
    mc1 "(No. Hold it together, [mc]. Don’t let her take control.)"
    k "AAAa-a-argh..."
    k "F-Fuck..."
    k "(Did he just get rougher?)"
    mc1 "You're so fucking tight, Kali..."
    mc1 "(That tight… is this her first time?)"
    mc1 "Does it hurt?"
    k "Ahh... What do you think?"
    k "Or is all your attention buried in my filthy little pussy, huh?"
    k "MMmmmmMMmm..."
    k "The way it sounds..." 
    k "Every time you slam that huge cock into me... ahh...."
    k "(I don’t even know what I’m saying anymore...)"
    "(Overwhelmed by pleasure, her mind processes it all as if it were the first time…)"

    mc1 "You really love dirty talk, don’t you?"
    mc1 "Every time... you squeeze me even harder..."
    k "Oh...." 
    k "You have no idea..."
    k "How much..."
    k "Ahhhh..."
    mc1 "(I’m close… at this pace, I’ll lose.)"
    k "It turns me on more when you call things by their real names..."
    k "Aaaahh..."
    k "The sound of my soft, soaked pussy... All those juices spilling out..."
    mc1 "There’s something about it..."
    k "I can feel it tightening…"
    k "Giving itself to you, right in your hands..."
    k "Mmmm..."
    k "But you know..."
    k "Is that really all you’ve got?"
    mc1 "(Listen to her now, she was shaking before, and now...)"
    k "What, went quiet all of a sudden?..." 
    k "Did I... ahhh...." 
    k "Hit your ego?..."
    mc1 "So that’s how it is, huh? Then I won’t hold back."
    k "Come on... I’m waiting."
    k "Drive that huge cock into my pussy. Rip it apart."
    k "Use me, like I’m nothing but the tip of your cock."

    play sounds2 whoosh 
    image s4_kali_2 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_2.webm")
    show s4_kali_2 with CropMove(time=0.1, mode='slideleft')

    mc1 "For someone dripping like that, you’re awfully brave."
    k "Harder..."
    k "More..."
    k "I need more..."
    k "(Riding a cock this big feels... fucking amazing.)"
    k "(But he doesn’t need to know that.)"
    mc1 "You went quiet. Still with me… or already drifting?"
    k "Arrogant bastard..."
    k "You talk too much, use your body instead..."
    k "AAAARRGHH...!"
    k "T-That's it!"
    k "Yes, yes, just like that!"
    k "Aaaahh... ahh... ahhhh..."
    mc1 "(What’s happening to my body… I want more. Harder.)"
    k "AaAaaahh..."
    mc1 "(Feels like I’m back in puberty… damn.)"
    mc1 "Ahhh... Y-Your pussy is squeezing..."
    k "Aaaahhhhhh..."
    k "I c-can't..."
    k "A-A-AAAARGHHH..."
    mc1 "Did you just cum?"
    k "Ahhh... yeahhhh..."
    k "Your cock is driving me insane..."
    mc1 "This isn’t over."    

    play sounds2 whoosh 
    image s4_kali_3 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_3.webm")
    show s4_kali_3 with CropMove(time=0.1, mode='slideleft')

    k "Oh my fuck, don’t stop!"
    k "(I’ve never felt so f-full in my entire life...)"
    k "MMmmmmMMmm..."
    k "(I’m afraid after tonight… I won’t let him go so easily.)"
    k "Aaaahh... ahh..."
    k "I’ll make you..."
    k "Mine...."
    k "Only mine..."
    mc1 "I don’t think so..."
    k "I want to feel you deeper..."
    k "Give it to me hard..."
    k "D-DEEPER..."
    k "I’m almost jealous of that one-eyed girl... She kept all the fun to herself."
    mc1 "Just look at you. You’re dripping like a burst pipe."
    mc1 "Enjoying it so mu-"
    mc1 "AAAARGH."
    k "And what about you? You’re pounding me like you’re trying to fuck me senseless."
    mc1 "You sound like you’re protesting."
    k "Nah. I’m all for it."
    k "I c-can't.."
    k "Again!"
    k "A-A-AAAARGHHH..."
    mc1 "How many times you already climaxed?"
    k "Mmmm..."
    k "Sixth? I lost count after the third..."
    k "Ahhhh..."
    k "AAAa-a-argh..."
    mc1 "You’re way too tight..."
    k "That’s because you’re too fucking big..."

    play sounds2 whoosh 
    image s4_kali_4 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_4.webm")
    show s4_kali_4 with CropMove(time=0.1, mode='slideleft')

    k "Y-yes!"
    k "Harder..."
    k "Give it to me hard..."
    k "D-DEEPER..."
    mc1 "Insatiable."
    mc1 "I... I can’t hold it..."
    k "I think I’m gonna cum..."
    k "Your cock is driving me insane..."
    k "Aaaahhhhhh..."
    k "I c-can't..."

    play sounds2 whoosh 
    image s4_kali_5 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_5.webm")
    show s4_kali_5 with dissolve 
    $ renpy.pause(7.4, hard=True)

    stop music1 fadeout 3.4
    scene black with dissolve 
    pause 2.2 

    $ renpy.end_replay()
    return

label olivia_Third_scene_replay:


    play music1 s4с7_olivia_scene fadein 5.4
    scene s4_g51 with dissolve 
    mc1 "(I don’t know if this is right or wrong… but seeing her like this tears me apart.)"
    mc1 "(And at the same time, if I go through with this, I might shatter Lora’s heart.)"
    scene s4_g52 with dissolve 
    mc1 "No. I can’t, Lora-"
    scene s4_g53 with dissolve 
    h "I… I have her consent."
    h "I don’t know if that changes how you—"
    scene s4_g52 with dissolve 
    mc1 "Are you sure?.."
    scene s4_g53 with dissolve 
    h "I want to be honest. With everyone."
    play sounds2 mmove 
    scene s4_g54 with dissolve 
    mc1 "(Yeah. I really might be the worst husband in existence.)"
    mc1 "(But the way she looked at me… something just snapped in my head.)"
    play sounds3 mmove 
    scene s4_g55 with dissolve 
    mc1 "(Her eyes… so much trust. So much vulnerability. I can’t just walk away from that.)"
    mc1 "(I don’t know if this is just a moment of weakness, but if I cross this line, I’ll have to take responsibility.)"
    play sounds2 rustling2  
    scene s4_g56 with dissolve
    mc1 "(What I’m doing behind Lora’s back… yet she hid the truth to protect everyone.)"
    mc1 "(She lied, but not out of malice.)"
    mc1 "(And still… looking into Olivia’s eyes like this, I can’t turn away.)"
    scene s4_g57 with dissolve 
    mc1 "(So should I stop now? I’ll hurt them both if I don’t.)"
    mc1 "(Yeah… I’m a real bastard.)"
    mc1 "(But having such a beautiful woman standing right in front of me—)"
    scene s4_g59 with dissolve 
    h "What’re you thinking about?"
    scene s4_g58 with dissolve 
    mc1 "With your hair down… you look incredible."
    mc1 "(After this, I’ll have to tell Lora everything.)"
    mc1 "(But the mission—)"
    scene s4_g59 with dissolve 
    h "You’re thinking about her right now, aren’t you?"
    h "I can tell by your eyes."
    h "You don’t know what the right thing to do is."
    scene s4_g58 with dissolve 
    mc1 "Sorry… Before, not knowing the reason, I could ignore it."
    mc1 "But now, knowing what happened, thinking about what a shitty thing I’m doing doesn’t exactly make life easier."
    scene s4_g59 with dissolve 
    h "So… what will it be?"
    h "Do you want to stop here, or—"

    scene s4_g58 with dissolve 
    mc1 "We keep going. I’ll deal with everything else later."
    scene s4_g57 with dissolve 
    h "Then I’ve got an idea how to really grab your attention."
    mc1 "Oh? And what would that be?"
    play sounds2 mmove 
    scene s4_g60 with dissolve 
    h "Two very convincing arguments. Like them?"
    mc1 "They really do look… impressive."
    scene s4_g61 with dissolve 
    h "{b}giggles"
    h "(Hopefully, at least for a couple of minutes, he can relax and get a break from all this.)"
    scene s4_g62 with dissolve 
    h "You know, [mc]…"
    h "I don’t know what happens after this, but—"
    h "No matter what comes next, I’ll always be on your side. Okay?"
    h "Now drop all those thoughts for just a moment and let your brain rest."
    h "In the end, we all need to unwind sometimes."
    scene s4_g63 with dissolve 
    h "(And I’m no exception.)"
    h "(Just thinking about the pleasure sends shivers through my whole body. But even more than that-)"
    h "(Feeling the tension leave him, bit by bit, makes my heart race like crazy.)"
    scene s4_g80 with dissolve 
    mc1 "(Her gaze cuts straight through me… I feel like I’m losing control.)"
    mc1 "Olivia… may I?"
    h "(whispering) Yes..."



    image s4_olivia_3 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_olivia_3.webm")
    show s4_olivia_3 with dissolve 

    h "(These sensations… the way he fills me… the way he holds me, I just melt in his arms.)"
    h "(And his eyes… full of passion and care…)"
    h "(whispering) Please… don’t stop…..."
    h "Aaahh..."
    "A soft, tender moan slipped from her lips."
    mc1 "You’re just… amazing."
    h "I-I... ahh... ahhhh... know..."
    h "I’m not sure..."
    h "(Oh, I feel every movement of his, every touch.)" 
    h "(Everything inside me is pulsing… and that look in his eyes...)"
    h "(Care mixed with desire… I don’t want this to end.)"
    h "(whispering) Don’t stop…"
    mc1 "(I don’t know if this is right… but seeing her like this… it’s intoxicating.)"
    mc1 "You’re too good…"
    h "{b}giggles"
    h "Aaaahh..."
    mc1 "(The way she melts in my arms… that trust—)" 
    mc1 "(I can’t just use her to satisfy a desire.)"
    mc1 "(whispering) Does it hurt?"
    h "MmMMMmm… no, it feels really good…"
    h "(I feel him with every part of my body. His breathing, his heartbeat, the way he pulses inside me...)"
    h "Aaaahhhhhh..."
    h "(All of it together… it’s fogging my mind...)"
    h "Please... keep going!"
    h "Aaaahh... ahh... ahhhh..."
    mc1 "Every part of you is a pleasure to look at."
    
    h "S-stop it, that’s embarrassing..."
    h "And this extra weight-"
    h "Aaahhh... "
    mc1 "Since when did you start thinking so low of yourself?"
    h "I-I..."
    mc1 "Those lovely curves?"
    mc1 "They’re beautiful."
    h "Aaahh... Y-you’re lying.."
    mc1 "And that stomach? Plenty of girls would envy it."
    h "S-stop..."
    h "(Since when do his words affect me like this?! I’m about to-)"
    mc1 "You spend enough time working on your body."
    mc1 "Have some confidence."
    h "(Please stop, I’m about to pass out from pleasure...)"
    h "This is amazing..."
    mc1 "Ahhh..."
    h "I’m… I’m at my limit, I can’t take it anymore..."
    mc1 "Almost… just a little more…"
    h "AaAaaahh..."
    h "(whispering) Please… don’t hold back."


    scene s4_g80 
    pause 0.5
    scene s4_g84 with dreamyzoom
    pause 0.4 
    scene s4_g84 with dreamyzoom
    h "A-A-AAAARGHHH..."
    scene s4_g81 
    pause 0.5
    scene s4_g83 with dreamyzoom
    h "AAaahhh..."
    scene s4_g85 with dissolve 
    h "*Heavy breathing* That… was… incredible…"
    h "How the sensations..."
    mc1 "Amazing… but now—"
    h "Yeah… we should tell Lo-"
    stop music1 fadeout 5.3 

    $ renpy.end_replay()
    return