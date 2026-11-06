init python:
    import getpass
    user_name = getpass.getuser()

    if not hasattr(persistent, 'first_start'):
        persistent.first_start = False


init:
    $ style.say_dialogue.outlines = [(3, "#000000")]  
    $ style.say_dialogue.color = "#FFFFFF"  
    $ persistent.Anya_path_replay == False
    $ style.say_label.outlines = [(3, "#000000")]  

label splashscreen:

    
    show MMLoad with dissolve
    pause 10
    show logo with dissolve
    pause 3
    scene black with dissolve 
    pause 0.5
    show warning1 with dissolve
    pause
    scene black with dissolve 
    pause 0.5
    return

default persistent.skipbutton = False

default tooltip = None
default persistent.profmenu = False
default persistent.mc_info = 0
default persistent.codex = False
default persistent.Anya_path_replay = False
default persistent.Olivia_path_replay = False
default persistent.Ivy_replay = False
default persistent.Flora_replay = False
define persistent.lora_First_scene = False
define persistent.lora_Second_scene = False
define persistent.olivia_Second_scene = False
define persistent.Miriel_replay = False
define persistent.Ivy_Second_scene = False
default persistent.Kalestra_replay = False
default persistent.Olivia_second_replay = False
define glitch_strong = cGlitchMemories(1, 3.0)
define persistent.first_start = True
define MMsong = "audio/MMSong.mp3"
define intro = "images/S0VT/"


image button_animation = Animation("images/MainMenu/ASTART.png", 0.1, "images/MainMenu/START.png", 0.1)
image MMLoad = Movie(play="images/MainMenu/MMWS.webm", loop= True)
image MMWarning = Movie(play="images/MainMenu/Warning.webm", loop=False)
image button_idle = "button_idle.png"  
image button_hover = "button_hover.png"  

transform resize_icon:
    zoom 0.5

#VIDEO IMPORT
image cutscene = Movie(play="video/Loading.webm",loop=False)
image started = Movie(play="video/Start.webm",loop=False) 
image anna0 = Movie (play='video/KISS.webm', loop=True)
image anna0 = Movie (play='video/KISS.webm', loop=True)
image anna1 = Movie (play='video/ABL1.webm', loop=True)
image anna2 = Movie (play='video/ABL2.webm', loop=True)
image anna3 = Movie (play='video/ABL3.webm', loop=True)
image anna4 = Movie (play='video/CUM.webm', loop=False)


#CHARACTER
default persistent.mc_name = "Kael"
define mc = DynamicCharacter("persistent.mc_name", color="#0044ff", substitute=False)
define A = Character('Alexa', color="#FF7F50")
define mc1 = Character('You', color="#0000ff")  
define a = Character('???', color="#00e1ff")  
define aa = Character('???', color="#d0ff00")  
define aaa = Character('???', color="#3432a0")  
define aaaa = Character('???', color="#ff5100")  
define aaaaa = Character('???', color="#69969c")  
define ab = Character('???', color="#ff0033")  
define B = Character('Rosie', color="#c07272")  
define b = Character('Both', color="#ff8899")  
define c = Character('Jack', color="#3CB371")  
define C = Character('Anya', color="#F4A460")  
define CC = Character('Anya?', color="#2986cc")  
define d = Character('Nikita', color="#708090")  
define D = Character('Man', color="#FF6347")  
define E = Character('Everyone', color="#d9d9d9")  
define ex = Character('Executor', color="#bfbfbf")  
define em = Character('Ember', color="#d896ff")  
define e = Character('Daniel', color="#9932CC")  
define el = Character('Elaena', color="#9932CC")  
define f = Character('Noon', color="#8fc923")  
define F = Character('General', color="#56c000")  
define Fl = Character('Flora', color="#009f30")  
define G = Character('Girl', color="#9370DB")  
define g = Character('Soldier A', color="#6e75ff")  
define gg = Character('Soldier B', color="#ffc3a0")  
define ggg = Character('Soldiers', color="#b4ff96")  
define gggg = Character('Soldier C', color="#e89cff")  
define ggggg = Character('Soldier D', color="#ff9696")  
define gggggg = Character('Soldier E', color="#ff9696")  
define H = Character('System', color="#af80ff")  
define h = Character('Olivia', color="#3daf50")  
define o = Character('Ostorius', color="#3daf80")  
define i = Character('Ivy', color="#3dafc0")  
define J = Character('Frog', color="#00ff15")  
define j = Character('Jacob', color="#D2691E")  
define k = Character('Kalestra', color="#D2691E")  
define l = Character('Robot', color="#9350DB")  
define L = Character('Lora', color="#ff009d")  
define Lor = Character('Lora?', color="#ff009d")  
define Lo = Character('Sunshine', color="#ff009d")  
define M = Character('Mina', color="#5F9EA0")  
define Mi = Character('Miriel', color="#20b8aa")  
define m = Character('Mona', color="#F08080")  
define n = Character('NoGlory', color="#4169E1")  
define am = Character('Astoria', color="#6495ED")  
define N = Character('Norman', color="#FF4500")  
define Ne = Character('Norman?', color="#ff1100")  
define new = Character('News report', color="#ff6600")  
define R = Character('Dr. Li Wei', color="#778899")  
define r = Character('Radio', color="#556677")  
define ri = Character('Richard', color="#899bc0")  
define ry = Character('Riya', color="#899bc0")  
define rey = Character('Ray', color="#5566aa")  
define y = Character('Yong', color="#7788bb")  
define t = Character('Troy', color="#aaaa99")  
define S = Character('Shiya', color="#4B0082")  
define s = Character('Sofia', color="#FF1493")  
define sss = Character('Lili', color="#fc57a3")  
define ss = Character('Robot', color="#ff33cc")  
define sci = Character('Scientist 1', color="#ff3d6a")  
define x = Character('Alexandro', color="#DC143C")  
define X = Character('Amelia', color="#f2286e")  
define z = Character('Zombie', color="#dc1a45")  
define zo = Character('Zoya', color="#dc1a45")  
define w = Character('Winter', color="#dc1a45")  
define ad = Character('Reconstruction', color="#ffd900")  
define aS = Character('Aisha', color="#ffd900")  
define add = Character('Profiler', color="#e41157")  
define az = Character('Azarkhan', color="#9400d3")
define yin = Character('Yin', color="#9400d3")
define sel = Character('Selvaria', color="#9400d3")
define scar = Character('Scarleia', color="#3e3f6b")
define Evrel = Character('Evrelia', color="#3e3f6b")
define v = Character('Veira', color="#3e3f6b")
define Go = Character('Gorem', color="#3e3f6b")
define keep1 = Character('1-ый Хранитель', color="#3e3f6b")
define keep2 = Character('2-ой Хранитель', color="#3e3f6b")
define keep3 = Character('Third', color="#3e3f6b")
define keep4 = Character('4-ый Хранитель', color="#3e3f6b")
define keep5 = Character('5-ый Хранитель', color="#3e3f6b")
define keep6 = Character('6-ой Хранитель', color="#3e3f6b")
define keep7 = Character('7-ой Хранитель', color="#3e3f6b")
define keep8 = Character('8-ой Хранитель', color="#3e3f6b")
define elf = Character('Elf', color="#3e3f6b")
define ketr = Character('Ketrin', color="#3e3f6b")
define cj = Character('Jacks daughter', color="#3e3f6b")
define npc = Character('NPC', color="#3e3f6b")
define lad = Character('Lady', color="#3e3f6b")


transform slide_left_to_right:
    xpos 0.51 
    ypos 0.55
    linear 2.0 xpos 0.05 ypos 0.15


define lora_relationship = 1
define flora_relationship = 1
define olivia_relationship = 1
define kalestra_relationship = 1
define miriel_relationship = 1
define astoria_relationship = 1
define evrelia_relationship = 1
define anya_relationship = 1

#PROLOGUE
label start:   
    $ renpy.music.set_volume(0.5, channel='music')
    $ renpy.music.set_volume(1.0, channel='sound')
    stop music fadeout 2
    show bb 1 with dissolve
    $ persistent.mc_name = renpy.input("My name: (Default Kael)")
    pause 1.0
    if persistent.mc_name == "":
        $ persistent.mc_name = "Kael"

    play sound mouseclick
    show pause 
    n "Excuse me, but I need your attention for just a couple of minutes."

    play music relaxing volume 1.0
    $ persistent.profmenu = True
    scene s0tt0 with dissolve
    a "..."
    scene s0tt1 with dissolve
    n "Dear?"
    n "Be nice."
    pause 0.8
    a "Mhm."
    play sounds2 mmove 
    scene s0tt2
    pause 0.4
    scene s0tt3 with dissolve
    pause 0.4
    scene s0tt2 with dissolve
    pause 0.4
    play sounds3 clench 
    scene s0tt4 with dissolve
    a "…Then just one thing."
    a "Top left, there’s an icon."
    play sounds3 mmove
    scene s0tt5 with dissolve
    a "…That’s your best friend."
    a "Codex, map, gallery… all our…"
    play sounds2 whoosh 
    scene s0tt6 
    a "…memories."
    play sounds3 hug2 
    scene s0tt7 with dissolve
    aa "There you are!"
    aa "Move it, or you’re gonna miss everything."
    play sounds2 mmove 
    scene s0tt8 with dissolve
    a "Wha—"
    scene s0tt9 with dissolve
    a "But the tutorial-"
    play sounds3 clothess 
    scene s0tt10 with dissolve
    pause 0.6
    scene s0tt11 with dissolve
    aaa "Hm..."
    scene s0tt12 with dissolve
    pause 0.7
    aa "Eh, whatever."
    aa "He’ll quit in thirty minutes anyway."
    scene s0tt13 with dissolve
    pause 0.9
    aa "And you..."
    aa "Do you need a personal invitation?"
    play sound mouseclick
    stop music
    scene black 
    aaa "Yeah, yeah… shorty."
    window hide
    pause 3.3
    


    image loading1 = Movie(channel="movie_dp", loop = False, play="video/loading1.webm")
    show loading1 with dissolve
    $ renpy.pause(62.0, hard=True)

    play sounds1 helicopterin fadein 1.0 loop
    scene s0a1 with dissolve
    show opdr with dissolve 
    "Earth, Al-Zahira — Middle East. Year 2018."
    mc "..."
    hide opdr with dissolve 
    play sounds2 notificationphone 
    "You’ve got a new message."
    play sounds4 rustling2 
    show s0a3 with dissolve
    Lo "Darling, darling!" 
    Lo "You won’t believe what just happened!"
    mc "What is it?"
    Lo "I got promoted!" 
    show s0a4 with dissolve
    mc "Heh… I knew you would."
    mc "Congrats, sunshine."
    Lo "You have no idea how happy I am!"
    Lo "Feels like a billion nanoparticles are about to tear me apart!"
    show s0a5 with dissolve
    mc "Let’s hope not."
    Lo "Oh, come on…" 
    Lo "We actually had a guy go out like that once. Beautiful explosion, though!"
    mc "..."
    Lo "Kidding! {w=0.5}Maybe..."
    mc "Still getting used to your humor."
    scene s0a3 with dissolve
    Lo "Grumpy… Anyway, I’ve been invited to a top-secret meeting!"
    Lo "The topic’s a bit unsettling."
    Lo "Something related to teleportation… I think."
    mc "Teleportation?"
    Lo "Yeah. I don’t have the full picture, but…"
    Lo "They said it requires… something organic."
    mc "Organic?"
    Lo "Yeah..."
    Lo "And before you ask, no, this isn't hallway gossip."
    Lo "They moved half my clearance overnight."
    Lo "Someone high up wants this buried and fast-"
    scene s0a5 with dissolve
    "Connection lost."
    mc "..."
    mc "(Organic... Teleportation...)"
    mc "(Sounds too close to our briefing.)"
    mc "(…Not good.)"
    play sounds4 rustling2 
    show s0a8 with dissolve
    pause 1.8
    h "Something happen?"
    h "Your face just… ain’t yours right now."
    show s0a9 with dissolve
    mc "..."
    h "[mc]?"
    pause 1.1
    show s0a10 with dissolve
    mc "You ever heard of… things that don’t make sense?"
    scene s0a9 with dissolve
    pause 0.7
    h "What, like ghosts?"
    h "Heard the stories. Why?"
    show s0a11 with dissolve
    mc "No."
    mc "Forget it."
    show s0a12 with dissolve
    mc "(…Hope I’m wrong.)"
    pause 1.1
    h "You’ve been off this whole ride."
    h "You gonna talk… or keep playing silent hero?"
    play sounds4 mmove
    show s0a13 with dissolve
    S "Quit pressuring him, Olivia!"
    show s0a14 with dissolve
    S "I’m sure he’s got more important things to deal with than babysitting us."
    show s0a15 with dissolve
    h "God, I hate it when he shuts us out."
    show s0www1 with dissolve
    h "We’re a team."
    h "You don’t have to carry this alone."
    h "We’re here. Use it."
    scene s0a14 with dissolve
    S "…Olivia, you’re going to break him at this rate."
    S "Let the man breathe."
    show s0a16 with dissolve
    x "Haha..." 
    x "Hey, hey, don’t start fighting, ladies."
    show s0a18 with dissolve
    S "…We’re not fighting."
    show s0a17 with dissolve
    x "Commander! I’m with Liv, we’re a team!"
    x "To me, you’re like the greatest crocodile in the world!"
    x "So don’t bottle it up, yeah?"
    show s0a20 with dissolve
    mc "Focus."
    mc "We stop the deal."
    mc "Everything else — after."   
    show s0a21 with dissolve
    c "He’s right. We’re acting like kids right now."
    show s0a22 with dissolve
    x "...Fair enough."
    pause 1.1
    m "Hope you haven’t forgotten something."
    show s0a23 with dissolve
    m "This is the commander’s last operation."
    m "So whatever happens, we owe him a drink after this."
    show s0a24 with dissolve
    pause 1.1
    x "Drinks? Count me in!"
    h "Yeah… wouldn’t say no to a cold beer."
    c "Dibs on not paying."
    m "..."
    show s0a25 with dissolve
    m "Way to kill the mood."
    m "You could at least pretend to offer."
    show s0a26 with dissolve
    g "..."
    play sounds3 radio volume 0.4 loop
    show s0a27 with dissolve
    g "Hate to break up the cozy chat, but we’re almost there."
    show s0a28 with dissolve
    g "We’ve got five minutes."
    show s0a29 with dissolve
    g "Keep your heads down, locals aren’t exactly friendly."
    gg "Three minutes to arrival."
    stop sounds3 
    show s0a30 with dissolve
    mc "Roger that."
    show s0a31 with dissolve
    mc "No fighting the locals unless provoked. Stick together."
    show s0a32 with dissolve
    mc "Everyone ready?"
    show s0a33 with dissolve
    E "..."
    show s0a34 with dissolve
    mc "Good."
    show s0a35 with dissolve
    gg "One minute! Brace yourselves — landing’s gonna be rough."
    window hide
    
    image s0transition0 = Movie(channel="movie_dp", loop = False, play="video/s0transition0.webm")
    show s0transition0 with dissolve
    $ renpy.pause(12.0, hard=True)

    window auto
    show s0a37 with dissolve
    pause 0.5
    show s0a38 with dissolve
    mc "Move, move, move!"
    show s0a39 with dissolve
    pause 0.5
    show s0a40 with dissolve
    h "Clear!"
    c "Clear!"
    x "No hostiles!"
    show s0a42 with dissolve
    mc "Shiya, status?"
    show s0a43 with dissolve
    S "Clear. I’ve got the scanner."
    stop sounds1 fadeout 5.1
    play sounds3 radio volume 0.1 loop
    show s0a44 with dissolve
    mc "Hawk, this is 6-Bravo. Landing successful."
    show s0a45 with dissolve
    g "6-Bravo, Hawk copies. Happy hunting."
    play sound raincity3 loop volume 0.3
    stop sounds3
    mc "..."
    play music covenant fadein 1.5 loop
    show s0a46 with dissolve
    mc "Move out!"
    play sounds2 grouprun volume 0.3
    scene black with dissolve
    pause 1.0
    show s0a47 with dissolve
    S "Where is everyone?"
    m "Not a soul. Like they just… vanished."
    c "I don’t like this silence."
    show s0a48 with dissolve
    h "Yeah…"
    h "Me neither."
    show s0a49 with dissolve
    mc "..."
    mc "(This place was alive two days ago…)"
    mc "(Satellite feed showed traffic here forty-eight hours ago.)"
    mc "(Now nothing.)"
    mc "(No bodies. No blood. No evacuation trail.)"
    m "Commander? How far?"
    mc "Rendezvous point in sight. Still no resistance."
    x "Then let’s hit them hard when we find them!"
    show s0a50 with dissolve
    S "Or maybe they’re waiting to do that to us?"
    c "Exactly. Charging in is a bad idea."
    mc "Recon first."
    mc "House at ten o’clock. Move."
    scene black with dissolve
    pause 1.0
    show s0a51 with dissolve
    "Rainwater drips through cracks in the ceiling."
    m "Commander… doesn’t this place look unstable?"
    m "Like it’s held together by duct tape and good intentions."
    show s0a52 with dissolve
    mc "Didn’t have much choice. Most buildings here are in the same crappy shape."
    show s0a54 with dissolve
    h "This doesn’t make sense…"
    h "Place was brand new… and now it looks like it aged twenty years overnight."
    show s0a55 with dissolve
    m "Feels like a zombie horror flick."
    scene s0a54 with dissolve
    h "I hate horror…"
    show s0a56 with dissolve
    mc "A few days ago we got a tip. Anonymous."
    mc "Said the disappearances are tied to a deal with Azarkhan."
    pause 1.1
    mc "At first HQ thought it was bait."
    mc "Then the drone footage came in."
    mc "Whole blocks emptied overnight."
    show s0a57 with dissolve
    h "Great. That helps."
    h "You got anything else?"
    scene s0a56 with dissolve
    mc "Only that the cargo contains an unknown substance."
    mc "Unstable. Unknown origin."
    mc "And everyone who tried to inspect it either vanished..."
    scene s0a57 with dissolve
    h "Perfect."
    h "Dropped into god-knows-what, for god-knows-why…"
    m "Always wanted to play the hero."
    show s0a58 with dissolve
    h "Pretty sure heroes don’t stack bodies every day."
    m "Then maybe stop shooting back."
    show s0a59 with dissolve
    h "[mc], this is it, right?"
    h "We’re not going deeper?"
    show s0a60 with dissolve
    mc "Yeah. We’re here. If HQ's timing is right, the deal goes down in a couple of hours."
    show s0a61 with dissolve
    mc "We prep while we’ve got time."
    show s0a62 with dissolve
    c "I’ll check the upper floors."
    show s0a64 with dissolve
    mc "Alexandro, go with Jack."
    show s0a65 with dissolve
    c "Sir? You can’t be serious. I can’t stand that guy."
    x "With him? No thanks."
    show s0a66 with dissolve
    mc "Last thing I want is reporting you both dead. Pair up. Got it?"
    b "Sir, yes, sir…"
    show s0a67 with dissolve
    S "Commander? I think I found the perfect spot."
    show s0a68 with dissolve
    mc "What do you mean?"
    show s0a69 with dissolve
    S "Building at eleven o’clock. Overlooks the entire area. Perfect vantage point."
    scene s0a68 with dissolve
    mc "Hold off. You’ll go there with Jack and Alexandro after their recon."
    scene s0a69 with dissolve
    S "Yes, sir..."
    mc "Mona, Liv! Grab the C4. You’re with me."
    stop music fadeout 2.0
    stop sound fadeout 1.0
    play sounds1 desertwind loop volume 0.2 fadein 1.5
    scene black with dissolve
    pause 1.0


label war2:
    "A day and a half later."
    show s0w2 with dissolve
    mc "(We’ve been stuck here for so long… The deal was supposed to happen hours ago, and yet, we’re still here.)"
    mc "(Thirty-six hours.)"
    pause 1.1
    mc "(Food left on tables, cars abandoned mid-street. Doors open.)"
    mc "(Like the whole city stood up at once...)"
    mc "..."
    mc "(Don’t spiral, [mc]. It’ll be fine.)"
    show s0w1 with dissolve
    mc "(Right?)"
    stop sounds1 fadeout 0.5
    play music intro1 fadein 3 volume 0.7 loop 
    play sound camera
    scene s0i1 with dissolve
    pause 1.0
    scene s0i2 with dissolve
    pause 1.0
    show s0i3 with dissolve
    mc "You sure about this?" 
    
    show s0i4 with dissolve
    L "No."
    show s0i5 with dissolve
    L "But if I keep saying “just one more minute,” we’ll be here all night." 
    show s0i6 with dissolve
    mc "..."
    scene s0i7 with dissolve
    pause 1.0
    show s0i8 with dissolve
    mc "Honestly?"
    mc "I don’t mind."
    mc "Standing here with you beats pretty much anything else."
    show s0i9 with dissolve
    L "Stop that. You're gonna make me tear up before we even start."
    show s0i10 with dissolve
    mc "That’s kind of the goal, isn’t it?  "    
    show s0i12 with dissolve
    mc "Emotional bomb right at the intro. Win them over fast."   
    scene s0i13 with dissolve
    pause 1.0
    scene s0i14 with dissolve
    pause 1.0
    scene s0i15 with dissolve
    pause 1.0
    show s0i16 with dissolve
    L "Oh god. Is this a sales pitch?"
    scene s0i17 with dissolve 
    pause 1.0
    scene s0i18 with dissolve
    pause 1.0 
    show s0i19 with dissolve
    mc "Always."
    mc "Hi, I’m [mc], and this is the love of my life. Limited-time offer. Zero regrets, all heart."
    show s0i20 with dissolve
    L "You're ridiculous."
    L "…But you’re also wearing your shirt inside out."
    show s0i21 with dissolve
    mc "…What?"
    scene s0i22 with dissolve
    pause 1.0
    show s0i23 with dissolve
    mc "…Great. Nothing says “romantic message to the parents” like looking mildly concussed."
    show s0i24 with dissolve
    L "{b}laughs{/b}"
    show s0i25 with dissolve
    L "It's perfect. "
    show s0i26 with dissolve
    L "Makes me feel a little less nervous, honestly.  "
    show s0i27 with dissolve
    L "You mess up, too."
    show s0i29 with dissolve
    mc "All the time."
    mc "Especially when it comes to you."
    scene s0i28 with dissolve
    L "…You’re really sure you want to do this?"
    show s0i29 with dissolve
    mc "I was sure the second I met you."
    play sound whoosh
    show s0i30 with CropMove(time=0.1, mode='slideleft')
    L "..."
    pause 1.4
    show s0i31 with dissolve
    mc "..."
    show s0i32 with dissolve
    mc "And what was that just now?"
    show s0i33 with dissolve
    L "Just showing you how much I love you."
    show s0i34 with dissolve
    mc "Okay. Camera’s rolling."
    mc "Deep breath?" 
    show s0i35 with dissolve
    L "Already took three."
    show s0i36 with dissolve
    mc "Alright. Let's do it."
    show s0i37 with dissolve
    mc "And done, we’re good to go. {w}I’m pressing the button now, and... {w}recording started."
    scene s0i38
    pause 1.0
    scene s0i39
    pause 1.0
    show s0i40 with dissolve
    b "..."
    show s0i45 with dissolve
    mc "Ahem ahem."
    show s0i46 with dissolve
    mc "Hi, Mom. Hi, Dad."
    scene s0i47 with dissolve
    pause 1.0
    scene s0i48 with dissolve
    pause 1.0
    scene s0i49 with dissolve
    pause 1.0
    scene s0i50 with dissolve
    pause 1.0
    mc "(Alright… pull yourself together.)"
    show s0i51 with dissolve
    mc "If you’re watching this, then I guess… I wanted you to meet her."
    show s0i52 with dissolve
    mc "She’s the reason I laugh more. Sleep less. Breathe deeper.  "
    show s0i53 with dissolve
    mc "This is Lora."
    mc "And the other day, I decided to commit my life to her."
    mc "And she said... {w}Yes."
    show s0i54 with dissolve
    L "Hi..."
    L "And yes, I did. I said yes. Loudly. Twice."
    show s0i58 with dissolve
    mc "You also punched me in the arm."
    show s0i56 with dissolve
    L "That was nerves."
    show s0i57 with dissolve
    mc "That was love."
    show s0i59 with dissolve
    L "We wanted to keep this moment. Just for us." 
    L "But then we thought, maybe you’d want to see it too."
    L "What this feels like. Right now."
    stop music fadeout 2
    play sounds1 desertwind loop volume 0.2 fadein 1.5
    show s0w1 with dissolve
    b "Just… us."
    show s0w2 with dissolve
    mc "(Hope her meeting went well...)"
    mc "(Last thing I need is her upset when I get back.)"
    play sound stepember1
    show s0w3 with dissolve
    c "What are you staring at, Commander?"
    c "Oh… your darling wife, as always."
    c "That explains the smile."
    show s0w4 with dissolve
    mc "Still dead air?"
    play sounds2 rustling2
    show s0w5 with dissolve
    pause 0.5
    show s0w6 with dissolve
    c "Dead as the grave, sir."
    c "Not a single ping since yesterday… and it’s looking worse by the hour."
    c "Still… maybe we should wait a little longer."
    show s0w7 with dissolve
    x "Two days in this furnace and we’re still just sitting here?"
    x "How much longer are we supposed to wait? Where the hell are they?"
    x "¡Que me besen el culo si creen que voy a quedarme aquí más tiempo!"
    show s0w9 with dissolve
    c "Speak English, or at least something we can understand!"
    play sounds3 rustling2
    show s0w10 with dissolve
    x "What’s your problem, huh?"
    play sound rustling2
    show s0w11 with dissolve
    x "What other language should I be speaking?"
    play sound rustling2
    show s0w12 with dissolve
    x "I risk my life like the rest of you."
    x "I’ve earned the right to speak however the hell I want."
    show s0w14 with dissolve
    c "Sure, but none of us know what you’re saying when you go off like that."
    c "It’s just noise, man. Noise and attitude."
    play sounds2 rustling2
    show s0w13 with dissolve
    x "Eso no es problema mío si tu cerebro diminuto no pudo molestarse en aprender algo más que tu inglés de mierda."
    show s0w15 with dissolve
    b "..."
    show s0w16 with dissolve
    c "Here we go again..."
    show s0w17 with dissolve
    mc "Dial it down. Both of you."
    mc "I’m not having you kill each other before we even start."
    show s0w18 with dissolve
    c "Alright, alright. Fair."
    c "Guess I forget that sometimes… I’ll try."
    show s0w19 with dissolve
    c "Hey, big guy. I’m sorry."
    show s0w20 with dissolve
    x "Go screw yourself."
    scene s0w19 with dissolve
    c "Closest thing to peace we’ll get."
    show s0w21 with dissolve
    m "Commander? {w=0.6}Mind if I ask something?"
    show s0w29 with dissolve
    mc "Shoot."
    scene s0w21 with dissolve
    m "You said you got married not long ago, right?"
    show s0w29 with dissolve
    mc "Yeah. Recently."
    scene s0w21 with dissolve
    m "So… what’s she like? Your wife."
    show s0w22 with dissolve
    c "The most amazing woman in the world!"
    c "Which is why my daughter’s so beautiful and perfect."
    show s0w23 with dissolve
    m "Sorry? I wasn’t asking you..."
    show s0w24 with dissolve
    c "Just wanted to share."
    show s0w25 with dissolve
    mc "How old is your daughter now?"
    scene s0w22 with dissolve
    c "Turned three last week."
    scene s0w24 with dissolve
    c "Crazy how fast they grow when you’re always gone."
    scene s0w23 with dissolve
    m "At least someone’s growing up during all this..."
    show s0w27 with dissolve
    h "Still… [mc], what’s the objective?"
    h "‘Cause I’ll be honest, that previous briefing?"
    h "Didn’t get shit."
    show s0w28 with dissolve
    m "You’re not the only one."
    m "Even I found it strange."
    m "{b}‘Reach the designated location and await further orders’{/b} — seriously?"
    scene s0w27 with dissolve
    h "See? Not just me."
    h "So quit holding out."
    h "What did HQ actually tell you?"
    scene s0w29 with dissolve
    mc "Intel says we’ve got contacts tied to Azarkhan Temirov."
    play sounds2 rustling2
    show s0w30 with dissolve
    m "And who is that supposed to be?"
    mc "Runs a neural implant lab..." 
    mc "...and he’s the one pulling the strings behind Masquerade."
    show s0w31 with dissolve
    S "And that makes him our target?"
    mc "No." 
    mc "But it’s enough to put him on our list."
    scene s0w27 with dissolve
    mc "Job’s simple. We stop the deal."
    scene s0w11 with dissolve
    x "The deal we’ve been sitting on for TWO DAMN DAYS!"
    mc "..."
    scene s0w9 with dissolve
    h "Maybe he’s stuck in traffic or something…"
    mc "We stay until it happens."
    m "But why?"
    scene s0w31 with dissolve
    mc "Because of what they’re trading."
    show s0w32 with dissolve
    mc "HQ calls it a substance sample."
    m "Calls it?"
    mc "That's the problem. They don't know what it is."
    mc "The city goes dark. Then the cargo appears."
    x "A substance sample. Big deal. What’s all the fuss about?"
    show s0w33 with dissolve
    mc "Scans detected its effect, not what it is."
    mc "Not the source."
    pause 1.1
    mc "Command is treating each unit like a weapon of mass destruction."
    x "Each one?"
    mc "Yeah."
    mc "And we don't know how many there are."
    show s0w34 with dissolve
    mc "We scout first."
    mc "Assess."
    mc "Then we move."
    E "Understood."
    show s0w35 with dissolve
    mc "Questions?"
    h "Why would Azarkhan show up himself?"
    h "Doesn’t seem like his style."
    mc "Last guy who worked with him is dead. He doesn’t have a choice."
    mc "And that cargo? Too important to delegate. He’ll show."
    mc "Anything else?"
    h "None."
    mc "Then we wait."
    play sounds3 radio volume 0.1 loop
    show s0w36 with dissolve
    r "6-Bravo, this is Eagle-2. Do you copy?"
    r "A convoy has been spotted approaching you from the east at high speed."
    r "Confirm you’ve received this information."
    stop sounds3
    show s0w37 with dissolve
    mc "Eagle-2, this is 6-Bravo. Copy. ETA?"
    play sounds3 radio volume 0.1 loop
    show s0w38 with dissolve
    r "6-Bravo, ETA is 20 minutes."
    r "They’re moving fast — two vehicles in total." 
    r "Do not engage first. {w}Await further instructions. {w}Out."
    stop sounds3
    play sounds2 mmove
    play sounds3 rustling2
    play music dt fadein 1.8 loop
    show s0w40 with dissolve
    mc "Positions. Twenty minutes."
    mc "Move. Now."
    scene black with dissolve
    pause 1.5

    

    image firstmach = Movie(channel="movie_dp", loop = False, play="video/firstmach.webm")
    show firstmach 
    $ renpy.pause(8.5, hard=True)

    play sounds3 rustling2
    show s0w41 with dissolve
    x "Finally, some action... {w=0.7}Can’t wait to shred these bastards to pieces. {w=0.7}Just show yourselves."
    show s0w111 with dissolve
    pause 1.0
    show s0w42 with dissolve
    mc "Shiya. You in position?"
    show s0w43 with dissolve
    S "Affirmative."
    scene s0w42 with dissolve
    mc "Report."
    scene s0w43 with dissolve
    S "Movement spotted to the east, two vehicles."
    S "One vehicle to the north. {w=0.7}Nothing else."
    show s0w45 with dissolve
    mc "Hold. No engagement without my order."
    x "Come on, Commander!"
    x "We can take them, just a handful of guys. Two volleys, and they’re done."
    show s0w46 with dissolve
    S "And what if this is only part of the group?"
    S "Or did your dumb brain skip that thought and jump straight to action?"
    x "What did you just say? Stupid brain?! {w=0.7}Oh, you little perra!"
    S "Oh, fuck off."
    show s0w47 with dissolve
    mc "Enough."
    mc "Alexandro — position. Now."
    mc "Shiya — continue observation."
    S "(whispering) Always complaining like a kid... {w=0.7}(louder)Understood."
    S "Aside from this group, no enemies in sight."
    show s0w48 with dissolve
    mc "Target?"
    S "Negative. The target isn’t visible. {w=0.7}There’s a chance this is a decoy. {w=0.7}What are your orders, sir?"
    mc "We wait."
    S "No outer perimeter either."
    S "No scouts. No overwatch."
    S "For cargo this hot... that's wrong."

    mc "(Either they're idiots...)"
    mc "(Or they know we're here.)"
    play sound cardoor
    show s0w50 with dissolve
    pause 1.0
    show s0w51 with dissolve
    play sounds2 stepember
    pause 0.5
    show s0w52 with dissolve
    a "Well, well... it’s been a long time."
    a "Glad to see you after all these years, my old friend."
    a "How’s the wife? {w=0.7}Daughter? {w=0.7}Everything great, I assume?"
    show s0w49 with dissolve
    az "I don’t have time for this. Let’s get to the point."
    az "Do you have the goods?"
    a "You’re still the same grumpy old man. {w=0.7}But yes, I have the goods."
    a "You have no idea what it cost me to get them."
    a "Although I wasn’t able to kill all the witnesses — one scientist managed to escape."

    mc "(A scientist...)"
    "For a split second, every muscle in [mc]'s body tenses."
    mc "(That was...)"

    mc "(Lora's meeting. The substance. A vanished city.)"
    "Slowly, he forces himself to relax."
    mc "(Don't jump. Confirm first.)"

    az "Doesn’t matter. {w=0.7}The important thing is that you secured the goods."
    az "So, where are they?"
    show s0w54 with dissolve
    a "Hey, rookies! Bring it out."
    play sound carhit
    show s0w53 with dissolve
    a "Our boss wants to take a look."
    show s0w55 with dissolve
    pause 0.5
    play sounds3 cardooropendback
    show s0w56 with vpunch
    pause 1.0
    show s0w57 with dissolve
    S "I see movement at the back. {w=0.7}It might be the target. {w=0.7}What are your orders?"
    mc "Wait. {w=0.7}Don’t rush — we need to confirm it’s the real deal."
    S "Understood."
    play sounds2 mmove
    play sounds3 rustling2
    show s0w58 with dissolve
    a "You know, I usually don’t stick my nose into other people’s business."
    a "But I’ll make an exception this time. {w=0.7}Mind telling me what this thing really is?"
    show s0w59 with dissolve
    a "No one I’ve asked seems to know its origin — like it just fell from the sky."
    a "And I don’t like secrets."
    show s0w68 with dissolve
    az "It doesn’t concern you."
    pause 1.1
    az "And I don’t repeat myself."
    az "You give me the goods, I give you the promised amount. {w=0.7}No more, no less. Got it?"
    show s0w69 with dissolve
    a "Alright, alright."
    a "Don’t want to cross the line — might end up like the others."
    show s0w60 with dissolve
    az "My patience isn’t limitless."
    show s0w61 with dissolve
    a "..."
    show s0w62 with dissolve
    pause 0.5
    show s0w63 with dissolve
    a "Your wish is my command."
    play sounds2 mmove
    show s0w70 with dissolve
    a "Handle it carefully. {w=0.7}This container is worth several hundred of your lives."
    scene s0w69 with dissolve
    pause 0.5
    show s0w64 with dissolve
    a "Now, allow me to present the crown jewel of my collection: dragon eggs!"
    scene s0w69 with dissolve
    az "..."
    show s0w68 with dissolve
    az "Dragon eggs? {w=0.7}Are you serious?"
    az "You’ve got to be joking..."
    show s0w65 with dissolve
    a "Just a little. {w=0.7}Open it."
    show s0w66 with dissolve
    a "I hope it’s what you’ve been looking for."
    show s0w71 with dissolve
    S "Commander..."
    S "I'm getting a spike from the case."
    S "Radiation?"
    S "No. Not exactly."
    S "Whatever it is, it's bending the readings."
    scene s0w66 with dissolve
    a "Plenty of my colleagues died for this, so the price has gone up."
    az "How much?"
    a "Twice as much."
    az "..."
    show s0w67 with dissolve
    az "Fine."
    scene s0w71 with dissolve
    mc "Shiya, status. {w}Can you see what’s in the container?"
    S "Negative. {w=0.6}Too much distortion."
    S "I don't have visual confirmation."
    S "But the readings are real."
    S "If that's bait, it's expensive bait."
    mc "What about other enemies? {w}Any more contacts?"
    S "No, sir. It’s clear."
    show s0w72 with dissolve
    mc "Mona, what’s your situation? How does it look?"
    m "All clear on my end. No hostiles in sight."
    show s0w73 with dissolve
    x "Commander?"
    x "If that thing really is like a mass-destruction threat…"
    show s0w74 with dissolve
    x "Blowing it up is a damn stupid plan."
    show s0w75 with dissolve
    c "Can’t believe I’m saying this… but he’s right."
    show s0w81 with dissolve
    mc "(If we let him walk away with it, we’re done.)"
    mc "(If we blow it, we might be done too.)"
    mc "(No clean options.)"
    scene s0w42 with dissolve
    pause 1.1
    S "Commander, orders?"
    scene s0w73 with dissolve
    mc "..."
    mc "(Damn it.)"
    show s0w79 with dissolve
    mc "Everyone in position?"
    scene s0w81 with dissolve
    E "Yes, sir!"
    scene s0w82 with dissolve
    mc "Olivia, are you ready?"
    
    
    show s0w76 with dissolve
    h "Ready as ever, darling."
    mc "..."
    scene s0w79 with dissolve
    mc "(No visual.)"
    mc "(No clean confirmation.)"
    scene s0w111 with dissolve
    mc "(But if that signal is real and we let it leave...)"
    mc "(Millions die.)"
    pause 1.1
    scene s0w76 with dissolve
    mc "(Orders were clear.)"
    mc "(Once the transfer starts, containment overrides confirmation.)"
    pause 1.1
    mc "Execute."
    play sounds3 c4
    scene s0w77 with dissolve
    pause 0.5
    stop music
    play sounds3 deatwishes
    scene s0w83 with dissolve
    pause 0.5
    play sounds4 machinegun loop
    scene s0w80 with dissolve
    pause 0.5
    play sounds2 c4boom volume 0.4
    play sounds4 headshotzombie
    scene s0w84 with dissolve
    pause 0.5
    scene s0w85 with dissolve
    pause 0.5
    stop sounds4
    show s0w81 with dissolve
    x "TAKE THAT!"
    c "Don’t yell in my ear!"
    show s0w82 with dissolve
    mc "Shiya. Report."
    scene s0w81 with dissolve
    S "Clear. {w}No more enemies in sight."
    S "The area is secured."
    scene black with dissolve
    pause 1.5
    play sounds3 rustling2
    play sound fire fadein 2.0  loop volume 0.2
    play music tda1 fadein 5.3 loop
    show s0w86 with dissolve
    pause 2.1
    mc "(Too clean.)"
    m "Commander… don’t you think—"
    m "That went a little too smoothly?"
    show s0w87 with dissolve
    mc "You’re right."
    mc "This wasn’t resistance. This was... compliance."
    mc "Either they didn’t know..."
    mc "Or they wanted us here."
    play sounds2 stepmc volume 0.2 
    show s0w88 with dissolve
    h "Nah…"
    h "I think they just didn’t see it coming."
    h "Couple cases of cash, that’s it."
    h "And the second vehicle?"
    h "Yeah… it’s burning real nice."
    show s0w90 with dissolve
    mc "No."
    mc "They don’t go down like that."
    show s0w89 with dissolve
    h "Or maybe…"
    h "we just did our job right."
    play sounds3 mmove
    show s0w91 with dissolve
    mc "We’ve been chasing him for months."
    mc "Men like him don’t get easy endings."
    mc "Not without a reason."
    play sounds2 scar1 volume 0.2 
    pause 0.5
    play sounds4 hdshot
    show s0w92 with dissolve
    pause 0.5
    show s0w94 with dissolve
    h "Was that really necessary?"
    h "He was already dead."
    show s0w95 with dissolve
    mc "I don’t deal in assumptions."
    show s0w97 with dissolve
    h "Well, at least now he won’t have to pay his taxes."
    mc "..."
    h "...Yeah."
    h "That one slipped."
    show s0w98 with dissolve
    m "Commander, may I have a word? {w}We’ve got a problem..."
    show s0w99 with dissolve
    mc "Report."
    show s0w100 with dissolve
    m "The cargo..."
    m "I'm not sure this is what we were looking for."
    pause 1.1
    mc "...Explain."

    m "There's no core. No cell."
    m "Just a sealed vial inside the case."
    m "Some kind of liquid."
    show s0w101 with dissolve
    mc "Liquid?"
    stop sounds1 fadeout 5.0
    stop music fadeout 5.0
    stop sound fadeout 5.0
    window hide
    $ renpy.music.set_volume(0.9, channel='music')
    image ath = Movie(channel="movie_dp", loop = False, play="video/ath.webm")
    show ath 
    $ renpy.pause(11.5, hard=True)
    window auto

label street:
    $ renpy.music.set_volume(0.5, channel='music')
    scene up 1 with dissolve
    scene up 2 with dissolve
    scene up 3 with dissolve
    play sound breath3 
    play music street1 loop fadein 4.4 
    show up 4 with dissolve
    show 8yr with vpunch
    pause 0.7
    mc "NOOOOO!"
    hide 8yr
    show up 6 with dissolve
    stop sound
    G "Freakin' dude!"
    show up 7 with dissolve
    mc "Sorry. Didn’t mean to startle you."
    show up 8 with dissolve
    G "Why on earth are you yelling like that for?"    
    show up 9 with dissolve
    G "People are jogging around here, you know?!" 
    show up 10 with dissolve
    G "Yeah, well, screw you. I don’t have time for this."
    show up 11 with dissolve
    G "Seriously… what’s wrong with people these days?"
    show up 12 with dissolve
    mc "…Right."
    scene up 13 with dissolve
    pause 2
    scene up 14 with dissolve
    pause 2
    scene ups 15 with dissolve
    mc "…That dream again."
    scene up 15 with dissolve
    mc "(Twenty years...)"
    mc "(Empty streets. Dead signal. The case.)"
    mc "(Mona's voice—)"
    mc "(Some kind of liquid.)"
    mc "(Then fire.)"
    show up 16 with dissolve
    mc "…Fuck."
    scene up 17 with dissolve
    play sound cars
    pause 2.0
    scene up 18 with dissolve
    pause 2.0
    scene up 19 with dissolve
    pause 0.5
    scene up 20 with dissolve
    pause 0.5
    scene up 21 with dissolve
    pause 0.5
    scene up 22 with dissolve
    pause 0.5
    show up 23 with dissolve
    mc "(Okay, enough, get it together.)"
    mc "(He'll be here soon.)"
    mc "(Big day today.)"
    stop sound fadeout 1.1
    stop music fadeout 2.0
    scene black with dissolve 
    pause 2.1
    play sounds1 whoosh
    show s0pp1 with CropMove(time=0.1, mode='slideright')
    mc "(Forty-four… and still going.)"
    play sounds3 mouseclick 
    play music1 news fadein 5.5 volume 0.5
    show s0pp2 with dissolve
    mc "(Could be worse.)" 
    show s0pp3 with dissolve
    mc "Let’s get to work."
    play sounds1 whoosh
    scene s0pp4 with CropMove(time=0.1, mode='slideleft')
    pause 0.7
    scene s0pp5 with dissolve
    pause 0.7
    scene s0pp4 with dissolve
    npc "And we’re back on ‘Science Uncovered.’"
    scene s0pp6 with dissolve
    mc "(…eight years.)"
    scene s0pp7 with dissolve
    npc "Today, we have a very special guest, Sofia Temirov!"
    npc "Welcome, Sofia."
    s "Likewise, Miki."
    scene s0pp8 with dissolve
    npc "Let’s get straight to it!"
    npc "Your latest discovery has stunned the entire world."
    scene s0pp9 with dissolve
    npc "Many are calling it the future of our civilization."
    npc "How would you comment on that?"
    scene s0pp10 with dissolve
    mc "(After everything… how do I face him?)"
    scene s0pp11 with dissolve
    s "We got lucky. That’s all."
    npc "Oh, come on, creating a substance capable of regenerating human organs is nothing short of genius!"
    s "The properties of this… 'substance' are extraordinary."
    s "That much is true."
    scene s0pp9 with dissolve
    mc "(Substance.)"
    mc "(Twenty years ago it was a vial in a case.)"
    mc "(Now it's a miracle on live TV.)"
    play sounds1 whoosh
    scene s0pp15 with CropMove(time=0.1, mode='slideleft')
    pause 1.7
    play sounds2 whoosh
    scene s0pp13 with CropMove(time=0.1, mode='slideright')
    s "But the process of obtaining it is… complicated."
    play sounds1 whoosh
    scene s0pp15 with CropMove(time=0.1, mode='slideleft')
    pause 1.1
    scene s0pp14 with dissolve
    pause 1.1
    scene s0pp12 with dissolve
    npc "Naturally, acquiring something like this won’t be easy!"
    npc "But many point out that we still don’t know the origin of the substance."
    play sounds2 whoosh
    scene s0pp16 with CropMove(time=0.1, mode='slideright')
    npc "Do you fully understand what you’re working with?"
    play sounds1 whoosh
    scene s0pp17 with CropMove(time=0.1, mode='slidedown')
    s "Our scientists are professionals." 
    s "They know what they’re dealing with."
    npc "Were there any incidents during the research?"
    scene s0pp18 with dissolve
    s "No." 
    s "Everything went according to plan." 
    s "No incidents."
    pause 1.1
    mc "(…No.)"
    mc "(Lie.)"
    scene s0pp65 with dissolve
    npc "Some sources link your project to the events of 2018 and 2030…"
    npc "Care to comment?"
    play sounds2 mmove 
    scene s0pp66 with dissolve
    s "Those theories were made up by fanatics and lunatics."
    s "A complete waste of time."
    play sounds2 mmove 
    pause 0.7
    play sounds3 fallpho
    scene s0pp67 with dissolve
    npc "You seem rather firm on that. Is it personal?"
    pause 1.1
    s "No comment."
    scene s0pp68 with dissolve
    pause 1.1
    play sounds2 mmove 
    scene s0pp69 with dissolve
    npc "Tell me… were any of the victims your colleagues?"
    pause 1.1
    s "That’s enough."
    s "We’re done here."
    npc "Wha—"
    scene s0pp70 with dissolve
    npc "We’ll be right back after a short break."
    mc "Heh."
    play sounds2 clothess 
    scene s0pp71 with dissolve
    mc "..."
    scene s0pp72 with dissolve
    pause 1.2
    play sounds3 fallbookd
    scene s0pp73 with dissolve
    pause 1.1
    scene s0pp74 with dissolve
    pause 1.1
    play sounds1 showerlockerroom loop fadein 1.2
    scene s0pp60 with dissolve
    pause 3.1
    stop sounds1 fadeout 3.6
    scene black with dissolve 
    pause 2.1
    play sounds3 windscene loop fadein 5.5 volume 0.6
    scene s0pp19 with dissolve
    mc "(Alright… beer and turkey?)"
    mc "(No… Norman hates turkey.)"
    mc "(Chicken? Yeah… that might work.)"
    scene s0pp20 with dissolve
    npc "Good afternoon, Mr.[mc]."
    scene s0pp21 with dissolve
    mc "Morning, Adam."
    scene s0pp19 with dissolve
    mc "(Didn’t like him at first… turned out he’s a decent guy.)"
    mc "(…Can’t say the same about you.)"
    stop music1 fadeout 5.4
    scene black with dissolve 
    pause 3.2
    play sounds2 footstep2
    play music season4act12 fadein 9.2 loop
    scene s0pp22 with dissolve
    pause 1.1
    mc "(…Yeah. Of course.)"
    scene s0pp23 with dissolve
    pause 1.2
    mc "Guess what."
    mc "I brought something."
    play sounds2 mmove 
    scene s0pp28 with dissolve
    mc "For you, Mona…"
    mc "Jack."
    scene s0pp24 with dissolve
    pause 1.1
    play sounds2 mmove 
    scene s0pp25 with dissolve
    pause 1.1
    mc "Cheers."
    play sounds1 mmove 
    scene s0pp26 with dissolve
    play sounds2 drinkingiv
    pause 1.1
    scene s0pp25 with dissolve
    pause 1.2
    mc "…I’m gonna see him."
    pause 1.1
    mc "My son."
    play sounds1 mmove 
    scene s0pp26 with dissolve
    play sounds2 drinkingiv
    pause 1.1
    scene s0pp27 with dissolve
    mc "So much happened today…"
    pause 2.1
    scene black with dissolve 
    pause 3.1
    scene s0pp29 with dissolve
    show 7yr with dissolve 
    pause 1.7
    mc "…and here I am."
    mc "Again."
    hide 7yr 
    scene s0pp30 with dissolve
    pause 1.8
    mc "..."
    play sounds2 mmove 
    scene s0pp31 with dissolve
    pause 1.7
    mc "(…Maybe.)"
    play sounds2 mmove 
    scene s0pp32 with dissolve
    pause 1.1
    scene s0pp33 with dissolve
    play sounds2 drinkingiv
    pause 1.7
    scene s0pp32 with dissolve
    mc "..."
    play sounds2 clench 
    scene s0pp34 with dissolve
    pause 0.7
    mc "(It’s time.)"
    play sounds4 mmove 
    scene s0pp35 with dissolve
    L "Please…"
    scene s0pp37 with dissolve
    pause 1.1
    scene s0pp36 with dissolve
    L "Norman…"
    play sounds4 mmove 
    scene s0pp38 with dissolve
    mc "...Right."
    mc "He needs me."
    play sounds2 glitchfear 
    scene s0pp39 with glitch 
    L "I’m sorry darling."
    scene s0pp40 
    pause 1.1
    mc "..."
    scene s0pp41 with dissolve
    mc "Funny."
    scene s0pp42 with dissolve
    pause 1.7
    play sounds2 mmove 
    scene s0pp43 with dissolve
    mc "See you tomorrow."
    stop sounds3 fadeout 0.6
    scene black with dissolve 
    pause 2.1
    play sounds1 showerlockerroom loop fadein 1.2
    scene s0pp61 with dissolve
    pause 3.1
    stop sounds1 fadeout 1.2
    scene s0pp62 with dissolve
    npc "…according to Sofia Temirov, soon we will be able not only to travel vast distances instantly…"
    npc "…but also significantly extend human li—"
    mc "(Teleportation. Regeneration.)"
    mc "(Same project. New packaging.)"
    play sounds2 mouseclick
    scene s0pp64 with dissolve
    mc "…Again."
    play sounds2 footstep2 
    play sound roomemptyambience1 fadein 5.5 loop volume 0.4
    scene s0pp75 with dissolve
    pause 2.1
    scene black with dissolve 
    pause 2.1
    play sounds doorclose 
    scene s0pp44 with dissolve
    mc "(14:00.)"
    mc "(We said 17:40.)"
    mc "(Plenty of time.)"
    scene s0pp45 with dissolve
    mc "(Temirov…)"
    mc "(Same project.)"
    mc "(Same handwriting…)"
    scene s0pp46 with dissolve
    mc "(Forest.)"
    mc "(Eight years since you vanished.)"
    scene s0pp47 with dissolve
    mc "(Nothing left.)"
    mc "(Just my son… and the other two.)"
    mc "(No bodies. No traces.)"
    mc "(Twenty years since Al-Zahira.)"
    mc "(Different years. Same damn pattern.)"
    mc "(So why...)"
    pause 2.1
    scene s0pp49 with dissolve
    show 7yr with dissolve
    pause 3.1
    mc "AAARGH—!"
    hide 7yr with dissolve
    play sounds2 punch1 
    scene s0pp48 with vpunch
    mc "FUCK ALL OF IT!"
    play sounds2 fall
    scene s0pp51 with dissolve
    pause 1.1
    scene s0pp50 with dissolve
    pause 1.1
    mc "(…Why am I even doing this?)"
    scene s0pp55 with dissolve
    pause 1.1
    scene s0pp56 with dissolve
    mc "(For me?)"
    mc "(For her?)"
    stop music fadeout 5.1
    play sounds2 phonevibr
    scene s0pp57 with dissolve
    pause 2.7
    play sounds3 phonetouch
    scene s0pp58 with dissolve
    mc "Yeah?"
    scene s0pp59 with dissolve
    N "Hey, Dad. You good? Everything okay?"
    scene s0pp58 with dissolve
    mc "I’m good. Where are you?"
    scene s0pp59 with dissolve
    N "Almost there, like thirty minutes out!"
    scene s0pp58 with dissolve
    mc "You driving?"
    scene s0pp59 with dissolve
    N "Yeah, Dad!"
    scene s0pp58 with dissolve
    mc "Mina with you?"
    scene s0pp59 with dissolve
    N "..."
    mc "Then you remember what I told you about using your phone while dri—"
    N "kssh —you're breaking up, old man— kssh..."
    M "Father, what are you—"
    scene s0pp59 with dissolve
    mc "(Never listens…)"
    mc "(Get up. Time to meet them.)"
    scene black with dissolve 
    play sounds doorclose
    pause 1.7
    stop sound fadeout 0.5

    play music street2
    show up 24 with dissolve
    pause 1.5
    scene up 25 with dissolve
    play sound cardoor
    pause 1.0
    stop sound
    show up 26 with dissolve
    M "Grandpa, Grandpa!!"
    show up 27 with dissolve
    mc "Hey there, sunshine."
    mc "Missed you."
    show up 28 with dissolve
    M "I missed you SO much! Like, {b}super{/b} much! I couldn’t wait anymore!"
    show up 29 with dissolve
    mc "Me too, sweetheart. More than you can imagine..."
    show up 30 with dissolve
    A "Mina, slow down, honey. Let Grandpa catch his breath first."
    show up 31 with dissolve
    M "But he doesn’t mind, right Grandpa!? RIGHT??"
    show up 32 with dissolve
    mc "Heh. Course I don’t."
    show up 32 with dissolve
    mc "Hold on…"
    mc "Did you get taller, or is that just me?"
    show up 33 with dissolve
    M "Nope! I {b}totally{/b} grew! Mom says I’m sprouting like a weed!"
    show ups 34 with dissolve
    A "Which, to be fair, is not the {b}most{/b} elegant comparison..."
    scene up 36 with dissolve
    mc "All in good time, my dear."
    mc "You should’ve seen your dad at your age."
    mc "That was something."
    show up 33 with dissolve
    M "Dad?! Being {b}small{/b}?! No way. He was born serious and boring!"
    show up 32 with dissolve
    mc "When we first took him in… he was worse than that."
    show up 37 with dissolve
    mc "Alexa… you haven’t changed much."
    mc "Still look good."
    show up 38 with dissolve
    A "Aw, thank you. You always know how to make an old woman smile."
    mc "Old? Please."
    mc "You’ve still got time to cause trouble."
    show up 39 with dissolve
    A "We’re all really happy to see you, you know. Mina’s been counting the days."
    show up 40 with dissolve
    mc "How’ve you been?"
    mc "Everything holding up?"
    show up 41 with dissolve
    A "Doing great." 
    A "Mina keeps me busy, and I’m teaching at that private school downtown." 
    A "It’s steady, nothing to complain about."
    show up 42 with dissolve
    A "And how about you? How are you doing? Anything new on your end?"
    show up 43 with dissolve
    mc "Same old."
    mc "Nothing worth talking about."
    mc "Just keeping things running."
    show up 44 with dissolve
    mc "Trying not to drop dead just yet."
    show up 45 with dissolve
    A "Oh, don’t say things like that!"
    A "You’re still in your prime, full of life and energy."
    show up 46 with dissolve
    mc "You flatter me. But I appreciate the sentiment."
    show up 47 with dissolve
    mc "How’s Norman?"
    mc "He behaving himself?"
    show up 50 with dissolve
    A "No, not at all. He’s wonderful — maybe too wonderful, if you ask me..."
    show up 51 with dissolve
    A "But because of his business trips lately, he hasn’t been able to spend much time with us."
    show up 52 with dissolve
    A "He is always buried in his work, and I’m not sure what it is exactly, but... "
    A "We’ve really started to miss him a lot."
    A "Every time I ask, he says it's classified."
    A "Which would sound cooler if it didn't keep stealing him from us."
    show up 53 with dissolve
    mc "..."
    mc "(Classified...)"
    mc "(Of course.)"
    show up 54 with dissolve
    N "Hey, it’s not that bad, babe."
    N "I’m busting my ass out there for you and Mina."
    show up 55 with dissolve
    N "You know that, right? I’m doing it for you. I love you both more than anything."
    show up 56 with dissolve
    pause 1.1
    show up 57 with dissolve
    A "If you say so, I guess..."
    show up 58 with dissolve
    A "But still, you spend way too much time at work."
    A "It’s like you’re practically living there. {w}You could be gone for weeks on end...."
    show up 59 with dissolve
    M "And again...."
    show up 60 with dissolve
    mc "This happen a lot?"
    scene ups 61 with dissolve
    pause 0.5
    show up 61 with dissolve
    M "No! Not that often, to be honest. {w}Just every now and then."
    show up 62 with dissolve
    M "Everything used to be fine between them, but lately, it seems to have gotten a lot worse."
    show up 63 with dissolve
    N "Alright… yeah. I’m sorry."
    N "I’ll try, okay? I’ll be around more."
    show up 64 with dissolve
    mc "Didn’t expect that."
    show up 65 with dissolve
    N "There we go again… I said I’m sorry, alright?"
    N "I {b}will{/b} spend more time with you and Mina, just… let me deal with this mess at work first, okay?"
    show up 66 with dissolve
    play music reunion1 fadeout 2.0 fadein 3.0
    N "...."
    scene up 68 with dissolve
    pause 1.5
    show up 69 with dissolve
    b "..."
    show up 70 with dissolve
    mc "Son..."
    show up 71 with dissolve
    N "…Dad."
    scene up 69 with dissolve
    b "..."
    show up 72 with dissolve
    mc "You've aged."
    scene up 69 with dissolve
    N "..."
    show up 73 with dissolve
    N "Says the guy who’s even older than me."
    stop music
    play music street2
 
    scene up 74 with dissolve
    pause 1.5
    scene up 76 with dissolve
    pause 1.0
    show up 77 with dissolve
    mc "How’ve you been, son?"
    mc "Heard you’ve been living at work lately."
    show up 78 with dissolve
    N "Come on, Dad… don’t start."
    N "I know it sucks, alright? But I don’t really have a choice right now…"
    N "Anyway, what about you?"
    N "You ever gonna take me up on that? Move in with us?"
    show up 79 with dissolve
    mc "No."
    mc "Can’t just leave this place."
    mc "Too much of Lora in these walls."
    show up 79 with dissolve
    mc "As for work, well..."
    mc "Same routine."
    mc "Work. Eat. Sleep. Repeat."
    show up 82 with dissolve
    mc "Ahm..."
    mc "(Even if things feel warm for now... they don’t stay that way forever.)" 
    show up 83 with dissolve
    mc "Come on in."
    mc "Place is old… but it’s still got some warmth left."
    stop music fadeout 1.8
    scene bb 1 with dissolve
    pause 2.0

label homedinner:
    
    stop music fadeout 1.8
    play music dinner1 fadein 2
    show s0f1 with dissolve
    mc "Alright. Dig in."
    scene s0f5 with dissolve
    M "..."
    scene s0f6 with dissolve
    M "Hmpf..."
    show s0f4 with dissolve
    A "Mina, honey, come on. {w}You need to eat if you want to grow up strong like Grandpa."
    show s0f8 with dissolve
    M "But I don’t like broccoli!"
    M "It smells like the garden after rain. Shi-"
    show s0f7 with dissolve
    A "Honey!"
    A "(sigh) Listen... {w}I know it’s not your favorite, but it’s good for you." 
    A "Your body’ll thank you later."
    scene s0f6 with dissolve
    M "(Scoffs)"
    show s0f9 with dissolve
    A "..."
    scene s0f10 with dissolve
    pause 1.0
    scene s0f11 with dissolve
    pause 1.0
    scene s0f12 with dissolve
    pause 1.0
    scene s0f13 with dissolve
    pause 0.4
    scene s0f14 with dissolve
    pause 0.4
    scene s0f13 with dissolve
    pause 0.4
    scene s0f16 with dissolve
    pause 1.0
    scene s0f17 with dissolve
    pause 0.4
    scene s0f18 with dissolve
    pause 0.4
    scene s0f19 with dissolve
    pause 0.4
    show s0f20 with dissolve
    N "Hey… Grandpa made that just for you. C’mon, just a couple bites? For him?"
    show s0f21 with dissolve
    M "Hmph..."
    scene s0f22 with dissolve
    mc "..."
    show s0f23 with dissolve
    mc "Alright, I’ve got an idea."
    show s0f24 with dissolve
    mc "Five bucks if you finish the broccoli."
    show s0f25 with dissolve
    mc "Help clean up, that’s another five."
    show s0f26 with dissolve
    mc "Deal?"
    scene s0f27 with dissolve
    pause 0.5
    scene s0f29 with dissolve
    pause 0.5
    show s0f30 with dissolve
    M "..."
    show s0f31 with dissolve
    M "..."
    show s0f35 with dissolve
    M "Ten bucks doesn’t just lie around..."
    scene s0f32 with dissolve
    pause 1.0
    scene s0f33 with dissolve
    pause 2.0
    scene s0f34 with dissolve
    pause 2.0
    show ch 34 with dissolve
    play sound dishes
    M "I’m gonna be rich~"
    scene ch 35 with dissolve
    pause 1.0
    show ch 36 with dissolve
    M "No more broccoli blues~"
    stop sound
    show s0f36 with dissolve
    mc "(…That was easy.)"
    show s0f37 with dissolve
    pause 1.0
    show s0f38 with dissolve
    pause 1.0
    show s0f39 with dissolve
    mc "So… what brings you out here?"
    mc "Not exactly close."
    show s0f40 with dissolve
    A "Norman finally got some time off. First in... what, a year?"
    show s0f41 with dissolve
    N "Figured we needed a break. Just us, no deadlines, no phones… no noise."
    show s0f42 with dissolve
    mc "Yeah… not something you get often."
    show s0f43 with dissolve
    mc "Sounds like you needed it."
    show s0f44 with dissolve
    mc "So where’d you go?"
    show s0f46 with dissolve
    mc "...."
    show s0f47 with dissolve
    mc "(Not bad.)"
    show s0f48 with dissolve
    pause 2.0
    show s0f49 with dissolve
    pause 2.0
    show s0f50 with dissolve
    pause 1.0
    show s0f51 with dissolve
    pause 1.0
    show s0f52 with dissolve
    pause 1.0
    show s0f53 with dissolve
    mc "..."
    show s0f54 with dissolve
    mc "…Something wrong?"
    show s0f55 with dissolve
    A "No. {w}No, nothing. Everything’s fine."
    show s0f56 with dissolve
    A "We just... went to the— {w}the mountains."
    show s0f57 with dissolve
    N "Yeah, snowboarding, hot cocoa… you know, the whole thing."
    show s0f59 with dissolve
    mc "Mountains, huh…" 
    mc "Good pick. Especially this time of the year."
    show s0f60 with dissolve
    M "But we weren’t even there! Why lie to grandpa? We were at Starlit Stand!"
    stop music fadeout 1.0
    show s0f61 with dissolve
    E "...."
    show s0f62 with dissolve
    M "What? Did I say something wrong?"
    show s0f63 with dissolve
    A "Mina..."
    A "Not at dinner, sweetheart."
    M "..."
    show s0f64 with dissolve
    M "Ah, oops... I forgot."
    show s0f65 with dissolve
    mc "Starlit Stand…?"
    show s0f66 with dissolve
    mc "Heh…"
    show s0f67 with dissolve
    play music napr 
    mc "..."
    show s0f68 with dissolve
    mc "Mountains… you said."
    show s0f70 with dissolve
    mc "..."
    show s0f71 with dissolve
    mc "…Of all places."
    scene s0f72 with dissolve
    mc "..."
    play sound raincity3 loop volume 0.3
    scene s0f116 with dreamyzoom 
    show strstd with dissolve 
    "Eight years ago."
    ri "Were you able to reach the other squad?"
    gg "Negative, sir."
    ri "Anyone else found?"
    gg "Everyone we’ve found so far is dead."
    hide strstd with dissolve 
    scene s0f117 with dissolve
    ri "Secure the perimeter. Seal off forest access!"
    g "Yes, sir!"
    ri "What the hell happened here…"
    scene s0f118 with dissolve
    mc "Lora…"
    scene s0f119 with dissolve
    mc "Why…"
    mc "Why did I let this happen…"
    scene s0f120 with dissolve
    ri "Don’t blame yourself. You couldn’t have gotten here any faster."
    scene s0f121 with dissolve
    ri "..."
    scene s0f122 with dissolve
    pause 0.5
    scene s0f123 with dissolve
    pause 0.5
    scene s0f121 with dissolve
    ri "..."
    ri "(Whispering) Same handwriting… 2018 all over again."
    scene s0f124 with dissolve
    gg "Sir, we found survivors."
    gg "But I have bad news, they don’t remember anything."
    gg "Looks like the shock was too much."
    scene s0f126 with dissolve
    ri "That’s a child…"
    mc "Norman!"
    scene s0f127 with dissolve
    g "Hey kid, are you—"
    N "Mom… she…"
    N "I’m sorry, Dad! {w=0.8}I’m sorry... {w=0.6}I’m sorry... {w=0.4}I’m sorry... {w=0.2}I’m sorry... {w=0.1}I’m sorry..."
    scene s0f128 with dissolve
    mc "..."
    ri "Get up. You need rest."
    stop sound fadeout 0.5
    scene s0f74 with linearblur
    N "Dad… you okay?"
    scene s0f73 with dissolve
    mc "Yeah… just a little dizzy."
    mc "But why there?"
    show s0f98 with dissolve
    N "It was… on the way. We just figured we’d stop for a bit, stretch our legs."
    show s0f97 with dissolve
    N "You know… get some air. Clear our heads."
    scene s0f75 with dissolve
    mc "..."
    scene s0f76 with dissolve
    mc "…Right."
    show s0f79 with dissolve
    N "Yeah… it was quiet. Just trees, sky… no traffic, no noise."
    scene s0f76 with dissolve
    mc "Sounds almost perfect."
    mc "If it weren’t for one small thing."
    show s0f77 with dissolve
    mc "Why that place?"
    scene s0f99 with dissolve
    N "I told you… it was on the way."
    scene s0f77 with dissolve
    mc "…on the way."
    show s0f100 with dissolve
    mc "(Sigh)"
    show s0f101 with dissolve
    mc "..."
    show s0f102 with dissolve
    mc "Let me get this straight."
    mc "First it’s the mountains…"
    mc "Now it’s the forest."
    mc "So which is it?"
    scene s0f78 with dissolve
    N "We just… took a detour, alright? Maybe a long one, yeah."
    show s0f81 with dissolve
    mc "Norman..."
    mc "I wouldn’t care if it was anywhere else."
    mc "Anywhere."
    mc "But that place?"
    show s0f82 with dissolve
    mc "You remember what happened there."
    mc "Everyone who went into that forest… disappeared."
    mc "Gone. Like they were never there."
    mc "You… and two others."
    mc "That’s all who made it out."
    mc "The 2030 incident."
    scene s0f100 with dissolve
    mc "(Sigh)"
    scene s0f101 with dissolve
    mc "..."
    scene s0f81 with dissolve
    mc "And now you’re telling me…"
    mc "You took your family back there?"
    scene s0f82 with dissolve
    mc "Why, Norman?"
    mc "What the hell were you thinking?"
    scene s0f80 with dissolve
    N "..."
    scene s0f82 with dissolve
    mc "Say something."
    mc "Norman."
    show s0f83 with dissolve
    mc "Why are you just sitting there—?!"
    play sound hit
    show s0f84 with vpunch
    mc "ANSWER ME!"
    show s0f85 with dissolve
    stop music fadeout 1.0
    mc "WHY DID YOU DO THAT!"
    N "We didn't go deep."
    N "I swear."
    N "Just the public trail."
    N "The memorial side."
    N "People go there now, Dad."
    pause 1.1
    N "I thought if I could stand there without breaking..."
    N "maybe you could, too."
    show s0f88 with dissolve
    play music grandpa1 fadein 1.5
    M "Grandpa... please don’t be mad at Dad..."
    M "We were just trying to help you."
    M "Dad said maybe there was still something there..."
    M "Not in the scary part!"
    M "Just... near the old sign."
    show s0f87 with dissolve
    M "Please... it’s not his fault."
    M "WE WANTED TO HELP YOU!"
    M "So please..."
    show s0f89 with dissolve
    mc "..."
    show ch 98 with dreamyzoom
    show memoryframe with dissolve
    $ Lora_path = True
    L "..."
    show ch 99 with dissolve
    show memoryframe with dissolve
    L "Remember one thing, darling..."
    L "Even if the whole world turns its back on you..."
    L "There will always be someone willing to reach out their hand."
    show ch 100 with dissolve
    show memoryframe with dissolve
    L "So when that moment comes... please don’t push them away."
    show ch 101 with dissolve
    show memoryframe with dissolve
    L "Alright?"
    show ch 103 with dissolve
    show memoryframe with dissolve
    mc "Alright, sunshine."
    show ch 102 with dissolve
    show memoryframe with dissolve
    L "He-he♥"

    $ unlock_lora = 1
    mc "..."
    show s0f89 with dreamyzoom
    mc "..."
    show s0f90 with dissolve
    mc "(…So that’s what you meant.)"
    mc "(A helping hand…)"
    show s0f91 with dissolve
    mc "(They came back alive…)"
    mc "(I almost pushed them away…)"
    pause 1.1
    mc "(Yelling won’t fix this.)"
    mc "(Calm down.)"
    mc "(Listen first.)"
    show s0f92 with dissolve
    mc "(Sighs)"
    show s0f93 with dissolve
    mc "…Sorry."
    mc "I went too far."
    show s0f94 with dissolve
    pause 2.0
    show s0f95 with dissolve
    mc "…Thanks."
    show s0f103 with dissolve
    mc "..."
    show s0f96 with dissolve
    mc "So..."
    mc "I’m listening."
    show s0f107 with dissolve
    N "..."
    show s0f104 with dissolve
    A "..."
    show s0f105 with dissolve
    pause 0.5
    show s0f106 with dissolve
    N "…Thanks."
    show s0f108 with dissolve
    N "Dad… can we step outside for a minute? Just you and me."
    scene s0f111 with dissolve
    mc "..."
    show s0f109 with dissolve
    M "But I wanted to hear more of his stories…"
    A "Mina, Dad and Grandpa have something important to talk about. Once they’re done, you can have all the time you want."
    show s0f110 with dissolve
    mc "Won’t be long, kid."
    M "Okay, you promised!"
    A "Alright Mina, let’s go clean up your room."
    mc "..."
    scene s0f111 with dissolve
    mc "I’ll be waiting for you outside."
    stop music fadeout 3.0
    scene bb 1 with Dissolve(2.0)
    pause 2.0

    play sound nightforest loop fadein 1.0 volume 0.1
    show ch 104   with dissolve
    mc "..."
    show ch 105 with dissolve
    play sounds1 beer
    mc "Alright."
    mc "We’re alone."
    mc "So… what was so important you had to pull me aside for?"
    show ch 107 with dissolve
    N "…I don’t even know where to begin."
    show ch 109 with dissolve
    mc "Then start at the beginning."
    mc "I need the truth."
    play sounds1 chair
    show ch 111 with dissolve
    N "…Alright."
    N "You remember… fifteen years ago, when you got back from the army?"
    N "Mom sent you that message."
    show ch 112 with dissolve
    mc "Yeah. I remember."
    mc "She said you were visiting your grandmother."
    show ch 111 with dissolve
    N "Yeah… that’s what we told you."
    show ch 112 with dissolve
    mc "So that was a lie?"
    show ch 111 with dissolve
    N "It just… wasn’t the whole truth."
    show ch 112 with dissolve
    mc "Then what was it?"
    show ch 113 with dissolve
    N "That day… she took me to that forest."
    N "The first time. Before everything that happened later."
    show ch 134 with dissolve
    mc "Wait… you were there?"
    mc "In that forest… before everything?"
    scene ch 113 with dissolve
    N "...yeah."
    stop sound fadeout 1.0
    image transiti11 = Movie(channel="movie_dp", loop = False, play="video/transition1.webm")
    show transiti11
    $ renpy.pause(1.2, hard=True)
    play sounds1 carengine3 fadein 2.0 loop
    show s0ch1 
    show 2yr with dissolve
    "Starlit Stand 2023, 15 year before the main event."
    show s0ch2 with dissolve
    N "Mom… this isn’t the way home."
    N "Where are we really going?"
    show s0ch3 with dissolve
    L "Hey… easy, sweetheart."
    L "You used to say you wanted to follow in my footsteps, remember?"
    L "I just thought… maybe it’s time you see more of that world."
    show s0ch4 with dissolve
    N "Then why tell Dad something else?"
    show s0ch5 with dissolve
    L "...Because if he knew, he'd come with us."
    L "And if he came with us..."
    L "They'd treat him like a breach."
    L "A soldier with combat clearance, walking into a black project?"
    L "No one down there would let that slide."
    N "But they let me in?"
    L "You're my son."
    L "On paper, you're a dependent under my responsibility."
    L "As long as you stay beside me, you're not a threat to them."
    L "You're leverage they don't have to take."
    L "Your father would be different."
    L "He'd ask questions. Push back. Reach for his gun if someone looked at us wrong."
    L "And then I'd have to choose between saving him… and exposing everything."
    show s0ch6 with dissolve
    N "..."
    N "So it's dangerous?"
    L "It might be."
    L "That's why I need you to stay close."
    L "And listen to everything I say."
    N "Mom..."
    L "I know."
    L "I would never bring you here if I had another choice."
    show s0ch7 with dissolve
    N "(…Then I heard her. She whispered something.)"
    L "(softly) This is the only way I can keep them both out of it..."
    N "(I should’ve asked more… I should’ve known something wasn’t right.)"
    N "(But she smiled… and when she did, everything just felt… safe.)"
    stop sounds1 fadeout 1.0

    scene bb 1 with dissolve
    N "The public trail isn't the place Mom took me."
    N "There was another way."
    N "Past the old service road."
    N "A place no tourist would ever find."
    show ch 134 with dissolve
    mc "And you never told me?"
    scene ch 113 with dissolve
    N "...No."
    N "I was scared."
    N "And after 2030..."
    N "I convinced myself maybe it was better buried."
    show ch 134 with dissolve
    mc "Norman..."
    scene ch 113 with dissolve
    N "That's the part I kept from you."
    scene bb 1 with dissolve
    N "That day… it all led to one thing."

    stop sounds1 fadeout 1.0
    scene bb 1 with Dissolve(1.0)
    pause 0.5
    show s0ch8 with dissolve
    play music spscs fadein 5.5 loop 
    play sounds1 concstep1
    L "We’re meeting someone."
    N "(A secret meeting… with a scientist named Dr. Li Wei.)"
    show s0ch9 with dissolve
    L "Not just anyone… so behave, alright?"
    show s0ch10 with vpunch
    pause 0.5
    show s0ch11 with dissolve
    L "Hey— watch it. {w}(under breath) idiot."
    show s0ch12 with dissolve
    R "In all my years, I’ve seen brilliance, imitation… and failure."
    R "But this?"
    R "This is something rarer."
    show s0ch13 with dissolve
    a "Dr. Li, that’s the seventh time you’ve said that this month."
    show s0ch14 with dissolve
    L "Sorry to keep you waiting."
    L "Road decided to complicate things."
    show s0ch15 with dissolve
    R "Well…"
    R "The elusive Ms. Lora."
    R "You do know how to make an entrance, even in absence."
    L "(quietly) Mrs."
    
    N "(They sounded calm… too calm.)"
    N "(And at the same time… there was something in Mom’s eyes.)"
    N "(Something like… resentment.)"
    show s0ch16 with dissolve
    L "Dr. Li Wei."
    L "So you’re the man behind all those… controversial ideas."
    show s0ch17 with dissolve
    R "Oh, please."
    R "I’m more impressed you’ve kept up."
    show s0ch16 with dissolve
    L "Of course. I grew up reading your papers."
    L "Combining shredding theory with wormhole mechanics… that’s incredible."
    L "Do you actually believe crossing between worlds is possible?"
    show s0ch17 with dissolve
    R "Faith… is a luxury a scientist cannot afford."
    R "But curiosity?"
    R "That, I allow myself."
    R "And yes—"
    R "I do intend to see it. With my own eyes."
    show s0ch19 with dissolve
    N "(I didn’t understand what made him so important.)"
    pause 0.5
    show s0ch20 with dissolve
    R "And this would be...?"
    show s0ch21 with dissolve
    L "My son. Norman."
    L "He stays with me until we're done."
    pause 1.1
    show s0ch23 with dissolve
    R "Unusual choice."
    L "Necessary one."
    show s0ch22 with dissolve
    N "It’s… an honor to meet you, sir."
    show s0ch23 with dissolve
    R "The honor’s mine, Norman."
    N "(As I later found out… he wasn’t just a scientist.)"
    show s0ch24 with dissolve
    a "Sir, you have a secured call from the board. Priority one."
    show s0ch25 with dissolve
    L "Sofia…"
    L "Still standing guard like nothing ever changes?"
    show s0ch27 with dissolve
    s "Ms. Lora." 
    s "Didn’t think I’d run into {b}you{/b} again."
    show s0ch26 with dissolve
    R "I wasn’t aware there was… history here."
    R "Should I be concerned… or entertained?"
    scene s0ch27 with dissolve
    s "Oh, there is." 
    s "But it’s classified under 'none of your business', sir."
    show s0ch29 with dissolve
    L "Oh, come on."
    L "Don’t act like we didn’t make a good team."
    show s0ch28 with dissolve
    s "You were the storm."
    scene s0ch27 with dissolve
    s "I was just cleaning up the wreckage you left behind."
    s "We’re done." 
    s "Sir, the call won’t wait."
    s "And the board wants the sample secured before nightfall."
    show s0ch26 with dissolve
    R "Right."
    R "Duty has impeccable timing, as always."
    R "My apologies, Ms. Lora."
    show s0ch29 with dissolve
    L "Dr. Li… one small correction."
    L "It’s Mrs."
    L "I prefer it that way."
    R "..."
    R "My apologies, Mrs. Lora."
    stop music fadeout 2.0
    play sound nightforest loop fadein 1.0 volume 0.1
    play sounds1 whoosh
    scene ch 134 with CropMove(time=0.1, mode='slideright')
    mc "Wait… how does any of this connect to that forest?"
    scene ch 135 with dissolve
    N "Because it’s not just a forest."
    N "There's something beneath it… a lab."
    scene ch 153 with dissolve
    pause 1.1
    scene ch 155 with dissolve
    mc "…lab?"
    scene ch 113 with dissolve
    N "Off the grid. Completely classified."
    N "They were working on something…"
    N "A substance, I think."
    N "Something meant to extend life."
    scene ch 134 with dissolve
    mc "Meant to?"
    scene ch 156 with dissolve
    N "…Yeah."
    N "But it turned out to be something else."
    scene ch 155 with dissolve
    mc "Into what?"
    scene ch 135 with dissolve
    N "It feeds… something inside."
    N "I didn't understand it back then."
    N "Only that the sample wasn't the project."
    N "It was feeding the project."
    stop sound fadeout 1.0
    scene bb 1 with Dissolve(1.0)
    pause 0.5
    play music horizons fadein 5.0
    scene s0ch30 with dissolve
    L "What you're about to see… breaks the rules."
    play sound concstep1 volume 0.4
    scene s0ch31 with dissolve
    R "Mrs. Lora… please."
    R "Bold claims are cheap."
    R "Science is not."
    play sound concstep1 volume 0.4
    scene s0ch32 with dissolve
    R "The world you're so eager to tear apart—"
    R "People paid for it. A lot."
    R "You don’t just ignore that."
    play sound srustle volume 0.4
    scene s0ch34 with dissolve
    L "I’m not ignoring it."
    scene s0ch36 with dissolve
    L "I’m trying to understand why it works."
    scene s0ch38 with dissolve
    L "Because if we don't..."
    scene s0ch39 with dissolve
    pause 1.1
    scene s0ch40 with dissolve
    L "Someone else will use it anyway."
    scene s0ch41 with dissolve
    R "..."
    R "That's not science, Mrs. Lora."
    R "That's fear."
    L "Maybe."
    play sound srustle volume 0.4
    scene s0ch46 with dissolve
    g "Apologies, ma’am. You can’t go beyond this point without a Level Five override."
    scene s0ch47 with dissolve
    scene s0ch48 with dissolve
    L "Jason… really?"
    L "Since when do you hide behind protocol?"
    scene s0ch47 with dissolve
    g "These are direct orders from—"
    scene s0ch49 with dissolve
    L "You know why you're here."
    scene s0ch50 with dissolve
    L "And who made that possible."
    scene s0ch51 with dissolve
    g "Still. I have to follow the protocol—"
    scene s0ch52 with dissolve
    L "I’m not asking you to break the rules."
    L "I’m asking you to think for a second."
    scene s0ch53 with dissolve
    g "…Sorry, ma’am. No issue. Proceed."
    scene s0ch55 with dissolve
    L "Thank you. Let’s move."
    scene s0ch56 with dissolve
    R "Ha-ha."
    R "You do have a talent for command."
    R "Fear works for you."
    play sound concstep1 volume 0.4
    scene s0ch57 with dissolve
    L "If you say so."
    play sound concstep1 volume 0.4
    scene s0ch60 with dissolve
    L "Now… I promised you something special."
    L "What you’re about to see..."
    L "It’s not theory. Not projection. It’s {b}real.{/b}"
    L "The first device ever built by human hands…"
    pause 1.1
    L "using data that doesn’t belong to this Earth."
    scene s0ch58 with dissolve
    L "A warp drive—"
    L "or at least… the first step toward one."
    stop music fadeout 2.0   
    play sound nightforest loop fadein 1.0 volume 0.1
    scene bb 1 with dissolve
    N "That moment..."
    N "It felt like we’d opened a door…"
    N "that was never meant to be opened."
    scene ch 155 with dissolve
    mc "A warp drive?"
    mc "You serious right now?"
    scene ch 153 with dissolve
    N "..."
    scene ch 154 with dissolve
    mc "..."
    scene ch 165 with dissolve
    mc "…Sorry."
    mc "It’s a lot to take in."
    scene ch 172 with dissolve
    N "Dad, this is, this is real. I’m not making this up!"
    scene ch 167 with dissolve
    pause 1.1
    scene ch 168 with dissolve
    mc "Even if it’s real…"
    mc "(Sounds insane… but the pieces fit.)"
    scene ch 166 with dissolve
    pause 1.1
    scene ch 165 with dissolve
    mc "Tell me something, Norman."
    mc "Why go back?"
    mc "A second time."
    scene ch 163 with dissolve
    pause 1.4
    N "It wasn't my choice… not really."
    N "At first it was just messages."
    N "Coordinates. Old photos. Things about Mom no stranger should know."
    N "Then I saw him."
    mc "Him?"
    N "A man… wearing a black mask."
    pause 1.1
    scene ch 177 with dissolve
    N "He gave me Mom's necklace."
    N "Said you'd know what it meant."
    play music jgnext fadein 10.0 volume 0.4
    scene ch 178 with dissolve
    pause 1.1
    scene ch 180 with dissolve
    N "He said… you’d know what to do."
    pause 1.4
    mc "(…Lora’s necklace?)"
    mc "(…No.)"
    scene ch 181 with dissolve
    pause 1.4
    scene ch 182 with dissolve
    mc "(…That’s not possible.)"
    N "Is that why you still… hate me?"
    scene ch 183 with dissolve
    pause 2.1
    scene ch 158 with dissolve
    mc "..."
    scene ch 159 with dissolve
    mc "Why ask that now?"
    scene ch 160 with dissolve
    N "Just… please. No dodging, just tell me. Yes or no."
    scene ch 162 with dissolve
    mc "…I never thought I’d hear that from you."
    mc "No, Norman."
    mc "Not then. Not now."
    scene ch 163 with dissolve
    N "But you said it yourself…"
    N "Mom was your ideal. And I was the reason she—"
    scene ch 164 with dissolve
    pause 1.1
    scene ch 163 with dissolve
    N "...the reason she didn’t make it."
    scene ch 164 with dissolve
    mc "..."
    scene ch 165 with dissolve
    mc "…So that’s what’s been eating you."
    scene ch 166 with dissolve
    pause 1.6
    scene s0f127 with dreamyzoom
    show memoryframe with dissolve 
    N "I’m sorry, Dad..."
    scene ch 166 with dissolve
    hide memoryframe 
    pause 1.1
    scene ch 165 with dissolve
    mc "You're talking about that day."
    scene ch 166 with dissolve
    pause 1.0
    scene ch 167 with dissolve
    mc "..."
    scene ch 168 with dissolve
    mc "I should’ve said this years ago."
    mc "When it mattered."
    scene ch 169 with dissolve
    mc "I never blamed you for what happened to Lora."
    mc "Never."
    mc "But... I was angry."
    mc "...I didn’t know what to do with it."
    mc "And instead of being your father…"
    mc "I lashed out."
    scene ch 171 with dissolve
    mc "I thought you’d hate me for it."
    mc "So I ran."
    mc "Coward."
    mc "..."
    scene ch 171 with dissolve
    mc "If you can still hear me out…"
    scene ch 170 with dissolve
    mc "I’m sorry."
    scene ch 164 with dissolve
    N "..."
    scene ch 172 with dissolve
    N "I… I don’t even know what to say."
    scene ch 172 with dissolve
    N "...but I hear you."
    scene ch 173 with dissolve
    pause 1.0
    scene ch 174 with dissolve
    pause 4.3
    b "..."
    scene ch 175 with dissolve
    N "...Dad?"
    scene ch 177 with dissolve
    N "...There’s something else."
    N "This one didn't come from him."
    N "My handler passed this along."
    N "She said it came from an old friend of yours."
    N "Said… you’d understand."
    stop music fadeout 4.0
    scene ch 183 with dissolve
    N "All they told me was…"
    scene ch 184 with dissolve
    N "That it’s connected to your old mission in Al-Zahira."
    play music axis2 fadein 1.0
    scene ch 184 
    pause 2.0
    image mystery = Movie(channel="movie_dp", loop = False, play="video/mystery.webm")
    show mystery with dissolve
    $ renpy.pause(7.1, hard=True)
    scene ch 188 
    mc "(…No.)"
    mc "(That’s not possible.)"
    show s0f112 with dissolve
    mc "(He’s supposed to be dead…)"
    pause 2.1
    scene ch 188 with dissolve
    ri "P.S. We need you."
    mc "..."
    show s0f114 with dissolve
    N "…What does it say?"
    show s0f115 with dissolve
    mc "If what’s written in that letter is true…"
    show s0f113 with dissolve
    mc "then I need to call in people I swore I’d never involve again."
    stop sound fadeout 1.0
    stop music fadeout 4.0
    scene bb 1 with Dissolve(2.0)
    pause 3.2
    $ persistent.chapter_act0_scene += 1


default anna_help = False
default Anya_Sister = False


label anna:
    stop music fadeout 1.8
    play music1 nb fadein 15.0
    play sounds1 streetevening volume 0.2 loop
    show s0g2 with dissolve
    show 7yr with dissolve
    mc "(I told myself I’d let you go…)"
    scene s0pp47 with dissolve 
    show memoryframe with dissolve 
    mc "(Even with all of this still around me.)"
    hide memoryframe with dissolve 
    show s0pp73 with dissolve 
    show memoryframe with dissolve 
    pause 2.1
    hide memoryframe with dissolve 
    scene s0g2 with dissolve
    mc "(And now you’re back…)"
    mc "(…Just enough to make me hope again.)"
    scene s0g3 with dissolve
    mc "(All I remember… is how powerless I was.)"
    scene s0g4 with dissolve
    mc "(How cruel is that, don’t you think?)"
    a "Well, don’t blame me for any of this."
    scene s0g5 with dissolve
    L "Back then… I didn’t think it would end like this."
    scene s0g6 with dissolve
    L "And I wasn’t planning to leave you."
    L "…Not like that."
    L "You know that."
    scene s0g7 with dissolve
    mc "You and your jokes…"
    mc "You’ve got no idea what those years were like."
    scene s0g8 with dissolve
    a "Who’s he talking to?"
    aa "Beats me. Let’s go — he’s giving me the creeps."
    scene s0g9 with dissolve
    Lor "I know, darling."
    Lor "You don’t have to explain it."
    Lor "I know what it felt like."
    scene s0g10 with dissolve
    mc "How would you know?"
    mc "You’re not real…"
    mc "(…So why does it feel like you are?)"
    Lor "..."
    scene s0g11 with dissolve
    Lor "Hey… don’t start that again."
    Lor "We both know where that spiral goes."
    scene s0g12 with dissolve
    mc "..."
    scene s0g13 with dissolve
    mc "Weren’t you the reason I needed that help?"
    scene s0g14 with dissolve
    Lor "You’re scared."
    scene s0g15 with dissolve
    mc "I didn’t say that."
    scene s0g16 with dissolve
    Lor "You didn’t need to say it."
    Lor "..."
    scene s0g17 with dissolve
    Lor "...Alright."
    Lor "Let’s not pretend you don’t know why I’m here."
    Lor "You saw the letter."
    Lor "That was enough."
    scene s0g18 with dissolve
    mc "Yeah."
    mc "They say they found out what happened to you."
    mc "Why you disappeared."
    scene s0g19 with dissolve
    Lor "Wait…"
    Lor "Since when is Norman tied to the military?"
    Lor "...No, right."
    Lor "You never told me."
    scene s0g18 with dissolve
    mc "He followed in my footsteps."
    mc "Though unlike me… he’s stuck behind a desk."
    mc "Doesn’t see much of the front."
    mc "Yeah… thanks for that, Richard."
    scene s0g19 with dissolve
    Lor "Oh."
    stop music1 fadeout 3.5
    scene s0g20 with dissolve
    mc "(…And just like that—)"
    a "Hah! Would you look at him. Trading his girl to pay off debts?"
    a "You're worse than all of us, you piece of shit."
    scene s0g21 with dissolve
    C "Is that true? You were going to trade me… to pay off a debt?"
    C "What the hell is wrong with you?"
    scene s0g22 with dissolve
    Lor "…Wait."
    Lor "Is that Anya?"
    scene s0g23 with dissolve
    mc "Looks like it."
    mc "Probably got herself into trouble again."
    scene s0g24 with dissolve
    Lor "So?"
    Lor "What are you going to do?"
    scene s0g26 with dissolve
    pause 1.1
    scene s0g25 with dissolve
    mc "Like I’ve got a choice."
    Lor "Remember what I told you?"
    Lor "When someone needs a hand..."
    mc "Don't push them away."
    Lor "Exactly."
    mc "Tho..."
    mc "If Olivia hears about this… I’m dead before sunrise."
    scene s0g27 with dissolve
    Lor "..."
    scene s0g28 with dissolve
    pause 1.1

    stop music fadeout 1
    $ unlock_anya = 1
    $ anna_help = True
    $ Anya_path = True
    
    scene s0g40 with dissolve
    j "Just this once, please? I’m begging you."
    scene s0g41 with dissolve
    j "If you don’t handle it, they won’t stop coming after me."
    scene s0g42 with dissolve
    C "No, Jacob. I’m not your solution tonight." 
    C "Or ever. Get that through your skull."
    play sounds2 bodytap
    scene s0g44 with dissolve
    d "Damn, Jacob. Didn’t you say she wouldn’t fight it?"
    scene s0g45 with dissolve
    d "She just made you look like a clown. That was brutal."
    scene s0g46 with dissolve
    C "Find yourself some other desperate girl to dump this on. I don’t do charity." 
    C "Especially not for idiots."
    scene s0g32 with dissolve
    a "..."
    a "I’m tired. Take your lackeys and get out of my face."
    scene s0g33 with dissolve
    D "Bitch could’ve waited a little longer with this..."
    play sound concstep1
    scene s0g34 with dissolve
    D "Hey, kids. Can we wrap this up?"
    D "I’ve got to pick up my kid from my ex."
    play sounds2 clench volume 0.3
    play sounds3 rustling2
    scene s0g35 with vpunch
    mc "..."
    scene s0g36 with dissolve
    mc "Easy…"
    mc "Don’t move."
    mc "Who sent you?"
    scene s0g37 with dissolve
    D "I-I don’t know what you’re talking about, m-man."
    D "I-I was told to keep an eye on those k-kids."
    play sounds2 clench volume 0.3
    scene s0g38 with vpunch
    pause 0.5
    scene s0g39 with dissolve
    mc "(Someone’s got a death wish… going against Olivia.)"
    play sounds2 fall volume 0.3
    scene s0g47 with dissolve
    e "And what would a girl like her see in a loser like you? What, she into weaklings?"
    scene s0g48 with dissolve
    C "Oh wow… that’s your move? Beg, fail, and then stand there like furniture?"
    play sounds2 bodytap
    scene s0g49 with dissolve
    e "Really? That’s great, mind if we get to know each other better?"
    e "I’m sure we’d have a very memorable time."
    scene s0g50 with dissolve
    e "Might even make each other... feel things."
    scene s0g51 with dissolve
    C "You think this is flirting? That’s cute. Really. Almost embarrassing."
    pause 1.1
    C "Kid, clean the milk off your lips before you start talking like you’ve seen the world."
    C "And maybe, just maybe, learn who you’re barking at before you open your mouth again."
    play sounds4 mmove volume 0.5
    scene s0g52 with dissolve
    d "We don’t care who you are — even if you’re Beastie’s little sister."
    d "We’re gonna have some real fun with you, then dump you in a ditch."
    scene s0g53 with dissolve
    d "Though, to be fair, you’re the best catch we’ve had in a while."
    scene s0g54 with dissolve
    d "So thanks to this idiot for handing you over."
    scene s0g55 with dissolve
    j "Sorry..."
    scene s0g56 with dissolve
    d "What a fucking moron."
    scene s0g57 with dissolve
    d "Y’know what? I just had a brilliant idea."
    d "How about we entertain ourselves, with him watching?"
    d "Bet the poor bastard loses his mind."
    scene s0g58 with dissolve
    C "Touch me… and I promise you won’t need to worry about girls ever again."
    scene s0g59 with dissolve
    C "Actually, scratch that. Judging by the way you act? Might already be a lost cause."
    play sound concstep1
    play music fighting fadein 2.1
    scene s0g60 with dissolve
    pause 1.1
    scene s0g61 with dissolve
    d "Feisty tongue."
    d "Would work great somewhere else."
    scene s0g62 with dissolve
    mc "I wouldn’t count on that."
    scene s0g63 with dissolve
    d "Huh? Who’s the old guy?"
    scene s0g64 with dissolve
    d "Do you even know who I am, old man?"
    d "Get lost before we send you to a nursing home."
    play sounds2 clench volume 0.3
    scene s0g65 with dissolve
    pause 0.5
    scene s0g66 with dissolve
    pause 0.5
    scene s0g67 with dissolve
    mc "Tell me something, gentlemen."
    mc "Who sent you?"
    mc "Choose your words carefully."
    mc "I’d rather not get my hands dirty again."
    scene s0g68 with dissolve
    d "K-kh… What’re you talking about, old man? N-no one sent us!"
    play sounds2 clench volume 0.3
    scene s0g69 with dissolve
    d "Alright, alright! L-look, we were told to bring that girl in, alive, as a hostage."
    d "That’s all I know!"
    mc "..."
    scene s0g70 with dissolve
    mc "Good."
    mc "If I find out you lied…"
    mc "you won’t get a second chance."
    play sounds2 fall volume 0.3
    scene s0g71 with dissolve
    e "Hey, old fart! Who the hell do you think you are?!"
    scene s0g73 with dissolve
    e "If our bosses hear about you, you’re dead meat! You hea—"
    play sound punch1
    scene s0g74 with vpunch
    pause 0.5
    scene s0g75 with dissolve
    pause 0.5
    play sound punch1
    scene s0g76 with vpunch
    pause 0.5
    play sounds2 fall volume 0.3
    scene s0g77 with dissolve
    C "That’s for putting your hands on me, you piece of shit."
    scene s0g79 with dissolve
    mc "Who were those guys?"
    scene s0g78 with dissolve
    C "Wish I knew… Sis is gonna flip when she hears about this."
    scene s0g80 with dissolve
    C "Still… thanks, [mc]. Seriously. I’ve lost count how many times you’ve bailed us out."
    scene s0g81 with dissolve
    d "You bastard! I won’t forget this!"
    play sounds4 mmove volume 0.5
    scene s0g82 with dissolve
    pause 0.5
    play sounds4 mmove volume 0.5
    scene s0g83 with dissolve
    pause 0.5
    scene s0g84 with dissolve
    d "You’ll pay for humiliating me!"
    play sound running
    scene s0g85 with dissolve
    d "DIE!"
    scene s0g86 
    C "hic!"
    scene s0g87 
    pause 1.0
    scene s0g88 
    pause 1.0
    play sounds2 fall volume 0.3
    stop music fadeout 3.5
    scene s0g89 with vpunch
    mc "(Amateurs.)"
    C "You okay? He had a knife!"
    scene s0g90 with dissolve
    mc "..."
    scene s0g91 with dissolve
    mc "I’m fine."
    mc "What do we do with him?"
    C "This one? God, I’d love to finish him right here… but nah."
    C "Get lost. While you still can."
    scene s0g92 with dissolve
    pause 0.5
    scene s0g91 with dissolve
    pause 0.5
    play sound running
    scene s0g93 with dissolve
    pause 0.5
    scene s0g94 with dissolve
    pause 0.5
    scene s0g96 with dissolve
    C "And don’t show your face again, rat. Next time I won’t be this nice."
    scene s0g95 with dissolve
    j "You won’t see me again!"
    scene s0g97 with dissolve
    C "Creepy, right? First he drags me into this, then they try to gut him."
    scene s0g98 with dissolve
    C "What? I’m serious. Getting stabbed in the back? Feels like absolute garbage."
    play sounds4 mmove volume 0.5
    scene s0g99 with dissolve
    mc "..."
    scene s0g100 with dissolve
    mc "How’d you even get into that mess?"
    scene s0g101 with dissolve
    pause 0.5
    play sounds4 rustling2
    scene s0g102 with dissolve
    pause 0.5
    play sounds4 rustling2
    scene s0g101 with dissolve
    pause 0.5
    scene s0g103 with dissolve
    C "Yeah, I know, I know… sounds stupid."
    C "Jack calls me, says he’s in trouble. I’m like, fine, why not."
    scene s0g104 with dissolve
    C "I get there, and he’s on his knees in front of some thugs."
    scene s0g105 with dissolve
    C "So I step in, thinking they’ll get scared and scatter."
    scene s0g106 with dissolve
    C "You know how it usually goes with me."
    scene s0g107 with dissolve
    C "See someone in trouble… hype myself up… jump in headfirst."
    scene s0g108 with dissolve
    C "Most of the time? They’re grateful. And I know exactly who I’m dealing with."
    scene s0g109 with dissolve
    C "If it’s some serious gang shit, I’m out."
    C "But punks like these? Why not have a little fun."
    scene s0g110 with dissolve
    C "You help people like that, word spreads."
    C "‘Oh, they’re nice, they’ve got your back’- boom, reputation up, money up. Easy."
    scene s0g111 with dissolve
    mc "That’s… one way to look at it."
    mc "But this time it went sideways."
    scene s0g112 with dissolve
    mc "What if I didn’t show up?"
    scene s0g113 with dissolve
    pause 0.5
    play sounds4 rustling2
    scene s0g114 with dissolve
    pause 0.5
    scene s0g115 with dissolve
    C "Honestly? {w}No clue."
    C "They’d probably pass me around… or just take what they want."
    C "Wouldn’t be the first time someone tried."
    scene s0g116 with dissolve
    mc "..."
    scene s0g117 with dissolve
    mc "You’ve got a strange way of looking at things."
    scene s0g118 with dissolve
    C "..."
    scene s0g119 with dissolve
    mc "If I hadn’t stepped in… your sister would’ve had my head."
    play sound concstep1
    scene s0g120 with dissolve
    mc "You really know how to cause her trouble."
    play sound concstep1
    scene s0g121 with dissolve
    C "Wouldn’t be me otherwise."
    C "Had to deal with her crap growing up—now it’s her turn."
    play sound concstep1
    scene s0g122 with dissolve
    mc "Wait… you do this on purpose?"
    scene s0g123 with dissolve
    C "Of course. What, you think I’m stupid or something?"
    mc "..."
    play sound concstep1
    scene s0g124 with dissolve
    C "Hey! Rude!"
    mc "Kidding."
    C "(sigh)…you’re unbelievable."
    scene s0g125 with dissolve
    C "So… what’s the plan for tonight?"
    mc "{b}We{/b} don’t have plans."
    play sound concstep1
    scene s0g126 with dissolve
    mc "{b}I{/b} do."
    mc "I’m meeting your sister."
    C "Ugh, you’re {b}such{/b} a grump."
    stop sounds1 fadeout 1.0
    stop music fadeout 2.0
    
    scene s0g127 with dissolve
    a "..."

    image s0transition1 = Movie(channel="movie_dp", loop = False, play="video/s0transition1.webm")
    show s0transition1
    $ renpy.pause(0.6, hard=True)

    play music arrived
    play sounds3 warptravaling fadein 0.6 loop
    scene s0g128
    pause 2.3
    scene s0g129 with dissolve
    pause 0.5
    play sound pisolsil
    scene s0g130 with dissolve
    pause 0.5
    play sound pisolsil
    scene s0g132 with dissolve
    D "Ah..."
    scene s0g133 with dissolve
    D "Ah... My head...."
    scene s0g134 with dissolve
    D "..."
    scene s0g135 with dissolve
    D "(What the hell is this?)"
    scene s0g136 with dissolve
    pause 1.1
    scene s0g137 with dissolve
    aa "{font=Cybertron.otf}What do we do with him? He didn’t try to harm our target."
    scene s0g138 with dissolve
    a "{font=Cybertron.otf}He saw us — that’s unacceptable."
    play sound pisolsil
    stop sounds3 fadeout 0.5
    stop music 
    scene black with vpunch 
    pause 1.5
    play sounds2 cityevening1 fadein 2.3 loop

    scene s0h1 with dissolve
    C "You know… I might not show it, but I was actually really glad I ran into you back there."
    C "So… what are you even doing here?"
    play sound concstep1
    scene s0h2 with dissolve
    mc "Honestly… I’m a bit out of place here."
    play sound concstep1
    scene s0h3 with dissolve
    C "You’re the only one who thinks that, you know."
    C "You should come by more often."
    C "Sis would be way too happy about it."
    play sound concstep1
    play music alexandroambience fadein 2.0
    scene s0h4 with dissolve
    x "No way… My eyes must be deceiving me!"
    scene s0h5 with dissolve
    mc "I know that voice…"
    play sound concstep1
    scene s0h6 with dissolve
    x "HERMANO! What brings you here?!"
    play sound bodytap
    scene s0h7 with dissolve
    x "Great to see you, amigo! 15 years, and you’ve only gotten stronger!"
    scene s0h10 with dissolve
    pause 0.5
    play sound bodytap
    scene s0h8 with dissolve
    x "Still training, huh? You’re in great shape as always, Commander!"
    scene s0h9 with dissolve
    mc "Good to see you too."
    mc "You look steady."
    scene s0h8 with dissolve
    x "Best prosthetic money can buy, hermano."
    x "Still complains when it rains, though."
    x "But hey. Could've been worse."
    scene s0h9 with dissolve
    mc "Yeah."
    x "Mona and Jack didn't get to complain."
    mc "But what are you doing here, Alexandro?"
    scene s0h13 with dissolve
    x "Hahaha! A lot’s changed since we last met."
    play sound bodytap
    scene s0h14 with dissolve
    pause 0.5
    scene s0h7 with dissolve
    x "You know better than anyone, Commander — vets have a hard time finding honest work these days."
    x "Gotta feed the family, right?"
    play sound mmove
    scene s0h15 with dissolve
    x "Thanks to Miss Anya and Olivia, I can take care of my family without depriving them of anything."
    x "I’m truly grateful to them."
    scene s0h16 with dissolve
    C "If anything, we should be thanking you."
    C "Not every place gets a guard like you."
    C "So yeah… works out pretty damn well for us."
    scene s0h18 with dissolve
    mc "I’m glad it worked out for you."
    stop music fadeout 2.0
    scene s0h19 with dissolve
    x "..."
    scene s0h20 with dissolve
    x "Commander… You okay? You look—"
    play music alexandromusic
    scene s0h19 with dissolve
    mc "..."
    x "..."
    scene s0h20 with dissolve
    x "Sorry, sir, I have to take this call."
    stop music
    play sound phonebuttonm
    scene s0h22 with dissolve
    x "Yes?"
    scene s0h21 with dissolve
    x "..."
    scene s0h23 with dissolve
    mc "(Is it that obvious…?)"
    scene s0h24 with dissolve
    mc "(Or was I just lying to myself…?)"
    play sound alexandromeme
    pause 1.5
    scene s0h25 with dissolve
    x "WHAT?!"
    x "No way… "
    x "How could they—"
    x "They threw out…... {w=1}my {w=1}plush crocodiles?!"
    stop sound fadeout 0.5
    play sounds1 funnymom fadein 1.5
    scene s0h26 with dissolve
    x "NOOOOOOOOOOO!"
    scene s0h27 with dissolve
    x "My croc babies… They tossed them… in the trash…"
    b "..."
    scene s0h28 with dissolve
    mc "…You good?"
    scene s0h29 with dissolve
    C "He’s like this every time someone mentions his crocodiles."
    scene s0h28 with dissolve
    mc "…We didn’t see that."
    scene s0h29 with dissolve
    C "Yeah… let’s just pretend none of that happened."
    play sounds1 funnymom1
    stop sounds2 fadeout 1.0
    scene black with dissolve
    mc "Good seeing you again, Alex."
    pause 1.0
    $ persistent.chapter_act0_scene += 1

label bar_olivica:
    stop music fadeout 0.4
    pause 0.4
    play music dractir1 volume 0.4 fadein 1.1

    play sounds1 doorclose 
    scene s0h30 with dissolve
    C "Well… welcome to our very humble little spot."
    C "Try not to judge too hard."
    scene s0h31 with dissolve
    mc "If this is humble, I’d hate to see what you call not humble."
    scene s0h32 with dissolve
    C "Thanks. We actually put a ton of work into this place."
    C "Expanded it, redid the whole interior…"
    scene s0h33 with dissolve
    C "Now it’s more like a proper lounge instead of that sad excuse of a bar we had before."
    scene s0h35 with dissolve
    C "Then again… calling it a bar back then is generous."
    C "It was more like a warehouse."
    C "…Or something worse."
    scene s0h34 with dissolve
    mc "..."    
    scene s0h36 with dissolve
    C "Anyway—"
    C "What’s up with you?"
    scene s0h37 with dissolve
    mc "I’ll admit… I’m impressed."
    mc "But how the hell did you pull this off?"
    scene s0h38 with dissolve
    C "(Deep sigh) …mmh."
    scene s0h39 with dissolve
    C "That’s a secret I’m not ready to spill just yet."
    C "Gotta keep some mystery, you know?"
    scene s0h40 with dissolve
    mc "Yeah… figures."
    mc "She had a hand in this, didn’t she?"
    scene s0h41 with dissolve
    C "I mean… it wasn’t just her."
    C "But yeah, Olivia carried most of it."
    C "Permits, paperwork, investors… she handled all that boring hell."
    scene s0h42 with dissolve
    C "Even pulled in some serious sponsors… no idea why they trusted us, but hey."
    C "…How are you holding up?"
    C "We heard what happened."
    C "She really was… something else."
    scene s0h43 with dissolve
    mc "..."
    scene s0h44 with dissolve
    mc "Yeah…"
    mc "She was."
    scene s0h45 with dissolve
    mc "So… did you get into that university?"
    mc "That was your plan, right?"

    image s0transition2 = Movie(channel="movie_dp", loop = False, play="video/s0transition2.webm")
    show s0transition2 with dissolve
    $ renpy.pause(0.7, hard=True)

    play sound metalhit2
    scene s0h46 
    b "..."
    scene s0h47 with dissolve
    pause 1.1
    scene s0h48 with dissolve
    pause 1.1
    scene s0h49 with dissolve
    mc "Someone over there looks ready to blow."
    scene s0h50 with dissolve
    C "No clue who you’re talking about."

    $ Olivia_path = True

    $ unlock_olivia = 1

    scene s0h51 with dissolve
    h "Touch me again—"
    h "I swear, I’ll drop you where you stand."
    scene s0h52 with dissolve
    h "Now."
    scene s0h53 with dissolve
    h "Run."
    h "Before I start taking fingers."
    scene s0h55 with dissolve
    C "Oof… yeah. That’s rage mode."
    C "She’s really pissed."
    scene s0h54 with dissolve
    mc "Yeah… she hasn’t changed."
    scene s0h56 with dissolve
    C "She kinda has to be like that."
    C "Every day it’s the same story, some cocky idiot thinks he’s special."
    C "Thinks he’s getting into her pants."
    stop music fadeout 5.0
    play music1 bar1 fadein 5.0
    scene s0h58 with dissolve
    h "..."
    scene s0h59 with dissolve
    mc "All these years… and you’re still the same."
    scene s0h60 with dissolve
    mc "…Hey."
    scene s0h61 with dissolve
    h "..."
    scene s0h62 with dissolve
    h "And what brings you here?"
    scene s0h63 with dissolve
    mc "Figured I’d stop by."
    mc "See how you’re holding up."
    scene s0h64 with dissolve
    C "Sis, ever thought about not scaring off the customers?"
    scene s0h65 with dissolve
    h "How I’ve been…?"  
    h "Oh, I’m thriving."
    h "Can’t you tell?"
    scene s0h66 with dissolve
    h "Signed contracts."
    h "Pulled sponsors."
    h "Expanded the place…"
    h "Even opened another bar across town."
    scene s0h67 with dissolve
    C "Hey! Don’t ignore me!"
    play sound pouring
    scene s0h69 with dissolve
    C "Wait… are you actually upset?"
    scene s0h70 with dissolve
    pause 0.5
    scene s0h71 with dissolve
    h "..."
    scene s0h72 with dissolve
    C "Poke."
    scene s0h73 with dissolve
    C "C’mon, don’t sulk."
    C "So I ignored your messages. Big deal."
    scene s0h74 with dissolve
    C "Now quit that and go charm our guest."
    C "You’ve got that scary-smile combo, use it."
    scene s0h75 with dissolve
    C "..."
    scene s0h76 with dissolve
    h "It’s the same loop, {w=0.7}sleep, {w=0.5}work, {w=0.4}sleep, {w=0.3}work, {w=0.2}SLEEP, {w=0.1}WORK…"
    scene s0h77 with dissolve
    h "I’m so fed up with it, you know? {w=0.9}HA-{w=0.2}HA-{w=0.1}HA, {w=0.5}Seven years — same damn grind. {w=1.2}And what do I have?{w=0.9} No boyfriend. {w=0.5}No husband. {w=0.3}Nothing."
    scene s0h78 with dissolve
    h "Meanwhile everyone else? Married. Kids. {w=0.9}CAN YOU BELIEVE IT? {w=0.7}AND THEY JUST LOVE REMINDING TO ME, {w=0.6}LAUGHING, {w=0.3}LIKE IT'S FUNNY."
    scene s0h79 with dissolve
    h "But whatever, just forget it. {w=0.9}And to top it all off, {w=0.7}you know, I haven’t had a good  {w=0.7}SCREW since THAT NIGHT… {w=0.7}FOR YEARS, AND YOU’RE STANDING HERE ASKING ME HOW I’M DOING???"
    play sound glassput
    play sound1 glasstablemov
    scene s0h80 with dissolve
    h "I’m doing amazing."
    h "Really."
    h "Couldn’t be better."

    scene s0h81 with dissolve
    mc "..."
    a "You know we’d love to spend the night with you!"
    scene s0h83 with dissolve
    h "Yeah, yeah, get lost."
    scene s0h84 with dissolve
    mc "Sounds like it’s been a long few years."
    mc "But after all this time…"
    mc "With the way people look at you?"
    mc "You could’ve had anyone."
    scene s0h85 with dissolve
    h "(Scoffs) That’s the thing."
    h "It’s not about who {b}wants{/b} me."
    h "It’s about who’s {b}worth{/b} it."
    scene s0h86 with dissolve
    h "..."
    scene s0h87 with dissolve
    mc "..."
    scene s0h88 with dissolve
    h "And no, it’s not about Anya. If that’s where your head went."
    scene s0h89 with dissolve
    pause 0.5
    scene s0h90 with dissolve
    pause 0.5
    scene s0h91 with dissolve
    mc "Before that..."
    mc "Anya ran into trouble outside."
    scene s0h85 with dissolve
    h "What kind of trouble?"
    scene s0h86 with dissolve
    mc "The kind where someone wanted her alive."
    mc "As leverage."
    scene s0h89 with dissolve
    h "..."
    h "Who?"
    scene s0h90 with dissolve
    pause 0.5
    scene s0h91 with dissolve
    mc "Didn't get a name."
    mc "But they knew she was your sister."
    scene s0h85 with dissolve
    h "Old business."
    h "Don't worry about it. I'll make a couple of calls later."
    scene s0h89 with dissolve
    pause 0.5
    scene s0h90 with dissolve
    pause 0.5
    scene s0h91 with dissolve
    mc "…Good."
    mc "Then I don’t need to step in."
    scene s0h92 with dissolve
    h "...How are {b}you{/b} holding up?"
    h "I heard what happened."
    h "I’m… sorry."
    scene s0h93 with dissolve
    mc "..."
    scene s0h94 with dissolve
    pause 0.5
    scene s0h95 with dissolve
    mc "I need a favor."
    mc "Take a look at this."
    scene s0h96 with dissolve
    mc "I know we said we were done with this."
    scene s0h97 with dissolve
    mc "But the past doesn’t stay buried."
    h "..."
    scene s0h98 with dissolve
    pause 0.5
    scene s0h99 with dissolve
    pause 0.5
    scene s0h100 with dissolve
    pause 0.5
    scene s0h101 with dissolve
    h "..."
    scene s0br1 with dissolve
    h "…Wait."
    h "That’s not possible…"
    h "He’s dead."
    h "You put him down yourself."
    h "Al-Zahira. Twenty years ago."
    scene s0h91 with dissolve
    mc "Yeah… so did I."
    mc "But this says otherwise."
    mc "He’s alive."
    mc "And looks better than both of us."
    scene s0h103 with dissolve
    mc "But that’s not why I’m here."
    mc "Look at the other one."
    scene s0h102 with dissolve
    h "You’re serious…?"
    scene s1s7 with dissolve
    h "Is that—?"
    mc "I don’t know."
    mc "But I need to find out."
    h "Don't do that."
    mc "Do what?"
    h "Sound hopeful."
    pause 1.1
    mc "Too late."
    "An awkward silence settles between them."
    scene s0h104 with dissolve
    h "Anya."
    h "We’re closing early."
    h "Give them an hour. No more."
    scene s0h105 with dissolve
    mc "Won’t that hurt your reputation?"
    scene s0h107 with dissolve
    h "I’ve got bigger problems than reputation."
    stop music1 fadeout 6.2
    scene black with dissolve 
    pause 2.1
    

    play music goneforever fadein 9.0 
    play sound closedoor
    play sounds1 raincity3 loop volume 0.3
    scene s0h108 with dissolve
    mc "..."
    play sounds mmove
    scene s0h109 with dissolve
    h "..."
    scene s0h110 with dissolve
    h "Where did you get this info?"
    scene s0h111 with dissolve
    mc "Norman gave me this earlier today."
    scene s0h110 with dissolve
    h "Norman?"
    h "Your kid?"
    scene s0h111 with dissolve
    mc "My son…"
    mc "Long story."
    scene s0h110 with dissolve
    h "How reliable is it?"
    scene s0h111 with dissolve
    mc "It came with coordinates."
    mc "And a photo no one should be able to take."
    scene s0h109 with dissolve
    b "..."
    scene s0h110 with dissolve
    h "We lost Jake and Mona that day. Alexandro lost a leg, for life."
    h "All because some genius commander called friendly fire. Beautiful, right?"
    scene s0h113 with dissolve
    h "And now, after all this time, they suddenly need you again?"
    h "Please tell me you told them to fuck off."
    scene s0h112 with dissolve
    mc "..."
    scene s0h114 with dissolve
    mc "You know Richard handled it."
    scene s0h110 with dissolve
    h "Yeah… figures. So you didn’t."
    scene s0h111 with dissolve
    mc "Azarkhan’s people were already inside."
    scene s0h113 with dissolve
    h "Don’t."
    h "We both know that’s bullshit."
    h "This whole thing? It’s about that photo of Lora."
    h "That’s the only reason you’re even thinking about going back."
    scene s0h112 with dissolve
    mc "..."
    scene s0h115 with dissolve
    h "I get it."
    h "You did your service. Came back. Tried to live quiet."
    h "Then boom, your wife’s ‘dead’, and somehow you end up blaming your own kid for it."
    scene s0h116 with dissolve
    h "And just when things start to calm down, here we go again."
    scene s0h118 with dissolve
    pause 1.0
    scene s0h119 with dissolve
    h "{b}Did you know? That global terrorist you supposedly killed is alive!{/b}" 
    h "Or {b}Oh, and your dead wife? Not so dead. Here, have some photos.{/b}"
    scene s0h118 with dissolve
    mc "..."
    scene s0h120 with dissolve
    mc "…What is that, a lollipop?"
    scene s0h118 with dissolve
    pause 1.0
    scene s0h119 with dissolve
    h "I quit smoking, remember?"
    h "Your dumb lollipop idea actually worked."
    h "So yeah… I’m sticking with it."
    scene s0h118 with dissolve
    pause 1.0
    scene s0h119 with dissolve
    h "You know… maybe it’s just not worth it."
    h "Yeah, the idea of bringing Lora back sounds nice."
    h "Too nice."
    pause 1.1
    h "But what if that’s not even her?"
    scene s0h118 with dissolve
    pause 1.0
    scene s0h119 with dissolve
    h "Maybe it’s time to stop chasing ghosts."
    h "Look around."
    h "You finally have Norman back in the room with you."
    h "You have a granddaughter who thinks you hung the moon."
    h "And you're about to walk into the same fire again."
    h "Trust me, even that doesn't last forever."
    scene s0h118 with dissolve
    pause 1.0
    scene s0h119 with dissolve
    h "Just saying."
    scene s0h120 with dissolve
    mc "Maybe."
    mc "But if there’s even a chance that photo is real..."
    mc "I have to know."
    scene s0h118 with dissolve
    pause 1.0
    scene s0h119 with dissolve
    h "You’re still the same."
    stop music fadeout 3.5
    play sound closedoor
    scene s0h121 with dissolve
    C "Sis, we’ve got trouble."
    scene s0h122 with dissolve
    h "What happened?"
    scene s0h123 with dissolve
    C "..."
    scene s0h124 with dissolve
    h "Why are you just standing there? Talk."
    play sounds2 notificationphone 
    scene s0h125 with dissolve
    pause 0.5
    scene s0h126 with dissolve
    C "Those guys from earlier?"
    C "Someone paid their boss to make noise here."
    scene s0h127 with dissolve
    h "We’ve got security for a reason."
    h "Why not let Alexandro throw them out?"
    scene s0h129 with dissolve
    C "This one’s some bigshot. We can’t use force."
    N "So, Dad, do you agree?"
    scene s0h130 with dissolve
    mc "I need to go."
    mc "If you’re in — tomorrow, 5:00 a.m."
    mc "Outside my place."
    scene s0h131 with dissolve
    h "Maybe. No promises."
    scene s0h132 with dissolve
    C "..."


    scene black with dissolve 
    pause 2.1
    stop sounds1
    stop music 
    $ persistent.chapter_act0_scene += 1

label norman_home:

    stop music fadeout 0.5
    play music1 loramemory1 fadein 5.5
    scene s0l122 with linearblur
    ri "My dear old friend,"
    scene s0k1 with linearblur
    ri "I’ve been meaning to write to you for a long time."
    scene s0k2 with dissolve
    ri "Something always stopped me — wrong time, wrong place, or maybe I just didn’t know how to begin."
    scene s0k3 with dissolve
    ri "I hope this letter finds you and your loved ones in good health."
    scene s0k4 with dissolve
    ri "I know how much you hate reading reports and briefings."
    scene s0k5 with dissolve
    ri "That’s why I’m writing you this letter..."
    scene s0k6 with dissolve
    ri "Not as your Commander-in-Chief, but as your old friend."
    scene s0k7 with dissolve
    ri "The world is in unrest — granted, it always has been, but now the tension has reached a breaking point."
    scene s0k8 with dissolve
    ri "If we don’t act, it won’t just affect you — it’ll affect everyone you care about."
    scene s0k9 with dissolve
    ri "Azarkhan has returned from the dead. {b}How{/b} — we don’t know."
    scene s0k10 with dissolve
    ri "But we’ve uncovered some information suggesting he’s backed by powerful entities."
    scene s0k11 with dissolve
    ri "Possibly... extraterrestrial."
    scene s0pp79 with dissolve
    ri "I know how insane that sounds." 
    scene s0pp78 with dissolve
    pause 1.1
    scene s0pp76 with dissolve
    ri "I wish I could share the details..."
    scene s0pp77 with dissolve
    pause 1.1
    scene black with vpunch 
    pause 2.1
    scene s0k12 with linearblur
    ri "but I can’t do that in a letter."
    play sounds4 roomemptyambience1 loop fadein 1.0 volume 0.7 
    scene s0k13 with dissolve
    ri "And yet, not mentioning the following would be a mistake."
    scene s0k14 with dissolve
    ri "What I can say is this: we found a photo, taken just before Lora disappeared."
    scene s0k15 with dissolve
    ri "We don’t know who took it, but it changed everything."
    scene s0k16 with dissolve
    ri "Azarkhan’s return, Lora’s vanishing, and what you saw eight years ago — they’re all connected. {w}To that forest."
    play sounds2 closecabinet
    scene s0l124 with linearblur
    ri "Or more precisely — to what’s {b}in{/b} it."
    ri "That’s why I’m asking. We need your help."
    scene s0l123 with dissolve
    ri "P.S. You’ll find coordinates at the bottom. If you decide you want answers."
    scene s0k17 with linearblur
    pause 0.5
    play sound pwot
    scene s0k18 with dissolve
    mc "(Going somewhere unknown… based on a letter.)"
    mc "(Most people would call that stupid.)"
    scene s0k19 with dissolve
    mc "(And maybe they’d be right.)"
    mc "(Maybe I should walk away.)"
    play sound putcase2
    scene s0k20 with dissolve
    mc "(A letter. Ghosts. Coordinates to nowhere.)"
    mc "(Yeah… sounds insane.)"
    mc "(But I’m not turning my back on this.)"
    play sounds1 putcase1
    scene s0k21 with dissolve
    mc "(There are answers out there.)"
    mc "(Answers I was never given.)"
    mc "(A life I never got to live.)"
    scene s0k22 with dissolve
    mc "(And somehow… it feels like hope.)"
    play sounds1 clampsilencer
    scene s0k24 with dissolve
    pause 0.5
    scene s0k23 with dissolve
    mc "(That hope… it’s enough.)"
    play sounds1 akreload
    scene s0k26 with dissolve
    pause 0.5
    scene s0k25 with dissolve
    mc "(Feels like I’m back there again.)"
    play sounds2 mmove
    scene s0k27 with dissolve
    pause 0.5
    scene s0k28 with dissolve
    mc "(This time… I find it.)"
    scene s0k29 with dissolve
    mc "(End what started.)"
    mc "(Take back what I lost.)"
    scene s0k30 with dissolve
    mc "Damn… sights are off again."
    play sounds2 tabletakes
    scene s0k31 with dissolve
    pause 0.5
    stop music1 fadeout 11.2
    scene s0k32 with dissolve
    pause 0.5
    play sounds1 oldladder
    scene s0k33 with dissolve
    pause 0.5
    scene s0k36 with dissolve
    mc "Why aren’t you asleep?"
    mc "Something wrong?"
    scene s0k34 with dissolve
    N "Dad… we need to talk."
    scene s0k37 with dissolve
    mc "..."
    play sounds2 mmove
    scene s0k38 with dissolve
    mc "It’s late."
    mc "Go get some sleep."
    scene s0k39 with dissolve
    N "DAD!"
    scene s0k40 with dissolve
    N "I’m not a kid anymore, alright?!"
    play sounds2 mmove
    scene s0k41 with dissolve
    N "I know what you’re planning."
    N "You’re going after Mom…"
    N "But you don’t even know where to start!"
    mc "I’ve got coordinates."
    N "Dad—!"
    scene s0k42 with dissolve
    pause 1.7
    scene s0k43 with dissolve
    pause 0.5
    play sound pwot
    scene s0k44 with dissolve
    pause 0.5
    scene s0k45 with dissolve
    mc "..."
    scene s0k46 with dissolve
    mc "…Alright."
    mc "What is it?"
    scene s0k47 with dissolve
    N "What time are we leaving?"
    scene s0k45 with dissolve
    mc "..."
    scene s0k46 with dissolve
    mc "We?"
    mc "You’re staying here."
    scene s0k47 with dissolve
    N "Why?! Why can’t I come with you?!"
    scene s0k45 with dissolve
    mc "..."
    scene s0k46 with dissolve
    mc "Because you’ve got a life ahead of you."
    mc "I’m not letting that place take you too."
    scene s0k47 with dissolve
    N "And what about your life?!"
    N "What did you read in that letter?"
    N "And why the hell can’t I come with you?!"
    scene s0k45 with dissolve
    mc "..."
    scene s0k48 with dissolve
    pause 0.5
    play sounds2 mmove
    scene s0k49 with dissolve
    mc "Let me ask you something."
    mc "You ever killed anyone?"
    scene s0k50 with dissolve
    N "N-no... not yet."
    play sounds2 mmove
    scene s0k51 with dissolve
    mc "I have."
    mc "Dozens."
    mc "Hundreds."
    scene s0k52 with dissolve
    mc "..."
    scene s0k53 with dissolve
    N "W-why are you telling me this…?"
    play sound clothess
    scene s0k54 with dissolve
    mc "Because if I don’t make it… no one’s surprised."
    mc "But you?"
    mc "That’s different."
    N "Don’t say that!"
    N "And besides… you don’t know that forest like I do!"
    scene s0k56 with dissolve
    mc "The public trail?"

    scene s0k64 with dissolve
    N "No."
    N "The place Mom took me."
    N "Past the old service road."
    N "Your coordinates won't get you through that part."

    scene s0k57 with dissolve
    mc "You should've opened with that."

    N "I thought you'd go without me."
    scene s0k56 with dissolve
    mc "..."
    scene s0k57 with dissolve
    mc "You sure about this?"
    scene s0k64 with dissolve
    N "Yeah. I am."
    scene s0k58 with dissolve
    pause 1.5
    scene s0k59 with dissolve
    pause 0.5
    play sound clench
    scene s0k60 with dissolve
    mc "You know how to use that?"
    scene s0k62 with dissolve
    N "Dad, I..."
    scene s0k63 with dissolve
    N "I don’t know if I’ve got the strength… or the guts."
    scene s0k45 with dissolve
    mc "..."
    scene s0k46 with dissolve
    mc "Then if you’re coming with me… you don’t slow me down."
    scene s0k45 with dissolve
    mc "..."
    scene s0k46 with dissolve
    mc "You can still walk away."
    scene s0k64 with dissolve
    N "No!"
    N "I’ll do whatever it takes. I promise."
    scene s0k65 with dissolve
    mc "..."
    play sound bodytap
    scene s0k66 with dissolve
    pause 0.5
    scene s0k67 with dissolve
    mc "I’m counting on you, Norman."
    scene s0k68 with dissolve
    N "…Thanks, Dad."
    scene s0k69 with dissolve
    pause 0.5
    scene s0k70 with dissolve
    pause 0.5
    play sound bodytap
    scene s0k71 with dissolve
    mc "You’ve grown."
    mc "Your mother would’ve been proud."
    scene s0k69 with dissolve
    pause 0.5
    stop sounds4
    scene black with dissolve
    pause 3.0


    scene s0k72 with dissolve
    mc "(Was this the right call…?)"
    mc "(Maybe I should talk him out of it…)"
    scene s0k73 with dissolve
    mc "(No. Enough.)"
    scene s0k74 with dissolve
    mc "(He’s not a kid anymore.)"
    mc "(Respect that.)"

    scene black with dissolve
    pause 2.0
    
    scene s0k75 with dissolve
    mc "(Alright… I’ve got everything.)"
    mc "(Just a few things left and—)"
    scene s0k76 with dissolve
    mc "..."
    play music lastgoodbye fadein 5.0
    scene s0k77 with dissolve
    mc "(Or maybe… not just me after all.)"
    scene s0k78 with dissolve
    mc "(Focus.)"
    mc "(We’ve done this before.)"
    scene s0k79 with dissolve
    pause 0.5
    scene s0l128 with dreamyzoom
    h "You’re taking us with you?! Oh wow, Anya is going to be thrilled!"
    L "Yeah… we thought it might be a good idea."
    scene s0l129 with dreamyzoom
    L "Come on, you two."
    L "One picture. For the memory."
    mc "Smile!"
    scene s0k80 with linearblur
    mc "{b}Sigh{/b}"
    scene s0k81 with dissolve
    mc "..."
    mc "(Now or never...)"
    scene s0l126 with dreamyzoom
    mc "Will you marry me?"
    L "Oh my God — YES! {w=0.2}YES! {w=0.2}YES! {w=0.2}YES!"
    L "A thousand times yes!"
    scene s0l127 with dreamyzoom
    L "Do you believe in fate, darling?"
    mc "Not really, no."
    L "Out of billions of people… and all the worlds out there—"
    L "we found each other here."
    L "If that’s not fate… what is?"
    scene s0k82 with dissolve
    mc "..."
    scene s0l125 with linearblur
    mc "Let go, you're gonna strangle me..."
    L "No!"
    L "You’re mine."
    L "I’m never letting go."   
    scene s0k83 with dissolve
    mc "..."    
    mc "Yeah…"
    mc "That’s how I’ll remember you."
    mc "Always smiling."
    mc "Always… alive."
    scene s0k84 with dissolve
    mc "(I’ve made my choice.)"
    mc "(Thank you.)"
    play sounds2 closecabinet
    scene s0k85 with dissolve
    mc "(…Goodbye.)"
    mc "(To the grave I built for you.)"
    scene s0k86 with dissolve
    Lor "..."
    Lor "...So you finally stopped running."
    scene s0k87 with dissolve
    Lor "...and chose to face it."
    scene s0k88 with dissolve
    Lor "..."
    scene s0k89 with dissolve
    Lor "Thank you… my love."
    Lor "For finally facing it."
    scene s0k91 with dissolve
    Lor "..."
    stop music fadeout 6.0
    scene black with dissolve
    pause 3.0
    play sounds2 roomemptyambience1 loop volume 0.4 fadein 1.1
    play sounds3 doorclose
    play music1 s45c4mcscene fadein 5.4
    scene s0pp80 with dissolve 
    pause 1.1
    scene s0pp81 with dissolve 
    pause 1.1
    scene s0pp82 with dissolve 
    pause 1.1
    scene s0pp83 with dissolve 
    pause 1.1
    scene s0pp80 with dissolve 
    pause 1.1
    scene s0pp85 with dissolve 
    mc "(Operation Drake. Al-Zahira, 2018.)"
    mc "(People vanished. No trace.)"
    mc "(The case.)"
    mc "(No core. No cell.)"
    mc "(Just that liquid.)"
    scene s0pp46 with dissolve 
    mc "(Forest. Starlit Stand.)"
    mc "(2030 incident.)"
    mc "(Same pattern. Different place.)"
    mc "(Flash reported.)"
    scene s0pp80 with dissolve 
    pause 1.1
    scene s0pp81 with dissolve 
    mc "(Different places… same result.)"
    scene s0pp82 with dissolve 
    mc "(…And I was there. Both times.)"
    scene s0pp83 with dissolve 
    pause 1.1
    scene s0pp84 with dissolve 
    mc "(Norman mentioned a lab… in the forest.)"
    mc "(So Al-Zahira… had one too.)"
    pause 1.5
    mc "(No…)"
    mc "(Not just a lab.)"
    mc "(Something inside it.)"
    scene s0pp85 with dissolve
    pause 1.8
    scene s0pp46 with dissolve
    pause 1.8
    scene s0a3 with dreamyzoom
    show memoryframe with dissolve
    Lo "The topic’s kind of unsettling, It’s something related to teleportation…"
    Lo "I heard it requires energy. Living energy."
    scene s0pp86 with dissolve 
    pause 1.2
    scene s0pp87 with dissolve 
    mc "(Energy…)"
    scene s0pp90 with dissolve
    pause 1.8
    scene ch 113 with dreamyzoom 
    show memoryframe with dissolve
    N "Something that was supposed to extend life."
    N "But it turned out to be something else."
    scene ch 135 with dissolve
    show memoryframe with dissolve
    N "It feeds… whatever’s inside."
    scene s0pp86 with dissolve 
    pause 1.2
    scene s0pp87 with dissolve 
    pause 1.2
    scene s0pp91 with dissolve 
    mc "(…Warp drive.)"
    mc "(Norman said that before…)"
    scene ch 155 with dreamyzoom
    show memoryframe with dissolve
    mc "A warp drive?"
    mc "You serious right now?"
    scene ch 172 with dreamyzoom
    show memoryframe with dissolve
    N "Dad, this is, this is real. I’m not making this up!"
    scene s0pp86 with dissolve
    mc "(And I laughed at him…)"
    mc "..."
    scene s0pp87 with dissolve
    mc "(But the man in the mask…)"
    scene s0pp86 with dissolve 
    pause 1.2
    scene s0pp89 with dissolve
    pause 1.8
    scene s0l122 with dreamyzoom 
    show memoryframe with dissolve
    ri "...he’s backed by powerful entities."
    ri "Possibly... extraterrestrial."
    scene s0pp87 with dissolve 
    pause 1.2
    scene s0pp86 with dissolve 
    pause 1.2
    scene ch 175 with dreamyzoom 
    show memoryframe with dissolve
    N "It wasn’t my choice… I was led there."
    N "A man… wearing a black mask."
    scene s0pp87 with dissolve 
    pause 1.2
    scene s0pp88 with dissolve 
    pause 1.2
    scene pp122 with dissolve
    mc "(That man…)"
    mc "(The one behind all this…)"
    mc "(It has to be him.)"
    scene ls 7 with dissolve
    mc "(He wasn’t random.)"
    mc "(He was leading people there.)"
    stop music1 fadeout 1.5
    scene black with dissolve
    mc "(…Or is it?)"
    pause 3.0
    play music anyasounds11 fadein 8.3
    play sounds1 anyahome loop fadein 5.1
    scene s0h133 with dissolve
    C "(Singing a tune)"
    scene s0h134 with dissolve
    C "Sooo… sis."
    C "What are you gonna do about [mc]’s little request?"
    scene s0h135 with dissolve
    h "I don’t really have a choice, do I?"
    play sounds2 rustling2
    scene s0h136 with dissolve
    h "After everything he’s done… walking away now would be a shitty move."
    pause 1.1
    h "And if Azarkhan really is breathing again..."
    h "Waiting for him to knock would be even dumber."
    scene s0h137 with dissolve
    C "Mhm… sure. Just pride."
    C "So what’s with the outfit?"
    C "You heading out on a job… or a very suspicious sleepover?"
    h "Very funny."
    scene s0h138 with dissolve
    h "Listen. I don’t know how long I’ll be gone."
    h "You’re in charge while I’m out. Don’t screw it up."
    scene s0h139 with dissolve
    h "If anything comes up, go to Alexandro."
    h "And no hero crap."
    h "If anyone asks for you by name, you call Kayla."
    C "Because of those guys?"
    h "Because I said so."
    scene s0h140 with dissolve
    h "But only if it’s really bad. Don’t panic-call her over nothing."
    scene s0h141 with dissolve
    C "Relax. I’ve got this."
    C "I’m not a kid anymore."
    play sounds2 mmove
    scene s0h142 with dissolve
    C "Just… be careful, okay?"
    C "I’ve heard things about that place. None of them nice."
    play sounds2 mmove
    scene s0h143 with dissolve
    h "We’ve handled worse. Don’t worry about me."
    scene s0h144 with dissolve
    C "Besides… he’s still stuck in the past."
    C "You keep going back, you’re just gonna tear yourself apart."
    stop music fadeout 3.0
    scene s0h145 with dissolve
    h "..."
    scene s0h146 with dissolve
    pause 0.5
    scene s0h147 with dissolve
    pause 0.5
    scene s0h149 with dissolve
    h "That’s my mess to deal with."
    h "Take care, Anya."
    h "And seriously, don’t burn the place down."
    scene s0h148 with dissolve
    C "Heh. No promises."
    
    play music shiyaroom fadein 3.0
    play sounds2 doorclose
    scene s0h150 with dissolve
    C "..."
    scene s0h151 with dissolve
    pause 0.5
    scene s0h152 with dissolve
    CC "Alone again. Cute."
    CC "Still pretending you matter… that anyone actually needs you."
    scene s0h153 with dissolve
    CC "You wanna know the truth, Anya?"
    CC "They don’t leave because they have to."
    CC "They leave because you’re exhausting."
    CC "Dead weight."
    scene s0h154 with dissolve
    CC "You ever wonder why Olivia’s so cold with you?"
    CC "There’s a reason."
    scene s0h155 with dissolve
    CC "She {b}blames{/b} you."
    CC "For mom. For everything that fell apart."
    scene s0h157 with dissolve
    C "—No."
    C "She just… trusts me."
    C "She knows I can handle myself."
    scene s0h156 with dissolve
    CC "No, sweetheart."
    CC "That’s just what you tell yourself."
    CC "She’s just too tired to keep saving you."
    scene s0h157 with dissolve
    C "We’ve been over this."
    scene s0h158 with dissolve
    CC "Yeah. And I keep repeating it for a reason."
    CC "Because you still won’t admit it."
    play sounds2 whoosh
    scene s0h159 with dissolve
    CC "You’ve always been a burden."
    CC "Mom died saving {b}you{/b}."
    CC "She should’ve let you go."
    scene s0h160 with dissolve
    CC "You think she chose you?"
    CC "No."
    CC "Panic. Instinct. A mistake."
    scene s0h161 with dissolve
    CC "And now you just… live with it."
    CC "Pretending you’re not the reason everything broke."
    scene s0h162 with dissolve
    C "Stop."
    scene s0h163 with dissolve
    CC "..."
    scene s0h164 with dissolve
    CC "Olivia had to grow up overnight."
    CC "Work at fifteen. Carry you through every breakdown."
    scene s0h165 with dissolve
    CC "Remember that?"
    CC "When you couldn’t even eat without falling apart?"
    scene s0h166 with dissolve
    CC "She gave up everything for you."
    scene s0h167 with dissolve
    CC "If it wasn’t for you—"
    CC "she’d have a normal life."
    CC "A future."
    CC "{b}Without you.{/b}"
    scene s0h168 with dissolve
    C "I SAID STOP!"
    scene s0h169 with dissolve
    pause 0.5
    play sounds2 whooshvortex
    scene s0h170 with vpunch
    pause 0.5
    scene s0h171 with dissolve
    C "You don’t get to say her name."
    scene s0h172 with dissolve
    pause 0.5
    scene s0h173 with dissolve
    pause 0.5
    stop music fadeout 2.0

    



    

    
    

label exit:
    scene bb 1 with linearblur 
    pause 3.0
    scene s0l1 with dissolve
    play sounds1 truckclose
    pause 0.5
    scene s0l2 with dissolve
    show trans1 with dissolve
    pause 0.5
    scene s0l4 with dissolve
    show trans2 
    play music lifeis
    h "Barely made it. The hell is with traffic at 5 AM?!"
    hide trans2 with dissolve
    scene s0l6 with dissolve
    h "Private Olivia reporting for duty! Ready to serve!"
    scene s0l7 with dissolve
    mc "Cut the formality. You know I hate that."
    scene s0l8 with dissolve
    h "Phew. I was waiting for you to say that."
    h "So? Anyone else joining, or am I stuck with you?"
    scene s0l9 with dissolve
    mc "No one else."
    mc "No one left."
    scene s0l10 with dissolve
    h "Oh. So just us?"
    h "Well... that’s…"
    scene s0l11 with dissolve
    h "I mean — what a shame."
    scene s0l12 with dissolve
    h "Traveling just the two of us? Risky business."
    scene s0l13 with dissolve
    h "But hey, I’m kind. I’ll tag along."
    scene s0l14 with dissolve
    mc "..."
    scene s0l15 with dissolve
    mc "You comfortable in th—"
    play sounds whoosh
    scene s0l16 with CropMove(time=0.1, mode='slideleft')
    h "We’re not talking about that."
    play sounds whoosh
    scene s0l15 with CropMove(time=0.1, mode='slideright')
    mc "But-"
    play sounds whoosh 
    scene s0l17 with CropMove(time=0.1, mode='slideleft')
    h "Drop it."
    scene s0l18 with dissolve
    mc "If you say so."
    mc "Why are you here?"
    mc "Thought you'd prefer to stay behind."
    scene s0l19 with dissolve
    h "Wow. Didn’t know you had such faith in me."
    h "Want me to turn around? Say the word."
    scene s0l20 with dissolve
    mc "Don’t blame me, remember what you said when we first met?"
    scene s0l21 with dissolve
    h "Told you to get lost?"
    scene s0l20 with dissolve
    mc "No, after tha—"
    A "Promise me something..."
    scene s0l22 with dissolve
    A "Promise me you’ll be back soon."
    scene s0l23 with dissolve
    h "Wait… That's Norman? Don’t tell me we’ve got more company."
    scene s0l24 with dissolve
    mc "No."
    mc "Alexa stays."
    mc "Norman’s with us."
    scene s0l25 with dissolve
    h "..."
    scene s0l26 with dissolve
    h "Absolutely not."
    h "Tell me you're joking."
    mc "I'm not."
    scene s0l27 with dissolve
    h "He trained?"
    mc "No."
    h "Then why the hell is he coming?"
    scene s0l28 with dissolve
    mc "Because he knows a way in."
    mc "A part of the forest Richard's coordinates won't get us through."
    pause 1.1
    mc "Time to move."
    scene s0l29 with dissolve
    A "Take care of yourself, eat properly, and call me if you find a signal, okay?"
    A "Come back quickly... I already miss you."
    scene s0l30 with dissolve
    N "Hey… don’t worry, alright?"
    N "We'll be back before you get tired of missing me."
    N "I love you."
    scene s0l31 with dissolve
    N "Take care of yourself while I’m gone, okay?"
    scene s0l32 with dissolve
    mc "Norman. Time to go."
    scene s0l33 with dissolve
    N "And when I get back… we’ll talk about that, yeah?"
    N "About… another baby."
    N "I love you."
    scene s0l34 with dissolve
    A "I’ll be waiting. I love you too."
    scene s0l35 with dissolve
    b "..."
    scene s0l36 with dissolve
    mc "Don’t worry — I’ll make sure he comes back safe and sound."
    scene s0l38 with dissolve
    A "Returning him to you... just for a while."
    scene s0l39 with dissolve
    mc "Alright, team — are we ready? Did we forget anything?"
    scene s0l40 with dissolve
    pause 0.5
    scene s0l41 with dissolve
    h "Gear’s on me."
    scene s0l42 with dissolve
    mc "Norman?"
    scene s0l43 with dissolve
    N "Yeah. I’m good."
    scene s0l48 with dissolve
    N "So… who’s she, exactly?"
    scene s0l44 with dissolve
    mc "Wait — you two haven’t met?"
    scene s0l48 with dissolve
    N "Nope. Why would I?"
    scene s0l49 with dissolve
    h "Good question. I was about to ask the same."
    scene s0l45 with dissolve
    pause 0.5
    scene s0l46 with dissolve
    play sound carenginestart
    mc "Well then, introductions are in order."
    scene s0l47 with dissolve
    play sounds1 carengine2 loop
    mc "Olivia, this is Norman — my son."
    scene s0l50 with dissolve
    mc "Not by blood…"
    mc "But it never mattered."
    scene s0l51 with dissolve
    mc "He’s as much a son to me as anyone could ever be."
    scene s0l52 with dissolve
    mc "Lora and I… couldn’t have kids."
    mc "So we adopted."
    mc "Best decision we made."
    scene s0l120 with dissolve
    N "Hey, come on, I wasn’t that bad."
    N "Alright… maybe a little."
    mc "I didn’t say that."
    N "I know."
    N "I just... back then, I couldn’t believe someone actually wanted me."
    scene s0l53 with dissolve
    h "Oh... so what, that makes you my little brother now?"
    N "Wait, what?"
    h "Your father… and Lora…"
    h "They kinda became family for us."
    h "Long story."
    pause 1.1
    h "We go way back. Before the army, before all that mess…"
    stop sounds1 fadeout 1.0
    stop music
    scene bb 1 with linearblur 
    pause 2.0
    play music throwback fadeout 1.0
    scene s0l55 with linearblur
    show 3yr with dissolve
    pause 1.0
    scene s0l55 with dissolve
    h "(Funny thing is… I remember that day way too well.)"
    scene s0l56 with dissolve
    h "(Rain was pouring like the city was trying to drown itself.)"
    scene s0l57 with dissolve
    h "(I was freezing under some rusty shelter. Broke. Soaked. Hungry as hell.)"
    scene s0l58 with dissolve
    h "(All I wanted was a job. Anything.)"
    h "(Help mom… maybe get Anya out of that life.)"
    play sounds punch1
    scene s0l59 with dissolve
    pause 0.5
    scene s0l60 with dissolve
    pause 0.5
    play sounds1 cartondrop
    scene s0l61 with dissolve
    pause 0.5
    play sounds2 concstep1
    scene s0l63 with dissolve
    h "(Yeah… turns out life doesn’t give a damn what you want.)"
    scene s0l64 with dissolve
    h "(I learned that early.)"
    play sounds2 mmove
    play sounds1 sitonfloor
    scene s0l65 with dissolve
    h "(Another “no”. Another door slammed in my face.)"
    h "(And that was it. I just… dropped.)"
    scene s0l66 with dissolve
    h "(Angry. Lost. Ashamed.)"
    h "(At the world… and mostly at myself.)"
    scene s0l67 with dissolve
    h "Well? This it, Olivia?"
    h "This what a loser looks like?"
    scene s0l71 with dissolve
    pause 0.5
    scene s0l69 with dissolve
    h "(Pathetic…)"
    scene s0l70 with dissolve
    h "Can’t even get a damn waitress job without a diploma?"
    h "Seriously?!"
    pause 1.1
    h "What now?"
    h "How the hell am I supposed to face mom… Anya…"
    scene s0l72 with dissolve
    h "I really thought this time was different…"
    play sounds2 mmove
    scene s0l73 with dissolve
    h "(Yeah… I was done. Completely.)"
    h "(Like something inside just snapped.)"
    scene s0l77 with dissolve
    h "(And then… this guy just sits next to me.)"
    h "(Your dad. Didn’t say a word at first.)"
    scene s0l75 with dissolve
    h "Get lost."
    scene s0l76 with dissolve
    h "Please..."
    scene s0l77 with dissolve
    h "..."
    h "(Yeah, I know. Rude.)"
    h "(But trust me, you’d be worse in my place.)"
    scene s0l78 with dissolve
    mc "..."
    scene s0l79 with dissolve
    mc "Sometimes… it’s easier to talk to a stranger."
    mc "Might sound crazy. But for some? It’s salvation."
    scene s0l80 with dissolve
    h "..."
    scene s0l79 with dissolve
    mc "Or if not — just let me sit here with you. Until the rain stops."
    mc "Lora says I do this too often."
    scene s0l81 with dissolve
    h "..."
    h "...Who's Lora?"
    mc "Someone who'd probably bring you soup and lecture me for leaving you in the rain."
    scene s0l82 with dissolve
    pause 0.5
    scene s0l83 with dissolve
    h "...Thanks."
    stop music fadeout 2.0
    #music here
    play sound driving loop
    scene s0l54 with dissolve
    h "Honestly? He looked like trouble."
    h "But back then, I didn’t care."
    h "Trouble beats starving."
    h "Funny thing is… that moment?"
    h "Yeah. That one changed everything."
    scene s0l121 with dissolve
    mc "Yeah, well... couldn’t just walk past someone like that. Would’ve haunted me."
    mc "That’s how it started." 
    mc "Kinda messy, but... good stories usually are, right?"
    scene s0l54 with dissolve
    h "Yeah. Brought back some memories."
    scene black with dissolve 
    pause 2.1
    play sounds2 carengine3 loop
    scene s0l84 with dissolve
    show 7yr with dissolve
    h "..."
    scene s0l85 with dissolve
    mc "(humming)"
    scene s0l86 with dissolve
    mc "(low humming)"
    scene s0l87 with dissolve
    pause 1.5
    scene s0l88 with dissolve
    pause 1.5
    scene s0l89 with dissolve
    h "Mmm..."
    scene s0l90 with dissolve
    h "What?"
    scene s0l91 with dissolve
    mc "See that car behind us?"
    scene s0l92 with dissolve
    h "Hmm...?"
    mc "Been on us for a while."
    play sounds mmove
    scene s0l93 with dissolve
    h "How long have they been on us?"
    scene s0l91 with dissolve
    mc "Long enough."
    mc "Glove box."
    mc "Take what’s inside."
    scene s0l93 with dissolve
    h "You really stuffed it in there? This far back?"
    scene s0l94 with dissolve
    h "..."
    scene s0l95 with dissolve
    h "...Oh, you’ve gotta be kidding me."
    play sounds rustling2
    scene s0l96 with dissolve
    h "Why the hell is there a suppressor on this thing?"
    scene s0l91 with dissolve
    mc "Because it looked cool. Duh."
    mc "Take it off if you want. No one’s judging."
    play music carbattle
    play sound carenfineacel loop
    scene s0l97 with dissolve
    a "They’re speeding up." 
    a "Can you slow them down?"
    scene s0l98 with dissolve
    aa "Orders were clear, we just watch."
    a "If we don’t do something, we’ll lose the target!"
    a "And if we lose it, Azarkhan will kill us himself!"
    scene s0l99 with dissolve
    aa "Can you at least drive like a nor—"
    play sounds1 pisolsil
    play sounds hdshot
    scene s0l100 with vpunch
    pause 1.0
    scene s0l101 with dissolve
    h "—Got one!"
    mc "Hold on—"
    play sounds drift
    scene s0l104 with dissolve
    aaa "They’re escaping! Why provoke them?!"
    a "Shut it. Plan B — take them out!"
    scene s0l105 with dissolve
    N "What’s happening?!"
    play sounds1 pisolsil
    scene s0l106 with dissolve
    mc "Relax. Just a couple of guys trying to kill us."
    scene s0l107 with dissolve
    h "Hey—!"
    h "You don’t happen to keep anything bigger back there, do you?!"
    play sounds1 cargun
    scene s0l108 with dissolve
    pause 0.5
    play sounds1 pisolsil
    scene s0l109 with dissolve
    h "They’re closing in—!"
    scene s0l110 with dissolve
    mc "Norman, check under the left seat!"
    play sounds1 pisolsil
    scene s0l111 with dissolve
    pause 0.5
    scene s0l112 with dissolve
    N "Is this the 'toy' you meant?"
    scene s0l113 with dissolve
    h "GIVE IT GIVE IT GIVE IT!"
    scene s0l114 with dissolve
    h "...Oh now we’re talking."
    h "Custom M4A1… TacticalGrip rail… suppressor…"
    h "Damn, you’ve been hiding the good stuff."
    play sounds1 cargun
    scene s0l115 with dissolve
    pause 1.0
    play sounds1 deatwishes
    scene s0l116 with dissolve
    h "Come on— just drop already!"
    stop music fadeout 2.0
    play sounds1 carcrashed
    scene s0l117 with dissolve
    h "..."
    scene s0l118 with dissolve
    h "Alright... let's wrap this up."
    scene s0l119 with dissolve
    mc "Nicely done."

    stop music fadeout 0.5
    stop sound fadeout 0.5

    scene bb 1 with dissolve
    pause 3.5
    stop sound
    $ persistent.chapter_act0_scene += 1



label jungle:

    stop music fadeout 0.5
    play sounds1 forestsound1
    play sounds2 carengine2 loop
    scene s0m7 with dissolve
    show 7yr with dissolve
    pause 1.0
    scene s0m8 with dissolve
    mc "Still on us?"
    scene s0m9 with dissolve
    h "We’ve gone pretty far."
    h "If someone was still on us, we’d know by now."
    scene s0m10 with dissolve
    h "But here’s what bugs me…"
    h "They were watching us."
    h "Then one idiot panicked and turned it into a firefight."
    h "Why?"
    scene s0m11 with dissolve
    mc "Because we got too close."
    mc "Or because they couldn't afford to lose us."
    h "...Yeah. Thought so."
    scene s0m12 with dissolve
    N "You know who it was, Dad?"
    scene s0m13 with dissolve
    mc "Azarkhan’s people."
    mc "Too familiar."
    pause 1.1
    mc "But Olivia's right."
    mc "That wasn't a clean hit."
    mc "That was surveillance gone bad."
    scene s0m14 with dissolve
    h "Seriously though…"
    h "What kind of world is this now?"
    h "Dead men just… getting back up like nothing happened?"
    scene s0m15 with dissolve
    h "First Azarkhan."
    h "Now his crew, all supposedly dead, and yet here they are."
    h "What’s next, huh?"
    h "Ghosts with guns?"
    scene s0m16 with dissolve
    mc "You said you needed a break."
    mc "This is it."
    scene s0m17 with dissolve
    h "Oh yeah. Amazing."
    h "Exactly the kind of vacation I was dreaming about."
    scene s0m18 with dissolve
    mc "Come on, don’t be mad. After this trip, I promise I’ll make it up to you — big time."
    scene s0m19 with dissolve
    h "Well, no one forced you to speak up."
    scene s0m18 with dissolve
    mc "Norman. Map."
    scene s0m19 with dissolve
    N "Hold on, Dad, I need to lock in our position."
    N "…and let them know we’re almost there."
    mc "Who?"
    scene s0m7 with dissolve
    N "My supervisor."
    N "Shiya Gray."
    scene s0m9 with dissolve
    h "Wait."
    h "Gray?"
    scene s0m11 with dissolve
    mc "Richard's daughter."
    N "...You know her?"
    mc "Long story."
    play sounds mmove
    scene s0m20 with dissolve
    N "Take the first left up ahead."
    scene s0m21 with dissolve
    N "If the map's correct, that’s our fastest route."
    scene s0m22 with dissolve
    N "Give it about an hour, we should be there."
    
    scene bb 1 with dissolve
    stop sounds2 fadeout 3.3
    pause 3.5
    stop sounds1

    scene s0m1 with dissolve
    show pl1 with dissolve
    play sound jungle loop
    play sounds1 carengine2 loop fadein 3.3
    mc "That’s as far as we go."
    mc "From here on, we walk."
    mc "Norman, how far to the lab?"
    show s0m67 with dissolve
    pause 1.1
    mc "Norman?"
    scene s0m66 with dissolve
    N "We’ve got a problem, Dad. GPS is dead."
    N "Something’s jamming the signal."
    show s0m67 with dissolve
    mc "How bad?"
    show s0m68 with dissolve
    N "Not ideal… but not critical."
    N "We need open ground, once we’ve got that, I can navigate off the map."
    show s0m69 with dissolve
    h "Wait, hold on—"
    h "Are you telling me we’re lost?"
    mc "Plans changed."
    mc "Had to make sure we weren’t being followed."
    h "Oh, great. Fantastic."
    h "So you {b}do{/b} know where we’re going… right?"
    mc "..."
    play sounds1 stopengine
    show s0m71 with dissolve
    N "We’re not lost. Dad logged the coordinates."
    N "This just makes things… a bit messier."
    show s0m4 with dissolve
    h "No, no... hang on."
    h "I wasn’t asking you."
    h "[mc]."
    h "Two things."
    h "Target."
    h "And motive."
    show s0m73 with dissolve
    mc "I gave you a reason back at the bar."
    show s0m72 with dissolve
    h "Let me paint you a picture."
    h "You’re in your bar."
    h "Someone walks in."
    h "Haven’t seen them in eight years."
    h "And suddenly they’re asking for help."
    h "I’m not asking for much."
    h "Just don’t lie to me."
    scene s0m3 with dissolve
    mc "You really want to hear it?"
    scene s0m4 with dissolve
    h "I’m already here."
    h "Bit late to hesitate now."
    show s0m75 with dissolve
    pause 1.1
    show s0m76 with dissolve
    pause 1.1 
    show s0m70 with dissolve
    mc "Alright… simple version."
    pause 1.9
    mc "Teleportation."
    pause 2.1
    h "...You’ve gotta be kidding me."
    h "Or what, you finally lost your mind?"
    mc "..."
    scene s0m77 with dissolve
    pause 0.5
    play sounds1 cardoor
    show s0m78 with dissolve
    mc "Even with the facts…"
    mc "I’m still not sure I believe it myself."
    scene s0m77 with dissolve
    h "You know what? Fine."
    h "Don’t wanna talk? Don’t."
    h "(muttering) Figures… only known each other, what, twenty-five years…"
    scene s0m5 with dissolve
    pause 1.1
    show s0m6 with dissolve
    mc "Olivia."
    mc "If I’m wrong about this…"
    mc "You get a wish."
    show s0m23 with dissolve
    h "Another one?"
    h "Wow. You’re really feeling generous today."
    show s0m24 with dissolve
    h "Relax. I walked into this myself."
    h "And…"
    h "Yeah, this place is kinda beautiful."
    h "You look at those trees and almost forget—"
    h "That forty minutes ago, some psychos were trying to kill us."
    show s0m25 with dissolve
    mc "Didn’t take you for the nature type."
    show s0m26 with dissolve
    h "Excuse me?"
    h "You got a problem with that?"
    show s0m27 with dissolve
    mc "You’re different when you look at this stuff."
    mc "In a good way."
    show s0m28 with dissolve
    h "..."
    h "Wow."
    h "And what did I do to earn that, huh?"
    h "...Thanks."
    pause 1.1
    mc "Norman. Status."

    show s0m29 with dissolve
    N "No luck reaching my handler."
    show s0m30 with dissolve
    N "I’ve tried, no response."
    show s0m31 with dissolve
    mc "Before she disappeared… your mother made a few calls from work."
    mc "Didn’t know the details."
    mc "But the signal was the same."
    mc "Dead."
    mc "(Same silence as Al-Zahira.)"
    scene s0m32 with dissolve
    N "Yeah… but we thought we fixed that."
    show s0m33 with dissolve
    mc "Guess not."
    mc "Norman?"
    show s0m34 with dissolve
    mc "Catch."
    play sounds1 mmove
    show s0m35 with dissolve
    N "…What’s this?"
    show s0m36 with dissolve
    mc "Your protection."
    mc "And a promise I made to Alexa."
    mc "Now go get changed."
    scene s0m35 with dissolve
    N "But the signal—"
    mc "Take a breather."
    mc "You’re wound too tight."
    N "…Alright."
    play sounds1 akreload
    show s0m38 with dissolve
    pause 0.5
    show s0m39 with dissolve
    mc "What do you think of him?"
    play sounds2 mmove
    show s0m40 with dissolve
    h "If things go loud?"
    h "He would be the first one to die"
    show s0m41 with dissolve
    h "Why’d you even bring him?"
    show s0m42 with dissolve
    mc "Because the coordinates only get us close."
    mc "Norman knows the rest."
    mc "And yes, I tried to talk him out of it."
    mc "Didn't work."
    show s0m43 with dissolve
    h "..."
    show s0m44 with dissolve
    h "Figures."
    h "Stubborn, just like you, huh?"
    h "Still… if he stays in the back he might actually make it."
    play sounds1 mmove
    show s0m45 with dissolve
    N "Bit oversized… but yeah, solid."
    N "Feels reliable."
    show s0m46 with dissolve
    h "Hey, kid."
    h "That vest? Doesn’t make you bulletproof."
    h "Shots fired? You hit the ground and stay there."
    h "Don’t be dead weight."
    scene s0m45 with dissolve
    N "…Got it."

    show s0m47 with dissolve
    mc "We’ll need him."
    show s0m48 with dissolve
    h "Oh yeah?"
    h "And when exactly is that supposed to be?"
    show s0m49 with dissolve 
    mc "He’s the only one who can get us in."
    mc "He knows the old service route."
    mc "The one Lora used."
    show s0m52 with dissolve
    N "I’m not much of a fighter, I’ll admit that."
    show s0m53 with dissolve
    N "But you’re gonna need me once we reach that lab."
    show s0m54 with dissolve
    h "Hold up—"
    h "What lab?"
    mc "According to Norman… there’s a lab at the center."
    show s0m48 with dissolve 
    h "..."
    play sounds1 mmove
    show s0m50 with dissolve
    h "And what’s the plan with it?"
    show s0m51 with dissolve
    N "…She’s got a point."
    show s0m55 with dissolve
    mc "..."
    scene s0m57 with dissolve
    mc "We don’t have a choice."
    mc "Right now… it’s just dead weight."
    show s0m58 with dissolve
    h "Heh…"
    h "Same old you."
    h "Glad nothing’s changed."
    play sounds1 foreststep
    show s0m59 with dissolve
    h "Hey, Norman… mind if I ask something?"
    N "Go ahead."
    show s0m60 with dissolve
    h "How did you meet your wife?"
    N "…That’s a long story."
    N "Feels like a different life."
    show s0m61 with dissolve
    h "We’ve got a long walk anyway."
    show s0m62 with dissolve
    h "Hey, are you not curious about your son’s love life?"
    show s0m63 with dissolve
    mc "I’m coming."
    show s0m64 with dissolve
    h "Go on, Norman."
    h "We’ve got time."
    N "Back in the day, back when dinosaurs still roamed the earth, I was a broke university student."
    N "Spent more time with books than people."
    stop music fadeout 3.2
    N "Didn’t think anyone would even notice me."
    N "Least of all her."
    stop music fadeout 1
    stop sound fadeout 3.2 
    stop sounds1 fadeout 3.2
    scene s0m65 with dissolve

    a "{font=Cybertron.otf}Yes, they’re heading toward the target. I’ll continue to monitor them."

    scene bb 1 with dissolve  
    pause 1.5
    stop sound
    play music villian fadein 5.5
    scene bb 1 with dissolve 
    
    image car = Movie(channel="movie_dp", loop = False, play="video/car.webm")
    show car with dissolve
    $ renpy.pause(3.4, hard=True)

    scene vil 1 with dissolve
    show 4yr with dissolve
    play sound cardooropen
    ggg "..."
    scene vil 2 with dissolve
    play sound cardooropen
    ggg "..."
    scene vil 3 with dissolve
    pause 0.5
    scene vil 4 with dissolve
    pause 1.5
    scene vil 5 with dissolve
    gggg "..."
    scene vil 7 with dissolve
    ggg "Oh, come on. It’s not {b}that{/b} dramatic."
    scene vil 8 with dissolve
    ggg "Still, I didn’t think we’d be the ones cleaning up their mess."
    scene vil 9 with dissolve
    ggg "But hey, if the roles were reversed, you know they’d do the same."
    scene vil 6 with dissolve
    gggg "..."
    scene vil 10 with dissolve
    g "Huh, you’re still breathing? Gotta say, I didn’t expect that. No hard feelings, though."
    scene vil 11 with dissolve
    pause 1.0
    scene vil 12 with dissolve
    pause 1.0
    stop music fadeout 3.0
    play sound fire fadein 2.0  loop
    scene bb 1
    pause 1.0
    scene vil 14
    pause 1.0
    scene vil 15 with dissolve
    pause 1.0
    scene vil 16 with dissolve
    g "Burns nicely, doesn’t it?"
    scene vil 17 with dissolve
    play sounds1 radio loop
    aaaa "..."
    scene vil 17 with dissolve
    aaaa "Yes. Everything’s been taken care of. No loose ends."
    scene vil 17 with dissolve
    aaaa "..."
    scene vil 17 with dissolve
    aaaa "Understood. We’ll stay on them."
    scene vil 19 with dissolve
    s "Remember — eyes only. No contact. No interference. Out."
    window hide
    stop sounds1
    stop sound
    play music villian1 fadein 5.5
    image Final = Movie(channel="movie_dp", loop = False, play="video/Final.webm")
    show Final 
    $ renpy.pause(26.1, hard=True)

    play sound helicopter fadein 3.3
    scene vil 20 with dissolve
    pause 1.0
    scene vil 21 with dissolve
    pause 1.0
    scene vil 22 with dissolve
    pause 1.0
    window auto
    scene vil 23 with dissolve
    az "Been a while, darling. Miss me?"
    scene vil 24 with dissolve
    s "Still better than being you..."
    scene vil 25 with dissolve
    s "Father."
    stop music fadeout 3.0
    stop sound fadeout 3.0
    stop sounds1 fadeout 3.0

    scene bb 1 with Dissolve(2.0)
    pause 1.0
    scene bb 1
    pause 2.0

label junglenext:

    
    scene s0m79 with dissolve
    play sound jungle loop fadein 3.0
    play music nextjg1 fadein 3.0
    play sounds1 foreststep
    pause 1.8
    scene s0m80 with dissolve
    h "Hey… [mc]."
    h "Why now?"
    h "After all this time… why go back?"
    mc "Because this time there was proof."
    mc "And because if I ignored it..."
    mc "I'd spend whatever's left of my life wondering."
    scene s0m81 with dissolve
    h "If I were you… I wouldn’t let it get to my head like that."
    mc "Heh."
    h "No, I mean it, [mc]. Serious."
    h "I get it."
    h "Lora meant everything to you."
    h "But it’s been too long."
    scene s0m82 with dissolve
    pause 1.5
    scene s0m83 with dissolve
    h "I’m all for digging up the truth."
    h "But if this goes sideways…"
    h "(quietly) I don’t wanna see you like you were before."
    scene s0m84 with dissolve
    mc "You won’t."
    mc "That version of me is gone."
    scene s0m85 with dissolve
    mc "…Norman."
    mc "How far?"
    scene s0m86 with dissolve
    N "..."
    N "...Dad?"
    mc "Norman?"
    N "According to the coordinates… we’re there, but—"
    scene s0m87 with dissolve
    N "The lab should be just past those cliffs."
    N "I don’t get it…"
    scene s0m88 with dissolve
    N "The coordinates are precise…"
    pause 0.5
    N "But there’s nothing here."
    scene s0m89 with dissolve
    b "..."
    play sounds1 rustle
    stop music fadeout 2.0
    scene s0m90 with dissolve
    mc "Don’t move."
    scene s0m92 with dissolve
    S "After all this time… and {b}this{/b} is how you say hello?"
    $ Shiya_path = True
    $ unlock_shiya = 1
    scene s0m90 with dissolve
    mc "Still hiding in bushes, huh?"
    mc "Some things don’t change."
    scene s0m93 with dissolve
    S "Guilty as charged. Old habits."
    S "Still… it’s good to see you again."
    S "Now, mind lowering the guns? We’re not enemies."
    play sounds1 mmove
    scene s0m91 with dissolve
    mc "Hope so."
    mc "Fifteen years."
    mc "A lot can change."
    play sounds1 clothess
    scene s0m94 with dissolve
    N "Let me introduce you, Shiya Gray."
    N "Senior Sergeant. And… my handler."
    scene s0m91 with dissolve
    mc "...Handler?"
    scene s0m95 with dissolve
    S "Yeah. That’s me."
    mc "You were using my son."
    S "I was keeping him alive."
    S "And before you ask, yes, he was necessary."
    S "The coordinates only bring people close."
    S "Without Norman's memory of the old service route, you'd still be walking in circles."
    pause 1.1
    S "Oh, right..."
    S "Hello, Commander… or should I say {b}former{/b} Commander."
    play sounds2 hug2
    scene s0m96 with dissolve
    h "...You really haven’t changed."
    scene s0m97 with dissolve
    S "Olivia. It’s really good to see you again."
    scene s0m98 with dissolve
    S "Heard you took Alexandro in."
    scene s0m99 with dissolve
    h "Yeah. Someone had to."
    play sounds1 mmove
    play sounds2 concstep1
    scene s0m100 with dissolve
    mc "And Richard?"
    mc "Still messing with his inventions?"
    scene s0m101 with dissolve
    S "Father? Lost his mind in his old age, but the army still respects him. So they let his quirks slide."
    scene s0m102 with dissolve
    h "Sounds like him."
    h "Good to know he’s still kicking."
    scene s0m101 with dissolve
    S "Honestly… when my father asked me to pass that letter on,"
    S "I didn’t think it would actually work."
    S "Nice to see I was wrong."
    scene s0m103 with dissolve
    S "But... What took you so long?"
    S "I was starting to think you’d bailed."
    scene s0m105 with dissolve
    N "We were attacked."
    scene s0m106 with dissolve
    S "Attacked? By who?"
    play sounds1 mmove
    scene s0m108 with dissolve
    mc "Azarkhan’s people."
    mc "No confirmation… but it fits."
    mc "Question is how does it tie back to this place?"
    scene s0m109 with dissolve
    S "..."
    scene s0m110 with dissolve
    S "(Whispering) So they finally pointed you at the ship."
    scene s0m111 with dissolve
    S "Alright. Come with me. It’s time you saw it for yourselves."
    S "I could explain it."
    S "But it won’t make sense until you see it."
    play sounds1 mmove
    play sounds2 concstep1
    scene s0m112 with dissolve
    N "Understood, ma—"
    S "Don’t call me ma’am. I’m not that old, Norman."
    scene s0m113 with dissolve
    b "..."
    stop music fadeout 2.0
    stop sound fadeout 4.4
    stop sounds1 fadeout 4.4
    $ persistent.chapter_act0_scene += 1

label spaceship:
    stop music fadeout 0.5
    scene bb 1 with Dissolve(2.0)
    pause 1.0
    play sound nightforest loop fadein 1.0 volume 0.1
    scene s0p2 with dissolve
    play music spaceship fadein 3.0
    S "Friendly advice, Commander, whatever you’re about to see, don’t freak out."
    S "It’ll help you keep your sanity a little longer."
    scene s0p2 with dissolve
    S "Now… look over there."
    scene s0p3 with dissolve 
    S "I didn’t believe it either."
    S "First time I saw it."
    pause 2.1 
    mc "(...what the hell is that?)"
    S "That thing crashed here thousands of years ago."
    scene s0p4 with dissolve
    S "It’s the source of every anomaly in this area."
    scene s0p5 with dissolve
    h "...That’s one hell of a leap."
    h "From {b}Lora went missing{/b} to {b}alien spaceship.{/b}"
    scene s0p7 with dissolve
    h "Or is it just me?"
    h "Am I the only one seeing how insane this sounds?"
    scene s0p8 with dissolve
    mc "Doesn’t show… but yeah. Same here."
    scene s0p9 with dissolve
    mc "Part of me still thinks this is a joke."
    scene s0p10 with dissolve
    h "How does that even make sense?"
    h "I thought we were alone out here."
    h "And now what, we’ve got uninvited guests from space?"
    h "Great. Love that for us."
    scene s0p11 with dissolve
    mc "(So Norman and Richard weren’t lying…)"
    scene s0p12 with dissolve
    mc "(Lora… what the hell did you get yourself into?)"
    stop music fadeout 2.8
    scene s0p13 with dissolve
    mc "So how does that thing tie to Lora?"
    scene s0p14 with dissolve
    play music bref fadein 8 volume 0.4
    ri "That’s exactly what we’re trying to figure out."
    scene s0p15 with dissolve
    ri "Three years ago, we found the ship itself."
    ri "Before that, all we had was the old facility above it."
    ri "We thought the lab was the source."
    ri "We were wrong."
    ri "The lab was built around this."
    ri "But the part about you came later."
    ri "Much later."
    ri "The ship ignored us for years."
    ri "Only recently did we connect its reaction to what got into your blood in Al-Zahira."
    scene s0p16 with dissolve
    ri "Still… I’m glad you came."
    scene s0p17 with dissolve
    mc "Let’s just say I didn’t have a reason to say no."
    mc "But one thing still bugs me."
    mc "Why me?"
    scene s0p18 with dissolve
    mc "You’ve got better people."
    mc "More experienced."
    mc "So why me?"
    scene s0p19 with dissolve
    ri "Because you’re the only person still alive who might know anything about this."
    mc "I'm not seeing the connection."
    scene s0p20 with dissolve
    ri "Al-Zahira. Twenty years ago."
    ri "The bastards who betrayed us were recently found dead in this forest."
    ri "And on one of their bodies, we found a photograph of your missing wife."
    mc "You said you'd taken care of them."
    ri "I thought I had."
    ri "Turns out I missed a few."
    scene s0p21 with dissolve
    mc "...Someone was watching us."
    ri "Which means we’re not the only ones looking for you."
    mc "You still haven't answered my question, Richard."
    mc "I want the truth."
    ri "..."
    ri "After the explosion in Al-Zahira, traces of that substance entered your bloodstream."
    ri "And as we recently discovered..."
    ri "The ship reacts to it."
    scene s0p22 with dissolve
    h "So you dragged them here because the alien coffin blinked at his blood?"
    scene s0p23 with dissolve
    ri "Do you know anyone else it reacts to?"
    ri "Because I don’t."
    ri "Either way..."
    ri "Look here. We found this... inside."
    pause 0.5
    scene s0p71 with dissolve
    mc "...That’s not human."
    h "Yeah… that checks out."
    scene s0p25 with dissolve
    h "Nope."
    h "No way I’m going in there."
    h "Not happening."
    scene s0p24 with dissolve
    mc "No way around it?"
    scene s0p26 with dissolve
    ri "Daughter, your thoughts?"
    scene s0p27 with dissolve
    S "No. We’ve checked the entire perimeter."
    S "No other entrances."
    S "We even tried making one, wasted ammo. Nothing worked."
    scene s0p29 with dissolve
    h "You’re seriously asking us to walk into that?"
    h "That’s not a mission."
    h "That’s a death sentence."
    scene s0p31 with dissolve
    mc "She’s right."
    mc "Right now this sounds like suicide."
    scene s0p28 with dissolve
    S "Everyone else said the same."
    scene s0p29 with dissolve
    h "And honestly?"
    h "Can you blame them?"
    h "Who the hell would sign up for that?"
    scene s0p30 with dissolve
    mc "If Lora went in there..."
    mc "We don't have a better option."
    mc "Getting past those sentries won’t be easy."
    scene s0p31 with dissolve
    mc "How many people are going in with us?"
    scene s0p32 with dissolve
    N "Excuse me, but have you tried going through those huge turbines?"
    scene s0p33 with dissolve
    N "They look big enough for a person to fit through."
    scene s0p34 with dissolve
    N "I know it sounds insane — but if there's no other way, maybe it’s worth a shot."
    scene s0p36 with dissolve
    N "..."
    N "It’s a long shot... but it’s something."
    scene s0p37 with dissolve
    S "Actually... maybe it's not so dumb."
    scene s0p38 with dissolve
    b "..."
    scene s0p39 with dissolve
    h "Okay."
    h "I hate it."
    h "But it’s better than walking through the front door."
    scene s0p40 with dissolve
    mc "..."
    mc "Richard? What about the others?"
    mc "Or... am I going in alone?"
    ri "Shiya and I are coming with you. If we can get inside..."
    mc "All right."

    stop music fadeout 4.0
    scene bb 1 with dissolve 
    pause 3.0
    scene s0p42 with dissolve
    mc "..."
    scene s0p43 with dissolve
    N "Up close… it’s even bigger than I thought."
    N "So how are we getting into those turbines?"
    scene s0p44 with dissolve
    ri "We’ll get a ladder."
    ri "After that… we improvise."
    scene s0p45 with dissolve
    h "Gotta admit…"
    h "Kid’s got a brain."
    scene s0p46 with dissolve
    h "But you—"
    h "you did it again."
    pause 0.7
    h "That look."
    h "Means you’re already halfway lost in your own head."
    scene s0ppp46 with dissolve
    mc "..."
    scene s0p46 with dissolve
    h "Remember?"
    h "Talking your head off to some random stranger…"
    h "Helped back then."
    scene s0p47 with dissolve
    mc "..."
    play music undertow fadein 5.5
    scene s0p48 with dissolve
    mc "Something’s off."
    mc "Tell me, Olivia… you believe in fate?"
    scene s0ppp47 with dissolve
    h "After the way we met?"
    h "Yeah… I’d say I do."
    scene s0p47 with dissolve
    mc "..."
    scene s0p48 with dissolve
    mc "What are the odds…"
    mc "that out of every planet, this thing crashes on Earth?"
    mc "That twenty years ago, we stumbled into a deal for something that came from this place?"
    scene s0p49 with dissolve
    mc "Out of all the missing people…"
    mc "the only thing that turns up is Lora's photo."
    mc "On men who should've died twenty years ago."

    mc "Then Norman shows up."
    mc "With a letter."

    scene s0l122 with dreamyzoom 
    show memoryframe with dissolve 
    ri "...he’s backed by powerful entities."
    ri "Possibly... extraterrestrial."
    scene ch 175 with dreamyzoom 
    show memoryframe with dissolve 
    N "It wasn’t my choice… I was led there."
    N "A man… wearing a black mask."
    scene s0p15 with dreamyzoom
    show memoryframe with dissolve 
    ri "Three years ago, we found this place."
    ri "Or rather… it let us find it."
    ri "Before that, we only knew about the old facility above it."
    ri "The ship itself stayed buried. Hidden under our noses."

    
    scene s0p49 with dreamyzoom 
    pause 1.5
    mc "Next day, Azarkhan’s people try to kill us."
    pause 0.5
    mc "And I’m supposed to believe that’s coincidence?"
    h "Huh…"
    scene s0p51 with dissolve
    mc "..."
    scene s0p52 with dissolve
    h "Never really looked at it like that…"
    h "But yeah."
    h "That’s way too many coincidences."
    scene s0p53 with dissolve
    h "Feels like someone’s feeding info."
    h "Or watching us real close."
    scene s0p54 with dissolve
    mc "..."
    scene s0p56 with dissolve
    mc "Stay sharp."
    mc "Anything can happen."
    scene s0p55 with dissolve
    h "I’ll try reaching Anya."
    h "There’s gotta be something here that actually works…"
    scene s0p57 with dissolve
    ri "So? Any luck?"
    scene s0p58 with dissolve
    N "Yeah, I found something."
    N "There’s a narrow passage."
    scene s0p59 with dissolve
    N "Go get Dad, I’ll need him for this."
    stop music fadeout 1.0
    scene bb 1 with linearblur 
    pause 1.5
    stop sound
    $ persistent.chapter_act0_scene += 1



default first_right1 = True
default first_door = True
default first_left_back = True
default first_left_mecha = True
default second_right1 = True
default second_front = True
default second_left_back = True
default second_left_mecha = True
default position = 0


label spaceship_into:
    stop music fadeout 0.4
    play sound spaceshipinto loop volume 0.2 fadein 2.0
    play music dangeom fadein 2.0
    scene s0p60 with dissolve
    N "Alright, if we unscrew these bolts, we can remove—"
    play sounds1 hutchfall volume 0.3
    scene s0p61 with dissolve
    E "..."
    h "Seriously?"
    h "You couldn’t be more careful?"
    mc "Drop it, Olivia."
    mc "Narrow entry."
    mc "Unknown drop."
    mc "If something waits below, better it gets one target than all of us."
    h "I hate when your logic makes sense."
    play sounds1 button
    scene s0p62 with dissolve
    h "You being this calm right now?"
    h "Yeah… that’s not comforting."
    mc "I’m going in first."
    play sounds1 mmove
    play sounds2 landing
    scene s0p63 with vpunch
    show trans4 with dissolve
    mc "Wait…"
    scene s0p64 with dissolve
    pause 0.5
    scene s0p65 with dissolve
    mc "Doesn’t look like anyone’s here."
    scene s0p64 with dissolve
    h "Then I’m coming with you."
    scene s0p66 with dissolve
    mc "Wait."
    mc "I go first."
    play sounds1 mmove
    scene s0p67 with dissolve
    h "No."
    h "Don’t do that."
    pause 0.5
    h "I’m serious."
    h "Don’t go in there alone."
    play sounds1 mmove
    scene s0p68 with dissolve
    mc "I’ll manage."
    scene s0p69 with dissolve
    mc "If I don’t come back…"
    mc "Don’t follow."
    h "...Damn it."
    play sounds1 metalstep
    scene s0p70 with dissolve
    mc "(Left… or right…?)"
    call screen path_first

label path_first_left:
    if position <= 1:
        play sounds1 metalstep
        scene s0q1 with dissolve
        mc "..."
        call screen path_first_left_next

    mc "(Enough.)"
    mc "(No point wandering blind.)"
    mc "(Time to bring the others in.)"
    jump meets11

label path_first_left_next_2:
    if position <= 1:
        $ first_left_back = False
        play sounds1 metalstep
        scene s0q3 with dissolve
        mc "(Too quiet…)"
        mc "(And that smell…)"
        mc "(Like something’s been rotting here for years.)"
        play sounds1 metalstep
        scene s0q4 with dissolve
        mc "..."
        if first_left_mecha == True:
            mc "(…What the hell happened here?)"
            mc "(So that’s the smell…)"
            mc "(Corpses.)"
            $ first_left_mecha = False
            $ position += 1
            jump path_first_left_back

        play sounds1 metalstep    
        scene s0q3 with dissolve
        mc "No."
        mc "Not going in there."


    mc "(Enough.)"
    mc "(No point wandering blind.)"
    mc "(Time to bring the others in.)"
    jump meets11


label path_first_left_back:
    if position <= 1:
        if first_right1:
            if first_left_back == False:
                play sounds1 metalstep
                scene s0q5 with dissolve
                mc "(What was this place…?)"
                mc "(A warship? A lab?)"
                mc "(It’s massive…)"
                mc "(Like a city buried inside a tomb.)"
                play sounds1 metalstep
                scene s0q2 with dissolve
                mc "(Every turn… more corridors.)"
                mc "(Like it was built to trap you.)"
                $ first_left_back = True
                call screen path_first_left_back

            play sounds1 metalstep
            scene s0q2 with dissolve
            mc "(Same question… every time.)"
            call screen path_first_left_back

        
        if first_left_back == False:
            if second_right1 == True:
                $ second_right1 = False
                play sounds1 metalstep
                scene s0q5 with dissolve
                c "(What was this place…?)"
                mc "(A warship? A lab?)"
                mc "(It’s massive…)"
                mc "(Like a city buried inside a tomb.)"
                play sounds1 metalstep
                scene s0q2 with dissolve
                mc "(Every turn… more corridors.)"
                mc "(Like it was built to trap you.)"
                $ first_left_back = True
                call screen path_first_left_back
        
        play sounds1 metalstep    
        scene s0q2 with dissolve
        mc "(Which way…?)"
        
        call screen path_first_left_back
        
    mc "(Enough.)"
    mc "(No point wandering blind.)"
    mc "(Time to bring the others in.)"
    jump meets11

label first_right:
    if position <= 1:
        if first_right1:
            $ first_right1 = False
            play sounds1 metalstep
            scene s0q6 with dissolve
            mc "(Blocked.)"
            mc "(Could climb it…)"
            mc "(Feels like a dead end.)"
            $ position += 1
        
        mc "..."
        play sounds1 metalstep
        scene s0q142 with dissolve
        mc "(Where should I go now?)"
        call screen path_right_back1
    
    mc "(Enough.)"
    mc "(No point wandering blind.)"
    mc "(Time to bring the others in.)"
    jump meets11

label meets11:
    play sounds1 metalstep
    scene s0q7 with dissolve
    mc "You still there?"
    mc "Or did you all leave me already?"   
    scene s0q8 with dissolve
    h "We would—"
    h "but then who’s gonna drag your wrinkly ass out of here?"
    N "We’re not leaving you behind, Dad. Not a chance."
    ri "What’s the situation?"
    scene s0q7 with dissolve
    mc "Bad enough I don’t wanna be here."
    mc "Not bad enough to turn back."
    mc "Found bodies."
    mc "Old. And dead."
    scene s0q8 with dissolve
    h "Move—!"
    play sounds1 mmove
    play sounds2 landing
    scene s0q11 with vpunch
    S "You okay?"
    h "Ow— shit…"
    h "Yeah, I’m fine."
    h "Would’ve been better if someone mentioned the damn drop!"
    scene s0q12 with dissolve
    mc "That used to be nothing for you."
    mc "Getting old?"
    play sounds1 mmove
    scene s0q10 with dissolve
    h "Oh, you wanna test that?"
    h "Say it again."
    scene s0q9 with dissolve
    S "I see you all still get along great, as always."
    play sounds2 mmove
    play sounds1 metalstep
    scene s0q18 with dissolve
    ri "We’re going to inspect this area and see what we can do." 
    scene s0q17 with dissolve
    ri "There has to be a control node somewhere."
    ri "A recorder. A map. Anything that tells us what happened here."
    play sounds1 metalstep
    scene s0q19 with dissolve
    N "I’ll back him up."
    N "Dad… watch yourself, alright?"
    play sounds2 mmove
    scene s0q20 with dissolve
    N "Sir… isn’t it a little too dark in here?"
    ri "You think so too? Let's fix that... Where is it... Oh, found it."
    scene s0q144 with dissolve
    ri "Shine like the sun, my dear."
    play sounds2 button
    scene s0q143 with dissolve
    ri "This must be enough to illuminate all this metallic junk around us." 
    scene s0q22 with dissolve
    h "Hah… they clicked fast."
    h "Kid’s got a talent for bonding with weirdos, I’ll give him that."
    scene s0q23 with dissolve
    h "Alright, enough."
    h "Back to business."
    pause 1.1
    h "We moving, or you planning to stand here all day?"

label front:   
    if second_front == True:
        $ second_front = False
        play sounds1 metalstep
        scene s0q145 with dissolve
        mc "Great plan."
        mc "I’ll just play meat shield, right?"
        h "[mc]…"
        h "You seriously gonna let a fragile, innocent girl walk in front of you?"
        play sounds1 metalstep
        scene s0q146 with dissolve
        mc "Of course not."
        mc "Shame I don’t see any."
        h "Careful there, cowboy."
        h "Might wanna check your ammo first—"
        h "before someone knocks your head clean off."
        if first_door == True:
            call screen path_front_next 

    

label door_space_ship:
    $ first_door = False
    play sounds1 metalstep
    scene s0q147 with dissolve
    mc "Save it for later."
    mc "Door. Three o’clock."
    scene s0q39 with dissolve
    h "I’ve got a good memory."
    h "Shiya— check it."
    h "See if we can get through."
    play sounds1 metalstep
    scene s0q40 with dissolve
    S "Alright. No promises, but I’ll give it a shot."
    play sounds1 metalstep
    scene s0q41 with dissolve
    h "Let’s hope this doesn’t take forever."
    scene s0q42 with dissolve
    S "Okay... Let’s see what we’re dealing with."
    S "Oh, right... I totally forgot. I can’t do a damn thing here."
    play sounds2 mmove
    scene s0q43 with dissolve
    S "I don’t read alien languages, so hacking it? Not an option."
    mc "Richard said it reacted to me."
    h "Please tell me you're not about to touch the alien door."
    scene sb121r with dissolve
    mc "I'm about to touch the alien door."
    mc "—!"
    h "And nothing."
    S "Reacted doesn't mean obeyed."
    S "If Dad's theory is right, you've got traces in your system."
    S "Enough for the ship to notice you."
    S "Not enough to open every damn lock."
    scene s0q44 with dissolve
    S "So we still need the opener. If luck’s on our side, we can get inside."
    scene s0q45 with dissolve
    mc "And where exactly do I find that?"
    scene s0q44 with dissolve
    S "Alright, alright. I’ll dig around, but don’t expect miracles."
    scene s0q45 with dissolve
    mc "Like I’ve got a choice."
    mc "Let’s hope luck’s on our side."
    play sounds1 metalstep
    scene s0q148 with dissolve
    mc "(A opener… of course.)"
    mc "(Because this place wasn’t annoying enough.)"
    mc "(Where the hell am I supposed to find one?)"
    call screen path_door_back




 
label path_front_next2:
    play sounds1 metalstep
    scene s0q24 with dissolve
    mc "(This place…)"
    mc "(Feels like a damn tomb.)"
    play sounds2 mmove
    scene s0q26 with dissolve
    mc "(Another door…)"
    scene s0q27 with dissolve
    mc "(Locked.)"
    scene s0q26 with dissolve
    mc "(Without a opener, I’m tied up...)"
    scene s0q25 with dissolve
    mc "No choice but to keep moving."
    play sounds2 mmove
    scene s0q29 with dissolve
    mc "..."
    mc "Of course..."
    scene s0q28 with dissolve
    mc "(A corpse.)"
    mc "(And something about this feels wrong.)"
    scene s0q30 with dissolve
    mc "(Maybe it’s nothing…)"
    mc "(Just a body.)"
    play sounds1 metalstep
    scene s0q31 with dissolve
    mc "(Charred… melted into the floor.)"
    mc "(Like it’s part of the ship.)"
    play sounds1 metalstep
    scene s0q32 with dissolve
    mc "(Wait…)"
    mc "(This thing crashed thousands of years ago.)"
    mc "(So why hasn’t it decomposed?)"
    play sounds1 metalstep
    play sounds2 mmove
    scene s0q33 with dissolve
    mc "Doesn’t matter."
    mc "Grab the opener and get out."
    play sounds3 metalstep
    play sounds2 mmove
    scene s0q34 with dissolve
    pause 1.5
    play sounds1 zombie volume 2.0
    scene s0q35 with vpunch
    z "AAAAAAAAHHHHHHHHH!" 
    mc "(Don't think.)"
    mc "(Shoot.)"
    play sounds1 gunm4
    play sounds2 headshotzombie
    scene s0q36 with vpunch
    mc "..." 
    play sounds2 fall
    scene s0q37 with dissolve
    mc "You done screaming?"
    play sounds2 mmove
    scene s0q38 with dissolve
    mc "Time to go."

define persistent.energy_c = False

label shoot:

    
    scene s0q149 with dissolve
    mc "(Did I imagine it, or did that corpse just... come back to life?)"
    mc "Wait…"
    scene s0q150 with dissolve
    mc "That door…"
    mc "It was locked." 
    mc "(The Opener... Did it cause this?)"
    play sounds2 button
    scene s0q151 with dissolve
    mc "..."
    mc "(Don’t do anything stupid…)"
    mc "(Just go back.)"
    mc "(I need to warn the others.)"
    scene s0q149 with dissolve
    mc "..."
    scene s0q151 with dissolve
    mc "(If I call them, they'll come. No questions asked.)"
    mc "(But what if it's dangerous?)"
    mc "(Can't risk their lives... Better I go alone.)"
    scene black with dissolve
    pause 1.0

    play sounds2 mmove
    play sounds3 metalstep
    scene s0q152 with dissolve
    mc "I knew it was big…"
    mc "Not this big."
    scene s0q153 with dissolve
    mc "(That stench...)"
    mc "What is this place?" 
    play sounds2 mmove
    play sounds3 metalstep
    scene s0q160 with dissolve
    mc "Who built this…?"
    mc "What the hell happened here?"
    scene s0q161 with dissolve
    mc "Too many questions…"
    mc "No answers."
    scene s0q162 with dissolve
    mc "..." 
    play sounds3 metalstep
    scene s0q188 with dissolve
    mc "What’s this...?" 
    scene s0q189 with dissolve
    mc "A recorder…?"
    mc "(Looks... human.)"
    mc "(So someone from the old lab made it this far.)"
    play sounds1 button
    play sounds4 radio loop volume 0.3
    play sounds3 metalstep
    scene s0q191 with dissolve
    a "Testing... one, two..."
    a "…Okay. Recording’s on."
    mc "(Heavy distortion.)"
    mc "(Female voice.)"
    mc "(Familiar...?)"
    scene s0q164 with dissolve
    a "Tomorrow’s a big day. They’ve entrusted me with something huge... I have to give it my all."
    scene s0q165 with dissolve
    a "Day 1: I finally get to work on the new project."
    a "…I’ve been waiting for this." 
    play sounds3 metalstep
    scene s0q166 with dissolve
    a "Day 7: I thought I’d record more often, but there’s too much work..."
    a "We stabilized the substance today."
    a "…It’s incredible."
    scene s0q167 with dissolve
    a "Day 13: A breakthrough."
    a "The properties of this substance are…"
    a "…beyond anything I’ve seen."
    mc "(No...)"
    mc "(That cadence.)"
    mc "(I know that voice.)"
    scene s0q168 with dissolve
    pause 0.5
    scene s0q168 with dissolve
    a "Day 22: For some strange reason… the liquid began turning into blood."
    a "…Or something like it."
    a "I don’t like this."
    play sounds2 mmove
    scene s0q168 with dissolve
    a "Day 37: The blood started being absorbed into the device…"
    a "…And I feel it."
    a "Like something’s draining me."
    scene s0q169 with dissolve
    mc "Wait…"

    scene ch 135 with dreamyzoom 
    show memoryframe with dissolve 
    N "It feeds… whatever’s inside."
    scene s0pp86 with dissolve 
    show memoryframe with dissolve 
    pause 1.2
    scene s0pp87 with dissolve 
    show memoryframe with dissolve 
    pause 1.2
    scene s0pp91 with dissolve 
    show memoryframe with dissolve 
    mc "(…Warp drive.)"
    mc "(Norman said that before…)"

    scene s0q169 with dissolve
    mc "(Don’t tell me this is the same thing…)"
    play sounds3 metalstep
    play sounds2 mmove
    scene s0q195 with dissolve
    a "Day 49: Scientists are collapsing from exhaustion."
    a "The ring… doesn’t stop."
    scene s0q196 with dissolve
    a "Day 53: It’s affecting us."
    a "We didn’t anticipate this."
    play sounds3 metalstep
    play sounds2 mmove
    scene s0q156 with dissolve
    mc "Something’s wrong…"
    scene s0q192 with dissolve
    mc "This is…"
    
    $ persistent.energy_c = True

    scene s0q193 with dissolve
    a "Day 61: No, no, no—!"
    a "What have we done…?!"
    a "It’s absorbing human bodies now!"
    a "We have to destroy it, before it’s too late!"
    scene s0q194 with dissolve
    a "Day 62: Everyone’s gone."
    a "…I’m the only one left."
    a "The exit’s sealed."
    a "I tried contacting HQ, nothing."
    scene s0q157 with dissolve
    a "No matter what it takes…"
    a "I have to preserve this."
    a "…I promised."
    scene s0q158 with dissolve
    a "Day 63: I’m… still alive."
    a "Somehow, everything’s back to normal."
    a "The ring stopped absorbing blood."
    a "…Like it had enough."
    a "It runs on it."
    a "Blood is the energy source."
    play sounds3 metalstep
    scene s0q159 with dissolve
    a "Day 64: Something came out of the ring…"
    a "Creatures."
    a "They look… human."
    a "But they’re not."
    a "What the hell is going on…?"

    a "I’m hiding in the lab."
    a "…Please don’t see me."
    a "Note: They speak some kind of language."
    scene s0q170 with dissolve
    a "Oh no…"
    a "They saw me."
    a "Looks like this is it…"
    a "I couldn’t keep my promise…"
    a "I’m sorry."
    a "…I really tried."
    Lor "I’m sorry, [mc]…"
    stop sounds4
    pause 2.1
    mc "Wait…"
    mc "(No.)"
    mc "(Lora?)"
    mc "That was her?"
    mc "But her voice... different?"

    image s0transition3 = Movie(channel="movie_dp", loop = False, play="video/s0transition3.webm")
    show s0transition3
    $ renpy.pause(0.6, hard=True)

    play sounds4 warptravaling fadein 0.6 loop
    scene s0q171 
    mc "What the hell…?"
    mc "What’s happening?"
    aa "{font=Cybertron.otf} You shouldn't be here. Not yet."
    play music naraka
    scene s0q176 with dreamyzoom
    a "..."
    scene s0q179 
    pause 1.5
    scene s0q178 
    pause 1.5
    scene s0q177 
    pause 1.5
    scene s0q172 with vpunch
    mc "AAAAAAAAAAA"
    window hide
    image memory2 = Movie(channel="movie_dp", loop = False, play="video/memory2.webm")
    show memory2 with dreamyzoom
    $ renpy.pause(5.2, hard=True)
    
    scene s0q173 
    mc "No {w=0.4}no {w=0.3}no {w=0.2}no {w=0.1}no..."

    image memory1 = Movie(channel="movie_dp", loop = False, play="video/memory1.webm")
    show memory1 with dreamyzoom
    $ renpy.pause(6.1, hard=True)

    scene s4_5bb10 with dreamyzoom
    pause 2.1

    scene s0q174 with dissolve
    mc "What’s happening to me?!" 
    
    scene s0q184 with dreamyzoom
    pause 1.2
    scene s0q185 with dissolve
    pause 1.2

    
    scene s0q175 with dissolve
    mc "Whose memories… were those?"

    stop sounds4 fadeout 1.0
    play sounds1 hit1 fadeout 0.5
    stop music
    scene bb 1 with vpunch
    pause 2.0
    play sounds4 breath3
    play music general fadein 1.5
    scene s0q186 with dreamyzoom
    mc "What just…"
    mc "I was…"
    play sounds1 metalstep
    scene s0q187 with dissolve
    mc "I need to get out. Now!" 
    play sounds1 metalstep
    scene s0q46 with dissolve
    mc "Everyone okay?"
    mc "We need to leave."
    mc "Now."
    mc "This place…"
    mc "The blood… the ring…"
    mc "It opens something."
    mc "A passage, maybe."
    mc "A portal— I don't know."
    scene s0q47 with dissolve
    h "Hey—"
    h "Slow down."
    h "What are you even saying?"
    h "Talk to me."
    scene s0q48 with dissolve
    mc "Answers…"
    mc "To everything."
    scene s0q47 with dissolve
    h "...Alright."
    h "Start from the beginning."
    scene s0q48 with dissolve
    mc "The door opened…"
    mc "I went in…"
    mc "Lora…"
    mc "She recorded it…"
    scene s0q49 with dissolve
    S "You sure about this? You were gone five minutes. All that happened in five minutes?" 
    scene s0q48 with dissolve
    mc "Wait — what?! No, I was in there much longer... Let me just find the recording—"
    mc "Where is it?!"
    mc "It was in my hand."
    mc "I know it was."
    b "..."
    scene s0q50 with dissolve
    h "You sure this wasn’t all in your head?"
    scene s0q52 with dissolve
    mc "You think I’m lying?"
    scene s0q48 with dissolve
    b "..."
    scene s0q50 with dissolve
    h "Hey— I didn’t say that."
    h "Just trying to figure out what the hell happened to you."
    scene s0q49 with dissolve
    S "Let’s set this aside. Did you find the opener?"
    scene s0q51 with dissolve
    mc "Not sure if this is it…"
    scene s0q53 with dissolve
    pause 0.5
    scene s0q54 with dissolve
    mc "I found it on a corpse…"
    mc "It started screaming."
    scene s0q50 with dissolve
    h "...Okay."
    h "Yeah."
    h "I really don’t like this."
    scene s0q56 with dissolve
    S "What?"
    scene s0q57 with dissolve
    mc "I’m not joking."
    mc "I saw it."
    S "..."
    scene s0q58 with dissolve
    S "You and your jokes, Commander..."
    scene s0q59 with dissolve
    mc "I’m not joking! I saw it!"
    S "Whatever it was, call Dad and Norman over."
    S "I don’t want to stay here another second."
    scene s0q60 with dissolve
    ri "No need, we heard the screaming and came to check on you."
    scene s0q61 with dissolve
    ri "You alright?"
    scene s0q62 with dissolve
    mc "I honestly don’t know anymore..."
    scene s0q61 with dissolve
    ri "Did you learn anything?"
    scene s0q62 with dissolve
    mc "Yeah…"
    mc "They used blood."
    mc "As fuel."
    mc "The team…"
    mc "They’re gone."
    mc "Fed into that thing…"
    mc "A ring…"
    mc "Some kind of portal…"
    pause 0.5
    mc "I think…"
    mc "I don’t even know anymore."
    scene s0q63 with dissolve
    ri "Whatever it was, it explains a lot..."
    ri "Wait — energy?"
    scene s0q64 with dissolve
    ri "Blood…?"
    ri "As fuel…?"
    ri "That matches the readings."
    ri "Not the method. God, not the method..."
    scene s0q65 with dissolve
    S "Please, stop. The more you talk, the worse I feel being here."
    scene s0q66 with dissolve
    S "Save the chatter for later. Focus on what we can deal with."
    stop sounds1 fadeout 5.4
    stop music fadeout 5.4
    stop sound fadeout 5.4
    scene black with dissolve
    pause 2.0
    $ persistent.chapter_act0_scene += 1
    
define persistent.warpdrive_memory = False

label spaceship_door:
    play music1 spscs 
    scene s0q67 with dissolve
    play sound concstep1
    mc "..."
    scene s0q68 with dissolve
    mc "..."
    play sound concstep1
    scene s0q69 with dissolve
    mc "..."
    scene s0q70 with dissolve
    h "Why’d you freeze?"
    h "You see something?"
    scene s0q72 with dissolve
    mc "Yeah."
    mc "Up ahead."
    mc "That thing…"
    mc "We’re not walking into it blind."
    h "Yeah, that’s reason enough to stop."
    h "So what’s the play?"
    mc "Thinking."
    scene s0q71 with dissolve
    mc "We need a way past."
    mc "No noise. No mess."
    scene s0q70 with dissolve
    h "We could try sneaking."
    h "Risky as hell, but doable if we keep it clean."
    scene s0q71 with dissolve
    mc "That’s a gamble."
    mc "If it’s automated — one mistake and we’re dead."
    mc "I need better than ‘maybe’."
    scene s0q73 with dissolve
    S "Why not just blow the damn thing to pieces? One well-placed boom, and we’re golden."
    scene s0q74 with dissolve
    h "Honestly?"
    h "Best idea I’ve heard all day."
    scene s0q75 with dissolve
    mc "Unless you’ve got a warhead in your pocket, we’re outgunned."
    scene s0q76 with dissolve
    S "Relax. I’ve got a little something tucked away for emergencies like this… Hold up…"
    play sound rustle_1 volume 0.3
    scene s0q77 with dissolve
    S "C4."
    S "If we place it right… it’ll take it down."
    scene s0q78 with dissolve
    h "...Okay, that might actually work."
    h "But where the hell did you get that?"
    scene s0q79 with dissolve
    S "That’s not your concern."
    scene s0q80 with dissolve
    h "..."
    scene s0q81 with dissolve
    h "...Right."
    # stop music fadeout 2.0
    # play music sneakysnitch volume 1.0 fadein 3.0
    play sound metalstep volume 0.3
    play sounds1 whoosh
    scene s0q82 with dissolve
    ri "We don’t have much time. I’ll handle it."
    scene s0q83 with dissolve
    S "What are you doing, pa?! That thing could—"
    scene s0q84 with dissolve
    ri "Don’t worry. I’ve dealt with one before, with Norman." 
    ri "It reacts to posture."
    ri "Weapons up threat."
    ri "Hands down passage."
    ri "At least, that's how it worked last time."
    scene s0q85 with dissolve
    ri "As long as we avoid the sensors, we’re good."
    scene s0q87 with dissolve
    h "Yeah, I think we can safely rule out ‘not dangerous’."
    h "Richard’s out there running field tests with his face."
    scene s0q88 with dissolve
    S "Guess we don’t need the C4 after all. Thanks, Dad. Really cleared things up for us."
    play sound metalstep 
    scene s0q89 with dissolve
    S "Hey, Dad? Maybe don’t push any more buttons on that murder machine. Just a thought."
    play sound metalstep 
    scene s0q90 with dissolve
    S "Last thing we need is it waking up in a bad mood."
    play sound metalstep 
    scene s0q91 with dissolve
    ri "You worry too much. Trust me."
    scene s0q92 with dissolve
    ri "I’m sure I’ve got it under control."
    stop music1
    scene s0q93 with dissolve
    play sound mecha1
    l "ACTIVATION INITIATED"
    play sounds1 heartbeat 
    scene s0q94 with dissolve
    ri "..."
    scene s0q95 with dissolve
    E "..."
    play sound rustle_1
    scene s0q96 with dissolve
    E "..."
    scene s0q97 with dissolve
    mc "Richard, what the hell?!"
    scene s0q98 with dissolve
    play music robotic fadein 2.0
    ri "No sudden moves. We’re fine."
    play sound scanningr
    scene s0q99 with dissolve
    ri "Totally fine. Just don’t look threatening."
    play sound scanningr
    scene s0q100 with dissolve
    ri "Everyone — lower your weapons."
    ri "That’s an {b}order{/b}. If we stay calm, so will it."
    play sound scanningr
    scene s0q101 with dissolve
    ri "No harm meant, no harm done. Right, metal friend? We’re just... passing through."
    play sound scanningr
    scene s0q102 with dissolve
    ri "Nice and easy."
    scene s0q103 with dissolve
    ri "That’s it. Lower your guns. Breathe."
    scene s0q104 with dissolve
    mc "You’ve lost your mind."
    mc "That thing’s not friendly."
    scene s0q105 with dissolve
    ri "Yeah, I’ve lost it. Now lower your weapon!"
    mc "..."
    scene s0q106 with dissolve
    ri "...Thanks."
    scene s0q107 with dissolve
    mc "I don’t like this."
    mc "Not even a little."
    scene s0q108 with dissolve
    ri "I’ll listen to your complaints after this."
    

    stop music fadeout 0.5
    play sounds1 access
    scene s0q109 with dissolve
    pause 1.0
    scene s0q110 with dissolve
    play sound breath2
    E "{b}sigh of relief{/b}"
    scene s0q112 with dissolve
    play sound radio loop
    pause 0.5
    scene s0q111 with dissolve
    S "We’re in contact."
    S "(Interference dropped.)"
    S "(Whatever that thing opened, it cleared a channel.)"
    pause 0.5
    r "Commander, do you read me?"
    scene s0q112 with dissolve
    play sound radio loop
    r "We're under attack. Armed hostiles." 
    scene s0q113 with dissolve
    play sounds1 waramb 
    r "Don’t know who, but they're organized, and they’re pushing us back."
    scene spds 91 with dissolve
    r "HQ's dark. Might be jamming — signals are shot to hell. We’re blind out here."
    stop sounds1
    scene s0q113 with dissolve
    ri "Something wrong?"
    stop sound 
    play sound metalrun
    scene s0q114 with dissolve
    S "We under attack!"
    scene s0q115 with dissolve
    ri "Under attack? From who? What the hell’s happening?"
    play sound metalrun
    scene s0q114 with dissolve
    S "No clue. But it’s real. And it’s bad."
    S "We’ll hold them off. You move ahead."
    S "If they reach this corridor, we're trapped."
    S "You keep moving. We'll hold the choke point."
    play sound metalrun
    scene s0q117 with dissolve
    ri "You keep moving, we’ll handle things outside."
    scene s0q116 with dissolve
    h "So what—"
    h "they ditched us, or we ditched them?"
    h "…Eh."
    h "Same difference."
    play sound metalrun
    scene s0q118 with dissolve
    pause 1.0
    play sound jumpstart
    scene s0q119 with dissolve
    pause 1.0
    play sound jumpmecha
    scene s0q120 with dissolve
    pause 1.0
    play sound jumpstart
    scene s0q121 with dissolve
    pause 1.0
    play sound jumpmecha 
    scene s0q122 with dissolve
    stop music fadeout 2.0
    play music decay volume 0.1
    h "...Okay, tell me I’m not seeing things."
    h "That thing just followed them, right?"
    scene s0q123 with dissolve
    mc "You saw it right."
    mc "And it’s with them."
    scene s0q124 with dissolve
    pause 0.5
    scene s0q125 with dissolve
    b "..."
    play sound metalstep volume 0.3
    scene s0q126 with dissolve
    mc "Alright."
    mc "We’re not waiting for the next disaster."
    mc "Move."
    play sound metalstep volume 0.3
    scene s0q127 with dissolve
    h "So what now?"
    h "We just stand here and stare at it until it opens itself?"
    scene s0q128 with dissolve
    mc "Tempting."
    mc "Still gotta open it."
    mc "No shortcuts."
    scene s0q129 with dissolve
    mc "Norman."
    mc "You’ve been quiet."
    mc "You good?"
    scene s0q131 with dissolve
    N "Yeah… I’m good."
    N "Just got this weird feeling... Like I’ve been here before."
    N "Not here exactly."
    N "Just... the sound."
    N "The air."
    N "Like the place Mom took me."
    scene s0q132 with dissolve
    mc "..."
    scene s0q133 with dissolve
    mc "Since when?"
    scene s0q134 with dissolve
    pause 0.2
    scene s0q135 with dissolve
    pause 0.2
    scene s0q131 with dissolve
    N "I don’t know, Dad… I just, can’t place it."
    scene s0q136 with dissolve
    h "Hey, Norman…"
    h "You even know how to shoot?"
    N "Nope."
    h "Then stay behind me."
    h "If things go south— I’ve got you."
    scene s0q137 with dissolve
    mc "Everyone ready?"
    scene s0q138 with dissolve
    h "Oh, I’m ready."
    scene s0q139 with dissolve
    N "I’ll keep up. I won’t slow you down."
    scene s0q140 with dissolve
    mc "Alright."
    mc "Stay sharp."
    mc "Let’s move."
    scene s0b1 with dissolve
    show memoryreboot with dissolve 
    
    $ persistent.warpdrive_memory = True
    $ persistent.chapter_act0_scene += 1




    


label endoftheporolgue:
    play sound closescidoor
    stop music fadeout 2.0
    play sounds1 generator loop volume 0.2
    mc "..."
    scene s0b2 with dissolve
    mc "(…What the hell is that.)"
    mc "...That’s not natural."
    play sound metalstep
    scene s0b4 with dissolve
    h "…Well."
    h "A floating black hole."
    h "Yeah, that wasn’t on my list for today."
    play sounds fall
    scene s0b5 with dissolve
    N "No… that’s not possible."
    N "What is that thing doing here?"
    scene s0b7 with dissolve
    mc "Norman."
    mc "You recognize it?"
    scene s0b6 with dissolve
    N "Dad… that’s what Mom was working on."
    pause 1.1
    N "Mom called it..."
    N "A warp drive."
    N "But this one..."
    N "This is bigger than the prototype."
    stop sounds1 fadeout 2.0
    play sound closescidoor
    play music anisolatedmoment
    scene s0b8 with dissolve
    az "Don’t worry… you’re not leaving. Not until I say so."
    az "My dear… {b}friends{/b}."
    az "No… not friends."
    scene s0b10 with dissolve
    az "...Or are you?"
    scene s0b9 with dissolve
    az "Twenty years…"
    az "Twenty long… stretching… years."
    az "And now you’re standing here. In front of me."
    az "But why…? Your faces… why can’t I see them?"
    az "Only… fire."
    az "Fire… No—no, no, no—!"
    az "It hurts…"
    play sound mmove
    scene s0b11 with dissolve
    h "(quietly) ...He’s not right in the head."
    h "You were dead."
    h "So how the hell are you standing here?"
    scene s0b12 with dissolve
    az "..."
    scene s0b13 with dissolve
    az "Was I?"
    az "I don’t remember."
    play sound mmove
    scene s0b14 with dissolve
    az "Did they kill me…?"
    az "No…?"
    az "Then why am I here…"
    az "Because of them."
    az "Yes… THEM."
    az "But why… why…"
    scene s0b15 with dissolve
    az "Ah—!"
    az "I remember—yes, yes— it was y—"
    az "No."
    az "I remember perfectly."
    az "You pulled the trigger."
    stop music 
    play sound gunshoot
    scene s0b16 with dissolve
    pause 0.5
    play sounds2 fall
    play sounds1 generator loop volume 0.2
    scene s0b17 with dissolve
    h "You should’ve stayed buried."
    scene s0b18 with dissolve
    mc "(Is he... actually dead?)"

    scene s0pp72 with dreamyzoom 
    show memoryframe with dissolve 
    npc "Substance capable of regenerating even human organs."

    scene s0b18 with dissolve
    mc "(Could it...?)"
    mc "..."
    mc "Olivia, careful. He's not dead yet."
    play sound mmove
    scene s0b19 with dissolve
    h "...Not?"
    h "I just put a bullet in his head."
    h "What do you mean ‘not’?"
    scene s0b20 with dissolve
    N "Dad’s right, he’s not dead!"
    scene s0b22 with dissolve
    h "Oh come on—"
    h "You’re telling me that thing’s still alive?"
    scene s0b21 with dissolve
    N "Mom's notes mentioned it."
    N "The substance doesn't just heal."
    N "It rewrites the host."
    N "After that, he stopped being human."
    stop sounds1 fadeout 2.2
    play music demiseofanation fadein 0.5
    scene s0b23 with dissolve
    az "A human?"
    az "No… no, I am human."
    az "Still human."
    play sound clench
    scene s0b24 with dissolve
    az "Just… different."
    az "A little… rearranged."
    play sound mmove
    scene s0b25 with dissolve
    az "Ah—!"
    az "That hurts…"
    az "Hurts-hurts-hurts…"
    scene s0b26 with dissolve
    play sound mmove
    mc "What... are you?"
    scene s0b27 with dissolve
    az "What?"
    az "I told you, human!"
    az "Just… slightly… modified."
    az "Improved, maybe."
    play sound soldierun volume 0.4
    scene s0b28 with dissolve
    az "I was like you once. Weak. Afraid. Small."
    az "Waiting to die."
    az "But death…"
    az "...death doesn’t end things."
    az "It bends them."
    az "Breaks them."
    play sound soldierun volume 0.4
    scene ls 24 with dissolve
    az "My daughter…"
    az "Poor thing. Loyal to the end."
    az "She made a deal."
    az "With a woman… strange… wrong."
    az "They told her: ‘We can bring him back.’"
    az "And she—"
    az "—she said yes."
    scene s0b13 with dissolve
    az "And now I’m here."
    az "See? Not so bad."
    az "We could even be friends."
    az "…Right?"
    play sound mmove
    scene s0b14 with dissolve
    az "No… no."
    az "No-no—NO."
    scene ls 25 with dissolve
    az "You killed me."
    az "That day."

    show s0w91 with dreamyzoom
    show memoryframe
    play sounds2 scar1 volume 0.2 
    pause 1.1
    play sounds4 hdshot
    scene s0w92 with dissolve
    show memoryframe
    pause 1.1

    scene ls 26 with dissolve
    az "And since then—"
    az "It replays. Every night."
    az "I shut my eyes—"
    az "—and there you are."
    scene s0b14 with dissolve
    az "You didn’t hesitate."
    az "That’s what I admire."
    scene s0b15 with dissolve
    play sound closescidoor
    az "It’s driven me mad."
    play sound metalstep
    scene s0b29 with dissolve
    pause 1.5
    mc "(…The masked guy?)"
    mc "How did you get in here?"
    az "You opened the way."
    az "All we had to do... was follow."
    scene s0b30 with dissolve
    a "Stay out of this, little man. He’s mine to deal with."
    scene s0b32 with dissolve
    az "That’s not what we agreed on."
    scene s0b31 with dissolve
    a "That man’s body… must be kept alive."
    play sound metalstep
    scene s0b33 with dissolve
    a "This is the will… of the woman who created me."
    scene s0b34 with dissolve
    aa "Sir, why send him personally? We could've taken the target at the entrance."
    scene s0b35 with dissolve
    az "No…"
    az "I want to watch."
    play sound deserteagle1 
    scene s0b36 with dissolve
    aa "But si—"    
    play sound fall
    scene s0b37 with dissolve
    az "You’re… irritating."
    play sounds1 deatwishes
    scene s0b38 with dissolve
    pause 2.1
    scene s0b39 with dissolve
    h "Out—!"
    h "Out of ammo, cover me!"
    play sound mmove
    scene s0b40 with dissolve
    pause 0.5
    scene s0b41 with dissolve
    mc "How much longer?!"
    play sound mmove
    scene s0b42 with dissolve
    h "Don’t rush me—!"
    h "I’m on it!"
    play sound whoosh 
    scene s0b43 with CropMove(time=0.1, mode='slideright')
    a "That won’t help you, little man."
    play sound whoosh 
    scene s0b44 with CropMove(time=0.1, mode='slidedown')
    pause 0.5
    play sound punch1
    scene s0b45 with vpunch
    pause 0.5
    play sound mmove
    scene s0b46 with dissolve
    mc "(Tough…)"
    mc "(Feels like hitting steel.)"
    mc "So you’re the one pulling the strings."
    a "Pulling… strings?" 
    a "I do not understand. Explain, little man."
    play sound whoosh 
    scene s0b47 
    pause 0.4
    play sound punch1
    scene s0b48 with vpunch
    pause 0.5
    play sound whoosh 
    scene s0b49 
    pause 0.2
    scene s0b50 with dissolve
    mc "(…Wrong target?)"
    a "Too slow."
    play sound whoosh 
    scene s0b51 
    pause 0.5
    play sound punch1
    scene s0b52 with vpunch
    a "You dodge well, little man. But how long can you keep it up?"
    scene s0b53 with dissolve
    az "..."
    scene s0b54 with dissolve
    az "Two against one?"
    az "Mm."
    az "How… disappointing."
    scene s0b55 with dissolve
    pause 0.5
    scene s0b56 with dissolve
    N "What’s he planning..."
    scene s0b58 with dissolve
    N "Don’t—"
    stop music
    play sound deserteagle1 
    scene s0b59 with vpunch
    pause 0.5
    play sounds1 fall
    scene s0b57 with dissolve
    pause 1.1
    play music theuntold fadein 3.0
    scene s0b60 with dissolve
    mc "NORMAN!" 
    play sound punch1
    scene s0b61 with vpunch
    a "Got you now, little man."
    scene s0b62 with dissolve
    pause 0.5
    scene s0b63 with dissolve
    pause 0.5
    scene s0b64 with dissolve
    h "[mc]!"
    play sound metalstep
    scene s0b65 with dissolve
    a "Honestly, I didn’t expect the little man to last this long."
    play sound metalstep
    scene s0b66 with dissolve
    h "Hold on—!"
    scene s0b67 with dissolve
    az "You’re all running out of time."
    az "You just don’t know it yet."
    play sound mmove
    scene s0b69 with dissolve
    az "No matter."
    az "Give him my regards…"
    scene s0b69 with dissolve

    image s0transition4 = Movie(channel="movie_dp", loop = False, play="video/s0transition4.webm")
    show s0transition4
    $ renpy.pause(0.6, hard=True)

    play sounds3 warptravaling fadein 0.6 loop
    stop music fadeout 2.1
    scene s0b70 with dissolve
    aaa "..."
    aaa "Miriel… thirty seconds."
    aaa "Small ones are mine."
    aaa "The big one… yours."
    Mi "…Understood."
    scene s0b71 with dissolve
    pause 0.2
    play sound pisolsil
    scene s0b72 with dissolve
    pause 0.2
    play sound pisolsil
    scene s0b73 with dissolve
    pause 0.2
    play sound pisolsil
    scene s0b74 with dissolve
    pause 0.2
    stop sounds3 fadeout 0.5
    play sounds4 hdshot
    scene s0b75 with dissolve
    pause 0.5
    play sounds4 hdshot
    scene s0b76 with dissolve
    pause 0.5
    play sounds1 fall
    scene s0b77 with dissolve
    a "The big man? What’s he doing here?"
    a "We need to deal with this before the queen sees."
    play sound glitchfear volume 0.3
    scene s0b78 with glitch
    Mi "Don’t worry… you’re facing me now."
    play sound mmove
    scene s0b79 with dissolve
    a "The Cold Reaper? Yes... you’re a worthy foe. Let’s fight!"
    play sound teleport 
    scene s0b80 with vpunch
    play sounds2 knifehit
    pause 1.2
    play sounds1 fall
    play music ending fadein 2.5
    scene s0b81 with dissolve
    Mi "…I don’t have time for you."
    play sounds1 metalstep
    scene s0b83 with dissolve
    h "[mc]…!"
    h "Hey—!"
    scene s0b84 with dissolve
    h "Stay with me…"
    h "Come on… stay with me."
    Mi "..."
    aaa "Well?"
    aaa "What do you see."
    scene s0b86 with dissolve
    Mi "…The lady’s words don’t add up."
    Mi "The portal… reacted to the older one."
    scene s0b87 with dissolve
    h "Help’s coming."
    h "You hear me?"
    h "They’re coming— they’ll fix this."
    scene s0b89 with dissolve
    h "You promised me."
    play sounds mmove
    scene s0b90 with dissolve
    h "So don’t you dare die on me now."
    h "Not like this…"
    h "Not here…"
    scene s0b91 with dissolve
    aaa "Take both. The girl doesn’t see the portal."
    aaa "Her mind… won’t survive it."
    scene s0b92 with dissolve
    Mi "I’ll secure them… and catch up."
    scene s0b93 with dissolve
    aaa "..."
    scene s0b94 with dissolve
    aaa "A portal…"
    aaa "Time displacement."
    scene s0b95 with dissolve
    aaa "So this is it."
    aaa "The source of the chaos."
    
    image s0transition5 = Movie(channel="movie_dp", loop = False, play="video/s0transition5.webm")
    show s0transition5
    $ renpy.pause(0.6, hard=True)

    play sounds3 warptravaling fadein 0.6 loop
    scene s0b96 with dissolve
    aaa "…What—"
    scene s0b97 with dissolve
    aaa "No…"
    aaa "That presence…"
    aaa "Selvaria..."
    scene s0b98 with dissolve
    Mi "Master… what’s happening?"
    stop sounds3 fadeout 0.5
    scene s0b99 with dissolve
    aaa "The boy. The girl."
    aaa "Take them."
    aaa "We leave. Now."
    scene s0b100 with dissolve
    Mi "Understood. I’ll handle it."

    image s0transition6 = Movie(channel="movie_dp", loop = False, play="video/s0transition6.webm")
    show s0transition6
    $ renpy.pause(10, hard=True)

    scene s0b102 with dissolve
    aaa "{font=Cybertron.otf}If he’s tied to Lora, we take him. Make sure he survives."
    Mi "…I’ll take care of it."
    scene s0b103 with dissolve
    aaa "This will be enough."
    aaa "To slow them."
    scene s0b105 with dissolve
    pause 1.8
    scene s0b106 with dissolve
    pause 1.1
    stop music fadeout 1.2
    scene black with dissolve
    pause 2.1
    play music shiyahospital1 fadein 4.0    
    scene s0b107 with dissolve
    aaaa "They escaped..."
    stop sounds1 fadeout 2.5
    scene s0b108 with dissolve
    aaaa "Told you — we should’ve moved faster."
    scene s0b109 with dissolve
    aa "They aren’t our target. You’ll get your revenge later."
    scene s0b110 with dissolve
    aaaaa "Steal what is mine… right under my gaze?"
    aaaaa "...Astoria."
    scene s0b111 with dissolve
    aaaaa "Some things… never change."
    scene s0b112 with dissolve
    aaaaa "Use their body."
    aaaaa "We’re going to pay… our old friends a visit."
    scene black with dissolve
    b "Yes, your highness."


    
    scene black 
    pause 3.0

    jump story02

    return


