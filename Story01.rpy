default Ostorius_help = False
default mc_status = 10
default qeustion = False
default mcmeety = False
default lora = 5

default mc_lust = 0
default Olivia = 10
default first_question_olivia = False
default first_question_place = False
default first_question_son = False
default whatplaceisit1 = False


label story02:
    $ death_shiya = 1
    $ death_olivia = 1
    $ persistent.chapter_act1 = True
    stop music fadeout 5.2

    scene black with dissolve
    pause 2.0

    play music bar2 fadein 0.5
    show s1p8 with dissolve
    show 7yr with dissolve 
    pause 0.7
    C "(…Weird.)"
    C "(Feels like I haven’t been somewhere this… dead in years.)"
    show s1p7 with dissolve
    C "(I wonder how Olivia’s doing…)"
    C "(It’s been quiet since last night…)"
    show s1p10 with dissolve
    C "(What if something went wrong?)"
    show s1p9 with dissolve
    C "(No. Stop.)"
    C "(Don’t start that.)"
    C "(It’s just bad signal. That’s it.)"
    C "(Nothing more.)"
    stop music fadeout 0.5
    play sounds1 breakingnews1 fadein 0.5 
    show s1p with dissolve
    new "In the early hours of the morning, sometime between midnight and 8 AM, a massive explosion ripped through the eastern sector."
    stop sounds1 fadeout 0.5

    play sounds2 kitchensound1 fadein 1.0 volume 0.2
    play sound kitchensound2 volume 0.2 loop
    show s1p12 with dissolve
    new "Witnesses describe a deafening blast..."
    new "Authorities believe this may have been an act of sabotage at a major oil facility."
    show s1p11 with dissolve
    new "Fires are still raging out of control."
    new "Officials are calling this one of the darkest days in recent history."
    stop sounds2
    stop sound 
    play music aftership2 volume 0.8
    show s1p13 with dissolve
    new "Sources now report that those responsible may be a rogue group of former military personnel."
    new "They are allegedly led by General Richard..."
    new "...who has just been placed on the country's most-wanted list."
    new "Authorities urge anyone with information to come forward immediately."
    show s1p14 with dissolve
    new "Several additional suspects have been identified."
    new "Among them: Olivia... Norman... [mc]... Shiy..."
    show s1p15 with dissolve
    new "At this time, the situation remains unstable."
    new "We will continue to monitor developments and bring you updates as soon as they come in."
    show s1p17 with dissolve    
    pause 0.5
    show s1p18 with dissolve
    D "Sir... there’s an urgent call for you."
    show s1p19 with dissolve
    a "...I’m listening."
    a "Is there anything else you need from me?"
    show s1p21 with dissolve
    s "..."
    a "I’ve done everything you asked."
    a "Every target. Every betrayal."
    a "Now it’s your turn."
    a "Let my family go."
    show s1p20 with dissolve
    s "Heh..."
    s "You’ve been... exceptional."
    s "Efficient. Precise. Obedient."
    scene s1p21 with dissolve
    a "...What’s that supposed to mean?"
    scene s1p20 with dissolve
    s "It means you did exactly what we needed."
    s "But your family?"
    s "...They were never part of the deal."
    scene s1p19 with dissolve
    a "...No."
    a "No, that’s not true."
    a "That’s NOT what we agreed!"
    scene s1p21 with dissolve
    a "You said they’d be safe!"
    a "You said—"
    scene s1p20 with dissolve
    s "You knew the risks."
    s "And you made your choice."
    scene s1p19 with dissolve
    a "You bastards..."
    a "I gave you EVERYTHING!"
    scene s1p21 with dissolve
    a "And this is how you repay me?!"
    scene s1p20 with dissolve
    s "You should be proud."
    s "...Goodbye."
    show s1p19 with dissolve
    a "Wait!"
    a "PLEASE—!"
    a "DON’T DO THIS!!"
    play sounds1 cinematichit3 fadeout 0.5
    stop music

    scene black 
    pause 3.0

    play music esc1 
    window hide
    image transi1 = Movie(channel="movie_dp", loop = False, play="video/transition2.webm")
    show transi1
    $ renpy.pause(4.1, hard=True)
    window auto


    show s1s9 with dissolve
    a "It’s a miracle he’s still breathing..."
    hide transi1
    show s1s10 with dissolve
    a "Sir, tomography shows the artery is ruptured and has caused internal bleeding. We need to repair it immediately."
    show s1s11 with dissolve
    a "We have to operate on the artery right now, or the damage will be irreversible."

    window hide
    image transi2 = Movie(channel="movie_dp", loop = False, play="video/transition9.webm")
    show transi2 
    $ renpy.pause(6.1, hard=True)
    window auto

    

    show s1s13 with dissolve
    a "Damn it, I told you this was reckless. Cybernetic heart implantation is almost always a guaranteed death."
    hide transi2
    show s1s14 with dissolve
    a "We don’t have time for this. Scalpel!"

    play sounds1 heartbeat fadein 7

    window hide
    image transi3 = Movie(channel="movie_dp", loop = False, play="video/transition6.webm")
    show transi3 
    $ renpy.pause(9.1, hard=True)
    window auto

    stop sounds1
    show s1s16 with dissolve
    hide transi3
    h "Please... don’t leave me here alone..."
    h "You promised me... Please..."
    scene black with dissolve

    window hide
    image transi4 = Movie(channel="movie_dp", loop = False, play="video/transition8.webm")
    show transi4 
    $ renpy.pause(9.1, hard=True)
    window auto
    
    stop music fadeout 1.5
    scene black 
    pause 3.0
    show act1s1 with dissolve
    pause 1.5
    show act1s2 with dissolve
    pause 1.5
    #Transition here
    play music wot fadein 5.0

    show s1p22 with dissolve
    pause 1.0
    show s1p23 with dissolve
    pause 1.0
    show s1p24 with dissolve
    pause 1.0
    show s1p25 with dissolve
    show 5yr with dissolve
    pause 0.7
    mc "..."
    hide 5yr with dissolve
    show s1p25 with dissolve
    mc "Where…"
    show s1p26 with dissolve
    mc "How did I even get here…?"
    show s1p27 with dissolve
    mc "What is this place…?"
    mc "Messing with me."
    show s1p28 with dissolve
    mc "…Nothing."
    mc "I can’t remember anything."
    show s1p29 with dissolve
    mc "I should move…"
    mc "…But there’s nothing here."
    show s1p31 with dissolve
    mc "No choice."
    show s1p32 with dissolve
    mc "Alright… here goes nothing"
    play sound footstep volume 2.0
    show s1p33 with dissolve
    pause 1.0
    show s1p34 with dissolve
    pause 1.0
    show s1p35 with dissolve
    mc "..."
    mc "…Wait."
    mc "I’ve been here."
    show s1p36 with dissolve
    mc "No…"
    show s1p30 with dissolve
    mc "Just the dark."
    scene s1p32 with dissolve
    mc "Messing with me."
    play sound footstep volume 2.0
    show s1p33 with dissolve
    pause 1.0
    show s1p34 with dissolve
    pause 1.0
    show s1p35 with dissolve
    mc "..."
    show s1p38 with dissolve
    mc "Is anyone out there?!"
    show s1p39 with dissolve
    mc "..."
    show s1p40 with dissolve
    mc "HEY!"
    mc "ANYONE?!"
    show s1p41 with dissolve
    mc "..."
    mc "…Nothing."
    mc "Not even an echo."
    scene s1p36 with dissolve
    mc "…Wait."
    mc "Light?"
    mc "If not for that…"
    scene s1p36 with dissolve
    mc "…Yeah."
    mc "I’m alone."
    scene s1p31 with dissolve
    mc "I have to keep hoping I’ll find a way out of here."
    mc "(Find Lora. Find a way home.)"
    mc "(Everything else comes after that.)"
    play sound footstep volume 2.0
    scene s1p32 with dissolve
    pause 1.0
    scene s1p33 with dissolve
    pause 1.0
    scene s1p34 with dissolve
    pause 1.0
    scene s1p35 with dissolve
    mc "..."
    mc "No way out…?"
    mc "Am I stuck here…?"
    show s1p36 with dissolve
    mc "No."
    play sound footstep volume 2.0
    scene s1p32 with dissolve
    pause 1.0
    scene s1p33 with dissolve
    pause 1.0
    scene s1p34 with dissolve
    pause 1.0
    scene s1p35 with dissolve
    mc "..."
    show s1p40 with dissolve
    mc "Is anyone here?!"
    play sounds1 sth1 fadein 2.0
    show s1p41 with dissolve
    a "To your left."
    show s1p42 with dissolve
    mc "…What?"
    show s1p43 with dissolve
    mc "It can’t be…"
    show s1p44 with dissolve
    mc "Light…"
    stop music fadeout 2.0
    play sound windparadise loop fadein 2.0
    scene black with dissolve
    pause 1.0   
    show s1p45 with dissolve
    pause 1.0
    show s1p46 with dissolve
    pause 1.0
    show s1p47 with dissolve
    mc "…What is this…"
    show s1p48 with dissolve
    mc "I’ve never seen anything..."
    show s1p49 with dissolve
    mc "..."
    show s1p50 with dissolve
    mc "Wait, is that…"
    show s1p51 with dissolve
    mc "…Someone?"
    show s1p52 with dissolve
    play music sweetheart fadein 5.0
    show s1p53 with dissolve
    mc "…Hey."
    show s1p54 with dissolve
    mc "Mind if I sit?"
    show s1p55 with dissolve
    mc "You’re the first person I’ve seen."
    mc "…In a while."
    show s1p56 with dissolve
    a "Of course… sit."
    show s1p60 with dissolve
    mc "..."
    show s1p61 with dissolve
    a "Peaceful, isn’t it…?"
    a "Makes you want to just sit here… and never leave."
    show s1p63 with dissolve
    mc "You seen anyone else?"
    show s1p62 with dissolve
    pause 1.0
    show s1p60 with dissolve
    pause 1.0
    scene s1p61 with dissolve
    a "Before you? No."
    a "You’re the first one I’ve seen… this whole time."
    show s1p64 with dissolve
    mc "Do you know where we are?"
    mc "Or how you got here?"
    show s1p65 with dissolve
    pause 2.0
    show s1p66 with dissolve
    a "..."


    show s1p67 with dissolve
    a "…No."
    a "I don’t."
    show s1p68 with dissolve
    mc "…I see."
    show s1p69 with dissolve
    mc "..."
    show s1p66 with dissolve
    a "..."
    pause 2.0
    show s1p70 with dissolve
    mc "Wait…"
    mc "You’re leaving?"
    mc "We just—"
    show s1p72 with dissolve
    pause 1.0
    show s1p73 with dissolve
    pause 1.0
    show s1p74 with dissolve
    pause 1.0
    show s1p77 with dissolve
    mc "Where are you going?"
    mc "…Stay."
    show s1p78
    a "..." 
    show s1p75 with dissolve
    a "…One last thing."
    scene s1p78 with dissolve
    pause 1.0
    show s1p76 with dissolve
    a "When I go… let me go with a smile."
    a "Don’t let grief take that light from you."
    a "Keep writing your story."
    a "Live with courage… live bright."
    show s1p84 with dissolve
    mc "…live bright."
    show s1p85 with dissolve
    pause 1.0
    show s1p80 with dissolve
    mc "…How do you know that?"
    Ne "You used to say that… whenever you thought of Mom."
    Ne "…And I’m sorry."
    Ne "Looks like I’ll be the one going first."
    show s1p81 with dissolve
    pause 1.0
    show s1p82 with dissolve
    Ne "One more thing…"
    Ne "Take care of Alex… and Mina."
    show s1p83 with dissolve
    Ne "Thank you… for everything, Dad."
    Ne "I’ll be waiting for you."
    show s1p86 with dissolve
    mc "Wait a minute!"
    mc "Wait—"
    show s1p87 with dissolve
    mc "NORMAN!"
    stop music
    stop sound

    play sounds1 glitchfear volume 0.5
    scene black with glitch
    pause 3.0

label laborat:
    play music mecd fadein 3.0

    image wakeupsamurai = Movie(channel="movie_dp", loop = False, play="video/wakeupsamurai.webm")
    show wakeupsamurai with dissolve
    $ renpy.pause(13.2, hard=True)

    

    show s1p94 with dissolve
    
    if persistent.inquisitor_access == 1:
        $ persistent.inquisitor_access = 2
        show clearlvl with dissolve 

    o "Ah… there you are."
    show s1p95 with dissolve
    o "Easy. Don’t rush it."
    o "You barely held together the first time when your artery ruptured, seams are still… questionable."
    show s1p96 with dissolve
    mc "Where am I?"
    mc "What did you do to me—"
    play sounds1 glitchsound2 volume 0.5
    show s1p97 with glitch
    mc "AH!"
    show s1p98 with dissolve
    o "Your body hasn’t fully agreed on being alive."
    o "Don’t fight it."
    o "Let your head catch up."
    play sounds1 button
    show s1p99 with dissolve
    o "Answers will come, with time."
    mc "That’s not good enough."
    show s1p100 with dissolve
    o "For now… breathe."
    o "Yeah. Like that."
    play sound button
    show s1p101 with dissolve
    mc "My head’s…"
    mc "It’s all a static noise."
    play sounds1 dooropen
    show s1p102 with dissolve
    R "That’s because it should be."
    show s1p103 with dissolve
    R "You were clinically dead."
    play sound footstep volume 2.0
    show s1p105 with dissolve   
    R "Several minutes without oxygen."
    R "By all known parameters… you are supposed to be gone."
    show s1p106 with dissolve
    R "And yet here you are."
    show s1p107 with dissolve
    R "We rebuilt you."
    mc "Rebuilt?! What do you mean?"
    R "Listen."
    R "You were dying. We had to replace all that we could replace, and stabilized the rest."
    show s1p108 with dissolve
    R "I will tell you more later, for now all you need to know is..."
    play sounds1 metalstep 
    show s1p109 with dissolve
    R "We brought you back."
    play sound sittingchar fadein 0.4
    show s1p110 with dissolve
    R "Remember anything?"
    mc "Should I?"
    show s1p111 with dissolve
    mc "(Where…?)"
    mc "(No...)"
    mc "(Why can’t I remember?)"
    show s1p112 with dissolve
    mc "It’s all…"
    mc "Just… fog."
    mc "I can’t reach it."
    show s1p113 with dissolve
    o "Looks like the memory blocker’s still running."
    o "That would explain the fog."
    o "Sit still. Let me take a look."
    play sounds1 metalstep 
    show s1p114 with dissolve
    mc "A memory blocker…?"
    mc "You put something in my head?!"
    show s1p115 with dissolve
    o "What, surprised?"
    pause 1.1
    o "Relax. It’s standard procedure. After trauma like yours, brains tend to melt."
    o "Memory blockers prevent this from happening."
    play sounds1 squish volume 0.5
    show s1p116 with dissolve
    o "I’m going to ease the flow a bit."
    show s1p117 with dissolve
    o "And here’s a friendly tip-"
    o "Try not to scream."
    show s1p118 with dissolve
    o "You will anyway, but… worth saying."
    play sounds1 glitchsound2 volume 0.5
    show s1p119 with glitch
    mc "Why does it—"
    mc "Fuck!"
    mc "It’s burning!"
    stop sounds1
    o "Pain means the signal’s getting through."
    o "Feels awful, I know. But still good news."
    o "Your memory should start coming back. Slowly."
    show s1p121 with dissolve
    R "Focus."
    R "Name?"
    show s1p125 with dissolve
    "Your memory starts coming back."
    mc "(…I died?)"
    pause
    mc "(No…)"
    mc "(No.)"
    R "You hear me?"
    R "Your name."
    show s1p125 with dissolve
    mc "(Name…?)"
    mc "(My name…)"
    show s1p126 with dissolve
    mc "[mc]."
    scene s1p125 with dissolve
    R "Age?"
    scene s1p126 with dissolve
    mc "44."
    mc "Before you ask more questions, who are you and why did you do this for me?"
    scene s1p121 with dissolve
    R "We’re not here to answer questions. We are here on the orders of The Lady."
    R "We just need to make sure you function."
    mc "Who is this Lady you are talking about?"
    R "You can ask those questions later, for now answer my questions."
    R "Any irregularities?"
    R "Dizziness. Nausea."
    R "Intrusive imagery… existential or otherwise."
    show s1p125 with dissolve
    mc "(Yeah… this doesn’t feel right. Not even close.)"
    mc "(And, showing weakness isn’t an option either.)"
    show s1p124 with dissolve
    mc "No."
    mc "Felt… normal."
    scene s1p121 with dissolve
    R "Convincing."
    R "True or not doesn’t matter."
    R "If you believe it, it holds."
    R "Let’s proceed."
    R "The last memory before you woke u-"
    mc "What’s the point of all this?"
    R "I already—"
    mc "Details."
    R "..."
    R "I can’t."
    R "That’s above me."
    show s1p125 with dissolve
    mc "(That’s all I’m getting out of him?)"

    mc "(Then...)"
    mc "(…What was last?)"
    scene s0p69 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(Mission… a ship. {w=0.5}No data. Just coordinates...)"
    scene s0p41 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(Blind orders.)"
    scene s1p125 with dissolve
    pause 1.1
    mc "(Tell them the truth?)"
    mc "(No... I don’t know them. This stays with me.)"
    show s1p126 with dissolve
    mc "We went in."
    mc "A structure… gutted from the inside. {w=0.5}No light. {w=0.5}No life. {w=0.5}Just wreckage and then-"

    scene s1p125 with dissolve
    pause 1.1
    scene s0q152 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(We weren’t alone. There was something else there.)"  # 8 tho  
    pause 1.1
    mc "(Not a survivor.)"
    scene s1p125 with dissolve
    pause 1.1
    scene s1p126 with dissolve
    mc "There was chaos... We saw—" 
    show s1p125 with dissolve
    mc "(Wait…)"
    
    scene s0b23 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(Not something.)"
    scene s0b12 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(Someone.)"
    scene s0b59 with dreamyzoom 
    show memoryframe with dissolve 
    N "Don’t—"
    scene s0b87 with dreamyzoom 
    show memoryframe with dissolve 
    h "Stay with me…"

    show s1p127 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(Olivia… Norman…)"
    pause 1.1
    show s1p128 with dissolve
    mc "OLIVIA!"
    mc "NORMAN!"
    mc "Where are they?!"
    mc "What happened?!"
    mc "They’re alive—"
    show s1p133 with dissolve 
    R "Calm yourself."
    show s1p137 with dissolve
    R "They’re alive."
    mc "(…Alive.)"
    
    R "For now… that is sufficie-."    
    mc "...Take me to them."
    mc "Now."
    pause 1.1
    show s1p140 with dissolve
    o "Okay, but first…"
    o "Walking the halls like that? You’ll attract attention."
    stop sounds1 fadeout 0.5
    stop sound fadeout 0.5 
    stop music fadeout 0.5
    scene black with dissolve
    pause 1.0
    
    play sounds1 dooropen
    play sound roomambient loop
    play music laboratory1 fadein 3.0
    $ mc_powerup += 1
    show s1pp1 with dissolve
    H "Access is restricted. Unauthorized presence will trigger protocol-level alerts."
    show s1pp3 with dissolve
    show 5yr with dissolve
    mc "(It seems like I’m in some kind of cutting-edge laboratory. Far too advanced for anything I’ve ever seen...)"  # 15 tho  
    show s1pp10 with dissolve
    R "You know… your arrival stirred quite a bit of unease."
    R "The right hand himself dragging someone in?"
    R "Personally? {w=0.5}That doesn't happen."
    show s1pp11 with dissolve
    mc "The right hand?"
    show s1pp10 with dissolve
    R "Yeah. Big name around here."
    R "Which makes it… interesting."
    R "What exactly makes you worth the trouble?"
    show s1pp11 with dissolve
    mc "Skip the speech."
    mc "And answer my questions."
    mc "What have you done to my body? It feels... different"
    scene s1pp10 with dissolve

    R "We integrated your body with implants."
    R "But that’s not the problem."
    R "Your body… interacts with them too well."
    R "Not like an external system."
    R "Like they belong to you."
    R "As if they always did."
    scene s1pp11 with dissolve
    mc "Where’s my son?"
    mc "Where’s Olivia?"
    show s1pp12 with dissolve
    R "Last time I saw your… friend, she was safe."
    R "Your son…"
    R "That’s a different question."
    mc "What did you do to him—"
    show s1pp13 with dissolve
    o "What he’s trying to say is..."
    o "We’re scientists. We study things most people would rather not understand."
    o "As for your friends…"
    o "They’re not under our protection."
    show s1pp14 with dissolve
    mc "Not good enough."
    R "If we simplify things."
    show s1pp17 with dissolve
    R "We only know about the girl because she kept coming here."
    R "Often."
    R "More than she should have."
    R "…Looking after you, I assume."
    show s1pp18 with dissolve
    mc "My son."
    mc "Now."
    show s1pp19 with dissolve
    R "As for your son... {w=0.5}no idea."
    mc "That’s not an answer."
    R "It’s the only one you’re getting from me."
    R "You’ll have to ask upstairs."
    show s1pp20 with dissolve
    R "…If you’re lucky."
    show s1pp21 with dissolve
    mc "Lucky…?"
    mc "(She brought me here…?)"
    show s1pp22 with dissolve
    o "He had… an unfortunate encounter with her."
    mc "She’s behind this, isn’t she?"
    o "The Lady?"
    o "Yes."
    show s1pp23 with dissolve
    o "But..."
    o "You don’t want to cross her on a bad day."
    o "Or any day, really."
    show s1pp24 with dissolve
    R "For once, I agree."
    show s1pp25 with dissolve
    mc "(Olivia’s alive. Norman no trace. Upstairs… the Lady.)"
    mc "(And they want me to meet her already...)"
    show s1pp27 with dissolve
    mc "How is she connected to Olivia and Norman?"
    mc "And how hard is it to get a meeting with her?"
    show s1pp28 with dissolve 
    o "Complicated."
    o "You don’t just walk in and ask for an audience."
    show s1pp27 with dissolve
    mc "So where’s the catch?"
    show s1pp28 with dissolve
    o "What are you getting at?"
    show s1pp30 with dissolve
    mc "I wake up, and I get an audience right away?"
    mc "You take me for a fool?"
    R "She knows things she shouldn’t."
    R "Things no one should."
    show s1pp31 with dissolve
    R "Your awakening—"
    R "She knew the exact moment."
    R "You would wake."
    show s1pp32 with dissolve
    mc "...She predicted it?"
    pause 1.1
    mc "Implants. Right?"
    o "If implants were the answer… this would be easy."
    show s1pp38 with dissolve
    mc "(So there’s something else at play… not just implants.)"
    show s1pp37 with dissolve
    o "Any more questions?"
    mc "Who exactly is the Lady?" 
    o "Astoria."
    o "She runs the upper city."
    mc "And why is everyone afraid of her?"

    o "Because her decisions rarely leave room for appeals."
    o "You’ll see the rest for yourself."

    o "But before we proceed—"
    mc "No."
    mc "You said she’s dangerous. I need to know why."
    o "You value your life?"
    o "Then don’t piss her off."
    mc "What kind of power is that?"
    o "..."
    o "From this point on… you’re with the Inquisiti-"
    mc "Stay on topic."
    o "Let me give you a piece of advice."
    o "Keep pushing like that, you won’t walk out of her office."
    mc "..."
    o "You’re with the Inquisition."
    scene s1pp72 with dissolve
    mc "The Inquisition…?"
    mc "I’m not joining."
    scene s1pp37 with dissolve
    o "You don’t really have a choice."
    mc "There’s always a choice."
    o "The fewer questions people ask about you…"
    o "The cleaner your story sounds."
    pause 1.3
    o "People don’t just appear here out of nowhere."
    scene s1pp34 with dissolve
    R "Oh, so beastmen get a free pass now?"
    o "Old man… don’t start."
    scene s1pp69 with dissolve
    mc "(Tension between them… noted.)"
    scene s1pp72 with dissolve
    mc "Fine. I’ll play along."
    mc "Anything else?"
    scene s1pp34 with dissolve
    R "Survive."
    R "That’s all that matters."
    scene s1pp40 with dissolve
    sci "Dr. Li, it’s urgent. They’ve made their move!"
    scene s1pp41 with dissolve
    R "Slow down."
    R "Start again."
    R "Clearly."
    scene s1pp42 with dissolve
    sci "The Inquisition! They’ve found out about our plans!"
    scene s1pp43 with dissolve
    mc "What is the Inquisition?"
    o "Internal enforcement."
    o "They control restricted technology, implants included."
    mc "So those implants belong to them."
    o "They think so."
    mc "(The Inquisition… Is this about me?)"
    scene s1pp44 with dissolve
    mc "Something happened?"
    scene s1pp45 with dissolve
    o "Yeah. You."
    o "Your implants…"
    o "Let’s just say, they don’t like that we took them... {w=0.5}without asking."
    scene s1pp46 with dissolve
    mc "Right. So you stole them."
    pause 1.1
    mc "Fantastic. Can't your so called Lady handle this?"
    o "It's... complicated"
    scene s1pp47 with dissolve
    R "Did they send someone?"
    R "Or is this just noise?"
    sci "Not just someone… a War Maiden. She’s here herself."
    scene s1pp48 with dissolve
    o "Hold on. What makes you think she’s here for us?"
    scene s1pp47 with dissolve
    sci "She’s... waiting at the entrance."
    scene s1pp49 with dissolve
    sci "And we’ve received an inspection request from the Inquisition department."
    scene s1pp50 with dissolve
    sci "It’s written here, black and white."
    sci "The Inquisition believes we’re behind the emergence of those monsters behind the wall."
    scene s1pp51 with dissolve
    R "Wait... soulless?"
    R "They think we’re behind this?"
    scene s1pp52 with dissolve
    R "And the implants?"
    sci "Second page, sir."
    scene s1pp51 with dissolve
    R "..."
    mc "(He’s nervous… and it’s not the Inquisition.)"
    mc "(The others aren’t.)"
    scene s1pp53 with dissolve
    R "I'm afraid our conversation ends here." 
    scene s1pp54 with dissolve
    R "I need to deal with this."
    scene s1pp55 with dissolve
    o "Don’t worry. I’ll handle things from here. You’ve got fire to put out."
    scene s1pp56 with dissolve
    mc "(Ship crash. Body-hacking scientists. Now the Inquisition…)"
    mc "(What the hell did I walk into?)"
    stop music fadeout 3.0
    play sounds1 sth1
    a "Help..."
    play sounds1 heartbeat
    scene s1pp57 with dissolve
    pause 0.5
    play sounds2 whooshvortex
    scene s1pp58 with dissolve
    pause 0.5
    scene s1pp59 with dissolve
    mc "(That voice again... what’s happening to me?)"  
    scene s1pp63 with dissolve
    mc "(Or was it just my imagination? Could it be... side effects?)"
    scene s1pp64 with dissolve
    o "Hey… you good?"
    scene s1pp65 with dissolve
    mc "No."
    mc "I’m hearing something."
    mc "Someone calling for help."
    scene s1pp66 with dissolve
    o "..."
    show s1pp67 with dissolve
    o "After your meeting, come see me."
    o "Your implant needs tuning."
    o "Don’t drag your feet."
    play sounds1 footstep
    
    stop sound
    scene black with dissolve
    pause 3.0

    play music1 eos fadein 3.0 volume 0.5
    play sounds1 metalstep 

    show s1pp75 with dissolve
    o "Alright… this is where I stop."
    o "Past that door, I’m not exactly welcome."
    mc "Why?"
    o "Security protocols."
    mc "Then why am I allowed in?"
    show s1pp76 with dissolve
    o "You’re a special case."
    o "But first, one more thing."
    play sounds2 whooshvortex
    show s1pp77 with dissolve
    o "Name."
    show s1pp78 with dissolve
    mc "(Name…?)"
    mc "(He wants me to shake his hand?)"
    mc "(No... this is a test.)"

    menu:
        "Keep your distance":

            show s1pp91 with dissolve
            mc "[mc]."
            scene s1pp92 with dissolve
            o "[mc]..."
            pause 1.1 
            o "(whispering) ...Careful."
            o "(whispering) Good."

            o "Don’t know that name."
            o "Where are you from?"
            scene s1pp91 with dissolve
            mc "Inquisition."
            play sounds1 metalstep 
            scene s1pp83 with dissolve
            o "Not bad."
            show s1pp83 with dissolve
            o "The Inquisition, elite."
            o "Act like it."

    
        "Take his hand":

            play sounds2 clench volume 0.3
            show s1pp79 with dissolve
            mc "[mc]."
            show s1pp81 with dissolve
            o "[mc]..."
            o "Straight to contact."
            pause 1.1
            o "(whispering) Bad habit."
            o "Where are you from?"
            scene s1pp79 with dissolve
            mc "Inquisition."
            scene s1pp81 with dissolve
            o "Almost."
            show s1pp83 with dissolve
            o "Close."
            o "Inquisition likes to make an impression."
            o "You… not quite there yet."

    
    o "Alright. I’m handing you over to Miriel."
    o "She’s quiet…"
    o "But don’t let that fool you. She’s better than anyone here. By a mile."
    play sounds1 metalstep
    show s1pp84 with dissolve
    o "And that voice you mentioned earlier…"
    show s1pp85 with dissolve
    o "If it gets worse, find me."
    o "Stage 32, implants lab."
    show s1pp87 with dissolve
    mc "I’ll remember."
    show s1pp86 with dissolve
    pause 0.5
    play sounds1 metalstep
    show s1pp89 with dissolve
    pause 0.5
    show s1pp90 with dissolve
    mc "(Too friendly.)"
    mc "(He definitely wants something.)"
    play sounds1 metalstep
    show s1pp95 with dissolve
    mc "(And this place… it’s different. The question is, how different.)"
    mc "(Find Olivia and Norman first. Everything else can wait.)"
    mc "(Then Lora.)"
    mc "(If this world took her from me, it also has to have a way back to her.)"
    show s1pp95 with dissolve
    pause 1.1
    show s1pp96 with dissolve
    o "Miriel. He’s yours now."

    scene s1tew5 with dissolve
    pause 1.1
    scene s1tew4 with dissolve
    pause 0.7
    scene s1tew3 with dissolve
    pause 0.5
    scene s1tew1 with dissolve
    Mi "Understood. Let’s move."
    scene s1tew2 with dissolve
    pause 1.1
    
    $ unlock_miriel = 1


    stop music1 fadeout 1.4

    play music testimony1 fadein 1.0 volume 0.6

    scene black with dissolve
    pause 3.0



label part2:
    
    image cybercity = Movie(channel="movie_dp", loop = False, play="video/cybercity.webm")
    show cybercity with dissolve
    $ renpy.pause(8.1, hard=True)

    play sounds2 elevator3 loop volume 0.2
    scene s1b2 with dissolve
    mc "What the..."
    mc "This... isn’t the sky."
    mc "Ships...?"
    mc "They’re... floating?"
    show s1b3 with dissolve
    mc "(Wait... ears?)"
    scene s1p95 with dreamyzoom 
    show memoryframe with dissolve 
    mc "(Hold on. That beastman earlier… they’re not human.)"

    scene s1b3 with dissolve
    pause 1.1
    mc "(Wait... then what the hell is this place?!)"

    scene s0a3 with dreamyzoom
    show memoryframe with dissolve 
    Lo "Something related to teleportation… I think."
    scene s0b6 with dreamyzoom
    show memoryframe with dissolve 
    N "Dad… that’s what Mom was working on."

    scene s1b3 with dissolve
    pause 1.1
    mc "..."
    mc "(Focus.)"
    show s1b4 with dissolve
    mc "Explain."
    mc "What is this place?"
    mc "And where did you bring me?"
    show s1b5 with dissolve
    Mi "My orders are clear. {w=0.5}I take you to the main office."
    Mi "No questions… {w=0.3}no small talk. {w=0.3}You follow. {w=0.3}I lead."

    scene ch 175 with dreamyzoom
    show memoryframe with dissolve     
    N "It wasn’t my choice… I was led there."     
    N "A man… wearing a black mask."

    scene s1b3 with dissolve
    mc "(Not a man… but... a black mask?)"
    scene s1b4 with dissolve
    mc "You brought me here so you must want something from me."
    show s1b6 with dissolve
    mc "Question is, what?"
    scene s1b3 with dissolve
    Mi "..."
    pause 1.1
    scene s1b3 with dissolve
    mc "(Talking to a wall.)"
    mc "(Let's try a different angle.)"
    show s1b2 with dissolve
    mc "You’re precise."
    mc "Not something you see every day."
    show s1b7 with dissolve
    Mi "..."
    show s1b8 with dissolve
    mc "Too much?"
    show s1b9 with dissolve
    Mi "No… just…"
    Mi "I’m not used to hearing that."
    show s1b10 with dissolve
    Mi "…Not from people like you."
    show s1b12 with dissolve
    mc "Someone like me?"
    scene s1b10 with dissolve
    Mi "…You’re human."
    scene s1b12 with dissolve
    mc "…And?"
    scene s1b10 with dissolve
    Mi "My ears…"
    Mi "They don’t bother you?"
    Mi "When you look at me…"
    Mi "Do you feel anything? {w=0.5}Anger… {w=0.5}hatred… {w=0.5}pity?"
    mc "(That hit something.)"
    scene s1b12 with dissolve
    mc "Why would it?"
    mc "You think shape decides who you are?"
    show s1b13 with dissolve
    mc "Ears don’t carry sins."
    mc "People do."
    scene s1b15 with dissolve
    Mi "…I see."
    scene s1b3 with dissolve
    mc "(She’s starting to open up.)"
    scene s1b18 with dissolve
    mc "If there’s something you need, say it."
    scene s1b15 with dissolve
    Mi "I..."
    Mi "…No, nothing."
    show s1b17 with dissolve
    Mi "I… am just following orders."
    mc "(Same old line… getting real tired of it.)"
    Mi "(whispering) …So that I can repay her."
    scene s1b18 with dissolve
    mc "(…Repay her?)"
    scene s1b17 with dissolve
    mc "…Her?"
    mc "This is about Lady, isn’t it?"
    show s1b22 with dissolve
    Mi "…That’s enough."
    Mi "This conversation ends here."
    show s1b23 with dissolve
    pause 1.1
    show s1b24 with dissolve
    mc "Wait, answer me."
    stop sounds2 fadeout 1.5
    play sounds1 elevator1
    stop music fadeout 0.6
    show s1b25 with dissolve
    pause 1.0
    show s1b26 with dissolve
    Mi "We’re here. Stay on my six."

    scene black with dissolve
    pause 3.0

    image oliviarun = Movie(channel="movie_dp", loop = False, play="video/OR.webm")
    show oliviarun with dissolve
    $ renpy.pause(3.1, hard=True)

    play sound hug2
    play sounds1 ra2 loop volume 0.7
    show s1b27 with dissolve
    pause 1.5

    $ death_olivia = 0
    
    scene s1b28 with dissolve
    h "YOU’RE ALIVE!"
    play music holdon fadein 4.0
    show s1b29 with dissolve
    h "You stubborn idiot!"
    h "Do you have any idea what you just put me through?!"
    pause 0.8
    h "I thought—"
    pause 0.8
    h "I really thought I lost you."
    pause 1.1
    h "For good."
    show s1b30 with dissolve
    mc "I didn’t mean..." 
    mc "To put you through that…"
    mc "You were worried—"
    show s1b31 with dissolve
    h "Worry?!"
    h "Don’t you dare call it that."
    show s1b33 with dissolve
    pause 0.4
    show s1b34 with dissolve
    pause 0.4
    play sound hitol 
    scene s1b33 with dissolve
    h "Do you even get what that felt like?!"
    show s1b36 with dissolve
    pause 0.5
    show s1b35 with dissolve
    pause 0.5
    play sound hitol 
    scene s1b36 with dissolve
    pause 0.5
    show s1b37 with dissolve
    mc "(I don’t know what she went through…)"
    mc "(But this…)"
    show s1b38 with dissolve
    pause 1.0
    show s1b39 with dissolve
    mc "(Say it.)"
    mc "..."
    play sound hitol 
    scene s1b38 with dissolve
    pause 1.0
    h "Waking up every day thinking you were gone..."
    h "Going through that hell again and again..."
    h "And now you just show up like nothing happened…"
    show s1b40 with dissolve
    mc "(Come on… say it.)"
    show s1b41 with dissolve
    pause 1.0
    mc "(Do it.)"
    show s1b42 with dissolve
    mc "…Liv."
    mc "I’m sorry."
    scene s1b41 with dissolve
    h "Yeah…"
    h "Now that you’re here… breathing…"
    h "...Feels like I can finally breathe too."
    show s1b43 with dissolve
    Mi "I’ll give you two a moment, but..."
    show s1b44 with dissolve
    Mi "Liv, you’ve got thirty minutes. Not a second more."
    show s1b45 with dissolve
    h "..."
    stop music fadeout 3.0
    
    show s1b46 with dissolve
    mc "You made friends…?"
    show s1b47 with dissolve
    h "Her?"
    h "Oh, she’s great."
    h "Bit dramatic though."
    h "‘Cold Reaper’? Seriously?"
    a "{font=Cybertron.otf} (There’s a reason for that.)"
    play sounds1 glitchsound2 
    show s1b48 with glitch
    mc "AAARGH!"
    show s1b49 with dissolve
    h "Hey?! What’s happening?!"
    mc "My eye! Just... sharp pain. Like something’s clawing from the inside..."
    mc "(Someone else… in my head?)"

    play music towers fadein 2.9 
    play sounds1 footstep volume 2.0 
    play sound towerambient fadein 1.0 loop 

    show s1b53 with dissolve
    a "Oh sweetheart, your neurons are barely holding hands as it is."
    h "Who the hell are you?"
    $ unlock_flora = 1
    show s1b57 with dissolve
    a "Looks like his head’s about to go out with a bang."
    show s1b58 with dissolve
    a "So, two options."
    show s1b59 with dissolve
    a "Option one: you let me take a look, and I {b}might{/b} keep him in one piece."
    show s1b60 with dissolve
    h "And the second option?"
    show s1b61 with dissolve
    a "..."
    show s1b62 with dissolve
    a "Or..."
    a "...leave it as is and hope his skull doesn’t pop. Odds aren’t great."
    show s1b64 with dissolve
    a "BAM~!"
    a "Ever seen a glassfruit under a gravity hammer? Very… expressive."
    show s1b90 with dissolve
    a "So unless you’re in the mood to mop brain off the floor, move. I’m working."
    scene s1bb92 with dissolve
    mc "(You’re kidding, right?)"
    mc "(Like I didn’t have enough problems already... now I’m a walking bomb too.)"
    show s1b91 with dissolve
    h "...Fine."
    h "Just don’t screw this up."
    scene s1b92 with dissolve
    a "I’ll try. No promises if he explodes, though."
    mc "No one asked me."
    b "Stay out of it."
    stop music fadeout 1.3

    image floracheck = Movie(channel="movie_dp", loop = False, play="video/alor.webm")
    show floracheck with dissolve
    $ renpy.pause(5.41, hard=True)

    scene s1b68 
    h "And?!"
    show s1b69 with dissolve
    a "Relax." 
    a "He’ll survive." 
    a "Probably."
    scene s1b68 with dissolve
    h "Probably?!"
    show s1b66 with dissolve
    mc "You’re enjoying this way too much."
    mc "Who are you?"
    show s1b67 with dissolve
    Fl "Flora, you?"
    show s1b66 with dissolve
    mc "[mc]."
    mc "Can’t say I’m glad to meet you."
    show s1b71 with dissolve
    Fl "Yeah-yeah… tweak this… recalibrate that…"
    mc "What did you— ah!"
    Fl "Hey... don’t move."
    Fl "Unless you’re planning to lose that eye."
    pause 1.1
    Fl "And..."
    play sounds4 cliccface
    show s1b72 with dissolve
    Fl "Done."
    Fl "Vitals holding. For now."
    #sound
    show s1b77 with dissolve
    mc "Feels... a little better. I think."
    play sounds2 clothess
    show s1b78 with dissolve
    Fl "You’re tougher than you look."
    mc "What did you just do?"
    play sounds2 clench
    show s1b79 with dissolve
    Fl "Finished my father’s work."
    Fl "And maybe soften that tone."
    Fl "I just made your life a lot easier."
    show s1b80 with dissolve 
    Fl "And you."
    Fl "Quick tip, learn to hide that look."
    Fl "Trouble tends to notice it before you do."
    mc "Wait, your father?"
    play sounds1 footstep volume 2.0 
    show s1b81 with dissolve
    Fl "Until next time. Try not to die. That would ruin my metrics."
    show s1b82 with dissolve
    h "…Yeah."
    h "She’s weird."
    h "And annoying."
    show s1b83 with dissolve
    mc "Still… she helped."
    mc "I just don’t get it—"
    scene s1b84 with dissolve
    mc "(…Still hurts.)"
    pause 0.8
    mc "(And the father… that beastman?)"

    show s1pp90 with dreamyzoom 
    show memoryframe with dissolve 
    o "If it gets worse, find me."
    mc "(Too friendly.)"

    mc "(Same as before.)"
    
    scene s1b84 with dissolve
    pause 1.0
    show s1b85 with dissolve
    h "..."
    show s1b86 with dissolve
    h "How’s the pain?"
    h "Still bad?"
    show s1b87 with dissolve
    mc "Manageable. But her grip... it’s terrifying."
    mc "How’ve you been holding up?"
    scene s1bb1 with dissolve
    h "...I managed."
    pause 1.1
    h "Somehow."
    # scene s1bb2 with dissolve
    scene s1bb5 with dissolve
    h "Past two months?"
    h "Barely slept."
    h "Ran on coffee… and spite."
    scene s1bb7 with dissolve
    mc "Wait. I was unconscious for two whole months? You’ve got to be kidding me..."
    scene s1bb8 with dissolve
    h "..."
    scene s1bb9 with dissolve
    h "…Yeah."
    h "And you know what?"
    h "I suddenly feel like punching you again."
    scene s1bb10 with dissolve
    h "..."
    scene s1bb12 with dissolve
    h "...You were out for two months."
    h "And they were the worst months of my life."
    h "Every day... same thought."
    h "That you were gone."
    h "And the doctors?"
    h "Didn’t exactly help."
    h "When I saw you like that…"

    scene s1bb13 with dissolve
    pause 0.5
    scene s1bb14 with dissolve
    pause 0.5
    scene s1bb16 with dissolve
    pause 0.5
    scene s1bb19 with dissolve
    h "..."
    scene s1bb20 with dissolve
    h "I felt like I was all alone here, in an unfamiliar place, without family or anyone close to me."
    h "A void started growing inside me..."
    scene s1bb19 with dissolve
    h "..."
    scene s1bb20 with dissolve
    h "But coming to see you every day, watching your condition improve little by little, gave me hope."
    scene s1bb21 with dissolve
    mc "If not for you…"
    mc "Yeah. That wouldn’t have ended well."
    mc "…Thank you."
    scene s1bb22 with dissolve
    h "..."
    scene s1bb26 with dissolve
    scene s1bb27 with dissolve
    mc "Something wrong?"
    scene s1bb28 with dissolve
    pause 0.5
    scene s1bb29 with dissolve
    h "You’ve changed... Your eyes, they..."
    scene s1bb32 with dissolve
    pause 0.5
    scene s1bb31 with dissolve
    h "...Wait."
    h "No way…"
    h "You can see with your left eye again?"
    mc "..."
    mc "Didn’t think I’d see out of it again."
    mc "But… yeah."
    scene s1bb33 with dissolve
    h "That’s… good."
    pause 1.1
    h "Really good."
    scene s1bb31 with dissolve
    h "(quietly) …but that eye…"
    mc "Hm?"
    h "(quietly) No. Forget it. Just my imagination."
    scene s1bb22 with dissolve
    pause 1.1
    h "Sit."
    h "...We’ve still got time."
    play sounds4 whoosh
    scene s1bb34 with CropMove(time=0.1, mode='slideleft')
    h "While you were out…"
    h "I tried to piece together what happened."
    scene s1bb36 with dissolve

define firstanswer = 0
define whatplaceisit = False
define boards = False
define factions = True
define factions1 = True
define arrangements = False
define blood = True
define races = False
define races1 = False
define memtd = True
define memtd1 = False

label firstanswer:

    menu:
        "Where are we?" if whatplaceisit == False:
            $ firstanswer += 1
            $ whatplaceisit = True
            scene s1bb37 with dissolve
            mc "Ships hanging in the sky..."
            mc "People who don’t look human."
            mc "Tell me, Olivia, this isn’t Earth, is it?"
            scene s1bb38 with dissolve
            h "Yeah. We’re way past Earth."
            h "I checked."
            pause 0.5
            h "Archives, logs… whatever I could get my hands on."
            pause 0.5
            h "Just fragments. Nothing solid."
            scene s1bb37 with dissolve
            mc "Nothing at all?"
            scene s1bb38 with dissolve
            h "There’s some kind of Inquisition."
            h "They lock everything down."
            h "Total blackout."
            scene s1bb37 with dissolve
            mc "How does that even work?"
            scene s1bb38 with dissolve
            h "I don’t know…"
            scene s1bb37 with dissolve
            mc "What about this place itself?"
            scene s1bb38 with dissolve
            h "Not much better there either."
            h "Half of this place still doesn’t make sense to me."
            h "Language’s different."
            h "Completely."
            h "I spent a month and a half with Miriel just trying to not sound like an idiot."
            scene s1bb38 with dissolve
            h "And even then… here’s what I’ve got:"
            h "Some ‘Lady’ running the place."
            h "An Inquisition breathing down everyone’s neck."
            h "And us?"
            h "Somewhere in the ass-end of the galaxy."
            h "That’s it."
            
            if factions1 == True:
                $ factions = False
            jump firstanswer

        "How long was I out?" if races == False:
            $ firstanswer += 1
            $ races = True
            scene s1bb37 with dissolve
            mc "Two months out cold..."
            scene s1bb38 with dissolve
            h "Out?"
            h "You don’t get it."
            h "You were dead, [mc]."
            h "Dead."           
            scene s1bb37 with dissolve
            mc "What are you talking about..."
            scene s1bb38 with dissolve
            h "When you got thrown back…"
            pause 0.7
            h "Your heart just... {w=0.5}gave out."
            scene s1bb37 with dissolve
            mc "And I’m alive…"
            mc "Somehow."
            scene s1bb38 with dissolve
            h "Those two scientists dragged you back."
            h "That’s all I know, alright?"
            pause 
            h "And... you’re sitting right here in front of me, that’s what matters."
            scene s1bb37 with dissolve
            mc "Dead... huh."
            pause 1.1
            mc "How did you deal with that?"
            scene s1bb38 with dissolve
            h "Badly."
            h "Trying to understand this place…"
            h "Trying not to lose it."
            h "Still working on that, honestly."
            h "Alone."
            h "Completely."
            h "If it wasn’t for Miriel…"
            h "I would’ve snapped."
            scene s1bb37 with dissolve
            mc "Miriel? What about her?"
            scene s1bb38 with dissolve
            h "For some reason, she’s started looking after me."
            h "Maybe it has to do with her past. I don’t know. But she helped me adapt here, and for that, I’m grateful."
            scene s1bb36 with dissolve
            $ races1 = True
            jump firstanswer

        "What happened to the others?" if boards == False:
            $ firstanswer += 1
            $ boards = True
            scene s1bb37 with dissolve
            mc "My son."
            mc "Is he alive?"
            scene s1bb38 with dissolve
            h "Norman… that’s complicated."
            h "I could visit you."
            h "Him? Nothing."
            h "I tried."
            h "Over and over."
            h "No access. No trace."
            scene s1bb37 with dissolve
            mc "And the others...?"
            scene s1bb38 with dissolve
            h "I can’t help you there."
            h "I already feel like crap for thinking we abandoned everyone..."
            scene s1bb36 with dissolve
            mc "..."
            if factions1 == True:
                $ factions = False
            jump firstanswer     

        "Why did they save me?" if arrangements == False:
            $ firstanswer += 1
            $ arrangements = True
            scene s1bb37 with dissolve
            mc "Why keep us alive?"
            scene s1bb38 with dissolve
            h "Because of you."
            pause 0.6
            h "And I don’t like it."
            scene s1bb37 with dissolve
            mc "Why?"
            scene s1bb38 with dissolve
            h "Because I don’t know what they want from you."
            scene s1bb37 with dissolve
            mc "...Are you serious?"
            scene s1bb38 with dissolve
            h "Dead serious. And they are too."
            h "We’re alive because of you."
            pause 0.6
            h "And that should worry you."
            scene s1bb37 with dissolve
            mc "This doesn’t add up."
            scene s1bb38 with dissolve
            h "I told you."
            h "Nothing here makes sense."
            scene s1bb36 with dissolve

            $ blood = False
            $ memtd = False

            jump firstanswer

        "I think… I’ve learned enough for now." if firstanswer >= 2:
            jump firstanswernext

label firstanswernext:
    $ persistent.chapter_act1_scene += 1
    $ persistent.ancient_blood_ = True 

    play sounds1 footstep volume 2.0 
    show s1bb35 with dissolve
    Mi "Time’s up. Let’s move."

    stop sound
    stop music fadeout 3.0

    play music zargo fadein 3.0
    scene black with dissolve
    pause 3.0

    image miriel = Movie(channel="movie_dp", loop = False, play="video/Miriel.webm")
    show miriel with dissolve
    $ renpy.pause(4.1, hard=True)


    play sound towerambient fadein 1.0 loop volume 0.4
    scene s1b93 with dissolve
    Mi "We’re here. Wait while I get clearance."
    play sounds1 footstep volume 2.0
    show s1b94 with dissolve
    Mi "And don’t get clever."
    Mi "No wandering. {w=0.2}No talking to ghosts. {w=0.2}No pressing random buttons."
    play sounds2 rustling2
    show s1b95 with dissolve
    mc "Ghosts? Define 'clever.'"
    show s1b96 with dissolve
    Mi "We once had a man strip naked… walk into the Madam’s office… and detonate."
    Mi "Very clever."
    Mi "So sit tight."
    Mi "And try to keep all your limbs attached."
    show s1b98 with dissolve
    Mi "I’ve brought the subject for the Madam."
    Mi "Why is access blocked?"
    g "New directive. No entries authorized until said otherwise. No further details provided."
    mc "(These guys look big… but only three?)"
    mc "(Or just the ones I can see…?)"
    mc "(No... wait. Why would she even need guards if she can see the future?)"
    show s1b97 with dissolve
    Mi "Who issued the directive?"
    mc "(Or is this just for show?)"
    pause 1.1
    mc "(Doesn’t matter. She sees the future? Good.)"
    mc "(Makes getting answers easier.)"

    scene s1b98 with dissolve
    g "I can't disclose who sent the order. The intel is above my level."
    Mi "When did it come in?"
    g "Seconds before your departure."
    
    show s1b106 with dissolve
    Mi "…Understood. We’ll wait here."
    show s1b107 with dissolve
    Mi "Change of plans."
    Mi "We wait."
    play sounds2 rustling2
    show s1b108 with dissolve
    mc "Something wrong?"
    show s1b110 with dissolve
    h "Nothing new. She’s just impossible to reach. Took me a full day just to get a five-minute audience."
    show s1b111 with dissolve
    mc "So... any advice before I walk into the lion’s den? Rules? Forbidden gestures?"
    scene s1b110 with dissolve
    h "She’s not a tyrant. Just don’t try too hard. Be honest. And whatever you do... don’t fake being smart. She hates that."
    scene s1b111 with dissolve
    mc "Noted. Anything else?"
    scene s1b110 with dissolve
    h "Her eyes."
    scene s1b111 with dissolve
    mc "Her eyes?"
    scene s1b110 with dissolve
    h "She looks at you like she already knows the ending. And she's just waiting to see if you'll catch up."
    show s1b112 with dissolve
    Mi "Avoid staring too long. It’s... unsettling."
    Mi "Might melt your brain."
    show s1b115 with dissolve
    b "Melt what?"
    show s1b113 with dissolve
    Mi "…Kidding."
    show s1b113 with dissolve
    mc "..."
    mc "(I hope it's really a joke. But something tells me not to test it.)"  # 20 tho  
    show s1b117 with dissolve
    play sounds2 radio loop volume 0.2
    g "Command, they’ve arrived. Three individuals. Awaiting entry."
    g "Only man?"
    g "Confirmed."
    stop sounds2
    show s1b119 with dissolve
    g "The Madam will see him now."
    play sounds1 footstep volume 2.0
    show s1b120 with dissolve
    mc "Time to get some answers."
    show s1b121 with dissolve
    h "And one more thing. {b}Don’t{/b} mention your past."
    h "Be careful in there, seriously."
    show s1b122 with dissolve
    mc "Got it."
    play sounds1 footstep volume 2.0
    show s1b123 with dissolve
    g "That door. Straight ahead."
    if Ostorius_help == True:
        show s1b124 with dissolve
        g "One more thing — word came down about what you did for Ostorius."
        show s1b125 with dissolve
        g "That sort of loyalty? We don’t forget it."
        show s1b126 with dissolve
        g "Thanks for honoring the old man’s request. You’ve earned some respect here."
        play sounds1 dooropen1 volume 2.0
        show s1b127 with dissolve
        mc "...Thanks. I think."
        mc "(But how the hell did they {b}know{/b}?)"
         
    show s1b128 with dissolve
    g "May Aldarion watch over you."
    stop sound 
    stop sounds1 
    stop sounds2
    stop music fadeout 1.0  

    play music1 astoria1 fadein 2.0

    scene s1b129 with dissolve
    a "We've tried all frequencies. No response."

    window hide
    image firstemeeting = Movie(channel="movie_dp", loop = False, play="video/firstmeeting.webm")
    show firstemeeting with dissolve
    $ renpy.pause(11.1, hard=True)

    show s1b131 with dissolve
    lad "Three days of silence. Not a whisper. Not a trace."
    show s1b132 with dissolve
    a "Last ping, then nothing. Like they were swallowed."
    show s1b135 with dissolve
    mc "..."
    show s1b136 with dissolve
    lad "Hmm..."
    show s1b137 with dissolve
    
    lad "Subject-378."
    lad "The last breath of a failed experiment."
    lad "Let’s see…"
    pause 1.1
    lad "How long you last this time."
    scene s1b138 with dissolve
    pause 0.5
    scene s1b139 with dissolve
    pause 0.5
    scene s1b140 with dissolve
    pause 0.5
    scene s1b141 with dissolve
    pause 0.5
    show s1b142 with dissolve
    lad "Tell me young man… why are you here?"
    scene s1b140 with dissolve
    mc "..."
    mc "(‘Young man’?)"
    scene s1b142 with dissolve
    lad "I asked you a question."
    show s1b133 with dissolve
    mc "You tell me."
    scene s1b140 with dissolve
    pause 0.5
    scene s1b141 with dissolve
    pause 0.5
    lad "Hm..."
    scene s1b142 with dissolve
    lad "Answer me."
    lad "Do you believe in fate?"
    scene s1b142 with dissolve
    lad "Or are you still naive enough to think you have a choice?"
    scene s1b133 with dissolve
    mc "Is there a point to this?"
    mc "What exactly do you want to hear?"
    show s1b143 with dissolve
    lad "Hmm..."
    show s1b144 with dissolve
    lad "Hear? Nothing."
    lad "But seeing... that's different."
    lad "Now tell me, why are you here?"
    scene s1b138 with dissolve
    menu:
        "You brought me here. Maybe you should be the one telling me?": 
            $ mc_status += 1
            show s1b133 with dissolve
            mc "You brought me here."
            mc "Maybe you should be the one answering that."
            show s1b145 with dissolve
            lad "..."
            show s1b146 with dissolve
            lad "Maybe."
            lad "Or maybe you already know."
            lad "You just haven’t realized it yet."
            scene s1b145 with dissolve
            pause 1.4
            scene s1b146 with dissolve
            lad "Why did your group enter the ship?"
            scene s1b145 with dissolve  
            

        "I don’t know. I was dragged here.":
            $ mc_status -= 2
            show s1b149 with dissolve
            mc "I don’t know. You’re the ones who dragged me here."
            show s1b138 with dissolve
            show s1b139 with dissolve
            show s1b140 with dissolve
            show s1b141 with dissolve
            show s1b142 with dissolve
            lad "You don’t know?"
            lad "Then you didn’t try to understand."
            lad "And those who don’t try… are worse than traitors."
            scene s1b145 with dissolve
            pause 1.4
            show s1b144 with dissolve
            lad "Let’s not waste time. Why did your group enter the ship?"
            scene s1b138 with dissolve

        "Something on that ship chose me.": 
            $ mc_status += 1
            show s1b133 with dissolve
            mc "Something on that ship chose me."
            show s1b145 with dissolve
            lad "..."
            show s1b146 with dissolve
            lad "There."
            lad "That’s your answer."
            scene s1b145 with dissolve
            pause 1.4
            scene s1b146 with dissolve
            lad "Why did your group enter the ship?"
            scene s1b145 with dissolve  

        "...":
            show s1b155 with dissolve
            mc "..."
            mc "(Let her talk.)"
            scene s1b138 with dissolve
            lad "..."
            show s1b144 with dissolve
            lad "Silence is an answer."
            lad "I don’t like that one."
            scene s1b145 with dissolve
            pause 1.4
            scene s1b144 with dissolve
            lad "Why did your group enter the ship?"
            scene s1b145 with dissolve

    menu:
        "We were sent to find out more.":
            $ mc_status += 2
            scene s1b133 with dissolve
            mc "We were sent to gather intel."
            mc "All we had was a crash date and coordinates."
            show s1b153 with dissolve
            lad "..."
            show s1b154 with dissolve
            lad "I know."
            scene s1b133 with dissolve
            mc "You know?"
            mc "Then why—"
            mc "…A test."
            show s1b154 with dissolve
            lad "Tell me…"
            lad "What did the ship whisper to you, once you stepped inside?"
            scene s1b153 with dissolve

        "I was looking for information about my wife...":
            $ mc_status += 1
            show s1b148 with dissolve
            mc "My wife… every lead pointed to that ship."
            show s1b152 with dissolve
            lad "..."
            show s1b151 with dissolve
            lad "Your wife…"
            pause
            lad "Personal motives make people predictable."
            lad "What did you see in there — that made your blood turn cold?"
            scene s1b152 with dissolve

        "We were told the ship held a weapon so powerful it could destroy entire worlds.":
            $ mc_status -= 1
            show s1b148 with dissolve
            mc "We were told the ship held a weapon so powerful it could destroy entire worlds."
            show s1b152 with dissolve
            lad "..."
            show s1b151 with dissolve
            lad "A lie."
            lad "What did you see in there — that made your blood turn cold?"
            scene s1b152 with dissolve

        "I don't know anything about that.":
            $ mc_status += 1
            scene s1b148 with dissolve
            mc "Orders."
            mc "That’s all we had."
            show s1b153 with dissolve
            lad "..."
            show s1b154 with dissolve
            lad "Blind loyalty. I’ve seen corpses with more conviction."
            lad "Very well. What did the ship whisper to you, once you stepped inside?"
            scene s1b153 with dissolve

    menu:

        "The ship was quiet.":
            $ mc_status += 1
            scene s1b133 with dissolve
            mc "Ships like that don’t exist where I’m from."
            mc "And still… it was silent."
            mc "Too silent."
            mc "That silence was worse than anything else."
            scene s1b152 with dissolve
            lad "..." 
            scene s1b151 with dissolve
            lad "I see."
            scene s1b152 with dissolve

        "There were definitely a few moments.":
            $ mc_status += 2
            scene s1b156 with dissolve
            mc "There were moments… something felt off."
            mc "Doors sealed shut. Machines torn apart."
            mc "The dead… didn’t stay dead."
            mc "But the worst part…"
            mc "Time."
            mc "The deeper we went, the less sense it made."
            scene s1b152 with dissolve
            lad "Hmm...."
            scene s1b151 with dissolve
            lad "It’s an anomaly."
            lad "You felt it, didn’t you?"
            lad "Something that doesn’t belong to your time."

        "The ship itself was practically screaming about the danger":
            $ mc_status += 3
            scene s1b149 with dissolve
            mc "With all due respect… the ship didn’t need to whisper."
            mc "It was screaming."
            scene s1b152 with dissolve
            lad "..."
            scene s1b151 with dissolve
            lad "...I see."
            lad "Then let me ask a better question."
            lad "What felt... {b}wrong{/b}, to you? Not just foreign. Wrong."
            scene s1b155 with dissolve
            mc "..."
            scene s1b156 with dissolve
            mc "The corpses. The machines."
            mc "Even the walls… felt alive."
            mc "None of it belonged to our world."
            scene s1b151 with dissolve
            lad "Then perhaps the ship didn’t crash."
            scene s1b152 with dissolve
            mc "...What?"
            scene s1b151 with dissolve
            lad "It was hidden."
            scene s1b157 with dissolve
            lad "..."

    stop music1 fadeout 2.0

    # if mc_status >= 15:
        
    show s1b163 with dissolve
    lad "..."
    
    scene s1b162 with dissolve
    lad "That’s enough."
    lad "One last question."
    scene s1b163 with dissolve
    pause 0.5
    play sounds1 boom3
    scene s1b162 with dissolve
    lad "Tell me."
    lad "What do you know about your wife?"
    play music astoria2 fadein 1.5
    scene s1b190 with dissolve
    mc "Lora? What do you know about her?" 
    mc "Where is she? Is she alive?! {w=1.5}I need to know, is my wife okay?!"
    scene s1b162 with dissolve
    lad "Enough."
    lad "Desperation doesn't suit you. It's too loud. Too brittle."
    scene s1b192 with dissolve
    mc "(Damn it, pull yourself together, [mc]. She can smell cracks in the armor...)"
    scene s1b193 with dissolve
    pause 0.5
    scene s1b194 with dissolve
    mc "…Won’t happen again."
    scene s1b163 with dissolve
    lad "..."
    scene s1b162 with dissolve
    lad "She’s here."
    lad "Alive."
    scene s1b156 with dissolve
    mc "...She made it this far?"
    scene s1b162 with dissolve
    lad "Apparently."
    lad "Whether by choice… is another question."
    scene s1b156 with dissolve
    mc "Explain."
    scene s1b162 with dissolve
    lad "She was like you."
    lad "She survived contact with something she shouldn't have."
    lad "It changed her."
    scene s1b156 with dissolve
    mc "Changed...?"
    scene s1b165 with dissolve
    lad "There was a connection inside her."
    lad "A path out of this world."
    scene s1b156 with dissolve
    mc "Why {b}was{/b}?"
    scene s1b165 with dissolve
    lad "Find a way out."
    lad "Then we’ll talk."
    scene s1b155 with dissolve
    mc "(She’s telling me more than before... And it looks like I’m more valuable to them than they are to me.)"
    scene s1b156 with dissolve
    mc "I understand why you need me."
    mc "Now tell me, why would I ever need you?"
    scene s1b163 with dissolve
    lad "..."
    scene s1b165 with dissolve
    lad "I don’t need you."
    lad "You need a reason to survive."
    scene s1b156 with dissolve
    mc "...What about Norman?"
    mc "No riddles."
    scene s1b165 with dissolve
    lad "He’s dead."
    pause 1.2
    scene s1b163 with dissolve
    mc "But-"
    mc "...No."
    pause 0.8
    mc "No. That’s not—"
    scene s1b165 with dissolve
    lad "He’s gone."
    lad "Completely."
    scene s1b155 with dissolve
    mc "..."
    scene s1b165 with dissolve
    lad "No dramatics. {w}You asked. {w}I answered." 
    lad "Mourn later — if you survive."
    play sounds1 dooropen1 volume 2.0
    scene s1b167 with dissolve
    lad "..."
    y "That was unusually... generous of you. You’ve always preferred silence to sympathy."
    scene s1b168 with dissolve
    lad "Even silence has a rhythm."
    lad "Sometimes, a single note must be played to break the pattern."
    play sound glitchfear volume 0.3
    scene s1b169 with glitch
    y "Do you regret telling him?"
    scene s1b172 with dissolve
    lad "This isn’t the first time he’s heard it."
    
    $ mcmeety = True
    scene s1b166 with dissolve
    a "Understood."
    lad "(The difference is… whether he can break it this time.)"
    stop music fadeout 3.0
    y "..."
    y "You saw it too, didn’t you?"
    scene s1b174 with dissolve
    a "Saw what?"
    scene s1b201 with dissolve
    lad "(The path changed.)"
    pause 1.1
    
    
    

    image asmodei1 = Movie(channel="movie_dp", loop = False, play="video/asmodei1.webm")
    show asmodei1 with dissolve
    $ renpy.pause(11.1, hard=True)

    jump norman

label norman:
    play music undertow fadein 1.9
    scene norman1 with dissolve
    mc "(So… it wasn’t a dream.)"



    mc "(Norman.)"
    show norman5 with dissolve  
    mc "(This silence… it’s real.)"
    scene norman6 with dissolve  
    pause 0.5  
    play sounds wallcrash
    scene norman7 with dissolve  
    pause 0.5  
    show norman8 with dissolve  
    mc "(All this time… I kept looking back.)"
    mc "(Chasing ghosts… instead of what was right in front of me.)"
    show norman9 with dissolve  
    mc "(And now you’re one of them.)"
    show norman10 with dissolve  
    mc "(Funny…)"
    mc "(The life with him... I took it for granted... Until he was gone.)"
    pause 1.1
    mc "(I didn’t see this coming.)"
    mc "(Not until it slipped through my hands.)"
    show norman11 with dissolve  
    mc "I’m sorry, Norman."
    mc "I failed you."
    show norman12 with dissolve  
    mc "(Wherever you are…)"
    mc "(I hope it’s far from here.)"
    pause 1.1
    mc "(…And me.)"
    mc "(I’m not done yet.)"
    show norman13 with dissolve  
    mc "Get it together."
    mc "This isn’t over."
    show norman14 with dissolve  
    mc "(I won’t look away again.)"
    mc "(Not this time.)"
    pause 1.1
    mc "(…No matter what it costs.)"
    stop music fadeout 3.2

# Часть 2
    scene black with dissolve
    pause 3.0
    show act1s1_1 with dissolve
    pause 1.5
    show act1s1_2 with dissolve
    pause 1.5

label norman_1:
    scene black with dissolve 
    "A few hours later. On the roof."
    pause 1.0
    play sounds1 windcyb fadein 5.0 loop volume 0.8
    play music1 season4act12 fadein 5.4 
    scene s1rew1 with dissolve 
    pause 1.8
    mc "…Yeah."
    mc "(Still not used to this.)"
    play sounds3 smoke
    scene s1rew3 with dissolve 
    pause 1.1
    scene s1rew4 with dissolve 
    pause 1.1
    scene s1rew5 with dissolve 
    pause 0.6
    mc "(A path out of this world…?)"
    scene ch 175 with dreamyzoom
    show memoryframe with dissolve     
    N "It wasn’t my choice… I was led there."     

    scene s1rew5 with dissolve 
    pause 0.6
    play sounds3 smoke
    scene s1rew3 with dissolve 
    pause 1.1
    scene s1rew4 with dissolve 
    pause 1.1
    scene s1rew5 with dissolve 
    pause 0.6

    scene s1b156 with dissolve
    show memoryframe with dissolve     
    mc "...She made it this far?"         
    scene s1b162 with dissolve      
    show memoryframe with dissolve        
    lad "Apparently."         
    lad "Whether by choice… is another question."

    scene s1rew5 with dissolve 
    pause 0.6
    play sounds3 smoke
    scene s1rew3 with dissolve 
    pause 1.1
    scene s1rew5 with dissolve 
    mc "(She was led here…?)"
    scene s1rew4 with dissolve 
    pause 1.1
    mc "(…Of course.)"
    scene s1rew5 with dissolve 
    mc "..."
    mc "(What’s next…)"
    play sounds2 closedoor
    h "So this is where you—"
    h "Hey!"
    
    play sounds2 mmove 
    scene s1rew7 with dissolve 
    h "You quit, remember?"
    scene s1rew6 with dissolve 
    h "..."
    scene s1rew5 with dissolve 
    mc "..."
    play sounds3 smoke
    scene s1rew3 with dissolve 
    pause 1.1
    scene s1rew8 with dissolve 
    h "Alright. Talk."
    h "What happened?"
    scene s1rew6 with dissolve 
    mc "What are you doing here?"
    scene s1rew7 with dissolve 
    h "I was looking for you."
    h "You disappeared after that meeting like you fell off the map."
    h "I tore half the place apart before I found you…"
    h "...brooding up here alone."
    scene s1rew5 with dissolve 
    h "So come on."
    h "What’s eating you?"
    play sounds3 smoke
    scene s1rew3 with dissolve 
    pause 1.1
    scene s1rew4 with dissolve 
    pause 1.1
    scene s1rew5 with dissolve 
    pause 0.6
    mc "Norman’s dead."
    h "..."
    scene s1rew8 with dissolve 
    h "...I’m sorry."
    scene s1rew6 with dissolve 
    mc "Why are you apologizing?"
    scene s1rew7 with dissolve 
    h "If it wasn’t for me, he—"
    play sounds3 smoke
    scene s1rew3 with dissolve 
    pause 1.1
    scene s1rew4 with dissolve 
    pause 1.1
    scene s1rew5 with dissolve 
    pause 0.6
    mc "It’s not your fault."
    h "I can see it in your eyes—"
    pause 0.7
    mc "(Enough.)"
    
    mc "(…I said I wouldn’t look away.)"
    mc "(So why can’t I let it go—)"
    mc "(…No. Not now.)"
    scene s1rew10 with dissolve 
    mc "Nice view, huh?"
    pause 1.1 
    h "..."
    scene s1rew9 with dissolve 
    h "...Yeah."
    pause 1.5
    mc "(I’ve buried so many…)"
    mc "(So why…)"
    play sounds2 mmove 
    scene s1rew11 with dissolve 
    mc "(Why can’t I let this go…?)"
    h "..."
    scene s1rew12 with dissolve 
    mc "(No… get it together.)"
    play sounds2 hug2 
    scene s1rew13 with dissolve 
    pause 1.9
    h "You did everything you could."
    play sounds3 mmove 
    scene s1rew14 with dissolve 
    h "And I’m pretty sure he wouldn’t want to see you like this."
    h "So stop."
    h "You hear me?"
    play sounds2 clench 
    scene s1rew18 with dissolve 
    pause 1.1 
    scene s1rew16 with dissolve 
    pause 1.9
    scene s1rew17 with dissolve 
    h "Stop blaming yourself."
    scene s1rew18 with dissolve 
    pause 1.9
    mc "…Thanks."
    scene s1rew15 with dissolve 
    pause 1.1
    scene s1rew14 with dissolve 
    h "We’re a team."
    h "Remember?"
    play sounds3 mmove 
    scene s1rew15 with dissolve 
    pause 1.5
    play sounds4 rustling2  
    scene s1rew19 with dissolve 
    mc "Yeah…"
    mc "Grown man… and I’m falling apart."
    scene s1rew20 with dissolve 
    h "So what?"
    h "Old man not allowed to fall apart now?"
    h "That’s bullshit."
    scene s1rew19 with dissolve 
    mc "...Old man, huh?"
    scene s1rew20 with dissolve 
    h "Listen."
    h "If anyone ever tells you that crap…"
    h "Spit in their face."
    h "Full force."
    scene s1rew19 with dissolve 
    mc "…I’ll remember that."
    scene s1rew21 with dissolve 
    pause 4.3
    show 7yr with dissolve 
    "Several minutes pass."
    hide 7yr
    mc "(…Quieter.)"
    pause 1.8
    mc "Liv?"
    h "Hm?"
    mc "One of the beastmen wanted to see me."
    scene s1rew22 with dissolve 
    h "Beastman?"
    mc "Ostorius. I think."
    scene s1rew23 with dissolve 
    mc "You know where I can find him?"

    stop music1 fadeout 3.3
    stop sounds1 fadeout 1.2
    scene black with dissolve 
    play sound systemambience fadein 3.0 loop volume 0.8
    pause 3.4
    play sounds2 scifidooropen2
    scene s1rew25 with dissolve 
    pause 1.5
    play sounds2 footstep2 
    scene s1rew24 with dissolve 
    h "...Yeah, this looks like a torture room."
    h "You sure we’re in the right place?"
    mc "You know any other implant labs?"
    h "Didn’t think so."
    scene s1rew27 with dissolve 
    pause 1.2
    scene s1rew26 with dissolve 
    h "Alright… so why do you need him?"
    h "Because of your eye?"
    h "Speaking of, how bad is it?"
    scene s1rew27 with dissolve 
    pause 1.2
    scene s1rew28 with dissolve 
    mc "I’ve had worse."
    h "And the Lady?"
    h "What did she tell you?"
    scene s1rew24 with dissolve 
    mc "She knows about Lora."
    h "...Then we’re in the right place?"
    scene s1rew27 with dissolve 
    mc "Yeah."
    scene s1rew26 with dissolve 
    h "And… that’s it?"
    scene s1rew28 with dissolve 
    mc "That’s all I’m sure of."
    mc "(Lora is alive. She worked in a tomb outside the city.)"
    mc "(If I want answers, I need access to those tombs—and someone who knows the routes.)"
    play sounds1 dronescan fadein 2.0 loop
    scene s1rew29 with dissolve 
    mc "The rest… I’m not sure I can trust it."
    mc "(What the hell…)"
    scene s1rew30 with dissolve 
    ss "Authorizing..."
    ss "Authorization successful."
    play sounds1 systemnotification 
    scene s1rew31 with dissolve 
    ss "What the hell are you doing here?"
    h "…Okay, what is that?"
    mc "Ostorius… here?"
    scene s1rew32 with dissolve 
    ss "Beep-beep. Visitors for Father? Please wait."
    mc "(Father?..)"
    play music floramoment fadein 5.4 
    scene s1rew33 with dissolve 
    pause 1.5
    play sounds4 whoosh
    scene s1rew305 with CropMove(time=0.1, mode='slideleft')
    pause 1.5
    play sounds3 whoosh
    scene s1rew306 with CropMove(time=0.1, mode='slideup')
    Fl "Yo. Fluffy. What do you want?"
    ss "Flora! Two individuals have come to see Father."
    play sounds3 whoosh
    scene s1rew307  
    Fl "Huh? Guests? For father?"
    ss "Yes! He didn’t mention anything, but I reviewed his report."
    play sounds2 systemnotification
    ss "O-O-O-O1... System rebooting."
    play sounds2 systemnotification
    play sounds3 whoosh
    scene s1rew309 with CropMove(time=0.1, mode='slideleft')
    o "Sweetheart, can you hear me? Come in, come in!"
    play sounds2 mouseclick 
    play sounds3 flamethrower
    scene s1rew308 with vpunch 
    o "I just caught a glimpse, looks like we’ve got guests. Can you believe that?"
    o "Be a dear and keep an eye on them for me, alright? They’re important."
    stop sounds3 fadeout 0.5
    play sounds4 whoosh
    scene s1rew310 
    Fl "What? No."
    Fl "I’ve got classes, dad. And where are you?"
    play sounds3 whoosh
    scene s1rew35 with CropMove(time=0.1, mode='slideleft')
    o "Ah, just dealing with the Inquisition. You know, routine stuff!"
    o "So I’m counting on my amazing, brilliant daughter, the best mechanic in the whole city!"
    o "Show them how things are done, yeah?"
    play sounds2 systemnotification
    scene s1rew36 with dissolve 
    Fl "Fine. But you owe me. Big time."
    o "Oh, absolutely! Dinner, a day off, your call!"
    o "Thanks, kiddo. You’re saving me again."
    scene s1rew37 with dissolve 
    mc "('Implant lab.' Right.)"
    Fl "Hey, what are you standing around for? Get in."
    play sounds3 whoosh
    scene s1rew38 with CropMove(time=0.1, mode='slideright')
    Fl "Well, well… look what walked in."
    h "Yeah, I’d take literally anywhere else over this."
    play sounds4 whoosh
    scene s1rew39 with CropMove(time=0.1, mode='slideleft')
    pause 1.6
    play sounds3 whoosh
    scene s1rew40 with CropMove(time=0.1, mode='slideright')
    Fl "Heh. Then leave. No one’s stopping you."
    Fl "Now… last touches."



    
    play sounds3 whoosh
    scene s1rew41 with dissolve 
    pause 1.1
    stop music fadeout 0.5
    play sounds2 hug2 
    scene s1rew42 with vpunch 
    Fl "And here it is, the one and only Reassembler 4000."
    Fl "And me, the best mechanic in the entire Federation. You’re welcome."
    scene s1rew44 with dissolve 
    h "Best mechanic?"
    h "At talking, maybe."
    scene s1rew43 with dissolve 
    mc "Olivia, enough."
    Fl "Careful. You’re getting a little bold for someone on my table—"
    mc "Flora, right?"
    mc "I’ll keep it simple. We’re here on business."
    mc "Can you help, or not?"
    Fl "..."
    play sounds2 mmove 
    scene s1rew45 with dissolve 
    Fl "Your augmentative system is running unstable."
    mc "Augment— what?"
    Fl "Augmentative system."
    Fl "That little thing keeping your brain from frying itself while synced with implants."
    play sounds3 mmove 
    scene s1rew46 with dissolve 
    mc "That’s not what I was told."
    mc "They said compatibility was… exceptional."
    Fl "And that’s exactly where the difference is."
    Fl "Body rejection and neural sync are not the same thing."
    Fl "First one? Your body stops being yours."
    Fl "Second?"
    Fl "You start seeing things."
    pause 1.1
    h "The hell do you mean ‘seeing things’?"
    scene s1rew47 with dissolve 
    Fl "Literally."
    Fl "You see what you don’t understand. Hear what you’re not supposed to."
    Fl "Pretty standard when your implants are… let’s say, not exactly cutting-edge."
    play sounds1 dronescan fadein 2.0 loop
    scene s1rew48 with dissolve 
    h "Wait! Hold on."
    h "You’re telling me he got patched together from scrap?"
    ss "Analyzing... Analysis complete."
    ss "Classification: Experimental subject  378."
    stop sounds1 fadeout 0.5
    scene s1rew48 
    mc "(Subject-378?)"
    
    play sounds1 glitchfear
    play music1 astoriamain fadein 1.1
    scene s1rew120 with glitch
    aa "-Ark..."
    scene s1rew123 with glitch
    aaa "We must—"
    scene s1rew121 with glitch
    aa "...unanimously."
    mc "(What the—)"
    scene s1rew122 with dissolve
    pause 1.5
    scene s1rew311
    pause 0.8
    scene s1rew312
    pause 0.8
    play sounds1 glitchfear
    scene s1rew48 with glitch 
    a "(The Ark… that’s where all the answers are.)"
    scene s1rew49 with dissolve 
    pause 1.1
    play sounds2 fall 
    stop music1 fadeout 0.5
    stop sound fadeout 0.5
    scene black with dissolve 
    play sounds2 heartbeat loop 
    mc "Wh—"
    h "[mc]!"
    scene black with dissolve 
    pause 2.1
    h "What the hell did you do?!"
    Fl "...I don’t know, he—"
    mc "(…Where am I?)"
    mc "(What are these voices…?)"
    scene s1rew50 with dissolve 
    pause 0.4
    scene black with dissolve 
    pause 0.7
    play sounds3 keyboard fadein 1.2
    play sound systemambience fadein 3.0 loop volume 0.2
    scene s1rew50 with dissolve 
    o "No. Not this time. Even for you."
    Mi "…Teacher’s orders."
    scene black with dissolve 
    pause 2.1
    play sounds1 dronescan fadein 2.0 loop
    scene s1rew51 with dissolve 
    pause 0.4
    scene black with dissolve 
    pause 0.7
    scene s1rew51 with dissolve 
    o "The Inquisition’s on you this time."
    o "I’ve got enough on my plate already."
    Mi "…Fine."
    stop sounds2 fadeout 2.2
    scene black with dissolve 
    pause 2.1
    scene s1rew52 with dissolve 
    pause 0.4
    scene black with dissolve 
    pause 0.7
    scene s1rew52 with dissolve 
    "Analyzing... Analys-"
    o "...don’t know. Something’s interfering."
    o "I’ve locked part of it down, for now. It should hold."
    stop sounds1 fadeout 0.5
    scene s1rew54 with dissolve 
    Mi "…I won’t forget this."
    scene s1rew55 with dissolve 
    o "Since you’re here… mind telling me why you’re so interested in him?"
    scene s1rew56 with dissolve 
    Mi "…He’s like the other two scientists."
    scene s1rew55 with dissolve 
    o "..."
    o "...Don’t tell me you used the gates again."
    o "…He’s going to burn himself out like this."
    scene s1rew56 with dissolve 
    Mi "…My teacher knew the risk."
    scene s1rew55 with dissolve 
    o "How bad is he?"
    Mi "..."
    o "...Yeah. Thought so."
    scene s1rew57 with dissolve 
    mc "Two scientists?"
    o "Hey… you’re back."
    o "How are you holding up?"
    mc "Could be worse."
    play sounds2 mmove 
    scene s1rew58 with dissolve 
    o "You’ve got a talent for timing."
    o "One day, and we’re already meeting again."
    scene s1rew59 with dissolve 
    mc "A day?.."
    mc "I was out for a full day?"
    o "Data conflict."
    o "Your brain couldn’t decide what was real and what wasn’t."
    o "So it shut you down."
    o "Roughly… sixty-six cycles."
    mc "...cycles?"
    play sounds2 mmove 
    scene s1rew60 with dissolve 
    Mi "Twenty-two hours… by your standards."
    scene s1rew61 with dissolve 
    mc "(…almost a day?)"
    Mi "…Consider yourself lucky."
    mc "Fine."
    mc "We’ll deal with that later."
    mc "Right now, those two scientists."
    scene s1rew59 with dissolve 
    mc "First Lora."
    mc "Who’s the second?"
    scene s1rew61 with dissolve 
    Mi "..."
    mc "And don’t dodge the question."
    play sounds2 mmove 
    scene s1rew64 with dissolve
    Mi "I’ll call for transport."
    mc "Stop running."
    Mi "I’ll be waiting outside."
    mc "(Of course… she’s gone.)"
    scene s1rew63 with dissolve 
    o "Dr. Li."
    o "He’s the one who saved your life."
    mc "(Norman mentioned him…)"
    play sounds2 mmove 
    play sounds3 clothess 
    scene s1rew65 with dissolve 
    o "Your brain’s going to need about a month to adjust to the implants."
    play sounds2 mmove 
    scene s1rew67 with dissolve 
    mc "So I’ll keep blacking out."
    scene s1rew66 with dissolve 
    o "There is a way to manage it."
    play sounds2 mmove 
    scene s1rew68 with dissolve 
    o "You’ll need to take them every thirty cycles or so."
    o "Keeps things… stable."
    mc "No."
    mc "Not without knowing what they do."
    scene s1rew69 with dissolve 
    o "Neuro-catalysts."
    o "They help your brain keep up with the load."
    pause 1.1 
    mc "You brought me back."
    mc "Fixed my eye."
    mc "Ran your tests."
    mc "Now pills."
    mc "Why?"
    scene s1rew70 with dissolve
    o "Call it an investment in staying alive."
    scene s1rew71 with dissolve 
    mc "That doesn’t add up."
    pause 1.1 
    o "Call it repaying a debt."
    mc "A debt?"
    mc "From what?"
    mc "(Lora...)"
    mc "…I’ll return the favor."
    o "..."
    stop sound fadeout 2.2
    play sounds desertwind loop fadein 2.0 volume 0.5
    scene black with dissolve 
    pause 2.1
    play sounds1 closedoor 
    play music mcscenefloor fadein 24 
    pause 1.1
    scene s1rew73 with dissolve 
    pause 1.1
    scene s1rew74 with dissolve 
    Mi "Advice… don’t breathe too deep here."
    mc "Let’s be clear."
    mc "Why are we here."
    Mi "..."
    mc "You didn’t answer me about the scientists."
    mc "So answer this instead."
    scene s1rew75 with dissolve 
    Mi "We’re heading to a tomb… outside the city."
    Mi "That’s where your wife works."
    Mi "Outside the walls."
    Mi "Past the zones most patrols refuse to cross."
    pause 1.1
    mc "A tomb?"
    scene s1rew72 with dissolve  
    Mi "Mistakes of the past… buried by time and war."
    mc "What do you mean by 'mistakes'?"
    Mi "The ancients... they did something... something we all are paying for."
    mc "(She doesn't sound like she's willing to explain more)"

    mc "And Lora, how does she fit into this?"
    mc "She was working… on the ship."
    pause 1.1
    Mi "That ship, where we find you... was a tomb."
    mc "And the Ark?"
    Mi "Something connected to it."
    Mi "Something Lora should never have touched."
    scene s1rew76 with dissolve
    pause 1.1
    mc "(…so many of them.)"
    mc "(Flying… everywhere.)"

    mc "How advanced is the current civilisation considering you have flying vehicles?"
    Mi "Advanced? Not really. The tomb had most of the technologies we currently use."
    scene s1rew77 with dissolve 
    pause 0.8
    mc "A tomb…"
    mc "Like some kind of storage?"
    Mi "..."
    scene s1rew79 with dissolve 
    mc "Miriel?"
    scene s1rew80 with dissolve 
    Mi "A graveyard, not a storage."
    Mi "A vessel left behind by the Ancients."
    scene s1rew79 with dissolve
    mc "And you call it a tomb because its creators are dead."
    scene s1rew81 with dissolve
    mc "And no one has a problem with that?"
    Mi "…Should they?"
    mc "A graveyard means people were buried there... and you are stealing technology from them..."
    scene s1rew80 with dissolve 
    Mi "…So?"
    mc "(Graves being looted...{w=0.5} Jack...{w=0.5} Mona...)"
    mc "You are just looting graves."
    pause 1.1 
    Mi "The dead… don’t need their belongings."
    scene s1rew78 with dissolve 
    pause 1.1
    Mi "Every day… millions die at the front."
    Mi "Numbers stopped meaning anything a long time ago."
    Mi "Do you really think anyone cares about a tomb?"
    scene s1rew82 with dissolve 
    Mi "We’re just trying to survive."
    pause 1.1
    mc "(…No.)"
    mc "I don’t agree."
    scene s1rew83 with dissolve 
    mc "If this is nothing to you…"
    mc "Then tell me."
    mc "What did you do with my son’s body?"
    scene s1tew6 with dissolve 
    Mi "..."
    scene s1tew7 with dissolve 
    pause 1.1
    scene s1tew8 with dissolve 
    Mi "…We burned it."
    scene s1tew9 with dissolve 
    mc "(…Burned.)"
    play sounds2 spaceshipflying3 fadein 0.5 
    scene s1rew85 with dissolve 
    h "Hey!"
    h "Look at this thing, it’s fly—"
    h "...What happened?"
    scene s1rew84 with dissolve 
    Mi "Get in."
    scene s1rew86 with dissolve 
    mc "..."
    h "[mc]?"
    scene s1rew87 with dissolve 
    mc "(…Burned.)"
    mc "(Nothing left.)"
    pause 0.6
    h "[mc]!"   
    scene s1rew88 with dissolve 
    pause 1.1
    play sounds3 clothess 
    scene s1rew91 with dissolve 
    Mi "..."
    mc "(…why help me?)"
    h "Don’t look at her like that."
    h "She doesn’t bite."
    scene s1rew92 with dissolve 
    h "Honestly? She’s not that bad."
    h "You should’ve seen her."
    h "She kept asking about you."
    scene s1rew93 with dissolve 
    Mi "Olivia?! What the—"
    
    scene s1rew94 with dissolve 
    h "Come on, admit it."
    h "You were curious too."
    Mi "Why would you do that to me?"
    mc "(…helping?)"

    scene s1rew95 with dreamyzoom  
    L "You two… that’s enough."
    scene s1rew97 with dissolve 
    L "Olivia, apologize to that girl."
    L "Anya… don’t blame your sister."
    pause 1.1
    play sounds2 hug2 
    scene s1rew98 with dissolve 
    L "(whisper) You’re bound by blood…"
    L "(whisper) so I’m asking you…"
    scene s1rew99 with dissolve 
    L "(whisper) no matter what happens, you’re on the same side."
    scene s1rew100 with dissolve 
    C "(whisper) Yes, mom…"
    scene s1rew101 with dissolve 
    L "You’re already adults…"
    L "…but still, come visit sometimes."
    scene s1rew102 with dissolve 
    mc "(Lora…?)"
    scene s1rew103 with dissolve 
    mc "..."
    L "[mc]?"
    scene s1rew104 with dissolve 
    h "[mc]?"
    h "Hey."
    h "[mc]!"
    scene s1rew88 with dissolve 
    pause 1.1
    scene s1rew89 with dissolve 
    mc "...Yeah."
    stop music fadeout 8.1
    stop sounds fadeout 8.2
    scene black with dissolve 
    "Several hours later."
    play sounds spaceshipengine1 fadein 3.5 volume 0.4 loop
    pause 3.2

    play music1 mirielship1 fadein 8.2
    scene s1rew106 with dissolve 
    Mi "..."
    scene s1rew108 with dissolve 
    mc "..."
    scene s1rew107 with dissolve 
    mc "Something bothering you?"
    scene s1rew105 with dissolve 
    Mi "…Tell me."
    Mi "What are you feeling right now?"
    scene s1rew106 with dissolve 
    mc "…Where’s that coming from?"
    Mi "..."
    mc "…Nothing."
    scene s1rew105 with dissolve 
    Mi "…I see."
    scene s1rew106 with dissolve 
    pause 2.4
    scene s1rew108 with dissolve 
    pause 1.1
    scene s1rew107 with dissolve 
    mc "Miriel…"
    pause 1.1
    mc "What was Lora doing here?"
    scene s1rew108 with dissolve 
    Mi "Saving lives."
    Mi "Killing monsters."
    scene s1rew107 with dissolve 
    mc "Monsters?"
    scene s1rew105 with dissolve 
    Mi "Yes."
    Mi "What’s left of past civilizations."
    scene s1rew106 with dissolve 
    h "Wow… guess the ancestors were real generous with their ‘gifts’, huh?"
    Mi "…Mhm."
    mc "She was a researcher, right? So how did it end up like this?"
    scene s1rew105 with dissolve 
    Mi "Not a typical researcher."
    Mi "It wasn’t her choice."
    scene s1rew107 with dissolve 
    mc "What do you mean?"
    scene s1rew108 with dissolve 
    Mi "After the Ark changed her, people began hunting her."
    Mi "My orders were to keep her alive. I was never told who started the hunt."
    scene s1rew107 with dissolve 
    mc "So she wasn’t here by choice. She was trapped between whoever wanted her, and whoever claimed to protect her."
    mc "Tell me… how did she feel being here?"
    scene s1rew108 with dissolve 
    Mi "..."
    Mi "She regretted it… every day."
    Mi "She just wanted to go home."
    scene s1rew106 with dissolve 
    mc "Go back… Was she being held here? By your Mistress?"
    scene s1rew105 with dissolve 
    Mi "No."
    scene s1rew106 with dissolve 
    mc "Then why did she—"
    mc "(No, wait… something doesn’t add up.)"
    mc "(What she said back then…)"
    
    scene s1b162 with dreamyzoom  
    show memoryframe with dissolve        
    lad "Apparently."         
    lad "Whether by choice… is another question."

    scene s1rew107 with dissolve 
    mc "She didn’t want to go back?"
    mc "Or… she couldn’t?"
    scene s1rew109 with dissolve 
    Mi "..."
    scene s1rew110 with dissolve 
    mc "No…"
    mc "No, that’s not how this works."
    mc "There has to be a way out."
    play sounds2 scifidooropen2
    scene s1rew111 with dissolve 
    Mi "…Answer me."
    pause 1.1
    Mi "If you’re told, you can change your previous choices."
    Mi "So you choose differently."
    scene s1rew112 with dissolve 
    Mi "But the outcome stays the same. In each one of them..."
    Mi "Was it ever a choice?"
    scene s1rew113 with dissolve 
    pause 1.1
    mc "..."
    mc "…That depends on the choice."
    scene s1rew114 with dissolve 
    Mi "..."
    Mi "We’re almost there."
    Mi "Be ready."
    mc "And… what’s your answer?"
    scene s1rew115 with dissolve 
    Mi "…I don’t know."
    Mi "My teacher never answered."

    image arriveteam = Movie(channel="movie_dp", loop = False, play="video/arriveteam.webm")
    show arriveteam  with dissolve 
    $ renpy.pause(6.1, hard=True)
    play sounds4 spaceshiparrvied 
    scene s1rew117 with dissolve 
    "Sector 5-S. Second level. Residential zone."
    Mi "We’re here."
    Mi "We’ll continue on foot."
    mc "Why?"
    play sounds2 mmove 
    scene s1rew118 with dissolve 
    Mi "Security."
    scene s1rew119 with dissolve 
    Mi "Move."
    stop music1 fadeout 5.4 
    stop sounds fadeout 2.2

    scene black with dissolve 
    pause 4.1
    play music wallfirest fadein 9.2
    play sounds4 desertwind fadein 4.4 loop volume 0.4
    scene s1rew259 with dissolve 
    "Sector 6. Second level. Border zone."
    mc "This… some kind of combat drill?"
    Mi "No."
    mc "Then what’s going on?"
    mc "Where are they all running to… and why do you need walls this massive?"
    play sounds3 spaceshippassby volume 0.3
    scene s1rew260 with dissolve 
    Mi "The soulless."
    mc "Those are the ones Lora was killing?"
    Mi "Yes."
    Mi "If even one gets into the city…"
    Mi "It turns into a slaughter."
    scene s1rew261 with dissolve 
    mc "You mean?"
    scene s1rew262 with dissolve 
    Mi "I… I don’t know how."
    Mi "But once they get into the city, they spread like a virus."
    scene s1rew261 with dissolve 
    mc "Why not just seal them off?"
    scene s1rew262 with dissolve 
    Mi "It’s too late."
    Mi "We’ve been fighting them for centuries."
    scene s1rew261 with dissolve 
    mc "And it’s like this everywhere?"
    scene s1rew262 with dissolve 
    Mi "Yes."
    play sounds3 spaceshippassby volume 0.3
    scene s1rew263 with dissolve 
    h "Hey, Mir?"
    h "Those guys… they look kinda off."
    Mi "Androids?"
    h "Yeah."
    h "Then why not use them instead?"
    Mi "Too expensive."
    Mi "...Humans are cheaper."
    scene s1rew264 with dissolve 
    h "...Right."
    scene s1rew265 with dissolve 
    h "..."
    Mi "..."
    scene s1rew266 with dissolve 
    Mi "Any more questions?"
    scene s1rew267 with dissolve 
    mc "Hold on…"
    mc "Then two questions."
    mc "Why build walls this huge, what, 300 meters?"
    scene s1rew268 with dissolve 
    mc "And why couldn’t we just fly here on that thing?"
    Mi "..."
    Mi "So nothing gets brought in."
    mc "What do you mean?"
    scene s1rew272 with dissolve 
    h "You grab one of those things…"
    h "Stuff it into a transport…"
    h "Fly it over the city…"
    h "Drop it—"
    h "Boom."
    h "City’s gone."
    mc "There were incidents?"
    Mi "…Yes."
    play sounds3 spaceshippassby volume 0.3
    scene s1rew273 with dissolve 
    mc "And Lora’s out there? Beyond the walls?"
    mc "Why take that kind of risk…"
    Mi "To survive."
    mc "(Survive?)"

    scene s1b165 with dreamyzoom 
    show memoryframe with dissolve 
    lad "I don’t need you."
    lad "You need a reason to survive."


    scene s1rew274 with dissolve 
    mc "..."
    mc "(I hope you’re okay…)"
    
    stop music fadeout 5.5
    g "Hey! Have you completely lost your mind?"
    scene s1rew275 with dissolve 
    gg "Three against one?"
    gg "Were you that desperate to steal my food—"
    play sounds1 punch1 
    scene s1rew276 with vpunch 
    pause 1.8
    play sounds2 clench 
    scene s1rew277 with dissolve
    h "..."
    scene s1rew278 with dissolve   
    h "...Hey."
    h "(whisper) Don’t play hero."
    h "(whisper) Please."
    scene s1rew279 with dissolve
    mc "(whisper) Three against one, Liv—"
    scene s1rew278 with dissolve   
    h "(whisper) Not our problem."
    h "We move."
    scene s1rew280 with dissolve   
    mc "I don’t like how this place works."
    pause 1.1
    scene s1rew281 with dissolve   
    Mi "..."
    play sounds3 mmove 
    scene s1rew282 with dissolve   
    Mi "Sometimes… what’s inside the walls hardens you more than killing monsters ever could."
    Mi "Let’s go."
    
    play sounds2 clench 
    scene s1rew296 with dissolve   
    pause 1.1
    scene s1rew297 with dissolve   
    a "Hm... I know the uniform. I know the pointy-eared elf. But him? No."
    play music1 inquisition fadein 5.5
    scene s1rew299 with dissolve 
    a "A rookie? ...Doesn’t feel like it."
    scene s1rew298 with dissolve 
    g "Let’s do this the easy way, hand over the food."
    a "(Annoying...)"
    scene s1rew297 with dissolve   
    pause 1.1
    play sounds2 mmove 
    scene s1rew300 with dissolve
    a "..."
    play sounds2 mcjump4 
    scene s1rew301 with dissolve
    pause 1.2
    scene s1rew303 with dissolve
    gg "You think I don’t see it?"
    gg "This isn’t about the food."
    scene s1rew302 with dissolve
    g "..."
    g "We’re not monsters."
    scene s1rew286 with dissolve
    gggg "Hey, Marty, leave him. I don’t think it’s him—"
    g "Stay out of it, Barek."
    ggggg "..."
    play sounds2 mmove 
    scene s1rew287 with dissolve
    ggggg "...Marty."
    scene s1rew288 with dissolve
    gggg "What do you—"
    gggg "..."
    play sounds2 mmove 
    scene s1rew283 with dissolve    
    a "Beating one man as a pack… no shame at all?"
    a "...Why am I even asking."
    play sounds1 whoosh 
    scene s1rew289 
    pause 0.7
    play sounds2 punch2 
    scene s1rew290 with vpunch 
    pause 1.1
    play sounds3 whoosh 
    scene s1rew291 
    pause 0.5
    play sounds2 fall 
    scene s1rew292 with vpunch
    pause 1.1
    play sounds3 punch1 
    scene s1rew293 with vpunch
    pause 1.1
    play sounds2 clench 
    play sounds1 whoosh 
    scene s1rew294 with dissolve 
    g "Th-that hurts..."
    a "Hey. Soldier."
    a "Explain your actions."
    g "H-he stole our food—"
    play sounds2 clench 
    a "Careful."
    a "Lie to me again, and you lose the hand."
    g "I’m not ly—"
    stop sounds4 fadeout 0.5
    stop music1 fadeout 0.5
    play sounds2 breakbone 
    scene black with vpunch 
    g "Argh!"
    a "I warned you."
    pause 1.8

    
    scene black with dissolve 
    "Sector 6. Research facility."
    play sounds2 doorclose
    play sound systemambience fadein 5.5 loop volume 0.1
    play music1 laboratorytt fadein 5.5 
    scene s1rew124 with dissolve 
    Mi "She spent most of her life here."
    mc "Here? Wait, I thought her workplace was outside the city."
    Mi "Yes."
    Mi "My teacher told me to bring you here first."
    Mi "He said you should take a look around."
    play sounds2 mmove 
    scene s1rew125 with dissolve 
    h "Huh…"
    h "Way better than I expected."
    h "Smells weird though…"
    h "...whatever."
    scene s1rew126 with dissolve 
    h "So what was she doing here?"
    scene s1rew127 with dissolve 
    Mi "I wasn’t part of her work."
    pause 1.1
    mc "(Lora…)"
    scene s1rew128 with dissolve 
    pause 1.1
    play sounds2 mmove 
    scene s1rew129 with dissolve 
    h "Hey, [mc]?"
    h "Crumbs on the floor."
    h "Still fresh, too—"
    play sounds2 mmove 
    scene s1rew131 with dissolve 
    mc "You serious right now?"
    scene s1rew130 with dissolve 
    h "Kidding!"
    h "But seriously. Someone’s been here recently."
    scene s1rew132 with dissolve 
    h "Mir?"
    h "You got any idea what these things are?"
    Mi "...I didn’t work on this."
    h "...Yeah, figured."
    scene s1rew133 with dissolve 
    h "Hey, old man, check this out."
    h "This thing hooks straight into your head."
    h "And there’s some weird fluid in it…"
    scene s1rew134 with dissolve 
    mc "Try not to touch anything."
    mc "(Connected to the head? Hold on…)"
    scene s1rew129 with dissolve 
    mc "(Looks like a brain scanner…)"
    mc "This isn’t good."
    mc "(Implants?.. No.)"
    mc "(Too crude.)"
    mc "(A malfunction?)"

    scene s1rew135 with dissolve 
    Mi "Not exactly to the head—"
    scene s1rew136 with dissolve 
    h "Hey!"
    h "Thought you said you didn’t know what this was."
    h "Lying’s not a good look on you."
    play sounds2 mmove 
    scene s1rew137 with dissolve 
    pause 1.1
    mc "(Why so many monitors?)"
    mc "(Analysis? Testing? Surveillance?)"
    play sounds3 maninhalingbreath
    scene s1rew141 with dissolve 
    pause 1.1
    scene s1rew142 with dissolve 
    mc "..."
    scene s1rew138 with dissolve 
    h "Kinda wanna see if this thing still works."
    scene s1rew139 with dissolve 
    Mi "That’s… not safe, Liv."
    mc "What is she—"
    scene s1rew143 with dissolve 
    h "Relax."
    h "I’ve done this like a hundred ti—"
    stop music1 fadeout 3.3
    play sounds2 whoosh 
    play sounds3 bodytap
    play music season4act12 fadein 5.4
    scene s1rew144 
    mc "Get down. Now."
    mc "What if something had happened to you?!"
    h "..."
    mc "…You okay?"
    scene s1rew145 with dissolve 
    pause 0.5
    scene s1rew146 with dissolve 
    pause 0.5
    scene s1rew145 with dissolve 
    pause 0.5
    scene s1rew144 with dissolve 
    mc "Please, don’t grab the wires, and don’t climb on this stuff."
    scene s1rew147 with dissolve 
    mc "I don’t want anything happening to you."
    play sounds2 mmove 
    scene s1rew148 with dissolve 
    h "Relax."
    h "It’s dead."
    mc "..."
    mc "…How do you know that?"
    h "Checked the meters behind the monitors."
    h "No power."
    scene s1rew149 with dissolve 
    mc "And instead of saying that, you decided to climb onto it?"
    scene s1rew150 with dissolve 
    h "What?"
    h "Thought I’d show it instead of explaining."
    scene s1rew152 with dissolve 
    mc "You’re staring a bit too hard."
    mc "Something wrong?"
    play sounds2 whoosh 
    scene s1rew153 
    Mi "…No."
    Mi "Just… thinking."
    scene s1rew154 with dissolve 
    mc "(What was that?)"
    pause 1.1
    play sounds2 bodytap 
    scene s1rew155 with dissolve 
    mc "You did good. But let’s make that the last time."
    scene s1rew156 with dissolve 
    h "Come on… admit it."
    h "You were worried."
    scene s1rew157 with dissolve 
    mc "Me? Why would I?"
    scene s1rew158 with dissolve 
    h "Wow."
    h "You’re kinda mean, you know that?"
    scene s1rew159 with dissolve 
    mc "…Maybe a little."
    mc "Just a little."
    scene s1rew160 with dissolve 
    pause 1.1
    mc "..."
    scene s1rew161 with dissolve 
    h "..."
    scene s1rew162 with dissolve 
    pause 1.8
    play sounds2 mmove 
    scene s1rew163 with dissolve 
    mc "If you find anything, let me know."
    h "Oki…"
    mc "That goes for you too."
    Mi "…Alright."

    
    
    scene s1rew164 with dissolve 
    mc "(Now you…)"
    mc "(…what were you doing here?)"
    scene s1rew165 with dissolve 
    pause 1.1
    scene s1rew166 with dissolve 
    mc "..."
    play music1 laboratorytt2 fadein 16.2 
    stop music fadeout 12
    scene s1rew167 with dissolve 
    mc "(A notebook?)"
    scene s1rew166 with dissolve 
    mc "..."
    L "{u}It’s not working…"
    L "{u}I’ve tried everything. Nothing holds."
    scene s1rew169 with dissolve 
    L "{u}Maybe… I should just leave it as it is."
    L "{u}...They’d be better off without me anyway."
    mc "(What were you doing here, Lora…?)"
    play sounds2 mmove 
    scene s1rew170 with dissolve 
    L "{u}I can feel it spreading…"
    L "{u}Crawling up, little by little…"
    L "{u}If it wasn’t for that thing, I could’ve—"
    L "{u}…No."
    scene s1rew171 with dissolve 
    L "{u}Medicine doesn’t work."
    L "{u}Implants…?"
    L "{u}...Or start over again?"
    L "{u}Why now…?"
    L "{u}Why this time…?"
    play sounds2 glitchfear
    scene s1rew172 with glitch 
    mc "(It was spreading…)"

    scene s1rew262 with dreamyzoom  
    show memoryframe with dissolve 
    Mi "They’re carriers."
    Mi "One bite… and you become one of them."

    scene s1rew172 with dissolve 
    mc "(…No.)"
    mc "(That’s not possible.)"
    mc "Miriel… is there any way… to stop the transformation?"
    Mi "The soulless?"
    Mi "Why are you asking?"
    mc "Answer me."
    scene s1rew173 with dissolve 
    Mi "No."
    mc "..."
    mc "(This is bad…)"
    play sounds2 footstep2
    scene s1rew174 with dissolve 
    pause 1.1
    scene s1rew175 with dissolve 
    pause 1.1
    scene s1rew176 with dissolve 
    L "{u}Help…"
    L "{u}Please… someone…"
    L "{u}I’m so tired…"
    play sounds2 glitchfear
    scene s1rew177 with glitch 
    mc "(…and no one came.)"
    pause 1.1
    mc "(…what did they do to you?)"
    scene s1rew178 with dissolve
    mc "A camera…"
    mc "Pointed right at her."
    mc "Why would they do that?"
    scene s1rew179 with dissolve 
    mc "(She was being watched.)"
    mc "(Constantly.)"
    mc "(Why…?)"
    scene s1rew180 with dissolve 
    mc "Olivia?"
    mc "Tell me, are you absolutely sure everything’s offline?"
    scene s1rew184 with dissolve 
    h "Yeah. I’m sure."
    scene s1rew185 with dissolve 
    mc "Check again. Just in case."
    scene s1rew186 with dissolve 
    h "I mean, I can try... but what happened to you?"
    h "Your voice, it's all tense. That’s not like you."
    scene s1rew187 with dissolve 
    mc "Lora was under surveillance."
    mc "I want to know why."
    h "You sure about that?"

    scene s1rew183 with dissolve 
    Mi "..."
    mc "Miriel?"
    scene s1rew182 with dissolve 
    pause 1.8
    scene s1rew181 with dissolve 
    Mi "The camera wasn’t there to protect her."
    scene s1rew182 with dissolve 
    mc "Then who was watching?"
    scene s1rew181 with dissolve 
    Mi "I never saw a name. Only sealed orders."
    
    scene s1rew188 with dissolve 
    mc "And what did those orders say?"
    scene s1rew189 with dissolve 
    Mi "Keep Lora alive. Move her when ordered. Ask no questions."
    Mi "That was all they trusted me with."
    scene s1rew188 with dissolve 
    mc "(Were they afraid the infection would spread?)"
    mc "(No… they would’ve just eliminated her.)"

    scene s1b165 with dreamyzoom
    show memoryframe with dissolve 
    lad "There was a connection inside her."
    lad "A path out of this world."

    scene s1rew188 with dissolve 
    mc "(A path out of this world…?)"
    mc "(Inside Lora?)"
    mc "(…Why her?)"

    scene s1b162 with dreamyzoom 
    show memoryframe with dissolve 
    lad "She was like you."
    lad "She survived contact with something she shouldn't have."
    lad "It changed her."
    
    scene s1rew188 with dissolve 
    mc "(Changed her… how?)"
    mc "(No. That still doesn’t explain this.)"
    play sounds2 mmove 
    scene s1rew190 with dissolve 
    L "{u}I have to save them…"
    L "{u}My son… and [mc]…"
    play sounds2 footstep2 
    
    L "{u}I can do it…"
    L "{u}...This time I’ll get it right."
    scene s1rew191 with dissolve 
    mc "..."
    play sounds2 mmove 
    scene s1rew192 with dissolve 
    L "{u}P.S. Attempt 435: failure."
    L "{u}P.P.S. Attempt 436:"
    scene s1rew193 with dissolve 
    mc "(Four hundred and thirty-six attempts connected to 'starting over.')"
    mc "(At least that much is clear. What she kept restarting… isn’t.)"
    scene s1rew194 with dissolve 
    pause 1.1
    scene s1rew195 with dissolve 
    mc "(…none of this makes sense.)"
    scene s1rew196 with dissolve 
    pause 1.1
    scene s1rew202 with dissolve 
    L "{u}Remember… remember…"
    scene s1rew197 with dissolve 
    pause 0.8
    L "{u}P.S. M— don’t forget…"
    pause 1.1

    scene s1rew199 with dissolve 
    pause 0.9
    L "{u}P.S. Inquisition…"
    pause 0.6
    mc "(A purge…?)"
    pause 1.1

    scene s1rew198 with dissolve 
    pause 1.1
    L "{u}P.S. J—"
    pause 1.1

    scene s1rew202 with dissolve 
    mc "..."
    mc "(…too much.)"
    play sounds2 mmove 
    scene s1rew203 with dissolve 
    pause 1.1
    scene s1rew204 with dissolve 
    h "So... how’d it go?"
    scene s1rew206 with dissolve 
    mc "She was digging into something."
    mc "But what…?"
    scene s1rew205 with dissolve 
    pause 1.8
    scene s1rew203 with dissolve 
    pause 1.1
    scene s1rew207 with dissolve 
    h "(whispering) She found something she wasn’t supposed to?"
    scene s1rew209 with dissolve 
    mc "(whispering) Looks like it."
    stop music1 fadeout 5.5
    scene s1rew208 with dissolve 
    h "..."
    scene s1rew209 with dissolve 
    mc "(whispering) I need a minute… to think."
    play sounds2 mmove 
    play sounds3 sittingchair
    scene s1rew210 with dissolve 
    mc "(I don’t get how any of this connects… at all.)"
    scene s1rew211 with dissolve 
    pause 1.1
    scene s1rew212 with dissolve 
    mc "(Wait… hold on…)"
    
    scene s1rew170 with dreamyzoom 
    show memoryframe with dissolve 
    L "I can feel it spreading…"
    L "If it wasn’t for that thing. I could’ve—"

    scene s1rew212 with dissolve 
    mc "(…I’ve heard this before.)"

    scene s0pp11 with dreamyzoom
    show memoryframe with dissolve 
    npc "...substance... regenerating..."
    scene s0b24 with dreamyzoom
    show memoryframe with dissolve 
    N "The substance... He absorbed it." 
    N "...he stopped being human."
    play music season4act3 fadein 5.5
    scene s1rew213 with dissolve 
    mc "(Then why is the effect different…)"
    pause 1.1
    scene s1rew213 with dissolve 
    mc "(And he didn’t turn.)"
    pause 1.1
    scene s1rew214 with dissolve 
    mc "(…something’s off. Or… no— something’s missing.)"
    h "You spacing out again?"
    mc "Hm?"
    scene s1rew215 with dissolve 
    mc "Hey, get down."
    mc "That’s not safe."
    scene s1rew216 with dissolve 
    h "Relax, I’ve got a good grip. You tell me, why the long face?"
    h "So what, got nowhere with it?"
    scene s1rew217 with dissolve 
    mc "Is it that obvious?"
    scene s1rew216 with dissolve 
    h "Pretty much. I know you well enough."
    h "C’mon, give your brain a break."
    h "Besides, we’ll run into Lora soon enough. It’ll all make sense then."
    scene s1rew218 with dissolve 
    mc "..."
    scene s1rew219 with dissolve 
    pause 1.1
    play sounds2 mmove 
    scene s1rew220 with dissolve 
    mc "What are you doing?"
    scene s1rew221 with dissolve 
    Mi "..."
    scene s1rew222 with dissolve 
    Mi "…Sitting."
    scene s1rew221 with dissolve 
    pause 1.1
    scene s1rew223 with dissolve 
    h "He means… why the floor?"
    scene s1rew222 with dissolve 
    Mi "One of the rules… for our sins."
    scene s1rew225 with dissolve 
    mc "You actually believe that?"
    scene s1rew226 with dissolve 
    h "Don’t bother, you won’t change her mind, I already tried—"
    scene s1rew227 with dissolve 
    h "What are you doing?"
    scene s1rew228 with dissolve 
    mc "Back in that flying thing, you were sitting normally."
    mc "So what changed?"
    scene s1rew229 with dissolve 
    Mi "…It doesn’t matter."
    scene s1rew228 with dissolve 
    mc "Why not sit like Olivia? On those crates, for example?"
    scene s1rew229 with dissolve 
    Mi "I’m more comfortable this way."
    play sounds2 mmove 
    scene s1rew230 with dissolve 
    pause 1.1
    scene s1rew231 with dissolve 
    pause 1.1
    Mi "Why are you—"
    scene s1rew232 with dissolve 
    mc "I’m more comfortable on the floor. That’s all."
    mc "Got a problem with that?"
    scene s1rew233 
    pause 0.1
    scene s1rew234
    pause 0.1
    scene s1rew233
    pause 0.1
    scene s1rew234
    pause 0.1
    scene s1rew235 with dissolve 
    h "...oh damn."
    play sounds2 mmove 
    scene s1rew236 with dissolve 
    Mi "(whispering) This is… kind of awkward…"
    play sounds3 hug2 
    play sounds1 whoosh  
    scene s1rew237 
    h "Oh wow, aren’t you adorable!"
    h "That’s it, I’m hugging you."
    scene s1rew238 with dissolve 
    mc "Cut it out."
    mc "Just be yourself."
    scene s1rew239 with dissolve 
    h "Oop, yeah, you hit a nerve there—"
    scene s1rew240 with dissolve 
    Mi "Olivia, stop!"
    scene s1rew241 with dissolve 
    h "Hey, come on… we’re friends, aren’t we?"
    scene s1rew242 with dissolve 
    Mi "Yes, but this is embarrassing!"
    play sounds2 mmove 
    scene s1rew243 with dissolve 
    mc "Hey, Miriel?"
    mc "We’re a team."
    scene s1rew244 with dissolve 
    pause 1.1
    scene s1rew245 with dissolve 
    h "..."
    play sounds2 mmove 
    scene s1rew246 with dissolve 
    h "Nope. That one’s on you."
    h "That actually means a lot to him."
    scene s1rew247 with dissolve 
    Mi "..."
    play sounds3 bodytap    
    scene s1rew248 with dissolve 
    Mi "…Mhm."
    mc "Then… welcome to the team."
    play sounds systemnotification
    scene s1rew249 with dissolve 
    "Miriel gets a new message."

    play sounds2 whoosh 
    play sounds3 flamethrower
    scene s1rew253 with CropMove(time=0.1, mode='slideleft') 
    Fl "Yo, your favorite mechanic here."
    scene s1rew254 with dissolve 
    pause 1.1
    scene s1rew255 with dissolve 
    pause 1.1

    scene s1rew256 with dissolve 
    Fl "Your package is ready. I tuned up your implants."
    scene s1rew257 with dissolve 
    pause 1.1
    play sounds systemnotification
    scene s1rew258 with dissolve 
    Fl "I’ll be in Sector 5."
    Fl "Try not to keep me waiting."

    play sounds2 glitchfear 
    scene s1rew250 with glitch     
    h "Hey… you okay, Miriel?"
    scene s1rew251 with dissolve 
    Mi "I’m fine… just…"
    Mi "I need to stop by somewhere."
    scene s1rew252 with dissolve 
    mc "Then we’re coming with you."
    stop music fadeout 5.4

    scene black with dissolve
    pause 5.5
    "Sector 6. Command post."

    play music1 backgroundsus fadein 5.5
    scene s1rrew305 with dissolve 
    g "No."
    Mi "Reason?"
    g "Listen up, pointy-ears."
    g "I don’t give a damn who gave you orders."
    scene s1rrew306 with dissolve 
    g "I’m in charge here."
    g "And I’m not authorizing anyone to leave the city. Got it?"
    Mi "..."
    g "I don’t hear an answer, pointy-ears."
    scene s1rrew307 with dissolve 
    Mi "Understood."
    scene s1rrew306 with dissolve 
    g "Now get the hell out of my office!"
    pause 1.1
    play sounds2 mmove 
    play sounds3 whoosh 
    scene s1rrew308 
    Mi "…Tch."
    Mi "Let’s go."
    play sounds2 mmove 
    scene s1rrew309 with dissolve 
    h "Hey, wait, Mir—"
    scene s1rrew310 with dissolve  
    pause 1.1
    scene s1rrew311 with dissolve 
    g "What are you staring at?"
    g "You think that uniform scares me?"
    pause 1.1
    scene s1rrew312 with dissolve 
    g "Look at you… fussing over some elf girl..."
    g "Pathetic."
    play sounds2 mmove 
    scene s1rew319 with dissolve 
    h "Huh?"
    h "Say that again, I dare you."
    scene s1rrew313 with dissolve
    g "Just thinking out loud."
    g "Though you’re just like that scientist, just as messed up."
    play sounds2 clench 
    scene s1rew316 with dissolve 
    g "What do you—"
    h "Old man, don’t!"
    play sounds2 mmove 
    play sounds3 clench 
    scene s1rew318 
    g "Kh—"
    scene s1rew317 with dissolve
    mc "Apologize."
    scene s1rew318 with dissolve 
    g "I- arch"
    g "You think this is gonna save you- kh—"
    play sounds3 clench 
    pause 0.8
    mc "…I’m waiting."
    h "[mc]! That’s enough—"
    g "You—"
    g "have no idea who you’re dealing with—"
    play sounds3 clench 
    scene s1rew317 with dissolve
    h "Stop! You’re gonna kill him!"
    scene s1rew318 with dissolve 
    mc "Don’t interfere."
    scene s1rew333 with dissolve 
    Mi "..."
    pause 0.8
    scene s1rew318 with dissolve 
    Mi "(whispering) …That’s enough…"
    g "The hell—kh—"
    pause 1.7
    g "F-fine—sorry—"
    scene s1rew320 with dissolve 
    mc "Next time…"
    pause 0.8
    mc "I won’t stop."
    play sounds3 clench 
    scene s1rew321 with dissolve 
    g "arch-"
    mc "..."
    play sounds2 fall volume 3
    play sounds3 tablesq 
    scene s1rew322 with vpunch 
    "He coughs, struggling to breathe."
    mc "Good."
    mc "Then we understand each other."
    scene s1rew323 with dissolve 
    pause 1.1
    g "...you’re gonna regret this."
    scene black with dissolve 
    mc "Let’s go."
    mc "…before he finds his spine again."

    play sounds2 bodytap
    scene s1rew324 with dissolve 
    h "He deserved to be put in his place."
    pause 1.1
    h "But you weren’t trying to scare him, [mc]."
    play sounds3 mmove 
    h "You almost killed him."
    scene s1rew325 with dissolve 
    mc "I stopped."
    scene s1rew326 with dissolve 
    h "Only after we told you to."
    h "Now the real question is, how screwed are we?"
    scene s1rew327 with dissolve
    h "Mir, what do you think?"
    scene s1rew328 with dissolve
    pause 1.1
    scene s1rew335 with dissolve 
    pause 1.1
    scene s1rew333 with dreamyzoom 
    show memoryframe with dissolve 
    Mi "..."
    scene s1rew334 with dissolve 
    mc "Apologize."
    scene s1rew335 with dissolve 
    Mi "(They stood up for me.)"
    Mi "(And for a moment… I was afraid he wouldn’t stop.)"
    scene s1rew336 with dissolve 
    h "Mir? Heeey, anyone home?"
    Mi "…Mm."
    play sounds2 mmove 
    scene s1rew329 with dissolve
    Mi "…Sorry."
    Mi "I got lost in thought."
    scene s1rew330 with dissolve
    h "..."
    h "...Look at her."
    h "...she’s smiling."
    mc "I see it."
    scene s1rew331 with dissolve
    Mi "I can hear you…"
    scene s1rew332 with dissolve
    h "Good. So… what now?"
    Mi "..."
    Mi "(…Teacher…?)"
    scene s1def150 with dreamyzoom
    show memoryframe with dissolve 
    Mi "...What if he refuses?"
    scene s1def151 with dreamyzoom
    show memoryframe with dissolve 
    a "Take him to Ember. I’ll put in a word for him."
    scene s1def150 with dreamyzoom
    show memoryframe with dissolve 
    Mi "But why not ask the Madam directly?"
    scene s1def150 with dreamyzoom
    show memoryframe with dissolve 
    a "Do as I say."
    scene s1rew331 with dissolve
    Mi "..." 
    Mi "(…I understand.)"
    Mi "Let’s go."
    stop music1 fadeout 5.5
    stop sound fadeout 1.1
    pause 4.1


label sectors_ruin:

    scene s1tew10 with dissolve 
    pause 1.1
    mc "(…That’s… on a whole different scale.)"
    mc "(But…)"
    mc "Miriel?"
    scene s1tew11 with dissolve 
    pause 1.1 
    mc "What are those ruins out there…?"

    scene s1rew80 with dreamyzoom 
    show memoryframe with dissolve 
    Mi "...buried by time and war."
    
    scene s1tew11 with dissolve 
    mc "...A graveyard…"
    Mi "..."
    scene s1tew12 with dissolve 
    Mi "Tombs."
    mc "And Lora… she works there?"
    Mi "…Yes."
    pause 1.1 
    "(Olivia snores softly.)"
    scene s1rew105 with dissolve 
    mc "(whispering) …She’s worn out."
    scene s1rew106 with dissolve 
    Mi "[mc]?"
    Mi "(whispering) About what happened with the commander…"
    Mi "(whispering) Thank you."
    Mi "(whispering) But next time… stop when I ask you to."
    scene s1rew105 with dissolve 
    mc "(whispering) I will."
    mc "(whispering) We’re a team. Remember?"
    scene black with dissolve 
    Mi "Yes..."

# 


label taxi:
    $ persistent.chapter_act1_scene += 1
    scene black with dissolve
    play sounds1 windcyb fadein 5.0 loop volume 0.8
    pause 3.0

    show s1c1 with dissolve
    "Sector 5-S. Third level. Residential zone."
    Fl "(Where is she?)"
    show s1c2 with dissolve
    h "So what, we just sit around and wait for Lora to come back on her own?"
    h "And what about that desert trip you promised?!"
    Mi "The commander revoked our clearance after what happened."
    show s1c3 with dissolve
    h "Gee, wonder whose fault that is, huh, [mc]?"
    mc "He crossed the line."
    Mi "And now the official route to Lora’s tomb is closed."
    show s1c4 with dissolve
    mc "…That part is on me."
    play sounds2 metalstep 
    show s1c6 with dissolve
    h "Ahem… anyway. What now?"
    Mi "The lower city."
    play sounds2 metalstep fadein 0.6
    show s1c7 with dissolve
    mc "Why there?"
    play sounds2 metalstep fadein 0.6
    show s1c8 with dissolve
    h "Astoria controls the upper sectors. The Inquisition follows its own chain of command."
    h "Down there, neither of them matters much."
    show s1c9 with dissolve
    mc "Who does?"
    Mi "Emberlyn. Most people call her Ember."
    Mi "If you want an unofficial route to Lora’s tomb, you need her."
    play sounds2 metalstep fadein 0.7
    show s1c11 with dissolve
    h "Fine. While you chase Lora, I’m finding out who sent Norman into that forest."
    mc "You’re not doing that alone."
    h "Wasn’t asking."
    Mi "And I need to know why my teacher sent us to Ember instead of the Madam."
    play sounds2 metalstep fadein 0.6
    show s1c12 with dissolve
    mc "Then we all have a reason to go."
    play sounds2 metalstep fadein 0.6
    show s1c13 with dissolve
    Mi "But first, Flora."
    Mi "The best mechanic in the city."
    play sounds2 metalstep fadein 0.6
    show s1c14 with dissolve
    Mi "Brilliant, if a little—"
    show s1c16 with dissolve
    h "—Intolerable?"
    show s1c30 with dissolve
    Mi "..."
    show s1c31 with dissolve
    Mi "I was going to say ‘prickly.’"
    Mi "But yes… teamwork isn’t exactly her strength."
    show s1c17 with dissolve
    h "Mir, because of her the old man lost his head."
    h "I’m not getting involved with her. No way."
    show s1c27 with dissolve
    Mi "..."
    show s1c29 with dissolve
    Mi "Even so… the fact remains."
    Mi "She’s the best at what she does."
    scene s1c17 with dissolve
    h "The best? Sure, I won’t argue that. But I’m not working with her."
    show s1c20 with dissolve
    mc "Olivia, that’s enough."
    show s1c18 with dissolve
    h "..."
    show s1c21 with dissolve
    mc "Listen. You don’t have to like her, just ignore her. Alright?"
    show s1c32 with dissolve
    Mi "If she steps out of line… I’ll deal with it."
    Mi "I promise."
    show s1c22 with dissolve
    h "Fine. I’ll play nice."
    show s1c34 with dissolve
    Fl "Hey, shorty. I told you, fix that look on your face."
    h "..."
    h "You hear that?"
    play music sprock fadein 3.0 volume 0.4
    show s1c23 with dissolve
    h "You got a problem or something?"
    scene s1c34 with dissolve
    Fl "It’s your attitude, shorty."
    Fl "...Not a fan of that tone."
    show s1c179 with dissolve
    mc "(This is spiraling. Fast.)"
    play sounds2 bodytap volume 0.3
    show s1c25 with dissolve
    h "I’m not scared of you—"
    scene s1c24 with dissolve   
    mc "Olivia, please."
    show s1c26 with dissolve
    h "(whispering) Let me handle this."
    mc "..."
    mc "…Fine."
    show s1c35 with dissolve
    h "Hey, stretch, let’s get one thing straight."
    h "You stay out of my way, I stay out of yours."
    Fl "..."
    show s1c36 with dissolve
    Fl "What did you just call me?"
    h "...Seriously?"
    h "Alright. Stretch."
    Fl "Say that again."
    pause 0.7
    Fl "...to my face."
    show s1c37 with dissolve
    Mi "Calm down. Don’t do anything stupid."
    play sounds2 metalstep 
    show s1c51 with dissolve
    Fl "..."
    h "..."
    show s1c52 with dissolve
    h "Wow… height issues? That’s rich."
    show s1c53 with dissolve
    Fl "Shorty."
    scene s1c52 with dissolve
    h "Streeetch."

    image florapunch = Movie(channel="movie_dp", loop = False, play="video/florapunch.webm")
    show florapunch 
    $ renpy.pause(1.8, hard=True)

    stop music fadeout 1.2
    show s1c55 
    mc "Enough!"
    pause 1.1
    h "She’s the one starting shit."
    show s1c57 with dissolve
    Mi "Why did you provoke her?"
    h "Hey, she started it!"
    Fl "..."
    show s1c38 with dissolve
    Fl "(…That was reckless.)"
    mc "Liv."
    pause 1.1
    mc "You went too far."
    mc "..."
    h "...sorry."
    stop music fadeout 2.0
    play sounds2 metalstep 
    show s1c40 with dissolve
    Mi "..."
    Mi "…We’ll split up."
    Mi "I’ll send Flora the data."
    Mi "She’ll brief you on the way."
    play sounds2 metalstep 
    show s1c41 with dissolve
    Mi "Liv, you’re with me."
    h "Hey, but sending him with—"
    play sounds2 metalstep 
    show s1c42 with dissolve
    h "(whispering) No… she’s right. What was I thinking…"
    show s1c43 with dissolve
    Mi "Sorry for the inconvenience."
    Mi "I’ll speak with your father later."
    show s1c45 with dissolve
    Fl "It’s fine."
    Fl "I like stacking debts on him."
    Fl "He pays them back. Eventually."
    show s1c46 with dissolve
    mc "You look way too calm."
    show s1c48 with dissolve
    Fl "After that punch…"
    pause 1.1
    Fl "I decided not to test her limits."
    Fl "Figured I’d cool it."
    show s1c47 with dissolve
    mc "That’s it? You just… decided to calm down?"
    scene s1c48 with dissolve
    Fl "I ran the risk. Made the call."
    Fl "Oh! Perfect example, actually."
    show s1c49 with dissolve
    Fl "Remember that. You’ll need it where we’re going."
    Fl "Come on."
    Fl "We’ve got work to do."
    stop sounds1
    stop sounds2 
    stop sound


label flashback:
    play sounds1 towerambient loop volume 0.2
    play music towers fadein 8.2
    scene black with dissolve
    pause 3.0
    
    show s1bo1 with dissolve
    pause 3.0
    show s1bo2 with dissolve
    h "..."
    play sounds2 stepmc
    show s1bo3 with dissolve
    Mi "Hey, Liv…"
    Mi "Are you alright?"
    play sounds2 stepmc
    show s1bo4 with dissolve
    h "Hm? Yeah."
    h "Just… something from my past."
    pause 1.1
    h "So… what did you want to talk about, Mir?"
    play sounds2 sittingchair
    show s1bo6 with dissolve
    pause 1.1
    show s1bo7 with dissolve
    Mi "Why… are you so attached to him?"
    play sounds rustling2
    show s1bo5 with dissolve
    h "You mean the old man?"
    h "Since when are you so curious?"
    scene s1bo7 with dissolve
    Mi "You and him…"
    pause 1.1
    Mi "It’s more than just a team."
    play sounds rustling2
    show s1bo8 with dissolve
    h "Well, look at that…"
    h "Mir, you’re getting curious."
    show s1bo9 with dissolve
    pause 1.1
    scene s1bo8 with dissolve
    h "You know… it’s a long story."
    show s1bo10 with dissolve
    Mi "…I understand."
    show s1bo11 with dissolve
    pause 1.2
    show s1bo13 with dissolve
    h "..."
    scene s1bo12 with dissolve
    h "Before I start… tell me something."
    h "What are we to you?"
    show s1bo13 with dissolve
    Mi "..."
    Mi "…A team, I suppose."
    play sounds clothess
    show s1bo14 with dissolve
    pause 1.4
    show s1bo15 with dissolve
    h "Huh… funny. You used to be against that."
    show s1bo17 with dissolve
    h "So what changed?"
    scene s1bo10 with dissolve
    Mi "You showed me…"
    pause 1.1
    Mi "Through your actions."
    scene s1bo13 with dissolve
    h "..."
    h "Well… yeah. The story."
    h "Long story short… I owe him."
    pause 1.1
    h "But if I’m being honest…"
    stop music fadeout 5.3
    play music1 mansoul1 fadein 3.0 volume 0.7
    scene s1bo12 with dissolve
    h "It started long before we ever met."
    scene black with dissolve
    pause 1.0
    show s1bo24 with dissolve
    h "We were poor."
    h "The kind that sticks to your bones and doesn’t let go."
    h "I don’t remember my father."
    h "And honestly? Good."
    show s1bo25 with dissolve
    h "He was a bastard."
    h "Only decent thing he ever did was pay off our debts… then disappear."
    scene s1bo12 with dissolve
    h "Mom handled the rest."
    h "Took whatever work she could get."
    h "Cleaning. Lifting. Bleeding hands and sleepless nights."
    h "Still smiled through it."
    h "Kept saying we had to live. Laugh."
    h "But mom didn’t last long."
    h "Work took everything out of her."
    show s1bo25 with dissolve 
    pause 1.2
    h "..."
    show s1bo26 with dissolve
    h "School?"
    h "Hell."
    h "Bullies. Looks. Whispers."
    show s1bo21 with dissolve
    h "Changed schools more times than I can count."
    scene s1bo8 with dissolve
    h "Truth is… I didn’t transfer."
    h "I got kicked out."
    play sounds whoosh
    play sounds3 punch1
    show s1bo27 with CropMove(time=0.2, mode='slideleft') 
    h "Who's the ugly little freak now, huh?! Come on, say something!"
    play sounds whoosh
    scene s1bo6 with CropMove(time=0.2, mode='slideright') 
    Mi "..."
    scene s1bo7
    Mi "That explains... {w=0.7}a lot."
    scene s1bo8 with dissolve
    h "That anger?"
    h "Wasn’t about me."
    h "It was about her."
    h "My sister."
    scene black with dissolve 
    h "Nobody touches her."
    h "Ever."
    play sound drc volume 0.6
    show s1bo28 with dissolve
    h "I'm home."
    show s1bo30 with dissolve
    C "You’re late."
    C "Something happen?"
    show s1bo31 with dissolve
    h "Nah, nothing serious."
    h "Just had to deal with a couple of idiots."
    h "Don’t worry."
    h "Handled it."
    show s1bo32 with dissolve
    C "Well… if you say it’s nothing, I’ll pretend I believe you."
    C "Just hope your ‘nothing’ didn’t end with someone in a hospital."
    show s1bo33 with dissolve
    C "Because if they decide to press charges..."
    C "We’re screwed. You know that, right?"
    show s1bo34 with dissolve
    h "Oh?"
    h "Is that concern I’m hearing?"
    h "Wow… my little sister’s going soft on me."
    h "Cute."
    show s1bo35 with dissolve
    h "(She always felt older than me.)"
    h "(Smarter.)"
    h "(Sharper.)"
    h "(Saw things I didn’t.)"
    show s1bo36 with dissolve
    h "…I got lucky, you know that?"
    show s1bo37 with dissolve
    h "Without you… I’d be screwed."
    show s1bo38 with dissolve
    h "Probably dead."
    h "Or worse."
    show s1bo39 with dissolve
    pause 0.5
    show s1bo40 with dissolve
    h "…Hey."
    h "What’s up?"
    show s1bo41 with dissolve
    C "I KNEW IT!"
    C "That smell, your sleeves! That’s blood again, isn’t it?!"
    show s1bo42 with dissolve
    C "You got into another fight? Seriously?!"
    C "How many times are we doing this?!"
    C "Sit. Down."
    C "Don’t argue, I’m getting the med kit."
    C "Last thing we need is you rotting from an infection."
    scene s1bo7 with dissolve
    Mi "She really cares for you."
    scene s1bo12 with dissolve
    h "After that…"
    pause 1.1
    h "She was all I had."
    show s1bo43 with dissolve
    C "So? What was it this time?"
    C "Was there really no other way?"
    C "Or do your fists just solve everything now?"
    show s1bo45 with dissolve
    h "I’m sorry..."  
    show s1bo44 with dissolve
    C "Hey, look at me when I’m talking to you!"
    show s1bo46 with dissolve
    h "(I had a plan. A stupid one.)"
    h "(Drop out. Get a job.)"
    h "(Help us survive.)"
    h "(Pay for Anya’s future.)"
    show s1bo47 with dissolve
    h "Anya..."
    show s1bo48 with dissolve
    C "What?"
    show s1bo49 with dissolve
    h "What if I just quit school and got a job?"
    h "Help Mom out a bit… take some weight off her."
    h "We could save up."
    h "For your college."
    h "You’ve always wanted that, right?"
    show s1bo50 with dissolve
    h "Ow!"  
    show s1bo51 with dissolve
    C "Stop moving."
    C "And no, you’re not dropping out."
    C "Don’t make dumb decisions because you think you’re helping."
    show s1bo52 with dissolve
    C "Because knowing you, you’d end up in some disgusting strip club."
    C "Or worse."
    scene s1bo12 with dissolve
    h "She never sugarcoated anything."
    h "Brutally honest. Always."
    h "Still is."
    scene s1bo6 with dissolve
    h "By the time I met [mc]… I was desperate."
    h "Tried everywhere."
    scene s1bo12 with dissolve
    h "Didn’t matter."
    h "Every place wanted the same thing—"
    h "a stupid piece of paper."
    h "Even for a basic job."
    scene s1bo13 with dissolve
    h "..."
    scene s1bo12 with dissolve
    h "Then one night…"
    h "Rain pouring like hell…"
    h "I met him."
    scene s1bo14 with dissolve
    pause 1.2
    scene s1bo15 with dissolve
    h "You know what [mc] told me that night?"
    scene s0l79 with dissolve
    h "He said, ‘Sometimes, spilling your guts to a stranger is the healthiest thing you can do.’"
    scene s0l80 with dissolve
    h "(Back then I thought, what a weirdo.)"
    scene s0l80 with dissolve
    h "You're kind of strange, you know."
    h "(And he just replied...)"
    scene s0l79 with dissolve
    mc "My wife’s a crazy scientist… and I’m just a bar owner."
    mc "Can’t even find someone to hire — funny, right?"
    mc "Does that make me strange? Yeah."
    mc "Do I care? Not really."
    scene s0l83 with dissolve
    h "..."
    h "You’re looking for... {w}an employee?"
    scene s0l82 with dissolve
    mc "Yeah, been a couple of weeks now, and I still can’t find anyone."
    scene s1bo12 with dissolve
    h "I couldn’t help it."
    h "And I just…"
    pause 1.1
    h "laughed."
    h "Because it made sense."
    scene s1bo13 with dissolve
    h "..."
    scene s1bo12 with dissolve
    h "...He gave me a place."
    h "A job."
    h "Food that wasn’t stolen or expired."
    h "And silence."
    h "No questions."
    h "No judgment."
    h "Just… space."
    scene s1bo13 with dissolve
    h "..."
    scene s1bo12 with dissolve
    h "And sometimes…"
    h "that’s all you need."
    h "To start again."
    
    stop music1 fadeout 3.2


label street3:
    $ persistent.chapter_act1_scene += 1
    scene black with dissolve
    play sound cybernight loop volume 0.4
    
    pause 3.0
    
    "Sector 5-S. Down in the Lower Level. The slums."
    show s1c111 with dissolve
    show 7yr with dissolve
    Fl "Oh please. It’s just a taxi."
    hide 7yr with dissolve
    show s1c113 with dissolve
    mc "Taxi? That wasn’t a taxi." 
    mc "We were diving straight down, headfirst."
    show s1c112 with dissolve
    Fl "Oh, relax. It wasn’t that bad."
    Fl "Well… for me, anyway."
    scene s1c113 with dissolve
    mc "Right… just casually mentioning we almost slammed into a couple of buildings."
    mc "Totally normal."
    show s1c119 with dissolve
    Fl "Anyway..."
    play music sneakysnitch volume 0.5 fadein 3.0
    show s1c122 with dissolve
    Fl "So? Still shaking, or did your stomach finally find its assigned quadrant again?"
    play sounds2 rustling2
    show s1c123 with dissolve
    mc "Mostly stable… though there’s still a bit left—"
    show s1c126 with dissolve
    play sounds2 vomits volume 0.2
    show s1c128 with dissolve
    mc "BLEEUUUGH."
    show s1c129 with dissolve
    Fl "Oh, that’s adorable."
    Fl "Nothing like a near-death experience to really bring people together."

    Fl "Take your time."
    Fl "This alley’s not going anywhere."

    Fl "Smells like death, rust, and poor life choices."
    Fl "You’ll fit right in."
    stop music fadeout 2.5
    show s1c130 with dissolve
    mc "Alright, alright. I’m coming."
    play sounds1 whoosh
    show s1c131 with dissolve
    pause 1.0
    show s1c132 with dissolve
    pause 1.0
    show s1c134 with dissolve
    Fl "Better?"
    play sounds1 dronescan volume 0.2 fadein 2.0 loop
    show s1c134 with dissolve
    Fl "Or are you developing a taste for dumpsters and industrial decay?"
    show s1c135 with dissolve
    mc "Ha-ha." 
    mc "Mocking the wounded. Very noble of you."
    mc "But seriously, what the hell is that?"
    show s1c137 with dissolve
    ss "Scanning..."
    show s1c139 with dissolve
    Fl "That?"
    Fl "That’s our friendly neighborhood sky warden."

    Fl "Fully autonomous, super-efficient."
    show s1c138 with dissolve
    mc "And what exactly does it do?"
    scene s1c139 with dissolve
    Fl "It scans everything."
    Fl "Docs, DNA… probably your worst decisions too."
    show s1c140 with dissolve
    Fl "And if something doesn’t line up?"
    Fl "It calls in backup."
    scene s1c139 with dissolve
    Fl "Unless it glitches."
    Fl "Which it does."
    show s1c141 with dissolve
    Fl "More often than they’ll ever admit."
    show s1c142 with dissolve
    Fl "If your eyes start burning?"
    Fl "Run."
    Fl "No questions. Just run."
    scene s1c141 with dissolve
    mc "And how long does it take?"
    show s1c143 with dissolve
    Fl "Depends."
    Fl "Usually instant."
    stop sounds1 fadeout 5.0 
    show s1c144 with dissolve
    mc "..."
    play sounds1 footstep volume 2.0
    show s1c146 with dissolve
    pause 1.0
    play sounds2 hitfacefriendly volume 0.1
    show s1c147 with dissolve
    pause 1.0
    play sounds2 rustling2
    show s1c149 with dissolve
    Fl "Rule one."
    Fl "Stay sharp."
    Fl "People who drift off don’t last long here."
    play music eos2 fadein 3.4 
    scene s1c148 with dissolve
    mc "Noted."
    mc "But why are we here?"
    play sounds1 footstep volume 0.6
    show s1c150 with dissolve
    Fl "Because of you, actually."
    Fl "So tell me… what does it look like?"
    mc "Who?"
    Fl "Don’t play dumb."
    Fl "I mean the Ark."
    play sounds1 footstep volume 0.6
    show s1c152 with dissolve
    mc "The Ark?"
    mc "Looks like a ship, I guess?"
    Fl "…You’re weird."
    Fl "Most people thought it was a myth."
    Fl "Others would tear each other apart to be in your place."
    play sounds1 footstep volume 0.6
    show s1c153 with dissolve
    mc "I never asked for any of this."
    Fl "Yeah."
    Fl "I’m a little jealous."
    play sounds1 footstep volume 0.6
    show s1c154 with dissolve
    mc "Tell me, this Ark of yours… what is it?"
    play sounds1 footstep volume 0.6
    show s1c155 with dissolve
    Fl "No idea."
    Fl "Just rumors stacked on rumors."
    mc "The most popular one?"
    Fl "The popular one?"
    Fl "Something about eternal life."
    Fl "Or whatever people tell themselves to sleep better."
    play sounds2 rustling2 volume 0.4
    show s1c156 with dissolve
    mc "And people actually believe that?"
    Fl "Maybe."
    Fl "Out here, belief isn’t optional."
    Fl "It’s survival."
    Fl "And the ones who know how to use that…"
    Fl "they live in places like this."
    show s1c157 with dissolve
    mc "How does that connect… to the slums?"
    Fl "Directly."
    Fl "There’s someone here… a ‘lizard’."
    Fl "They might help."
    play sounds1 footstep volume 0.6
    show s1c158 with dissolve
    mc "A lizard?"
    Fl "You’ll see."
    Fl "Try to keep up."
    show s1c159 with dissolve
    pause 0.5
    show s1c160 with dissolve
    a "..."
    
    
    play sounds1 neonsound loop fadein 3.0 volume 0.3
    show s1c164 with dissolve
    Fl "And here we are."
    Fl "First stop on our charming little tour."
    show s1c165 with dissolve
    pause 1.0
    show s1c178 with dissolve 
    mc "..."
    show s1c166 with dissolve
    mc "Wait... isn’t this just a strip cl—"
    play sounds2 rustling2 volume 0.4
    show s1c170 with dissolve
    Fl "..."
    show s1c171 with dissolve
    Fl "No, no, don’t get ahead of yourself." 
    Fl "First, it’s not what you think."
    Fl "And second, I’m going in alone." 
    Fl "I’ll grab what we need and scope out the next step."
    mc "And the reason I can’t go in is…?"
    play sounds2 rustling2 volume 0.4
    show s1c172 with dissolve
    Fl "When’s the last time you looked in a mirror?"
    Fl "You’re wearing Inquisition gear."
    Fl "If I walk in with you, the whole place goes loud."
    Fl "And I don’t feel like cleaning up a scene tonight."
    
    Fl "You?"
    Fl "You stay right here."
    Fl "Don’t touch anything."
    Fl "Don’t talk to anyone."
    Fl "Stand still."
    Fl "Look… vaguely competent."
    show s1c175 with dissolve
    Fl "I’ll be back before your brain finds a new way to break."
    show s1c177 with dissolve
    mc "Stand around and do nothing."
    mc "Sounds like a dream job."
    stop music fadeout 3.0
    show s1c176 with dissolve
    mc "..."
    stop sounds1

    scene black with dissolve
    pause 1.5
    #A couple of hours later... 
    play music mecd1 fadein 4.0
    show s1dd8 with dissolve
    show 7yr with dissolve
    mc "..."
    play sounds2 rustling2 volume 0.4
    show s1dd9 with dissolve
    mc "(‘Wait right here,’ she said.)"
    play sounds2 rustling2 volume 0.4
    show s1dd10 with dissolve
    mc "(‘Won’t be long,’ she said…)"
    show s1dd11 with dissolve
    mc "So how long exactly am I supposed to stand here?"
    show s1dd12 with dissolve
    play sounds2 lighter
    show s1dd13 with dissolve
    play sounds1 smoking
    show s1dd14 with dissolve
    mc "(Get it together.)"
    mc "(So… what have I figured out so far?)"
    show s1dd2 with dissolve

default question = 0
default question_what_happened = False
default question_world = False
default question_lora = False
default question_boss = False


label choice1:
    menu: 
        
        "What Happened" if not question_what_happened:
            $ question +=1
            $ question_what_happened = True
            play sounds1 smoke
            scene s1dd3 with dissolve
            mc "(Azarkhan nearly ripped me to pieces.)" 
            mc "(Should’ve died. Should’ve just stayed dead.)"
            scene s0b59 with dreamyzoom
            show memoryframe with dissolve
            mc "(He killed me, my son...)" 
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            scene s0b100 with dreamyzoom
            show memoryframe with dissolve
            mc "(And if it weren’t for that guy… Olivia would’ve died too.)"
            mc "(That guy…)"
            mc "(Why him?)"
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(Lora’s from here… and he’s the one who dragged me back here too...)"
            scene s1s13 with dreamyzoom
            show memoryframe with dissolve
            mc "(Dragged… hell, more like pulled me back from the dead.)"
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(Again.)" 
            mc "(But why me?)"
            scene s1b165 with dreamyzoom
            show memoryframe with dissolve
            lad "Find a way out."
            lad "Then we’ll talk."
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(A way out… What did she mean by that?)"
            mc "(I don’t get it…)"

            if question >= 4:
                jump HelpArc
            else:
                jump choice1
            
        "Where am I?" if not question_world:
            $ question +=1
            $ question_world = True
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(This isn’t Earth. That much is clear.)"
            mc "(But life here… it’s a damn nightmare.)"
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            
            scene s1rew259 with dreamyzoom 
            show memoryframe with dissolve
            Mi "Every day… millions die at the front."
            scene s1rew270 with dreamyzoom 
            show memoryframe with dissolve
            Mi "Saving lives."
            Mi "Killing monsters."
            scene s1rew269 with dreamyzoom 
            show memoryframe with dissolve
            mc "(A human life here is worth less than a box of ammo.)" 
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve

            scene s1rew1 with dreamyzoom 
            show memoryframe with dissolve
            mc "(And yet…)"
            scene s1rew111 with dreamyzoom 
            show memoryframe with dissolve
            mc "(This world… it’s something else.)"
            scene s1rew77 with dreamyzoom 
            show memoryframe with dissolve
            mc "(At least on the surface.)"
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(But the deeper you go, the more you see how rotten it really is.)"
            scene s1rew276 with dreamyzoom 
            show memoryframe with dissolve
            gg "Were you that desperate to steal my food—"
            scene s1rrew313 with dreamyzoom 
            show memoryframe with dissolve
            g "Look at you… fussing over some elf girl..."
            scene s1b10 with dreamyzoom
            show memoryframe with dissolve
            Mi "…Not from people like you."
            Mi "…You’re human."
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            if question >= 4:
                jump HelpArc
            else:
                jump choice1

        "Lora" if not question_lora:
            $ question +=1
            $ question_lora = True
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(The Mistress… that’s what everyone calls her.)" 
            mc "(Said Lora is alive. No proof. Just words.)"
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(But from what I’ve pieced together…)"
            scene s1rew56 with dreamyzoom 
            show memoryframe with dissolve 
            Mi "…He’s like the other two scientists."
            scene s1rew108 with dreamyzoom 
            show memoryframe with dissolve 
            mc "What...Lora...doing..."
            Mi "Saving lives."
            Mi "Killing monsters."
            scene s1rew273 with dreamyzoom 
            show memoryframe with dissolve 
            mc "Why take that kind of risk…"
            Mi "To survive."
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(Lora was my compass.)" 
            mc "(My anchor in a world that never stopped spinning.)" 
            scene s1rew170 with dreamyzoom 
            show memoryframe with dissolve 
            L "I can feel it spreading…"
            scene s1rew178 with dreamyzoom 
            show memoryframe with dissolve 
            mc "Lora was under surveillance."
            Mi "…She was being hunted."
            scene s1dd3 with dissolve
            mc "(Without her... {w}I’m lost.)"

            if question >= 4:
                jump HelpArc
            else:
                jump choice1
            

        "The Lady" if not question_boss:
            $ question +=1
            $ question_boss = True
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(The Mistress...)"
            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(She keeps to the shadows.)" 
            show s1pp23 with dreamyzoom
            show memoryframe with dissolve
            o "You don’t want to cross her on a bad day."
            o "The Lady."

            mc "(People talk about her like she’s a ghost.)"
            mc "(Something that only exists when it chooses to.)"

            play sounds1 smoke
            scene s1dd2 with dissolve
            pause 1.0
            scene s1dd3 with dissolve
            mc "(I know next to nothing.)"
            mc "(And that scares me more than I’d like to admit.)"
            mc "(What does she want from me?)" 
            mc "(Why am I worth the trouble?)"
            if question >= 4:
                jump HelpArc
            else:
                jump choice1

     
default ivy_help = False
default ivy_help_first = False
default ivy_help1 = False
    

    
label HelpArc:
    if ivy_help_first == False:
        stop music fadeout 3.0
        show s1dd3 with dissolve
        a "Please... no! Don’t!"
        show s1dd4 with dissolve
        pause 1.0
        scene s1dd1 with dissolve
        pause 1.0

        image Ivystreet = Movie(channel="movie_dp", loop = False, play="video/Ivystreet.webm")
        show Ivystreet with dissolve
        $ renpy.pause(2.1, hard=True)

        scene s1dd7 with dissolve
        aa "Stop! She hasn’t done anything—!"
        


    menu:
            "Help":
                
                mc "(…No.)"
                pause 1.1
                mc "(Damn it.)"
                mc "(I can't just stand here.)"
                $ ivy_help1 = True
                scene black

                image mcka = Movie(channel="movie_dp", loop = False, play="video/mcka.webm")
                show mcka with dissolve
                $ renpy.pause(10.5, hard=True)

                scene s1dd15 with dissolve
                pause 1.0
                play sound raincity3 loop
                show s1dd17 with dissolve
                mc "(…Hands still shaking.)"
                show s1dd18 with dissolve
                aa "SISTER!"
                show s1dd19 with dissolve
                pause 0.8
                
                show s1d11 with dissolve
                aa "Hey, are you alright?"
                aa "Wake up, we need to get out of here."
                play sounds1 footstep volume 0.6
                
                show s1d12 with dissolve
                Fl "What the hell happened here?!"
                play sounds1 footstep volume 0.6
                show s1d13 with dissolve
                Fl "Oh, fantastic."
                Fl "Absolutely fantastic."
                Fl "Do you have any idea what you just did?"
                pause 1.1
                Fl "This wasn’t a bar fight."
                show s1d14 with dissolve
                play sounds1 footstep volume 0.6
                show s1d15 with dissolve
                Fl "Which part of “stand still and don’t interfere” did you miss?!"
                show s1d16 with dissolve
                mc "I wasn’t going to stand there and watch them beat a girl."
                show s1d17 with dissolve
                mc "So I stepped in."
                show s1d18 with dissolve
                mc "That’s it."
                show s1d19 with dissolve
                pause 0.5
                show s1d20 with dissolve
                Fl "..."
                show s1d21 with dissolve
                Fl "...Damn it."
                Fl "You really don’t do things halfway, do you?"
                show s1d22 with dissolve
                mc "I’ll handle it."
                Fl "Why do I even bother…"
                Fl "Stay close. Now."
                play music kmc fadein 2.0
                show s1d23 with dissolve
                ss "Flora! You’ve got a serious problem." 
                ss "A strike team’s en route fully armed, no patience."
                play sounds1 grouprun 
                show s1d29 with dissolve
                pause 1
                show s1d30 with dissolve
                pause 1
                stop sounds1
                scene s1d21 with dissolve
                Fl "Then we run."
                scene s1d20 with dissolve
                Fl "..."
                show s1d24 with dissolve
                Fl "That’s Plan B, by the way."
                show s1d25 with dissolve
                Fl "I’ll cover the rest. Find you later."
                Fl "Move."
                pause 1.1
                Fl "Now."

                menu:
                    "Stay":
                        $ ivy_help = True
                        
                        show s1d32 with dissolve
                        aaa "Hey-hey, can you move? Stay with me, alright?"
                        show s1d33 with dissolve
                        a "I… yeah… I think so."
                        a "Everything’s spinning… What the hell happened?"
                        scene s1d32 with dissolve
                        aa "One of those peacekeeper bastards decided you were his."
                        aa "You fought back, and he snapped."
                        aa "Didn’t expect inqusition to step in. Hell, no one did."
                        show s1d34 with dissolve
                        a "...He saved me?"
                        show s1d35 with dissolve
                        aa "Didn’t even hesitate."
                        aa "Just, moved."
                        show s1d36 with dissolve
                        aa "You have no idea what that means to us." 
                        aa "If you ever need a place to hide, Sector 6-S. {w}Blue Moon." 
                        aa "Tell them Mira sent you."
                        play sounds1 footstep volume 0.6
                        show s1d37 with dissolve
                        aa "Go. Now."
                        play sounds1 mmove
                        show s1d40 with dissolve
                        g "Sir, targets are pulling back."
                        show s1d41 with dissolve
                        gg "Forget them. Focus on the inqusition."
                        show s1d42 with dissolve
                        g "On your knees."
                        pause 1.1
                        g "Now."
                        show s1d38 with dissolve
                        g "No sudden moves."
                        g "Don’t make this worse than it already is."
                        play sounds2 clench volume 0.3
                        show s1d39 with dissolve
                        pause 1.0

                        stop music fadeout 1.0
                        stop sound fadeout 1.0

                        scene black with dissolve
                        pause 3.0

                        play music eos3 fadein 7.0
                        show s1d43 
                        pause 1.0
                        show s1d44 with dissolve
                        pause 1.0
                        play sounds2 rustling2 volume 0.4
                        scene s1d43 with dissolve
                        mc "Ninety-seven… ninety-eight…"
                        play sounds2 rustling2 volume 0.4
                        scene s1d43 with dissolve
                        pause 1.0
                        play sounds2 rustling2 volume 0.4
                        show s1d45 with dissolve
                        pause 1.0
                        play sound concstep1
                        show s1d46 with dissolve
                        pause 1.0
                        show s1d47 with dissolve
                        g "This way, please."
                        play sounds1 scifidooropen2
                        play sound concstep1
                        show s1d48 with dissolve
                        pause 1.0
                        
                        show s1d49 with dissolve
                        pause 1.0
                        show s1d50 with dissolve
                        g "Here he is. This the one?"
                        show s1d51 with dissolve
                        Mi "Yes, it’s him."
                        g "..." 
                        play sound concstep1
                        show s1d52 with dissolve
                        g "Alright, you’ve got 15 minutes."
                        show s1d53 with dissolve
                        Mi "Thanks."
                        play sounds1 scifidooropen2
                        
                        show s1d54 with dissolve
                        mc "Didn’t go as planned."
                        play sounds2 rustling2 volume 0.4
                        show s1d57 with dissolve
                        Mi "You stood up for me… so I returned the favor."
                        Mi "That’s what a team does… right?"
                        show s1d59 with dissolve
                        mc "Already getting used to the idea?"
                        mc "Good."
                        show s1d60 with dissolve
                        mc "What about the girl?"
                        play sounds2 rustling2 volume 0.4
                        scene s1d58 with dissolve
                        mc "The one they were beating to a pulp. I need to know if she made it."
                        scene s1d60 with dissolve
                        Mi "She’s fine." 
                        play sounds2 rustling2 volume 0.4
                        scene s1d59 with dissolve
                        mc "Good."
                        show s1d54 with dissolve
                        Mi "And… it’s a good thing you saved her."
                        scene s1d57 with dissolve
                        pause 1.0
                        play sounds2 rustling2 volume 0.7
                        scene s1d59 with dissolve
                        mc "What do you mean?"
                        scene s1d60 with dissolve
                        Mi "She… works for someone very important."
                        scene s1d58 with dissolve
                        mc "Care to elaborate?"
                        scene s1d60 with dissolve
                        Mi "..."
                        play sounds2 rustling2 volume 0.7
                        show s1d61 with dissolve
                        pause 1.0
                        show s1d62 with dissolve
                        Mi "…Her name is Ember."
                        Mi "She’s the one you were supposed to meet."
                        mc "..."
                        play sounds2 rustling2 volume 0.7
                        show s1d63 with dissolve
                        pause 1.0
                        show s1d64 with dissolve
                        pause 1.0
                        play sounds2 rustling2 volume 0.7
                        show s1d65 with dissolve
                        pause 1.0
                        show s1d66 with dissolve
                        mc "The lizard?"
                        show s1d67 with dissolve
                        Mi "…Forget that word."
                        Mi "If you don’t want to die."
                        scene s1d66 with dissolve
                        mc "That bad?"
                        scene s1d67 with dissolve
                        Mi "If she decides to kill you…"
                        Mi "no one will stop her."
                        Mi "No one."
                        scene s1d66 with dissolve
                        mc "…And you’re sending me to her anyway. Why?"
                        play sound bodytap
                        show s1d68 with dissolve
                        Mi "If anyone knows anything… it’s her."
                        Mi "You won’t get much from the Lady… but Ember is an informant."
                        Mi "My teacher pulled some strings."
                        Mi "We’ve arranged a meeting."
                        play sounds1 scifidooropen2
                        show s1d69 with dissolve
                        g "Sorry to interrupt, ma’am. You’re free to go."

                        stop music fadeout 3.0

                        play music1 zargo fadein 3.0

                        play sound emptyroom loop

                        show s1d159 with dissolve
                        pause 1.0   
                        show s1d161 with dissolve
                        pause 1.0
                        show s1d163 with dissolve
                        
                        o "BRING ME THOSE SCUMS! I won’t let this stand!"
                        play sounds2 rustling2 volume 0.4
                        show s1d165 with dissolve
                        g "Sir, please—"
                        show s1d164 with dissolve
                        o "You had no idea who she was working for?!"
                        o "What the hell were you thinking?!"
                        play sounds2 rustling2 volume 0.4
                        show s1d166 with dissolve
                        g "But... she was just an elf, sir..."
                        show s1d167 with dissolve
                        o "...What did you say?"
                        show s1d169 with dissolve
                        g "She’s an elf—"
                        show s1d170 with dissolve
                        o "Say it again."
                        play sounds2 rustling2 volume 0.4
                        show s1d171 with dissolve
                        g "She’s—"
                        play sounds1 punch2
                        show s1d172 with vpunch
                        pause 1.5
                        play sounds2 tablesq
                        show s1d173 with dissolve
                        o "AN ELF, YOU SAY?"
                        o "So that makes it fine?"
                        o "Get out. Now."
                        o "Before I personally send you to have a word with her."
                        show s1d174 with dissolve
                        Mi "She’ll be furious… when she finds out."
                        play sounds1 scifidooropen2
                        show s1d175 with dissolve
                        o "I’ve already sent my apologies."
                        pause
                        o "…let’s hope that’s enough."
                        mc "(All that… over one beating.)"
                        play sounds1 bodytap
                        show s1d176 with dissolve
                        o "Ah… there you are."
                        o "Good to see you still in one piece, my friend."
                        o "Sorry you had to walk in on that."
                        o "We’re usually… a bit more civilized than this."
                        show s1d177 with dissolve
                        mc "Yeah… not exactly a pleasant experience."
                        show s1d178 with dissolve
                        o "How’s your eye holding up?"
                        o "You taking the meds?"
                        mc "..."

                        scene s1d177 with dissolve
                        mc "Slipped my mind."
                        o "Yeah… figures."
                        play sounds1 bodytap
                        scene s1d176 with dissolve
                        o "When you step out, don’t forget to take them."
                        o "Seriously."
                        show s1d182 with dissolve
                        Mi "We should move."
                        Mi "We’re running late."
                        show s1d183 with dissolve
                        o "Take care of yourself out there."
                        o "I expect you back in one piece."
                        show s1d180 with dissolve
                        mc "...thanks."
                        stop music1 fadeout 3.1
                        scene black with dissolve
                        pause 2.0
                        
                        play sound concstep1 volume 0.3
                        play music ambrosia fadein 3.4
                        play sounds1 streetevening volume 0.2 loop
                        show s1d124 with dissolve
                        show 7yr with dissolve
                        mc "..."
                        play sound concstep1 volume 0.3
                        show s1d126 with dissolve
                        mc "Before I meet… Ember."
                        mc "If I want to walk out alive, what do I need to know?"
                        play sound concstep1 volume 0.3
                        show s1d127 with dissolve
                        Mi "Tell me…"
                        Mi "Do you know how to keep your mouth shut when it matters?"
                        play sound concstep1 volume 0.3
                        show s1d130 with dissolve
                        mc "Depends on the situation."
                        play sound concstep1 volume 0.3
                        show s1d131 with dissolve
                        Mi "We have something she might want."
                        Mi "Information."
                        play sound concstep1 volume 0.3
                        show s1d132 with dissolve
                        Mi "Control what you say."
                        Mi "And say as little as possible."
                        show s1d133 with dissolve
                        Fl "Like he’s capable of that..."
                        show s1d134 with dissolve
                        Fl "Did you forget how she plays?"
                        Fl "And don’t even tell me he’s walking in like that."
                        play sound concstep1 volume 0.3
                        show s1d136 with dissolve
                        Mi "That’s not what you should be worried about."
                        Mi "Your father already took care of his clearance."
                        Mi "Your job is to keep her in—"
                        show s1d135 with dissolve
                        mc "Alright, hold on."
                        mc "Short version, keep my mouth shut, right?"
                        mc "And if I don’t?"
                        scene s1d134 with dissolve
                        Fl "Death."
                        Fl "Immediate."
                        show s1d137 with dissolve
                        Mi "You won’t even get the chance to react."
                        Mi "And if you do…"
                        Mi "you’ll regret surviving."
                        show s1d138 with dissolve
                        mc "If the odds of dying are that high… why take the risk?"
                        mc "For information that might not even be worth it?"
                        show s1d139 with dissolve
                        Mi "..."
                        show s1d140 with dissolve
                        Mi "You asked for answers."
                        Mi "This is the price."
                        show s1d141 with dissolve
                        Mi "If you don’t agree… you can walk away."
                        Mi "But—"
                        show s1d142 with dissolve
                        show s1d143 with dissolve
                        mc "Fair enough."
                        mc "Without your help, I’d still be rotting in that hole."
                        show s1d144 with dissolve
                        Mi "..."
                        show s1d145 with dissolve
                        Mi "…Don’t make me pull you out again."
                        play sound concstep1 volume 0.3
                        show s1d155 with dissolve
                        mc "Then I won’t screw it up."

                        jump bar_cyber

            #         "Leave":

            #             show s1d26 with dissolve
            #             mc "(I told myself I wouldn’t get involved. I made a promise — no more detours, no more playing the hero.)"
            #             mc "(And yet… here I am. Again.)"
            #             show s1d27 with dissolve
            #             mc "(I didn’t help. I didn’t stop them. I just walked away.)"
            #             mc "(Maybe I preserved my cover. Maybe I saved myself. But I lost something too…)" 
            #             mc "(Whatever was left of my conscience.)"
            #             mc "(Now’s not the time. Later. Process it later. Right now, I need to disappear.)"
            #             show s1d28 with dissolve
            #             pause 0.5

            #             scene black with dissolve
            #             stop music fadeout 1.0


            #             image mcrun = Movie(channel="movie_dp", loop = False, play="video/mcrun.webm")
            #             show mcrun with dissolve
            #             $ renpy.pause(3.5, hard=True)

                        
            #             play sounds2 wall2
            #             play sounds1 rungroup2
            #             scene s1d93 with dissolve
            #             pause 0.5
                        
            #             show s1d94 with dissolve
            #             mc "..."
            #             show s1d95 with dissolve
            #             Fl "Well, well... Look who crawled back in one piece. Honestly? Wasn’t betting on it."
            #             show s1d96 with dissolve
            #             mc "What’s that supposed to mean?"
            #             show s1d97 with dissolve
            #             show s1d98 with dissolve
            #             Fl "Relax. Just surprised you found this place on your own. I assumed you followed the coordinates I sent."
            #             scene s1d96 with dissolve
            #             mc "Coordinates?"
            #             scene s1d98 with dissolve
            #             Fl "Wait — hold on. You’re saying you {b}didn’t{/b} get them?"
            #             scene s1d96 with dissolve
            #             mc "No. My eye... it pulled me here. Like it knew where I needed to be."
            #             scene s1d98 with dissolve
            #             Fl "...The eye. Right. Of course it did."
            #             Fl "That thing’s more trouble than it’s worth."

            #             Fl "Come on. Let’s move before our welcoming committee decides to throw a second party."
                    
            #             scene black with dissolve
            #             pause 1
            #             stop sound fadeout 1.0
            #             play sounds1 stationaban fadein 2.0 loop

            #             show s1d102 with dissolve
            #             Fl "..."
            #             show s1d103 with dissolve
            #             pause 2.0
            #             show s1d104 with dissolve
            #             Fl "You’ve got that look again."
            #             show s1d105 with dissolve
            #             mc "What look?"
            #             play sounds2 rustling2
            #             show s1d106 with dissolve
            #             Fl "The one that says you’re stuck in your own head. Again."
            #             scene s1d105 with dissolve
            #             mc "I left them behind. The girl. Her sister. I don’t even know if they made it out."
            #             show s1d107 with dissolve
            #             Fl "This city eats people alive. You saved who you could. That’s more than most."
            #             show s1d108 with dissolve
            #             mc "It doesn’t feel like enough."
            #             show s1d109 with dissolve
            #             show s1d110 with dissolve
            #             Fl "It never does."
            #             scene s1d108 with dissolve
            #             mc "Maybe I should’ve—"
            #             scene s1d107 with dissolve
            #             Fl "No. You did what you had to. If you had stayed, you’d be in a body bag right now, and they’d still be in danger." 
            #             Fl "You made the only call you {b}could{/b}."
            #             Fl "But I get it. Guilt clings to you like smoke. Just… don’t let it choke you."
            #             scene s1d108 with dissolve
            #             mc "You ever feel like you were built to do one thing, but life keeps pulling you the other way?"
            #             scene s1d107 with dissolve
            #             Fl "Every damn day."
            #             scene s1d108 with dissolve
            #             mc "I keep wondering if I’m even real. Or just some thread being pulled by something bigger."
            #             scene s1d107 with dissolve
            #             Fl "The stuff of myth, mostly. They’re called the Weavers of Rialt. Supposedly connected to the World Web — an infinite network of realities."
            #             scene s1d108 with dissolve
            #             mc "And you believe in that?"
            #             scene s1d107 with dissolve
            #             Fl "Belief’s a luxury I can't afford. But I {b}have{/b} seen things... things that don't follow the rules."
            #             scene s1d108 with dissolve
            #             mc "And Weavers can navigate it?"
            #             scene s1d107 with dissolve
            #             Fl "The real ones? They don’t navigate it. They bend it."
            #             $ persistent.parallel_threads_ = True 
            #             scene s1d108 with dissolve
            #             show memoryreboot with dissolve 
            #             mc "Sounds like a curse wrapped in a miracle."
            #             scene s1d110 with dissolve
            #             Fl "You’d be surprised how often the two are the same thing."
            #             play sounds2 scifinot
            #             show s1d111 with dissolve
            #             pause 2.0
            #             show s1d112 with dissolve
            #             Fl "Anyway... train’s here."
            #             show s1d113 with dissolve
            #             show s1d114 with dissolve
            #             mc "..."
            #             play sounds2 rustling2
            #             show s1d115 with dissolve
            #             Fl "What? Something wrong?"
            #             play sounds1 footstep volume 0.6
            #             show s1d120 with dissolve
            #             mc "A train? Didn’t peg you for old tech."
            #             Fl "It’s cheap, it’s fast, and it doesn’t ask questions. That’s all I care about."
            #             play sounds1 footstep volume 0.6
            #             show s1d121 with dissolve
                        
            #             mc "Fair point."
            #             Fl "Come on. We’ve got ground to cover. And maybe, if we’re lucky, some answers waiting at the end of the line."
            #             play sound whoosh4
            #             show s1d123 with dissolve
            #             pause 0.5
            #             jump bar_cyber




            # "Refuse" if ivy_help_first == False:
            #     play sounds1 smoke
            #     show s1dd1 with dissolve
            #     pause 2.0
            #     scene s1dd4 with dissolve
            #     mc "(I said I wouldn’t interfere. No more getting involved. No more consequences. But here I am - watching it all unfold... doing nothing.)"
            #     a "Please, don’t! Stop it!"
            #     scene s1dd1 with dissolve
            #     play sounds1 smoke
            #     pause 2.0
            #     scene s1dd4 with dissolve
            #     aa "She didn’t do anything! Let go of her!"
            #     scene s1dd6 with dissolve
            #     a "Help...."

            #     menu:
            #         "Help":
                        
            #             scene s1dd4 with dissolve
            #             aa "..."
            #             $ ivy_help_first = True
                        
            #             jump HelpArc

                        

            #         "Refuse":
                            

            #             scene s1dd1 with dissolve
            #             play sounds1 smoke
            #             pause 2.0
            #             scene s1dd4 with dissolve
            #             a "Let me go! I haven’t done anything!"
            #             scene s1dd7 with dissolve
            #             aa "Sister, no!"
            #             mc "(I made a promise. And I’m not breaking it. Not this time. No matter what it costs them... or me.)"
                        
            #             scene black with dissolve
            #             pause 2.0
            #             show 7yr with dissolve

            #             Fl "Well, well. Look who finally caught up. Miss me?"
            #             mc "...Yeah."

            #             stop sounds1 fadeout 0.5
            #             stop sounds2 fadeout 0.5
            #             stop sound fadeout 0.5
            #             scene black with dissolve
            #             pause 2.0

            #             play music astral fadein 0.5

            #             image scifiship1 = Movie(channel="movie_dp", loop = False, play="video/scifiship.webm")
            #             show scifiship1 with dissolve
            #             $ renpy.pause(6.7, hard=True)
                        
            #             scene s1d70 with dissolve
            #             Fl "Oklaron to [mc]: are you present, or did you check out mid-crisis again?"
            #             play sound metalstep volume 0.3
            #             show s1d71 with dissolve
            #             Fl "No response. Must be a hell of a dream you’re having. Mind letting the rest of us in?"
            #             Fl "Was it my riveting monologue on molecular binding during teleportation that knocked you out?"
            #             Fl "Too dense for your brain to handle?"
            #             play sound metalstep volume 0.3 fadein 0.5
            #             show s1d72 with dissolve
            #             mc "No. I was... listening."
            #             play sound metalstep volume 0.3 fadein 0.3
            #             show s1d74 with dissolve
            #             Fl "Cute answer. Except I never said a word. So what were you really listening to?"
            #             play sound metalstep volume 0.3
            #             show s1d75 with dissolve
            #             Fl "Look, I know I’m... a lot. Loud, reckless, hard to pin down. You don’t have to say it — I already know."
            #             show s1d76 with dissolve
            #             mc "..."
            #             play sounds2 rustling2
            #             show s1d78 with dissolve
            #             Fl "But even so..."
            #             show s1d80 with dissolve
            #             Fl "Ah♥"
            #             show s1d81 with dissolve
            #             mc "..."
            #             show s1d84 with dissolve
            #             Fl "You’re not really here, are you?"
            #             show s1d85 with dissolve
            #             mc "Just... running numbers. Trying to understand the cost."
            #             show s1d86 with dissolve
            #             pause 0.5
            #             show s1d87 with dissolve
            #             pause 0.5
            #             scene s1d86 with dissolve
            #             pause 0.5
            #             scene s1d87 with dissolve
            #             pause 0.5
            #             show s1d88 with dissolve
            #             Fl "..."
            #             play sounds1 slap
            #             show s1d89 with dissolve
            #             Fl "...Well, daydream’s over. Whatever answer you were hoping for — don’t count on getting it tonight."
            #             show s1d90 with dissolve
            #             mc "Don’t act like you weren’t enjoying the silence."
            #             show s1d91 with dissolve
            #             Fl "Only part I enjoyed was not hearing your awful jokes."
            #             Fl "Come on. We've got a mess to clean up."
                                            
                



label bar_cyber:
    $ persistent.chapter_act1_scene += 1
    stop music fadeout 2.0
    scene black with dissolve 
    pause 2.5
    play music sc2d fadein 3.4
    show s1ee14 with dissolve
    show 7yr with dissolve
    mc "Tell me…" 
    mc "What are the odds I die the moment I walk in?"
    hide 7yr with dissolve
    show s1ee1 with dissolve
    Fl "Scared?"
    mc "I don’t know what to expect, and—"
    Fl "Can’t blame you."
    mc "..."
    show s1ee2 with dissolve
    Fl "That means your instincts aren’t completely useless."
    Fl "Don’t get me wrong, I’m not trying to scare you."
    Fl "But about half the people who walk in there?"
    Fl "Don’t walk back out."
    show s1ee3 with dissolve
    mc "How do I make sure I’m in the half that walks out?"
    show s1ee4 with dissolve
    Fl "You already improved your odds."
    Fl "Saving that elf girl bought you a little goodwill."
    scene s1ee3 with dissolve
    mc "I’m serious."
    scene s1ee4 with dissolve
    Fl "Me too."
    scene s1ee3 with dissolve
    mc "Wait. If things go sideways…"
    scene s1ee4 with dissolve
    Fl "Death."
    Fl "You think I’m joking?"
    Fl "I wish I was."
    Fl "But not here."
    Fl "And definitely not with her."
    show s1ee9 with dissolve
    a "Don’t mention Yong."
    show s1ee10 with dissolve
    pause 1.0
    show s1ee11 with dissolve
    pause 1.0
    show s1ee12 with dissolve
    mc "Did I… say something wrong?"
    show s1ee6 with dissolve
    Fl "...Yeah."
    Fl "Stop talking. Seriously."
    Fl "And remember this."
    pause 1.1
    Fl "The less you say—"
    Fl "the longer you live."
    show s1ee8 with dissolve
    mc "..."
    
    

    stop music fadeout 4.5
    play music1 gymnopedieno1 fadein 5.1
    scene black with dissolve
    pause 1.5

    
    play sounds1 ntsound loop 
    show s1e131 with dissolve
    Fl "And here we are." 
    Fl "The bleeding heart of her empire… dressed up like a cheap bar." 
    Fl "Charming, isn’t it?"
    show s1e132 with dissolve
    mc "Doesn’t look like much."
    show s1e133 with dissolve
    Fl "Don’t touch anything. Don’t look too long." 
    Fl "And for the love of your remaining organs, don’t lie."
    show s1e134 with dissolve
    mc "That bad?"
    show s1e135 with dissolve
    Fl "The territory owner’s… Dragon."
    show s1e136 with dissolve
    mc "...You’re serious?"
    mc "And you’re only telling me now?"
    show s1e137 with dissolve
    rey "Lady Flora. A surprise... though not an unwelcome one." 
    rey "You rarely descend to our level these days."
    play sounds2 rustling2 volume 0.4
    show s1e138 with dissolve
    Fl "Ray."
    Fl "Still wearing that charming scowl, I see."
    Fl "We need Emberlyn."
    Fl "Now."
    Fl "And before you ask, I’m not doing this only for him."
    Fl "Lora’s research may explain why his implants accepted him so easily. I want those answers too."
    Fl "Let us in."
    play sounds2 rustling2 volume 0.4
    show s1e140 with dissolve
    rey "You know protocol. No exceptions."
    rey "And this one..."
    play sounds2 rustling2 volume 0.4
    show s1e139 with dissolve
    rey "So… this would be him?"
    show s1e141 with dissolve
    Fl "Yes."
    Fl "My father should’ve mentioned him."
    show s1e142 with dissolve
    rey "I assume you’ve heard the rumors."
    show s1e143 with dissolve
    Fl "We don’t have time for rumors right now—"
    show s1e144 with dissolve
    rey "I’m afraid I can’t allow you inside."
    show s1e145 with dissolve
    Fl "...Wait what?"
    Fl "Why?"
    scene s1e144 with dissolve
    rey "He is… acquainted with that woman."
    rey "That alone would be sufficient cause for his execution."
    rey "And secondly… his attire."
    Fl "..."
    show s1e146 with dissolve
    mc "(whispering) What’s going on?"
    show s1e147 with dissolve
    Fl "Your Lora."
    Fl "That’s what’s happening."
    scene s1e146 with dissolve
    mc "Wh—"
    scene s1e147 with dissolve
    Fl "Later."

    
    if ivy_help == True:
        stop music1 fadeout 1.5
        play sounds2 rustling2 volume 0.4
        play music milehigh fadein 2.3 volume 1
        show s1e154 with dissolve
        i "Is there a problem, Mister Ray? You seem to be detaining our guests."
        show s1e44 with dissolve
        rey "Miss Ivy. A pleasure, as always." 
        rey "We’ve encountered… an unfortunate complication with their clearance."
        rey "And as you know, I do not grant exceptions… without sufficient cause."
        show s1e46 with dissolve
        i "May I ask what the issue is?"
        play sounds2 rustling2 volume 0.4
        show s1e57 with dissolve
        rey "It concerns the scholar… and her ties to the Inquisition."
        rey "Our Lady does not… tolerate the latter."
        show s1e47 with dissolve
        i "Hm… he may dress like them, but he doesn’t act like one."
        i "He helped me earlier today. A small gesture, perhaps, but meaningful."
        show s1e48 with dissolve
        i "I repay my debts — promptly and properly."
        show s1e55 with dissolve
        i "Besides, Miss Flora seems to be vouching for him as well."
        i "I trust her judgment carries weight?"
        play sounds2 rustling2 volume 0.4
        scene s1e57 with dissolve
        rey "I appreciate your willingness to intervene, Miss Ivy… but it is not sufficient."
        show s1e156 with dissolve
        mc "(whispering) So this is about the clothes?"
        scene s1e157 with dissolve
        Fl "(whispering) No."
        Fl "(whispering) Inquisition members actually carry weight here."
        show s1e158 with dissolve
        Fl "(whispering) My father knew that."
        Fl "(whispering) He was trying to give you leverage, but..."
        scene s1e157 with dissolve
        Fl "(whispering) I don’t get it."
        Fl "(whispering) Something’s off."
        Fl "(whispering) It’s like..."
        Fl "(whispering) she’s playing with us."

        show s1e150 with dissolve
        Fl "Hey, dad? You there?"
        Fl "They’re not letting us through..."
        show s1e148 with dissolve
        Fl "..."
        Fl "Yeah. Got it."
        Fl "Putting you through."

        show s1e153 with dissolve
        Fl "Mr. Ray."
        Fl "My father wants a word."
        rey "..."
        rey "Mister Ostorius. A pleasure to hear your voice."
        rey "..."
        rey "...No."
        pause 1.1
        rey "My answer remains unchanged."
        rey "No."
        
        show s1e56 with dissolve
        i "I’ll keep an eye on him myself, Mister Ray."
        play sounds2 rustling2 volume 0.4
        scene s1e57 with dissolve
        rey "Your dedication is noted, but—"
        scene s1e56 with dissolve
        i "On my name, I take full responsibility for him… and anything he does."
        scene s1e57 with dissolve
        rey "Are you certain?"
        scene s1e56 with dissolve
        i "I insist."
        rey "..."
        rey "You do understand what you are placing at stake?"
        play sounds1 bodytap
        show s1e61 with dissolve
        rey "Your name, sir?"
        show s1e63 with dissolve
        mc "[mc]"
        show s1e62 with dissolve
        rey "Once you cross this threshold…"
        rey "you accept her rules."
        rey "And should you overstep…"
        rey "and be put down… we bear no responsibility for your life."
        rey "Do you accept?"
        scene s1e63 with dissolve
        mc "...Understood."
        show s1e64 with dissolve
        rey "This way, Miss Flora. Mister [mc]. On behalf of Lady Emberlyn, welcome."
        rey "You will wait in the reception room."
        rey "Pray that you prove worthy of her time."
        show s1e62 with dissolve
        rey "I will inform Lady Emberlyn of your arrival."

        stop music fadeout 4.5
        scene black with dissolve
        pause 1.2

    else:

        show s1e150 with dissolve
        Fl "Hey, dad? You there?"
        Fl "They’re not letting us through..."
        show s1e148 with dissolve
        Fl "..."
        Fl "Yeah. Fine."
        Fl "Putting you through."

        show s1e153 with dissolve
        Fl "Mr. Ray."
        Fl "My father wants a word."
        rey "..."
        rey "Mister Ostorius. A pleasure to hear your voice."
        rey "..."
        rey "...No."
        pause 1.1
        rey "My answer remains unchanged."
        rey "No."

        rey "Tell me, young man."
        rey "What is it you seek inside?"
        show s1e145 with dissolve
        Fl "We’re here to meet—"
        rey "I addressed him, Miss Flora… not you."
        scene s1e146 with dissolve
        mc "..."
        mc "I want the truth."
        scene s1e153 with dissolve
        rey "The truth…?"
        rey "And what are you prepared to offer in return for entry?"
        mc "Informati—"
        rey "Unacceptable."
        mc "..."
        mc "...It’s already been taken from me."
        mc "I paid with my life."
        pause 1.1
        mc "(…too fast.)"
        rey "..."
        pause 1.1
        rey "...Hm."
        rey "Desperation… is something Lady Emberlyn finds quite appealing."

        show s1e62 with dissolve
        rey "Once you cross this threshold…"
        rey "you accept her rules."
        rey "And should you overstep…"
        rey "and be put down… we bear no responsibility for your life."
        rey "Do you accept?"
        scene s1e63 with dissolve
        mc "...Understood."
        show s1e64 with dissolve
        rey "This way, Miss Flora. Mister [mc]. On behalf of Lady Emberlyn, welcome."
        rey "You will wait in the reception room."
        rey "Pray that you prove worthy of her time."
        show s1e62 with dissolve
        rey "I will inform Lady Emberlyn of your arrival."



        stop music1 fadeout 4.5
        scene black with dissolve
        pause 1.2


            
    
    play sound ntsound loop 
    
    show s1e65 with dissolve
    mc "You alright?"
    Fl "..."
    mc "Flora?"
    show s1e66 with dissolve
    Fl "Ray was acting off."
    scene s1e65 with dissolve
    mc "How so?"
    scene s1e66 with dissolve
    Fl "(whispering) He knew why we were here."
    Fl "(whispering) Knew about you, your uniform… everything."
    Fl "(whispering) But then..."

    scene s1e139 with dreamyzoom
    show memoryframe with dissolve 
    rey "So… this would be him?"

    scene s1e66 with dissolve
    Fl "Something shifted."
    mc "Could be because of Lora?"
    show s1e67 with dissolve
    Fl "...Yeah."
    Fl "That could be it."
    mc "What did she do to deserve that?"
    Fl "She said no to Ember."
    scene s1e65 with dissolve
    mc "Wait… that’s it?"
    show s1e69 with dissolve
    Fl "That’s it?"
    Fl "You really don’t get it, do you..."
    Fl "You don’t say no to her."
    Fl "No one does."
    Fl "Not under any circumstances."
    mc "..."
    show s1e70 with dissolve
    mc "And what happens if someone does?"
    show s1e71 with dissolve
    Fl "…You think highly of yourself, don’t you?"
    mc "I’m curious why Lora got away with it."

    if ivy_help == True:
        scene s1e75 with dissolve
        i "She’s under Lady Astoria’s full protection… Mind if I join you?"
        scene s1e76 with dissolve
        Fl "Do we even get a say?"
        scene s1e75 with dissolve
        i "I put my name on the line to get you in… so I’m afraid you don’t really have a choice."
        scene s1e77 with dissolve
        mc "..."
        scene s1e78 with dissolve
        mc "...Take a seat."
        play sounds2 sittingchair
        scene s1e79 with dissolve
        i "Thank you."
        i "And… thank you for stepping in earlier."
        scene s1e80 with dissolve
        mc "Ivy, right?"
        scene s1e81 with dissolve
        i "Oh! Where are my manners? Ivy. I sing here."
        i "And you are…?"
        mc "..."
        scene s1e82 with dissolve
        mc "What do you want?"
        play sounds1 slurping
        scene s1e83 with dissolve
        i "Rude."
        i "And… haven’t I already answered that?"
        mc "You stepped in because I helped you."
        mc "Paying off a debt, right?"
        scene s1e84 with dissolve
        i "You’re quite observant…"
        scene s1e85 with dissolve
        Fl "Hey. Ivy, enough games."
        Fl "What do you actually want?"
        scene s1e84 with dissolve
        i "..."
        scene s1e86 with dissolve
        Fl "I was wondering what felt off..."
        Fl "Ray acting strange. You stepping in out of nowhere..."
        Fl "A test."
        Fl "Has to be." 
        Fl "I’m more interested in the why."
        play sounds1 slurping
        show s1e87 with dissolve
        i "Miss Flora, don’t you think you’re overthinking this just a little?"
        i "I only wanted to repay the man who helped me."
        show s1e88 with dissolve
        Fl "..."
        show s1e89 with dissolve
        Fl "…A singer, right?"
        Fl "Funny."

        Fl "So how exactly does a ‘singer’ know about his girl?"
        show s1e90 with dissolve
        i "..."
        i "You’d make a good writer, Miss Flora. All that imagination... it’s almost poetic."
        scene s1e89 with dissolve
        Fl "Don’t dodge."
        Fl "Answer."
        show s1e91 with dissolve
        b "..."
        show s1e159 with dissolve
        i "I don’t care what she thinks. I owe you. And this is how I pay my debts."
        scene s1e160 with dissolve
        mc "And what exactly are you doing?"
        show s1e161 with dissolve
        i "First, the debt I already owe you."
        i "Emberlyn controls the Lower City. She knows about the relay tower, and a route out."
        i "That information is yours whether you accept the rest or not."
        i "The rest is a separate deal."
        show s1e162 with dissolve
        mc "What kind of deal?"
        menu: 
            "Decline.":
                show s1e163 with dissolve
                pause 1.0
                show s1e164 with dissolve
                pause 1.0
                show s1e165 with dissolve
                pause 1.0               
                show s1e165 with dissolve               
                mc "..."
                show s1e166 with dissolve 
                mc "If this was about repaying a debt… then we’re even."
                mc "You don’t owe me anything for your life."
                show s1e166 with dissolve               
                mc "And whatever this next deal is… I’m not interested."
                show s1e167 with dissolve      
                i "..."
                show s1e168 with dissolve      
                i "Your choice."
                i "Thank you for saving me… and I’m glad I could return the favor."
                




            "Hear her out.":
                scene s1e160 with dissolve
                mc "And what exactly are you offering?"
                show s1e169 with dissolve
                i "Somewhere a little more private."
                show s1e170 with dissolve
                i "Where we won’t have… unwanted ears around."
                scene s1e89 with dissolve
                Fl "Well, that’s an obvious trap."
                scene s1e90 with dissolve
                i "A trap? Please. I’m acting out of pure goodwill."
                menu: 
                    "Alright, then.":
                        $ mc_lust += 1
                        $ lora -= 1
                        show s1e172 with dissolve
                        i "In that case, let’s not waste any time. Come along."
                        show s1e173 with dissolve
                        mc "I’ll be back soon."
                        show s1e94 with dissolve
                        pause 0.5
                        show s1e96 with dissolve
                        Fl "Seriously?"
                        Fl "Right now? This is really the best time for this?"
                        show s1e97 with dissolve
                        mc "Trust me."
                        show s1e99 with dissolve
                        Fl "..."

                        $ persistent.Ivy_replay = True

                        scene black with dissolve
                        pause 3.0
                        scene s1ee19 with dissolve 
                        pause 1.0
                        scene s1ee20 with dissolve 
                        i "And how do you like it here? Are you enjoying yourself?"
                        scene s1ee21 with dissolve 
                        i "I hope I won’t disappoint your expectations."
                        scene s1ee15 with dissolve 
                        mc "..."
                        scene s1ee17 with dissolve 
                        mc "Let’s cut to it."
                        scene s1ee18 with dissolve 
                        i "Why so tense?"
                        scene s1ee17 with dissolve 
                        mc "..."
                        scene s1ee18 with dissolve 
                        i "Relax a little…"
                        i "You look like you’re about to interrogate me."
                        scene s1ee17 with dissolve 
                        mc "Maybe I am."
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
                        mc "I didn’t come here for that."

                        scene s1ee29 with dissolve 
                        i "Oh, really?"
                        i "Then why did you say yes?"

                        scene s1ee30 with dissolve 
                        mc "We both want the same thing."
                        mc "Or you think I don’t see what you’re doing?"


                        scene s1ee31 with dissolve 
                        i "You’re not wrong… but only halfway."
                        i "I am curious about you, that’s true… but—"

                        scene s1ee34 with dissolve 
                        i "This is actually my first time doing something like this…"
                        i "In a setting like this."
                        scene s1ee35 with dissolve 
                        mc "Who’s Ember?"
                        scene s1ee36 with dissolve 
                        i "Persistent, aren’t you…"
                        i "You know what, let’s make it a game."
                        i "If I win, you get your information."
                        i "If you win—"
                        scene s1ee35 with dissolve 
                        mc "Same deal."
                        mc "Rules?"

                        scene black with dissolve
                        pause 1.5
                        scene s1ee37 with dissolve 
                        mc "What, getting shy now?"
                        mc "You didn’t seem the type earlier."
                        mc "So what changed?"
                        scene s1ee38 with dissolve 
                        mc "..."
                        scene s1ee39 with dissolve 
                        mc "…And?"
                        scene s1ee40 with dissolve 
                        i "If I hadn’t seen your reaction downstairs… I might’ve thought you weren’t interested."
                        i "But then again…"
                        scene s1ee41 with dissolve 
                        i "I’ve always wondered what it feels… with a real person."
                        i "You help me, I help you."
                        i "That’s all there is to it."
                        scene s1ee42 with dissolve 
                        i "..."
                        jump ivy1


            #         "Not interested":
            #             show s1e164 with dissolve
            #             mc "..."
            #             show s1e166 with dissolve
            #             mc "Not interested."
            #             show s1e167 with dissolve
            #             i "..."
            #             scene s1e169 with dissolve
            #             i "Shame. But you’ve made your choice."
            #             i "Best of luck with your mission, then. Let’s hope it’s worth more than what you just turned down."

        play sounds1 slurping 
        show s1e92 with dissolve
        Fl "..."
        show s1e93 with dissolve
        Fl "And why did you turn it down?"
        show s1e94 with dissolve
        mc "No point risking it."
        show s1e95 with dissolve
        Fl "Exactly."

        

    jump bar_cyber1
    
label ivy1:
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
    mc "Who… is Ember?"
    i "(I need to… pull it together—)"
    mc "I’m waiting."
    i "Ember…"
    
    i "She’s not just the head…"
    i "She’s the one holding this whole place together."
    i "(Breathing heavier.)"
    i "Ah~"
    i "(N-no… focus. I have to—)"
    mc "Arch—…"
    i "H-how are you connected to that scho—"
    i "Ahh—!"
    mc "She’s…"
    mc "(Hold it together…)"
    mc "..."
    i "You keep asking questions…"
    i "But you don’t answer anything yourself."

    mc "...someone close to me."
    i "C-close… how close are we talk—"

    pause 1.1


    menu: 
        "Continue.":
            jump ivy2

        "Change angle.":
            jump ivy1_1

label ivy1_2:
    image Ivyy4 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy2.webm")
    show Ivyy4 with dissolve
    pause 

    menu: 
        "Continue.":
            jump ivy2

        "Change angle.":
            jump ivy1_1

label ivy1_1:
    hide Ivyy4
    image Ivyy9 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy3.webm")
    show Ivyy9 with dissolve
    pause 

    menu: 
        "Continue.":
            jump ivy2

        "Change angle.":
            jump ivy1_2

label ivy2:
    image Ivyy5 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy5.webm")
    show Ivyy5 with dissolve
    $ renpy.pause(13.9, hard=True)
    
    image Ivyy6 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy6.webm")
    show Ivyy6 with dissolve

    mc "What..."
    mc "did Lora do?"
    i "(No… I… have to hold—)"
    i "...keep my mouth shut."
    i "Lora…"
    i "She…"
    pause 0.8
    i "..."
    mc "Don’t dodge it."
    i "...you already know this isn’t a simple question."
    mc "Answer."
    i "Ah… I don’t know…"
    mc "(…Not enough.)"
    mc "I don’t need fragments."
    i "Hey… what’s gotten into you…"
    mc "Finish it."
    i "N-no! A-another ques—"

    pause 1.1

    menu: 
        "Continue.":
            jump ivy3

        "Change angle.":
            jump ivy2_1

label ivy2_2:
    image Ivyy6 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy6.webm")
    show Ivyy6 with dissolve
    pause 
    menu: 
        "Continue.":
            jump ivy3

        "Change angle.":
            jump ivy2_1

label ivy2_1:
    hide Ivyy6
    image Ivyy10 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy8.webm")
    show Ivyy10 with dissolve
    pause 

    menu: 
        "Continue.":
            jump ivy3

        "Change angle.":
            jump ivy2_2

label ivy3:

    image Ivyy7 = Movie(channel="movie_dp", loop = True, play="video/s1/ivy10.webm")
    show Ivyy7 with dissolve
    mc "Answer me."
    i "(Breathing quickens.)"
    i "I—"
    i "She knows…"
    pause 0.8
    i "About the tower…"
    mc "The tower—?"
    i "And the way out."
    mc "Wha-"
    mc "What way out?"
    mc "(…damn it, I’m losing it…)"

    pause 1.1

    menu: 
        "End.":
            jump ivy4

label ivy4:

    image Ivyy8 = Movie(channel="movie_dp", loop = False, play="video/s1/ivy11.webm")
    show Ivyy8 with dissolve
    $ renpy.pause(5.7, hard=True)

    window show

    
    scene s1ee44 with dissolve 
    pause 1.0
    i "(My first time…)"
    scene s1ee45 with dissolve 
    i "You… still haven’t… answered."
    mc "…Yeah."
    scene s1ee46 with dissolve 
    mc "(Catches his breath.)"
    mc "I don’t know."
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

    show s1e92 with dissolve
    Fl "..."
    show s1e93 with dissolve
    Fl "I'm surprised you got here faster than I thought. Did you calm your nerves?"
    mc "I got what I needed."

    jump bar_cyber1


label bar_cyber1:
    $ persistent.chapter_act1_scene += 1
    play sound ntsound loop 
    

    play music ember2 fadein 3.1 volume 0.4
    show s1e101 with dissolve
    a "What kind of bug did you drag in this time?"
    show s1e106 with dissolve
    Fl "Don’t be cruel, Ember."
    Fl "That ‘bug’ has potential."
    show s1e106 with dissolve
    em "Hmm..."
    show s1e105 with dissolve
    mc "I’m—"
    show s1e104 with dissolve
    em "Quiet, bug."
    mc "(bug…?)"
    play sounds1 sittingchair 
    show s1e109 with dissolve
    Fl "Could you {b}try{/b} not to spit on every gues-"
    show s1e110 with dissolve
    em "Watch your mouth, Flora."
    play sounds2 rustling2 volume 0.4
    show s1e113 with dissolve
    Fl "Tsk. You used to love my company."
    show s1e112 with dissolve 
    em "Only when you actually have something worth saying."
    em "Five minutes. Then you're out."
    scene s1e113 with dissolve
    Fl "The Ark’s been found."
    show s1e116 with dissolve
    mc "(Just blurting it out like that…?)"
    em "..."
    Fl "You heard me. It’s not a myth. It’s here. And he—"
    show s1e127 with dissolve
    mc "Flora, that’s eno—"
    play sounds2 hit1
    play sounds3 clench 
    play sounds4 tablesq
    scene s1def3 with vpunch  
    mc "Kh—!"
    scene s1def1 with dissolve 
    em "...who gave you permission to speak?"
    scene s1def2 with dissolve 
    Fl "EMBER, YOU’LL KILL HIM!"
    scene s1def1 with dissolve 
    em "I didn’t like his tone."
    scene s1def4 with dissolve 
    mc "(…in an instant…)"
    mc "(No. hold it together—)"
    em "Don’t even twitch."
    pause 1.1
    play sounds3 clench 
    em "You’ve got ten seconds before I crush his throat."
    play sounds2 mmove  
    scene s1def6 with dissolve 
    Fl "Wh-"
    Fl "Wait—!"
    scene s1def8 with dissolve 
    play sounds3 clench 
    em "Seven."
    play sounds2 glitchfear 
    mc "(My head… stay with me—)"
    scene s1def7 with dissolve 
    Fl "He’s more useful alive!"
    play sounds3 clench 
    em "Three."
    play sounds2 heartbeat
    scene s1def5 with dissolve 
    mc "(Am I… going to die?)"
    mc "(No… I have to—)"
    mc "...inf—information… I—"
    scene s1def9 with dissolve 
    Fl "He’s like Lora!"
    scene s1def10 with dissolve 
    pause 1.1
    scene s1def11 with dissolve 
    em "..."
    play sounds2 clothess  
    play sounds3 fall 
    scene s1def12 with vpunch
    pause 1.8 
    mc "(…I’m still breathing.)"
    mc "(Why?)"
    play sounds2 mmove 
    scene s1def13 with dissolve 
    Fl "You alright?"
    scene s1def14 with dissolve 
    mc "..."
    mc "(whispering) I’ll live."
    scene s1def16 with dissolve 
    Fl "(whispering) I warned you..."
    em "..."
    em "...Interesting."
    play sounds2 mmove 
    scene s1def15 with dissolve 
    em "Take your bug. You’re coming with me."
    stop sound
    stop music fadeout 2.1
    scene black with dissolve 
    play sounds1 emberroom2 fadein 1.2 loop volume 0.5
    pause 2.3
    
    play music evermore fadein 15.5
    play sounds2 scifidooropen2
    scene s1def18 with dissolve 
    pause 1.1
    scene s1def19 with dissolve 
    Fl "(whispering) How are you holding up?"
    mc "(whispering) I’ve had worse."
    Fl "You know, for someone who almost got his neck crushed…"
    Fl "you’re weirdly calm."
    scene s1def20 with dissolve 
    em "Terms?"
    Fl "..."
    pause 1.1
    scene s1def21 with dissolve 
    Fl "(whispering) Say what she wants to hear."
    scene s1def22 with dissolve 
    mc "What’s the Ark?"
    scene s1def24 with dissolve 
    em "In return, you tell me how you're connected to Astoria."
    mc "..."
    scene s1def23 with dissolve 
    mc "You’re only going to give me half the truth anyway."
    scene s1def25 with dissolve 
    Fl "...You’re serious right now?"
    Fl "She’ll kill you before this ‘deal’ even starts!"
    scene s1def27 with dissolve 
    pause 1.1
    scene s1def28 with dissolve 
    pause 1.1
    scene s1def29 with dissolve 
    em "We’ll see."
    scene s1def28 with dissolve 
    Fl "Hey, hey, don’t do anything stupid—"
    scene s1def29 with dissolve 
    em "Answer."
    scene s1def25 with dissolve 
    pause 1.1
    scene s1def26 with dissolve 
    mc "Fine. One answer for one answer."
    em "Then I’m waiting."
    scene s1def24 with dissolve 
    mc "..."
    scene s1def23 with dissolve 
    mc "Astoria, right…"
    
    scene s1b165 with dreamyzoom 
    show memoryframe with dissolve 
    lad "Find a way out."
    lad "Then we’ll talk."
    
    scene s1def26 with dissolve 
    mc "We have an agreement."
    scene s1def27 with dissolve 
    em "..."
    scene s1def29 with dissolve 
    em "A ship."
    scene s1def27 with dissolve 
    em "..."
    scene s1def33 with dissolve 
    mc "That’s it?"
    play sounds2 footstep2 
    scene s1def30 with dissolve 
    em "Were you expecting more?"
    scene s1def31 with dissolve 
    Fl "(whispering) I told you so..."
    scene s1def32 with dissolve 
    em "I pay exactly what it’s worth."
    scene s1def35 with dissolve 
    mc "..."
    mc "Same terms?"
    scene s1def36 with dissolve 
    pause 1.1
    scene s1def34 with dissolve 
    em "No."
    em "On top of that, you’re telling me how you’re connected to that scientist."
    em "Call it a tax on your attitude."
    scene s1def37 with dissolve 
    mc "Astoria told me to find a way out."
    mc "No idea."
    mc "And the scientist…"
    scene s1def38 with dissolve 
    pause 1.1
    scene s1def37 with dissolve 
    mc "Lora is my wife."
    scene s1def39 with dissolve 
    Fl "..."
    em "..."
    scene s1def40 with dissolve 
    em "Now… you’re finally paying for real."
    pause 1.1 
    play sounds2 keyboard 
    scene s1def41 with dissolve
    mc "(…that got her attention.)"
    scene s1def42 with dissolve
    em "Among my kind... there was a myth."
    scene s1def41 with dissolve
    pause 0.7
    scene s1def42 with dissolve
    em "A world without war."
    em "Without betrayal."
    em "...we thought it was a lie."
    scene s1def43 with dissolve
    mc "(Are they talking about Earth? But… another world?)"
    $ persistent.ark_origin_ = True
    scene s1def43 with dissolve
    show memoryreboot with dissolve
    em "The Ark isn’t just a ship."
    play sounds2 spacepick2 fadein 0.2
    play sounds4 ha 
    scene s1def44 with dissolve
    em "It’s something that carves a path between worlds."
    mc "(Carves a path…?)"
    
    scene s0a3 with dreamyzoom
    show memoryframe with dissolve
    Lo "...something related to teleportation…"
    scene s1bb38 with dissolve 
    show memoryframe with dissolve
    h "Somewhere in the ass-end of the galaxy."

    scene s1def45 with dissolve
    play sounds4 mmove 
    play sounds2 footstep2 
    mc "(A path between worlds... right.)"
    mc "Is it one-way?"
    em "Is that your second condition?"
    scene s1def46 with dissolve
    mc "(…there has to be a way back.)"
    mc "(So why didn’t Lora return? Conditions? Limits?)"
    mc "..."
    play sounds4 mmove 
    scene s1def47 with dissolve
    mc "No. That’s not what I’m asking."
    mc "You said it carves a path."
    play sounds4 mmove 
    play sounds3 footstep2 
    scene s1def48 with dissolve
    mc "If there’s an entrance… there has to be an exit."
    em "A question."
    scene s1def49 with dissolve
    mc "Why here?"
    mc "Out of the entire galaxy, why this place?"
    em "..."
    scene s1def53 with dissolve
    em "Hm… and what are you willing to pay?"
    scene s1def54 with dissolve
    mc "Information."
    scene s1def53 with dissolve
    em "I already got what I wanted."
    scene s1def157 with dissolve
    pause 0.8
    scene s1def156 with dissolve
    mc "That wasn’t worth the answer."
    scene s1def155 with dissolve
    em "Watch your tone, bug."
    Fl "(whispering) Let’s go, [mc]."
    Fl "Don’t push her."
    scene s1def57 with dissolve
    mc "(…think.)"
    mc "(Wait… why is she so calm?)"
    scene s1def58 with dissolve
    mc "(Flora said it’s a myth… so why doesn’t she doubt it?)"
    
    scene s0q159 with dreamyzoom
    show memoryframe with dissolve
    a "Day 64: Something came out of the ring…"
    a "They look… human."
    a "But they’re not."
    
    scene s1def59 with dissolve
    mc "You didn’t react like this was new to you."
    mc "You’ve already been to the Ark, haven’t you?"
    scene s1def61 with dissolve
    em "(whispering) Potential… yes."
    scene s1def153 with dissolve
    em "You’re asking questions people don’t get answered for free."
    em "Some pay everything for answers like that."
    scene s1def152 with dissolve
    pause 1.1
    em "Hm..."
    scene s1def153 with dissolve
    em "Fine. Then your life will be the price."
    scene s1def154 with dissolve
    Fl "Hey.. Ember, that’s a bit mu—"
    scene s1def60 with dissolve
    mc "That’s a steep price."
    scene s1def58 with dissolve
    em "Then make me an offer."
    mc "(With what…?)"
    
    scene s1rew71 with dreamyzoom 
    show memoryframe with dissolve
    o "I’m repaying a debt."
    mc "(There’s another way to pay… right?)"
    
    scene s1def155 with dissolve
    pause 1.1
    scene s1def156 with dissolve
    mc "Does it have to be my life?"
    mc "I can offer something else."
    scene s1def157 with dissolve
    pause 1.1
    em "Hmm..."
    scene s1def156 with dissolve
    mc "My services."
    mc "I solve problems."
    scene s1def152 with dissolve
    pause 1.1
    em "..."
    scene s1def50 with dissolve
    em "Tell me, what do you see?"
    scene s1def51 with dissolve
    mc "...a structure."
    pause 1.1
    mc "An exit…"
    em "..."
    scene s1def52 with dissolve
    em "A gate system."
    Fl "Hey, are you serious, Ember?!"
    Fl "Those systems are forbidden!"

    scene s1def57 with dissolve
    mc "(Forbidden by whom?)"
    pause 0.6
    mc "..."

    
    scene s1rew197 with dreamyzoom 
    show memoryframe
    pause 0.8
    mc "They used blood."
    mc "As fuel."

    scene s1def58 with dissolve
    mc "(…fuel.)"
    pause 0.6
    scene s0q193 with dreamyzoom
    show memoryframe
    L "It’s absorbing human bodies now!"
    scene s1def59 with dissolve
    mc "(No…)"

    scene s1def62 with dissolve
    mc "(…how many did it take?)"

    
    stop music fadeout 0.5
    
    image towerboom = Movie(channel="movie_dp", loop = False, play="video/Towerboom.webm")
    show towerboom with dissolve
    $ renpy.pause(5.8, hard=True)
    stop sounds1
    stop sound 
    play sounds2 punch1

    scene black with vpunch 
    pause 4.4
    
    play sounds2 desertwind loop volume 0.4 fadein 2.2 
    scene s1def63 with dissolve
    pause 1.1
    play sounds3 spacepick2
    "Analysis complete: The substance level at 76%%."
    play sounds4 towerexplos 
    scene s1def64 with dissolve
    L "(It’s spreading…)"
    L "(Too fast.)"
    scene s1def65 with dissolve
    pause 1.1 
    play sounds warptravaling fadein 1.6 loop volume 0.2
    scene s1def66 with dissolve
    g "Wh-what is that?"
    play sounds3 mmove 
    scene s1def67 with dissolve
    L "(It’s begun…)"
    pause 1.1 
    stop sounds fadeout 0.5
    stop sounds2 fadeout 0.5
    scene black with dissolve
    pause 4.4

# часть 3
    scene black with dissolve
    pause 3.0
    show act1s1_3 with dissolve
    pause 1.5
    show act1s1_4 with dissolve
    pause 1.5
    
    scene s1def72 with dissolve
    play sounds ringingsound fadein 0.5 
    scene black with dissolve
    pause 0.5
    play sound fire fadein 2.0  loop volume 0.4
    play music1 ember2 fadein 11.2
    scene s1def69 with dissolve
    pause 0.8 
    scene black with dissolve
    pause 0.9 
    play sounds2 scrapmetalbig 
    scene s1def70 with dissolve 
    em "...I’ll make you regret th—"
    scene black with dissolve 
    pause 1.2 
    play sounds2 scrapmetalbig fadein 3.3
    scene s1def71 with dissolve 
    em "...AAARGH—!"
    scene black with dissolve 
    pause 0.7 
    scene s1def73 with dissolve 
    mc "(…noise.)"
    mc "(Can’t hear…)"
    mc "(My head…)"
    mc "(An explosion?)"
    scene s1def74 with dissolve 
    mc "(…my hands.)"
    mc "(I can’t—)"
    scene s1def75 with dissolve 
    mc "(Flora…)"
    scene s1def76 with dissolve 
    pause 1.1 
    play sounds3 whoosh 
    scene s1def77 with CropMove(time=0.2, mode='slideright')        
    mc "No— no, no… Flora!"
    scene s1def78 with dissolve 
    mc "..."
    play sounds4 heartbeat fadein 2.2
    mc "(Pulse… there.)"
    mc "(She’s alive.)"
    em "Alive?"
    play sounds2 mmove 
    scene s1def79 with dissolve 
    mc "For now."
    mc "But we need to move."
    scene s1def80 with dissolve 
    em "Take her. Move."
    scene s1def82 with dissolve 
    pause 0.6
    play sounds3 wallfall1
    pause 0.3
    scene s1def83 with vpunch 
    pause 1.1 
    play sounds4 mmove 
    play sounds1 whoosh  
    scene s1def85 with CropMove(time=0.1, mode='slideright')        
    pause 1.1 
    stop sound fadeout 0.5
    stop music1 fadeout 0.5
    scene black with dissolve
    pause 3.8 

label warehouse1:

    "Sector 4-S, border with Sector 5-S."
    play sounds2 scifidooropen2
    play music mctakegun fadein 3.1
    play sounds alarm loop volume 0.2
    scene s1def86 with dissolve 
    g "…No, sir, no connection!"
    gg "Get to Mr. Ray! Find out anything you can!"
    g "Y-yes, sir!"
    play sounds2 whoosh 
    scene s1def87
    pause 1.1 
    play sounds3 clench 
    play sounds4 whoosh 
    scene s1def88
    em "Stop."
    em "Why the rush?"
    g "L-Lady Emberlyn?!"
    play sounds4 mmove 
    scene s1def89 with dissolve 
    g "Comms are down! It’s like… we’ve gone deaf!"
    g "Nothing… nothing’s working."
    em "Global comms?"
    g "Dead. Local pings still answer, but nothing reaches outside the sector."
    em "Who’s giving the orders?"
    play sounds3 clothess 
    scene s1def90 with dissolve 
    g "Jo... Brother Jonathan is in command."
    play sounds2 systemnotification
    "All commanding officers, report to the briefing hall."
    scene s1def89 with dissolve 
    g "I—I have to go…"
    scene s1def92 with dissolve 
    mc "(To repay him.)"
    scene s1rew71 with dreamyzoom 
    show memoryframe with dissolve
    pause 1.5
    scene s1def92 with dissolve 
    mc "(To repay him.)"
    mc "(whispering) Just a little longer…"
    mc "...hang in there, Flora."
    play sounds2 mmove 
    play sounds3 whoosh 
    scene s1def93 
    em "Wait."
    em "Tell Scarleia it’s from me."
    em "She’ll handle the rest."
    play sounds3 running 
    scene s1def94 with dissolve 
    mc "I’ll handle it."
    pause 1.1
    scene s1def95 with dissolve 
    g "W-what?"
    g "Y-you… why didn’t you do anything to him?!"
    g "He’s an Inquisitor!"
    em "..."
    scene s1def96 with dissolve 
    em "Maybe."
    em "He dies when I decide."
    em "Until then—"
    scene black with dissolve 
    em "Gather the others."
    em "Time to collect what’s owed."
    stop music fadeout 3.3
    stop sounds fadeout 1.1
    scene black with dissolve 
    play sound systemambience fadein 3.0 loop volume 0.8
    pause 4.4

    play sounds1 keyboardanix 
    scene s1def97 
    pause 0.1 
    scene s1def98 
    pause 0.1 
    scene s1def97 
    pause 0.1 
    scene s1def98 
    pause 0.1 
    scene s1def97 
    pause 0.1 
    scene s1def98 
    pause 0.1 
    play sounds3 systemnotification
    scene s1def97 with dissolve 
    scar "..."
    scar "(Dead...)"
    play sounds4 scifidooropen2
    mc "Scarleia here?!"
    scene s1def100 with dissolve 
    scar "(whispering) Another one? Seriously?"
    scar "You here for treatment? Get lost."
    scar "The equipment’s dead. We’re closed."
    play sounds3 mmove 
    scene s1def97 with dissolve 
    mc "You don’t have a choice. Treat her."
    scar "..."
    scar "Hey, piss off, yeah? I really don’t have time fo—"
    scene s1def103 with dissolve 
    mc "Hey. You all this arrogant around here?"
    scene s1def98 with dissolve 
    mc "Help her. I’ll pay."
    scar "..."
    scene s1def102 with dissolve 
    scar "(Flora?)"
    scar "Bring her here."
    play music mirielwalk fadein 14.2
    scene black with dissolve 
    pause 3.2 
    play sounds2 mmove 
    play sounds3 heartbeat 
    scene s1def104 with dissolve 
    scar "Hmm..."
    mc "How is she?"
    play sounds2 mmove 
    scene s1def105 with dissolve 
    scar "Will she live? Yeah."
    scar "The rest? No idea."
    pause 1.1 
    mc "Price."
    play sounds2 mmove 
    scene s1def106 with dissolve 
    scar "..."
    scar "(That suit’s familiar… but the attitude’s different. Is this the guy Ivy kept talking about?)"
    mc "Hey?"
    scene s1def107 with dissolve 
    mc "I don’t have time."
    scene s1def108 with dissolve 
    scar "Then go."
    scene s1def107 with dissolve 
    mc "And her?"
    play sounds2 mmove 
    scene s1def109 with dissolve 
    scar "I’ll watch her. Relax."
    play sounds3 rustling2  
    scene s1def111 with dissolve 
    mc "For free?"
    mc "Then what was all that earlier?"
    scene s1def110 with dissolve 
    scar "Thought you didn’t have time."
    scene s1def112 with dissolve 
    mc "You know what… you’re right."
    mc "Thanks for the help."
    scene s1def114 with dissolve 
    mc "When she wakes up, tell her to stay here."
    play sounds2 running
    scene s1def115 with dissolve 
    mc "I’ll come back for her once I’m done."
    pause 1.1 
    scene s1def116 with dissolve 
    scar "..."
    scar "(He ran off.)"
    scene s1def117 with dissolve 
    scar "So... how long have you been awake?"
    scene s1def116 with dissolve 
    Fl "..."
    scene s1def118 with dissolve 
    pause 1.1
    scene s1def119 with dissolve 
    pause 0.7 
    scene s1def120 with dissolve 
    pause 0.7 
    scene s1def121 with dissolve 
    Fl "Since we walked in, I guess."
    scar "Why?"
    Fl "Okay, so—"
    Fl "Here’s the thing…"
    Fl "I spent half the day hyping myself up as this top-tier mechanic to him."
    Fl "And then the next second?"
    Fl "I’m out cold."
    scar "And?"
    Fl "And?!"
    Fl "You know I have standards, right?!"
    Fl "How am I supposed to look him in the eye now—"
    play sounds2 mmove 
    play sounds3 whoosh  
    scene s1def122
    Fl "Anyway!"
    Fl "I don’t owe you anything, right?"
    Fl "So… care to explain what the hell is going on?"
    scene s1def123 with dissolve 
    scar "..."
    play sounds2 mmove 
    scene s1def124 with dissolve 
    scar "How long are you planning to keep running like this?"
    scar "You could at least thank him."
    scene s1def125 with dissolve 
    scar "Maybe start with a ‘thanks’ for saving your life."
    scar "That kind of thing doesn’t happen often around here."
    scene s1def126 with dissolve 
    Fl "..."
    scene s1def127 with dissolve 
    scar "..."
    scar "You’re… a lot like her."
    scene s1def128 with dissolve 
    Fl "Hmph."
    scene s1def129 with dissolve 
    Fl "Don’t compare me to her."
    Fl "She—"
    scene s1def131 with dissolve 
    pause 1.1 
    scene s1def130 with dissolve 
    scar "Professor Joy was the best."
    scar "Just like her daughter, right?"
    scene s1def131 with dissolve 
    Fl "...Yeah."
    pause 1.5
    scar "(Please… don’t make the same mistakes she did.)"
    stop music fadeout 5.5
    stop sound fadeout 2.2


    scene black with dissolve 
    pause 3.2
    play sounds industryroom loop volume 1
    play music1 dardd fadein 5.4 
    scene s1def133 with dissolve 
    g "...Trying not to think about it."
    g "I won’t let them turn my family into monsters…"
    gg "Hey… look."
    scene s1def134 with dissolve 
    mc "(Unwanted attention…)"
    g "(whispering) Great… they’re here again, throwing their weight around."
    gg "(whispering) Easy. Keep it down, he’ll hear you."
    g "(whispering) Don’t care. Nothing but trouble with them."
    play sounds2 mmove 
    scene s1def135 with dissolve 
    mc "(Trying to provoke me?)"
    mc "Say it to my face."
    g "..."
    mc "(Yeah. Thought so.)"
    mc "(Annoying.)"
    play sounds2 mmove 
    scene s1def136 with dissolve 
    gggg "(whispering) Who does he think he—"
    em "I won’t repeat myself."
    scene s1def137 with dissolve 
    g "S-sorry, Lady—"
    mc "Situation?"
    scene s1def138 with dissolve 
    em "I didn’t give you permission to be here."
    scene s1def139 with dissolve 
    mc "I came to pay the price for information. That’s it."
    scene s1def140 with dissolve 
    pause 1.1
    scene s1def141 with dissolve 
    em "..."
    em "(Good answer.)"
    scene s1def158 with dissolve 
    em "The city has fallen."
    em "The soulless are devouring everything."
    scene s1def159 with dissolve 
    pause 1.1 
    scene s1def158 with dissolve 
    em "Disgusting."
    scene s1def160 with dissolve 
    mc "This connected to the blast, right?"
    em "..."
    mc "And the walls?"
    mc "How did they even get inside?"
    scene s1def158 with dissolve 
    em "Unknown."
    scene s1def140 with dissolve 
    pause 1.1
    scene s1def139 with dissolve 
    mc "Comms are down too…"
    scene s1def140 with dissolve 
    mc "(Hold on, Liv. I’ll find you.)"
    scene s1def141 with dissolve 
    mc "My objective?"
    em "Find out what happened to comms."
    em "Sector 8. The radio tower."

    mc "I restore it, and you give me the route Lora used to reach the tomb."
    em "Return alive, and the route is yours."
    em "I hope you’re a worthwhile investment."
    scene s1def140 with dissolve 
    mc "(An investment? Huh. Not a bug anymore.)"
    mc "(Progress.)"
    scene s1def142 with dissolve 
    em "Rey. Ammunition."
    rey "Your preference, Lady Emberlyn?"
    em "Give him the Devourer. That’ll do for a test."
    play sounds2 mmove
    play sounds3 whoosh
    scene s1def143 with CropMove(time=0.1, mode='slideright')   
    mc "(Light…)"
    em "Titanium alloy. Self-charging rounds."
    play sounds2 mmove
    play sounds3 clothess 
    scene s1def144 with dissolve 
    mc "Reliable?"
    em "If you die, it’ll be your own incompetence."
    scene s1def146 with dissolve 
    mc "Reassuring."
    mc "Two things."
    mc "The enemy, and the terrain."
    mc "Any advice?"
    play sounds2 mmove
    scene s1def149 with dissolve 
    em "Shoot anything that moves."
    scene s1def148 with dissolve 
    mc "That’s not funny."
    em "..."
    mc "What about civilians?"
    stop music1 fadeout 5.5
    play music astoria1 fadein 5.5
    scene s1def169 with dissolve 
    g "Civilians?"
    play sounds2 stepember
    scene s1def171 with dissolve 
    g "(laughs)"
    g "You hear that? The Inquisitor’s asking about—"
    scene s1def172 with dissolve 
    em "What’s funny?"
    scene s1def173 with dissolve 
    pause 1.1
    play sounds2 mmove 
    scene s1def174 with dissolve 
    g "L-Lady Ember—"
    scene s1def175 with dissolve 
    em "I won’t say it twice."
    scene s1def176 with dissolve 
    g "..."
    g "...Nothing."
    scene s1def178 with dissolve 
    pause 1.1
    scene s1def177 with dissolve 
    em "How are we any better than Astoria’s dogs…"
    em "…if we mock what others hold dear?"
    scene s1def178 with dissolve 
    g "..."
    scene s1def177 with dissolve 
    em "Shameful. Out of my sight."
    play sounds2 running 
    play sounds3 mmove 
    scene s1def179 with dissolve 
    pause 1.1
    scene s1def180 with dissolve 
    mc "They’d tear out throats for you."
    scene s1def181 with dissolve 
    em "They’re far from perfect."
    scene s1def183 with dissolve 
    pause 1.1
    scene s1def181 with dissolve 
    em "You."
    em "Why do you care about civilians?"
    scene s1def182 with dissolve 
    mc "You want me to spill my soul?"
    scene s1def183 with dissolve 
    em "..." 
    scene s1def184 with dissolve 
    em "No."
    pause 1.1
    em "Rey. A word."
    scene black with dissolve 
    stop music fadeout 3.3 
    stop sounds fadeout 3.3


    play sound systemambience fadein 3.0 loop volume 0.8
    pause 4.4
    play music1 flora03 fadein 5.5
    scene s1deg16 with dissolve 
    Fl "..."

    scene s1def78 with dreamyzoom
    show memoryframe with dissolve 
    mc "No! No, no… Flora!" 

    scene s1deg16 with dissolve 
    pause 0.7
    scene s1deg17 with dissolve 
    pause 1.1

    scene s1def125 with dreamyzoom 
    show memoryframe with dissolve 
    scar "Maybe start with a ‘thanks’ for saving your life."
    
    
    scene s1deg17 with dissolve 
    Fl "..."
    play sounds2 mmove 
    scene s1deg18 with dissolve 
    pause 0.7
    play sounds3 clench
    scene s1deg19 with dissolve 
    pause 0.7

    scene s1c81 with dissolve 
    show memoryframe with dissolve 
    o "Value the ones who’d give their life for you."


    scene s1deg20 with dissolve 
    Fl "(...Just say it.)"
    Fl "(It’s not that hard.)"
    play sounds3 clench
    scene s1deg21 with dissolve 
    pause 1.1   
    Fl "(So why…)"
    Fl "(is this so hard…?)"
    play sounds2 mmove 
    scene s1deg23 with dissolve 
    Fl "..."
    scene s1deg24 with dissolve 
    Fl "(No… this can’t keep happening.)"
    play sounds3 whoosh 

    play sounds2 running 
    scene s1deg10 
    Fl "(I have to—)"
    scene s1deg11 with dissolve 
    pause 0.6
    scene s1deg12 with dissolve 
    pause 0.6
    scene s1deg13 with dissolve 
    Fl "(If I don’t say it now…)"
    scene s1deg14 with dissolve 
    Fl "(I never will.)"
    scene s1deg15 with dissolve 
    pause 1.8
    
    play sounds3 hit1 
    scene s1deg8 with vpunch
    pause 1.1 
    

    scene s1deg1 with dissolve 
    Fl "(There he is…)"
    Fl "(Come on… just one word…)"
    Fl "(Say it.)"
    Fl "..."
    scene s1deg2 with dissolve 
    Fl "(Why can’t I?)"
    Fl "(Come on! Say it.)"
    Fl "..."
    scene s1deg6 with dissolve 
    Fl "(Say it already.)"
    Fl "(What’s wrong with you?)"
    Fl "..."
    pause 1.1

    scene s1rew42 with dreamyzoom 
    show memoryframe with dissolve 
    Fl "(“The best mechanic.” …Right.)"
    scene s1def75 with dreamyzoom 
    show memoryframe with dissolve 
    Fl "(He said my name like it mattered…)"
    
    scene s1def124 with dreamyzoom 
    show memoryframe with dissolve 
    Fl "(How long are you going to keep running…?)"
    
    scene s1deg6 with dissolve 
    pause 1.1

    scene s1deg8 with dissolve 
    pause 0.4
    Fl "…Th—"
    pause 0.6
    Fl "(…no, don’t choke now—)"

    scene s1deg7 with vpunch 
    Fl "THANK YOU!!"

    scene s1deg3 with dissolve 
    mc "(Wha—)"
    scene s1deg4 with dissolve 
    mc "..." 

    scene s1deg8 with dissolve 
    pause 0.8
    scene s1deg9 with dissolve 
    Fl "GO WRECK THEM OUT THERE, GOT IT?!"

    scene s1deg4 with dissolve 
    mc "..." 
    mc "(Glad she's alive...)"
    scene s1deg5 with dissolve 
    mc "Yeah."

    scene s1deg8 with dissolve 
    pause 1.8

    stop music1 fadeout 4.4
    stop sound fadeout 2.2
    scene black with dissolve 
    pause 4.4
    



    
    
    
    
    
    



define minigame = 1

label cyberstreet1:
    stop music fadeout 0.5
    $ persistent.chapter_act1_scene += 1
    play music1 cybercityopen2 fadein 3.3
    play sounds4 cybercityopen fadein 1.4 loop
    show s1g1 with dissolve
    pause 1.1
    "A few minutes later."
    show s1g2 with dissolve
    mc "(For a city this size… it’s dead quiet.)"
    show s1g3 with dissolve
    mc "Abandoned… left to rot."
    mc "(Restore the tower. Get Ember’s route. Reach Lora.)"
    mc "(That’s the job.)"
    play sounds2 radio volume 0.09 loop 
    show s1g4 with dissolve
    Fl "H—hey… can you hear me?!"
    Fl "[mc], come in!"
    mc "Flora?"
    mc "What did you do?"
    show s1g5 with dissolve
    Fl "Trying to keep the connection alive..."
    show s1g6 with dissolve
    Fl "I’m here."
    Fl "Came to help you."
    Fl "I mean… I am responsible for you, after all."
    show s1g7 with dissolve
    mc "Flora. Answer the question."
    show s1g8 with dissolve   
    Fl "Hm? Oh... right, right."
    Fl "I hooked into your implants."
    Fl "Something’s lagging. I can’t—"
    pause 0.8
    Fl "Your eye, specifically."
    Fl "Figured it’s better than nothing."
    mc "You don’t know where Olivia or Miriel are?"
    Fl "How would I know?"
    Fl "No network, I’m basica-"
    stop sounds2 
    mc "..."
    mc "Flora?"
    mc "..."
    mc "(Get it together… I need to keep moving.)"
    show pause with dissolve
    n "Sorry to interrupt, but I wanted to clarify something. Do you wish to participate in a similar game like the one on the spaceship, or would you prefer to avoid them in the future?"  
    menu:
        "No, I’m not interested in that.":  
            $ minigame = 0
            n "Thank you for your answer."  
            hide pause with dissolve
        # "Yes, of course, I find that interesting.":  
            
        #     n "Thank you for your answer. Good luck with the hunt!"  
        #     hide pause with dissolve


    if minigame == 1:
        call screen path_first_1
    else:
        scene s1g44 with dissolve   
        Fl "Interference… annoying… rerouting host and—"
        Fl "Okay. That should hold. Temporarily."
        scene s1g46 with dissolve   
        mc "...fresh body."
        Fl "Ugh. That’s… disgusting."
        Fl "I’m gonna—"
        Fl "…"
        Fl "I don’t feel so good."
        show s1g49 with dissolve   
        mc "Focus on my voice."
        show s1g50 with dissolve   
        Fl "…"
        mc "Flora, I’ll take it from here."
        Fl "NO!"
        Fl "I can still help, just... just give me a second…"
        mc "Take your time."
        show s1g52 with dissolve   
        pause 1.0
        show s1g53 with dissolve   
        pause 1.0
        show s1g55 with dissolve   
        pause 1.0
        show s1g51 with dissolve   
        mc "...No head. Again."
        mc "Flora, don’t look."
        show s1g57 with dissolve    
        Fl "I… need to see it."
        Fl "What my father’s dealing with."
        mc "..."
        mc "(Same pattern… one clean strike. Head gone.)"
        show s1g58 with dissolve   
        mc "Flora, give me everything you’ve got on the soulless."
        show s1g59 with dissolve   
        Fl "Y-yeah, just— one sec—"
        Fl "N-no—!"
        show s1g60 with dissolve   
        mc "...Something wrong?"
        show s1g61 with dissolve   
        Fl "Nothing’s working…"
        Fl "I— I’m sorry. I’m useless right now."
        pause 0.8
        show s1g62 with dissolve   
        mc "Flora?"
        mc "You’re doing better than most would."
        Fl "...thanks."
        stop music1 fadeout 5.3
        jump path_second_up_3_3


define pathfirstright2 = False
define pathfirstright3 = False
define pathfirstright4 = False
define pathfirstleft1 = False
define pathfirstleftnext5 = False
define pathfirstleftnext6 = False

default inquisition = 1

label path_second_up_3_3:
    play sound stepmc fadein 1.0
    stop music1 fadeout 4.0
    play music doom fadein 4.5
    show s1g79 with dissolve   
    mc "Alright… what are we dealing with?"
    Fl "Soulless."
    Fl "Mutants driven by hunger… and rage."
    mc "Weaknesses?"
    $ persistent.mutants_screen_ = True
    show s1g80 with dissolve   
    show memoryreboot with dissolve 
    Fl "No idea…"
    Fl "But kill one, and two more show up in its place."
    hide memoryreboot with dissolve 
    mc "You’re joking?"
    Fl "Not literally."
    Fl "They multiply insanely fast! Like a virus."
    mc "(A virus…?)"
    Fl "[mc]!"
    Fl "Movement ahead, tight formation."
    Fl "Stay sharp."
    play sounds2 rustling2
    show s1g81 with dissolve   
    mc "Don’t worry."
    Fl "Try not to die immediately."
    Fl "That’d be great."
    play sound stepmc fadein 1.0
    show s1g82 with dissolve   
    mc "I’d promise… but we both know how I handle bad ideas."
    scene black with dissolve
    pause 0.5
    play sound riflesound
    show s1g83 with dissolve   
    g "Cover me! Go, go, go!"
    play sound riflesound
    show s1g84 with dissolve   
    pause 0.5
    play sounds1 hdshot
    show s1g85 with dissolve   
    gg "How many rounds left?!"
    show s1g86 with dissolve   
    mc "..."
    play sound riflesound
    show s1g87 with dissolve   
    g "Two mags! After that, it’s fists and prayers!"
    play sounds1 hdshot
    show s1g88 with dissolve   
    gg "Seriously?! They’re swarming like it’s feeding time!"
    play sound riflesound loop
    show s1g89 with dissolve   
    g "Shit! Reloading!"
    show s1g90 with dissolve   
    gg "I’ve got you! Make it fast. I’m down to fumes myself!"
    show s1g91 with dissolve   
    pause 0.5
    show s1g92 with dissolve   
    g "—WHAT THE HELL?!"
    gg "What?!"
    g "I’m out. Nothing left."
    show s1g93 with dissolve   
    gg "You’re joking?!"
    gg "Back pocket, top right! Spare mag! Drop it, and I’ll drop you!"
    stop sound
    play sound zombie
    show s1g95 with dissolve   
    pause 0.6
    play sounds1 hdshot
    show s1g96 with dissolve   
    pause 0.6
    play sound rs1 loop
    play sounds1 killmutant loop
    show s1g99 with dissolve   
    pause 0.6
    show s1g101 with dissolve   
    pause 0.6
    show s1g103 with dissolve   
    pause 0.6
    show s1g104 with dissolve   
    pause 0.6
    show s1g106 with dissolve   
    pause 0.6
    show s1g107 with dissolve   
    pause 0.6
    stop sound
    stop sounds1
    show s1g108 with dissolve   
    mc "..."
    mc "(Hot…)"
    show s1g109 with dissolve   
    mc "Soldier. Report."
    gg "Yes, sir." 
    gg "We were deployed to the east-"
    mc "Wait-!"
    mc "(Something’s off.)"
    mc "(…behind me. Too hot.)"
    play sound glitchfear
    show s1g110 with glitch   
    Fl "BEHIND YOU!"
    show s1g111 with dissolve   
    mc "(…I know.)"
    play sound rs1
    play sounds1 killmutant
    play sounds2 whoosh 
    show s1g112 with CropMove(time=0.1, mode='slidedown')   
    pause 0.9
    mc "(…die—)"
    stop sound
    stop sounds1
    play sounds2 fall
    show s1g113 with dissolve   
    mc "..."
    mc "(That wasn’t a soulless.)"
    show s1g114 with dissolve   
    mc "Flora, I need everything you’ve got on that thing."
    Fl "Y-yeah! Give me a second— I’m checking."
    mc "And… thanks."
    Fl "...You’re alive."
    Fl "That’s what matters."
    show s1g117 with dissolve   
    g "We were done. Just done."
    show s1g116 with dissolve   
    mc "Don’t relax. Not here."
    mc "What happened to you?"
    show s1g116 with dissolve   
    pause 0.5
    show s1g118 with dissolve   
    pause 0.5
    scene s1g116 with dissolve   
    gg "Eastern wall fell." 
    gg "Turned around... They we're already inside."
    mc "How did they breach the defenses?"
    show s1g118 with dissolve   
    b "..."
    g "Not sure they broke through."
    gg "Yeah… they hit us from behind."
    scene s1g116 with dissolve   
    Fl "I asked around about that thing."
    Fl "From what I got? It’s a real pain in the ass."
    mc "(whispering) Anything more useful?"
    Fl "They move alone."
    Fl "Can go invisible…"
    Fl "But they give off heat signatures."

    show s1g116 with dissolve   
    mc "Sector 8. The comm tower. You know anything about it?"
    g "Uh— yeah."
    g "Come with us. We’ll take you to the commander."
    show s1g119 with dissolve   
    gg "We tried to get backup from the eastern sector..."
    gg "But—"
    show s1g116 with dissolve   
    mc "That’s enough. Move."
    play sounds1 ghoulsound1
    show s1g120 with dissolve 
    b "..."
    show s1g121 with dissolve   
    mc "Now!"
    show s1g122 with dissolve   
    gg "FOLLOW ME!"
    
    scene black with dissolve
    pause 2.5
    play sounds1 minigunfut 
    show s1g123 with dissolve   
    pause 1.5
    show s1g124 with dissolve   
    pause 1.5
    show s1g125 with dissolve   
    gg "First door, that’s the command post."
    gg "You’ll find the commander there."
    show s1g126 with dissolve   
    mc "Thank you."
    stop music fadeout 5.5
    scene black with dissolve
    pause 4.5
    play music executor fadein 3.0
    play sounds2 scifidooropen2
    show s1g131 with dissolve  
    Fl "Well, would you look at that…"
    Fl "Brings back memories."
    show s1g132 with dissolve 
    mc "You’ve been here before?"
    show s1g133 with dissolve  
    Fl "Sadly, yeah."
    Fl "Grew up around here."
    mc "Didn’t expect that. Thought you came from money."
    stop sounds4 fadeout 2.0
    play sounds2 footstep2
    show s1g134 with dissolve  
    Fl "Oh wow~ so I made a good first impression, then?"
    mc "Your father’s a big shot, isn’t he? So how’d that happen?"
    show s1g135 with dissolve  
    Fl "My dad..."
    Fl "the old man always had his principles."
    Fl "Thought he could make this sector… a little safer."
    play sounds2 footstep1
    show s1g136 with dissolve  
    mc "So you know people from around here?"
    Fl "...Yeah."
    Fl "Or what’s left of them."
    mc "..."
    play sounds2 footstep3
    show s1g137 with dissolve  
    mc "Hey, Flor?"
    mc "What did the blind man say when he walked into a bar?"
    mc "“Hello to everyone I couldn’t see!”"
    show s1g138 with dissolve  
    Fl "..."
    Fl "*A faint, almost reluctant chuckle.*"
    pause 0.6
    Fl "…Okay, yeah."
    Fl "That was stupid."
    Fl "But I’ll give you that— it was funny."
    pause 0.9
    Fl "…and..."
    Fl "...thanks."
    play sounds2 footstep1
    show s1g139 with dissolve  
    mc "..."
    play sounds2 footstep3
    show s1g140 with dissolve  
    mc "We don’t forget."
    play sounds2 footstep1
    show s1g142 with dissolve  
    Fl "Right."
    pause 1.1
    Fl "Focus."
    Fl "We’re here for information."
    play sounds2 footstep3
    show s1g144 with dissolve  
    mc "I’ll handle it."
    pause 1.1
    show s1g145 with dissolve  
    g "What about the civilians? We can’t deploy Titans in here."
    show s1g146 with dissolve  
    gg "If we just sit on this, the city’s going down!"
    show s1g147 with dissolve  
    ex "We clear the civilians. Fast."
    ex "Then we burn this sector to the ground. No hesitation."
    show s1g148 with dissolve  
    g "That’s insanity!"
    ex "No. That’s containment."
    ex "Sector 6 is still holding."
    ex "When it breaks and it will— we’re next in line."
    show s1g149 with dissolve  
    pause 0.6
    ex "...You."
    ex "...you’re that ear-girl’s friend, aren’t you?"
    ex "What’s an Inquisition lapdog doing in my warzone?"
    mc "Lower your voice."
    mc "If you had this under control, I wouldn’t be here."
    ex "..."
    Fl "You know him?"
    Fl "Full story later."
    show s1g150 with dissolve
    mc "I’ve seen the streets."
    mc "You need backup."
    mc "So talk. What’s left?"
    play sounds2 footstep3
    show s1g151 with dissolve  
    ex "We’re bleeding out."
    ex "Supplies - gone."
    ex "Comms- dead."
    ex "And my people are dropping one by one while we stand here talking."
    play sounds2 footstep1
    show s1g152 with dissolve  
    ex "One man…"
    ex "is not going to fix my battlefield."
    mc "Information."
    mc "Sector 8. The tower."
    ex "..."
    play sounds2 footstep3
    show s1g159 with dissolve  
    ex "Dave. Report."
    show s1g162 with dissolve  
    gg "That blast fried everything it could."
    gg "We’re deaf. Blind. Completely cut off."
    show s1g146 with dissolve  
    g "That’s exactly my point."
    g "We can’t afford to take any more risks!"
    g "We wait for a signal from the tower."
    show s1g163 with dissolve  
    mc "I’m not here for panic."
    mc "Sector 8. Tower. Now."
    show s1g166 with dissolve  
    ex "Sector 8. Old relay tower."
    play sounds2 ha volume 1.0
    show s1g167 with dissolve
    ex "Only way out of this mess."
    ex "Problem is— getting there alive."
    show s1g168 with dissolve  
    mc "How far?"
    show s1g169 with dissolve  
    gggg "Beyond the wall."
    mc "(Beyond the wall… this is gonna be rough.)"
    show s1g170 with dissolve  
    g "No one’s going beyond the wall right now."
    g "And if they do... they’re not coming back."
    g "We wait for word from the to—"
    show s1g171 with dissolve  
    gg "We don’t have time to wait!"
    mc "(Lora… she was out there too…)"
    show s1g172 with dissolve  
    mc "I’m going."
    Fl "Hey— hey, are you out of your mind?!"
    Fl "You were just supposed to—"
    mc "..."
    g "Alone?"
    show s1g173 with dissolve  
    mc "Less people, better odds."
    show s1g174 with dissolve  
    ex "No."
    ex "You don’t get to die on your own terms in my command."
    mc "You gonna stop me?"
    ex "No."
    ex "I’m going to make sure your death isn’t useless."
    show s1g175 with dissolve  
    gg "I’m going with him."
    gg "Better that than sitting around waiting for a miracle."
    show s1g176 with dissolve  
    ex "..."
    ex "Fine."
    ex "I’ll scrape together whoever’s still breathing."
    ex "You move as a unit. You follow orders."
    ex "You screw this up— don’t bother coming back."
    mc "Alright."
    stop music fadeout 2.0
    stop sounds1
    stop sounds2

    scene black with dissolve
    pause 1.5

    play sound roomambient loop
    show s1fg22 with dissolve  
    R "(The Inquisition…)"
    R "(They don’t even let you breathe.)"
    play sounds1 metalstep
    show s1fg23 with dissolve  
    R "(From a respected scientist....)"
    R "(To a glorified errand boy.)"
    R "(…Just wait.)"
    R "(All of you.)"
    play sounds1 metalstep
    show s1fg24 with dissolve  
    R "(whisper) You’ll pay for this."
    play music selmusiv fadein 2.0
    show s1fg25 with dissolve  
    R "What the—"
    show s1fg26 with dissolve  
    aa "You’re late."
    R "…I was delayed."
    show s1fg27 with dissolve  
    aa "You won’t share their fate."
    show s1fg28 with dissolve  
    R "…I released them."
    R "Just as you asked."
    show s1fg30 with dissolve  
    aa "We know, Doctor Li."
    aa "Her Highness is… pleased you made the right choice."
    show s1fg29 with dissolve  
    R "…We had an agreement."
    R "…My side of the deal."
    scene s1fg26 with dissolve  
    aa "Of course. Doctor, of course."
    
    show s1fg31 with dissolve  
    lad "..."
    
    show s1fg32 with dissolve
    lad "Tell Veira to come back."
    play sounds2 glitchfear volume 0.3
    show s1fg33 with glitch 
    yin "Yes, ma’am."
    play sounds3 warptravaling fadein 0.6 loop
    show s1fg34 with dissolve  
    lad "..."
    stop sounds3
    show s1fg35 with dissolve  
    lad "Now."
    show s1fg36 with dissolve  
    pause 1.1
    play sounds2 glitchfear volume 0.3
    show s1fg37 with glitch 
    aa "Not planning to run, Lady Astoria?"
    show s1fg38 with dissolve  
    am "What are you doing here?"
    show s1fg39 with dissolve  
    aa "Don’t pretend you don’t know."
    am "Gorem won’t like this."
    show s1fg40 with dissolve  
    sel "Father… mistook restraint for wisdom."
    sel "You started this. I’m simply continuing it."
    show s1fg41 with dissolve  
    am "What do you want."
    scene s1fg42 with dissolve  
    sel "What do I want?"
    sel "Balance. For my people."
    scene s1fg41 with dissolve  
    am "Don’t lie to me."
    play sounds2 glitchfear volume 0.3
    scene s1fg43 with glitch 
    y "(whispering) They’ve taken our planet hostage."
    am "..."
    scene s1fg45 with dissolve  
    sel "Don’t look at me like that."
    sel "You already understand the situation."
    sel "I’m offering you a way forward."
    sel "Refusing would be… inefficient."
    scene s1fg44 with dissolve  
    am "..."
    am "(The Inquisition?)"
    y "(I sent the messages, like you asked.)"
    y "(They’ll take care of Sector 8.)"
    stop sound fadeout 2.0
    stop music fadeout 2.0
    scene black with dissolve
    pause 1.5






label gate2:
    $ persistent.chapter_act1_scene += 1
    play music nightc fadein 1.5
    show s1h71 with dissolve  
    show 7yr with dissolve
    mc "…All set."
    mc "Weapons check. Gear’s in place."
    mc "Flor? What’ve you got on the data?"
    play sound mouseclick
    show s1h72 with dissolve  
    Fl "Hard to say."
    Fl "There’s nothing on Sector 8."
    Fl "Like… literally nothing."
    show s1h73 with dissolve  
    mc "And still no way to reach Olivia…"
    show s1h74 with dissolve  
    pause 1.1
    mc "Flor?"
    mc "How do these sectors even work?"
    show s1h75 with dissolve  
    Fl "Sectors— wait."
    Fl "You don’t know?!"
    Fl "Then how exactly were you planning to find—"
    Fl "...Ugh, fine."
    Fl "Short version?"
    Fl "A sector is just distance from the tower."
    show s1h76 with dissolve  
    mc "…That’s a weird system."
    scene s1h75 with dissolve  
    Fl "You think so?"
    Fl "I kinda like it."
    Fl "Besides, everyone’s used to it by now."
    show s1h77 with dissolve  
    mc "Then Sector 5-S…"
    mc "That makes it the fifth from the tower, right?"
    Fl "Mm-hm."
    mc "Then what does the ‘S’ stand for?"
    play sound mouseclick
    scene s1h72 with dissolve  
    Fl "‘S’ means sublevel."
    Fl "Underground."
    Fl "We’re in Sector 5-S right now."
    Fl "Basically the edge of the city."
    show s1h78 with dissolve  
    mc "..."
    mc "Wait."
    mc "If the walls are in Sector 6…"
    mc "why’s the tower in Sector 8, not 7?"
    show s1h79 with dissolve  
    Fl "You already know why."
    Fl "You’re just pretending you don’t."
    show s1h80 with dissolve  
    mc "Those ruins… in sector 7."
    mc "What happened to them?"
    show s1h81 with dissolve  
    Fl "..."
    show s1h82 with dissolve  
    mc "Flor?"
    Fl "...Not now."
    Fl "Just... not now."
    pause 0.8
    Fl "I found something more interesting."
    show s1h83 with dissolve  
    Fl "...contraband."
    mc "What exactly?"
    show s1h84 with dissolve  
    Fl "Remember that club?"
    Fl "Where we met Ember?"
    show s1h85 with dissolve  
    mc "..."
    mc "Let’s say I do."
    show s1h86 with dissolve  
    Fl "..."
    show s1h86 with dissolve  
    mc "Flor?"
    show s1h87 with dissolve  
    Fl "Yeah."
    Fl "I’m trying to phrase this delicately."
    Fl "City’s falling apart…"
    show s1h88 with dissolve  
    Fl "...and someone’s still paying good money for a custom piece of silicone the size of a small weapon."
    scene s1h87 with dissolve  
    Fl "Or not really small."
    scene s1h86 with dissolve  
    mc "..."
    mc "People adapt."
    scene s1h83 with dissolve  
    Fl "That’s one way to put it."
    Fl "...I was trying not to say it out loud."
    show s1h89 with dissolve  
    mc "You failed."
    Fl "...Yeah."
    stop music
    play sound whoosh
    show s1h90 with CropMove(time=0.2, mode='slideright') 
    play music dardd fadein 4.5 volume 0.15
    Fl "*A faint, reluctant chuckle.*"
    Fl "…Thanks."
    mc "..."
    show s1h90 with dissolve  
    mc "Back to the topic."
    
    play sound stepmc
    $ mc_powerup += 1
    show s1h91 with dissolve  
    mc "Nice try. Stay on it."
    mc "What’s wrong with the ruins?"
    play sounds1 rustling2 fadeout 1.5
    show s1h92 with dissolve  
    Fl "..."
    Fl "You know anything about the Tombs?"
    play sound stepmc fadeout 2.5
    play sounds1 rustling2 fadeout 2.5
    show s1h93 with dissolve  
    mc "Graveyard. That’s all I’ve heard."
    show s1h96 with dissolve  
    Fl "And you still don’t see it?"
    mc "Am I supposed to?"
    Fl "Here’s the thing—"
    Fl "No one knows when the tower was built."
    show s1h97 with dissolve  
    mc "Wait..."
    mc "Then who named the sectors?"
    show s1h98 with dissolve  
    Fl "...Exactly."
    Fl "No one knows."
    Fl "The sectors were already there long before us."
    play sounds1 rustling2 fadeout 4.5
    show s1h99 with dissolve  
    mc "Hold on, that doesn’t make any sense."
    scene s1h98 with dissolve  
    Fl "I don’t know."
    Fl "But people talk."
    Fl "They say those sectors hide tech way beyond our time."
    show s1h100 with dissolve  
    mc "Tombs…"
    stop music fadeout 5.1
    show s1h101 with dissolve  
    Fl "Now you get it."
    scene s1h98 with dissolve  
    Fl "But later."
    Fl "Your team’s here."
    play music dardd1 volume 0.5 
    play sound stepmc volume 0.7 fadein 0.2
    show s1h102 with dissolve  
    g "Our best shot is Sector 6, northeast gate."
    g "There’s an underground passage there. That’s how we get out of the city."
    play sound stepmc volume 0.7 fadein 1.0
    show s1h103 with dissolve  
    gg "We still gotta make it to Sector 6 first."
    show s1h104 with dissolve  
    g "You ready to move?"
    show s1h105 with dissolve  
    mc "Always."
    scene s1h104 with dissolve  
    g "Good. Coordinates are on their way." 
    g "We’ll link up with the other squad en route."
    scene s1h105 with dissolve  
    mc "Reinforcements?"
    show s1h104 with dissolve  
    g "It’s… an old friend of ours."
    g "He was already heading our way, we managed to reach him."
    scene s1h105 with dissolve  
    mc "Comms? I thought they were down."
    show s1h106 with dissolve  
    g "Doesn’t work. We had to use the old stuff."
    g "What was it called again…?"
    show s1h106 with dissolve  
    ggg "A radio."
    show s1h104 with dissolve  
    g "Range is crap, though."
    pause 1.1
    mc "Let’s move."
    show s1h107 with dissolve  
    g "Yeah. Move out."
    stop music fadeout 2.9

label gate3:
    scene black with dissolve   
    pause 2.8
    
    play sounds raincity3 volume 0.1 loop
    show s1h109 with dissolve  
    show 7yr with dissolve
    "Sector 6. Level One. Exit beyond the walls."
    mc "Made it to the location."
    mc "Too quiet…"
    hide 7yr with dissolve
    play sounds2 radio volume 0.09 loop 
    show s1h110 with dissolve  
    Fl "Should you be worried? Maybe."
    Fl "But that’s not today’s problem, is it?"
    Fl "Eyes forward."
    Fl "Do you see the gates?"
    stop sounds2 fadeout 1.0
    mc "I see them. "
    play sound stepmc volume 1.0 fadein 0.2
    play sounds2 radio volume 0.09 loop 
    show s1h112 with dissolve  
    Fl "..."
    Fl "Hey, [mc]?"
    stop sounds2 fadeout 1.0
    show s1h113 with dissolve  
    mc "Yeah?"
    play sound stepmc volume 1.0 fadein 0.2
    play sounds2 radio volume 0.09 loop 
    show s1h114 with dissolve  
    Fl "Once you step past those walls…"
    Fl "I lose you."
    Fl "And…"
    pause 0.6
    Fl "...yeah, about that."
    stop sounds2 fadeout 1.0
    play sounds2 radio volume 0.09 loop 
    show s1h115 with dissolve  
    Fl "Come back alive."
    Fl "Got it?"
    mc "I’ll do my best."
    Fl "You might be a weird old man…"
    Fl "but you’re… entertaining."
    Fl "Would be a shame to lose that."
    stop sounds2 fadeout 1.0
    play sound stepmc volume 1.0 fadein 0.2
    show s1h116 with dissolve  
    mc "…Since when?"
    mc "You’re burying me already, and I haven’t even left yet."
    play sounds2 radio volume 0.09 loop 
    show s1h117 with dissolve  
    Fl "I just said it, okay?!"
    stop sounds2 fadeout 1.0
    play sounds2 radio volume 0.09 loop 
    show s1h118 with dissolve  
    Fl "...fine."
    Fl "So tell me instead..."
    Fl "how did you meet Lora?"
    stop sounds2 fadeout 1.0
    play sounds2 radio volume 0.09 loop 
    Fl "I’ve heard things about her, but…"
    stop sounds2 fadeout 1.0
    show s1h119 with dissolve
    mc "And what kind of rumors are going around about her?"
    Fl "Hey! I asked first!"
    pause 1.1
    show s1h119 with dissolve  
    mc "We met, yeah…"
    mc "One night, a girl walks into my restaurant. Bunny suit. Says no one can see her but me."
    show s1h120 with dissolve  
    mc "I laugh it off, until I realize no one actually does. Not until I say her name out loud."
    mc "Wild story, right?"
    play sounds1 sth1 volume 0.4 fadeout 0.5
    show s1h123 with dissolve  
    pause 0.4
    show s1h125 with dissolve  
    mc "Too wild. None of that happened."
    mc "We met at university. Went on a date. That’s it."
    mc "…At least, that’s the version I stick to."
    show s1h124 with dissolve  
    Fl "..."
    play sounds2 radio volume 0.09 loop 
    Fl "...You absolute bastard."
    Fl "I almost believed you."
    Fl "Almost."
    stop sounds2 fadeout 1.0
    play music smcs fadein 4.9 volume 0.3
    play sounds2 radio volume 0.09 loop 
    show s1h126 with dissolve  
    Fl "...wait."
    Fl "Movement."
    Fl "West."
    stop sounds2 fadeout 1.0
    show s1h127 with dissolve  
    play sounds2 radio volume 0.09 loop 
    Fl "Stay sharp."
    stop sounds2 fadeout 1.0
    play sounds2 whoosh volume 1.0
    play sounds1 rustling2 volume 1.0
    show s1h128  
    mc "Understood."
    show s1h220 
    h "..."  
    stop music fadeout 1.3
    show s1h129 with dissolve 
    play sounds1 rustling2 volume 1.0 
    mc "Olivia...?!"
    show s1h130 with dissolve  
    mc "What are you doing here?!"
    mc "I thought you were back at HQ!"
    show s1h132 with dissolve  
    h "I was looking for you!"
    show s1h137 with dissolve  
    h "After what happened… I couldn’t just sit still."
    show s1h138 with dissolve  
    h "So yeah… here I am."
    scene s1h142 with dissolve  
    mc "But how did you find me?"
    scene s1h143 with dissolve  
    h "Miriel’s teacher told us where you were…"
    h "Without him… I don’t know what we would’ve done."
    scene s1h144 with dissolve  
    h "Speaking of help where’s that annoying cat?"
    h "Don’t tell me she bailed the second things got messy."
    play sounds2 radio volume 0.09 loop 
    scene s1h145 with dissolve  
    Fl "TELL THAT SELF-RIGHTEOUS GREMLIN I CAN HEAR HER—"
    Fl "and she’d better WATCH HER DAMN MOUTH."
    Fl "Without me, she’d be crying in some bunker right now!"
    stop sounds2 fadeout 1.0
    mc "..."
    scene s1h144 with dissolve  
    h "...Something wrong? You went quiet."
    scene s1h146 with dissolve  
    mc "Flora’s here." 
    mc "She’s… in my ear. And she heard everything."
    play sounds2 radio volume 0.09 loop 
    scene s1h147 with dissolve  
    Fl "And I demand an apology."
    stop sounds2 fadeout 1.0
    scene s1h148 with dissolve  
    h "Aww, poor thing. Want a medal?" 
    h "Or a standing ovation for doing your job?"
    play sounds2 radio volume 0.09 loop 
    scene s1h147 with dissolve  
    Fl "WHAT DID SHE JUST—"
    Fl "I SWEAR TO EVERY STAR—"
    stop sounds2 fadeout 1.0
    H "Connection temporarily lost. "
    scene s1h143 with dissolve  
    h "She still yelling?"
    scene s1h142 with dissolve  
    mc "Why do you keep provoking her?"
    scene s1h147 with dissolve  
    mc "..."
    play music utb1 fadein 5.4 volume 0.2
    scene s1h143 with dissolve  
    h "The way she treated you… I didn’t like that."
    scene s1h142 with dissolve  
    mc "In that case… you owe her an apology."
    scene s1h143 with dissolve  
    h "That’s not something I hear from you every day…"
    h "Alright."
    scene s1h142 with dissolve  
    mc "Tell me, Liv… are you sure you want to do this?"
    scene s1h149 with dissolve 
    h "..."
    scene s1h150 with dissolve  
    mc "..."
    scene s1h152 with dissolve  
    pause 0.5
    scene s1h153 with dissolve  
    pause 0.5
    scene s1h154 with dissolve  
    pause 0.5
    show s1h155 with dissolve  
    h "Team, remember?"
    h "From the start…"
    mc "...to the end."
    pause 1.1
    stop music fadeout 4.9
    show s1h156 with dissolve  
    h "...they’re here already?"
    pause 1.1
    play music pts fadein 3.3 volume 0.3
    show s1h157 with dissolve  
    o "Sector 6, east side’s already fallen."
    o "The rest… I don’t know yet."
    g "So that’s it? No backup?"
    o "Someone has to hold the city."
    show s1h158 with dissolve  
    g "..."
    gg "Chin up! Time to be heroes!"
    stop music fadeout 25.2
    show s1h160 with dissolve  
    Mi "Why did you rush ahead?"
    Mi "You could’ve been killed."
    scene s1h159 with dissolve  
    h "Oh, come on, I was a scout, remember?"
    h "I know how to get out of a mess in one piece."
    show s1h161 with dissolve  
    h "Besides, you weren’t exactly calm when all this started either."
    show s1h162 with dissolve  
    mc "Is it just me, or did you two get closer?"
    show s1h163 with dissolve  
    h "Hm? You think so?"
    show s1h164 with dissolve  
    h "We talked a bit."
    h "Turns out we’re not that different."
    show s1h165 with dissolve  
    h "Then we just sat there complaining about how unfair the world is."
    show s1h166 with dissolve  
    Mi "..."
    play music sneakysnitch volume 0.4 fadein 3.0
    show s1h169 with dissolve  
    Mi "..."
    show s1h170 with dissolve  
    Mi "And what exactly do you think you’re doing?"
    show s1h171 with dissolve  
    h "Oh, I noticed a little... tension in the atmosphere."
    show s1h172 with dissolve  
    h "So I figured I’d distract you a little!"
    h "(whispering) and looks like it worked."
    play sounds3 metalhit2 fadein 2.9
    show s1h173 with dissolve  
    Mi "…Let go."
    h "..."
    show s1h174 with dissolve  
    Mi "..."
    stop music fadeout 13.2
    show s1h175 with dissolve  
    h "Love you too!"
    Mi "…!"
    mc "Don’t wander too far."
    play music1 emotpi fadein 8.9 volume 0.4
    show s1h176 with dissolve  
    o "*quiet chuckle*"
    show s1h177 with dissolve  
    o "..."
    o "...I heard what you did."
    show s1h179 with dissolve  
    o "I owe you my daughter’s life."
    show s1h178 with dissolve  
    mc "What do you mean?"
    show s1h182 with dissolve  
    o "..."
    o "I saw it myself."
    o "You pulled her out of that."
    pause 1.1
    o "Thank you."
    scene s1h178 with dissolve  
    mc "Yeah."
    play sounds2 radio volume 0.09 loop 
    show s1h183 with dissolve  
    Fl "[mc]— do you hear me?!"
    Fl "The signal— it’s breaking up—!"
    Fl "Stay alive—"
    show s1h184 with dissolve  
    mc "...you too."
    stop sounds2 fadeout 1.0
    
    scene s1h183 with dissolve  
    mc "..."
    show s1h185 with dissolve  
    o "Flora?!"
    o "What happened?!"
    show s1h186 with dissolve  
    mc "Just the comms. It’s happened before."
    stop music1 fadeout 4.2
    play music sthe fadein 14.2 
    show s1h187 with dissolve  
    g "Sir. We’ve got a problem."
    o "What happened?"
    show s1h188 with dissolve  
    g "This."
    show s1h189 with dissolve  
    o "Why isn’t it open?"
    show s1h190 with dissolve  
    g "We… miscalculated."
    g "After that surge, the gate jammed."
    g "I can’t get it open."
    show s1h191 with dissolve  
    gg "We’ve got explosives." 
    gg "Let’s just turn the whole damn gate into dust!"
    show s1h192 with dissolve  
    g "Blow it open? Waste every round we’ve got on a door? Brilliant."
    g "And what do we fight with after that? Sharp looks and angry words?"
    show s1h193 with dissolve  
    g "That thing’s made of quantum titanium. It could shrug off a tank."
    show s1h194 with dissolve  
    mc "We were supposed to go underground from the start."
    mc "What’s the problem?"
    show s1h195 with dissolve  
    o "Problem is, the maps are a mess."
    o "And even if we had a clean route…"
    o "We’d still have to deal with the locals."
    play sounds2 bbom
    show s1h196 with dissolve  
    mc "...!"
    pause 0.2
    mc "(What the—)"
    show s1h197 with dissolve  
    mc "(OLIVIA!)"
    g "They started purging Sector 6?!"
    show s1h198 with dissolve  
    o "No more waiting." 
    o "We figure it out as we go."
    show s1h199 with dissolve  
    pause 1.1
    show s1h200 with dissolve  
    pause 0.5
    play sounds3 raincity3 loop volume 0.1
    play sounds hug2 volume 0.2
    show s1h204 with dissolve
    h "Hey, hey, miss me that much?"
    mc "Olivia! We’re leaving."
    show s1h206 with dissolve
    h "Wait, what was that explosion—?"
    show s1h207 with dissolve
    mc "Purge."
    scene s1h208 with dissolve
    h "A purge—?"
    scene s1h207 with dissolve
    mc "I’ll explain later."
    mc "Where’s Miriel?"
    play sounds4 glitchfear
    show s1h214 with glitch
    Mi "We’re leaving."
    Mi "The horde is almost here."
    play sounds bbom fadeout 2.3
    show s1h215 with vpunch
    mc "..."
    mc "We need to move."
    mc "This is getting worse by the second."
    show s1h218 with dissolve
    pause 0.6
    o "Everyone, into the tunnel! Move!"
    stop sounds3 fadeout 2.1

label gate4:
    stop music fadeout 5.5
    $ persistent.chapter_act1_scene += 1
    scene black with dissolve
    pause 4.2
    play sound spaceshipinto loop volume 0.2 fadein 2.0
    play music dangeom fadein 12.0 volume 0.5
    play sounds3 metalstep volume 0.1
    "Sector 6. Level 2. Ancient tunnels."
    show s1m1 with dissolve
    pause 1.1
    play sounds3 metalstep volume 0.1
    show s1m2 with dissolve
    mc "(Don’t like this place.)"
    mc "Status?"
    g "...I’ve got nothing. Visibility’s garbage."
    show s1m3 with dissolve
    o "Stay close."
    o "Easy to get lost down here."
    show s1m4 with dissolve
    mc "Where do we go?"
    show s1m5 with dissolve
    o "The nav-device still works locally."
    o "Short range only. Enough to keep us from getting lost."
    show s1m6 with dissolve
    o "Without it, we’re dead."
    play sounds3 rustling2 fadeout 2.1
    play sounds2 systemnotification
    show s1m8 with dissolve
    pause 0.5
    play sounds2 spacepick volume 0.3
    show s1m9 with dissolve
    o "Target’s a couple kilometers east."
    o "Sector 8-S."
    play sounds2 spacepick volume 0.3 fadein 0.2
    show s1m10 with dissolve
    o "Shortest route’s through this tunnel."
    play sounds4 stepmc
    show s1m11 with dissolve
    g "That one? That’s a death trap."
    g "One wrong shot and we’re buried."
    o "Got a better idea?"
    show s1m12 with dissolve
    g "We take the service route."
    play sounds3 clothess volume 0.2
    play sounds2 spacepick volume 0.3
    show s1m13 with dissolve
    g "Slower… but it won’t cave in on us."
    mc "We don’t have time for a detour."
    g "Too risky."
    play sounds3 rustling2 fadeout 2.1
    show s1m14 with dissolve
    mc "We take the risk."
    gg "Inquisitor’s got a point."
    o "Risk it is."
    o "Check your ammo."
    o "We don’t get a second try."
    show s1m15 with dissolve
    gg "Full."
    show s1m17 with dissolve
    o "And you?"
    show s1m19 with dissolve
    mc "Locked, loaded, and not in the mood to die."
    play sounds3 clothess volume 0.2
    show s1m20 with dissolve
    h "..."
    show s1m21 with dissolve
    h "Same. Let’s get this over with."
    show s1m22 with dissolve
    o "He’s right."
    o "Shortest route’s our only shot."
    g "(whispering) This is insane..."

    play sounds4 stepmc
    show s1m23 with dissolve
    pause 1.0
    show s1m24 with dissolve
    o "Right turn ahead."
    show s1m25 with dissolve
    o "No contacts—"
    o "...wait. Got the entrance."
    play sounds1 glitchfear
    show s1m26 with glitch
    Mi "So this is it."
    play sounds4 stepmc
    show s1m27 with dissolve
    o "According to the nav, yeah."
    Mi "…This is their territory."
    show s1m28 with dissolve
    mc "What are we walking into?"
    show s1m29 with dissolve
    pause 1.0
    show s1m30 with dissolve
    pause 1.3
    show s1m31 with dissolve
    Mi "…They didn’t tell you?"
    show s1m32 with dissolve
    mc "Clearly not."
    show s1m33 with dissolve
    Mi "…You should know."
    show s1m34 with dissolve
    o "Agreed..."
    o "Tell me…"
    o "you scared of something big enough to bite your head clean off?"
    mc "Not enough to turn back."
    show s1m35 with dissolve
    gg "Or we stop talking and just blow it open."
    g "You and your bombs…"
    g "It’s already open."
    show s1m36 with dissolve
    g "Move. Stay close. Eyes up."

    stop music fadeout 1.7
    stop sound
    
    scene black with dissolve
    pause 1.0
    play sounds4 spaceshipinto loop fadein 2.0
    play sounds3 footstep
    "Sector 7-S. Level 2. Ventilation drains."
    h "(whispering) It’s so damn dark… feels like we’re crawling through someone’s ass. Smells like it too."
    play sounds2 stepmc
    mc "Right behind me."
    scene s1k1 with dissolve
    o "Eyes up."
    o "No talking."
    o "Comms silent."
    play sounds1 nve volume 0.32 
    pause 0.2 
    play music tunnel1 fadein 1.1 
    scene s1k2 with dissolve
    o "Stay sharp."
    o "Crawlers don’t like company."
    play sounds3 footstep
    scene s1k3 with dissolve
    h "You still haven’t told us what those things actually are…"
    play sounds3 footstep
    scene s1k4 with dissolve
    Mi "Spiders… in your terms."
    play sounds3 footstep
    scene s1k5 with dissolve
    mc "(whispering) Spiders? That’s what we’re worried about?"
    play sounds3 footstep
    scene s1k6 with dissolve
    Mi "The smallest ones run about one to five meters."
    mc "...You’re kidding me."
    Mi "The rest…"
    play sounds3 footstep
    scene s1k7 with dissolve
    h "(whispering) Okay… yeah, maybe we turn around? Just saying."
    mc "(whispering) You scared?"
    pause 0.8
    mc "(whispering) Yeah. Me too."
    scene s1k8 with dissolve
    h "(whispering) I really don’t want to see those things, [mc]."
    mc "(whispering) Stay close."
    h "..."
    h "...Yeah."
    scene s1k9 with dissolve
    mc "What is this place supposed to be?"
    o "Ventilation shaft."
    o "Used to push air into the lower city."
    scene s1k10 with dissolve
    mc "...Used to?"
    o "..."
    o "...Crawlers."
    pause 0.8
    scene s1k11 with dissolve
    o "They didn’t like us being here."
    o "Started sealing everything."
    o "Webbing the tunnels shut."
    o "Anyone who tried to push through…"
    scene s1k12 with dissolve
    Mi "No survivors."
    scene s1k13 with dissolve
    mc "Then we change that."
    h "(whispering) It’s fine… I’ve got [mc]."
    stop music fadeout 7.2
    scene s1k14 with dissolve
    Mi "(whispering) Hey… Liv. You good?"
    scene s1k15 with dissolve
    h "(whispering) M-me? Yeah… I just... I hate spiders, okay?"
    scene s1k16 with dissolve
    mc "..."
    play  music battleground fadein 8.0
    scene s1k17 with dissolve
    mc "...We’re not alone."
    scene s1k18 with dissolve
    mc "That’s them?"
    scene s1k19 with dissolve
    o "What did you—"
    mc "Ceiling. Look."
    play sounds3 hit4
    pause 0.2
    scene s1k20
    o "..."
    o "Weapons up!"
    o "Lights on them— NOW!"
    play sounds4 rs1 loop volume 0.3
    scene s1k21 
    mc "Now I see why you hesitated…"
    scene s1k22 with dissolve
    o "Move! Push through!"
    scene s1k23 with dissolve
    h "Behind us!"
    stop sounds4  
    play sounds scar1
    play sounds4 hdshot
    scene s1k25 
    pause 0.5
    play sounds2 fall
    scene s1k26 
    pause 0.5
    scene s1k27 with dissolve  
    mc "I owe you one."
    scene s1k28 with dissolve  
    h "...just like Drake."
    scene s1k29 with dissolve  
    h "Chaos, smoke, no backup… good times."
    play sounds4 rs1 loop volume 0.3
    play sounds2 scar1 loop
    scene s1k30 with dissolve  
    mc "Yeah."
    scene s1k31 with dissolve  
    mc "Except back then, they didn’t have eight legs and acid blood."
    stop sounds4
    stop sounds2 
    play sounds riflesound1 loop volume 0.2
    scene s1k32 with dissolve  
    g "They’re closing in! We’re surrounded!"
    play sounds3 killmutant loop volume 0.1
    scene s1k33 with dissolve  
    pause 0.5
    scene s1k34 with dissolve  
    pause 1.1
    play sounds2 rs1 loop volume 0.3
    scene s1k37 with dissolve  
    pause 1.1
    scene s1k38 with dissolve  
    pause 1.1
    scene s1k39 with dissolve  
    o "Miriel, status?"
    stop sounds fadeout 1.9
    stop sounds1 fadeout 1.9
    stop sounds2 fadeout 1.9
    stop sounds3 fadeout 1.9
    stop sounds4 fadeout 1.9
    scene s1k41 with dissolve  
    Mi "One inhibitor left. Almost there!"
    play sounds3 systemvoice
    scene s1k42 
    H "All phases complete. Reaper mode activated. Happy hunting, Miss Miriel."
    play sounds4 glitchfear
    scene s1k43 with glitch
    pause 1.0
    play sounds2 whoosh4
    scene s1k44 with CropMove(time=0.1, mode='slideleft')
    pause 0.8
    play sounds hdshot 
    play sounds3 killmutant volume 0.1
    play sounds2 spaceshipinto loop fadein 2.0 volume 0.1
    scene s1k45 with vpunch
    H "Task complete. Enemy casualties: 67."
    stop music fadeout 3.2
    play sounds1 systemvoice1
    play sound fcy
    scene s1k46 
    H "Warning. Activation code denied. Weapons deactivated."
    Mi "…Every time…"
    Mi "it gets worse."
    show s1k47 with dissolve  
    mc "What was that? She... how did she—?"
    show s1k48 with dissolve  
    o "She was built for war."
    show s1k72 with dissolve  
    o "Just like you."
    play sounds3 monstergrowl
    pause 0.6
    show s1k74  
    b "..."
    show s1k75 
    h "...That didn’t sound friendly."
    scene s1k74 with dissolve  
    o "...That’s bad."
    o "That’s really bad."
    play music runsongm fadein 1.4
    play sounds4 grouprun loop volume 0.04
    show s1k76 with dissolve  
    o "RUN!"
    show s1k77 with dissolve  
    mc "What the hell are we running from?!"
    show s1k78 with dissolve  
    o "Trust me, you don’t want to know."
    o "Move! Now!"
    scene s1k79 with dissolve  
    mc "(What the hell did we just walk into…?)"

    image mon1 = Movie(channel="movie_dp", loop = False, play="video/mon1.webm")
    show mon1 
    $ renpy.pause(3.4, hard=True)

    play sounds3 monstergrowl
    scene s1k80 with dissolve  
    mc "(…Okay. Now I get it.)"
    scene s1k82 with dissolve  
    gg "Over here! Move!"
    gg "We’ll hold it!"
    

    image mon2 = Movie(channel="movie_dp", loop = False, play="video/mon2.webm")
    show mon2 
    $ renpy.pause(6.1, hard=True)
    play sound rl2

    scene s1k81 with dissolve  
    gg "TAKE THAT, YOU BASTARD!"
    play sounds4 bbom
    scene s1k83 with dissolve  
    gg "Keep it back!"
    gg "Show it what happens when it picks a fight with us!"

    scene s1kk1 with dissolve  
    o "Status. You good to move?"
    Mi "I… can’t."
    Mi "My body’s not responding."
    scene s1kk2 with dissolve  
    o "Someone stays with he-"
    scene s1kk3 with dissolve  
    mc "I’ve got her."
    o "..."
    o "Good, then we move."
    scene s1kk4 with dissolve  
    g "Second wave incoming!"
    g "We stall even a second, we’re dead!"

    stop music 
    stop sound
    stop sounds1
    stop sounds2
    stop sounds3
    stop sounds4
    play sounds2 cinematichit1


    scene black 
    scene black with dissolve
    pause 3.5

    play music aioa fadein 5.4 volume 1.0
    play sound spaceshipinto loop fadein 2.0 volume 0.2
    play sounds stepmc volume 0.1
    show s1k85 with dissolve
    show 7yr with dissolve 
    mc "How’re you holding up, Liv?"
    hide 7yr
    play sounds stepmc volume 0.1
    show s1k86 with dissolve
    h "Still a bit shaky."
    h "Pretty sure I won’t be sleeping anytime soon after… that."
    play sounds stepmc volume 0.1
    show s1k87 with dissolve
    mc "Hey, you wanted a change of scenery."
    h "Oh, screw you."
    h "Yeah, I wanted that, but fighting things—"
    h "—with more eyes than sense—"
    h "...was NOT part of the deal."
    play sounds stepmc volume 0.1
    show s1k88 with dissolve
    mc "..."
    mc "We’ll make it back."
    mc "And I’ll make it up to you."
    play sounds1 rustling2 volume 0.2
    show s1k89 with dissolve
    h "I’ll hold you to that…"
    h "Oh, and looks like Sleeping Beauty’s up."
    h "How you feeling, sweetheart?"
    show s1k90 with dissolve
    Mi "…Liv?"
    Mi "…Where are we?"
    show s1k91 with dissolve
    mc "Somewhere around Sector 7. Middle levels, I think."
    Mi "..."
    Mi "You’ve… been carrying me this whole time?"
    mc "We’re a team. Remember?"
    Mi "..."
    Mi "(whispering) …Thank you."
    play sounds1 rustling2 volume 0.7
    show s1k92 with dissolve
    Mi "…Did anything else happen?"
    show s1k93 with dissolve
    mc "Not really."
    mc "We ran. Ended up here."
    show s1k94 with dissolve
    mc "Feels like a dead zone."
    mc "Too quiet."
    mc "Even those things avoid it."
    mc "Like they know something we don’t."
    show s1k95 with dissolve
    h "Oh, come on… Mir, you were incredible!"
    h "One second, boom! And all the spiders just GONE!"
    show s1k96 with dissolve
    h "THAT WAS"
    h "JUST"
    h "SO DAMN COOL!"
    show s1k97 with dissolve
    mc "Yeah."
    mc "You were impressive."
    Mi "..."
    Mi "…Th-thank you…"
    play sounds stepmc volume 0.1
    show s1k98 with dissolve
    o "Hey— [mc], got a second."
    show s1k99 with dissolve
    mc "Something wrong?"
    show s1k100 with dissolve
    g "According to the scanner… we’re already there."
    mc "We’re in Sector 8 already?"
    play sounds clothess volume 0.4
    show s1k101 with dissolve
    g "That’s the problem."
    g "Something’s off."
    g "Either the nav’s bugged…"
    show s1k112 with dissolve
    g "Or the data was wrong to begin with."
    mc "So what’s the plan?"
    play sounds rustling2 volume 0.4
    show s1k102 with dissolve
    g "No idea…"
    g "We can push deeper into Sector 8 and try to find it—"
    g "But if this is another dead lead—"
    play sounds clothess volume 0.4
    stop music fadeout 13.1
    show s1k103 with dissolve
    gggg "CONTACT FRONT!"
    show s1k104 with dissolve
    gggg "Identify yourself!" 
    gggg "Division and clearance! NOW!"
    a "..."
    play sounds rustling2 volume 0.4
    play sounds stepmc volume 0.1
    show s1k105 with dissolve
    gg "I don’t like this…"
    o "I’ll check it out."
    show s1k106 with dissolve
    o "If he so much as twitches, drop him."
    play sounds1 stepember volume 0.3
    play music inquisition fadein 2.9 volume 0.5
    a "No need."
    show s1k107 with dissolve
    a "He won’t be moving again."
    a "He was dead long before you got here."
    play sounds mmove 
    show s1k108 with dissolve
    o "..."
    o "...What brings a War Maiden down here?"
    show s1k109 with dissolve
    a "Curiosity."
    a "…And maybe a bit of judgment."
    a "Lower your weapon."
    play sounds mmove 
    show s1k110 with dissolve
    a "Good."
    o "..."
    show s1k111 with dissolve
    a "Now explain."
    a "Why are you here?"
    show s1k113 with dissolve
    o "I figured we might be here for the same rea—"
    play sounds rustling2 volume 0.4
    show s1k114 with dissolve  
    a "Careful."
    a "Say too much, and I’ll kill you."
    a "But you already knew that."
    show s1k115 with dissolve  
    mc "Why are we hiding?" 
    show s1k116 with dissolve
    h "(whispering) They’re insane."
    h "(whispering) If she sees your uniform… I don’t know what she’ll do."
    show s1k117 with dissolve  
    mc "Li—"
    h "(whispering) Trust me."
    Mi "..."
    show s1k118 with dissolve  
    a "Well, well... the Cold Reaper herself."
    a "How are you, pointy-ears?"
    a "And how’s your chaplain holding up?"
    Mi "I’m well."

    show s1k119 with dissolve  
    o "She’s n-"
    show s1k120 with dissolve  
    a "Don’t interrupt me."
    o "..."
    a "You’re coming with me."
    o "...Alright."
    show s1k115 with dissolve  
    mc "(…So that’s why everyone’s on edge around them.)"
    mc "(Too calm. Doesn’t fit the rest.)"
    play sounds rustling2 volume 0.4
    show s1k121 with dissolve  
    a "..."
    a "Interesting..."
    play sounds stepmc volume 0.4
    show s1k122 with dissolve  
    Mi "I refuse."
    a "Hm..."
    a "Alright."
    show s1k123 with dissolve  
    Mi "..."
    o "(whispering) Watch them."
    o "(whispering) Until she figures it out—"
    Mi "She knows."
    Mi "She’s just pretending she doesn’t."
    show s1k124 with dissolve  
    a "Commander, time is ticking."
    o "On my way."

    stop music fadeout 4.5
    scene black with dissolve  
    pause 1.5

    play sounds stepmc volume 0.4
    show s1k125 with dissolve  
    show 7yr with dissolve
    h "Hey, Mir… what was that back there?"
    hide 7yr with dissolve
    show s1k126 with dissolve  
    mc "She knew about us, didn’t she?"
    h "Wait what?!"
    Mi "…Yes."
    mc "Then why were we hiding?"
    Mi "…It was a performance."
    Mi "For the others."
    show s1k127 with dissolve  
    mc "Where’d the others go?"
    Mi "Sector 8."
    Mi "Next checkpoint."
    mc "And us?"
    Mi "..."
    play sounds clothess volume 0.1
    show s1k128 with dissolve  
    mc "Splitting up right now is a bad call."
    mc "I’m not playing hide-and-seek with them every step we take."
    Mi "..."
    play sounds clothess volume 0.1
    show s1k129 with dissolve  
    h "Sorry, Mir, but I’m with [mc] on this."
    h "Yeah, she’s dangerous. Creepy as hell, sure."
    h "But we’re not exactly helpless either."
    show s1k130 with dissolve  
    h "And honestly…"
    h "I can’t shake the feeling you were trying to ditch us."
    h "Would actually make that whole little performance make a lot more sense."
    show s1k131 with dissolve  
    Mi "N-no… it’s not like that…"
    mc "We’re not pushing you, Mir."
    mc "But don’t treat us like we’re stupid."
    show s1k132 with dissolve  
    h "Yeah."
    h "We’re a team, remember?"
    show s1k133 with dissolve  
    Mi "..."
    Mi "We need somewhere safe."
    scene s1k134 with dissolve  
    mc "Alright."
    scene s1k135 with dissolve  
    mc "Let’s move."

label olivia_fr_scene:

    scene black with dissolve  
    stop sound fadeout 0.5
    play sounds stepmc volume 0.4
    play sounds3 drc volume 0.1
    pause 2.5
    
    $ persistent.chapter_act1_lewd_scene += 1
    play music storetroom fadein 15.2 volume 0.1
    show s1k136 with dissolve  
    Mi "Dusty… dirty…"
    Mi "It’ll do."
    h "I think you’re dodging the real question."
    show s1k137 with dissolve  
    Mi "..."
    Mi "I…"
    mc "(We’re pushing her too hard.)"
    show s1k138 with dissolve  
    mc "Mir?"
    Mi "Hm?"
    mc "Why the mask?"
    show s1k139 with dissolve  
    Mi "..."
    Mi "I already told you."
    h "Yeah, yeah gas, I heard you. Come on, I feel fine."
    h "Go on, take it off."
    play sound rustling2 
    show s1k140 with dissolve  
    Mi "...Alright."
    show s1k141 with dissolve  
    h "...Gorgeous."
    Mi "..."
    Mi "…Thank you."

    scene s1deg25 with dissolve  
    mc "(A performance…)"
    pause 0.8
    mc "(…wait.)"
    mc "(Something’s off.)"

    scene s1h143 with dreamyzoom   
    show memoryframe with dissolve 
    h "Miriel’s teacher told us where you were…"

    scene s1deg26 with dissolve  
    mc "(How did he know…?)"
    mc "(No… if he was watching, then—)"

    scene s1rew178 with dreamyzoom
    show memoryframe with dissolve 
    mc "(She was being watched.)"

    scene s1deg26 with dissolve  
    pause 0.6
    scene s1deg27 with dissolve  
    mc "(I don’t like where this is going.)"
    scene s1deg28 with dissolve  
    mc "Something’s not adding up."
    mc "No comms… so how did your teacher know where to find me?"
    show s1k148 with dissolve  
    h "Yeah… wait, how would he even know…?"
    play sound rustling2 
    show s1k149 with dissolve  
    pause 1.1
    show s1k146 with dissolve  
    Mi "…Because of the implants."
    scene s1deg29 with dissolve  
    mc "..."
    scene s1deg30 with dissolve  
    h "Meaning what, exactly?"
    Mi "[mc] has the same one as my teacher."
    Mi "I don’t fully understand how they work, but…"
    Mi "they send signals between—"
    h "In plain English?"
    Mi "A local signal."
    Mi "Not the city network. Implant to implant."
    Mi "Short range."
    scene s1deg31 with dissolve  
    mc "(Local signal…?)"
    mc "(Then how…?)"

    scene s1pp42 with dreamyzoom
    show memoryframe with dissolve 
    sci "The Inquisition! They’ve found-"
    scene s1pp45 with dreamyzoom
    show memoryframe with dissolve 
    o "Your implants…"
    o "...we took them. Without asking."
 
    scene s1deg31 with dissolve  
    mc "(Why didn’t they take them right away?)"
    scene s1deg32 with dissolve  
    mc "Liv… your teacher."
    mc "Who is he?"

    scene s1deg33 with dissolve  
    pause 0.7
    scene s1deg34 with dissolve  
    Mi "The Chaplain."
    scene s1deg33 with dissolve  
    mc "...who?"
    scene s1deg34 with dissolve  
    Mi "He’s… the link between the Lady and the Inquisition."
    scene s1deg35 with dissolve  
    h "You never told me that…"
    scene s1deg36 with dissolve  
    Mi "..."
    h "What?"
    mc "(Still doesn’t explain the act…)"

    scene s1g116 with dreamyzoom   
    show memoryframe with dissolve 
    gg "...they’re already inside."

    show s1k94 with dreamyzoom
    show memoryframe with dissolve 
    mc "...know something we don’t."

    scene s1deg37 with dissolve  
    mc "We’re not here for the tower, are we?"
    Mi "..."
    scene s1deg38 with dissolve  
    mc "Then the silence…"
    mc "and that Inquisition girl showing up..."
    mc "it all lines up too well."

    scene s1deg39 with dissolve  
    h "You’re… overthinking this."
    scene s1deg40 with dissolve  
    h "It’s like you’re—"
    scene s1deg41 with dissolve   
    mc "OLIVIA!"
    play sound hug2
    show s1deg42 with vpunch
    mc "Liv?! Hey—"
    mc "What's wrong?!"
    show s1deg43 with dissolve  
    mc "Miriel?!"
    show s1deg44 with dissolve  
    pause 0.8
    Mi "..."
    show s1deg45 with dissolve  
    Mi "(This isn’t good…)"
    show s1deg46 with dissolve  
    Mi "She inhaled gas."
    Mi "Lay her down."
    Mi "I’ll… find a stabilizer."
    play sounds2 rustling2 
    show s1k166 with dissolve  
    Mi "..."
    play sounds2 rustling2 
    show s1k167 with dissolve  
    Mi "…Hold her steady."
    Mi "Vitals are crashing— "
    Mi "…Come on, come on…"
    pause 1.1
    play sounds3 sug
    Mi "…She’s stable."
    stop music fadeout 13.9
    play sounds4 generatoroom volume 0.1
    show s1k168 with dissolve  
    pause 0.8 
    scene black with dissolve 
    pause 3.3 
    

    play sound stepmc
    scene s1k169 with dissolve  
    "A couple of minutes later."
    play sounds2 rustling2 
    show s1k170 with dissolve  
    pause 1.0   
    show s1k171 with dissolve  
    Mi "..."
    play music iif volume 0.3 fadein 8.2
    show s1k173 with dissolve  
    mc "So?"
    show s1k172 with dissolve  
    Mi "Let her rest for now."
    Mi "She should come to soon."
    scene s1k173 with dissolve
    mc "Good."
    mc "Glad to hear it."
    pause 1.1
    mc "And you?"
    scene s1k176 with dissolve  
    Mi "Trying to sort out my thoughts…"
    Mi "And… understand."
    scene s1k177 with dissolve  
    b "..."
    scene s1k173 with dissolve 
    mc "Understand what?"
    scene s1k174 with dissolve  
    Mi "..."
    scene s1k172 with dissolve  
    Mi "Sometimes… I don’t understand…"
    Mi "if I’m even going the right way."
    scene s1k173 with dissolve  
    mc "If you want to talk… I’m listening."
    scene s1k172 with dissolve  
    Mi "That’s… a rather personal question."
    Mi "Why are you looking for Lora?"
    scene s1k174 with dissolve  
    mc "..."
    scene s1k172 with dissolve  
    Mi "S-sorry… that was stu—"
    scene s1k173 with dissolve  
    mc "Hey— no."
    mc "It’s fine."
    mc "Just… wasn’t expecting that."
    scene s1k174 with dissolve  
    pause 1.1
    scene s1k178 with dissolve  
    mc "Why am I looking for Lora…"
    mc "(…Yeah. Why?)"
    pause 0.6
    mc "...Because of the past."
    scene s1k176 with dissolve  
    Mi "…past?"
    scene s1k178 with dissolve  
    mc "I spent most of my life with her."
    mc "Grew up with her."
    mc "...Truth is—"
    scene s0pp31 with dreamyzoom
    show memoryframe with dissolve 
    pause 1.7
    scene s0pp34 with dreamyzoom
    show memoryframe with dissolve 
    pause 0.7
    scene s1k178 with dissolve  
    mc "...I wouldn’t have made it without her."
    scene s1k175 with dissolve  
    pause 0.7
    Mi "…I see."
    Mi "And changing it?"
    Mi "Did you ever try to change anything?"
    scene s1k173 with dissolve  
    mc "I tried."
    mc "More than once."
    mc "...Didn’t really change anything."
    scene s1k172 with dissolve  
    Mi "My teacher… once told me…"
    Mi "…as long as you haven’t stopped—"
    Mi "you can still fix things."
    scene s1k174 with dissolve  
    pause 1.1
    scene s1k173 with dissolve  
    mc "He sounds important to you."
    scene s1k172 with dissolve  
    Mi "Yes…"
    Mi "Without him, I…"
    scene s1k173 with dissolve  
    mc "So what is he to you?"
    show s1k174 with dissolve  
    pause 0.8
    scene s1k175 with dissolve  
    Mi "A father figure."
    show s1k176 with dissolve  
    Mi "…I think."
    scene s1k178 with dissolve  
    mc "Yeah…"
    mc "Guess we’re not that different."
    scene s1k177 with dissolve  
    pause 0.7
    scene s1k172 with dissolve  
    Mi "...yeah."
    scene s1k177 with dissolve  
    Mi "..."
    scene s1k172 with dissolve  
    Mi "You know… Olivia talked about you a lot."
    scene s1k178 with dissolve  
    mc "Liv talked about me?"
    mc "Heh."
    mc "You want the story?"
    scene s1k177 with dissolve  
    pause 0.7
    scene s1k172 with dissolve  
    Mi "…Yes."
    scene s1k178 with dissolve  
    mc "...Alright."
    mc "Where do I even start…"
    stop music fadeout 3.2

    play music1 warmagain fadein 8.3 volume 0.5
    scene black with dissolve  
    pause 1.5
    play sounds4 windlight fadein 9.3 loop volume 0.2
    show s1k179 with dissolve  
    mc "(…Oh. Yeah.)"
    mc "(We started with nothing.)"
    mc "(A storage corner, a tiny kitchen… and a couple of stupid dreams.)"
    mc "(That was it.)"
    show s1k180 with dissolve  
    mc "(At first it was just the two of us. No experience. No clue what we were doing.)"
    mc "(Still… people kept showing up.)"
    mc "(Somehow.)"
    mc "(So we figured— guess we’re doing something right.)"
    mc "(And then… we needed help.)"
    show s1k181 with dissolve  
    L "Hey, love?"
    L "Where did you find this beauty?"
    show s1k182 with dissolve  
    mc "Found her wandering the streets. Looking for work."
    show s1k183 with dissolve  
    mc "...Couldn’t just walk past that."
    show s1k184 with dissolve  
    mc "(Truth is… she reminded me of myself back then.)"
    mc "(And something in me just… clicked.)"
    show s1k185 with dissolve  
    L "You know… I’m starting to question your talent."
    L "The number of girls in trouble you somehow keep finding?"
    L "It’s getting a little suspicious."
    L "...But I’ll allow it."
    L "Sweetheart, give us a smile."
    show s1k186 with dissolve  
    h "Like this?"
    b "..."
    L "Mmm… close."
    L "We’ll work on that."
    show s1k187 with dissolve  
    mc "She’s got heart."
    mc "Just… doesn’t quite fit yet."
    show s1k188 with dissolve  
    b "..."
    h "Did I do something wrong?"
    show s1k189 with dissolve  
    mc "…I don’t say this often… but you’re beautiful."
    scene s1k188 with dissolve  
    h "Wha—"
    h "But your wife—"
    show s1k190 with dissolve  
    L "I agree with him."
    scene s1k188 with dissolve  
    h "Huh?!"
    scene s1k189 with dissolve 
    mc "Hey… love, mind bringing that over?"
    play sounds2 rustling2
    show s1k191 with dissolve  
    L "You read my mind."
    show s1k192 with dissolve   
    mc "..."
    mc "...Hey."
    mc "Your name’s Olivia, right?"
    mc "Hey… relax, okay? You’re way too tense."
    show s1k194 with dissolve  
    mc "If something doesn’t feel right here—"
    show s1k193 with dissolve  
    h "N-no, no! I like it, I really do! It’s just…"
    h "It’s just… you’re the first people, strangers, who’ve been this kind to me."
    h "I keep waiting for the catch… but I can’t seem to find one."
    scene s1k194 with dissolve  
    mc "(Back then… I had no idea that shy little girl would end up changing everything for us.)"
    play sounds1 whoosh
    play sounds2 rustling2
    scene s1k195 with CropMove(time=0.1, mode='slideleft')
    L "Funny, isn’t it?"
    L "Such a small detail… and everything changes."
    show s1k196 with dissolve  
    L "(whispering) Easy, sweetheart… don’t tense up."
    show s1k198 with dissolve  
    L "Alright, sweetheart— we’re curious."
    L "What do you think?"
    scene s1k199 with dissolve  
    h "I… how much do I need to pay for this?"
    show s1k197 with dissolve  
    mc "Pay? No. It’s on the house."
    show s1k200 with dissolve  
    h "Wha—"
    h "THANK YOU!"
    h "Thank you so much for this opportunity!"
    h "I’ll do everything I can, I won’t let you down."
    mc "(She really did try… like, really try. But—)"

    scene black with dissolve  
    pause 1.5
    play sounds2 platebroke

    
    show s1k201 with dissolve  
    h "OH COME ON! Not again..."
    mc "(God… she was clumsy.)"
    mc "(Always dropping something.)"
    play sounds2 rustling2
    scene s1k202 with dissolve  
    mc "(...but we never made a big deal out of it.)"
    mc "(Didn’t feel right.)"
    mc "(Honestly… most people would’ve kicked her out in a week.)"
    play sounds2 bodytap
    scene s1k203 with dissolve  
    mc "(We didn’t even think about it.)"
    mc "(We just… stuck with her.)"
    mc "(’Cause we knew exactly what that felt like.)"

    stop music1 fadeout 5.4
    stop sounds4 
    play sounds4 generatoroom volume 0.3 loop
    scene s1k204 with dissolve  
    mc "I think… that’s why she got so attached to us."
    mc "We didn’t treat her like a problem."
    scene s1k205 with dissolve  
    mc "And hey— gotta give her credit too."
    mc "Most people would’ve cracked under that kind of pressure."
    mc "...She didn’t."
    mc "Not once."
    scene s1k206 with dissolve  
    Mi "…That’s quite a story."
    scene s1k208 with dissolve 
    Mi "It makes me wonder…"
    Mi "how different things might’ve been…"
    Mi "if someone had given me that chance."
    scene s1k205 with dissolve  
    mc "What do you mean?"
    scene s1k206 with dissolve  
    Mi "…It’s nothing."
    play sounds2 clothess volume 0.2
    scene s1k207 with dissolve  
    mc "You never told us your story."
    scene s1k209 with dissolve  
    mc "Only if you want to."
    mc "No pressure."
    play sounds2 rustling2
    scene s1k210 with dissolve  
    Mi "Maybe one day."
    Mi "For now… I’ll check the perimeter."
# 
    play sounds3 stepmc volume 0.2
    scene black with dissolve  
    pause 3.5

    
    scene s1k211 with dissolve 
    show 7yr with dissolve 
    mc "(…Miriel’s been gone too long.)"
    hide 7yr with dissolve
    mc "(Should I check…?)"
    mc "(No. Can’t leave Olivia alone.)"
    mc "(…Why isn’t she waking up…?)"
    play sounds2 rustling2 volume 0.3
    scene s1k212 with dissolve  
    h "Mmm..."
    scene s1k213 with dissolve  
    h "Mmm... No, not yet... please..."
    scene s1k214 with dissolve  
    h "...Not here... not in front of them..."
    scene s1k216 with dissolve  
    mc "(…Dreaming?)"
    play sounds2 clothess volume 0.4
    scene s1k217 with dissolve  
    mc "Olivia... hey." 
    mc "Wake up. You with me?"
    scene s1k218 with dissolve  
    h "No... just a few more minutes..."
    scene s1k219 with dissolve  
    h "..."
    scene s1k220 with dissolve  
    h "...Why’d you pull me out of something that perfect…?"
    play sounds2 rustling2
    scene s1k221 with dissolve  
    h "..What... what happened?" 
    h "Why are we on the ground? And where’s Miriel?"
    scene s1k222 with dissolve  
    mc "You passed out."
    mc "Gas in the air."
    mc "Miriel stepped out. She’ll be back."
    scene s1k223 with dissolve  
    h "..."
    scene s1k224 with dissolve  
    mc "How do you feel?"
    mc "You had us worried."
    scene s1k226 with dissolve  
    h "...sorry… didn’t mean to worry you…"
    scene s1k224 with dissolve  
    mc "Hey… it’s alright."
    mc "You’re awake. That’s what matters."

    play sounds drc
    play sounds2 rustling2
    scene s1k253 with dissolve  
    Mi "How… is Olivia?"
    scene s1k254 with dissolve  
    h "Oh, Mir. Just woke up."
    Mi "How are you feeling?"
    h "I’ll live."
    scene s1k261 with dissolve  
    Mi "Then we move."
    mc "Where’s the rush?"
    Mi "I… found tracks."
    mc "(Tracks…?)"

    

    



    
label final2:

    # scene black
    # pause 1.5
    # if ivy_help == True:
    #     play music nightc fadein 1.5
        
    #     play sound mouseclick
    #     scene s1l21 with dissolve
    #     Fl "Connect. Just connect already, damn you!"
    #     play sound mouseclick
    #     scene s1l22 with dissolve
    #     Fl "I entered everything right! Why won’t you work!?"
    #     Fl "This interface is garbage. Who designed this crap—"
    #     play sound scifidooropen2
    #     scene s1l23 with dissolve
    #     a "Need a hand?"
    #     scene s1l24 with dissolve
    #     Fl "Honestly? Yes. As long as you don’t slow me down."
    #     scene s1l25 with dissolve
    #     a "Always this charming, or am I just special?"
    #     scene s1l26 with dissolve
    #     Fl "This is my charming. Got a problem with it?"
    #     play sounds2 chairroll
    #     scene s1l27 with dissolve
    #     Fl "Mysterious stranger."
    #     play sounds1 stepmc
    #     scene s1l28 with dissolve
    #     a "Not at all. I find it... endearing."
    #     scene s1l29 with dissolve
    #     i "It’s been a long time, hasn’t it?"
    #     scene s1l27 with dissolve
    #     Fl "...So it’s you."
    #     play sounds1 stepmc
    #     play sounds2 rustling2
    #     scene s1l30 with dissolve
    #     i "Yeah. It’s me. What’s the issue?"
    #     scene s1l32 with dissolve
    #     Fl "Aside from this junk terminal? Protocol conflict. System keeps throwing a 418."
    #     Fl "I’ve cleared cache, rerouted DNS, even bypassed the firewall. Still nothing."
    #     play sound mouseclick
    #     scene s1l33 with dissolve
    #     Fl "And the worst part? It connects sometimes. Like it’s being sabotaged."
    #     scene s1l31 with dissolve
    #     i "Or the signal’s unstable."
    #     i "Let me take a look. I have a few tricks you haven’t ruined yet."

    #     stop sound
    #     stop music
    #     stop music1
    #     scene black with dissolve
    #     pause 1.5

    $ persistent.chapter_act1_scene += 1
    stop sounds2 
    stop sounds3
    stop sounds4
    stop sound
    stop sounds1
    scene black with dissolve
    pause 1.5
    play sounds1 stepmc
    play sounds2 towers loop
    play music unbound1 fadein 0.2

    scene s1l1 with dissolve  
    pause 1.0
    "Sector 7-S."
    scene s1l2 with dissolve  
    Mi "The tracks… lead here."
    play sounds1 stepmc
    scene s1l3 with dissolve  
    h "Tracks? Hey, Mir… you sure we should keep going?"
    h "Just the three of us… yeah, I really don’t like this."
    play sounds1 stepmc
    scene s1l4 with dissolve  
    mc "You didn’t bring us here for nothing."
    mc "What did you find?"
    Mi "I-I think…"
    Mi "this is one of the tombs."
    scene s1l5 with dissolve  
    h "Mhm… or maybe, we wait for the others?"
    h "And maybe not go playing heroes-"
    scene s1l6 with dissolve  
    Mi "Olivia… this is a tomb."
    scene s1l7 with dissolve  
    mc "...She’s got a point."
    mc "Walking in blind is stupid."
    scene s1l8 with dissolve  
    h "See?! He agrees with me!"
    Mi "..."
    Mi "We’re going."
    h "Wha- hey, Mir!"
    play sounds1 stepmc
    scene s1l9 with dissolve  
    Mi "..."
    scene s1l10 with dissolve  
    play sounds1 stepmc
    h "Where the hell are you going?!"
    play sounds1 stepmc
    scene s1l11 with dissolve
    mc "(…Something’s off about her.)"
    mc "Miriel."
    mc "You still haven’t told us why we’re here."
    scene s1l13 with dissolve
    Mi "..." 
    scene s1l12 with dissolve
    mc "Let me put it simpler."
    mc "What exactly is in that tomb?"
    Mi "..."
    Mi "…Your wife."
    play sounds1 stepmc
    scene s1l14 with dissolve
    pause 1.1

    scene s1l15 with dissolve
    mc "...My wife?"
    scene s1l17 with dissolve
    Mi "I’ll explain inside."
    play sounds3 oldroom fadeout 3.2
    scene s1l18 with dissolve
    pause 1.1


    stop music fadeout 0.5
    stop sounds2 fadeout 0.5


    scene black with dissolve 
    pause 4.3

    play sound spaceshipinto fadein 5.5 loop volume 0.5
    play music1 gymnopedieno1 fadein 5.5
    play sounds1 stepmc
    scene s1tew13 with dissolve 
    pause 0.5
    mc "Clear."
    play sounds3 mmove 
    scene s1tew14 with dissolve 
    pause 1.1
    h "Ugh… this place gives me the creeps."
    h "And the smell… yeah, it stinks."
    scene s1tew15 with dissolve 
    mc "(…A statue?)"
    h "(whispering) Hey… look. He’s naked!"
    mc "Liv. Focus."
    
    play sounds1 stepmc
    scene s1tew16 with dissolve 
    h "..."
    h "Gladly, just say the word."
    h "You do have a plan, right?"
    play sounds3 mmove 
    scene s1tew17 with dissolve 
    mc "(whispering) Making it up as I go."
    h "(whispering) Promise me, if things go south, we’re out."
    mc "..."
    scene s1tew18 with dissolve 
    h "(whispering) [mc]."
    mc "(whispering) …Alright."
    scene s1tew19 with dissolve 
    pause 1.1 
    play sounds1 stepmc
    scene s1tew20 with dissolve 
    mc "Mir?"
    Mi "..."
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew21 with dissolve 
    Mi "You asked… whether others care…"
    Mi "about excavating tombs."
    mc "…About that."

    scene s1def55 with dreamyzoom
    show memoryframe with dissolve
    Fl "...Council banned..."

    play sounds1 stepmc
    scene s1tew22 with dissolve 
    mc "The Council. Who are they?"
    Mi "They make the laws concerning the tombs."
    scene s1tew23 with dissolve
    mc "And they banned excavation?"
    Mi "All unauthorized contact."

    scene s1rew178 with dreamyzoom
    show memoryframe with dissolve 
    mc "(She was being watched.)"

    scene s1tew23 with dissolve 
    pause 1.1
    scene s1tew24 with dissolve 
    mc "So you were watching her… because you were afraid."
    Mi "Everything related to her was under strict restriction."
    Mi "That’s how we kept her safe from them."
    scene s1tew25 with dissolve 
    mc "And she’s here?"
    Mi "Yes."
    mc "What about the second tea—"
    play sounds3 whoosh 
    scene s1tew26 with CropMove(time=0.2, mode='slideleft')  
    mc "…What are you doing?"
    h "Exploring!"
    mc "..."
    scene s1tew27 with dissolve 
    h "Hm? Something dripping?"
    scene s1tew28 with dissolve 
    h "..."
    scene s1tew29 with dissolve 
    h "Hey, old man… care to join me?"
    scene s1tew30 with dissolve 
    Mi "..."
    mc "Get down, Liv."
    mc "That’s not safe."
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew31 with dissolve 
    h "Neither is this whole place!"
    scene s1tew32 with dissolve 
    h "But seriously, I checked the room, there’s no one here."
    scene s1tew34
    a "..."
    scene s1tew32 with dissolve 
    pause 0.4
    play sounds3 whoosh 
    scene s1tew33 
    pause 0.8
    play sounds4 whoosh 
    scene s1tew35 
    Mi "..."
    mc "This isn’t the time to mess around."
    scene s1tew36 with dissolve 
    Mi "..."
    Mi "Move."
    Mi "(…Or was it?)"

    stop music1 fadeout 0.7
    scene black with dissolve 
    pause 4.1 

    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew37 with dissolve 
    pause 1.3
    scene s1tew38 with dissolve 
    mc "(That metallic taste again...)"
    mc "(…A lab?)"
    mc "(whispering) …What were you doing here, Lora…?"
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew39 with dissolve 
    mc "So… this is the tomb?"
    play music s45c9mcmemoryscene fadein 5.4
    scene s1tew40 with dissolve 
    pause 1.1
    scene s1tew41 with dissolve 
    mc "(…That glow?)"
    play sounds4 mutantheart loop
    play sounds heartbeat loop
    scene s1tew42 with dissolve 
    pause 0.8
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew43 with dissolve 
    h "Too quiet…"
    h "I don’t like this."
    mc "(whispering) What is that…?"
    mc "..."
    scene s1tew44 with dissolve 
    mc "Mir. Get over here."
    h "What did you find over there, old man? Your voice—"
    play sounds3 mmove 
    scene s1tew45 with dissolve 
    pause 1.2
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew46 with dissolve 
    mc "Tell me I’m wrong…"
    Mi "No… I see it too."
    scene s1tew48 with dissolve 
    mc "Blood… yeah?"
    Mi "Not blood."
    Mi "Energy."
    pause 1.1
    mc "Mir…"
    mc "What’s the real reason these tombs are banned?"
    Mi "..."
    Mi "…Because of the substance."
    scene s1tew47 with dissolve 
    mc "We’re leaving."
    mc "Too much doesn’t add up."
    Mi "…You noticed it too?"
    stop music fadeout 4.5
    scene s1tew49 with dissolve 
    pause 1.6
    play sounds4 whoosh 
    scene s1tew50 
    pause 0.8
    mc "..."
    mc "Mir, we’re moving. Now."
    Mi "…Yes."
    h "Wha— finally!"
    mc "Liv, stay sharp."
    stop sounds fadeout 0.5
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew41 with dissolve 
    pause 1.8 
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew39 with dissolve 
    Mi "[mc]… the door’s locked."
    h "WHAT?! ARE YOU KIDD—"
    play music1 season4act21 fadein 5.5
    scene s1tew51 with dissolve 
    mc "Liv. Quiet."
    mc "..."
    mc "…We’re being watched."
    play sounds3 mmove 
    scene s1tew52 with dissolve 
    h "(whispering) I told you… this was a bad idea…"
    mc "(whispering) Panicking won’t help."
    mc "Breathe. Stay with me."
    h "(whispering) I’m trying…"
    scene s1tew53 with dissolve 
    mc "(whispering) Mir. You good?"
    Mi "…I’m fine."
    mc "Good."
    scene s1tew54 with dissolve 
    mc "We move."
    mc "Stay close. No one splits."
    h "Wait, you want to go… in there? Are you insane?!"
    play sounds2 whoosh 
    scene s1tew55 
    h "(whispering) This place is practically screaming danger…"
    mc "You got a better way out?"
    h "(whispering) …no."
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew56 with dissolve 
    mc "(whispering) I know you’re scared. So am I."
    mc "(whispering) But we keep moving."
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew57 with dissolve 
    h "..."
    h "H-hey, wait… we’re seriously going in there?"
    play sounds3 mmove 
    scene s1tew58 with dissolve 
    pause 0.8
    scene s1tew59 with dissolve
    mc "Nothing’s happening to you while I’m here."
    scene s1tew62 with dissolve
    h "Wow… drop the heroic act, old man. It looks ridiculous."
    h "(…and yet… it does calm me down.)"
    h "(whispering) …okay."
    scene s1tew63 with dissolve
    pause 1.5
    scene s1tew64 with dissolve
    pause 0.7
    scene s1tew65 with dissolve
    pause 0.7
    play sounds3 mmove 
    scene s1tew66 with dissolve
    a "..."
    play sounds3 clothess  
    scene s1tew67 with dissolve
    pause 1.4
    scene s1tew68 with dissolve
    a "..."

    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew69 with dissolve
    pause 1.6
    play sounds3 mmove 
    scene s1tew73 with dissolve
    mc "(…Yeah. They’re herding us.)"

    scene black with dissolve 
    "A couple of minutes later."

    play sounds2 walkdirt volume 0.7
    play sounds heartbeat loop volume 0.5
    scene s1tew74 with dissolve
    h "This red stuff…"
    Mi "The substance."
    pause 0.7
    h "...that’s blood, right…?"
    play sounds2 walkdirt volume 0.7
    h "And why were you so damn eager to get here?"
    Mi "I’m… worried."
    h "Huh? You..."
    play sounds2 walkdirt volume 0.7
    scene s1tew75 with dissolve
    h "Hold on…"
    h "You mean Lora?"
    Mi "…Mhm."
    play sounds2 walkdirt volume 0.7
    play sounds3 mmove 
    stop music1 fadeout 3.3
    scene s1tew76 with dissolve
    h "...you’re telling me everything later."
    mc "..."
    mc "Hey."
    mc "You need to see this."
    h "What did you—"
    mc "Now!"
    b "..."
    h "Alright, I’m coming…"
    stop sounds fadeout 0.5
    play music astoriamain fadein 4.4
    scene s1tew77 with dissolve
    mc "(…This isn’t a tomb.)"
    mc "(Not even a graveyard…)"
    scene s1tew78 with dissolve
    mc "(…This is a crypt.)"
    h "..."
    h "Shit…"
    scene s1tew79 with dissolve
    mc "(…I can’t see the end of it.)"
    mc "(There are thousands…)"
    scene s1tew80 with dissolve
    mc "(Tens of thousands.)"
    h "Shit {w=0.9}shit {w=0.5}shit {w=0.3}SHIT!"
    h "WHAT THE DUCK IS THIS PLACE?!"
    scene s1tew79 with dissolve
    mc "Liv, calm down—"
    h "CALM DOWN?! HOW THE DUCK AM I SUPPOSED TO CALM—"
    mc "OLIVIA!"
    h "..."
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew82 with dissolve
    mc "I know."
    mc "I see it too."
    mc "But we keep it together. Stay sharp."
    h "...sorry."
    mc "..."
    play sounds3 mmove 
    scene s1tew83 with dissolve
    mc "You knew about this?"
    Mi "N-no… I…"
    Mi "No."
    mc "..."
    mc "…And you don’t know what this is?"
    Mi "…No."
    play sounds3 mmove 
    play sounds1 stepmc
    scene s1tew84 with dissolve
    mc "(…Then that’s worse.)"
    mc "(What does all this even mea—)"
    
    scene s1rew207 with dreamyzoom 
    show memoryframe with dissolve
    h "...found...wasn’t supposed to?"
    
    scene s1tew84 with dissolve
    mc "Miriel… where did soulless even come from?"
    Mi "They came from the tombs."
    
    scene s1tew48 with dreamyzoom 
    show memoryframe with dissolve
    mc "...real reason...tombs are banned?"
    Mi "…The substance."

    scene s1tew84 with dissolve
    mc "(…The substance…)"
    mc "(If that’s the reason…)"
    mc "(Then what the hell are soulless doing here…?)"

    scene s1rew262 with dissolve 
    show memoryframe
    Mi "they spread like a virus."

    scene s1tew85 with dissolve
    mc "(A virus…?)"
    pause 0.7
    mc "(No, wait.)"
    mc "(Who the hell would spread virus like that?)"
    mc "(No. That doesn’t fit.)"
    mc "(Too clean… too convenient.)"
    
    scene s1tew51 with dreamyzoom 
    show memoryframe with dissolve
    Mi "The door… it’s locked."
    scene s1tew73 with dreamyzoom
    show memoryframe with dissolve
    mc "(…They’re leading us.)"


    scene s1tew86 with dissolve
    mc "We didn’t find this place."
    mc "We were brought here."
    play sounds2 mmove 
    scene s1tew87 with dissolve
    mc "..."
    mc "…We’re not alone."
    stop music 
    play sounds1 spacepick
    pause 0.7
    
    play sounds3 industryon
    play sounds4 powersup
    scene s1tew89 with dissolve
    H "Power source activated. Intruders detected. All restrictions lifted."
    pause 1.1
    play music battle2 fadein 5.5
    scene s1tew90 with dissolve
    mc "MOVE!"
    Mi "The door… it’s locked."
    scene s1tew91 with dissolve
    pause 1.1
    scene s1tew92 with dissolve
    pause 0.8
    play sound rs1 volume 0.3
    scene s1tew93 
    mc "(Drop dead!)"
    scene s1tew94 
    pause 1.1

    
    scene s1tew96 
    h "WHAT DO WE DO?!"
    mc "Fight!"
    scene s1tew97 with dissolve
    pause 0.7
    play sound rs1 loop volume 0.3
    play sounds3 scar1 loop volume 0.2
    scene s1tew98 with vpunch 
    pause 0.9
    scene s1tew99 with dissolve
    mc "(We’re not dying here. Not like this!)"
    scene s1tew100 with dissolve
    mc "Liv, watch the rear!"
    play sounds4 whoosh 
    scene s1tew101 
    pause 1.1
    play sounds1 swordswing
    play sounds2 hdshot 
    scene s1tew102 with vpunch
    pause 1.1
    play sounds4 whoosh 
    play sounds2 swordswing
    scene s1tew103 
    pause 1.1
    scene s1tew104 with dissolve
    h "ABOVE US!"
    play sounds4 whoosh 
    scene s1tew105 
    pause 1.1
    stop sound 
    play sounds2 clench 
    scene s1tew106 
    pause 1.1
    play sounds rockfall
    play sounds2 hdshot 
    scene s1tew107 with vpunch
    pause 1.1
    scene s1tew108 with dissolve
    pause 1.1
    play sounds2 hdshot 
    scene s1tew109 with vpunch
    pause 1.1
    scene s1tew110 with dissolve
    h "They’re coming from everywhere!"
    mc "Keep firing!"
    play sound rs1 loop volume 0.3
    scene s1tew104 with dissolve
    mc "We’re getting out of here, all of us!"
    play sounds1 scifidooropen2
    play sounds3 grouprun volume 0.3
    scene s1tew112 with dissolve
    pause 0.8 
    scene s1tew113 with dissolve
    g "...There they are!"
    play sounds1 riflesound1 volume 0.1
    scene s1tew111 with dissolve
    o "Aim carefully!"
    play sounds4 whoosh 
    play sounds2 swordswing
    scene s1tew103 
    Mi "[mc]— there!"
    scene s1tew114 with dissolve
    mc "Liv, to Ostorius now!"
    scene s1tew115 with dissolve
    pause 1.1
    play sounds4 zombiegroup loop volume 0.4
    scene s1tew116 with dissolve
    mc "(…Too many…)"
    mc "(Come on… keep it together…)"
    o "Don’t play hero!"
    scene s1tew117 with dissolve
    pause 0.5
    scene s1tew119 with dissolve
    pause 0.5
    scene s1tew120 with dissolve
    mc "(Almost there…!)"
    play sounds4 whoosh 
    play sounds2 swordswing
    scene s1tew122 
    pause 0.8
    play sounds4 whoosh 
    scene s1tew123 
    mc "(Wha-?!)"
    scene s1tew124 with dissolve
    pause 1.1
    scene s1tew125 with dissolve
    o "That’s it — everyone out!"
    
    stop sounds2 
    stop sounds3 
    stop sound 
    stop sounds
    stop sounds4 
    stop sounds1
    scene black with dissolve
    pause 1.5
    

    scene s1l81 with dissolve
    o "RUN! DON’T LOOK BACK!"
    scene s1l82 with dissolve
    pause 0.5
    scene s1l83 with dissolve
    pause 0.5
    scene s1l84 with dissolve
    pause 0.7
    scene s1l85 with dissolve
    o "Detonate it! NOW!"
    stop music
    stop music1
    stop sounds4
    play sounds3 c4
    scene s1l86 with dissolve
    pause 0.5
    play sounds2 c4boom volume 0.4
    play sound towers loop fadein 3.5 volume 0.4
    scene s1l87 with dissolve
    pause 1.5
    scene s1l88 with dissolve
    mc "..."
    
    scene s1l90 with dissolve
    o "You holding up?"
    scene s1l89 with dissolve
    mc "Been worse."
    mc "How’d you find us?"
    scene s1l90 with dissolve
    o "Not us. The Inquisitor moved first."
    o "We followed her… and found you."
    mc "..."
    scene s1l89 with dissolve
    mc "Good to see you made it."
    scene s1l90 with dissolve
    o "Likewise."
    scene s1l89 with dissolve
    mc "One question."
    mc "Why split up?"
    play music ending2
    scene s1l90 with dissolve
    o "..."
    o "Your implants could’ve caused problems."
    scene s1l91 with dissolve
    h "Okay, can someone explain what the hell just happened?"
    scene s1l93 with dissolve
    mc "..."
    mc "That wasn’t random."
    mc "We were being tested."
    mc "Only explanation that fits."
    scene s1l92 with dissolve
    h "What do you mean?"
    scene s1l94 with dissolve
    mc "You didn’t feel it?"
    mc "Like we were being watched the whole time."
    mc "Those things… they were tracking us."
    play sounds1 whoosh
    
    
    scene s1l98 with dissolve
    o "You sure?"
    o "Soulless are primitive. Tracking us?"
    scene s1l99 with dissolve
    mc "No… not them."
    mc "Something else."
    o "Even then… that’s impossible."


    scene s1l100 with dissolve
    mc "I saw it."
    mc "With my own eyes."
    mc "That thing triggered the tomb."
    scene s1l101 with dissolve
    Mi "..."
    Mi "I… I think I found something."
    Mi "Here—"
    mc "What is it?"
    Mi "An Ark marker."
    h "A tracker?"
    Mi "A key."
    Mi "Markers activate parts of the Ark."
    mc "And this one?"
    Mi "It isn't opening anything."
    Mi "It's calling someone."
    mc "Who?"
    Mi "I don't know."

    "She presses the small object into his hand."

    mc "(Warm.)"
    mc "(Like it was waiting for me.)"
    scene s1l102 with dissolve
    "Noticing the panic on Miriel's face."
    mc "Miriel?"
    scene s1l103 with dissolve
    Mi "no… {w=1.2} No {w=0.8} No {w=0.4} NO {w=0.1} NO!"
    o "Miriel? Report."
    scene s1l104 with dissolve
    Mi "They’re trying to activate the gate!"

    stop music 
    stop sound
    stop sounds
    stop sounds2
    stop sounds3
    stop sounds4
    play sounds1 hit1 

    jump story03

    # stop music 
    # stop sound
    # stop sounds
    # stop sounds2
    # stop sounds3
    # stop sounds4
    # play sounds1 hit1 

    # scene black with dissolve
    # pause 3.0


    # $ renpy.music.set_volume(0.4, channel='movie_dp')

    # image ending2 = Movie(channel="movie_dp", loop = False, play="video/ending2.webm")
    # show ending2 with dissolve
    # pause 67.0

    # scene black with dissolve
    # n "Don't forget to leave a review with your opinion on the game, it would be much appreciated!"
    # n "Also if you liked my game, and wanted to support me, than welcome to my patreon or subscribestar. (Feels shy to say that tbh)"
    # n "And yeah... Please save game here. Lovely :D"
    # scene black with dissolve
    # pause 3.0







    

            

    
   


return


