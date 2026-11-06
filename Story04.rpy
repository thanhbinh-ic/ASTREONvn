
define persistent.olivia_Third_scene = False
define harem_end = 0

# Флора
label story05:
    stop music fadeout 0.6
    $ persistent.chapter_act4 = True
    scene black with dissolve
    pause 5.2
    show act4s1 with dissolve
    pause 1.5
    show act4s1_1 with dissolve
    pause 2.1
    scene black with dissolve
    pause 1.2
    play music season4act1 fadein 3.4
    show act4_s1 with dissolve 
    pause 1.5
    scene black with dissolve
    pause 1.0
    "Two hours until the operation begins."
    play sounds industryroom loop volume 0.3
    play sounds3 bodytap 
    show s4_aaa13 with dissolve
    k "Brings back memories, huh, sis?"
    a "Hmpf..."
    show s4_aaa15 with dissolve
    Fl "I know I have no right to ask you for this."
    Fl "This mission is practically suicide, and-"
    show s4_aaa16 with dissolve
    mc "Flora, that’s enough."
    mc "Every one of us made our choice long before we walked into this room."
    h "Saving a planet… yeah, that’s definitely a first for us, right, [mc]?"
    mc "Yeah."

    play sounds4 factoryambience loop fadein 3.2 volume 0.5
    play sounds3 alarm loop volume 0.2
    scene black with dissolve 
    Fl "All right. Then we begin."
    show s4_aaa17 with dissolve
    Fl "The Peacekeepers will act as the decoys. They’ll draw the main strike."
    Fl "The Syndicate teams will evacuate survivors to the lower city."
    play sounds2 rungroup2
    show s4_aaa2 with dissolve
    Fl "My father’s special units will move into the gas chambers with cryo-units-"
    Fl "to freeze the enemy all at once."
    a "Not confident in the plan?"
    Fl "..."
    stop sounds3 fadeout 0.4
    stop sounds4 fadeout 0.4
    show s4_aaa14 with dissolve
    Mi "What is our role?"
    Fl "Meanwhile, your squad will head for the tower."
    play sounds4 factoryambience loop fadein 3.2 volume 0.5
    show s4_aaa18 with dissolve
    Fl "If what we learned is true, if they really plan to turn us into an energy source..."
    Fl "then whatever it costs, you have to stop them."
    show s4_aaa3 with dissolve
    mc "How do we get into the tower?"
    Fl "By air."
    a "The main tower, an impregnable fortress."
    a "Any unauthorized ship will be shot down by the internal AA system."
    Fl "You’ll go in through the lower cargo routes-"
    a "No chance." 
    a "Too slow. Too dangerous."
    pause 1.2  
    Fl "Arcana’s unit will cover you with fire support. We’ll disable part of their AA."
    show s4_aaa4 with dissolve
    Fl "And… Ember has offered her personal cruiser." 
    Fl "With it, you’ll break through. Any questions?"
    a "..."
    play sounds2 scifidooropen2 
    show s4_aaa5 with dissolve
    Fl "Good. Then one last thing."
    Fl "Your most important mission."
    pause 1.2
    Fl "Come back alive."
    Fl "All of you."
    show s4_aaa6 with dissolve
    h "We’ll do everything we can, but-"
    Mi "..."
    mc "Yeah."
    k "Pff. What happened to all that fire? Come on, this is where the fun starts."
    h "Crazy…"
    show s4_aaa7 with dissolve
    k "If you’re that scared, you can hide behind my back. Actually, nah. You’d just keep whining."
    h "Huh?"
    k "In the end… if not us, then who?"
    play sounds3 bodytap 
    show s4_aaa8 with dissolve
    mc "Everyone here has something they’re trying to protect."
    mc "We can’t let them down."
    L "Yes. If they’re putting in that much effort… then we should, too."
    scene s4_aaa9 with dissolve
    Fl "(They don’t owe us this. If anything, it’s we who should be...)"
    Fl "(And yet…)"
    scene s4_a91 with dissolve
    Fl "(No. Not now. Focus. You can repay them later, when this is over.)"
    Fl "(Right now we need to do everything we possibly can… and we succeed.)"
    scene s4_a81 with dissolve
    Fl "(whisper) Yes… we will succeed. All of us."

    show s4_aaa10 with dissolve
    g "Good luck."
    play sounds3 clothess 
    show s4_aaa11 with dissolve
    pause 0.7
    play sounds2 clench 
    scene s4_aaa12 with dissolve
    mc "Likewise."
    g "It’s been an honor working with you." 
    stop sounds4 fadeout 2.2
    scene s4_a80 with dissolve 
    show act4_s4 
    "Ten minutes until the operation begins."
    g "Miss Flora."
    Fl "Y-yeah… it’s time."
     
    
    scene s4_a94 with dissolve
    Fl "Attention, everyone."
    Fl "The western front is moving. Your task is to cover the evacuation, hold the line, and execute the plan."
    pause 0.3
    Fl "Mistakes are unacceptable. You know your roles, act fast and act precise."
    stop music fadeout 4.3
    Fl "The fate of many is at stake. We can’t afford hesitation."
    scene black with dissolve 
    Fl "Begin the operation."
    scene black with dissolve 
    pause 3.2

    play music season4act2 fadein 2.2
    "One hour into the operation."
    pause 3.2
    play sounds rs1 volume 0.3 loop 
    play sounds3 inqusitionradio loop volume 0.6
    show s4_aa18 
    aa "Sixty-Three to command… We’re not holding! There’s too many of them!"
    stop sounds 
    scene black 
    a "Command to Sixty-Three. Status?!"
    show s4_aa19 
    play sounds rs1 volume 0.3 loop 
    play sounds4 zombiegroup loop 
    aaa "Mission failed, enemy numbers are overwhelming! Requesting evac-!"
    stop sounds
    stop sounds4 
    scene black 
    a "Sixty-Three? …Sixty-Three!!"
    pause 0.5
    a "Connection to Squad Sixty-Three is lost."
    show s4_aa20 with dissolve
    play sounds1 nve volume 0.32 
    pause 0.2 
    aaaa "Iron Dome to command. We’ve spotted survivors. Orders?"
    a "Sending transport to the marked coordinates."
    a "Continue your route."
    stop sounds3
    play sounds2 spacepick2 fadein 0.2
    show s4_aa21 with dissolve
    a "Miss Flora, western sector made contact with the enemy. Heavy resistance."
    a "They’re calling for backup, numbers are too high."
    play sounds2 ha
    show s4_aa22 with dissolve 
    Fl "Send a few squads from the east. They need to hold until backup arrives."
    Fl "(I thought I was ready. I really did. I thought it would be like the simulations.)"
    Fl "(I thought Mom was wrong, but-)"
    play sounds2 ha
    show s4_aa23 with dissolve 
    aa "Thirty-Eighth reports AA guns northwest!"
    play sounds2 ha
    scene s4_aa22 with dissolve
    Fl "Arcana platoon, transmitting the coordinates."
    aaa "Copy. Working."

    
    image s4_video_1 = Movie(channel="movie_dp", loop = False, play="video/s4/s4_video_1.webm")
    show s4_video_1 with dissolve
    $ renpy.pause(4.2, hard=True)

    
    scene s4_aa21 with dissolve
    aaa "Target neutralized. Runway is clear for the bird."
    Fl "Good work."
    Fl "(The screaming. The pain. All of it…)"
    Fl "(I’m sorry, Dad. I can’t, I can’t take this.)"
    Fl "(whispering) I want to run."
    play sounds2 ha
    scene s4_aa22 with dissolve
    Fl "Any updates from the other sectors? Did anyone respond to our signal?"
    a "Nothing, Miss Flora. Might be something else jamming them."
    play sounds2 spacepick2 fadein 0.2
    show s4_aa24 with dissolve 
    Fl "(This is bad. We’re short on people, short on supplies. They’re holding on morale alone… and that runs out.)"
    Fl "(Everything’s against us… Hope-)"
    pause 0.5
    Fl "..."
    play sounds2 spacepick2 fadein 0.2
    show s4_aa25 with dissolve 
    Fl "(whispering) Focus. We still have a chance."
    Fl "([mc], please… don’t let me down.)"
    stop music fadeout 3.2
    scene black with dissolve 
    pause 5.4

# Сцена первая - разговор по душам.




    play music season4act3 fadein 5.4
    play sounds industryroom loop volume 0.5
    show s4_a1 with dissolve    
    show act4_s3 with dissolve 
    mc "(As long as I can remember, I wanted a quiet, peaceful life.)"
    mc "(When I came back from the army, I really thought I could make it real.)"
    mc "(A loving wife. A good family. A big house. Maybe a dog... the American dream done.)"
    show s4_a3 with dissolve 
    mc "(But now I’m here. At the ass end of the galaxy. Why?)"
    mc "(Because of Lora? ...Or because of the memories of her?)"
    mc "(Maybe because of Norman? So his sacrifice wouldn’t be for nothing?)"
    mc "(Or because of my own damn ego?)"
    show s4_a2 with dissolve 
    mc "Olivia?"
    show s4_a12 with dissolve 
    h "What do you want?"
    show s4_a13 with dissolve 
    mc "How do you manage... not to lose your mind in all this?"
    pause 0.8 
    scene s4_a12 with dissolve 
    h "Hold on, what makes you think that?"
    mc "I thought… you were the only one holding it together."
    mc "Acting like nothing’s worth worrying abou-"
    h "Okay, stop right there. That was kinda rude."
    pause 0.5
    h "Out of all the things you could’ve said… you went with THAT? Seriously?"
    h "You really think you’re the only one having a hard time here?"
    h "Come on, don’t play the victim."
    h "(What the hell are you doing, Olivia? Get a grip. He’s the guy who literally saved your life.)"
    h "Just pull yourself toge-"
    play sounds3 mmove 
    show s4_a10 with dissolve 
    h "(Still… that stung.)"
    h "(I’m trying so damn hard to keep it together, doing everything I can, and that`s what I get back…?)"
    h "(He didn’t even mean it like that, so why am I getting pissed…?)"
    scene s4_a3 with dissolve 
    pause 0.5
    scene s4_a1 with dissolve 
    mc "(She’s… right, in a way.)" 
    mc "(For some reason, I thought I was the only one struggling, blind to everyone else’s feelings.)"
    mc "(And the worst part… I took their help for granted.)"
    scene s4_a2 with dissolve 
    mc "You’re right." 
    mc "I really did start thinking I was the only one suffering here."
    h "No, that’s not what I meant-"
    scene s4_a2 with dissolve 
    mc "I act like a damn superhero." 
    mc "Charging straight through, not thinking about consequences… not thinking about the people close to me."
    h "..."
    mc "And the funniest part? From the very beginning…" 
    mc "I never even thank you." 
    mc "Not once."
    scene s4_a1 with dissolve 
    h "Hey, hey! Cut the dramatic speech, will you? Did your age finally catch up with you or what?"
    scene s4_a2 with dissolve 
    mc "I don’t know, Olivia. I really don’t. But… thank you."
    mc "From the bottom of my heart. Thank you for always being there. For having my back…"
    scene s4_a14 with dissolve 
    h "..."
    scene s4_a15 with dissolve 
    pause 0.6
    show s4_a16 with dissolve 
    h "{b}Doesn’t matter what’s happening around you, what matters is how YOU deal with it.{/b} Something like that. Take a page outta Anya’s book."
    show s4_a17 with dissolve 
    h "(She’s the one who kept us going more than anyone…)"
    mc "{b}Everything depends on how you choose to look at it.{/b}" 
    mc "You know… there’s something real in that."
    h "One thing she was always good at, talking sense into people. I’ll give her that."
    pause 0.5
    mc "Yeah..."
    mc "I wonder how she’s doing…"
    show s4_a18 with dissolve 
    h "I… try not to think about it. But I’m sure she’s doing great. No doubt in my mind!"
    show s4_a20 with dissolve 
    mc "That’s a mindset."
    play sounds3 mmove 
    show s4_a21 with dissolve 
    h "But you know… sometimes…"
    h "I’m scared. Thinking we might not make it back. That Anya could end up al-"
    mc "At least she’s got Alexandro and his damn “crocodiles.” They won’t leave Anya to rot, that’s for sure."
    scene s4_a23 with dissolve 
    pause 1.3
    scene s4_a21 with dissolve 
    h "Yeah… you’re right. {w}Right now, we need to focus on staying alive."
    h "And still, with all this chaos, I can’t wrap my head around one thing: out of all the people out there, why us?"
    show s4_a22 with dissolve 
    mc "I don’t know. I thought if I’d find Lora… I’d finally get answers. At least a piece of the truth."
    mc "In the end, nothing solid. Nothing real."
    show s4_a24 with dissolve 
    mc "They brought me back to life. On one hand… I’m grateful. On the other, this life isn’t any better than the last one."
    mc "In some ways… it’s worse."
    mc "Sleep is a luxury. Every day could be my last. My body aches nonstop-"
    mc "But the real question is… what the hell are we fighting for?"
    show s4_a25 with dissolve 
    "At the same time, Miriel was reading a book, while quietly eavesdropping on their conversation."
    "Deciding to stay silent, she went on reading… until her eyes caught a line."
    "{b}It’s damn hard to talk calmly and kindly about pain…"
    stop music fadeout 3.2
    play music1 season4act12 fadein 3.2
    Mi "({b}…until you’re free from her.{/b})"
    Mi "(Whispering) Free..."
    pause 0.5
    Mi "(He proved his worth… he did so much… and all he got was pain in return.)"
    show s4_a26 with dissolve 
    Mi "(whispering) Is this really what you taught me, Teacher…?"
    scene s4_a25 with dissolve
    Mi "(All my life, I followed your plans. And even now… I want to trust you, but-)"
    play sounds2 closebook
    show s4_a27 with dissolve 
    Mi "(No. This can’t keep going. They’ve proven enough. They deserve to know.)"
    h "Mir? Something wrong? You look way too serious."
    play sounds3 deepbreath1
    show s4_a28 with dissolve 
    Mi "(Even if just a part… I have to choose for myself.)"
    show s4_a29 with dissolve 
    Mi "[mc]?"
    mc "Hmm?"
    Mi "When we were on the Ark… you touched a certain sphere." 
    Mi "After that, you passed out. Do you remember?"
    show s4_a30 with dissolve 
    mc "(Too sudden. Why is she bringing up the Ark now?)"
    scene s0q158 with dreamyzoom
    mc "(Sphere?)"
    mc "Yeah. I remember. Not everything, but enough."
    Mi "When you left the team to look for the keycard, you wandered into the technical sector."
    scene s0q152 with dreamyzoom
    mc "How do you… Yeah. I remember something like that."
    mc "(The feelings I had back then… those memories…)"
    scene s0q154 with dreamyzoom
    mc "(Memories?)"
    mc "(Wait… Could it be… the implants are back to normal?)"
    show s4_a34 with linearblur
    h "Hold on, hold on, what are you two talking about? I was there too-"
    show s4_a46 with dissolve 
    Mi "No. Not that place. Another one. Where the experiments were actually conducted."
    show s4_a45 with dissolve 
    mc "Experiments again? Because of this “immortality” crap?"
    show s4_a47 with dissolve 
    Mi "Yes."
    Mi "What they were experimenting on there… is the reason you suddenly became so important to everyone."
    scene s3dd7 with dreamyzoom
    mc "(That masked guy… he said something like this. Said I was connected to this? No way this is just about that sphere…)"
    mc "(The Abyss… Astoria’s younger “sister”… some other force with its own agenda…)"
    mc "(And somehow I’m stuck in the middle of this mess.)"
    play sounds2 whoosh
    scene s4_a47 with CropMove(time=0.1, mode='slidedown')
    h "Okay, nope. I don’t like where this is going."
    h "What’s so damn special about this… sphere, or whatever it is, that everyone suddenly wants it?"
    Mi "That sphere was connected to the Gate."
    Mi "And after you touched it, the Gate started reacting to you."
    h "What? That one?"
    show s4_a38 with dissolve 
    mc "(Think, [mc]. Think. I'm connected, but to what?)"
    mc "(Ember… back then, in her room… she said they made it back to Earth through a gate. Is it inside the tower?)" 
    show s4_a48 with dissolve 
    h "(And he’s spacing out again… whatever. Let him. We’ll give him a few minutes.)"
    scene s4_a32 with dissolve 
    mc "(I’m connected to the Gate?)"
    mc "(whispering) No. That’s not it. Doesn’t add up."
    mc "(The words of the white mask… the Abyss… a gate to the Abyss?)"
    show s4_a39 with dissolve 
    mc "Can I actually get into the Abyss… somehow?"
    show s4_a38 with dissolve 
    Mi "Yes."
    show s4_a42 with dissolve 
    h "I’m losing the plot here, what are we talking about? The Abyss? Experiments? All that weird crap?"
    show s4_a41 with dissolve 
    Mi "You and I… we’ve already spent time studying this."
    show s4_a42 with dissolve 
    h "You only mentioned the Abyss, like, twice! That’s it!" 
    h "And now I’m suddenly hearing that-"
    show s4_a43 with dissolve 
    h "(No, no, calm down. She’s the first, maybe the only one, who actually told you the truth about what’s going on.)" 
    h "(If you snap at her now… yeah, you’d look like a complete idiot.)"
    show s4_a42 with dissolve 
    h "Alright. Fine."
    h "So we’re going to this tower of yours… not to save the planet?" 
    show s4_a46 with dissolve 
    Mi "We’ll prevent the gate from opening. We’ll save the planet."
    scene s4_a45 with dissolve 
    mc "What happens after that?"
    scene s4_a44 with dissolve 
    Mi "I’ll take you back home."
    scene s4_a43 with dissolve 
    mc "(Home… but what about Lora… No. Don’t go there.)" 
    mc "(Lora seems like she belongs here now anyway.)"
    mc "(And yet… I can’t just leave her like this… Or can I?)"
    scene s4_a45 with dissolve 
    mc "What do you think?"
    h "I’m in. This place is… fine, I guess, but I don’t wanna have anything to do with it anymore. No offense, Mir."
    scene s4_a38 with dissolve 
    Mi "I understand."
    Mi "(whispering) If it were my choice… I would’ve left this place long ago."
    pause 0.6
    mc "..."
    scene s4_a31 with dissolve 
    mc "Then come with us."
    Mi "I…"
    pause 0.6
    mc "I’m not forcing you. But I’m serious, think about it."
    scene s4_a42 with dissolve 
    h "Totally agree."
    scene s4_a41 with dissolve 
    Mi "I’ll think about it."
    stop music1 fadeout 4.3
    pause 0.6
    scene s4_a43 with dissolve 
    Mi "..."
    mc "(They’re nervous. Both of them.)" 
    mc "(And I’m no exception… We need a break.)"
    play music season4act4 fadein 3.3
    scene s4_a20 with dissolve
    mc "Olivia?"
    h "Yeah?" 
    mc "Remember when you used to run around the city, dragging people into that bar? Acting like it was the end of the world."
    scene s4_aa33 with dreamyzoom
    h "That bar had a name! But yeah, I remember. And honestly…"
    h "I'd still think that way! That time was pure hell!"
    play sounds2 whoosh
    scene s4_a17 with CropMove(time=0.1, mode='slidedown')
    mc "Yeah? I thought you hated this little “adventure” of ours more than anything else."
    scene s4_a15 with dissolve 
    pause 0.5
    scene s4_a16 with dissolve 
    h "Let’s just say this little trip has its perks." 
    scene s4_aa34 with dreamyzoom
    h "(Running around the city sure as hell didn’t.)"
    h "Help!"
    scene s4_a16 with CropMove(time=0.1, mode='slidedown')
    h "I just wanna relax, [mc]… run a hot bath… and stay in it for an hour. Or two." 
    h "Maybe even with someone who owes me…"
    scene s4_a20 with dissolve 
    mc "Hm… I thought I cleared all my debts."
    scene s4_a18 with dissolve 
    h "And what makes you think it’s gonna be YOU? You’ve got Lora, remember?" 
    mc "..."
    play sounds3 bodytap
    scene s4_a21 with dissolve 
    h "Mm-hm. Honestly, I don’t mind either way. But do me a favor and sort things out between you two." 
    h "We’re adults, right? So why act like a couple of kids?"
    scene s4_a23 with dissolve 
    Mi "I agree."
    scene s4_a42 with dissolve 
    h "Right?! For a second I thought it was just me."
    scene s4_a41 with dissolve 
    Mi "One of you is trying to protect what once was. The other is desperate to bring it back." 
    Mi "But neither of you wants to look the truth in the eye." 
    Mi "You’re living in the present, not the past." 
    Mi "So maybe you should think about your future… instead of clinging to nostalgia."
    scene s4_a38 with dissolve 
    h "That’s how it is."
    scene s4_a39 with dissolve 
    mc "Present… {w}Miriel? Tell me, why are you helping us?"
    h "Hey! Don’t change the subject!"
    scene s4_a38 with dissolve 
    mc "(You care about the elves… yet you follow us instead of protecting them.)"
    mc "(So why? You’re terrified of opening up. That moment on the ship… and before that…)"
    scene s4_a49 with dissolve 
    pause 0.8
    scene s4_a50 with dissolve 
    Mi "(What am I supposed to do? Tell the truth?)"
    Mi "(But would they believe it? If I were in their place… I wouldn’t.)" 
    scene s4_a51 with dissolve 
    h "Okay, nope. I don’t like this silence. At all."
    Mi "(Fine.)"
    scene s4_a52 with dissolve 
    Mi "No reason. I just want all of this to end. As soon as possible."
    Mi "(You’ve spent so much time with them… and still-)" 
    scene s4_a38 with dissolve 
    mc "(Her eyes keep moving. Nervous. Truth… or a lie?)"
    Mi "..."
    scene s4_a39 with dissolve 
    mc "That’s enough. Thank you, Miriel."
    scene s4_a53 with dissolve 
    Mi "(What…?)"
    mc "(Truth or lie, she’s helped us more than anyone here.)"
    mc "(At least she’s not hiding in the corner anymore. She takes part now.)"
    mc "(That’s progress. Isn’t it?)"
    scene s4_a54 with dissolve 
    Mi "You’re not going to… ask?"
    mc "Would that really change anything? I can already see enough in your eyes."
    Mi "I..."
    show s4_a35 with dissolve 
    h "Stop it, [mc], you’re scaring her. Don’t mind him, Mir. He means well. Mostly."
    mc "{b}Mostly{/b}? I’m the definition of calm."
    h "Oh really? You jumped on poor Mir like you were interrogating her, and now you’re acting all wise and enlightened!"
    show s4_a36 with dissolve 
    Mi "(What is this feeling in my chest? It’s… warm.)"
    mc "Did you notice? Your face got softer. More relaxed." 
    show s4_a37 with dissolve 
    h "Actually… yeah. I kinda relaxed there for a moment…"
    mc "Glad to hear it."
    Mi "By the way… Kalestra was looking for you."
    
    $ persistent.chapter_act4_scene += 1

#Сцена первая - сторона Лоры.

label story05_1:

    stop music fadeout 3.2
    scene black with dissolve 
    pause 3.2

    
    play music season4act5 fadein 5.4
    show s4_a55 with dissolve 
    L "(Maybe… maybe it’s not too late to turn back, to stay with them just a little longer?)"
    L "(No. If we’re going to move even a single step forward, it has to be now.)"
    L "(Sigh) It hurts…"
    show s4_a57 with dissolve 
    k "Lor- Len- whatever. One eye or two, you’ll manage."
    k "Tell me. What did mistress say?"
    L "(Why would she ask that all of a sudden?)"
    show s4_a56 with dissolve 
    L "You already have the information. Why ask?"
    scene s4_a57 with dissolve 
    pause 0.6
    show s4_a58 with dissolve 
    k "I’m curious how different our goals really are."
    pause 0.3
    k "I’ve got this feeling… that someone here isn’t being entirely honest with me."
    k "And I really don’t like that."
    show s4_a61 with dissolve 
    a "Kalestra. Stop."
    show s4_a62 with dissolve 
    k "(Stop? Hm… Do I want to? Nah.)"
    show s4_a60 with dissolve 
    k "(I was wondering why, out of the whole group, only you sisters were sent. Together with her.)"
    k "(You’re a shooter, that makes sense. But a scientist? That’s a different conversation.)" 
    k "Enough with the ‘Kalestra this, Kalestra that’. Time-out, sweetheart. It’s honesty time."
    show s4_a63 with dissolve 
    k "So keep quiet, little sister. The grown women are talking."
    k "Now, you. Are you going to talk, or not?"
    show s4_a64 with dissolve 
    L "(What is she doing? …No. There’s no point in answering her.)"
    k "Decided to play cat and mouse? Oh, what a pity."
    k "Such a shame you won’t get to see your husband’s face when he learns about you."
    k "Oh, I {b}wonder{/b} how he’ll react when he finds out his wife isn’t quite who she claims to be."
    L "(“Not who I claim to be”? What do you even know about me?)"
    scene s4_a62 with dissolve 
    L "(I don’t see her stepping in… am I really on my own here?)"
    a "..."
    L "(So be it. Looks like I’ll have to deal with her myself.)"
    show s4_a65 with dissolve 
    L "Fine. I agree. What is it you want to hear?"
    play sounds3 mmove 
    show s4_a66 with dissolve 
    k "First. How did you find us?"
    k "Your dear husband might buy that story, but I won’t."
    L "(Her tone… I don’t like it. “Buy it”? Go to hell.)"
    show s4_a67 with dissolve 
    k "(whispering) You know… for once, I actually enjoy your company."
    k "(whispering) And you have no idea how delightful it is to watch your face when I talk about him…"
    show s4_a68 with dissolve
    L "(Endure it. Endure it… She’s provoking you. You can’t break.)"
    k "Well? I’m waiting."
    show s4_a70 with dissolve
    L "Yong. Yong sent out a distress signal. We were the closest. That’s all."
    show s4_a69 with dissolve
    L "(So she can’t read minds after all? Or there are conditions?)"
    L "(Either way… I’ll stick to the truth. Until it starts to smell like fire.)"
    k "Hmmm...."
    play sounds3 mmove 
    show s4_a71 with dissolve
    k "(Something doesn’t quite line up with the truth.)"
    k "(Yes, it’s his duty, but something tells me there’s more.)"
    k "Second! What’s your objective?"
    L "(My husband’s safety.)"
    L "Save the planet?"
    show s4_a72 with dissolve
    pause 0.5
    show s4_a73 with dissolve
    k "Ah, right, details. I always forget those."
    k "So tell me… what exactly is inside that tower?"
    show s4_a74 with dissolve
    a "I don’t recall you having clearance for that information."
    show s4_a75 with dissolve
    k "And what’s the problem? I’m curious."
    k "Or are {b}you{/b} against it?"
    L "(She doesn’t know? Nonsense. She’s playing with us. She knows perfectly well.)"
    L "What’s the point of this performance?"
    play sounds3 mmove 
    show s4_a77 with dissolve
    k "Out of boredom, I suppose? Time’s ticking. Tick-tock. Tick-"
    show s4_a78 with dissolve
    L "(She’s starting to get on my nerves. Really on my nerves…)"
    L "A mechanism. One that can move anything… anywhere. For a price."
    scene s4_a77 with dissolve
    k "Ohhh, so that’s why there are so many corpses."
    k "I see. I see."
    k "(Someone’s trying to bring someone back.)"
    k "So. What exactly are they planning to move, and where? I smell something big."
    show s4_aa1 with dissolve
    L "Your mistress is plan-"
    a "She might let something slip."
    show s4_aa2 with dissolve
    k "No, no, go on. Keep talking. What is mistress planning?"
    show s4_aa3 with dissolve
    L "..."
    k "(Oh? Now you’ve decided to play the silent game?)"
    play sounds3 mmove 
    show s4_aa4 with dissolve
    k "I see. Well then, where’s [mc]? Time for him to-"
    show s4_aa5 with dissolve
    L "Wait!"
    L "Fine. I agree."
    L "Bring her sister back. That’s it. No more questions. And you keep your mouth shut."
    play sounds2 bodytap 
    show s4_aa6 with dissolve
    k "Third!"
    show s4_aa7 with dissolve
    L "No. I said everythi-"
    show s4_aa9 with dissolve
    k "Can I sleep with your husband?"
    stop music fadeout 3.2
    L "..."
    a "..."
    play music1 season4act14 fadein 3.1
    show s4_aa10 with dissolve
    L "Are you serious?"
    play sounds3 mmove 
    show s4_aa11 with dissolve
    k "Well? What do you say?"
    show s4_aa13 with dissolve
    L "You’re insane."
    show s4_aa14 with dissolve
    k "Thank you!"
    k "(whispering) And now…"
    k "(whispering) Be a good girl, and no one finds out. Deal?"
    L "(Go to hell.)"
    L "..."
    show s4_a79 with dissolve
    k "I’ll take that as a yes."
    k "And don’t worry, I’ll keep my mouth shut."
    k "For now. Cheers."
    show s4_aa15 with dissolve
    L "(She’s completely unhinged. And the worst part is… I can’t do anything about it.)"
    a "Was that really your smartest decision."
    show s4_aa16 with dissolve
    L "You could’ve stepped in, if you disliked that idea so much."
    a "In her current state, she’s unpredictable. Provoking her further would be unwise."
    L "What are her weaknesses?"
    scene s4_aa17 with dissolve
    a "You intend to pressure her? That won’t work."
    scene s4_aa16 with dissolve
    L "If she doesn’t keep her mouth shut, we’ll have problems."
    scene s4_aa1 with dissolve
    a "The problem isn’t that I don’t want to."
    a "The problem is that it’s impossible."
    L "What do you mean?"
    scene s4_a75 with dissolve
    pause 1.5
    scene s4_aaa1 with dreamyzoom
    a "..."
    scene s4_a74 with linearblur
    a "…It’s a long story."
    scene s4_a75 with dissolve
    L "We have plenty of time ahead."
    a "Not now."
    L "(Sigh) Fine. I’ll stay silent this time."
    L "But I {b}will{/b} expect an explanation."
    

    $ persistent.chapter_act4_scene += 1


    



##Сцена вторая - Калестра. 

label story05_2:

    stop music1 fadeout 2.2
    scene black with dissolve 
    pause 3.2
    
    play music season4act6 fadein 3.2
    play sounds3 scifidooropen2
    show s4_c1 with dissolve 
    mc "So, why did you want to see me?"
    k "Hmm... no real reason. Thought I’d have a little face-to-face talk. Kill the boredom, maybe?"
    play sounds2 mmove 
    show s4_c2 with dissolve 
    mc "Alright then. I’ve got a couple questions, and I’d really like some answe-"
    show s4_c3 with dissolve 
    k "Have you ever died? Physically."
    mc "..."
    mc "(That… was unexpected. Where did that even come from?)"
    show s4_c4 with dissolve 
    mc "Yes."
    scene s4_c3 with dissolve 
    k "And how did it feel?"
    scene s4_c4 with dissolve 
    mc "Lame. If I can put it like that."
    mc "But… I don’t get the point."
    k "(I don’t even know why I asked that...)"
    play sounds2 whoosh
    play sounds3 punch1
    show s4_c5 
    mc "(What the-?!)"
    play sounds1 brickcollapse
    show s4_c6 with vpunch
    pause 1.2
    k "Good reflexes. Not good enough, though."
    play sounds3 mmove 
    show s4_c8 with dissolve 
    mc "You’re crazy. Why?!"
    play sounds3 mmove 
    show s4_c7 with dissolve 
    k "I just wanted to see what you’re capable of."
    mc "We’ve spent enough time together, isn’t that enough?"
    k "Where we’re going… that place is different."
    k "And honestly... you’re a pretty good toy. I’d rather not lose you."
    show s4_c9 with dissolve 
    mc "(There’s truth in her words. Besides, a good spar wouldn’t hurt.)"
    mc "Don’t regret it later. I’ll be fighting for real."
    show s4_c10 with dissolve 
    k "Hmph..."
    play sounds2 whoosh 
    scene s4_c11 
    pause 0.5
    scene s4_c12 
    pause 0.7
    play sounds3 whoosh 
    scene s4_c13 
    pause 0.6
    play sounds3 mmove 
    play sounds2 clench  
    show s4_c14 with dissolve 
    k "Caught you."
    play sounds3 punch1  
    show s4_c15 with vpunch
    mc "Arkgh..."
    show s4_c16 with dissolve 
    k "Is that it? That’s all you’ve got? I expected more."    
    mc "This definitely isn’t my best performance..."
    k "Old man, you should’ve retired long ago instead of storming towers in this condition."
    show s4_c17 with dissolve 
    mc "I can’t."
    k "Oh? And why’s that?"
    show s4_c18 with dissolve 
    mc "(I’ve gone too far. Too many sacrifices... There’s no way back.)"
    mc "(Now.)"
    play sounds3 mmove 
    show s4_c19
    pause 1.1
    play sounds2 clench 
    show s4_c20
    k "(Huh? ...Am I looking at the ceiling?)"
    play sounds1 punch1 
    show s4_c21 with vpunch 
    k "(And now I’m on the floor...)"
    stop music fadeout 3.4
    play music1 season4act15 fadein 7.4 volume 0.3
    play sounds3 mmove 
    show s4_c22 with dissolve 
    mc "Because I made a promise." 
    play sounds2 clench  
    show s4_c23 with dissolve 
    mc "A promise that I’d do everything in my power to stop this apocalypse."
    show s4_c24 with dissolve 
    mc "Yeah, compared to you and everyone else, I’ve got no strength. Just a dumb old man who wagered everything and lost."
    show s4_c25 with dissolve 
    mc "And still, as long as I’m breathing, I’ll keep trying."
    show s4_c26 with dissolve 
    k "(The toy’s really going wild. Then again... isn’t that why he’s always fun?)"
    k "(Fun...)"
    pause 0.5
    show s4_c27 with dissolve 
    k "When I first met you, that’s exactly what you looked like. Unremarkable. Weak. A stupid old man." 
    k "I could’ve killed you at any moment."
    scene s4_c26 with dissolve 
    mc "But you didn’t kill me. Why? Because of Astoria?"
    play sounds3 mmove 
    show s4_c28 with dissolve 
    pause 1.1
    show s4_c29 with dissolve 
    k "Because of myself."
    k "In you, I saw a part of myself. One I thought I’d lost a long time ago."
    play sounds3 mmove 
    show s4_c33 with dissolve 
    k "(That’s when I got curious... what kind of feeling crawled back into my chest.)"
    show s4_c34 with dissolve 
    k "(Painfully familiar. Disgusting.)"
    k "(Attachment.)"
    play sounds3 mmove 
    show s4_c35 with dissolve 
    k "Looks like someone got a little too excited. Your little friend’s practically poking at me."
    show s4_c36 with dissolve 
    mc "What are yo-"
    play sounds3 whoosh  
    play sounds2 punch1 
    show s4_c38 
    mc "(Dirty move...)"
    mc "Cheap."
    k "Oops. Did I hurt your ego?"
    show s4_c39 with dissolve 
    pause 0.5
    mc "(She’s insane, that’s a fact. Crazier than anyone I’ve ever met… but even she-)"
    mc "Attachment, huh."
    show s4_c40 with dissolve 
    k "You heard that? Thought I’d disabled that implant."
    mc "Sorry."
    pause 2.1
    mc "How did you end up in the Inquisition?"
    scene s4_c39 with dissolve 
    k "I don’t see the point in answering. And besides… it’s a boring story."
    mc "Boring? And how many people have you told it to?"
    mc "You just never found someone who’d appreciate it."
    scene s4_c40 with dissolve 
    pause 2.3
    k "Eow... Did I seriously damage something when I hit you?"
    pause 0.5
    mc "Oh, go to he-"
    play sounds2 mmove 
    scene s4_c41 with dissolve  
    k "Get up, old man."
    pause 0.5 
    play sounds3 mmove 
    show s4_c43 with dissolve 
    k "So you do want to hear how I ended up in the Inquisition, huh?"
    show s4_c44 with dissolve 
    mc "It would be useful. You’re the one I know the least here."
    mc "Paired with that loudmouth you call a sister."
    play sounds3 mmove 
    show s4_c45 with dissolve 
    k "And why exactly are you so interested in my past?"
    show s4_c46 with dissolve 
    mc "Tradition in our squad. You share your story, we repay you with a couple jokes and saving your ass."
    show s4_c47 with dissolve 
    k "Does that mean I’ll have to sit through your tear-soaked life story too?"
    show s4_c48 with dissolve 
    mc "Unfortunately, yes."
    play sounds3 mmove 
    scene s4_c50 with dissolve 
    pause 0.5
    scene s4_c51 with dissolve 
    pause 0.5
    play sounds2 mmove 
    scene s4_c50 with dissolve 
    pause 0.5
    show s4_c49 with dissolve 
    k "Boring… But fine."
    scene s4_c52 with dissolve 
    pause 1.2
    scene s4_c53 with dissolve 
    k "So. Where do I start?"
    stop music1 fadeout 2.3
    play music season4act7 fadein 5.4
    play sound towers fadein 1.3 loop volume 0.5
    play sounds3 scifidooropen2
    scene s4_c61 with dreamyzoom 
    k "(You know, the place where I grew up... some would’ve called it hell.)" 
    k "(An orphanage where the strong did whatever they wanted, and the weak only learned how to obey.)"
    k "(We weren’t an exception.)"
    k "(Me, and the one who now walks right behind your dear wife, Veyra.)"
    play sounds3 mmove 
    scene s4_c62 with dissolve 
    v "You never stop surprising me. I honestly thought you’d go beat up those idiots from the next class again today."
    v "Though I have to admit, your ridiculous reputation finally started working in your favor."
    play sounds2 footstep2  
    scene s4_c63 with dissolve 
    k "Yeah, yeah, about those big-headed idiots. Did they start bothering you again?"
    v "They wanted a rematch. You really did a number on their fragile egos."
    k "They got off easy with me."
    play sounds2 sittingchair 
    scene s4_c64 with dissolve 
    v "I already told them that. Can’t say it stopped them."
    play sounds3 clothess  
    scene s4_c65 with dissolve 
    k "Should’ve broken more fingers..."
    k "(But in practice, most people were too scared to touch us. And the ones who tried… ended very, very badly.)"
    mc "..."
    play sounds4 whoosh
    scene s4_c47 with CropMove(time=0.1, mode='slideleft')
    k "Usually this is where people start squirming. You’re taking it surprisingly calm."
    scene s4_c46 with dissolve 
    mc "I’ve seen worse sights."
    play sounds4 whoosh
    scene s4_c66 with CropMove(time=0.1, mode='slideright')
    play sounds3 mmove 
    play sounds2 hitfacefriendly 
    v "You’re seriously unhinged, you know that?"
    k "I knew you’d like it."
    k "(Cruel? Don’t care. What mattered was that it worked. And most of the time, no one touched us.)"
    scene s4_c67 with dissolve 
    a "Silence."
    k "(From a very young age, we were taught a few simple things. Strength and dominance over your enemy, lead to victory.)"
    k "(And the second one.)"
    scene s4_c68 with dissolve 
    a "An order is absolute. And our purpose is to see it carried out."
    k "(Every lecture started with that phrase. They drilled it into our heads our whole lives.)"
    k "(Soulless. No creativity. No freedom.)"
    scene s4_c69 with dissolve 
    k "(Just like the rest of the training. We were being prepared as cannon fodder.)"
    k "(Oh right, “peacekeepers.” I always forget that part.)"
    scene s4_c70 with dissolve 
    k "(And among all the others… I was-)"
    scene s4_c72 with dissolve 
    play sounds1 pisolsil
    pause 0.3
    play sounds2 pisolsil
    pause 0.3
    play sounds1 pisolsil
    pause 1.1
    scene s4_c71 with dissolve 
    k "(I was the worst of the worst. Aside from minor scuffles, I was only good at two things.)"
    k "(Talking. And shattering expectations.)"
    v "You’re getting worse every time."
    k "Love you too, sis."
    k "(Still, my heart was always set on something else.)"
    scene s4_c57 
    k "(Becoming an actress. Ironic, isn’t it?)"
    k "(Born for creation. Sentenced to violence.)"
    k "(I spent almost all my free time rehearsing in one of the art bars near the campus.)"
    scene s4_c58
    k "(It helped during stress. Or when I was bored. That’s when I actually felt alive.)"
    k "(That happiness didn’t last long.)"
    play sounds2 warambient2 loop volume 0.5
    scene s4_c113 with dissolve 
    a "It doesn’t matter who you are, or what you hoped to become. In the face of a threat, everyone is equal. Life is short. Death is inevitable. That’s a fact."
    a "But there is one thing we {b}can{/b} control - the meaning of our actions."
    a "The lives of our fallen were not wasted. We give their deaths meaning."
    scene s4_c114 with dissolve 
    a "And we will do the same for ourselves."
    a "Will we die? Maybe."
    scene s4_c115 with dissolve 
    a "But if we fall, we will leave a mark, one future generations will turn into a lesson, and into strength."
    a "So stop hesitating. Move. Fight with resolve."
    scene s4_c116 with dissolve 
    a "Show the enemy we do not bow to fear. Fight so the world knows this: we are here, and we prevail."
    scene s4_c121 with dissolve
    k "(Our commander knew how to speak. For us, she became something like a mother, one we never asked for, but desperately needed.)"
    k "(That day, though... was when I first met what others called war.)"
    stop music fadeout 0.5 
    play sounds3 scar1 
    play sounds4 hdshot
    scene s4_c122 with vpunch
    pause 2.2
    scene s4_c123 with dissolve
    k "(Total shock. Bang!)"
    play sounds1 heartbeat fadein 2.2 loop volume 0.6
    k "(I just stood there, terrified, watching someone I’d studied with for half my life fall to the ground with a hole in their head.)"
    play sounds3 punch1 
    play sounds4 fall 
    scene s4_c124 with vpunch
    k "(I would’ve been next, if not for the commander.)"
    a "What the hell are you doing?! Get a grip!"
    play music1 season4act16 fadein 16.4 volume 0.5
    scene s4_c125 with dissolve    
    k "(I didn’t even hear her back then. My head was full of something else.)"
    k "(That was the first time I truly felt fear.)"
    scene s4_c126 with dissolve
    k "(And the funniest part? When I saw his corpse, I just pissed myself. Hilarious, right?)"
    k "(Like that was all I was good for.)"    
    stop sounds2 fadeout 2.2 
    stop sounds1 fadeout 2.2
    scene s4_c55 with dissolve
    k "You could at least flinch, for appearances’ sake. Most people are already running out of the room at this point."
    scene s4_c54 with dissolve
    mc "All I’m seeing right now is a broken kid. Nothing more."
    scene s4_c52 with dissolve
    k "..."
    scene s4_c53 with dissolve
    k "Yeah. Sure. Whatever you say."
    k "Keep your concern to yourself, I’m doing just fine without it."

    scene s4_c127 with dissolve
    k "(Truth is, after that moment I couldn’t eat properly for a whole week.)"
    k "(Every time a steak hit the table, I saw guts.)"
    scene s4_c128 with dissolve
    k "(And that’s really not what you want on your mind while eating.)"
    play sounds4 girlvomiting
    scene s4_c129 with dissolve
    pause 1.2
    play sounds2 hit volume 0.3
    scene s4_c130 with dissolve
    v "Kali?! Again?!"
    k "(In one week, I even managed to drop two kilos. Impressive, right?)"
    scene s4_c132 with dissolve
    k "Sorry, sis. Not the prettiest thing to watch."
    scene s4_c133 with dissolve
    v "Yeah. True."
    scene s4_c132 with dissolve
    pause 1.1
    scene s4_c133 with dissolve
    v "Hey… you okay?"
    scene s4_c134 with dissolve
    k "I’m perfectly fi-!"
    play sounds4 girlvomiting
    scene s4_c135 with dissolve
    k "Bleeegh-"
    k "(Yeah… I’ve been better.)"

    scene black with dissolve 
    pause 1.2
    scene s4_c72 with dissolve 
    play sounds1 pisolsil
    pause 0.3
    play sounds2 pisolsil
    pause 0.3
    play sounds1 pisolsil
    scene s4_c71 with dissolve 
    v "You know shooting really isn’t your thing. Maybe you should try something else?"
    scene s4_c73 with dissolve 
    k "Easy for you to say. Best shot in the academy and all…"
    scene s4_c74 with dissolve 
    v "Well, unlike someone, my hands actually grow from the right place."
    play sounds1 pisolsil
    pause 0.3
    play sounds2 pisolsil
    k "Next time someone comes to ‘settle things’ with you, don’t drag me to the shooting range."
    v "Hey, hey, that’s against the rules."
    scene s4_c75 with dissolve 
    play sounds2 pisolsil
    k "And who said I’d play by them?"
    scene s4_c76 with dissolve 
    v "Oh, you just wait. I’m definitely getting back at you for that."
    play sounds2 pisolsil
    v "Another duel?"
    play sounds3 mmove 
    scene s4_c77 with dissolve 
    k "(We were inseparable back then. Had each other’s backs however we could. Honestly, not much has changed.)"
    k "(Except she used to be a lot more talkative.)"
    stop music1 fadeout 2.2
    scene s4_c79 with dissolve 
    pause 1.1
    scene s4_c78 with dissolve 
    a "Kalestra Elverin Ord’Laria. A word."
    scene s4_c79 with dissolve 
    k "(whispering) By my full name? Yeah… this won’t end well. I can feel it."
    v "(whispering) What did you do this time?"
    k "(whispering) I didn’t do anything… at least, not this time."
    scene s4_c80 with dissolve 
    a "This is about your future training."
    play sounds3 mmove 
    scene s4_c81 with dissolve 
    b "..."
    play sound cybernight loop volume 0.4
    scene black with dissolve 
    k "(That moment probably became the one that turned my whole life upside down.)"
    play sounds1 smoke
    scene s4_c82 with dissolve 
    k "So why exactly did you drag me out here in this shit, this gray weather?"
    scene s4_c84 with dissolve 
    pause 0.5 
    scene s4_c85 with dissolve    
    a "Answer me this. What is a warrior’s most important trait?"
    play sounds1 smoke
    scene s4_c86 with dissolve    
    k "Sorry? A warrior’s quality? Is this some kind of philosophical question or what?"
    scene s4_c87 with dissolve
    a "Just answer."
    scene s4_c88 with dissolve
    k "Devotion to the cause. That’s what you taught us, isn’t it?"
    scene s4_c89 with dissolve
    a "..."
    k "(Honestly, I have no idea what she was thinking back then, but her look said enough.)"
    play sounds3 rustling2  
    scene s4_c90 with dissolve
    a "Let me give you some advice."
    play music season4act8 fadein 7.2 
    scene s4_c91 with dissolve
    a "Leave the Peacekeepers."
    k "(At the time, I actually thought she was joking.)"
    play sounds3 mmove 
    scene s4_c92 with dissolve
    k "I-I... This is a joke, right? You’re joking?"
    k "I’ve spent my whole life on th-"
    play sounds2 mmove 
    scene s4_c93 with dissolve
    a "You’re the worst of them all. You cause problems, you’re lazy, incompetent, and you put everyone else at risk."
    a "There is nothing in you that belongs in a real warrior."
    scene s4_c94 with dissolve
    k "..."
    k "(Her words... That was when I learned words can cut deeper than steel.)"
    a "This isn’t for you."
    play sounds3 mmove 
    play sounds2 footstep2
    scene s4_c95 with dissolve
    a "Do what you’re actually good at. Good luck."
    k "(I was shattered. Completely.)"
    scene s4_c96 with dissolve
    k "(Funny, isn’t it? I was against the idea of becoming one of them, but something inside me just... clicked.)"
    scene s4_c97 with dissolve
    k "(I kept thinking: how dare they? I can’t stand it when someone decides my fate for me.)"
    scene s4_c98 with dissolve
    k "(That’s when I decided to go all in. To put everything I had on the line.)"
    play sounds3 mmove 
    play sounds2 punch1 
    scene s4_c99 with vpunch
    k "Please... Give me one last chance!"
    k "(I dropped to my knees and screamed it across the whole street. God, the shame... I wouldn’t wish that on anyone.)"
    scene s4_c100 with dissolve
    k "(But the need to prove I was worth something outweighed my pride.)"
    k "(Still, most of that was on the commander. One word from her, and my future was decided.)"
    stop sound fadeout 0.5
    scene s4_c101 with dissolve
    k "(And now the important part, how the hell I ended up in the Inquisition. The selection process was... weird, honestly.)"
    k "(First, you go into the peacekeepers. And after that, that’s it. Do whatever you want. Go wherever. Nobody gives a damn.)"
    mc "(So then, how did you end up there?)"
    play sounds2 keyboard fadein 0.2
    scene s4_c102 with dissolve
    k "(Honestly? No idea. They said there was a selection, but how or by what criteria, nobody ever really knew.)"
    k "(But that’s for later. Right now, I was just patching up my reputation.)"
    k "(Got my shit together back then. More or less. Some results showed up.)"
    k "(Except shooting. At that, I still sucked.)"
    scene black with dissolve 
    k "(So our commander decided to teach me something else.)"
    scene s4_c103 with dissolve
    k "So. Why are we here?"
    a "I’ve been ordered to train you in close combat."
    play sounds3 clench 
    play sounds1 whoosh
    scene s4_c104 with dissolve
    k "Close combat? Right. So, death then. Well… doesn’t sound too bad."
    a "Catch."
    play sounds2 jumpkalesta
    scene s4_c105 with vpunch
    k "(Funny thing, that “small blade” she handed me felt like it weighed forty sbards.)"
    k "(I remember thinking: how the hell am I supposed to fight with this club if I can’t even lift it?)"
    play sounds3 mmove 
    scene s4_c106 with dissolve
    k "(Didn’t have a choice though. I had to lift it somehow. Pain, tears, sheer stubborn will, and somehow, I did.)"
    k "(And then training. Lots of training. Way too much.)"
    scene s4_c107 with dissolve
    k "(Oh, and trust me, I regretted every damn minute of that decision. But my glorious ego...)"
    scene s4_c108 with dissolve
    k "(The idea that the commander herself was training me, that alone gave me fuel. And barely, just barely…)"
    play sounds3 fall 
    scene s4_c110 with vpunch 
    k "(I failed.)"
    k "(I had no talent. None at all. Well... okay. Some tiny bit. But nowhere near enough.)"
    k "(Nowhere near enough to be the best of the best.)"
    mc "(And yet somehow, you still managed to pull it off.)"
    play sounds3 clothess 
    scene s4_c111 with dissolve
    k "(Yeah. But not alone. If I’m being honest, I’d have quit a long time ago by myself.)"
    k "(But with her faith in me, that was a different story.)"
    scene s4_c112 with dissolve
    v "Wow. Look at you, absolutely glowing."
    k "Bruises and bumps? Yeah… call it bruised and battered, I’m shining like a damn Christmas tree."
    v "Dreams always come with a price. But in your case… The whole squad’s rooting for you."
    scene s4_c111 with dissolve
    k "(Honestly, I didn’t really need anyone else’s support... but gotta admit, it felt damn good to hear it.)"
    a "On your feet. Break’s over."
    play sounds2 mmove 
    scene s4_c109 with dissolve
    a "We’re not leaving until you land a hit."
    scene black with dissolve 
    k "(And like that, a few months just… vanished.)"
    stop music fadeout 2.3
    # scene s4_c136 with dissolve
    # k ""
    # scene s4_c137 with dissolve
    # ""
    # scene s4_c138 with dissolve
    # ""
    
    play sounds1 desertwind loop volume 0.2 fadein 1.5
    scene s4_c119 with dissolve
    k "(Until my sister and I were sent on a new assignment.)"
    k "(Eliminate someone. Or something like that. Honestly, I don’t even remember anymore.)"
    scene s4_c120 with dissolve
    k "You know, sis… I’m happy you made it far enough to look down on everyone else."
    k "Just… not from the bottom of my heart."
    scene s4_c119 with dissolve
    v "If anything, you’re the one who’s been stuck at the bottom for way too long."
    v "What about the target?"
    play sounds2 mmove 
    scene s4_c139 with dissolve
    k "I don’t see anyone. Are you sure we’re even in the right place?"
    v "Patience. That guy handles blood shipments for the elves."
    k "Oh. So an important asshole, huh? Got it."
    play sounds3 radio loop volume 0.2
    scene s4_c140 with dissolve
    k "Yeah. Arachnid Eyes listening."
    k "..."
    mc "(You okay?)"
    k "(Uh… yeah. Yeah. Just a bad memory.)"
    scene s4_c141 with dissolve
    a "Get out of there, now! You’ve been spotted!"
    k "(Back then, we either overestimated ourselves, or seriously underestimated the enemy.)"
    stop sounds3 
    play sounds3 scar1 
    play sounds4 hdshot
    scene s4_c142 with dissolve
    k "(The result…)"
    play sounds2 fall 
    scene s4_c143 with dissolve
    k "(And that’s the moment I thought I’d finally become stronger, when my sister got her head blown off.)"
    k "(Bang, and all those old injuries, from the first time, came rushing back.)"
    play sounds3 mmove 
    play music kalestratheme fadein 5.5
    scene s4_c146 with dissolve
    k "(This time it was worse than ever. No commander to save my ass.)"
    k "(My sister, instead of that kid backdays. Yeah. That was… worse. I was left alone.)"
    play sounds2 fall
    scene s4_c148 with dissolve
    k "(Seeing that hole in her head, my insides clenched. Not from fear. From rage. From bitterness.)"
    play sounds3 mmove 
    scene s4_c149 with dissolve
    k "(Losing the one you called family...)"
    scene s4_c147 with dissolve
    k "(What was going on in my head back then? Heh…)"
    scene s4_dd8 with dissolve
    k "No… This is a dream. Anyone but her…"
    scene s4_c76 with dreamyzoom
    v "You know shooting really isn’t your thing. Maybe you should try something else."
    scene s4_c99 with dreamyzoom
    a "You’re the worst of them all. You cause problems, you’re lazy, incompetent, and you put everyone else in danger."
    scene s4_dd9 with dissolve
    pause 1.6
    scene s4_dd10 with dissolve
    k "I just wanted to…"

    scene s4_c122 with dreamyzoom
    a "There is nothing in you that belongs in a real warrior."
    scene s4_c123 with dissolve
    pause 2.2
    scene s4_c130 with dreamyzoom
    v "You’re getting worse every time."
    scene s4_dd11 with dissolve
    k "I wanted to prove it…"
    scene s4_c82 with dreamyzoom
    v "Dreams come at a cost. But in your case..."
    scene s4_c56 with dreamyzoom
    a "Do what you’re actually good at. Take care."
    scene s4_dd12 with dissolve
    k "..."
    scene s4_dd13 with dissolve
    k "(Funny, right? All it took was one person dying to break me. Hilarious.)"
    scene s4_c150 with dissolve
    k "(And yet… my whole body filled with energy. I swore to myself I’d endure. I’d get out of that place.)"
    k "(And the funniest part…)"
    scene s4_c151 with dissolve
    k "(I decided to get out with her.)"
    k "(Most people would call it stupid. Insane. I didn’t give a damn.)"
    k "(I wasn’t leaving my sister behind. Not even her corpse.)"
    scene s4_c152 with dissolve
    k "(That’s when the real fun began. Me. Alone. With my sister’s body. Against a whole crowd.)"
    scene s4_c153 with dissolve
    k "(But I had nothing left to lose. So I acted. Pushed all feelings aside. Everything I knew, shoved to the back.)"
    k "(And when I saw my first target…)"
    play sounds3 whooshvortex
    scene s4_c154 with dissolve
    k "(I didn’t hesitate. I lunged at him with every ounce of rage I had.)"
    k "(They’d call it animalistic. Even by my standards, yeah. It was too much.)"
    play sounds2 katahit 
    scene s4_c155 with dissolve
    k "(My first kill…)"
    k "(And there was nothing great about it. Ugly. Animal. Absurd.)"
    scene s4_c156 with dissolve
    pause 0.7
    scene s4_aaa1 with dissolve
    k "(That’s when I carved it into my skull: Either me, or them. How? Didn’t matter.)"
    k "(...)"
    play sounds1 sth1
    pause 1.1
    scene s4_c117 with dissolve
    k "(By some miracle, I made it out alive. How? No idea. But facts are facts.)"
    k "(I took my sister with me.)"
    scene s4_c118 with dissolve
    k "(Later, thankfully, I found out she was alive. The bullet went straight through, missed the brain.)" 
    k "(I remember thinking how lucky she was… And at the same time, how glad I was I didn’t leave her.)"
    stop music fadeout 4.3 
    stop sounds1 fadeout 0.5

    scene black with dissolve 
    pause 3.2

    play sounds hospitalroom loop 
    scene s4_c158 with dissolve
    k "(And just like that, my whole life flipped upside down. All those old dreams, becoming an actress, gone. Just like that.)"
    k "(Do I regret it? Yeah. I do. But at the same time... I’m glad for what I have now.)"
    scene s4_c159 with dissolve
    a "What you did was absurd… and at the same time, noble."
    k "I didn’t really have a choice."
    a "I know."
    scene black with dissolve 
    a "The young lady asked to see you."
    k "What? Why?!"
    a "..."
    a "I’m glad you survived."
    stop sounds fadeout 0.1
    play music1 season4act14 fadein 2.0
    play sounds1 sth1
    scene s4_c160 with dissolve
    k "(And by sheer coincidence, I met her. Evrelia. The head of the Inquisition herself.)"
    mc "(Astoria’s younger sister?)"
    k "(That’s her.)"
    k "You wanted to see me?"
    play sounds heartbeat loop volume 0.3
    scene s4_c162 with dissolve
    k "(Her posture, her eyes, her presence... Absolute. Like the weight of the whole world suddenly crashing down on you.)"
    k "(I could feel her power with my entire body.)"
    scene s4_c163 with dissolve
    k "(There was one catch, though. How she looked, and how she acted. That part threw me off.)"
    play sounds3 mmove 
    scene s4_c164 with dissolve
    Evrel "Cute face."
    scene s4_c165 with dissolve
    k "(And the funniest thing? I expected a lot, but that level of absurdity? From her? Yeah, no. I froze, had no clue how to even respond.)"
    Evrel "Your report was… interesting."
    Evrel "Interesting enough that even my sister took notice."
    scene s4_c166 with dissolve
    Evrel "Tell me something."
    Evrel "How do you feel about deciding other people’s fates?"
    stop sounds fadeout 1.1 
    scene s4_c167 with dissolve
    k "(Didn’t take me long to answer, honestly. And just like that, I signed up for the next couple of years as a trainee.)"
    
    scene s4_c136 with dissolve
    k "So what’s the result? My body turned into a weapon. Scars, burns, everything you can see. One ugly mess, really."
    scene s4_c137 with dissolve
    k "Then again… isn’t that what they say? Scars make a warrior, right?"
    scene s4_c138 with dissolve
    mc "Scars are experience. Bitter, unpleasant, but necessary. I don’t see anything wrong with them."
    k "You’ve got a smooth tongue, I’ll give you that."
    k "Alright. Enough."

    stop music1 fadeout 3.3 
    scene black with dissolve 
    pause 2.2
    play music storetroom fadein 6.1 volume 0.1
    play sounds warehouseamb1 loop fadein 2.2 volume 0.6
    scene s4_c52 with dissolve
    k "..."
    scene s4_c53 with dissolve
    k "You know, I just remembered something."
    k "Your implants, still giving you trouble?"
    scene s4_c54 with dissolve
    mc "What’s with the sudden interest? Thought it was my turn to tell a story."
    scene s4_c55 with dissolve
    k "Oh, trust me, I’d love to hear your story and all that, but not right now."
    k "A little bird whispered in my ear that I should take a look at your implants. Call it curiosity."
    scene s4_c54 with dissolve
    mc "If I remember correctly, you couldn’t care less before. What changed?"
    scene black with dissolve 
    k "Let’s go."

    $ persistent.chapter_act4_scene += 1
    
# kali scene

label story05_2_1:

    stop music fadeout 2.2 
    play sounds footstep2 
    scene black with dissolve 
    pause 1.2
    play sounds2 factoryambience fadein 1.1 loop volume 0.5
    scene s4_e1 with dissolve
    show act4_s5 
    mc "(Life didn’t go easy on her, that’s for sure. But it doesn’t fully explain her mental state. Still…)"
    hide act4_s5 with dissolve
    mc "You’re a tough one."
    k "Oh, I know that without you. And watch your head, by the way."
    play sounds3 punch1 
    scene s4_e2 with vpunch
    mc "Arkh…"
    k "Told you."
    k "And about what you said earlier, truth is, that’s not really my achievement."
    play sounds3 mmove 
    scene s4_e3 with dissolve
    k "Just like you, I’m packed to the brim with implants. They’re the ones responsible for everything my body does."
    mc "Not that different, are we?"
    mc "(Whispering) My head…"
    k "Heh..."
    scene s4_e4 with dissolve
    k "Different? I don’t even know if this is really me, or someone else. Either way, I don’t lose sleep over it."
    scene s4_e5 with dissolve
    mc "(Ostorius mentioned something like this…)"
    mc "Side effects?"
    scene s4_e4 with dissolve
    k "Bingo."
    k "Nasty stuff. Don’t keep an eye on them, and in the middle of a fight your head might just-click-shut down."
    k "And ding-ding. You’re dead."
    scene s4_e5 with dissolve
    mc "With honor and glory, huh?"
    play sounds mmove 
    scene s4_e6 with dissolve
    k "Yeah. Face down in dirt and shit. Nothing noble about it."
    mc "Depends on how you look at it, but overall, I agree."
    stop sounds2 fadeout 3.4
    play sounds scifidooropen2  
    play sound warehouseamb1 fadein 4.3 loop volume 0.7
    play music1 metromusic1 fadein 2.2 volume 0.4
    scene s4_e7 with dissolve
    k "Yeah, yeah. Strip. Time to see what you’ve got under the hood."
    k "Pants stay on. One time was more than enough, I’m good."
    mc "Don’t remember agreeing to this. But I doubt I can talk you out of it."
    play sounds3 footstep2 
    scene s4_e9 with dissolve
    mc "What I don’t get is, why do you need to undress?"
    k "Hm..."
    k "I don’t like talking about this, but answer me one thing."
    scene s4_e9 with dissolve
    k "Would you rather lose all your memories… or never be able to make new ones?"
    play sounds2 footstep3 
    scene s4_e10 with dissolve
    mc "This is…"
    mc "(Is she talking about herself? Or in general?)"
    mc "Personal experience, or you want my opinion?"
    play sounds3 mmove 
    scene s4_e11 with dissolve
    k "Let’s call it personal curiosity."
    k "How did you put it? “You tell me your story, I trade you a couple of gags and saving your ass.”"
    k "Your story won’t tell me much. Your views, though? That’s a different matter."
    scene s4_e12 with dissolve
    mc "(Views, huh… Giving up the past for the sake of the future, or living in the past with no future at all?)"
    mc "(The past or the future? On one hand, how could I forget the deaths of my comrades, my own son, the betrayals and-)"
    scene s4_e13 with dissolve
    mc "(On the other… what would be the point of everything else then? By that logic, I could’ve stayed back on Earth.)"
    mc "(But honestly, why am I doing all this? Did the others really want the same thing I did?)"
    mc "(Or is this just a cover for my own selfish need?)"
    play sounds3 mmove 
    scene s4_e14 with dissolve
    mc "(Take Norman, for example. His death… and that moment at the end. In the end, he just wanted to see me… happy?)"
    play sounds4 rustling2 
    mc "(Yes, he wanted Lora back too, that’s true, but was that really the main goal?)"
    mc "(And Lora herself… At first, I ignored everything, waited, moved forward. But if I’m being honest-)"
    mc "(Whispering) Is this really the same Lora?"
    play sounds3 clothess  
    scene s4_e15 with dissolve
    mc "Probably never would."
    mc "That life is all I have left."
    play sounds2 bodytap 
    scene s4_e16 with dissolve
    k "..."
    mc "What are you doing?"
    k "Making a bad decision. Don’t interrupt."
    scene s4_e17 with dissolve
    k "So… trading the past for the future?"
    k "Honestly? Not surprised. Sounds like you."
    k "But hey, I’m feeling generous. I’ll give you a tip."
    play sounds4 bloodsqish fadein 0.3
    scene s4_e18 with vpunch
    k "Sometimes you just say ‘to hell with it’, and live all the way."
    k "One day at a time. No plans. No regrets."
    scene s4_e19 with dissolve
    k "And for that, you need enough strength not to drop dead from a sneeze."
    mc "Hey, hey, wait. Your whole neck is-"
    play sounds3 mmove 
    scene s4_e21 with dissolve
    k "Forget it. This’ll hurt. You’ll live."
    mc "That’s an implant, right?"
    scene s4_e22 with dissolve
    k "..."
    k "Inquisition architecture. Same base system as yours."
    mc "So my body won’t reject it."
    k "Your system should recognize it as a clearance key."
    mc "Should?"
    k "I said I was making a bad decision."
    scene s4_e23 with dissolve
    play sounds3 mcsystem
    pause 2.3
    $ persistent.ancient_blood_ = True
    $ persistent.tomb_screen_ = True
    $ persistent.mutants_screen_ = True
    $ persistent.inquisitor_screen_ = True
    $ persistent.warpdrive_memory = True
    $ persistent.energy_c = True
    $ persistent.parallel_threads_ = True
    $ persistent.ark_origin_ = True
    if persistent.inquisitor_access == 4:
        $ persistent.inquisitor_access = 5
        show clearlvl with dissolve 
        pause 0.5
    elif persistent.inquisitor_access == 1:
        $ persistent.inquisitor_access = 5
        show clearlvl with dissolve 
        pause 0.5
    scene s4_e24 with dissolve
    show memoryreboot with dissolve 
    k "I’m no neuromechanic. Hell if I know how this crap actually works."
    hide memoryreboot
    mc "(Same as with Mireille… but now it’s the body.)"
    k "But with this, hah… you’ll knock a lot of heads around, that’s for sure."
    play sounds3 mmove 
    scene s4_e25 with dissolve
    mc "You were against this idea."
    mc "Thanks, I guess, but what suddenly changed?"
    k "Hmm..."
    play sounds3 clench 
    scene s4_e26 with dissolve
    k "An hour ago I locked myself in the ladies’ room and masturbated thinking about you."
    mc "..."
    mc "Sorry, what?"
    scene s4_e27 with dissolve
    k "Kidding."
    play sounds3 mmove 
    scene s4_e28 with dissolve
    mc "It’s not going to stop on its own, is it?"
    k "Huh? It’ll bleed a bit. Then stop. Hopefully."
    scene s4_e29 with dissolve
    mc "What were you thinking, ripping an implant out of your neck?"
    scene s4_e30 with dissolve
    k "..."
    mc "Sit down. I’ll find something to treat that wound."
    scene s4_e31 with dissolve
    k "What, you my mom now? I can handle it."
    scene s4_e32 with dissolve
    mc "Kalestra."
    pause 1.1
    scene s4_e31 with dissolve
    k "Yeah, yeah… mom."
    scene s4_e32 with dissolve
    pause 1.1
    play sounds3 rustling2 
    scene s4_e33 with dissolve
    mc "Alright. So what exactly did you shove into my head?"
    scene s4_e36 with dissolve
    k "I had a talk with the one-eyed girl."
    play sounds3 rustling2 
    scene s4_e33 with dissolve 
    mc "The one-eyed one? Lora?"
    scene s4_e37 with dissolve 
    k "Yeah. Long story short, I told her I’d sleep with you."
    k "Ow, damn it. That hurts!"
    scene s4_e35 with dissolve 
    mc "And her reaction?"
    k "..."
    play sounds3 rustling2 
    scene s4_e34 with dissolve 
    k "She didn’t like it. Looked at me like she wanted me dead."
    k "Honestly? Kinda enjoyed it."
    scene s4_e35 with dissolve 
    mc "Predictable."
    play sounds3 rustling2 
    scene s4_e37 with dissolve 
    k "Later I thought about it… and caught myself on a weird idea."
    k "You two are married, right?"
    scene s4_e33 with dissolve 
    mc "Yeah."
    scene s4_e34 with dissolve 
    k "So how do you deal with arousal then? Implants. All that crap."
    stop music1 fadeout 3.3 
    scene s4_e33 with dissolve 
    mc "Where are you going with this?"
    scene s4_e37 with dissolve 
    k "I need to blow off steam, [mc]. Like, actually need to."
    scene s4_e35 with dissolve 
    mc "No."
    play sounds3 rustling2 
    scene s4_e36 with dissolve
    k "This isn’t a whim. It’s a need. I lent you power, you help me with something else."
    scene s4_e35 with dissolve 
    mc "I have a wife."
    scene s4_e36 with dissolve
    k "And? Honestly, I don’t give a damn."
    k "But if you really need an excuse…"
    play music season4act9 fadein 3.4 
    play sounds2 whoosh 
    play sounds3 punch1
    scene s4_e39 with vpunch
    k "Time to test your new toy."
    scene s4_e40 
    mc "(What-)"
    play sounds2 whoosh 
    scene s4_ee1 
    pause 0.6
    scene s4_ee2
    pause 0.6
    play sounds2 whoosh 
    scene s4_ee3
    k "Oh-ho! Just look at you. You can actually do something now."
    play sounds2 whoosh 
    scene s4_e42 
    k "(Those moves again?)"
    scene s4_e41 
    pause 0.6
    play sounds2 whoosh 
    scene s4_e43 
    pause 0.4
    scene s4_e45 
    pause 0.3
    play sounds2 whoosh 
    play sounds3 mmove  
    scene s4_e46
    pause 0.6
    scene s4_e47 with dissolve 
    k "(Damn… speed-type. Just what I need.)"
    play sounds2 whoosh 
    scene s4_e48 
    pause 0.5
    scene s4_e49 with dissolve 
    k "(Fast. Too fast.)"
    play sounds4 court1
    scene s4_e50 
    pause 0.6
    play sounds3 punch1
    scene s4_e51 with vpunch
    pause 1.2
    scene s4_e52 
    k "(Not bad.)"
    play sounds4 clench 
    scene s4_e53
    k "(Hey, wait, that’s-)"
    play sounds3 mmove
    play sounds2 rustling2 
    scene s4_e54 
    k "(My trick…)"
    k "(Hello, floor. Again.)"
    mc "Cool off a bit?"
    play sounds3 clothess 
    scene s4_e55 with dissolve 
    k "(Strength type too? Speed and power… huh. Interesting combo.)"
    k "(But this won’t do. My body’s on fire.)"
    scene s4_e56 with dissolve 
    k "Hey, old man, still standing?"
    k "Or you already running out of steam?"
    scene s4_e57 with dissolve 
    mc "I’m fine."
    play sounds3 mmove 
    play sounds4 clench 
    scene s4_e58 
    k "Then I just need to push you to the edge."
    play sounds2 clench 
    scene s4_e59 with dissolve 
    k "(This could end badly…)"
    k "(Screw it. Time to have some fun.)"
    mc "Arkh… you… sto-"
    play sounds2 whoosh 
    scene s4_ee5
    mc "What the-"
    play sounds4 whoosh 
    scene s4_ee4
    pause 0.6
    play sounds3 punch1
    scene s4_ee6 with vpunch
    k "Hey, hey, easy. Didn’t hit too hard, did I?"
    mc "*Spits*"
    scene s4_ee9 with dissolve 
    k "You know… if this is all you’ve got, even with implants?"
    k "I’m disappointed."
    k "Honestly, I expected more from you."
    scene s4_ee7 with dissolve 
    k "But looks like all you’re good for is eating dust with your face."
    mc "(That smug grin of hers… it’s starting to get under my skin.)"
    play sounds4 whoosh 
    scene s4_ee8 with CropMove(time=0.1, mode='slideleft')
    pause 0.6
    play sounds3 mmove  
    scene s4_ee10
    mc "(I have to go all in. In a straight fight, I won’t beat her.)"
    mc "(Make her swallow the bait.)"
    play sounds3 punch1
    scene s4_ee11 with vpunch
    k "(Yeah… show me that rage.)"
    k "(Come on, show me everything you’ve got.)"
    play sounds2 whoosh 
    scene s4_ee12 with CropMove(time=0.1, mode='slideleft')
    pause 0.7
    scene s4_ee13
    mc "(Now!)"
    play sounds3 clench 
    scene s4_ee15
    k "(Mmm… the hair?)"
    play sounds2 whoosh 
    scene s4_ee14
    pause 0.6
    scene s4_ee16
    k "(This is bad.)"
    play sounds3 punch1
    scene s4_ee17 with vpunch
    pause 0.8
    scene s4_ee18
    mc "(No matter the cost, I’m wiping out that first-round humiliation.)"
    scene s4_ee20
    k "(All in, huh? Bold.)"
    k "(Stupid, but bold.)"
    play sounds2 whoosh 
    scene s4_ee19
    pause 0.8
    play sounds4 whoosh 
    scene s4_ee21
    pause 0.6
    play sounds3 punch1
    scene s4_ee22 with vpunch
    k "(Just the way I like it.)"
    play sounds1 hit1 
    scene s4_ee23 with vpunch
    k "Ahh, now that’s the good stuff. Come on, come on!"
    k "Let it out, let your instincts take over!"
    mc "(She’s at her limit. If I don’t end this now, she’ll snap.)"
    scene s4_ee26 with dissolve 
    k "Don’t tell me you’re not enjoying this, huh, [mc]?"
    k "You feel it too, don’t you? That rush?"
    scene s4_ee24 with dissolve  
    mc "(No. Don’t fall for it. Pull yourself together, [mc]. Focus.)"
    mc "(Just a little more…)"
    scene s4_ee25 with dissolve 
    pause 0.6
    play sounds3 punch1
    scene s4_ee27 with vpunch
    mc "(Hold it…)"
    play sounds4 whoosh 
    scene s4_ee28
    pause 0.6
    play sounds3 punch1
    scene s4_ee29 with vpunch
    mc "(Hold it! And-)"
    scene s4_ee30
    mc "Got you."
    scene s4_ee32 
    k "(Huh?)"
    play sounds3 whoosh 
    scene s4_ee31 with CropMove(time=0.1, mode='slideleft')
    pause 0.9
    scene s4_ee33
    mc "How did you put it again..."

    play sounds2 hit
    play sounds3 punch1
    stop music fadeout 0.5
    scene s4_e62 with vpunch
    mc "(whispering) bingo..."
    k "Hmph. Congrats."
    k "Now you can go brag to your mommy about beating up a girl."
    mc "You really know how to get under my skin."
    k "Enough talking."
    k "If you’re not gonna do anything with me, let go."
    scene s4_e60 with dissolve 
    mc "I want an apology."
    k "Huh? And why exactly would I do that?"
    mc "(whispering) I’m waiting."
    scene s4_e61 with dissolve 
    k "*Spits*"
    menu:
        "(So that’s your answer?)":
            play music1 kali_scene1 fadein 11.4 loop
            scene s4_e60 with dissolve 
            mc "..."
            mc "(So that’s your answer?)"

        "Do nothing.":

            mc "...Let go." 
            play music season4act10 fadein 5.4 loop
            scene s4_e63 with dissolve 
            k "Huh?"
            play sounds3 clothess  
            scene s4_e15 with dissolve 
            mc "Fight’s over."
            play sounds3 mmove 
            scene s4_e13 with dissolve 
            k "Oh come on."
            k "Don’t tell me you went soft all of a sudden."
            scene s4_e13 with dissolve 
            mc "You’re not asking for sex."
            k "Oh?"
            play sounds3 clothess  
            scene s4_e15 with dissolve 
            mc "You’re trying to drown something."
            mc "Rage. Pain. Whatever the hell is eating you."
            scene s4_e11 with dissolve 
            k "Heh…"
            k "Listen to him."
            play sounds3 mmove 
            scene s4_e12 with dissolve 
            mc "Find another way."
            scene s4_e11 with dissolve 
            k "You think I haven’t tried?"
            scene s4_e12 with dissolve 
            mc "Then try harder."
            scene s4_e11 with dissolve 
            k "...You’re serious."
            play sounds3 clothess  
            scene s4_e15 with dissolve 
            mc "Dead serious."
            k "Wow."
            k "Your wife must be one hell of a woman."
            mc "She is."
            play sounds3 mmove 
            scene s4_e117 with dissolve 
            k "Heh."
            k "You know what the worst part is?"
            play sounds3 mmove 
            scene s4_e12 with dissolve 
            mc "What?"
            scene s4_e15 with dissolve 
            k "That actually makes you more interesting."
            mc "Not my problem."
            play sounds3 mmove 
            scene s4_e10 with dissolve 
            k "Oh it is."
            k "Because now I want to break that discipline of yours even more."
            scene black with dissolve 
            mc "Good luck with that."
            k "Don’t worry."
            k "I always get what I want."
            $ harem_end += 2
            jump story05_3


    
    play sounds2 mmove 
    scene s4_e64 with vpunch 
    mc "(Fine. Time to put you in your place.)"
    k "..."
    play sounds3 mmove 
    scene s4_e65 with dissolve 
    k "(Took you long enough, idiot.)"
    scene s4_e66 with dissolve 
    "(Her heavy breathing, her eyes roaming over [mc]’s body, as if waiting for his next move.)"
    "([mc] reaches out, grabs her by the waist, and pulls her closer, feeling the heat of her body against his.)"
    k "Finally decided to take control?"
    scene s4_e67 with dissolve 
    mc "Before we start… tell me. Do you have any experience?"
    k "And why, does that matter to you?"  
    mc "I’m a bad husband, but I try to be an attentive partner."  
    mc "If I fail to please you, it’s going to bruise my ego."
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
    mc "(That arrogant smile… strange thing is, I want to make her beg.)"
    mc "I can see you’re impatient. But then I thought…"
    "[mc] grinds his cock against her pussy, soaked in her juices, feeling how wet she is."
    k "Hey, hey. Don’t tease. Put it in already."
    scene s4_e73 with dissolve 
    mc "..."
    mc "What do good girls do?"
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
    mc "You’re… incredible."
    k "Mmmm... Are you enjoying the way my pussy squeezes around your dick?"
    mc "(Her pussy grips me like a living thing, pulling me in deeper every time…)"
    mc "(No. Hold it together, [mc]. Don’t let her take control.)"
    k "AAAa-a-argh..."
    k "F-Fuck..."
    k "(Did he just get rougher?)"
    mc "You're so fucking tight, Kali..."
    mc "(That tight… is this her first time?)"
    mc "Does it hurt?"
    k "Ahh... What do you think?"
    k "Or is all your attention buried in my filthy little pussy, huh?"
    k "MMmmmmMMmm..."
    k "The way it sounds..." 
    k "Every time you slam that huge cock into me... ahh...."
    k "(I don’t even know what I’m saying anymore...)"
    "(Overwhelmed by pleasure, her mind processes it all as if it were the first time…)"

    mc "You really love dirty talk, don’t you?"
    mc "Every time... you squeeze me even harder..."
    k "Oh...." 
    k "You have no idea..."
    k "How much..."
    k "Ahhhh..."
    mc "(I’m close… at this pace, I’ll lose.)"
    k "It turns me on more when you call things by their real names..."
    k "Aaaahh..."
    k "The sound of my soft, soaked pussy... All those juices spilling out..."
    mc "There’s something about it..."
    k "I can feel it tightening…"
    k "Giving itself to you, right in your hands..."
    k "Mmmm..."
    k "But you know..."
    k "Is that really all you’ve got?"
    mc "(Listen to her now, she was shaking before, and now...)"
    k "What, went quiet all of a sudden?..." 
    k "Did I... ahhh...." 
    k "Hit your ego?..."
    mc "So that’s how it is, huh? Then I won’t hold back."
    k "Come on... I’m waiting."
    k "Drive that huge cock into my pussy. Rip it apart."
    k "Use me, like I’m nothing but the tip of your cock."

    play sounds2 whoosh 
    image s4_kali_2 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_2.webm")
    show s4_kali_2 with CropMove(time=0.1, mode='slideleft')

    mc "For someone dripping like that, you’re awfully brave."
    k "Harder..."
    k "More..."
    k "I need more..."
    k "(Riding a cock this big feels... fucking amazing.)"
    k "(But he doesn’t need to know that.)"
    mc "You went quiet. Still with me… or already drifting?"
    k "Arrogant bastard..."
    k "You talk too much, use your body instead..."
    k "AAAARRGHH...!"
    k "T-That's it!"
    k "Yes, yes, just like that!"
    k "Aaaahh... ahh... ahhhh..."
    mc "(What’s happening to my body… I want more. Harder.)"
    k "AaAaaahh..."
    mc "(Feels like I’m back in puberty… damn.)"
    mc "Ahhh... Y-Your pussy is squeezing..."
    k "Aaaahhhhhh..."
    k "I c-can't..."
    k "A-A-AAAARGHHH..."
    mc "Did you just cum?"
    k "Ahhh... yeahhhh..."
    k "Your cock is driving me insane..."
    mc "This isn’t over."    

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
    mc "I don’t think so..."
    k "I want to feel you deeper..."
    k "Give it to me hard..."
    k "D-DEEPER..."
    k "I’m almost jealous of that one-eyed girl... She kept all the fun to herself."
    mc "Just look at you. You’re dripping like a burst pipe."
    mc "Enjoying it so mu-"
    mc "AAAARGH."
    k "And what about you? You’re pounding me like you’re trying to fuck me senseless."
    mc "You sound like you’re protesting."
    k "Nah. I’m all for it."
    k "I c-can't.."
    k "Again!"
    k "A-A-AAAARGHHH..."
    mc "How many times you already climaxed?"
    k "Mmmm..."
    k "Sixth? I lost count after the third..."
    k "Ahhhh..."
    k "AAAa-a-argh..."
    mc "You’re way too tight..."
    k "That’s because you’re too fucking big..."

    play sounds2 whoosh 
    image s4_kali_4 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_kali_4.webm")
    show s4_kali_4 with CropMove(time=0.1, mode='slideleft')

    k "Y-yes!"
    k "Harder..."
    k "Give it to me hard..."
    k "D-DEEPER..."
    mc "Insatiable."
    mc "I... I can’t hold it..."
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

    play music season4act10 fadein 5.4 
    scene s4_e75 with dissolve 
    mc "Can I ask you something? Were the implants really the reason… or was it something else?"
    k "What’s with the sudden question?"
    k "You think I just decided to fuck you out of pure romance?"
    mc "..."
    scene s4_e76 with dissolve 
    k "You know."
    k "That was my first time."
    scene s4_e77 with dissolve 
    mc "Wait, what?"
    scene s4_e76 with dissolve 
    k "What?"
    scene s4_e77 with dissolve 
    mc "That was your first time?!"
    scene s4_e79 with dissolve
    k "Yeah."
    k "I don’t get why you’re so shocked."
    k "Or what, did you think I jump every guy I meet?"
    scene s4_e78 with dissolve 
    mc "Yeah?"
    k "I’ve got a dildo for that, you know."
    k "Conversation over."
    scene s4_e81 with dissolve 
    mc "Damn… you really are unhinged. Why me?"
    scene s4_e76 with dissolve 
    k "Guess I got attached."
    k "Then things just… spiraled."
    k "That’s all."
    scene s4_e78 with dissolve 
    k "By the way, about what I said earlier…" 
    k "Go sort out your mess with your wife, yeah?"
    k "Because from now on…"
    k "I’m gonna be using you a lot more often."
    scene s4_e75 with dissolve 
    mc "This was a one-time thing."
    k "The last time will be when you’re dead."
    stop music fadeout 4.5
    k "Until then?"
    k "You and I are tied together now."
    $ persistent.Kalestra_replay = True

    $ persistent.chapter_act4_scene += 1

    


    

##Сцена вторая - Астория.

label story05_3:

    stop sound fadeout 1.1
    scene black with dissolve 
    pause 1.2
    play music memoryastoria fadein 5.4
    pause 2.2
    play sound gatebackground fadein 5.4 loop volume 0.5
    
    show s4_b2 with dissolve    
    show act4_s6 
    am "..."
    show s4_b3 with dissolve 
    sel "You know, I’m amazed at how calm your face looks in a moment like this."
    sel "The capital is burning, our armies are fighting tooth and nail for every planet… and here you stand, simply watching."
    sel "Most would call you-"
    show s4_b4 with dissolve 
    am "Mad?"
    show s4_b5 with dissolve 
    sel "Exactly."
    am "You’re all the same, strong and clever on the outside, yet hollow and helpless within."
    show s4_b6 with dissolve 
    sel "Emotionless as always. But tell me, sitting idle while the other races spit on us… is that truly your idea of a solution?"
    show s4_b7 with dissolve 
    am "Before you lie to me, learn to believe your own falsehoods."
    am "You murdered your father and stole the throne. Why?"
    am "The answer is simple, self-interest."
    show s4_b8 with dissolve 
    sel "So easy to speak for someone who has lived her whole life above the world."
    sel "Though, what am I saying, you even locked your own sister in the abyss."
    scene s4_b10 with dissolve 
    am "Time. A fundamental constant, one that never needed a definition to exist."
    am "Tell me, why has every era tried to claim dominion over it?"
    scene s4_b9 with dissolve 
    sel "Because of fear, fear of your own frailty."
    sel "Even beings like us share one terror: we are not immortal."
    scene s4_b10 with dissolve 
    am "This power did not save your father."
    scene s4_b11 with dissolve 
    sel "Nor did it save your sister."
    show s4_b12 with dissolve 
    sel "Tell me, Evrelia possessed this power, yet her path led to chains. Why?"
    scene s4_b13 with dissolve 
    am "..."
    scene s4_b14 with dissolve 
    sel "Don’t pretend you never thought it through."
    show s4_b15 with dissolve 
    sel "People fear what they cannot control."
    sel "And you were no exception. You locked her away because you feared her strength."
    show s4_b16 with dissolve 
    am "I acted for the Federation’s sake."
    scene s4_b18 with dissolve 
    sel "So did I."
    sel "It’s always easier to judge another’s sins… while refusing to look at your own."
    sel "Your sister became the proof of it."
    scene s4_b17 with dissolve 
    am "She knew what she was stepping into, yet she chose stupidity over reason."
    scene s4_b19 with dissolve 
    sel "Both betrayed, yet, I wonder… To die feels kinder than living an entire life knowing your own blood betrayed you."
    scene s4_b20 with dissolve
    am "You could have spared him. You chose not to."
    sel "He was a weak ruler. He bowed and endured humiliation from every other race."
    scene s4_b21 with dissolve 
    am "He was wise, not weak."
    sel "And you call that wisdom? Bowing before those we surpass, absurd."
    sel "Because of him we lost respect. Because of him, they mocked us, and despised us."
    scene s4_b22 with dissolve 
    pause 0.5
    scene s4_b24 with dissolve 
    am "He did what he did to save your people."
    scene s4_b25 with dissolve 
    sel "To suffer for what we never did? Please…"
    sel "Death is preferable to such disgrace."
    show s4_b27 with dissolve 
    am "Few can kneel and silence their pride."
    am "Which is why the other leaders respected him. None ever looked down on him for it."
    sel "..."
    am "Why are you here?"
    show s4_b26 with dissolve 
    sel "The same reason you didn’t stop us."
    sel "The Abyss."
    show s4_b28 with dissolve 
    am "..."
    sel "But what interests me more is this, why didn’t you do it yourself?"
    show s4_b29 with dissolve 
    am "(Because I already tried...)"
    stop music1 fadeout 0.6
    stop sound 
    play sounds4 cinematichit3
    play music season4act11 fadein 5.4
    show s4_b30 with dissolve 
    show act4_s7 
    em "Stop acting like a spoiled child. You knew the law, and you chose to break it anyway? Lost your mind?"
    hide act4_s7 with dissolve 
    Evrel "Yeah, yeah, I screwed up, happy now? And maybe, {b}just maybe{/b}, I got a little carried away and made a mess."
    em "Got carried away,’ she says. There’s a whole damn galaxy hunting you now. If not for your sister, I’d have handed you to the Keepers myself."
    Evrel "Oh please. Forgot to ask the big lizard for her opinion."
    em "You wanna get mouthy now? Go ahead, tell her something. She barely listens to me as it is."
    am "(If I hand her over, the Federation falls. If I don’t… I lose her.)"
    show s4_b31 with dissolve 
    am "I agree with Ember. You crossed a forbidden line."
    play sounds2 mmove 
    show s4_b32 with dissolve 
    Evrel "Asti, forgive me, really. I messed up, I admit it. But who could’ve thought a small spatial jump would stir up this kind of storm?"
    Evrel "(I never imagined the consequences would be this bad...)"
    show s4_b33 with dissolve 
    em "Jump or no jump. Rules exist to keep people like you in check, and you broke them."
    play sounds2 glitchfear volume 0.3
    show s4_b34 with glitch
    pause 0.6
    show s4_b35 with dissolve 
    Evrel "Come on. They’ve always been looking for an excuse to get rid of me. This little stunt just gave them one."
    Evrel "Can’t control it, eliminate it. Sounds familiar, doesn’t it?"
    play sounds2 clothess 
    show s4_b36 with dissolve 
    Evrel "(So flawless, so noble on the outside...)"
    Evrel "(...and underneath the masks, greedy, selfish hypocrites.)"
    pause 0.5
    am "(Am I ready to lose her? And is the Federation worth more than one life…?)"
    am "What will you do now?"
    play sounds2 glitchfear volume 0.3
    show s4_b37 with glitch
    Evrel "Honestly? No idea. I’ll figure something out. Wouldn’t be the first time I crawl out of trouble like this."
    show s4_b38 with dissolve 
    em "I doubt it. They’re not letting you walk away from this."
    Evrel "And why exactly wouldn’t they?"
    play sounds2 glitchfear volume 0.3
    play sounds3 heels1
    show s4_b39 with glitch
    am "It will damage their authority."
    show s4_b41 with dissolve 
    Evrel "You both know damn well they don’t care about authority!" 
    Evrel "After what they did to the elves, especially not."
    show s4_b40 with dissolve 
    am "Evrelia."
    am "We all know what became of the first expedition that entered the First Tomb."
    am "Everything the Empire unleashed, and everything that remains, is absolute taboo."
    scene s4_b41 with dissolve 
    Evrel "That’s just an excuse-"
    scene s4_b39 with dissolve 
    am "You broke that taboo. What happened to the elves… now awaits us."
    scene s4_b41 with dissolve 
    Evrel "I-"
    pause 1.0
    scene s4_b39 with dissolve 
    Evrel "(No… she’s right. What was I even thinking, going to that tomb?)"
    Evrel "(Seriously… what {b}was{/b} I thinking?)"
    pause 0.7
    am "(She’s powerful, unbelievably powerful… but her recklessness has never led to anything good. And still, I cannot give her up.)"
    am "(Even if it costs us everything.)"
    show s4_b42 with dissolve 
    am "I will send you into the future."
    show s4_b45 with dissolve 
    pause 1.2
    show s4_b44 with dissolve 
    Evrel "WHAT?! ARE YOU OUT OF YOUR MIND?! This will destroy you, and the entire Federation!"
    Evrel "Asti, please, tell me you’re joking-"
    am "I won’t allow them to harm you."
    Evrel "Then I’ll kill them myself!"
    am "..."
    am "If you kill them, the galaxy will collapse into chaos."
    show s4_b47 with dissolve 
    Evrel "The idea of you sacrificing yourself doesn’t exactly make me smile!"
    show s4_b46 with dissolve 
    em "Let this be a damn lesson-"
    Evrel "Don’t interfere."
    am "Evrelia, listen to me..."
    scene s4_b47 with dissolve 
    Evrel "If this is your way out, then I hate it. The thought that I stay alive at the cost of your life is the worst thing imaginable!"
    Evrel "And I decide what I do with my damn life!"
    show s4_b48 with dissolve 
    am "Don’t do anything foolish. This is the only way."
    show s4_dd18 with dissolve 
    pause 2.3
    show s4_dd19 with dissolve 
    em "She’s gone." 
    em "Damn, that girl’s got a nasty temper, really nasty."
    scene s4_dd18 with dissolve 
    pause 1.2
    em "Wait, were you actually ready to trade everything you own for her?" 
    em "Should’ve handed her to me instead, I would’ve-"
    scene s4_dd18 with dissolve 
    pause 1.2
    show s4_dd20 with dissolve 
    em "Alright, alright, don’t glare at me." 
    em "I’ll see what I can do, but don’t get your hopes up."
    stop music fadeout 4.3
    scene black with dissolve 
    am "Thank you, Em."
    em "I’m not doing it for free." 
    em "I’ll take my cut, and it’ll be big."
    play music1 season4act17 fadein 5.4
    pause 3.2

##вторая часть 

    show s4_b49 with dissolve 
    am "(A world in exchange for one life… or one life in exchange for a world?)"
    pause 0.5
    am "(Sometimes we must make choices so heavy that everything hangs on their outcome.)"
    show s4_b52 with dissolve 
    am "(And a path that appears righteous… may lead to anything but salvation.)"
    am "(At times, we must compromise with fate itself.)"
    show s4_b53 with dissolve 
    Evrel "{b}Sings"
    am "(All our lives we stood side by side, our triumphs, our failures, our joy and our suffering were always shared between the two of us.)"
    show s4_b54 with dissolve 
    am "(Without her, I would not exist. And without me, neither would she.)"
    am "(Yet one day the world decided it wished to take her from me.)"
    show s4_b55 with dissolve 
    Evrel "You know… sometimes I wonder what it would be like if we all turned into flowers."
    show s4_b56 with dissolve 
    am "A flower?"
    scene s4_b55 with dissolve 
    Evrel "To live your entire life in one quiet place. On a beautiful meadow, wrapped in nature’s calm."
    Evrel "If that isn’t paradise… then what is?"
    scene s4_b56 with dissolve 
    am "It does sound… not entirely unpleasant."
    pause 2.1 
    scene s4_b55 with dissolve 
    Evrel "So? Did you come here to change my mind?"
    pause 0.6
    scene s4_b57 with dissolve 
    am "Will it work?" 
    am "You’ve already chosen your path."
    scene s4_b58 with dissolve 
    Evrel "When flowers die, they shed their petals…"
    Evrel "…so something new can grow."
    Evrel "And then, they begin a new life."
    pause 0.6
    scene s4_b57 with dissolve 
    am "You don’t regret leaving this world like this?"
    scene s4_b59 with dissolve 
    Evrel "We’ve both lived a long life. By everyone else’s standards, far too long."
    scene s4_b60 with dissolve 
    Evrel "And for better or worse, everything has an end. I just chose to hurry the inevitable."
    Evrel "Do I regret it?"
    Evrel "Not even a little."
    scene s4_b62 with dissolve 
    Evrel "But you… you’re a different matter."
    Evrel "I’m sorry, Asti, but you’ll have to keep living without me."
    Evrel "And take care of this whole Federation… and everything that comes with it."
    pause 0.5 
    scene s4_b63 with dissolve 
    am "Cruel."
    scene s4_b61 with dissolve 
    Evrel "I’m sorry."
    scene s4_b64 with dissolve 
    pause 2.1
    scene s4_b65 with dissolve 
    am "Do you remember how we spent time here as children?"
    Evrel "Huh? Oh, don’t remind me, I still get chills remembering how angry Mother got when she saw the bruises."
    scene s4_b66 with dissolve 
    am "Can you blame her? You were a real little shit back then."
    Evrel "Whoa, since when do you use words like that?"
    scene s4_b67 with dissolve 
    am "Back off."
    scene s4_b68 with dissolve 
    pause 2.1
    scene s4_b69 with dissolve 
    Evrel "(I’d almost forgotten what it feels like… to just sit and talk with family.)"
    Evrel "(Funny how, right before death, you start thinking about things like that.)"
    scene s4_b70 with dissolve 
    Evrel "Sis?"
    scene s4_b69 with dissolve 
    am "Yes?"
    scene s4_b70 with dissolve 
    Evrel "Thank you."
    am "..."
    scene s4_b71 with dissolve 
    am "(Every minute stretches into eternity… and eternity passes in a single minute.)"
    am "(It’s hard. It hurts. It feels hopeless… and worst of all, nothing can change it.)"
    scene s4_b72 with dissolve 
    Evrel "Beautiful."
    scene s4_b73 with dissolve 
    am "Why didn’t you go to the past and try to fix this?"
    scene s4_b72 with dissolve 
    Evrel "I tried."
    Evrel "But I couldn’t."
    scene s4_b74 with dissolve 
    pause 1.1
    scene s4_b75 with dissolve 
    am "What? How?"
    scene s4_b76 with dissolve 
    Evrel "No matter how much power you have, messing with time never ends well."
    Evrel "In the end, Asti… we’re not all-powerful."
    pause 2.2
    Evrel "Well… I guess it’s time. They’ve arrived."
    scene s4_b79 with dissolve 
    "The air shuddered ever so slightly, and three figures in white cloaks appeared in the garden."
    scene s4_b78 with dissolve 
    a "And I am pleased to see you as well, Lady Astoria… young lady."
    scene s4_b80 with dissolve 
    Evrel "Disgusting as ever."
    scene s4_b81 with dissolve 
    am "What does a Keeper want in my home?"
    scene s4_b82 with dissolve 
    a "By Order Seventy-Two, Lady Evrelia is to be brought before the court and punished for her crimes."
    am "Who issued this order?"
    a "Unanimously. The Council of Keepers."
    a "Any resistance will result in your entire race being wiped from the face of the galaxy."
    a "But I suspect you already know that."
    scene s4_b81 with dissolve 
    am "May I ask a single question, why her?"
    scene s4_b80 with dissolve 
    a "I fail to see what you mean."
    scene s4_b84 with dissolve 
    am "Very well, I’ll answer it myself: you fear that one day she will surpass you."
    am "You fear what you cannot control, and so you chose to erase her."
    scene s4_b85 with dissolve 
    a "I understand your emotions, but you are crossing the bounds of what is permit-"
    scene s4_b86 with dissolve
    am "Many have committed far worse crimes than she, yourself included. Yet you select her as the sacrificial lamb?"
    scene s4_b87 with dissolve
    am "Then hear this: if you intend to destroy her, you will have to destroy all of us."
    scene s4_b88 with dissolve
    am "Every last one."
    a "..."
    scene s4_b89 with dissolve
    aa "What are your orders, Keeper? If she joins the fight, we won’t stand a chance."
    scene s4_b91 with dissolve
    a "If I were you, I would think very carefully about your next move."
    scene s4_b90 with dissolve
    y "I wouldn’t advise it."
    aa "How dare you speak to a Keeper that way, servant?!"
    y "..."

    scene s4_b93 with dissolve
    am "(whisper) If a flower is meant to begin a new life today… then I will become the soil for it."
    am "(whisper) I’ll hold them off. Run. Run with everything you have."
    scene s4_b95 with dissolve
    Evrel "(Her voice shakes… yet I can feel the anger and hurt behind her mask of strength and independence. Damn, Asti… you’re amazing.)"
    scene s4_b96 with dissolve
    Evrel "(But none of this will change anything.)"
    scene s4_b97 with dissolve
    Evrel "(whisper) A choice without a choice… right?"
    scene s4_b98 with dissolve
    Evrel "You were incredible. I always felt safe behind your back."
    Evrel "I was really, really lucky to have a big sister like you."
    Evrel "In that sense… I guess I won the lottery at birth."
    scene s4_b99 with dissolve
    pause 0.5 
    Evrel "Still… it’s time to say goodbye."
    "Tears begin to well up in Astoria’s eyes."
    scene s4_b100 with dissolve
    am "It’s cruel..."
    scene s4_b101 with dissolve
    am "So cruel... unbearably cruel..."
    scene black with dissolve 
    Evrel "(A compromise with fate, sis. A compromise with fate...)"
    pause 3.2 
    scene s4_b102 with dissolve
    Evrel "One last smile, sis. I don’t want the last thing I see to be your sad face."
    Evrel "That’s better."
    Evrel "Take care of yourself."
    scene black with dissolve 
    a "Please, come with us, Lady Evrelia."
    pause 1.1 
    scene s4_b103 with dissolve
    y "I don’t know much… but I heard they plan to cast her into the Abyss."
    scene s4_b104 with dissolve
    y "I’m not sure how different that is from death… but still."
    scene s4_b105 with dissolve
    y "How are you holding up?"
    scene s4_b106 with dissolve
    am "I… could you leave me alone?"
    scene s4_b105 with dissolve
    y "..."
    scene s4_b106 with dissolve
    am "Please."
    scene s4_b105 with dissolve
    pause 3.2
    scene s4_b107 with dissolve
    y "I’ll go keep an eye on the young lady."
    am "Thank you."
    scene s4_b108 with dissolve
    am "(Sometimes we must make choices... and their consequences reshape our entire lives.)"
    am "(A world for one life… so that’s what it truly means…)"
    scene s4_b109 with dissolve
    am "AAAAAAAAAAAAAAAAAAAAaaah...!"
    "Regret and sorrow fused into one. A voice that had always remained restrained finally broke, torn apart by raw, unbearable pain."
    scene black with dissolve 
    show memoryreboot with dissolve 
    pause 1.1
    $ persistent.keepers_screen_ = True
    
    $ persistent.chapter_act4_scene += 1




    
    
    
    



##Сцена третья - Откровения
label story05_4:

    stop music1 fadeout 4.2
    pause 2.2
    scene black with dissolve 
    pause 4.2

    play sounds spaceshipengine1 fadein 3.5 volume 0.1 loop
    play music season4act3
    scene s4_d1 with dissolve 
    show act4_s8 
    L "(What an idiot I am… Why, why can’t I just go to him and say it all as it is?)"
    hide act4_s8 with dissolve 
    L "(No lies. No pretending. Just tell him everything. What happened. What I did.)"
    L "(Just...)"
    scene s4_d3 with dissolve 
    L "(whispering) God… I really am a fool..."
    v "..."
    play sounds2 mmove 
    scene s4_d5 with dissolve 
    L "(When did everything go wrong? When I started the research? Or when I got involved with Li?)"
    L "(And was there ever a way out of this? I don’t know...)"
    scene s4_d6 with dissolve 
    L "Tell me... what would you do if one day you found out that the person you love..." 
    L "Someone you thought you knew your whole life..."
    L "Had been lying to you?"
    scene s4_d5 with dissolve 
    v "Are you talking about yourself?"
    scene s4_d6 with dissolve 
    L "Just answer the question."
    scene s4_d7 with dissolve 
    v "That depends on the circumstances."
    v "If the intentions were good - acceptable."
    v "If not… that’s a different matter."
    scene s4_d8 with dissolve 
    L "Everything is poison, everything is medicine. It’s all about the dose… isn’t it."
    play sounds2 keyboard  
    scene s4_d9 with dissolve 
    v "Something like that."
    play sounds3 mmove   
    scene s4_d11 with dissolve 
    L "Then… can I tell him the truth? He’s suffered enough already. At least he deserves to know why-"
    scene s4_d10 with dissolve 
    pause 2.1
    scene s4_d9 with dissolve 
    v "Out of the question. The less he knows, the better it is, for all of us."
    scene s4_d12 with dissolve 
    L "(“Better”? You’re just afraid that if he learns the truth, you’ll have to kill him. And you can’t do that.)"
    L "(Though it’s almost funny… He went to the edge of the galaxy for me.)"
    play sounds3 clothess   
    scene s4_d13 with dissolve 
    L "(And in return… what do I give him? Lies? Pain? Ignorance… and a broken heart?)"
    L "(What a reward. Well done. Wife of the year... no, of the decade…)"
    play sounds3 mmove   
    scene s4_d4 with dissolve 
    L "..."
    L "(So, Lora, what are you going to do? Keep running away… or finally tell him what really happened?)"
    L "..."
    scene s4_d6 with dissolve 
    L "You have the helm. I… need to step away for a moment."
    scene s4_d7 with dissolve 
    v "The Lady won’t approve."
    scene s4_d14 with dissolve 
    L "I’ll deal with her later."
    v "(You will regret this.)"

    scene black with dissolve 
    pause 3.2 

    play sounds3 scifidooropen2   
    scene s4_d15 with dissolve 
    L "(whisper) I’m sorry, my love… I did all this to protect you."
    play sounds4 clothess 
    scene s4_d19 with dissolve 
    L "(Will he believe me? I’ve lied for so long… and he, he saw it, but chose to accept it.)"
    L "(But what if the truth changes everything? What if he doesn’t believe me at all?)"
    play sounds3 mmove 
    scene s4_d22 with dissolve 
    L "(What if, after I tell him everything, he thinks it’s just another lie?)"
    L "(Then it’s over. After all this… trust would be almost impossible to restore.)"
    play sounds3 footstep3    
    scene s4_d16 with dissolve 
    L "(Maybe… maybe it’s not too late to leave everything as it is?)"
    stop music fadeout 5.4
    L "..."
    
    scene s4_d17 with dissolve 
    L "(Sighs) May I come in?"
    
    play music1 mirielwalk fadein 5.4
    scene s4_d23 with dissolve 
    h "Lora? What are you doing here?"
    mc "..."
    mc "(So the main heroine finally shows up… Guess it’s time to settle everything here and now.)"
    L "I-"
    scene s4_d24 with dissolve 
    mc "Lora? We need to talk."
    scene s4_d25 with dissolve 
    L "(That look… He’s serious. There’s no point in running, is there? Right…)"
    scene s4_d26 with dissolve 
    L "Alright. But before that… I need to ask you for one thing."
    L "No matter what happens after this, promise me you’ll do exactly what I say. Okay?"
    scene s4_d27 with dissolve 
    mc "I have to hear-"
    L "[mc]! Please… Just this. I’m begging you…"
    scene s4_d31 with dissolve 
    pause 0.7
    mc "(And what do I do? Agree? Like I even have a choice…)"
    mc "(On the other hand, what do I lose? She’s your wife, after all… or trying to be.)"
    scene s4_d30 with dissolve 
    mc "I’ve already given you enough chances."
    mc "Sorry. I really am trying… but I can’t."
    scene s4_d28 with dissolve 
    L "I-"
    L "(It hurts… my chest feels tight, like it’s being crushed. But I should have expected this.)"
    scene s4_d29 with dissolve 
    L "Yes. I understand."
    pause 0.7
    L "(Sighs) Alright then. I’ll tell you everything exactly as it is."
    L "No secrets. No lies. The truth. And only the truth."
    scene s4_d31 with dissolve 
    mc "..."
    L "No one knows if we’ll survive. If we’ll even be able to complete this mission…"
    L "I thought about it for a long time. Weighed every possible outcome."
    mc "(She’s scared, voice shaking, eyes darting everywhere. Part of me wants to pull her close… but the other part-)"
    scene s4_d32 with dissolve 
    h "Yeah, alright, I’ll just-"
    scene s4_d33 with dissolve 
    L "No. You all need to hear this. Every single one of you."
    scene s4_d34 with dissolve 
    mc "Even Miriel and Kalestra?"
    L "..."
    L "They will be the guarantee of your survival."
    scene s4_d35 with dissolve 
    mc "A guarantee for survival? Fine."
    scene s4_d36 with dissolve 
    L "(Sighs) Well… it’s time."
    stop music1 fadeout 2.2

    scene black with dissolve 
    "13 years before the key events. Or 4 years by Earth standards."
    play sounds1 carengine3 fadein 2.0 loop
    scene s4_d37 with dissolve 
    pause 0.5
    scene s4_d38 with dissolve 
    L "{b}humming softly{/b}"
    L "(What should I make for dinner today? Curry? No, [mc] hates it. Maybe baked chicken?)"
    L "(No, that won’t work. Norman won’t eat that… Hmm. Cutlets? Yes! That’s perfect!)"
    scene s4_d39 with dissolve 
    L "(whispering) The best cutlets in the whole world… yay…"
    scene s4_d40 with dissolve 
    a "Dr. Lora? You seem to be in a great mood today. Something nice happen?"
    scene s4_d41 with dissolve 
    L "We’re having a family dinner today!"
    scene s4_d42 with dissolve 
    L "Well, just like yesterday… but today is even more special than yesterday!"
    scene s4_d43 with dissolve 
    a "Really? Glad to hear that. Please, go ahead, and have a lovely family dinner, Dr. Lora."
    scene s4_d44 with dissolve 
    L "Oh, yes, yes. And tell your wife thank you for the recipe, it was absolutely wonderful."
    a "I will."
    a "And give my regards to your son. He’s always welcome here."
    L "Take care Jason."
    stop sounds1 fadeout 0.7

    scene black with dissolve 
    L "(That day felt just as ordinary as any other. At first, nothing hinted at what was coming.)"
    L "(But that was the day we were assigned to a new site, code-named “Ark.”)"
    L "(The place where the warp-drive was taken from.)"
    scene s0ch58 with dreamyzoom 
    play music season4act10 fadein 2.2
    L "(For the record, I’m talking about this thing right here.)"
    L "(I knew his origin wasn’t entirely… earthly. I just never imagined it was this far from it.)"
    scene s4_d45 with dreamyzoom 
    L "With all due respect, Doctor Li, I can’t. I have a family dinner tonight. I need to be there."
    scene s4_d46 with dissolve 
    R "Dr. Lora, without you this entire expedition is going to fall apart."
    R "And as unpleasant as it may sound, this expedition needs you."
    scene s4_d47 with dissolve 
    L "Oh, really? Well, thank you for the compliment. It’s nice to know I’m valued so highly, but still… I can’t."
    L "My husband and I talked about this side of my work. We both decided to spend more time together."
    scene s4_d48 with dissolve 
    R "You don’t need to worry. It won’t take much of your time."
    R "After that, we’ll take you straight home. Deal?"
    scene s4_d49 with dissolve 
    L "I… I need to make a call."

    scene s4_d50 with dissolve 
    mc "And how long is this going to take?"
    scene s4_d51 with dissolve 
    L "I don’t know. They say I should be home by evening."
    scene s4_d52 with dissolve 
    mc "Lora, we’ve been through this before."
    L "I know, love. I know. That’s why I’m asking you… What do you think?"
    scene s4_d53 with dissolve 
    mc "(sigh) Just this once, alright? If you’re late, Norman and I will eat everything and leave you nothing."
    scene s4_d54 with dissolve 
    L "Hey! That’s not what we agreed on!"
    scene s4_d55 with dissolve 
    mc "Yeah, yeah, I’ll listen to all your complaints later… Take care."
    scene s4_d56 with dissolve 
    L "I love you. Kisses for both of you!"

    

    scene black with dissolve 
    R "Ready?"
    L "Yes."
    L "(The moment that turned our entire lives upside down.)"

    play sounds2 rain2 volume 0.4 loop 
    scene s4_d62 with dissolve 
    L "(The Ark. An alien vessel designed to transport a relocation mechanism. In simple terms, a gate.)"
    L "(One important clarification: a breach and a gate are not the same thing.)"
    L "(A breach is a natural phenomenon. A gate is a machine built to control one.)"
    L "(The truth is… we learned that much, much later.)"
    play sounds4 footstep2 
    scene s4_d58 with dissolve 
    L "What… what is this?"
    scene s4_d59 with dissolve 
    R "A spacecraft."
    R "How it ended up here, we don’t know."
    R "But that’s where the gate research started. Or so I was told."
    scene s4_d60 with dissolve 
    L "That’s it?! I thought… I thought it was just a marketing name or something…"
    L "(whispering) An actual alien ship… Someone pinch me."
    L "Wait, and you expect us to go inside? Don’t you think that’s a little… reckless?"
    scene s4_d61 with dissolve 
    R "I agree. Completely."
    R "To be honest, I know no more than you do."
    L "Wait, what? Then how-"
    scene s4_d62 with dissolve 
    aa "There’s no need to worry. We’ll explain everything, on one condition."
    aa "You cooperate."
    R "And what happens if we refuse?"
    aa "We’d really hate for something… unfortunate to happen to you."
    scene black with dissolve 
    L "(Everything we knew was kept under strict confidentiality. We were forced to sign stacks of non-disclosure agreements.)"
    stop sounds2 fadeout 5.2
    L "(Though, to be fair, those papers weren’t exactly the real guarantee.)"
    L "(The real guarantee were the guns pressed against our heads.)"
    scene s4_d64 with dissolve 
    mc "So that’s when you started calling only from your phone..."
    scene s4_d65 with dissolve 
    L "I remember how angry that made you. But I didn’t have a choice. Honestly, convincing them to even allow phone calls was already a small victory."
    scene s4_d64 with dissolve 
    mc "If you’d refused, none of this might’ve happened."
    scene s4_d65 with dissolve 
    L "I- yes. You’re right. Maybe I should’ve refused. Maybe I should have walked away..."
    L "But I couldn’t."
    scene s4_d67 with dissolve 
    h "Don’t push her. You know how much all that science crap means to her. She didn’t even realize it would turn out like this."
    play sounds2 footstep2 
    scene s4_d68 with dissolve 
    mc "Oh, so now you’re on her side?"
    play sounds3 hug2 
    scene s4_d71 with dissolve 
    h "You’re both just as important to me. And watching you tear into each other? Not exactly my idea of a good time."
    h "And come on. Don’t forget, we’ve been in her shoes before. If anyone should get how she feels, it’s you."
    scene s4_d73 with dissolve 
    mc "(If she had told us all this from the start, I wouldn’t have said a word. But now? Now it’s a different story entirely.)"
    h "(Oh, great. So now he’s playing the victim? Wow, impressive-)"
    mc "Olivia."
    mc "(Stop drilling holes in me with your eyes.)"
    scene s4_d72 with dissolve 
    h "What, [mc]?"
    scene s4_d76 with dissolve 
    mc "(No. Get a grip.)"
    scene s4_d77 with dissolve 
    mc "(sigh) Let’s just continue, alright?"

    play sounds4 systemambience loop  volume 0.1
    scene s4_dd1 with dissolve 
    L "(We spent some time aboard that ship. A month? Maybe a little less.)"
    L "(At some point, I started keeping a journal, just to keep myself sane.)"
    scene s4_dd2 with dissolve 
    L "(At first, everything seemed… manageable. We were assigned to study the gates. To understand their purpose. To figure out how to activate them.)"
    scene s4_dd3 with dissolve 
    pause 0.5
    scene s4_dd4 with dissolve 
    L "(Hour after hour. Day after day. Everything only got worse.)"
    L "(We didn’t know how to open them. And we weren’t even sure they really were gates at all.)"
    scene s4_dd5 with dissolve 
    L "(Those who broke faster… they were simply taken away.)"
    L "(Where to - no one ever told us.)"
    # 
    mc "(Those zombies… they’ve got to be connected to this somehow.)"
    

    stop music fadeout 5.4
    play music1 season4act18 fadein 25.4 volume 0.5
    scene s4_d78 with dissolve 
    h "So… how did you end up here?"
    scene s4_d79 with dissolve 
    mc "(So that recorder really was hers…)"
    mc "They found the source. The filthiest one imaginable, but they found it."
    h "(His voice… is he shaking?)"
    scene s4_d80 with dissolve 
    h "That bad?"
    h "(Alright, this is getting way too tense. Time to crack a joke.)"
    scene s4_d81 with dissolve 
    h "Why do the Ninja Turtles always attack in a group of four?"
    h "Because their teacher is a rat!"
    scene s4_d83 with dissolve 
    k "Heh. Not bad."
    h "(Yeah… not the reaction I was hoping for.)"
    scene s4_d84 with dissolve 
    h "So what’s this mysterious energy source everyone’s freaking out about?"
    scene s4_d85 with dissolve 
    Mi "Blood. More precisely, the life carried inside it."
    h "..."
    scene s4_d88 with dissolve 
    h "What?"
    mc "(They aren’t burning the blood itself. They’re extracting the life energy carried within it.)"
    scene s4_d86 with dissolve 
    mc "Disgusting, isn’t it?"
    scene s4_d89 with dissolve 
    h "That’s… yeah. Wow."
    h "Wait. Is that why there’s a bloodbath in the streets right now?"
    mc "Yes. Every death gives the system more of it."
    h "For what?"
    scene s4_d89 with dissolve 
    mc "I don’t know… But that’s not the point right now."
    mc "So what happened next? I get how you ended up here, more or less."
    scene s4_d70 with dissolve 
    mc "Astoria and Ember opened the gate and led the survivors in."
    mc "What interests me is the reason. How?"


    play sounds1 generator loop volume 0.2 
    scene s4_dd6 with dissolve 
    L "(The reason? Should I really say it as it was, or-)"
    L "It wasn’t exactly like that. The gates… didn’t open the way they were supposed to." 
    scene s4_dd7 with dissolve 
    L "(No, Lora. Say it. All of it. They need to know. He needs to know.)"
    L "They pulled me somewhere else entirely."
    stop sounds1 fadeout 2.2 
    scene black with dissolve 
    L "The Abyss."
    stop sounds4 fadeout 2.2 

    scene s4_d90 with dissolve 
    mc "(Wait, what?)"
    mc "So you were in the Abyss? But how?"
    scene s4_d91 with dissolve 
    Mi "It’s…"
    k "(whistling) Well damn… now that’s a revelation."
    play sounds3 mmove 
    scene s4_d92 with dissolve 
    h "Hey, hey, hold on. Can someone explain to me where that reaction even came from?"
    scene s4_d94 with dissolve 
    k "You ruined the whole mood. Absolutely butchered the scene."
    scene s4_d96 with dissolve 
    h "Then maybe enlighten me, what kind of abyss is this supposed to be? So I’m not completely out of the loop."
    scene s4_d97 with dissolve
    k "No light, no darkness. Just the Abyss, lurking in the shadows. No time to run. No sound to scream."
    k "That little rhyme’s been floating around for ages."
    k "Or, even simpler, picture a black screen in front of you. And here we are, welcome to the Abyss."
    scene s4_d98 with dissolve
    Mi "That’s an oversimplification… but in plain terms, yes. That’s it."
    h "Mm-hm. Interesting. If there’s nothing there… then how the hell do you get out?"
    play sounds3 clothess  
    scene s4_d95 with dissolve
    k "Ding-ding, we’ve got a winner. You don’t."
    k "That’s exactly why her story’s so damn intriguing."
    scene s4_d99 with dissolve
    mc "(And still, that place, the one the younger sister of Astoria stood in, I remember every detail I saw there.)"
    scene s4_d100 with dissolve
    mc "If no one’s ever been in the Abyss, then where did the rumor even come from?"
    play sounds3 mmove 
    scene s4_d101 with dissolve
    k "That’s… actually a good question. Where did it come from?"
    k "Huh. Never really thought about it."
    scene s4_d102 with dissolve
    Mi "People like to gossip about things they don’t understand."
    Mi "For most of them, the Abyss is nothing more than a myth."
    scene s4_d103 with dissolve
    k "Yeah. Pretty much."
    h "A myth? You hear that, [mc]? So what now… we’re mythbusters? Ha!"
    scene s4_d104 with dissolve
    pause 0.6
    scene s4_d105 with dissolve
    mc "(Chuckle) Guess so."
    mc "Time to find out what that myth is hiding. Lora?"

    play sounds3 desertwind loop volume 0.4
    scene black with dissolve 
    scene s4_d130 with dissolve 
    L "(Endless scorched plains. No animals. No plants. Nothing. Just dust.)"
    scene s4_d131 with dissolve 
    L "(I never saw a sun. No star. No source of light. Yet something, or someone, was lighting my path.)"
    scene s4_d132 with dissolve 
    L "(I wandered that place for hours. Maybe longer. Searching for an exit. No success. At some point, I caught myself thinking-)"
    L "(If I don’t find a way out… how am I supposed to survive here? That’s when the panic started.)"
    L "(I tried to fight it. Talk myself out of it. Convince myself it wasn’t real.)"
    play sounds1 punch1 
    scene s4_d133 with vpunch 
    L "(Didn’t help much. Cold. Hunger. Panic. Exhaustion. That was my constant state.)"
    scene s4_d134 with dissolve 
    L "(It kept pressing down on me. Slowly. At first, all I wanted was to go home. Later… I just wanted it to end.)"
    scene s4_d135 with dissolve 
    L "(But you… and Norman. You gave me strength. Enough to keep moving.)"
    scene s4_d136 with dissolve 
    L "(Funny thing is - hunger barely affected my body. I felt it, sure. It was unpleasant. But that was all.)"
    L "(Honestly, I don’t know how long I stayed there. But to me… it felt like an eternity.)"
    scene s4_d137 with dissolve 
    L "(Thirst. Labored breathing. Complete exhaustion.)"
    L "(And then my body just gave up.)"
    L "(No strength to move. No will. Nothing.)"
    scene s4_d138 with dissolve 
    pause 0.6
    scene s4_d139 with dissolve 
    L "(The end.)"
    scene s4_d140 with dissolve 
    pause 0.6
    scene s4_d141 with dissolve 
    pause 0.6
    scene s4_d142 with dissolve 
    L "(Or so I thought.)"
    L "(When I opened my eyes again… I was back where it all began.)"
    scene s4_d131 with dissolve 
    L "..."
    stop sounds3 fadeout 1.1

    mc "(This…)"
    play sounds2 hug2  
    play sounds1 whoosh 
    scene s4_d106 with CropMove(time=0.1, mode='slideright')
    h "INSANITY! Get over here, you, you massive asshole! Why, tell me WHY you didn’t say this from the start?!"
    h "Why did you keep all of this to yourself?!"
    scene s4_d107 with dissolve
    L "Compared to what came after… that was nothing."
    scene s4_d108 with dissolve
    mc "(I… I don’t even know what to feel anymore. What to think…)"
    scene s4_d76 with dissolve 
    mc "(While I was worrying about her, raging at her, blaming her… she was surviving. Literally surviving.)"
    mc "(And still, a part of me wants to tear myself apart, why didn’t she tell me from the start?)"
    scene s4_d77 with dissolve 
    mc "Why didn’t you tell me the truth? From the very beginning, why?"
    mc "You think I would’ve treated you differently because of this? You think I would’ve-"
    scene s4_d109 with dissolve 
    L "No. That wasn’t the reason."
    scene s4_d108 with dissolve 
    Mi "Tell me… how did you find the place? When there was nothing around you at all?"

    play sounds3 desertwind loop volume 0.4
    scene black with dissolve 
    L "..."
    scene s4_d143 with dissolve 
    L "(It didn’t happen right away.)"
    L "(On the fourth attempt, I noticed something in the distance. What exactly it was, I still don’t know.)"
    scene s4_d144 with dissolve 
    L "(Not then. Not now. But it became my reference point.)"
    play sounds1 footstep2 
    scene s4_d145 with dissolve 
    L "(I started moving toward it, thinking it was the way out.)"
    L "(But every time I blacked out, reset. Back to the beginning.)"
    scene s4_d146 with dissolve 
    L "(I tried. I fought. I searched for a way to break that limit.)"
    scene s4_d147 with dissolve 
    L "(I stayed awake as long as I could.)"
    L "(Tried different paths.)"
    L "(Tried doing nothing at all.)"
    L "(Tried… anything.)"
    scene s4_d148 with dissolve 
    L "(Anything at all.)"
    L "(Until I heard a voice. Her voice.)"
    play sounds1 footstep3
    scene s4_d149 with dissolve 
    L "(Suddenly, she was standing in front of me.)"
    L "(Red eyes. White, silky hair. A dress. And a gentle smile.)"
    scene s4_d150 with dissolve 
    L "(Astoria’s younger sister. Evrelia.)"
    L "(She didn’t say a word. Just stood there. Watching me.)"
    scene s4_d151 with dissolve 
    L "(I tried to talk to her. Asked who she was. Where we were.)"
    L "(Silence.)"
    L "(And yet… in her gaze, in that smile, I felt something strange.)"
    L "(Warmth.)"
    L "(For the first time… I felt something.)"
    play sounds3 mmove 
    scene s4_d153 with dissolve 
    L "(Something that made me stop wanting to scream from pain and regret.)"
    scene s4_d154 with dissolve 
    L "(And so… together with her, I walked toward that reference point.)"

    stop sounds3 fadeout 0.2 
    play sounds1 whoosh 
    scene s4_d110 with CropMove(time=0.1, mode='slideright')
    k "Hm… Evrelia? You’re sure it was really her?"
    scene s4_d111 with dissolve 
    mc "What’s with that tone? Something wrong?"
    scene s4_d112 with dissolve 
    k "Yeah. Your description matches her scarily well. Except for one thing, a gentle smile?"
    k "You were in your right mind back then, right?"
    h "Rude. You know that, right?"
    scene s4_d114 with dissolve 
    Mi "But she’s not wrong."
    Mi "Most people know the Lady’s younger sister as a tyrant… with a cold heart."
    Mi "A gentle smile was never something people associated with her name."
    scene s4_d115 with dissolve 
    mc "You said the same thing about the Abyss, and look how that turned out."
    play sounds1 swordswing
    scene s4_d116 with dissolve 
    k "Don’t butt in, sweetheart. We’re still not sure whether that was the Abyss…"
    k "or just your little wife having a vivid hallucination."
    scene s4_d117 with dissolve 
    mc "You’re saying she’s lying?"
    scene s4_d116 with dissolve 
    k "Could be."
    k "Still, there’s a grain of truth in what she said."
    scene s4_d117 with dissolve 
    mc "Can you confirm that claim?"
    scene s4_d118 with dissolve 
    k "Nope."
    scene s4_d76 with dissolve
    mc "(Honestly, that last bit about this… Evrélia? Hard to swallow.)"
    mc "(But judging by her description, and what I saw in that dream, everything lines up so far.)"
    mc "You’re surprisingly calm and quiet, are you okay?"
    scene s4_d109 with dissolve 
    L "I’m telling it exactly as it is. Whether they believe me or not is their choice."
    L "I can’t, and won’t, try to convince them."
    L "(whispering) In the end… I can understand them."

    play sounds3 desertwind loop volume 0.4
    scene s4_d155 with dissolve 
    L "(We walked together, day after day.)" 
    L "(Maybe because of everything I’d been through, my senses dulled, I barely felt hunger or cold.)"
    L "(Or maybe… she had something to do with it.)"
    L "(Either way, I didn’t dig into it.)"
    scene s4_d156 with dissolve 
    L "(The picture started to come together.)"
    L "(I began to see outlines, towers, mechanisms, structures.)"
    L "(Asking myself what it all was, I foolishly decided to ask her instead.)"
    L "(I had nothing to lose.)"
    L "(And then-)"
    scene s4_d158 with dissolve 
    Evrel "Tell me… why are you here?"
    scene s4_d157 with dissolve 
    L "(Her voice sounded like a melody. Every word, like a note.)"
    scene s4_d161 with dissolve 
    L "I… don’t know the true reason myself."
    L "I was simply pulled into this place."
    L "(She only smiled in response.)"
    scene s4_d162 with dissolve 
    Evrel "From the moment you appeared here, I’ve been watching you. Seeing you. Feeling you."
    Evrel "You have a pure heart."
    scene s4_d163 with dissolve 
    L "Uh- thank you? Sorry, this might be awkward, but… what should I call you?"
    scene s4_d164 with dissolve 
    Evrel "Evrelia."
    scene s4_d165 with dissolve 
    L "My name is Lora. It’s nice to meet you."
    L "But may I ask, what is this place?"
    scene s4_d167 with dissolve 
    Evrel "This place? It has many names."
    Evrel "Some call it the Abyss. Others, a tomb."
    Evrel "Some, the ruins of an empire."
    Evrel "But to me… this is home."
    scene s4_d166 with dissolve 
    L "But… what are you doing here?"
    scene s4_d168 with dissolve 
    pause 2.1
    scene s4_d169 with dissolve 
    Evrel "Before you came, I thought. I dreamed. After that… I watched."
    Evrel "Tell me, do you like this place?"
    scene s4_d170 with dissolve 
    L "I’m sorry, but it’s dark here."
    L "Dry. Cold. Gray."
    L "I understand this is your home, but still…"
    scene s4_d171 with dissolve 
    Evrel "It really is…"
    scene s4_d172 with dissolve 
    pause 0.5
    scene s4_d173 with dissolve 
    pause 0.5
    scene s4_d174 with dissolve 
    L "(After that, a snap of her fingers, and I froze.)"
    L "(The world that once felt dead and hollow turned into a living garden.)"
    L "(Ruins became towering buildings.)"
    L "(Dust became people.)"
    L "(All of it, with a single snap.)"
    L "(But the most disturbing part…)"
    scene s4_d175 with dissolve 
    Evrel "Does it feel familiar?"
    L "(In that moment, I realized-)"
    L "(All this time… I had been on Earth.)"
    stop sounds3 fadeout 2.2

#
    $ persistent.abyss_screen_ = True
    $ persistent.gate_screen_ = True
    play sounds1 whoosh 
    stop music1 fadeout 15.2 
    play music season4act12 fadein 15.4 
    scene s4_d123 with CropMove(time=0.1, mode='slideright')
    show memoryreboot with dissolve 
    b "WHAT?!"
    scene s4_d124 with dissolve 
    k "..."
    scene s4_d125 with dissolve 
    h "Okay… yeah. This is definitely not what I was expecting."
    scene s4_d127 with dissolve 
    mc "But I don’t get it. What was the point of all this? Why the whole damn show?"
    scene s4_d126 with dissolve 
    Mi "So the ancient empire was on Earth…?"
    Mi "Unthinkable…"
    scene s4_d127 with dissolve 
    mc "And you’re surprised? Shouldn’t you already know this?"
    scene s4_d128 with dissolve 
    L "This is something no one knows. Except Astoria… and me."
    scene s4_d129 with dissolve 
    k "So that’s why she treats you so special. Interesting."
    k "And what about the sister?"
    L "She doesn’t know."
    scene s4_d176 with dissolve 
    h "Alright, we cleared that up, but you still didn’t say why they’re hunting you. What’s the point of all this?"
    scene s4_d177 with dissolve 
    k "Seriously? I thought I was the dumbest one here. Turns out, I was wrong."
    scene s4_d178 with dissolve 
    h "You looking for trouble?"
    scene s4_d179 with dissolve 
    k "Oh, me? Picking a fight? Trust me, if I were, you’d already be on the floor."
    k "This? Just friendly banter."
    h "Then do us all a favor and explain what’s actually going on. See, not everyone here is a genius who spent their whole life swimming in this shit."
    h "Sometimes people need things spelled out. You know. Slowly. Okay? Now shut-"
    k "Pfft… poor thing. Aww, did I hurt your feelings?"
    play sounds2 mmove 
    scene s4_d180 with dissolve 
    mc "You two, enough."
    mc "Right now, we’re a team. Tearing each other’s throats out isn’t exactly helping."
    scene s4_d181 with dissolve 
    mc "Afterward, do whatever the hell you want, but for now, try to get along."
    scene s4_d182 with dissolve 
    mc "Are we clear?"
    scene s4_d183 with dissolve 
    h "Yeah."
    scene s4_d184 with dissolve 
    mc "Kalestra?"
    k "..."
    mc "Don’t start."
    play sounds2 mmove 
    scene s4_d185 with dissolve 
    k "Yeah, yeah. I’ll do everything within my power. Or something like that."
    play sounds3 clothess 
    scene s4_d186 with dissolve 
    k "And on that lovely note, I’ll be quiet as a fish till the meeting’s over."
    scene s4_d187 with dissolve 
    h "(whispering) Short, I get it, hurts, but fair. But stupid? Coming from her, of all people? That’s bullshit."
    play sounds2 footstep2 
    scene s4_d188 with dissolve 
    mc "(whispering) Her intentions were good."
    h "(whispering) Doubt it."
    scene s4_d189 with dissolve 
    mc "(whispering) Don’t take it to heart. I know you’re smart, stubborn too."
    h "(This…)"
    scene s4_d190 with dissolve 
    h "(He- he called me smart! No, stop. Get a grip, you’re smiling like an idiot…)"
    h "(But damn… that’s the first compliment from him in ages. Hell yeah.)"
    play sounds2 mmove 
    play sounds3 footstep2 
    scene s4_d191 with dissolve 
    mc "So, forgive the little spectacle."
    mc "Now… tell me. Why are they hunting Lora?"
    scene s4_d192 with dissolve 
    Mi "With that knowledge, she can tune the gate to the Aby-" 
    Mi "to Earth. To the range where the second part is hidden." 
    Mi "That alone makes her the primary target for everyone."
    scene s4_d193 with dissolve 
    h "Nothing new. Looks like information is valuable everywhere."
    play sounds2 mmove 
    scene s4_d194 with dissolve 
    h "(But after all these revelations… I feel like crap. Like, genuinely awful.)"
    h "(Especially since I have no idea how I’m even supposed to react to this.)"
    scene s4_d195 with dissolve 
    h "(Do I joke it off? Keep a straight face? Or just let it sink me?)"
    h "(Judging by everyone else, and the vibe in the room, I’m afraid the confessions aren’t over yet.)"
    mc "And the second reason?"
    scene s4_d196 with dissolve 
    Mi "She-"
    play sounds2 mmove 
    scene s4_d197 with dissolve 
    L "(Should I…? This moment, it could make him hate me.)"
    L "(And yet…)"
    scene s4_d198 with dissolve 
    L "Miriel, I…"
    L "(And still, this is the first time I truly don’t know what will happen next.)"
    scene s4_d199 with dissolve 
    L "In a sense… I can control time. By changing the future."
    stop music fadeout 5.4  
    play music1 season4act12 fadein 5.4 
    play sounds2 mmove 
    scene s4_d200 with dissolve 
    mc "What… does that mean, Lora?"
    mc "(This a joke? Lora, please… tell me you’re joking. Tell me Norman’s death, my fate-)"
    play sounds2 mmove 
    scene s4_d201 with dissolve 
    mc "So you knew everything that was going to happen to us?!"
    scene s4_d202 with dissolve 
    mc "Then why did you still go there? Why did you-"
    scene s4_d203 with dissolve 
    L "In the Abyss, I gained what others would call immortality. In reality, it’s a resurrection point."
    L "I can’t choose the moment."
    L "I can’t truly change anything."
    L "I tried to end it in a way where both of you survived."
    L "Where you both lived long, happy lives."
    scene s4_d204 with dissolve 
    L "And unfortunately… in that version of your lives-"
    L "I wasn’t there."
    mc "(I… nothing. Completely empty. I don’t even know what I’m supposed to feel.)"
    mc "That’s cruel."
    scene s4_d206 with dissolve 
    mc "Tell me, Lora-" 
    mc "Who gave you the right to decide what my life should be?"
    scene s4_d207 with dissolve 
    mc "(And here you are shouting… but deep down, you’re not angry at her-)"
    mc "Better short and happy than long and… pathetic."
    scene s4_d208 with dissolve 
    mc "(You’re angry at yourself, at your own helplessness.)"
    play sounds3 clothess 
    scene s4_d209 with dissolve 
    L "In another timeline, you and I already talked about this."
    L "And… yes. You’re right."
    play sounds2 maninhalingbreath
    scene s4_d210 with dissolve 
    L "But if our fates were reversed-"
    L "Tell me… would you have done it differently?"
    mc "(You know exactly why she did it. Because you would’ve done the same damn thing.)"
    scene s4_d211 with dissolve 
    mc "I-"
    mc "No. I wouldn’t have been able to."
    scene s4_d212 with dissolve 
    k "..."
    k "(That… didn’t sit right with me.)"
    scene s4_d213 with dissolve 
    k "(The hell? What kind of nonsense is that? Why would I even care?)"
    k "Hmpf..."
    scene s4_d214 with dissolve 
    mc "(And that’s why it hurts, because she lived what should’ve been yours.)"
    play sounds3 mmove 
    scene s4_d215 with dissolve 
    L "That’s exactly why…"
    L "I’m asking you to forgive me for it."
    scene s4_d216 with dissolve 
    mc "(So what am I supposed to do now…?)"
    menu:
        "Forgive.":
            play sounds3 clothess
            scene s4_d217 with dissolve 
            mc "(Looking at yourself from the outside… yeah. You’re disgusting.)"
            mc "(Sitting here, crying like a little girl, debating forgiveness-)"
            mc "(while doing absolutely nothing yourself.)"
            $ lora_relationship += 2
            


        "Don't forgive.":
            play sounds3 clothess
            scene s4_d217 with dissolve 
            mc "(Forgive her? But can I…? Too much time has passed.)"
            mc "(And even if I did, could we really live like before? I doubt it.)"
            scene s4_d219 with dissolve 
            mc "Part of me wants to forgive you, Lora. But the other part-"
            mc "I’m trying. I really am. But… I can’t."
            $ lora_relationship -= 2


    play sounds2 footstep2  
    scene s4_d220 with dissolve 
    h "You know… it actually hurts to watch this. And the thought that my whole life’s already been decided? That makes it even worse."
    play sounds3 clothess
    scene s4_d221 with dissolve 
    h "But why tell us all this now? Why not sooner?"
    play sounds2 mmove 
    scene s4_d223 with dissolve 
    h "I seriously doubt it’s because of that gorilla’s sister."
    scene s4_d225 with dissolve 
    k "I can hear you, shorty."
    h "..."
    if lora_relationship >= 2:
        play sounds3 mmove 
        scene s4_d226 with dissolve 
        mc "(She had her reasons. And… in the end, I understand why she did it.)"
        mc "(Yes, she abandoned everything, but was it truly her choice?)"
        play sounds2 footstep2 
        scene s4_d232 with dissolve 
        L "What are you-"
        play sounds3 mmove 
        scene s4_d233 with dissolve 
        mc "(Blaming her for that? Ridiculous.)"
        mc "(Some would call this foolish. Naive.)"
        mc "(But she’s the reason I set out on this journey in the first place.)"
        scene s4_d235 with dissolve 
        mc "(All of us had our ups and downs. Watching everyone along the way, everyone grew.)"
        mc "(Everyone… except me.)"
        mc "(How many times were decisions made for me? How often did I just stand there, powerless?)"
        play sounds3 clothess
        scene s4_d236 with dissolve 
        mc "(But I’m not powerless. I have a choice.)"
        mc "(And this, this is my chance.)"
        mc "(I can’t change the past.)"
        mc "(But I can shape the future.)"
        scene s4_d239 with dissolve 
        k "What kind of cheap melodrama are they putting on now..."
        k "Makes me sick just watching."
        scene s4_d240 with dissolve 
        Mi "I’m glad to see them like this."
        Mi "They value each other more than anything. It reminds me of home…"
        scene s4_d239 with dissolve 
        k "Yeah, sure. A relationship built on lies."
        k "That’s hilarious."
        scene s4_d240 with dissolve 
        Mi "You’re just jealous of them."
        k "..."
        scene s4_d241 with dissolve 
        mc "Why are you two just standing there?"
        h "We’re a team, aren’t we?"
        h "(whispering) Even that gorilla..."
        scene s4_d242 with dissolve 
        b "..."
        play sounds2 hug2 
        scene s4_d243 with dissolve 
        mc "(I didn’t want to return to that old life. I really didn’t.)"
        mc "(But their lives depend on my decisions.)"
        mc "(I won’t let them down.)"


    else:
    
        scene s4_d226 with dissolve 
        mc "(That doesn’t mean I’ll let her mistakes destroy us.)"
        mc "(The team comes first. I won’t let them suffer because of my choice.)"
        scene s4_d227 with dissolve 
        mc "(I can’t just forget the pain and pretend everything’s fine.)"
        mc "(No… it’s better to leave everything between us in the past.)"
        scene s4_d228 with dissolve 
        mc "I tried. I really did."
        mc "But I can’t forgive you."
        mc "And in the end… I’m no better."
        scene s4_d229 with dissolve 
        L "(So that’s it? It’s over… between us?)"
        L "(No, Lora. Breathe. You knew it could end like this.)"
        scene s4_d230 with dissolve 
        L "Alright, love. If that’s your choice… I’ll accept it."
        scene s4_d229 with dissolve 
        mc "(Please, don’t look at me like that. Don’t turn me into the villain.)"
        mc "Let’s move. We’ve got things to discuss."
        scene s4_d231 with dissolve 
        L "Yes, and…"
        L "I’m sorry."
        
    scene black with dissolve 
    pause 3.4
    
    "Minutes later, in pairs."
    "Silence swallowed the room, thick and heavy, pressing down on everyone like it had weight you could feel."
    scene s4_d76 with dissolve 
    show act4_s9
    mc "(That was a hard performance. But it was necessary.)"
    hide act4_s9 with dissolve 
    mc "(The situation is clearer now than it was before. That’s a plus.)"
    scene s4_d79 with dissolve 
    mc "(The weight of it, though, that’s the real cost.)"
    mc "(We’re carrying problems on a galactic scale.)"
    scene s4_d78 with dissolve 
    h "So… Astoria isn’t acting because she wants her sister back?"
    Mi "Seems like it is."
    scene s4_d80 with dissolve 
    h "Then what the hell was all this circus for?! Why drag us into this, WHY KILL SO MANY PEOPLE?!"
    h "For a sister?! That’s just-"
    pause 1.1
    scene s4_d79 with dissolve 
    h "(But if I were in her place… would I really do it any differently?)"
    h "Argh… this is heavy."
    scene s4_d111 with dissolve 
    mc "We have no reason to blame her. Yes, the situation is fucked. That’s a fact."
    mc "But we move forward with what we have. First priority, survive."
    scene s4_d77 with dissolve 
    mc "Then we go home."
    mc "Everyone on board?"
    scene s4_d128 with dissolve 
    E "The squad nodded in unison."
    a "I hate to interrupt, but we’ll arrive in twenty minutes."
    stop music1 fadeout 4.5
    scene black with dissolve 
    mc "Good. Then it’s time to put the puzzle together."
    pause 2.2

    $ persistent.chapter_act4_scene += 1

    


    scene black with dissolve
    pause 5.2
    show act4s2 with dissolve
    pause 1.5
    show act4s2_1 with dissolve
    pause 2.1
    scene black with dissolve
    pause 1.2

    
    


##Сцена четвертая что дальше?
label story05_5:


    stop music1 fadeout 4.5

    image s4_video_2 = Movie(channel="movie_dp", loop = False, play="video/s4/s4_video_2.webm")
    show s4_video_2 with dissolve
    $ renpy.pause(19.2, hard=True)
    play sounds2 ha
    scene s4_f2 with dreamyzoom 
    show act4_s10 
    mc "Our objective is what’s inside the tower."
    hide act4_s10 with dissolve 
    mc "A gate to Earth."
    mc "We stop the summoning of Evrelia-"
    L "We’ll make it out alive."
    scene s4_f3 with dissolve
    mc "In twenty minutes, this ship at full speed crashes into the tower."
    mc "That gives us the window we need to punch through the defenses and get inside."
    scene s4_f4 with dissolve
    mc "We don’t know the exact situation inside the tower."
    mc "First priority, find out what the hell is going on."
    k "Breaking in by force?"
    k "Yeah, no. Might as well shoot myself in the head, better odds of surviving."
    mc "We’re all going to die someday."
    mc "Just not today."
    play sounds2 mmove 
    scene s4_f5 with dissolve
    show act4_s11
    L "I can get you through, I know enough holes in your security."
    hide act4_s11 with dissolve 
    k "..."
    scene s4_f6 with dissolve
    mc "From there on, enemy or ally, we won’t know."
    mc "Killing everyone isn’t rational."
    mc "Avoid casualties whenever possible."
    h "And if avoiding it isn’t an option?"
    play sounds2 swordswing
    scene s4_f7 with dissolve
    mc "Neutralize them."
    mc "Your life comes first."
    h "Can’t say I’m thrilled."
    play sounds2 scar1 
    pause 0.5
    play sounds3 hdshot
    play sounds1 katahit 
    scene s4_f8 with dissolve
    mc "If hiding in a corner were an option, I’d already be there."
    Mi "What about communications?"
    play sounds2 mmove 
    scene s4_f9 with dissolve
    mc "That’s our main problem. We can’t move as a large group, too visible."
    mc "But splitting up is even worse without communication."
    play sounds3 clothess  
    scene s4_f10 with dissolve
    Mi "So… we move together?"
    scene s4_f11 with dissolve
    mc "We don’t have a choice."
    Mi "Alright."
    mc "Lora. The gate, what do we know?"
    scene s4_f12 with dissolve
    L "The tower’s core. Sublevel thirty-two." 
    L "Once it activates, everything on this planet turns into energy."
    mc "How do we get there?"
    L "The gate needs cooling, we’ll swim along the coolant line."
    play sounds2 mmove 
    scene s4_f14 with dissolve
    h "Swim through it?!"
    L "Yes. A water reservoir, big enough to swim through, and the fastest way."
    play sounds3 jumpkalesta 
    scene s4_f15 with dissolve
    mc "Time is against us."
    mc "Every minute is death."
    mc "Every death brings the end closer."
    L "According to my calculations, we have enough time. If nothing changes, everything goes smoothly."
    Mi "In numbers?"
    scene s4_f16 with dissolve
    show act4_s12
    L "Two days."
    hide act4_s12 with dissolve
    h "Not exactly a lot of time."
    mc "Right now, Flora should be engaging the enemy’s main forces."
    scene s4_f1 with dissolve
    h "But what if the Gate is already active?"
    mc "..."
    L "Then we’d already be gone."
    scene s4_f3 with dissolve
    L "We follow my plan. Exactly."
    mc "Why?"
    scene s4_f4 with dissolve
    L "Better odds… of getting a new ending."
    k "I don’t like it when my life gets called an ‘ending.’"
    pause 0.7
    mc "You said you didn’t know where this path would lead."
    L "No, but I know how the other paths end."
    scene s4_f2 with dissolve
    mc "With all due respect, darling- I can’t agree to that."
    L "..."
    h "That might actually be useful."
    a "3 minutes."
    scene s4_f3 with dissolve
    mc "(Sigh) Fine."
    mc "All paths. All outcomes."
    scene s4_f4 with dissolve
    mc "I want everything."
    L "Alright, darling."
    mc "We don’t get a second chance."


    stop music fadeout 3.4 
    stop sounds fadeout 0.5
    scene black with dissolve 
    "Cryo-Cooling Reservoir."
    play sounds2 underwateer 
    pause 2.3
    scene s4_f18 with dissolve
    play sounds factoryambience fadein 6.5 volume 0.3 loop 
    show act4_s13 
    k "Nice and warm… Hey, shorty, this what you were dreaming about?"
    play sound swimming1 volume 0.5 loop fadein 2.2
    h "I was dreaming of a proper bath. You know, clean water. Not… whatever this is."
    k "Should’ve been more careful with your wishes."
    play sounds3 mmove 
    scene s4_f19 with dissolve
    h "Screw you..."
    mc "Hold on."
    play sounds4 clench  
    scene s4_f20 with dissolve
    h "Hey, Lora? I really don’t like this whole ‘predicting my death’ thing, but still-"
    h "Was there even one successful outcome? Out of all our attempts?"
    play sounds3 mmove 
    scene s4_f21 with dissolve
    L "It’s..."
    pause 0.7
    h "Mm-hmm. Yeah, figured. Couldn’t be worse."
    L "I haven’t said anything yet."
    scene s4_f22 with dissolve
    Mi "A delay… did its job."
    h "So what, one hundred percent chance we’re walking straight to our deaths? Real suicide squad, huh."
    mc "Where did {b}I shape my own fate{/b} go?"
    mc "Or {b}I don’t believe in prophecies{/b}?"
    scene s4_f23 with dissolve
    h "Look, I don’t plan on dying. But this stuff? It really kills morale."
    mc "I can give a speech, if you want."
    h "Nah, I’ve had enough speeches for now. Thanks."
    play sounds3 mmove 
    scene s4_f24 with dissolve
    k "..."
    k "So… what are you doing?"
    play sounds4 clothess   
    scene s4_f25 with dissolve
    mc "Trying to help."
    mc "Unless you want to do it yourself?"
    k "Oh, how sweet...."
    k "Really makes me wonder, what did I do to deserve that kind of treatment?"
    play sounds2 hit1 
    scene s4_f27 with vpunch 
    pause 0.5
    play sounds3 whoosh 
    scene s4_f28 with dissolve
    pause 0.5
    scene s4_f29 with dissolve
    k "Wouldn’t happen to be because of that little talk we had, huh, [mc]?"
    mc "..."
    h "What are you talking about?"
    play sounds3 mmove 
    scene s4_f30 with dissolve
    k "Oh, nothing."
    k "Just enjoyed each other’s company."
    k "What do you call it? Blowing off some steam?"
    mc "(whispering) Why are you provoking them?"
    k "(whispering) Let me think… because it’s fun. And I kinda like watching them get jealous."
    scene s4_ff1 with dissolve
    mc "Everyone here? Let’s move."
    scene s4_ff2 with dissolve
    h "[mc]? Can I steal you for a minute…"
    mc "Did something happen?"
    h "About everything Lora said. My brain’s finally starting to catch up with it all."
    h "I get that we’re supposed to stay positive and believe we’ll pull through, but…"
    h "What if we don’t come back?"
    mc "..."
    scene s4_ff3 with dissolve
    h "The longer I think about it, the clearer it gets… I’m scared, [mc]."
    h "And yeah, my head knows I’m supposed to be brave. Strong. All that crap."
    h "But…"
    h "I’ve already caught myself regretting coming with you. More than once."
    mc "..."
    scene s4_ff4 with dissolve
    h "(What did I just…?)"
    scene s4_ff5 with dissolve
    h "No! That’s not what I meant— I mean—"
    scene s4_ff6 with dissolve
    pause 0.5
    scene s4_ff7 with dissolve
    mc "We all fear death. I’m no exception."
    mc "In this short time… I wanted to run. More times than I can count."
    scene s4_ff8 with dissolve
    h "Why didn’t you?"
    scene s4_ff7 with dissolve
    mc "Because of all of you."
    mc "Life’s a funny thing. When you’ve got nothing, you can walk straight into death without a second thought."
    mc "But once someone appears in it…"
    mc "You start fighting. Fighting for every single moment."
    scene s4_ff9 with dissolve
    h "You’re a lousy speaker…"
    mc "Hey, I was trying."
    scene s4_ff10 with dissolve
    pause 1.1
    scene s4_ff11 with dissolve
    h "You know, it’s weird… but that actually helped."
    mc "Maybe I’m not such a bad motivator after all, huh?"
    scene s4_ff12 with dissolve
    h "Oh, shut up…"
    scene s4_ff13 with dissolve
    mc "Olivia."
    scene s4_ff14 with dissolve
    h "Hm?"
    mc "Chin up."
    scene s4_ff15 with dissolve
    pause 0.7
    scene s4_ff16 with dissolve
    h "Yeah."

    stop sounds fadeout 1.5
    stop sound fadeout 1.5

    scene black with dissolve
    pause 3.2

    play sounds industryroom loop volume 0.5
    play music1 season4act19 fadein 23.2
    play sounds3 inqusitionradio volume 0.4 loop 
    scene s4_aa22 with dissolve
    show act4_s14 with dissolve 
    Fl "Twenty-Second, move to Ray’s position with the Syndicate forces, cover their rear."
    scene s4_aa21 with dissolve
    aaa "Moving out."
    a "Shaft Thirteen is online!"
    scene s4_aa23 with dissolve
    Fl "Good... just a little more..."
    stop sounds3 fadeout 3.2
    play sounds industryroom loop volume 0.5
    show s4_a86 with dissolve 
    em "(Under that kind of pressure… and she’s still giving orders.)"
    show s4_a87 with dissolve 
    em "She’ll go far."
    show s4_a85 with dissolve 
    pause 0.5
    show s4_a84 with dissolve 
    aS "You’re really not going to intervene?"
    em "Hm? I’ve already done everything I could. My people are under her command. What more does she want?"
    aS "Forgive my bluntness, but this is absurd. If we just keep standing by, this will turn into a complete failure."
    aS "And this isn’t even about faith anymore, it’s about reality."
    aS "You can’t control a crowd like that as a rookie, it’s just impossi—"
    scene s4_a88 with dissolve 
    aS "…come on. Just a little more…"
    scene s4_a89 with dissolve
    "Defeat."
    em "She’ll handle it."
    pause 0.5
    scene s4_a90 with dissolve 
    play sounds2 mmove 
    aS "..."
    aS "Why are you so fiercely against helping her?"
    scene s4_a86 with dissolve 
    aS "She’s already proven her worth, hasn’t she?"
    scene s4_a87 with dissolve 
    em "I gave my word. And I don’t break it."
    em "We are not intervening. Is that clear?"
    scene s4_a90 with dissolve 
    aS "So you’d rather sit here and watch your people get slaughtered?"
    em "..."
    scene s4_a81 with dissolve 
    Fl "(Why do innocents have to die because of people like Astoria?)"
    Fl "(Why won’t you protect them...)"
    Fl "(Why... {w=0.2}why am I so useless?!)"
    em "Are you alright? You don’t look well."
    play sounds3 mmove 
    play sounds2 spacepick2 fadein 0.2
    scene s4_aa25 with dissolve 
    Fl "(Get it together. You have to. They’ve put their lives in your hands.)"
    Fl "Ember… I need your help."
    em "(Sighs) What exactly are you offering in return?"
    play sounds3 mmove 
    scene s4_aa29 with dissolve 
    Fl "..."
    Fl "(Right. I almost forgot what kind of person she is.)"
    Fl "(I can’t betray their expectations. I won’t let all these sacrifices be for nothing.)"
    Fl "(And if I have to give up everything I have for them… then I will.)"
    scene black with dissolve
    pause 3.3
    play sounds4 radio loop volume 0.2
    o "Eastern Front, reading you."
    scene s4_aa26 with dissolve 
    o "We’ve received your distress signal. A strike team is on its way to your position."
    scene s4_aa28 with dissolve 
    Fl "(That voice…)"
    play sounds warambient2 volume 0.5 loop
    scene s4_aa30 with dissolve 
    Fl "DAD!"
    o "Flora? Sweetheart, are you alright?! Thank the gods…"
    o "I’m so glad to hear your voice."
    scene s4_aa31 with dissolve 
    Fl "I… I’m so glad to hear yours too…"
    o "Easy, dear, easy. This is an open channel, we need to shut this hell down first."
    play sounds2 c4boom volume 0.4
    scene s4_aa32 with vpunch 
    Fl "Y-yes, Father, sorry. I just—"
    aaaa "Honored to hear you, sir!"
    o "Men, you’re alive?"
    stop sounds fadeout 0.5
    stop sounds4 fadeout 0.5
    play sounds2 spacepick2 fadein 0.2
    scene s4_aa23 with dissolve 
    aaaa "Thanks to your daughter. She—"
    play sounds2 ha fadein 0.2
    scene s4_aa24 with dissolve 
    aa "The Ninth Assault Group is in trouble!"
    Fl "Anyone nearby?"
    a "Thirty-Second Group requesting further orders!"
    play sounds2 spacepick2 fadein 0.2
    scene s4_aa25 with dissolve 
    Fl "Send them to support the Ninth. They need to regroup."
    scene s4_aa31 with dissolve 
    o "Flora?"
    Fl "Yes?"
    o "You’re doing well. Really well."
    stop music1 fadeout 3.2
    scene s4_aa27 with dissolve 
    Fl "..."
    scene s4_a86 with dissolve 
    Fl "Yeah…"
    scene s4_ff47 with dissolve 
    em "(This scene...)"
    em "Tch..."
    play music mdd fadein 11.9
    play sounds2 mmove 
    play sounds3 footstep2  
    scene s4_ff48 with dissolve 
    aS "Don’t like what you see?"
    em "Let’s go."
    aS "Wait— Ember? H-hey, I’m coming!"
    
    play sounds3 footstep2  
    play sound scifidooropen2
    show s4_a96 with dissolve 
    aS "But… why didn’t you tell her?"
    show s4_a97 with dissolve 
    em "What are you talking about?"
    aS "About Lady Astoria’s message. She asked yo—"
    scene s4_a98 with dissolve 
    em "Don’t you dare."
    aS "B-but why?"
    scene s4_a99 with dissolve 
    em "I said, don’t. You. Dare."
    aS "I’m sorry..."
    em "(My patience is wearing thin. You asked me not to interfere, but my people are not endless.)"
    em "(This was supposed to end with far fewer losses.)"
    em "(What use are those lands to me if everyone on them is dead?)"
    em "(Seems even you can’t foresee everything.)"
    scene s4_a100 with dissolve 
    em "Aisha. Gather the others. It’s time to make adjustments to our plan."
    scene black with dissolve 
    aS "Right away. I’ll gather everyone."
    em "(This farce ends now. And no, one continent won’t be enough this time, Astoria.)"

    $ persistent.chapter_act4_scene += 1

label story05_6:
    stop music fadeout 3.3

    scene black with dissolve 
    pause 5.4

    play sounds towers loop volume 0.1
    play music season4act3 fadein 4.3
    scene s4_g1 with dissolve 
    show act4_s15 with dissolve 
    h "So, um… Lora? If this actually works out… will you come back with us?"
    hide act4_s15 with dissolve 
    L "Back to Earth?"
    h "Home, yeah."
    L "And why the sudden question?"
    h "I don’t know. Just got this feeling you’re not planning to come back with us. Like… you belong here more than there."
    play sounds3 mmove 
    scene s4_g3 with dissolve 
    L "If I had the chance to return, I would."
    L "But for me… it was a dream that could never come true."
    h "Hey! What about positive thinking and all that?"
    h "We’re definitely coming back! You know…"
    play sounds2 mmove 
    scene s4_g2 with dissolve 
    Mi "I wouldn’t be so sure."
    h "Hey! You’re supposed to be on our side."
    Mi "On your side… or on {b}yours{/b}?"
    h "They don’t contradict each other."
    play sounds3 mmove 
    scene s4_g3 with dissolve 
    L "You know… maybe you’re right."
    L "With everything that’s happened, I forgot how to think positively."
    mc "Never give up, huh?"
    L "Exactly."
    play sounds2 footstep2 
    scene s4_g4 with dissolve 
    h "Yo, by the way, how are your implants holding up? Because what you pulled a few hours ago was seriously messed up."
    Mi "Agreed."
    h "But hey, don’t overdo it, okay? I’ve got no clue how those things really work, but judging by Miriel—"
    scene s4_g5 with dissolve 
    mc "’m fine. Not perfect, but functional."
    mc "I’ve still got a lot to learn… but it was a worthwhile upgrade."
    mc "(Though sometimes… it feels like something’s pressing from the inside.)"
    scene s4_g6 with dissolve 
    mc "(Still, the pros outweigh the cons.)"
    L "Please, just be careful with those implants."
    L "They’re not all-powerful."
    mc "Yeah. I know…"
    stop music fadeout 0.5
    play sounds2 cinematichit3 
    play sounds3 warptravaling fadein 0.6 loop
    play music1 astoriamain fadein 1.1
    scene s4_g7 with glitch  
    a "You’re in a much better state now."
    mc "(That voice… the white mask?)"
    mc "And here I thought you were just a figment of my messed-up mind."
    scene s4_g10 with dissolve 
    a "Yes… and no. But your mind wouldn’t survive that truth right now."
    mc "(This feeling… it’s the same as with Yong and Lora…)"
    a "No one else can hear us."
    play sounds1 mmove 
    scene s4_g9 with dissolve 
    mc "Alright. Why are you here this time?"
    a "To warn you. You won’t be able to stop the gate. It’s already too late."
    mc "Then what am I supposed to do?"
    a "Accept the fact that not everyone can be saved."
    scene s4_g11 with dissolve 
    mc "And you’re so sure because… what? You’re still just something in my head."
    a "I know far more than you do."
    mc "Maybe. I won’t deny that. But that doesn’t tell {b}me{/b} anything."
    mc "So who the hell are you, really?"
    scene s4_g12 with dissolve 
    k "Keepers."
    play sounds2 whoosh  
    scene s4_g13
    a "How did you—"
    play sounds1 swordswing 
    scene s4_g14 with vpunch 
    k "(Hmph… figures.)"
    k "Trying to fill his head with your fairy-tale bullshit, huh?"
    a "I mean no harm to the one who serves as my vessel."
    k "Oh, listen to that tone. I’ve heard plenty about your kind from Evrelia. Hypocritical bastards, the lot of you."
    scene s4_g15 with dissolve 
    mc "You can see him too-"
    k "My implant feeds me everything you see, straight into my skull."
    k "And this thing felt something was off… so it crawled out of whatever hole it came from."
    play sounds1 glitchfear 
    stop sounds3 fadeout 0.5
    stop music1 fadeout 0.5
    scene s4_g16 with dissolve 
    k "(I’ll give it that, though. Ripping open a parallel reality with your own hands… Impressive.)"
    play music undertow fadein 13.3 
    play sounds1 glitchsound2 volume 0.5
    scene s4_g17 with dissolve 
    mc "Ghh!"
    h "Wh— [mc]!"
    L "My love!"
    play sounds2 fall 
    scene s4_g18 with dissolve 
    mc "(It hurts… My head’s about to… explode…)"
    L "Your body… it’s overloaded."
    scene s4_g19 with dissolve 
    k "(Why would they even put those implants in him… especially if the Mistress had already seen him?)"
    k "(On purpose? …Tch. Whatever.)"
    play sounds3 clench 
    scene s4_g20 with dissolve 
    h "What did you do to him, you gorilla?!"
    k "..."
    h "Answer me!"
    k "I saved him."
    play sounds2 clothess 
    scene s4_g21 
    k "Pointy-ears. Pills."
    h "How did you—"
    Mi "What happened to him?"
    k "Pills."
    scene s4_g22 with dissolve 
    k "Or would you rather watch him lose his damn mind?"
    play sounds2 mmove 
    scene s4_g23 with dissolve 
    pause 0.5
    scene s4_g24 with dissolve 
    pause 0.5
    play sounds3 clench 
    play sounds4 mmove 
    scene s4_g25 
    k "(Well… guess I don’t have much of a choice.)"
    scene s4_g27 with dissolve 
    k "(Then again, who am I kidding? Pissing all of you off kinda gets me going.)"
    L "..."
    h "Wh—"
    scene s4_g28 with dissolve 
    h "Mouth to mouth… hey, tell me I didn’t just imagine that. She seriously just—"
    Mi "S-she kissed him… yes…"
    L "..."
    scene s4_g29 with dissolve
    k "(We’ll have our fun later. You and me.)" 
    L "What do you think you’re doing?"
    scene s4_g30 with dissolve 
    k "(Someone’s pissed. Like, really pissed.)"
    play sounds2 mmove 
    scene s4_g33 with dissolve 
    k "You should be thanking me. For once in your life, I actually saved him."
    scene s4_g31 with dissolve 
    L "(She’s crossed the line. I need to put her back in her place.)"
    scene s4_g32 with dissolve 
    L "If you hadn’t done something so reckless, this would’ve ended far more smoothly."
    L "Stop playing with my husband’s life."
    k "Hm..."
    scene s4_g33 with dissolve 
    k "Even if that were true, what are you gonna do about it?"
    k "Try to stop me?"
    scene s4_g31 with dissolve 
    L "(She helped him, and still, I feel sick with rage.)"
    L "..."
    scene s4_g33 with dissolve 
    k "(Whispering) Just like I thought."
    L "(I’ll cleanse every trace of her filth from him. I swear I will.)"
    play sounds2 footstep2 
    stop music fadeout 4.3
    scene s4_g34 with dissolve 
    k "He’ll be back on his feet soon."
    k "But don’t get it twisted, those pills aren’t a miracle."
    k "They just push the inevitable a little further down the road."
    play sounds2 hug2 
    scene s4_g35 with dissolve 
    L "My love? How are you feeling?"
    mc "I’m fine. Let’s move-"
    mc "(Though my temples are still pounding...)"
    L "No."
    scene s4_g37 with dissolve 
    L "We’ll take a break."
    mc "Lora. We don’t have time."
    L "(No. I’m not letting this slide. I need to have a word with that psychopath.)"
    L "I don’t care. We’re stopping here. Understood?"
    L "You’re not going anywhere in that condition."
    scene s4_g35 with dissolve 
    mc "We’re a team. Other people’s decisions matter too."
    L "I—"
    h "(She’s really pissed. Not even trying to hide it.)"
    h "(Alright, Liv, stop. Why are you getting so worked up? You’re no better than her.)"
    play sounds3 mmove 
    scene s4_g36 with dissolve 
    h "Lora’s right. We should take a break."
    h "(And while we do… I need to clear something up between us.)"


    scene black with dissolve 
    h "(whispering) Can I steal you for a minute?"
    pause 2.4
    play music mallmusic fadein 3.4
    pause 3.1

    scene s4_g38 with dissolve 
    mc "Alright. What did you want to talk about?"
    h "You know… for as long as I can remember, you and Lora have always taken up a huge part of my life."
    mc "..."
    scene s4_g39 with dissolve 
    mc "Is something bothering you?"
    h "It’s not that something’s wrong, it’s just—"
    h "So much has happened. So many problems, disasters, all that crap… you get it, right?"
    mc "..."
    scene s4_g40 with dissolve 
    h "And no matter what went down, you were always there."
    h "Saving my ass. More times than I can even count."
    mc "Really? Don’t remember it that way."

    scene black with dissolve 
    "A couple of years ago"
    play sounds3 mmove 
    scene s4_g64 with dissolve 
    h "(Oh, I remember it perfectly. Like that fight, with that bitch Anya got tangled up with.)"
    h "(She was a real piece of work. There were moments I honestly thought I’d lose.)"
    scene s4_g65 with dissolve 
    h "(But even then… when my head was screaming that this was the end.)"
    mc "Right hook, right hook- YES!"
    mc "COME ON! WRECK THAT BITCH!"
    h "(Funny, right? Just words. But somehow… they gave me strength.)"
    play sounds3 punch1 
    scene s4_g66 with vpunch  
    h "(You’re the one who taught me how to stand up for myself.)"
    h "(Hell… our training sessions became something sacred to me.)"
    mc "..."
    scene s4_g67 with dissolve 
    mc "(But where are you going with this?)"
    h "(What I’m getting at is… without you, I’m not sure who I’d even be.)"
    mc "(Didn’t seem to stop you back on Earth.)"
    scene s4_g68 with dissolve 
    h "(Back then, I just ran. From everything. Telling myself I was strong and independent.)"
    mc "Olivia! That’s my girl!"
    h "(But deep down…)"
    play sounds3 hug2 
    scene s4_g69 with dissolve 
    mc "Hip-hip, hooray!"
    h "(You became the support I never asked for.)"
    scene s4_g70 with dissolve 
    h "(But desperately needed.)"
    h "(At first, I confused gratitude with something more.)"
    mc "(Liv...)"
    h "(Still… the closer we got, the more I realized, that wasn’t it.)"
    scene s4_g71 with dissolve 
    h "(whispering) Thank you, [mc]."
    h "(Yeah, yeah, I know how that probably sounds… but still.)"

    play sounds2 mmove 
    scene s4_g41 with dissolve 
    mc "And yet… here we are. Alone."
    h "..."
    h "You know, [mc]…"
    h "I’m a mess of a girl. Loud. Hot-headed. Dumb. Useless—"
    mc "No. Stop. Where did you even get that idea?"
    scene s4_g42 with dissolve 
    h "Isn’t it true though?"
    mc "Your optimism. Your experience. Your confidence. Your skills."
    h "Yeah, but compared to the others, I’m just—"
    mc "You’ve got your own kind of charm."
    play sounds2 mmove 
    scene s4_g43 with dissolve 
    mc "And if anyone tells you otherwise… I’ll knock their teeth in."
    h "Even Kalestra? She says it all the time."
    play sounds3 rustling2  
    scene s4_g44 with dissolve 
    mc "She… doesn’t mean it like that. Mostly."
    mc "That’s just how she talks. Give her time, you’ll see, she’s alright."
    play sounds2 mmove 
    scene s4_g45 with dissolve 
    h "That kiss she gave you. Right in front of Lora…"
    play sounds3 hug2  
    scene s4_g46 with dissolve 
    mc "Olivia? What are you-"
    h "I’m scared… really scared, just thinking about it."
    h "In all of this mess—"
    h "With all these girls orbiting around you…"
    scene s4_g48 with dissolve 
    h "There’s no place for me."
    scene s4_g47 with dissolve 
    pause 1.1
    scene s4_g48 with dissolve 
    h "And that… that honestly terrifies me."
    h "I get it. Lora’s your wife. And I owe her so much. Same with you—"
    h "But I just can’t…"
    stop music fadeout 3.3
    scene s4_g49 with dissolve 
    h "I can’t stay on the sidelines anymore, pretending these feelings don’t exist."
    scene s4_g50 with dissolve 
    mc "..."
    mc "(So… what do I do now?)"

label mcchoice1:

    scene s4_g50 with dissolve 
    mc "..."
    mc "(What am I supposed to do now?)"
    if lora_relationship >= 2:
        menu:
            "To remain friends.":
                scene s4_g52 with dissolve 
                mc "You did well. Really."
                mc "But I’m not the kind of man who has the right to accept feelings like that."
                scene s4_g51 with dissolve 
                mc "(I’m sorry, Liv. Truly. But this… this is for your sake.)"
                scene s4_g52 with dissolve 
                mc "I won’t abandon you."
                mc "But if we keep going, it’ll break us both."
                mc "So… distance is the only option."
                scene s4_g53 with dissolve 
                h "I… I don’t like this."
                scene s4_g74 with dissolve 
                mc "I know. I’m sorry…"
                scene s4_g75 with dissolve 
                h "Well… at least now I’m glad I finally dumped all that weight off my chest."
                scene s4_g76 with dissolve 
                h "And I’m sure I’ll start living an even better life now. You’ll see, [mc]—"
                scene s4_g77 with dissolve 
                mc "Olivia, your tears-"
                scene s4_g78 with dissolve 
                h "Huh? No— it’s not that… I—"
                scene s4_g79 with dissolve 
                h "(No, stop it. You’re strong. We’ve been over this already…)"
                scene s4_g72 with dissolve 
                "(quietly, as he hugs her)"
                h "Why… I was ready."
                scene s4_g73 with dissolve 
                h "So why can’t I let you go?!"
                "Without a word, he gently strokes her hair, while she, through laughter and tears, tries to come to terms with the storm raging in her heart."

                k "..."
                k "Tch."

                $ persistent.chapter_act4_scene += 1

                stop music fadeout 3.3



            "To let Olivia step into his life as more than just a friend.":

                play music1 season4act20 fadein 5.4 loop
                scene s4_g51 with dissolve 
                mc "(I don’t know if this is right or wrong… but seeing her like this tears me apart.)"
                mc "(And at the same time, if I go through with this, I might shatter Lora’s heart.)"
                scene s4_g52 with dissolve 
                mc "No. I can’t, Lora-"
                scene s4_g53 with dissolve 
                h "I… I have her consent."
                h "I don’t know if that changes how you—"
                scene s4_g52 with dissolve 
                mc "Are you sure?.."
                scene s4_g53 with dissolve 
                h "I want to be honest. With everyone."
                play sounds2 mmove 
                scene s4_g54 with dissolve 
                mc "(Yeah. I really might be the worst husband in existence.)"
                mc "(But the way she looked at me… something just snapped in my head.)"
                play sounds3 mmove 
                scene s4_g55 with dissolve 
                mc "(Her eyes… so much trust. So much vulnerability. I can’t just walk away from that.)"
                mc "(I don’t know if this is just a moment of weakness, but if I cross this line, I’ll have to take responsibility.)"
                play sounds2 rustling2  
                scene s4_g56 with dissolve
                mc "(What I’m doing behind Lora’s back… yet she hid the truth to protect everyone.)"
                mc "(She lied, but not out of malice.)"
                mc "(And still… looking into Olivia’s eyes like this, I can’t turn away.)"
                scene s4_g57 with dissolve 
                mc "(So should I stop now? I’ll hurt them both if I don’t.)"
                mc "(Yeah… I’m a real bastard.)"
                mc "(But having such a beautiful woman standing right in front of me—)"
                scene s4_g59 with dissolve 
                h "What’re you thinking about?"
                scene s4_g58 with dissolve 
                mc "With your hair down… you look incredible."
                mc "(After this, I’ll have to tell Lora everything.)"
                mc "(But the mission—)"
                scene s4_g59 with dissolve 
                h "You’re thinking about her right now, aren’t you?"
                h "I can tell by your eyes."
                h "You don’t know what the right thing to do is."
                scene s4_g58 with dissolve 
                mc "Sorry… Before, not knowing the reason, I could ignore it."
                mc "But now, knowing what happened, thinking about what a shitty thing I’m doing doesn’t exactly make life easier."
                scene s4_g59 with dissolve 
                h "So… what will it be?"
                h "Do you want to stop here, or—"
                menu: 
                    "Go all the way.":
                        scene s4_g58 with dissolve 
                        mc "We keep going. I’ll deal with everything else later."
                        scene s4_g57 with dissolve 
                        h "Then I’ve got an idea how to really grab your attention."
                        mc "Oh? And what would that be?"
                        play sounds2 mmove 
                        scene s4_g60 with dissolve 
                        h "Two very convincing arguments. Like them?"
                        mc "They really do look… impressive."
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
                        mc "(Her gaze cuts straight through me… I feel like I’m losing control.)"
                        mc "Olivia… may I?"
                        h "(whispering) Yes..."



                        image s4_olivia_3 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_olivia_3.webm")
                        show s4_olivia_3 with dissolve 

                        h "(These sensations… the way he fills me… the way he holds me, I just melt in his arms.)"
                        h "(And his eyes… full of passion and care…)"
                        h "(whispering) Please… don’t stop…..."
                        h "Aaahh..."
                        "A soft, tender moan slipped from her lips."
                        mc "You’re just… amazing."
                        h "I-I... ahh... ahhhh... know..."
                        h "I’m not sure..."
                        h "(Oh, I feel every movement of his, every touch.)" 
                        h "(Everything inside me is pulsing… and that look in his eyes...)"
                        h "(Care mixed with desire… I don’t want this to end.)"
                        h "(whispering) Don’t stop…"
                        mc "(I don’t know if this is right… but seeing her like this… it’s intoxicating.)"
                        mc "You’re too good…"
                        h "{b}giggles"
                        h "Aaaahh..."
                        mc "(The way she melts in my arms… that trust—)" 
                        mc "(I can’t just use her to satisfy a desire.)"
                        mc "(whispering) Does it hurt?"
                        h "MmMMMmm… no, it feels really good…"
                        h "(I feel him with every part of my body. His breathing, his heartbeat, the way he pulses inside me...)"
                        h "Aaaahhhhhh..."
                        h "(All of it together… it’s fogging my mind...)"
                        h "Please... keep going!"
                        h "Aaaahh... ahh... ahhhh..."
                        mc "Every part of you is a pleasure to look at."
                        
                        h "S-stop it, that’s embarrassing..."
                        h "And this extra weight-"
                        h "Aaahhh... "
                        mc "Since when did you start thinking so low of yourself?"
                        h "I-I..."
                        mc "Those lovely curves?"
                        mc "They’re beautiful."
                        h "Aaahh... Y-you’re lying.."
                        mc "And that stomach? Plenty of girls would envy it."
                        h "S-stop..."
                        h "(Since when do his words affect me like this?! I’m about to-)"
                        mc "You spend enough time working on your body."
                        mc "Have some confidence."
                        h "(Please stop, I’m about to pass out from pleasure...)"
                        h "This is amazing..."
                        mc "Ahhh..."
                        h "I’m… I’m at my limit, I can’t take it anymore..."
                        mc "Almost… just a little more…"
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
                        mc "Amazing… but now—"
                        h "Yeah… we should tell Lo-"
                        stop music1 fadeout 5.3 
                        scene s4_g86 with dissolve 
                        k "Wow. Seriously? At a time like this… What, the kitty decided to mark her prey?"
                        play sounds3 mmove 
                        scene s4_g88 with dissolve 
                        h "Buzz off, gorilla."
                        scene s4_g87 with dissolve 
                        k "Ohhh, did I hurt your feelings alrea-"
                        scene s4_g88 with dissolve 
                        mc "What are you doing here?"
                        play music eos3 fadein 4.4 loop
                        scene s4_g87 with dissolve 
                        k "Her moaning? Yeah, in case you’re wondering, everyone here heard exactly what you two were doing."
                        h "Wh-"
                        mc "..."
                        scene s4_g90 with dissolve 
                        k "Yeah, yeah… what do you say, one-eye? Quite the performance, huh?"
                        play sounds2 footstep2 
                        L "..."
                        scene s4_g92 with dissolve 
                        k "Hey, one-eye. What’s with the silence?"
                        scene s4_g91 with dissolve 
                        L "Shut up."
                        play sounds3 mmove 
                        scene s4_g94 with dissolve
                        mc "(She’s angry. Really, really angry…)"
                        play sounds3 mmove 
                        scene s4_g93 with dissolve
                        mc "Lora, I… I’m guilty. I admit it. No one else is to blame here but me."
                        mc "If there’s anyone you should lash out at, anyone to blame, it’s me."
                        scene s4_g94 with dissolve
                        L "So you’re not even trying to hide it anymore?"
                        mc "Would you prefer a different answer?"
                        L "..."
                        scene s4_g95 with dissolve
                        h "(I… didn’t think it would feel like this… But his care, his honesty… it made my heart melt.)"
                        scene s4_g96 with dissolve
                        k "Hey, shorty. You kinda smell like shit."
                        play sounds3 mmove 
                        scene s4_g97 with dissolve
                        h "Got a problem?"
                        scene s4_g96 with dissolve
                        k "Nah. Just sayin’."
                        scene s4_g98 with dissolve
                        mc "I could’ve refused her. Yes, that’s true. But I chose to go all the way."
                        mc "And now I’m not going to run."
                        mc "I’ll take full responsibility for what I did."
                        scene s4_g99 with dissolve
                        L "And what exactly are you going to do?"
                        scene s4_g98 with dissolve
                        mc "I’ll take care of both of you. Equally."
                        scene s4_g99 with dissolve
                        L "..."
                        L "Hypocritical."
                        scene s4_g100 with dissolve
                        mc "I know."
                        mc "But if that’s not acceptable, we can sto—"
                        play sounds3 mmove 
                        stop music fadeout 0.5
                        play music1 bxlena fadein 7.3 loop
                        play sounds2 whoosh 
                        scene s4_g101 
                        mc "(I’ll be careful… I can’t hurt them. They’re both important to me.)"
                        scene s4_g107 with dissolve
                        pause 1.1
                        scene s4_g106 with dissolve
                        L "I didn’t say no."
                        L "I don’t like the idea, but I agree."
                        L "On my terms. And you will respect them."
                        scene s4_g107 with dissolve
                        mc "Alright."
                        scene s4_g105 with dissolve
                        L "First: I personally evaluate every candidate."
                        L "Second: if she doesn’t pass, total ban."
                        
                        L "Third: seven girls. Maximum."
                        L "That’s it for now. But the rules can change at any moment."
                        L "Any problems with that?"
                        scene s4_g108 with dissolve
                        mc "No objections."
                        L "..."
                        L "So. Out of our group, have you already slept with everyone?"
                        mc "..."
                        mc "Almost."
                        L "Who’s left?"
                        if harem_end >= 2:
                            play sounds3 clothess  
                            scene s4_g104 with dissolve
                            Mi "..."
                            play sounds2 whoosh 
                            scene s4_g102 
                            h "What? Hold on, when did you manage that, gorilla?"
                            scene s4_g103 with dissolve
                            k "Couple hours before you."
                            h "..."

                            stop music1 fadeout 2.3
                            scene black with dissolve 
                            mc "Alright. We’ll deal with the rest later. For now, back to work."

                        else:

                            play sounds3 clothess  
                            scene s4_g104 with dissolve
                            Mi "..."
                            play sounds2 whoosh 
                            scene s4_g96 
                            k "You know… I wouldn’t mind turning this into a threesome."
                            scene s4_g97
                            h "In your dreams."
                            h "We’re not inviting you."


                            stop music1 fadeout 2.3
                            scene black with dissolve 
                            mc "Alright. We’ll deal with the rest later. For now, back to work."
                            

                        $ persistent.olivia_Third_scene = True

                        $ persistent.chapter_act4_scene += 1
                        

                        
    

                        

                    # "To discuss everything with Lora first.":

                    #     scene black with dissolve
                    #     "Not available yet."
                        
                    #     jump mcchoice1
    else: 
        menu:
            "To remain friends.":
                scene s4_g52 with dissolve 
                mc "You did well. Really."
                mc "But I’m not the kind of man who has the right to accept feelings like that."
                scene s4_g51 with dissolve 
                mc "(I’m sorry, Liv. Truly. But this… this is for your sake.)"
                scene s4_g52 with dissolve 
                mc "I won’t abandon you."
                mc "But if we keep going, it’ll break us both."
                mc "So… distance is the only option."
                scene s4_g53 with dissolve 
                h "I… I don’t like this."
                scene s4_g74 with dissolve 
                mc "I know. I’m sorry…"
                scene s4_g75 with dissolve 
                h "Well… at least now I’m glad I finally dumped all that weight off my chest."
                scene s4_g76 with dissolve 
                h "And I’m sure I’ll start living an even better life now. You’ll see, [mc]—"
                scene s4_g77 with dissolve 
                mc "Olivia, your tears-"
                scene s4_g78 with dissolve 
                h "Huh? No— it’s not that… I—"
                scene s4_g79 with dissolve 
                h "(No, stop it. You’re strong. We’ve been over this already…)"
                scene s4_g72 with dissolve 
                "(quietly, as he hugs her)"
                h "Why… I was ready."
                scene s4_g73 with dissolve 
                h "So why can’t I let you go?!"
                "Without a word, he gently strokes her hair, while she, through laughter and tears, tries to come to terms with the storm raging in her heart."

                k "..."
                k "Tch."

                $ persistent.chapter_act4_scene += 1

                stop music fadeout 3.3



            "To let Olivia step into his life as more than just a friend.":

                play music1 season4act20 fadein 5.4 loop
                scene s4_g51 with dissolve 
                mc "(I don’t know if this is right or wrong… but seeing her like this tears me apart.)"
                scene s4_g52 with dissolve 
                mc "Are you sure?.."
                scene s4_g53 with dissolve 
                h "Yes."
                play sounds2 mmove 
                scene s4_g54 with dissolve 
                mc "(The way she looked at me… something just snapped in my head.)"
                play sounds3 mmove 
                scene s4_g55 with dissolve 
                mc "(Her eyes… so much trust. So much vulnerability. I can’t just walk away from that.)"
                mc "(I don’t know if this is just a moment of weakness, but if I cross this line, I’ll have to take responsibility.)"
                play sounds2 rustling2  
                scene s4_g56 with dissolve
                mc "(And looking into Olivia’s eyes like this, I can’t turn away.)"
                scene s4_g57 with dissolve 
                pause 2.1
                scene s4_g59 with dissolve 
                h "What’re you thinking about?"
                scene s4_g58 with dissolve 
                mc "With your hair down… you look incredible."
                scene s4_g59 with dissolve 
                h "So… what will it be?"
                menu: 
                    "Go all the way.":
                        scene s4_g58 with dissolve 
                        mc "We keep going. I’ll deal with everything else later."
                        scene s4_g57 with dissolve 
                        h "Then I’ve got an idea how to really grab your attention."
                        mc "Oh? And what would that be?"
                        play sounds2 mmove 
                        scene s4_g60 with dissolve 
                        h "Two very convincing arguments. Like them?"
                        mc "They really do look… impressive."
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
                        mc "(Her gaze cuts straight through me… I feel like I’m losing control.)"
                        mc "Olivia… may I?"
                        h "(whispering) Yes..."



                        image s4_olivia_3 = Movie(channel="movie_dp", loop = True, play="video/s4/s4_olivia_3.webm")
                        show s4_olivia_3 with dissolve 

                        h "(These sensations… the way he fills me… the way he holds me, I just melt in his arms.)"
                        h "(And his eyes… full of passion and care…)"
                        h "(whispering) Please… don’t stop…..."
                        h "Aaahh..."
                        "A soft, tender moan slipped from her lips."
                        mc "You’re just… amazing."
                        h "I-I... ahh... ahhhh... know..."
                        h "I’m not sure..."
                        h "(Oh, I feel every movement of his, every touch.)" 
                        h "(Everything inside me is pulsing… and that look in his eyes...)"
                        h "(Care mixed with desire… I don’t want this to end.)"
                        h "(whispering) Don’t stop…"
                        mc "(I don’t know if this is right… but seeing her like this… it’s intoxicating.)"
                        mc "You’re too good…"
                        h "{b}giggles"
                        h "Aaaahh..."
                        mc "(The way she melts in my arms… that trust—)" 
                        mc "(I can’t just use her to satisfy a desire.)"
                        mc "(whispering) Does it hurt?"
                        h "MmMMMmm… no, it feels really good…"
                        h "(I feel him with every part of my body. His breathing, his heartbeat, the way he pulses inside me...)"
                        h "Aaaahhhhhh..."
                        h "(All of it together… it’s fogging my mind...)"
                        h "Please... keep going!"
                        h "Aaaahh... ahh... ahhhh..."
                        mc "Every part of you is a pleasure to look at."
                        
                        h "S-stop it, that’s embarrassing..."
                        h "And this extra weight-"
                        h "Aaahhh... "
                        mc "Since when did you start thinking so low of yourself?"
                        h "I-I..."
                        mc "Those lovely curves?"
                        mc "They’re beautiful."
                        h "Aaahh... Y-you’re lying.."
                        mc "And that stomach? Plenty of girls would envy it."
                        h "S-stop..."
                        h "(Since when do his words affect me like this?! I’m about to-)"
                        mc "You spend enough time working on your body."
                        mc "Have some confidence."
                        h "(Please stop, I’m about to pass out from pleasure...)"
                        h "This is amazing..."
                        mc "Ahhh..."
                        h "I’m… I’m at my limit, I can’t take it anymore..."
                        mc "Almost… just a little more…"
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
                        mc "Amazing…"
                        h "Yeah…"
                        scene black with dissolve
                        mc "(Whatever happens next… this moment was real.)"

                        $ persistent.olivia_Third_scene = True

                        $ persistent.chapter_act4_scene += 1

# 
label story05_7:

    play music covenant fadein 1.5
    scene black with dissolve 
    pause 0.7
    show act4_s16 with dissolve 
    pause 1.6
    scene s4_f31 with dissolve
    h "Target at eight o’clock. One-minute window."
    mc "Working on it."
    play sounds4 rustling2 
    scene s4_f32 with dissolve
    g "Hm? What was that?"
    scene s4_f33 with dissolve
    pause 2.1
    play sounds2 breakbone  
    scene s4_f34 with vpunch 
    pause 0.5
    play sounds1 rustling2
    scene s4_f35 with dissolve
    mc "Target neutralized."
    h "[mc], ten seconds!"
    play sounds3 footstep2 
    scene s4_f36 with dissolve
    h "Gotta admit, clean work."
    mc "The end justifies the means."
    mc "Access to the security room is clear."
    h "Thanks, [mc]. Gorilla, you’re up."
    scene s4_f37 with dissolve
    k "With pleasure. Though since when did you become a commander?"
    h "I can afford it. I’m the only one here who sees the whole picture."
    h "So keep it shut."
    play sounds2 glitchfear 
    scene s4_f38 with glitch 
    k "Oh yeah?"
    k "Interesting… and thanks to whom exactly did you end up there-"
    play sounds3 footstep2 
    scene s4_f39 with dissolve
    mc "Why is it so hard for you two to work together?"
    mc "Both of you, cut the circus."
    mc "Miriel. Kalestra. Inside. Now."
    k "..."
    play sounds3 footstep1
    play sounds2 mmove 
    scene s4_f40 with dissolve
    k "He’s on you."
    play sounde1 clothess 
    scene s4_f41 with dissolve
    mc "..."
    play sounds4 scar1 
    stop music fadeout 3.2
    scene black with vpunch 
    pause 2.1

    play music1 season4act21 fadein 5.4
    play sounds4 roomemptyambience1 loop fadein 1.0 volume 0.7 
    play sounds3 doorclose
    scene s4_f42 with dissolve
    mc "You’ve got thirty minutes."
    mc "Grab the data and we move."
    h "Oki!"
    Mi "Don’t you feel like things are going… a little too smoothly?"
    play sounds2 footstep2 
    scene s4_f43 with dissolve
    h "How about we don’t jinx it, huh? Everything’s going smooth, let’s keep it that way!"
    Mi "Lora… how did we die?"
    pause 1.2
    k "Can’t wait that much, huh?"
    play sounds3 radio volume 0.2 
    scene s4_f45 with dissolve
    Mi "Information is power. If we know every possible outcome, we can prepare for them."
    k "Fair enough."
    scene s4_f44 with dissolve
    h "For once, I’m actually curious too. So how does your so-called immortality work?"
    h "And just how much do you really know… what do you think, [mc]?"
    mc "..."
    mc "Lora?"
    play sounds3 keyboard
    scene s4_f46 with dissolve
    L "(Should I really tell them this? It could break them completely...)"
    L "(But watching them die again, and again...)"
    L "(No. You have to. You promised.)"
    play sounds2 ha
    scene s4_f47 with dissolve
    L "I can’t “see” the future as such. All I know are the events, in a certain order."
    L "When I live through a life, I can change its ending… but what that change leads to, I don’t know, not until I live it again."
    play sounds3 spacepick2
    scene s4_f48 with dissolve
    h "So if you already know everything, what are we doing he- oh!"
    h "You’re checking whether anything’s shifted from the previous path?"
    L "More or less. And about our deaths…"
    play sounds3 doorclose
    scene s4_f49 with dissolve
    Mi "Considering how things went up to this point… and what we faced along the way, none of it posed a real threat."
    Mi "Which means we reached our objective in most cases. So the real question is, what was waiting for us there?"
    play sounds2 mmove 
    scene s4_f50 with dissolve
    mc "Impressive."
    play sounds3 clothess 
    scene s4_f51 with dissolve
    Mi "I don’t believe that small group of soldiers could’ve stopped us."
    scene s4_f50 with dissolve
    mc "I agree."
    mc "Still, wasn’t it thanks to her information that we avoided running into them?"
    mc "And you of all people should know, underestimating the enemy gets you killed."
    Mi "..."
    scene s4_f53 with dissolve
    L "(sigh) Miriel’s right. None of that was thanks to me."
    scene s4_f52 with dissolve
    h "Hey, hey, we’re a team, remember? Where’s the team spirit?"
    h "And yeah, I’m sure this brainy one’s got a plan."
    scene s4_f54 with dissolve
    k "You’re a cutie, shorty, defending the one-eyed one like that… Should’ve learned a thing or two from her-"
    mc "Speak."
    mc "What is it you want?"
    play sounds2 clench 
    scene s4_f55 with dissolve
    pause 0.7
    play sounds3 spacepick2
    scene s4_f56 with dissolve
    L "She thinks I’m working for the enemy. And honestly, I don’t blame her."
    L "But for better or worse… I’m not."
    play sounds3 ha 
    scene s4_f57 with dissolve
    mc "You mean… who?"
    L "The Elven Empress. Selvari-"
    play sounds4 swordswing
    scene s4_f58 with dissolve
    k "You’re hiding something, darling."
    mc "Lower the blade."
    k "Don’t get involved, honey. Love you, sure, but I won’t stand for lies."
    scene s4_f59 with dissolve
    k "If you’re not on her side, why drag your feet?"
    k "All this drama with the Abyss, Evrelia… nonsense."
    scene s4_f60 with dissolve
    L "And what would be the point of lying to you?"
    scene s4_f59 with dissolve
    k "Just as much as telling us the truth."
    play sounds2 bodytap 
    scene s4_f61 with dissolve
    mc "Enough."
    mc "Whether it’s truth or lies, that’s for me to decide."
    k "Hand’s off."
    play sounds3 rustling2 
    scene s4_f62 with dissolve
    mc "..."
    k "I’m helping you outta fun, that’s it. And your wifey? She’s ruining it with her lies."
    scene s4_f63 with dissolve
    mc "(What happened to her? Where did this sudden shift come from?)"
    mc "What’s going on with y-"
    mc "Your implants…"
    k "..."
    play sounds2 footstep1 
    play sounds3 mmove 
    scene s4_f64 with dissolve
    mc "We’re all on edge right now."
    mc "I understand why you’re acting like this, and what pushed you there."
    mc "But I won’t allow you to take it out on the team."
    play sounds2 clothess 
    scene s4_f65 with dissolve
    mc "If that’s what you need, I’m willing to help you deal with it."
    mc "Are we clear?"
    play sounds1 clench 
    scene s4_f66 with dissolve
    k "..."
    play sounds2 clothess 
    scene s4_f67 with dissolve
    k "(Whisper) You’re a little gem yourself."
    pause 0.6
    play sounds2 mmove 
    scene s4_f68 with dissolve
    k "Ciao."
    mc "And where exactly are you going?"
    k "Just need some air."
    play sounds3 doorclose 
    scene s4_f69 with dissolve
    h "Implants, huh… Miriel?"
    h "So what, you gonna pump me full of those too?"
    scene s4_f70 with dissolve
    Mi "Can’t wait to walk around constantly agitated and aggressive?"
    scene s4_f71 
    pause 0.2
    scene s4_f70 
    pause 0.2
    scene s4_f71 
    pause 0.2
    scene s4_f70 
    pause 1.2
    scene s4_f71 
    pause 0.2
    scene s4_f72 with dissolve
    h "Wait, agitated? Excited?? They actually affect the body like that?"
    h "Okay, dumb question, of course they do. But why excitement, specifically?"
    scene s4_f73 
    pause 0.6
    play sounds2 mmove 
    scene s4_f74 
    pause 0.6
    scene s4_f75 with dissolve
    Mi "High blood circulation. Energy builds up… and once it reaches its limit, it needs release."
    Mi "And after that… I think you understand."
    scene s4_f69 with dissolve
    h "So she went to blow off some steam? Masturbating?"
    Mi "No. Knowing her, definitely not."
    Mi "At least not under circumstances like these."
    play sounds2 mmove 
    scene s4_f149 with dissolve 
    L "Thank you, darling."
    pause 0.5
    scene s4_f150 with dissolve 
    mc "This is your last chance. And if even this turns out to be a lie…"
    L "I know, darling. The truth, nothing but the truth."
    stop music1 fadeout 5.4
    scene s4_f151 with dissolve 
    pause 1.1

    play music mirmc fadein 4.2 
    scene s4_f135 with dreamyzoom 
    mc "Why didn’t you say this from the start?"
    scene s4_f134 with dissolve 
    L "I couldn’t. Not of my own free will. I wanted to tell you, but Astoria…"
    scene s4_f139 with dissolve 
    L "The fewer people knew, the more likely we were to fool the pattern."
    mc "The pattern?"
    scene s4_f140 with dissolve
    L "Every choice leads to another outcome."
    L "Astoria and I were trying to find the one where everyone survives."
    scene s4_f138 with dissolve 
    L "And for that… we had to keep things hidden."
    mc "(This is absurd… and I’m just supposed to believe this?)"
    mc "I’ll be honest, this sounds like complete nonsense."
    mc "But fine."
    mc "Still… if you’re telling me now, does that mean we’ve already lost the chance to choose that path?"
    L "I don’t know. This is the first time I’ve dared to do it."
    scene s4_f141 with dissolve 
    L "I get it, to everyone else, I must look horrible."
    L "A selfish, hypocritical bitch. But… I had to do it."
    scene s4_f142 with dissolve 
    mc "I…"
    mc "(What am I even supposed to do? I can barely take care of myself… let alone protect her.)"
    mc "How can I help you?"
    scene s4_f144 with dissolve 
    L "..."
    L "(He’s made it this far - even without the power I have.)"
    L "(But what if…)"
    scene s4_f145 with dissolve 
    L "(If he had it too- No. Do you really want him to suffer like that?)"
    L "(He’s suffered enough already. I have to finish this, and then, for sure-)"
    scene s4_f146 with dissolve 
    mc "Lora?"
    scene s4_f145 with dissolve 
    L "In the tower, Astoria’s opening a controlled path to Evrelia."
    L "She’s using the elves’ interests as cover, drawing attention to them."
    mc "A distraction? From whom?"
    L "From the Keepers. A higher power that keeps order in the galaxy."
    scene s4_f144 with dissolve 
    mc "So Astoria is the enemy?"
    L "No. She isn’t the enemy."
    L "Three plans are converging on the same Gate."
    mc "Three?"
    L "Astoria intends to open a narrow, controlled path to Evrelia."
    L "Selvaria intends to seize that opening."
    L "She’ll feed the Gate with the planet’s life energy and force it fully open."
    mc "And us?"
    scene s4_f143 with dissolve 
    L "We use Astoria’s window to reach the core before Selvaria takes control."
    L "I change the destination to Earth."
    L "We cross, then shut the Gate behind us."
    mc "And if you can’t rewrite it?"
    L "Then we don’t go home."
    L "We block the cooling system."
    L "That should force an emergency shutdown before Selvaria can stabilize the Gate."
    mc "So the first plan gets us out."
    mc "The second only stops them."
    L "Exactly."
    scene s4_f148 with dissolve 
    pause 1.2

    $ persistent.chapter_act4_scene += 1

    stop music fadeout 5.4
    scene s4_f151 with dissolve 
    mc "..."
    play sounds3 doorclose 

label story05_8:

    stop music fadeout 5.4

    scene black 
    pause 3.2

    play sound factoryambience loop volume 0.4 fadein 4.3 
    play music season4act13 fadein 5.4 volume 0.6
    play sounds2 footstep2 
    scene s4_f76 with dissolve
    h "What the hell happened here? The smell’s awful…"
    L "A slaughter. The Peacekeepers held as long as they could."
    L "As you can see, it wasn’t enough."
    play sounds3 walkdirt1 volume 0.7
    scene s4_f77 with dissolve
    L "Still… credit where it’s due. If it weren’t for them—"
    k "Yeah, right. If it weren’t for the rats, things might’ve gone a hell of a lot better."
    k "What’s wrong, one-eye?"
    play sounds3 walkdirt volume 0.7
    L "What are you implying?"
    Mi "(That style...)"
    scene s4_f78 with dissolve
    mc "This is not the time. Focus on the objective."
    k "Yeah, yeah…"
    play sounds3 walkdirt1 volume 0.7
    h "Yo… so behind those doors is where the real trouble starts?"
    h "Maybe-"
    Mi "(No... this can’t be.)"
    play sounds2 walkdirt volume 0.7
    scene s4_f79 with dissolve
    L "Afraid?"
    h "You’re not? I still remember my run-in with that Astoria, she tossed me around like I was nothing."
    h "And now she’s not alone. There’s two of them. Two. And they’re angry!"
    k "(So this is where they locked Evrelia up… Yeah. What a shithole.)"
    play sounds3 mmove 
    scene s4_f80 with dissolve
    k "Hey, [mc]?"
    mc "Yeah?"
    k "Can you promise me one thing?"
    k "If I lose my mind in there, shoot me."
    mc "You’ll be fi-"
    k "Promise."
    mc "..."
    mc "Alright."
    scene s4_f81 with dissolve
    mc "(Even she isn’t sure we’ll make it out alive… almost funny.)"
    mc "(We came this far, only to realize this journey might be our last.)"
    scene s4_f83 with dissolve
    mc "(No. No matter the cost, we survive. We have to.)"
    stop music fadeout 0.3
    play sounds1 cinematichit3 
    play sounds4 fall 
    scene s4_f82 with vpunch
    Mi "NO-!"
    play sounds2 whoosh 
    scene s4_f84 with CropMove(time=0.1, mode='slideleft')
    mc "Miriel?!"
    play sounds3 mmove 
    scene s4_f86 
    mc "What happened? Are you alright?"
    Mi "No... not this... not again..."
    mc "Miriel, calm down!"
    play music1 season4act22 fadein 7.2 volume 0.2
    scene s4_f85 with dissolve
    Mi "(What are they doing here?! I have to warn my teacher...)"
    play sounds2 footstep2
    scene s4_f87 with dissolve
    L "What happened to you?!"
    h "Miriel! What’s wrong with her?!"
    mc "I don’t know. She won’t respond… she’s terrified."
    k "(So they tried. And failed… That’s unsettling.)"
    scene s4_f89 with dissolve
    k "(If we don’t convince her, we’re dead. No other way around it.)"
    k "Hey, one-eye. We’ve got a problem."
    L "..."
    L "Not yet."
    play sounds2 mmove 
    scene s4_f90 with dissolve
    k "Feels like we do. There’s a Keeper’s corpse lying around. And not just one."
    L "There will be more if we don’t move."
    k "Got a plan?"
    L "Yes."
    play sounds3 mmove 
    scene s4_f91 with dissolve
    Mi "(Pull yourself together, Miriel. Pull yourself together. The Teacher entrusted you with this. You have to see it through.)"
    Mi "I can’t… I—I…"
    Mi "(Push the emotions away. Push the memories-)"
    play sounds2 bodytap 
    scene s4_f92 with dissolve
    mc "We’re with you."
    Mi "..."
    Mi "(Yes… right. I’m not alone anymore. Not alone.)"
    play sounds3 mmove 
    scene s4_f93 with dissolve
    Mi "[mc]… we have to leave. Before they arrive!"
    mc "(She’s shaking. Her voice is breaking. She’s on the verge of hysteria because of those people.)"
    scene s4_f94 with dissolve
    Mi "I don’t want to feel that pain again… I don’t want to lose you too!"
    mc "..."
    scene s4_f95 with dissolve
    Mi "I don’t want to… I don’t want to... I don’t want to…"
    play sounds3 mmove 
    scene s4_f96 with dissolve
    mc "Quiet, Miriel. We’re here."
    mc "(I’ve never seen her this scared.)"
    scene s4_f97 with dissolve
    L "Can I?"
    mc "..."
    mc "Yes."
    play sounds3 mmove 
    scene s4_f98 with dissolve
    pause 0.6
    scene s4_f99 with dissolve
    pause 0.6
    scene s4_f100 with dissolve
    mc "What are you doing?"
    scene s4_f102 with dissolve
    L "Elven ears are their most intimate spot."
    L "If you stroke them like this, they calm down."
    L "What do you say, dear?"
    scene s4_f101 with dissolve
    Mi "Mmh..."
    Mi "P-please... just not in front of him... I-I’m embarrassed..."
    L "You’re adorable."
    L "(whispering) So… did you like my husband?"
    scene s4_f103 with dissolve
    Mi "W-WHAT?! NO, I-!"
    L "In this state, she always reminds me of Mina."
    L "Makes me want to just squeeze those cheeks."
    scene s4_f104 with dissolve
    mc "(That sadistic streak of hers... give her an inch and she bares her fangs.)"
    mc "(Still, it worked. Miriel’s calmer.)"
    scene s4_f105 with dissolve
    h "(whispering) The more I watch them, the more I realize..."
    h "(whispering) You two are seriously creepy up close. Gives me chills."
    h "(whispering) And these are the ones keeping balance in the galaxy? Yeah right, more like villains."    
    play sounds3 clothess  
    scene s4_f106 with dissolve
    pause 0.6
    play sounds2 mmove 
    scene s4_f107 with dissolve
    h "(No-)"
    stop music1 fadeout 0.5
    play sounds3 hit1 
    scene s4_f108 with vpunch
    h "(No...)"
    scene s4_f109 with dissolve
    h "..."
    h "(Fell...)"
    mc "Olivia?"
    play music sneakysnitch fadein 5.4
    scene s4_f110 
    h "It wasn’t me!"
    pause 0.2
    scene s4_f111 
    pause 0.2
    scene s4_f110 
    pause 0.2
    scene s4_f111 
    pause 0.2
    scene s4_f110 with dissolve
    h "I think?"
    scene s4_f112 with dissolve
    h "I mean, who would’ve thought one little poke would knock him out cold?"
    h "What are they made of, cardboard? Why are they so damn fragile?!"
    scene s4_f113 with dissolve
    mc "Olivia. Enough."
    scene s4_f112 with dissolve
    h "I- yeah. Sorry. That one’s on me."
    play sounds3 mmove 
    scene s4_f115 with dissolve
    k "That hit sealed it, we need to move."
    k "I’m afraid her little stunt aggroed pretty much everything with a pulse."
    mc "Interesting. Where exactly are we supposed to go? We’re cornered. Lora, doors?"
    L "Sealed shut. They won’t open."
    scene s4_f116 with dissolve
    h "Yo, [mc]? I think I found a way out."
    mc "Olivia, this is not the time for jokes."
    h "No, seriously. I’m not joking. Look."
    scene s4_f117 with dissolve
    mc "..."
    mc "Any idea where it leads?"
    k "No clue. But I’m damn sure it doesn’t lead anywhere good."
    scene s4_f118 with dissolve
    h "For once, I agree with the gorilla. And I have zero desire to check what’s down there."
    scene s4_f119 with dissolve
    mc "Olivia? Remember the promise?"
    scene s4_f120 with dissolve
    h "{b}Giggle"
    scene s4_f122 with dissolve
    h "Nope. Not happening. I’m not crawling in there. No way in hell."
    play sounds3 mmove 
    play sounds2 whoosh 
    play sounds1 jumpkalesta
    stop sound fadeout 0.5
    stop music fadeout 4.4
    scene s4_f123 with dissolve
    pause 2.3

    $ persistent.chapter_act4_scene += 1
    


label story05_9:

    stop music fadeout 0.5

    scene black with dissolve 
    pause 1.2
    
    play music yongmusic2 fadein 8.2
    pause 5.4

    play sound gatebackground fadein 5.4 loop volume 0.3
    show s4_ff19 with dissolve 
    pause 0.8
    play sounds3 mmove 
    show s4_ff20 with vpunch 
    show 4yr with dissolve 
    a "Move it, you worthless trash."
    show s4_ff18 with dissolve 
    R "H-how dare you talk to me li—"
    a "You humans deserve nothing better."
    show s4_ff17 with dissolve 
    R "(So this is how you repay my work? Hypocrites!)"
    show s4_ff21 with dissolve 
    am "You really couldn’t find someone… even remotely competent?"
    show s4_ff22 with dissolve 
    sel "You do realize the Keepers have started hunting anyone tied to the tombs."
    sel "Finding someone who won’t embarrass themselves is already an accomplishment."
    show s4_ff21 with dissolve 
    am "Could have brought your own scientists, you know."
    show s4_ff24 with dissolve 
    sel "Unlike you, we consider our scientists a strategic resource."
    sel "And even if I agreed to this little ‘Abyss’ venture, I’m not throwing my own people into it."

    show s4_ff25 with dissolve 
    a "My Queen, we’ve got a problem."
    sel "What is it?"
    play sounds3 mmove 
    show s4_ff29 
    R "Then kill me already!"
    aa "Stand down."
    aa "What about the gate?"
    show s4_ff30 with dissolve 
    R "There’s a problem, I can’t activate it."
    sel "The reason? Not enough sacrifices?"
    R "No, something’s jamming them… from the other side."
    show s4_ff32 with dissolve 
    sel "You didn’t invent that excuse… simply because you don’t know how to activate them, did you?"
    show s4_ff31 with dissolve 
    R "How dare you question my intellect!"
    aa "Watch your tongue, boy."
    scene s4_ff32 with dissolve 
    sel "You have exactly one hour to fix this."
    sel "If he fails, kill him."
    show s4_ff31 with dissolve 
    R "How da—"
    a "Yes, Your Majesty."

    am "The sacrifices were never part of our agreement."
    sel "They became necessary when your clean solution stopped being sufficient."
    am "Necessary for your plan. Not mine."

    show s4_ff28 with dissolve 
    sel "Tell me, Astoria… what’s worth more: a star you can lose for the sake of the world,"
    sel "or a world where one star shines brighter than all the rest?"
    show s4_ff27 with dissolve 
    am "The star. Even a single one can set the darkness on fire." 
    am "A world without light is nothing but emptiness." 
    am "Truth is born from sacrifice. Value comes from the one you’d give everything up for."
    show s4_ff26 with dissolve 
    sel "Or perhaps… the world matters more." 
    sel "If the star goes out, life changes, but the universe continues." 
    sel "Value is measured by what preserves the system, not by a single life." 
    show s4_ff31 with dissolve 
    am "And what if the world itself is ready to abandon its star?" 
    am "Worth isn’t measured by what survives, it’s measured by who is willing to give themselves so something else can." 
    show s4_ff32 with dissolve 
    sel "Then who is more important, the one others die for, or the one who can choose to sacrifice?"
    sel "Truth lives in the choice: what you decide to protect… and what you’re willing to let go."
    show s4_ff34 with dissolve 
    am "The one people are willing to give everything for, that’s what matters." 
    am "Without them, sacrifice is nothing but strategy."
    am "Greatness is the person you’re willing to break your rules for… even if it destroys you."
    show s4_ff35 with dissolve 
    sel "And sometimes, the one who seems precious only tests who is truly willing to sacrifice." 
    sel "Worth exists in the eyes of the one who judges." 
    sel "The truth of sacrifice is seeing the pain, and walking forward anyway." 

    play sounds3 warptravaling fadein 0.6 loop volume 0.1
    show s4_ff36 with dissolve 
    am "The truth is simple: the one who makes the decision is stronger than the one who merely seems important."  
    am "And sometimes sacrifice isn’t loss at all, it’s a test of whether you can live with what follows."
    show s4_ff37 with dissolve 
    am "(But the real power lies in the one who can do the impossible… for the person they cannot afford to lose.)"  
    show s4_ff38 
    pause 0.8
    show s4_ff41 with glitch 
    am "(Sometimes the ‘rational’ choice is just a mask… hiding what has already begun inside.)"
    show s4_ff44 with dissolve 
    pause 1.2
    show s4_ff45 with dissolve 
    am "(I’ve already stepped onto this path.)"
    show s4_ff46 with dissolve 
    pause 1.2
    show s4_ff56 with dissolve 
    am "(No one will notice… not until it ends.)"
    show s4_ff41 with dissolve 
    pause 1.2
    show s4_ff42 with dissolve 
    am "(If my principles brought me to this ending…)"
    show s4_ff57 with dissolve 
    pause 1.2
    show s4_ff58 with dissolve 
    pause 1.2
    show s4_ff59 with dissolve 
    am "(What were they ever worth?)"
    show s4_ff60 with dissolve 
    pause 1.2
    play sounds3 mmove 
    show s4_ff61 with dissolve 
    am "(If a flower is meant to begin a new life…)"
    play sounds2 clench
    show s4_ff62 with dissolve 
    pause 1.2
    play sounds3 hdshot
    show s4_ff63 with vpunch  
    am "(Then I will become the soil for it.)"
    stop sounds3 fadeout 3.3
    stop music fadeout 3.3
    stop sound fadeout 3.3

    jump story05_5_1

    scene black with dissolve 
    pause 1.1
    show 6yr
    pause 1.1
    play music1 bar1 fadein 8.0
    pause 2.1
    play sounds2 heels1 
    scene s4_ff53 with dissolve 
    pause 1.6
    scene s4_ff54 with dissolve 
    pause 1.6
    scene s4_ff49 with dissolve 
    C "(A customer? At this hour?)"
    scene s4_ff50 with dissolve 
    CC "*whistles* Now that’s a big fish."
    CC "(whispering) What’s a lady like that doing in a bar this dead?"
    scene s4_ff55 with dissolve 
    CC "What can I do for you?"
    scene s4_ff52 with dissolve 
    Evrel "..."
    Evrel "I’m looking for a girl..."
    Evrel "Named Lora."

            



# 0.4.5
    
label story05_5_1:

    $ persistent.main_menu_choice = 2
    
    $ config.main_menu_music = menu_music.get(
        persistent.main_menu_choice,
        "audio/MMSong1.mp3"
    )

    $ renpy.save_persistent()

    stop music fadeout 0.5
    scene black with dissolve 
    pause 2.1
    show 0_4_5 with dissolve
    "A ventilation shaft stood just a few steps from the gate."
    play sound alivecor loop volume 0.4 fadein 4.3 
    play sounds2 waterfall 
    scene s4_5aaa1 with dissolve 
    
    mc "Status?"
    k "You can come down."
    play music elevatormus2 fadein 5.4 
    scene s4_5aaa2 with dissolve 
    pause 1.1
    play sounds2 whoosh 
    scene s4_5aaa3
    pause 1.1
    play sounds3 waterfall 
    scene s4_5aaa4 with dissolve 
    mc "So this is our bypass route?"
    mc "Smells off…"
    scene s4_5aaa5 with dissolve 
    k "Ventilation’s dead. Where exactly would clean air come from?"
    k "Not that there was any left topside either."
    scene s4_5aaa6 with dissolve 
    mc "You sure this route is safe?"
    play sounds2 mmove 
    scene s4_5aaa7 with dissolve 
    k "Safe? Pfft."
    k "As long as it’s not a dead end, good enough."
    h "Yo! How’s it looking? We coming down?"
    pause 1.1
    play sounds2 mmove 
    scene s4_5aaa8 with dissolve 
    k "Don’t overthink it. Might be a lousy option, but hey-"
    k "sharing the fate of the guys upstairs isn’t on my to-do list."
    play sounds3 clothess  
    scene s4_5aaa9 with dissolve 
    mc "Same here."
    play sounds2 mmove 
    scene s4_5aaa10 with dissolve 
    mc "Come down!"
    play sounds3 whoosh 
    scene s4_5aaa14 
    play sounds4 hug2 
    pause 1.1
    scene s4_5aaa11 with dissolve 
    pause 1.1
    h "..."
    scene s4_5aaa12 with dissolve 
    h "Put me down."
    scene s4_5aaa13 with dissolve 
    mc "On the bright side, you finally got some height."
    scene s4_5aaa12 with dissolve 
    h "On the dark side, I might die of embarrassment."
    scene s4_5aaa14 with dissolve 
    mc "Pick your poison."
    play sounds2 clench 
    scene s4_5aaa15 with dissolve 
    h "Oh, shut up."
    play sounds3 whoosh 
    play sounds4 mmove 
    scene s4_5aaa16 with dissolve 
    h "(whispering) Look… I do value what we’ve got. Really."
    h "(whispering) But maybe don’t do that while the gorilla’s watching, yeah?"
    pause 1.1
    mc "Noted."
    play sounds4 mmove 
    scene s4_5aaa17 with dissolve
    mc "Next!"
    play sounds2 glitchfear
    scene s4_5aaa18 with glitch 
    Mi "Thank you… but I can manage."
    scene s4_5aaa19 with dissolve 
    h "Oh! That reminds me-"
    h "The Soulless… they’re basically humans in mutant bodies, right?"
    scene s4_5aaa17 with dissolve
    k "Where are you going with this?"
    h "How… do they spread?"
    if lora_relationship >= 2:
        play sounds2 waterfall 
        scene s4_5ff42 with vpunch
        mc "That’s—"
        scene s4_5ff43 with dissolve 
        L "Through the air."
        L "(whispering) Thank you, dear."
        scene s4_5ff44 with dissolve 
        h "Wait wait, what do you mean {b}through the air{/b}?!"
        h "There are mutants everywhere outside, how are we still alive?!"
        scene s4_5ff40 with dissolve 
        k "Hey. Old man."
        k "You planning on putting her down anytime soon?"
        scene s4_5ff41 with dissolve 
        h "Funny."
        h "Didn’t look like you had a problem getting close earlier."
        scene s4_5ff40 with dissolve 
        k "That was necessary."
        k "You want him stable, or sentimental?"
        scene s4_5ff44 with dissolve 
        mc "Enough. Not here."
        mc "We’re talking about the air."
        scene s4_5ff45 with dissolve 
        L "Airborne, yes."
        L "But it depends on the concentration."
        

    else:
        play sounds2 mmove 
        scene s4_5aaa20 with dissolve
        mc "That’s—"
        play sounds2 waterfall 
        scene s4_5aaa21 with dissolve
        L "Through the air."
        scene s4_5aaa22 with dissolve
        h "Wait wait, what do you mean {b}through the air{/b}?!"
        h "There are mutants everywhere outside, how are we still alive?!"
        scene s4_5aaa21 with dissolve
        L "Airborne, yes."
        L "But it depends on the concentration."

    play sounds3 clapnhands
    scene s4_5aaa24 
    pause 0.1
    scene s4_5aaa25 
    pause 0.1
    scene s4_5aaa24 
    pause 0.1
    scene s4_5aaa25 
    h "Oh."
    h "So the miasma’s already down here."
    L "Miasma isn’t a cloud."
    L "It’s what leaks from unstable Gates."
    L "It poisons places first. Then bodies."
    play sounds2 mmove 
    scene s4_5aaa26 with dissolve
    mc "Why the sudden question?"
    play sounds3 clothess  
    play sounds4 windcyb fadein 2.4 loop 
    scene s4_5aaa27 with dissolve 
    h "Lower City run."
    h "Same smell there as here."
    scene s4_5aaa28 with dissolve 
    h "And those massive ventilation shafts… like someone was deliberately spreading it—"
    play sounds2 fcy
    h "(coughs)"
    play sounds2 breath1
    scene s4_5aaa31 with dissolve 
    L "Breathe…"
    L "I thought it was strange too, but—"
    scene s4_5aaa32 with dissolve 
    mc "Lora. A word."
    L "Of course, dear."
    L "You feeling better?"
    scene s4_5aaa33 with dissolve 
    h "Y-yeah… thanks."
    play sounds2 breath1
    scene s4_5aaa37 with dissolve 
    mc "That device."
    mc "Why did you give it to me?"
    play sounds2 breath2
    scene s4_5aaa38 with dissolve 
    L "The Blood of the Ancients…"
    L "That’s what they call the charge inside the device."
    L "It and the miasma come from the same living source."
    L "Contained, it can power a Gate."
    L "Released, it spreads through living tissue and takes control."
    mc "Fuel and infection."
    L "The same source. A different state."
    L "Please, don’t be angry. I’ll explain."
    stop sounds4 fadeout 0.5
    scene s4_5aaa40 with dissolve 
    mc "..."
    play sounds2 mmove 
    scene s4_5aaa39 with dissolve 
    L "(whispering) I want to believe we’ll make it through this…"
    L "(whispering) But if something happens to you…"
    play sounds2 clench 
    scene s4_5aaa41 with dissolve 
    L "Please… use it."
    pause 1.1
    mc "It kills."
    scene s4_5aaa42 with dissolve 
    L "Everything is poison. Everything is medicine."
    L "It’s all in the dose."
    L "A rapid release will cause an explosion." 
    scene s4_5aaa44 with dissolve 
    L "A slow one…" 
    L "…can heal even a fatal wound."
    scene s4_5aaa45 with dissolve 
    mc "..."
    pause 1.1
    mc "I don’t agree with this, Lora."
    scene s4_5aaa46 with dissolve 
    L "I know, dear, but—"
    mc "..."
    mc "(This thing carries other people’s lives… and you want me to spend them?)"
    mc "(How am I supposed to justify that…)"
    scene s4_5aaa40 with dissolve 
    mc "Let’s hope it never comes to that."
    scene black with dissolve 
    stop music fadeout 1.1
    stop sound fadeout 1.1
    pause 1.2
    scene black with dissolve 
    play sound spaceshipinto loop volume 0.2 fadein 2.0
    play music backgroundsus fadein 7.2
    pause 2.1
    "Once again, ventilation shafts."
    show s4_5a27 with dissolve 
    mc "Let's move."
    play sounds2 metalstep 
    scene s4_5a9 with dissolve     
    mc "(The closer we get to the center… the worse it feels.)"
    mc "(Every instinct I have is screaming, run. Run as fast as you can.)"
    play sounds3 mmove
    scene s4_5a10 with dissolve  
    mc "(But my legs keep walking.)"
    scene s4_5a35 with dissolve  
    mc "(I’ve never been the kind of person who’d give his life for someone else.)"
    mc "(If anything… the opposite.)"
    mc "(And yet… when I look at them…)"
    scene s4_5a36 with dissolve  
    Mi "...Are you okay?"
    scene s4_5a35 with dissolve  
    mc "Yeah. Why?"
    Mi "(Something’s weighing on him.)"
    Mi "(He looks steady on the outside, but…)"
    play sounds2 metalstep 
    scene s4_5a37 with dissolve  
    Mi "(whispering) Deep down… you’re afraid…"
    mc "..."
    play sounds3 mmove 
    scene s4_5a38 with dissolve  
    Mi "We’re… more sensitive to our surroundings."
    scene s4_5a39 with dissolve  
    Mi "And…"
    play sounds3 mmove 
    scene s4_5a40 with dissolve  
    pause 1.2 
    scene s4_5a41 with dissolve  
    mc "(whispering) Thanks, Miriel."
    mc "But don’t worry."
    play sounds3 mmove 
    scene s4_5a40 with dissolve  
    pause 0.5
    play sounds4 systemnotification
    scene s4_5a38 with dissolve  
    "Threat level: Moderate. Four o`clock."
    scene s4_5a13 with dissolve  
    pause 0.8
    play sounds3 ha 
    play sounds1 runmetal volume 0.2 
    scene s4_5a14 with dissolve  
    mc "(whispering) Enemy."
    k "Oh? More pretty faces. Finally, something fun."
    play sounds1 runmetal volume 0.2 
    scene s4_5a34 with dissolve  
    mc "(whispering) No. We let them pass."
    k "…Yeah, I don’t think so."
    play sounds3 bodytap
    scene s4_5a42 
    mc "(whispering) If we can avoid casualties, we do."
    scene s4_5a43 with dissolve  
    k "Wow. How noble of you."
    k "Not that I care about their lives. But I’m not just going to ignore what they’ve done."
    scene s4_5a44 with dissolve  
    mc "You’ll only make it worse. Every body we drop plays into the enemy’s hands."
    k "…"
    scene s4_5a45 with dissolve  
    k "You and your logic. Always ruining the fun."
    pause 0.8
    play sounds3 swordswing
    play sounds2 metalstep 
    scene s4_5a46 with dissolve  
    k "Fine."
    play sounds3 metalstep 
    scene s4_5a47 with dissolve  
    h "Oh wow."
    h "What happened to “screw the plan, we charge in”?"
    scene s4_5a48 with dissolve  
    k "Crazy thing called ‘reputation.’ You should try getting one."
    play sounds2 mmove  
    scene s4_5a49 with dissolve  
    k "Oh, and one more thing."
    play sounds3 rustling2 
    scene s4_5a50 with dissolve  
    k "That implant? Not a miracle cure. Don’t rely on it too much."
    k "We’ve already got one lunatic on the team."
    scene s4_5a38 with dissolve  
    mc "(Reputation… huh.)"
    mc "Kali? Thanks."
    play sounds2 whoosh 
    scene s4_5a51     
    pause 1.2
    scene s4_5a52 with dissolve  
    k "Yeah, yeah."
    scene s4_5a38 with dissolve  
    mc "(Small win.)"
    mc "Let’s move."
    stop music fadeout 2.3
    stop sound fadeout 1.1
    
    scene black with dissolve 
    pause 2.1
    
    play sounds1 towers loop volume 0.6
    play sounds3 metalstep 
    scene s4_5a60 with dissolve  
    "Entrance to the compressor zone."
    pause 1.5
    Mi "...why."
    play sounds4 whoosh volume 0.3
    scene s4_5a54 
    pause 0.1
    play sounds2 bodytap 
    pause 1.6
    scene s4_5a53 with dissolve  
    Mi "Why didn’t you kill them?"
    mc "(Why did that look give me chills?)"
    scene s4_5a54 with dissolve  
    pause 1.1
    mc "I don’t kill for pleasure. If a fight can be avoided, I avoid it."
    play sounds3 mmove 
    scene s4_5a55 with dissolve  
    Mi "They’ve murdered innocent civilians."
    scene s4_5a57 with dissolve  
    mc "So have we."
    play sounds3 bodytap
    scene s4_5a58 with dissolve  
    Mi "…"
    mc "None of us are clean."
    mc "(whispering) …but if I can shave off even the smallest fraction of the world’s cruelty-"
    play sounds3 metalstep 
    scene s4_5a59 with dissolve  
    mc "—I sleep better at night."
    mc "(Hypocritical? Absolutely.)"
    pause 0.5
    mc "Now move."
    play sounds3 metalstep 
    scene s4_5a60 with dissolve  
    pause 1.1
    scene s4_5a61 with dissolve  
    k "Hey, shorty."
    play sounds3 whoosh  
    play sounds metalstep  
    scene s4_5a62 with CropMove(time=0.2, mode='slideright') 
    h "What do you want?"
    play sounds2 whoosh 
    scene s4_5a63 with CropMove(time=0.2, mode='slideleft') 
    k "What’s [mc] deal? Why’s he so obsessed with protecting lives?"
    play sounds3 whoosh 
    play sounds4 metalstep  
    scene s4_5a64 with CropMove(time=0.2, mode='slideright') 
    k "I’ve never seen him kill anyone who wasn’t a mutant."
    scene s4_5a65 with dissolve 
    h "That’s…"
    h "He had his reasons."
    play sounds3 metalstep  
    scene s4_5a63 with dissolve  
    k "Oh yeah? Like what?"
    scene s4_5a66 with dissolve  
    # Флешбек нахлынули на оливию 
    # Минута, две.
    scene s4_5a66 with dissolve  
    h "If he wants you to know, he’ll tell you."
    play sounds2 metalstep 
    scene s4_5a67 with dissolve  
    k "Boring."

# Сцена 1.1
    # Продвигаясь все глубже. 
    play sounds mmove   
    play sounds4 systemnotification
    scene s4_5a28 with dissolve  
    "Air contamination level: Critical."
    pause 1.5
    mc "Lora. {w=0.4}This Selvaria… who is she?"
    play sounds2 metalstep 
    scene s4_5a29 with dissolve  
    L "The Empress of the Elves. Terror made flesh."
    play sounds3 mmove 
    scene s4_5a9 with dissolve  
    mc "An empress… right."
    play sounds2 metalstep 
    scene s4_5a10 with dissolve  
    mc "What are her weaknesses?"
    play sounds2 metalstep 
    scene s4_5a7 with dissolve  
    L "Weaknesses… She doesn’t have any."
    L "We tried everything. Every plan, every angle—"
    L "I… I don’t know."
    stop sounds1 fadeout 15.2
    play music wot fadein 8.2 volume 0.5
    scene s4_5a8 with dissolve  
    pause 0.5
    "A heavy silence drops over the group, thick as smoke."
    play sounds2 mmove  
    scene s4_5a5 with dissolve  
    h "Yeah."
    h "Figures. We’re screwed."
    play sounds2 metalstep 
    scene s4_5a4 with dissolve  
    mc "(Everyone here’s packing implants, tricks, second chances…)"
    mc "(But walking in blind? That’s just suicide with extra steps.)"
    play sounds2 metalstep 
    scene s4_5a28 with dissolve  
    mc "Lora. A word."
    play sounds4 systemnotification
    scene s4_5a68 with dissolve  
    "Air contamination level: Within acceptable limits."
    L "Yeah, love?"
    mc "(whispering) How long till we reach her?"
    play sounds2 metalstep 
    scene s4_5a69 with dissolve  
    L "(Whispering) Half an hour. Give or take."
    play sounds mmove 
    scene s4_5a70 with dissolve  
    pause 0.6
    play sounds3 rustling2 
    scene s4_5a71 with dissolve  
    pause 0.6
    play sounds2 clench 
    scene s4_5a72 with dissolve  
    pause 1.1
    scene s4_5a73 with dissolve  
    mc "(whispering) I need you to do something."
    scene s4_5a74 with dissolve  
    L "(That look again… The same one he had when he enlisted.)"
    L "(When he’d already decided, and nothing could stop him.)"
    L "(Whispering) Please… No stupid heroics."
    scene s4_5a73 with dissolve  
    mc "(whispering) Take the others."
    mc "(whispering) Get out."
    play sounds2 whoosh 
    scene s4_5a75 
    L "(Whispering) What?!" 
    L "(Whispering) Have you lost your mind? No!"
    scene s4_5a76 with dissolve  
    pause 0.7
    play sounds mmove 
    scene s4_5a78 with dissolve  
    pause 0.7
    scene s4_5a79 with dissolve  
    mc "(whispering) They don’t have what you have, Lora. For them… death’s final."
    play sounds2 mmove 
    scene s4_5a80 with dissolve  
    mc "(whispering) My clock says you still have time to run."
    scene s4_5a81 with dissolve  
    L "(Whispering) …And you?"
    scene s4_5a82 with dissolve  
    mc "…"
    play sounds mmove 
    scene s4_5a70 with dissolve  
    mc "…I’ll try to talk to her."
    play sounds2 hug2  
    scene s4_5a83 with dissolve  
    L "(Whispering) No. Please… I—" 
    L "Watching you die… over and over…"
    L "Do you know what that does to me?"
    play sounds mmove 
    scene s4_5a84 with dissolve  
    L "Norman dying every time—"
    L "I blamed myself. Every single time."
    L "And you…"
    L "Losing you tore me apart."
    scene s4_5a85 with dissolve  
    mc "(whispering) Selfish bastard, huh."
    play sounds4 windcyb fadein 2.4 volume 0.2 loop 
    scene s4_5a31  with dissolve  
    k "(All that whispering. Standing way too close.)"
    k "(God, it’s annoying.)"
    scene s4_5a32 with dissolve  
    k "Hey. Lovebirds."
    k "Especially you, one-eye."
    k "What’s the plan with the elf queen?"
    scene s4_5a31  with dissolve  
    L "(Does she just hate me…?)"
    play sounds2 mmove 
    scene s4_5a87 with dissolve  
    L "I… I don’t know. Without Astoria, we—"
    play sounds3 metalstep 
    scene s4_5a88 with dissolve  
    L "(Focus. Stop drifting. Mission first.)"
    L "She’s a Higher Being." 
    L "We can’t kill her. No matter what we try."
    mc "Why?"
    play sounds3 metalstep 
    scene s4_5a89 with dissolve  
    Mi "Every higher being carries some kind of safeguard."
    Mi "Mortals can’t really hurt them."
    play sounds2 mmove 
    play sounds3 whoosh 
    scene s4_5a90 
    k "So we just need a bigger gun. Easy."
    scene s4_5a91 with dissolve  
    mc "Kalestra?"
    scene s4_5a92 with dissolve  
    k "Nah. I’m useless here."
    k "But if you want, I can give you a hundred and one reasons why higher beings are a pain in the ass."
    scene s4_5a108 with dissolve  
    mc "(Flora mentioned something like this before… but somehow they managed to kill one of those Higher Beings.)"
    mc "(How?)"
    pause 0.5
    mc "Options?"
    pause 1.1
    E "..."
    # тишина 
    # смотря на Лору 
    scene s4_5a109 with dissolve  
    mc "Nothing? Not even one?"
    mc "What about all those resets of yours?"
    scene s4_5a93 with dissolve  
    L "In none of them did we kill her. Not once."
    L "I thought… maybe if killing her wasn’t possible, we could negotiate—"
    stop music fadeout 3.4
    play music1 emberagony fadein 7.2
    scene s4_5a94 with dissolve  
    k "That’s called betrayal, sweetheart."
    k "And traitors don’t get forgiven."
    L "(If betrayal saves my husband’s life… Then so be it.)"
    play sounds3 mmove 
    scene s4_5a95 with dissolve  
    L "Not betrayal. Strategy."
    k "That pointy-eared monster wiped out half a planet."
    L "And she’ll wipe us out too if we don’t try something."
    play sounds3 clench 
    stop sounds4 fadeout 0.5
    scene s4_5a96 with dissolve  
    k "(God, she’s irritating.)"
    k "..."
    L "What? You gonna kill me for saying it?"
    k "You doubting I would?"
    play sounds3 clench 
    scene s4_5a109 
    pause 0.9
    play sounds2 swordswing
    scene s4_5a98
    pause 0.4
    # Калестра замахивается мечом на Лору но мс останавливает её.
    # тишина
    play sounds3 cinematichit 
    play sounds4 whoosh 
    scene s4_5a102 with vpunch  
    mc "Kalestra."
    mc "Sword down."
    scene s4_5a103 with dissolve  
    k "How long are you gonna keep excusing her crap?!"
    scene s4_5a104 with dissolve  
    mc "Any outcome where we’re still alive… is a good one."

    # смотря на лору 
    play sounds2 mmove 
    scene s4_5a101 with dissolve  
    mc "(If she couldn’t do it… what makes me think I can?)"
    mc "Yeah. It’s stupid."
    scene s4_5a104 with dissolve  
    mc "But I get why she tried."
    mc "(We don’t owe these people anything. And still… here we are.)"
    play sounds3 clench 
    scene s4_5a103 with dissolve  
    k "I’m not siding with that pointy-eared freak."
    scene s4_5a105 with dissolve  
    mc "You won’t have to."
    stop music1 fadeout 3.4
    play music covenant fadein 15.2
    scene s4_5a106 with dissolve  
    h "That grin... You’ve got something, don’t you?"
    play sounds3 mmove 
    scene s4_5a107 with dissolve  
    mc "We came here to stop the Gates from opening."
    mc "We don’t need to kill her."
    mc "Selvaria’s just the symptom. The Gates are the disease."
    play sounds2 mmove 
    scene s4_5a108 with dissolve  
    mc "Everyone remembers what happens if they stay open."
    mc "Everything alive dies."
    mc "(I didn’t come here for anyone’s ideals. I came to survive.)"
    mc "(And protect what matters to me.)"
    h "(That look of his… Damn. It actually gives hope.)"
    play sounds2 mmove 
    scene s4_5a110 with dissolve  
    h "…There’s something to that."
    scene s4_5a111 with dissolve  
    Mi "We’re talking about an ancient mechanism here." 
    Mi "How exactly do you plan to shut all that down?"
    scene s4_5a112 with dissolve  
    mc "You got a better idea?"
    play sounds2 mmove 
    scene s4_5a113 with dissolve  
    Mi "…no."
    scene s4_5a107 with dissolve  
    mc "We won’t stop Selvaria by killing her. We’ll just die trying."
    k "So what’s your genius plan?"
    scene s4_5a75 with dissolve  
    L "May I?"
    mc "Yeah."
    # мс кивает
    scene s4_5a87 with dissolve  
    L "Then we use the fallback."
    L "The Gates use a cooling system."
    L "If we block it… in theory, it should force an emergency shutdown."
    scene s4_5a97 with dissolve  
    Mi "“In theory”?"
    Mi "So, no guarantees?"
    L "..."
    mc "(Hands shaking. Breathing uneven.)"
    mc "(Yeah… now I see why she considered siding with Selvaria.)"
    play sounds4 windcyb fadein 2.4 volume 0.2 
    scene s4_5a115 with dissolve  
    k "(That damn understanding look.)"
    k "(After all her mistakes… why does he still look at her like that?)"
    play sounds2 clench 
    scene s4_5a116 with dissolve  
    k "You know, she’s really starting to piss me off."
    h "Huh?" 
    k "You’re the scientist. And you don’t know squat?"
    k "Funny."
    k "Feels like you’re holding something back."
    scene s4_5a117 with dissolve  
    mc "Lora?"
    L "I really don’t know… Yes, I worked with the Gates. That’s true."
    L "But I only opened them. Closing them? All I have are theories dug out of tombs."
    play sounds2 mmove 
    scene s4_5a114 with dissolve 
    h "So we’re screwed. Correct?"
    scene s4_5a118 with dissolve  
    mc "(Chase a slim chance… or walk straight into the beast’s den and try to talk?)"
    mc "(whispering) Get them out of here."
    scene s4_5a35 with dissolve  
    mc "Miriel. Olivia. And… Kalestra."
    mc "Stick with Lora. Try to shut the Gates down through cooling."
    scene s4_5a36 with dissolve  
    Mi "Understood."
    scene s4_5a38 with dissolve  
    h "Wait. What about you?"
    mc "..."
    play sounds ha
    "Threat Level: Moderate. Seven o’clock remaining."
    play sounds3 mmove 
    scene s4_5a13 with dissolve  
    pause 0.7
    play sounds4 rungroup2
    scene s4_5a14 with dissolve  
    h "No…"
    h "You’re not actually—"
    # Разгоняясь он замахивается на стену.
    play sounds3 mmove 
    scene s4_5a15 with dissolve  
    mc "(Principles… or the people I love?)"
    play sounds2 hit1
    play sounds3 rockfall
    scene s4_5a17 with vpunch 
    pause 1.1
    play sounds4 clench 
    scene s4_5a18 
    pause 0.8
    play sounds3 fall 
    scene s4_5a19
    pause 0.7 
    play sounds whoosh 
    scene s4_5a20
    pause 1.1
    play sounds2 pisolsil
    play sounds1 hdshot
    scene s4_5a21 with vpunch 
    pause 0.6
    play sounds3 pisolsil
    play sounds4 hdshot
    scene s4_5a22 with vpunch 
    mc "(Sorry. You didn’t leave me a choice.)"
    scene s4_5a23 with dissolve  
    h "Holy—"
    scene s4_5a38 with dissolve 
    mc "Do everything you can. I’ll do the same."
    scene s4_5a119 with dissolve 
    pause 0.5 
    scene s4_5a120 with dissolve 
    pause 0.5 
    play sounds2 mmove 
    scene s4_5a121 with dissolve 
    L "Take care of yourself."
    scene s4_5a122 with dissolve 
    pause 1.5
    play sounds2 metalstep 
    scene s4_5a26 with dissolve 
    mc "Why aren’t you with them?"
    scene s4_5a25 with dissolve 
    k "Didn’t like your order."
    scene s4_5a26 with dissolve 
    mc "What about your precious reputation?"
    scene s4_5a25 with dissolve 
    k "Yeah. Well."
    k "Reputation doesn’t cover crap like this."
    pause 0.5
    k "Besides..."
    k "dying with you sounds way more fun."
    stop music fadeout 4.3
    scene black with dissolve 
    pause 4.2
    $ persistent.chapter_act4_5_scene += 1

# Сцена 2.
label story05_5_2:
    stop music fadeout 0.5
    play sounds2 metalrun 
    play music1 s45c1mcscene fadein 15.1
    scene s4_5a123 with dissolve 
    "High above the gate."
    mc "Move. We’re short on time."
    k "Yeah, yeah. Running."
    play sounds3 mmove 
    scene s4_5a124 with dissolve 
    k "Hey, old man. You sure about this?"
    mc "..."
    play sounds2 mmove
    scene s4_5a126 with dissolve 
    k "Drop the doubt."
    k "Even the dumbest plans sometimes blow up into victories."
    play sounds3 metalstep
    scene s4_5a125 with dissolve 
    mc "And that was?"
    k "Advice."
    mc "Sounds more like incompetence."
    scene s4_5a126 with dissolve 
    k "Choosing the better of two terrible ideas doesn’t make it good."
    k "Now wipe the tears and run."
    play sounds3 mmove
    scene s4_5a123 with dissolve 
    mc "Time?"
    k "Thirty minutes."
    play sounds3 mcjump volume 4.2
    scene s4_5a127 with dissolve 
    mc "Good. Time to buy them some."
    
    play sounds3 whoosh 
    scene s4_5ff2 with CropMove(time=0.1, mode='slideup') 
    pause 2.3
    play sounds4 mcjump2 volume 4.2
    scene s4_5b1 with vpunch 
    mc "(One.)"
    pause 0.5

    play sounds2 mmove 
    scene s4_5b2 with dissolve 
    g "What the—"
    mc "(Two.)"
    pause 0.5

    g "Who the hell are you supposed to be?"
    mc "(Three.)"
    play sounds1 riflesound1 
    scene s4_5b3 
    pause 1.2
    play sounds2 mmove 
    scene s4_5b4 
    pause 0.5
    play sounds3 scar1
    pause 0.3
    play sounds4 hdshot 
    scene s4_5b5 with vpunch  
    "Analysis complete. Displaying optimal elimination method."
    mc "(Was that really the only way?)"
    play sounds2 ha 
    scene s4_5b6 with dissolve  
    mc "(whispering) Or just the easiest?"
    play sounds3 scar1
    scene s4_5b7 with vpunch 
    pause 0.3
    play sounds4 hdshot
    mc "(whispering) Shut it down. No hesitation."
    play sounds2 ha 
    scene s4_5b8 with dissolve 
    "Three hostiles. Eight o’clock. Life threat: high."
    scene s4_5b112 with vpunch 
    play sounds3 scar1
    pause 0.6
    play sounds3 scar1
    play sounds rifflesounds21 volume 0.6 loop
    play sounds2 mmove 
    scene s4_5b9 with dissolve 
    mc "(They’re just like me.)"
    pause 1.1
    mc "(With their own fears… their own lives.)"
    pause 1.1
    play sounds2 mmove 
    play sounds1 rs1 loop volume 0.5
    scene s4_5b10 with dissolve 
    mc "(Maybe there’s still a way to—)"
    mc "We can still—"
    pause 0.8
    play sounds2 hdshot
    scene s4_5b113 with vpunch 
    mc "—Argh!"
    play sounds2 ha 
    "External injuries detected—"
    mc "I KNOW!"
    pause 0.7
    mc "(No. Too late now.)"
    pause 1.1
    play sounds3 hdshot
    scene s4_5b114 with vpunch 
    mc "…Hold it together."
    mc "(No going back. Either I—)"
    play sounds2 hdshot
    scene s4_5b115 with vpunch 
    mc "(whispering) or they kill me."
    pause 0.8
    stop sounds fadeout 0.3 
    scene s4_5b116 with dissolve 
    pause 1.7
    play sounds2 fall 
    scene s4_5b117 with dissolve 
    a "(Willy… Mecca… how—)"
    a "Your Majesty, why aren’t we stopping him?!"
    scene s4_5b118 with dissolve 
    a "He’s slaughtering our people down there!"
    scene s4_5b124 with dissolve 
    sel "And in doing so… he saves us the trouble."
    scene s4_5b123 with dissolve 
    a "But their lives—"
    scene s4_5b124 with dissolve 
    sel "Necessary losses."
    scene s4_5b120 with dissolve 
    pause 1.7
    scene s4_5b121 with dissolve 
    sel "You object?"
    scene s4_5b120 with dissolve 
    a "No, Your Majesty."
    sel "(Your eyes say otherwise.)"
    scene s4_5b122 with dissolve 
    pause 0.5
    scene s4_5b123 with dissolve 
    pause 0.5
    stop sounds1 fadeout 0.5
    scene s4_5b124 with dissolve 
    sel "He’s at his limit."
    play sounds riflesounds3 volume 0.2 loop
    scene s4_5b125 with dissolve 
    pause 1.2
    scene s4_5b126 with dissolve 
    a "My lady… allow me to kill him myself!"
    scene s4_5b127 with dissolve 
    sel "Go."
    scene s4_5b133 with dissolve 
    pause 0.5
    play sounds2 whoosh 
    scene s4_5b134 with CropMove(time=0.1, mode='slideleft') 
    pause 1.2
    play sounds2 glitchfear
    scene s4_5ff11 with glitch 
    pause 1.1

    
    scene s4_5b128 with dissolve 
    mc "(Hold on… hold on…)"
    mc "(Don’t black out. Not now.)"
    # воспоминания о близких.
    scene s4_5b129 with dissolve 
    mc "…Fight. Keep fighting!"
    play sounds2 mmove 
    scene s4_5b130 with dissolve 
    mc "(I just need to buy them time.)"
    play sounds2 whoosh 
    scene s4_5b131 with CropMove(time=0.1, mode='slideup') 
    pause 1.1
    stop sounds fadeout 0.5
    play sounds1 grenadeflash
    scene s4_5b131 with dreamyzoom
    pause 0.1
    play sounds2 mmove 
    scene s4_5b132
    pause 1.2
    play sounds3 clench
    play sounds1 rs1 loop volume 0.5
    scene s4_5b111 with CropMove(time=0.1, mode='slidedown')
    mc "(Even if it costs me everything.)"
    
    play sounds3 glitchfear 
    play sounds4 ha
    scene s4_5b11 with CropMove(time=0.1, mode='slideleft')
    "Fatal threat level. Three o’clock remaining."
    mc "(Where the hell did that—)"
    play sounds2 ha 
    scene s4_5b12
    "Analysis complete. Elimination impossible."
    scene s4_5ff4
    a "You’ll pay for my brothers!"
    mc "(Move, move MOVE!)"
    play sounds2 glitchfear
    scene s4_5ff5 with glitch 
    pause 1.1
    scene s4_5ff3 
    pause 3.1
    play sounds2 whoosh 
    scene s4_5ff6 with CropMove(time=0.1, mode='slidedown')
    pause 2.1

    play sounds1 swordhitkalesta
    scene s4_5b13 with vpunch  
    pause 4.3

    scene s4_5b14 with dissolve 
    k "How’s that saying go?"
    k "The hero shows up at the last second, right?"
    scene s4_5b15 with dissolve 
    mc "Where the hell have you been?!"
    play sounds1 swordhitkalesta
    scene s4_5ff8 with vpunch
    pause 0.8
    play sounds1 swordswing
    scene s4_5ff9 with dissolve 
    k "Enjoying your new combat mode."
    k "While eliminating potential problems."
    play sounds2 mmove 
    scene s4_5ff7 with dissolve 
    k "(whispering) Eyes forward. Blondie’s our real target. And right now… she’s watching you."
    mc "(whispering) We holding up or—"
    scene s4_5b216 with dissolve 
    k "(whispering) …Told you so."
    mc "Yeah, yeah."
    mc "Don’t rely on implants."
    play sounds2 whoosh 
    scene s4_5ff12 with CropMove(time=0.1, mode='slideright')
    pause 1.5
    play sounds1 swordhitkalesta
    scene s4_5b202 with vpunch
    k "Hey! We were talking here—!"
    play sounds1 rs1 loop volume 0.5
    play sounds3 clench 
    scene s4_5ff16 with CropMove(time=0.1, mode='slideright')
    pause 1.1
    play sounds2 whoosh 
    scene s4_5ff14 
    pause 1.1
    scene s4_5ff15
    pause 1.1
    play sounds3 mmove
    play sounds2 hit1 
    scene s4_5ff17 with vpunch 
    k "You handle the small fry."
    play sounds2 whoosh 
    scene s4_5ff18 
    pause 1.1
    play sounds3 whoosh 
    play sounds2 swordhitkalesta
    scene s4_5b196 with vpunch
    k "I’ll deal with the bigger fish."
    play sounds4 whoosh 
    scene s4_5b198 with CropMove(time=0.1, mode='slidedown') 
    pause 0.8
    scene s4_5b199 with dissolve
    k "(Trusting this old man with my back?)"
    k "(Yeah. I’m shocked too.)"
    play sounds4 swordhitkalesta
    scene s4_5b16 with vpunch 
    k "Hey, elf ears! Let’s talk!"
    k "(And that idiot… Somehow got under my skin more than I expected.)"
    play sounds2 mmove
    play sounds4 whoosh 
    scene s4_5b17 with CropMove(time=0.1, mode='slidedown') 
    pause 1.1
    play sounds2 hit1  
    play sounds3 rockfall
    scene s4_5b18 with vpunch 
    k "Come on, stop running and let me kill you already!"
    scene s4_5b19 with dissolve 
    a "I only want him. Not you."
    k "Oh yeah?"
    k "Too bad. I kinda like the guy. So no."
    stop sounds1 fadeout 0.5
    play sounds2 jumpkalesta 
    scene s4_5b20 with vpunch  
    a "Your Majesty?! That was my prey!"
    scene s4_5b194 
    k "The—?"
    play sounds4 hdshot 
    scene s4_5b22 with vpunch  
    pause 0.8
    scene s4_5b23 with dissolve 
    k "(You sneaky little—)"
    play sounds2 swordswing 
    scene s4_5b25 with dissolve 
    a "Oops. Missed."
    a "Falling for tricks like that… Guess the rumors about inquisitions were fake?"
    play sounds4 whoosh 
    scene s4_5b26 with CropMove(time=0.1, mode='slidedown')
    k "What… did you just say?"
    a "(Wh-)"
    scene s4_5b28 
    k "Don’t you dare—"
    scene s4_5b29 with dissolve 
    k "Look—"
    play sounds1 swordhitkalesta
    scene s4_5b30 with vpunch
    k "Down on me."
    play sounds2 swordswing
    scene s4_5b31 with dissolve 
    k "(No. Hold it.)"
    k "(Kill her too fast, and this gets ugly.)"
    pause 0.6
    k "Yo, elfie, you still—"
    play sounds3 whoosh 
    scene s4_5b195 with CropMove(time=0.1, mode='slideright')
    pause 0.8
    play sounds2 swordhitkalesta
    scene s4_5b200 with vpunch 
    k "Clever bastard!"
    scene s4_5b197 with dissolve 
    a "All you humans are the same!"
    a "Always thinking you’re above us!"
    play sounds2 clench 
    scene s4_5b196 with dissolve 
    k "At least nobody ever called us—"

    k "M-O-G-Y-R. \n(S-L-A-V-E-S.)"
    play sounds1 swordhitkalesta
    scene s4_5b197 with vpunch 
    a "Dagnin gin si! \n(I’LL KILL YOU!)"
    scene s4_5b200 
    pause 0.6
    play sounds1 swordhitkalesta
    scene s4_5b198 with vpunch  
    k "(Time. Stall for time.)"
    k "(That old idiot will think of something.)"
    scene s4_5b202 with dissolve  
    k "(Shoulder… damn.)"
    k "(Wait… gunfire stopped. Did he die?)"
    scene s4_5ff19 with dissolve 
    pause 2.1

    scene s4_5b35 with dissolve 
    sel "Impressive."
    pause 0.5
    play sounds2 mmove 
    scene s4_5b36 with dissolve 
    mc "(One word… and my whole body locks up.)"
    mc "(No. Focus. Time.)"
    mc "Selvaria. That’s you… right?"
    scene s4_5b37 with dissolve 
    sel "Hm."
    scene s4_5b38 with dissolve 
    sel "And you… Astoria’s little boy?"
    scene s4_5b37 with dissolve 
    mc "(She knows me?)"
    mc "(Wait, how would the elven empress know anything about me?)"
    mc "What do you mean, ‘that boy’?"
    scene s4_5b38 with dissolve 
    sel "Astoria never told you?"
    mc "(More secrets. Fantastic. Maybe this time they'll work in my favor.)"
    scene s4_5b124 with dissolve 
    sel "I see. So you truly don’t know."
    sel "Tell me, [mc]."
    sel "Do you like riddles?"
    scene s4_5b123 with dissolve 
    mc "(Riddles? Now?)"
    mc "Why?"
    sel "..."
    play sounds1 scar1 
    scene s4_5b40 with vpunch
    pause 0.9 
    scene s4_5b38 with dissolve 
    sel "I enjoy digging through other people’s minds."
    play sounds2 glitchfear
    scene s4_5b41 with glitch 
    aa "(whispering) Losto. Daro i gwaith. Dâd cennannen vi i thâl nedh. \n(They’re stalling. Two individuals spotted on lower floors.)"
    scene s4_5b42 with dissolve 
    sel "Nêl. \n(Three.)"
    pause 0.6
    aa "(whispering) Man i orch? \n(Orders?)"
    sel "Tegil hen. Hên hen nín. \n(Handle them. This one is mine.)"
    aa "Nae, Aran nín. \n(Yes, Your Majesty.)"
    play sounds1 scar1 
    scene s4_5b43 with vpunch 
    mc "No one leaves here!"

    scene s4_5b203 with dissolve 
    k "(Bad feeling.)"
    k "(She’s way too calm. Too empty. Gives me chills—)"
    play sounds3 whoosh 
    scene s4_5b195 with CropMove(time=0.1, mode='slideright')
    pause 1.1 
    play sounds1 swordhitkalesta
    scene s4_5b202 with vpunch 
    k "You’re getting on my nerves…"
    a "I’m your opponent!"
    scene s4_5b201 with dissolve 
    k "(Empress? Yeah, right.)"
    k "(That thing feels like a monster wearing a crown.)"
    k "(…Not that I mind monsters.)"
    play sounds1 swordswing
    scene s4_5b24 with dissolve 
    k "(But if we don’t do something—)"
    play sounds2 swordhitkalesta
    scene s4_5b196 with vpunch 
    pause 1.1
    play sounds2 whoosh 
    scene s4_5ff17 with CropMove(time=0.1, mode='slideright')
    a "(How?! Why is she this strong?! Why can’t I hurt her?!)"
    play sounds3 whoosh 
    scene s4_5b198 with CropMove(time=0.1, mode='slideright')
    pause 0.5
    play sounds3 mmove
    scene s4_5b31 with dissolve 
    k "..."
    scene s4_5b33 with dissolve 
    pause 1.1
    scene s4_5b34 with dissolve 
    k "(Wait.)"
    k "(Am I… scared?)"
 
    play sounds3 mmove 
    scene s4_5b45 with dissolve 
    sel "Boy. I have a proposal for you."
    sel "Agree… and I will leave this planet."
    mc "And if I refuse?"
    play sounds2 mmove 
    scene s4_5b206 with dissolve 
    pause 0.8
    scene s4_5b207 with dissolve 
    sel "Death."
    stop music1 fadeout 0.7
    play sounds2 cinematichit volume 0.4
    play sound glitchfear volume 0.3
    play music metromusic5 
    scene s4_5b208 with glitch
    "Error! Error! Err—"
    play sounds mmove 
    scene s4_5b209 
    mc "(How is she—)"
    play sounds2 mmove 
    scene s4_5b210 with CropMove(time=0.1, mode='slideright')
    mc "(My head’s going to explode…)"
    sel "Join me."
    stop music fadeout 7.5
    play music1 memoryastoria fadein 5.4
    scene s4_5b211 with dissolve 
    mc "..."
    mc "…What?"
    
    scene s4_5b212 with dissolve 
    aa "Aran nín, man i orch? \n(Your Majesty, what about the plan?!)"
    play sounds2 whoosh 
    scene s4_5b46 with dissolve 
    sel "What do you say? One life… in exchange for an entire planet."
    scene s4_5b47 with dissolve 
    mc "(My life… for the planet?)"
    mc "(If they live, then fine. I’ll pay it. But—)"
    mc "What’s the catch?"
    sel "..."
    play sounds1 swordhitkalesta
    scene s4_5b16 with vpunch 
    a "Where do you think you’re going?!"
    play sounds2 swordhitkalesta
    scene s4_5b200 with vpunch
    k "Get off me!"
    pause 0.5
    play sounds1 swordswing
    scene s4_5b202 with dissolve 
    k "Hey, old man. Don’t forget what the one-eyed witch said."
    k "They’ve got loose tongues. All they do is talk."
    play sounds3 mmove
    scene s4_5b213 with dissolve
    mc "(I know.)"
    mc "(But the idea of saving all of you… even if it costs me…)"
    mc "(Even if it’s a lie… I want to believe it.)"
    play sounds2 mmove 
    scene s4_5b51 with dissolve 
    sel "What’s your answer?"
    scene s4_5b52 with dissolve 
    pause 0.7 
    scene s4_5b213 with dissolve 
    sel "Betray the others, and they live."
    sel "Or share their fate. Cross over together."
    sel "Choose."
    play sounds2 mmove 
    scene s4_5b215 with dissolve 
    mc "(This…)"
    scene s4_5b214 with dissolve 
    mc "What guarantees do I have that if I betray them… you won’t touch them?"
    scene s4_5b51 with dissolve 
    sel "Answer."
    scene s4_5b52 with dissolve  
    mc "(Nothing this clean comes without a trap.)"
    mc "I—"
            
    play sounds2 whoosh
    scene s4_5b54  
    k "Enough of this bullshit, you decrepit hag!"
    mc "Kali, don’t—"
    play sounds3 jumpkalesta
    play sounds1 swordswing
    scene s4_5b55 
    k "Die!"
    play sounds4 swordhitkalesta
    play sounds2 shieldimpact2
    scene s4_5b56 with vpunch 
    sel "..."
    k "What, without all your fancy magic toys, too scared?!"
    scene s4_5b57 with dissolve 
    sel "Correction. Not magic. Technology."
    scene s4_5b60 with dissolve 
    k "And that’s supposed to matter?"
    k "Same slop, different bowl."
    scene s4_5b59 with dissolve 
    sel "Ignorant. Comparing crude “magic” to our technology—"
    scene s4_5b60 with dissolve 
    mc "Go back!"
    k "Oh? Did I hurt your—"
    stop music1 fadeout 0.5 
    play sounds3 hdshot
    play sounds4 heartbeat loop volume 0.4
    scene s4_5b135 with vpunch
    pause 1.5
    scene s4_5b136 with dissolve  
    pause 0.8
    play music kalideath fadein 9.2
    scene s4_5b137 with dissolve 
    pause 0.9
    play sounds2 swordhitkalesta
    scene s4_5b138 with vpunch 
    pause 0.7
    scene s4_5b143 with dissolve 
    mc "(N-no…)"
    scene s4_5b139 with dissolve 
    pause 3.5
    scene s4_5b141 with dissolve 
    k "(whisper) Run…"
    play sounds4 fall 
    scene s4_5b145 with vpunch 
    pause 2.2
    scene s4_5b144 with dissolve 
    pause 1.1
    scene s4_5b149 with dissolve 
    mc "-ah..."
    play sounds4 clench  
    scene s4_5b148 with dissolve    
    mc "(This can’t be how it ends.)"

    play sounds2 mmove 
    play sounds1 rs1 loop volume 0.3 
    scene s4_5b150 
    pause 1.6
    scene s4_5b151 with dissolve  
    mc "(I’m not letting this end here.)"
    scene s4_5b152 with dissolve
    pause 0.9
    scene s4_5b153 with dissolve  
    pause 0.8
    play sounds1 mmove 
    scene s4_5b154 with dissolve 
    mc "We can still—"
    play sounds2 scar1
    scene s4_5b155 with dissolve 
    mc "AAAAAAAH!"
    scene s4_5b156 with dissolve 
    mc "COME ON!"
    play sounds2 scar1
    scene s4_5b162 with dissolve 
    mc "DIE!"
    scene s4_5b161 with dissolve 
    k "You idiot…"
    scene s4_5b164 with dissolve 
    k "(No. I have to help…)"
    scene s4_5b165 with dissolve 
    mc "(Why won’t it break? With all my strength… I—)"
    play sounds1 hit1 
    play sounds2 shieldimpact2
    scene s4_5b157 with vpunch 
    pause 0.7 
    play sounds3 hit1 
    play sounds4 shieldimpact1
    scene s4_5b158 with vpunch 
    pause 0.7 
    play sounds1 hit1 
    play sounds2 shieldimpact2
    scene s4_5b157 with vpunch 
    mc "(COME ON! COME ON!)"
    play sounds4 shieldimpact1
    scene s4_5b158 with vpunch 
    pause 0.7 
    play sounds2 shieldimpact2
    scene s4_5b157 with vpunch
    sel "(Pathetic…)"
    play sounds4 shieldimpact1
    scene s4_5b158 with vpunch 
    pause 1.2
    play sounds2 shieldimpact2
    scene s4_5b160 with vpunch 
    sel "You’re all the same."
    play sounds4 shieldimpact1
    scene s4_5b166 with vpunch
    pause 1.7 
    play sounds2 mmove 
    scene s4_5b167 with dissolve 
    mc "(It’s useless…)"
    sel "Throwing promises around—"
    sel "promises you can never keep."
    pause 1.1 
    mc "(promises?)"
    mc "(No…)"

    scene s3a66 with dreamyzoom 
    show memoryframe with dissolve
    L "You want me to tell you everything. You think you can handle it."
    L "But sometimes knowing ruins more than not knowing ever could."
    hide memoryframe
    scene s4_d36 with dreamyzoom 
    show memoryframe with dissolve
    L "The Empress of the Elves."
    L "Weaknesses… She doesn’t have any."
    hide memoryframe
    scene s4_f141 with dreamyzoom 
    show memoryframe with dissolve
    L "We tried everything. Every plan, every angle—"
    L "I… I don’t know."
    hide memoryframe
    scene s4_d146 with dreamyzoom 
    show memoryframe with dissolve
    L "(I tried. I fought. I searched for a way to break that limit.)"
    hide memoryframe
    scene s4_5aaa39 with dreamyzoom 
    show memoryframe with dissolve
    L "(whispering) I want to believe we’ll make it through this…"
    hide memoryframe
    scene s4_5aaa41 with dreamyzoom 
    show memoryframe with dissolve
    L "Please… use it."
    hide memoryframe
    play sound gatebackground fadein 5.4 loop volume 0.2
    scene s4_5b168 with dreamyzoom 
    sel "Any last words?"
    mc "..."    
    
    play sounds2 running 
    
    scene s4_5ff37 with dissolve 
    show 4yr with dissolve 
    "(Cooling control zone.)"
    hide 4yr
    play sounds3 scar1 
    scene s4_5ff38 with dissolve 
    pause 1.5
    play sounds4 scar1 
    scene s4_5ff39 with dissolve 
    L "(Come on… hurry up!)"

    scene s4_5b169 with dissolve 
    sel "Well then. For the effort—"
    scene s4_5b170 with dissolve 
    sel "—I’ll grant you a painless death."
    play sounds2 whoosh 
    scene s4_5b171 with vpunch 
    mc "..."
    play sounds2 clench
    scene s4_5b172 with dissolve 
    mc "If this is how it ends…"
    scene s4_5b205 with dissolve 
    mc "…so be it."
    scene s4_5b204 with dissolve 
    sel "Don’t try anything stupid."
    play sounds2 glitchfear
    scene s4_5b175 with glitch 
    mc "..."
    scene s4_5b176 with dissolve 
    N "Once more, you’ve taken too much onto your shoulders, Father."
    scene s4_5b177 with dissolve 
    c "Don’t even try to talk him out of it."
    c "Same as always."
    scene s4_5b178 with dissolve
    m "And that’s what makes him so hard to let go of, right?"
    m "Stubborn idiot."
    scene s4_5b180 with dissolve
    mc "Jack… Mona… you—"
    b "..."
    scene s4_5b179 with dissolve 
    m "We’re dying to see you again, Commander, but—"
    c "Yeah. Don’t you dare die on us."
    c "You owe us."
    scene s4_5b175 with dissolve 
    mc "I…"
    
    scene s4_5b181 with dissolve 
    N "We know, Father. You miss us."
    play sounds3 scar1 volume 0.6 
    scene s4_5ff29 with dissolve 
    show 4yr with dissolve 
    play sounds2 keyboard volume 0.5
    pause 0.3
    play sounds4 scar1 volume 0.6 
    pause 0.6
    N "And we will meet again."
    scene s4_5ff30 with dissolve 
    N "Just… not yet."
    play sounds4 powersup
    scene s4_5ff31 with dissolve 
    pause 1.1
    scene s4_5ff32 with dissolve 
    stop music fadeout 0.5
    play sounds3 industryon
    am "Now. Move!"
    play music1 s45c2kaliscene fadein 9.2
    scene s4_5b182 with dissolve 
    mc "Wh—?"
    play sounds3 c4boom 
    scene s4_5b183 with vpunch 
    pause 0.7
    scene s4_5b185 with dissolve 
    pause 0.8
    play sounds2 whoosh 
    play sounds4 running
    scene s4_5b184  
    pause 0.6
    scene s4_5b187 with dissolve 
    sel "KILL HIM!"
    play sounds3 mmove 
    scene s4_5b186 with dissolve 
    mc "(Was that…?)"
    mc "(Whatever that was…)"
    play sounds2 glitchfear
    scene s4_5b188 with glitch
    a "I WON’T LET YOU!" 
    play sounds2 whoosh 
    scene s4_5b191 
    pause 0.8
    play sounds3 whoosh 
    scene s4_5b192 
    am "The present path is lost."
    am "I’m sending you to the only man who ever shut the System down."
    am "Go. Find Gorem."
    am "I’ll handle the rest."
    play sounds3 swordhitkalesta
    scene s4_5b193 with vpunch
    a "Wh—"

    scene s4_5b189 with dissolve 
    sel "What are you doing?! We had an agre—"

    
    play sounds2 gateexplousion fadein 1.1 volume 0.5
    scene s4_5b190 with dissolve 
    pause 0.8
    stop sound fadeout 0.5
    scene black with dissolve 
    play sound windscene loop fadein 2.0
    pause 2.1
# 


    scene s4_5c1 with dissolve 
    pause 0.6
    play sounds4 systemnotification
    play sounds2 fall 
    scene s4_5c2 with dissolve 
    "Analysis complete. Condition: critical."
    mc "No. Stay with me."
    mc "(whispering) I won’t…"
    scene s4_5c3 with dissolve 
    mc "Stay awake."
    mc "Don’t close your eyes."
    play sounds2 mmove 
    scene s4_5c4 with dissolve 
    pause 0.8
    scene s4_5c5 with dissolve 
    pause 0.8
    scene s4_5c6 with dissolve 
    a "You could use some help yourself."
    mc "I’ll manage."
    scene s4_5c7 with dissolve 
    a "..."
    scene s4_5c8 with dissolve 
    a "There’s a hole in her chest."
    a "She’s dying."
    scene s4_5c9 with dissolve 
    mc "Hey, Kali. Can you hear me?" 
    mc "Don’t you dare pass out!"
    scene s4_5c10 with dissolve 
    mc "You hear me?"
    mc "Just… don’t."
    play sounds2 bodytap  
    scene s4_5c11 with dissolve 
    k "(He’s trying so hard… For someone like me?)"
    k "...leave me. I—"
    scene s4_5c12 with dissolve 
    mc "It’s not your time. Got it?"
    k "…yeah."
    mc "Go chase that dream of yours."
    scene s4_5c13 with dissolve 
    mc "Become the best damn actress out there."
    pause 0.6
    k "Don’t go crying on me…"
    k "old man…"
    scene s4_5c14 with dissolve 
    mc "Hey, Kali, stay with me. Don’t close your—"
    play sounds4 systemnotification
    "Blood loss exceeds critical—"
    scene s4_5c15 with dissolve 
    mc "(God, he’s getting on my nerves.)"
    mc "(If I keep listening to him, she’s going to die.)"
    play sounds2 hdshot
    scene s4_5c16 with dissolve 
    mc "Screw it."
    scene s4_5c17 with dissolve 
    pause 0.6
    a "Ironic. {w=0.7}Fighting so hard to save the one who was ready to kill you."
    scene s4_5c18 with dissolve 
    pause 0.8
    scene s4_5c19 with dissolve 
    mc "...but she didn’t."
    scene s4_5c20 with dissolve 
    pause 0.6
    mc "I’ve ruined more lives than I can count."
    mc "Too many…"
    scene s4_5c4 with dissolve 
    pause 0.8
    scene s4_5c5 with dissolve 
    pause 0.8
    scene s4_5c7 with dissolve 
    a "And saving this girl—"
    a "is that your redemption?"
    mc "..."
    scene s4_5c20 with dissolve 
    mc "Redemption… don’t flatter me."
    mc "More like… doing one useful thing in my life."
    scene s4_5c21 with dissolve 
    mc "Pathetic, I know."
    a "..."
    a "(I don’t understand him. {w=0.8}Why go this far for a piece of flesh that’s already used up?)"
    scene s4_5c22 with dissolve 
    a "..."
    a "(Strange man.)"
    a "(And yet… I want to help.)"
    a "...There is another way."
    pause 1.1
    a "The miasma."
    scene s4_5c23 with dissolve 
    mc "That would kill her."
    play sounds2 mmove 
    scene s4_5c24 with dissolve
    a "Or save her."
    scene s4_5c25 with dissolve
    mc "..."
    play sounds2 clench 
    scene s4_5c26 with dissolve 
    a "They’ll either save her…"
    a "Or turn her into one of those Soulless you’ve been killing."
    scene s4_5c27 with dissolve 
    mc "(If that’s what it takes for her to live…)"
    mc "(And if it fails, I’ll have to be the one to kill her.)"
    scene s4_5c28 with dissolve 
    mc "...Damn it."
    mc "(I hope it doesn’t come to that.)"
    mc "Please… live."
    scene s4_5c29 with dissolve 
    pause 0.8
    play sounds2 hdshot 
    scene s4_5c30 with dissolve 
    pause 0.6
    play sounds3 mmove 
    scene s4_5c32 with dissolve
    a "(What am I doing? Using miasma like this breaks the Codex.)" 
    mc "Done. What now?"
    
    a "..."
    scene s4_5c33 with dissolve 
    a "It’s too cold here. She needs warmth."
    stop sound fadeout 0.5
    play sounds1 windinhouse fadein 0.5 loop volume 0.5
    scene s4_5c35 with dissolve 
    pause 1.5
    play sounds2 hit1 
    scene s4_5c36 with vpunch  
    mc "(whispering) Warmer… works better, right? …Flora?"
    scene s4_5c37 with dissolve 
    pause 0.7
    scene s4_5c38 with dissolve 
    pause 0.8
    play sounds2 mmove 
    scene s4_5c39 with dissolve 
    mc "(Dusty. Filthy. No one’s been here in years.)"
    scene s4_5c40 with dissolve 
    mc "(Warm enough. If only I could find a bed… something to cover her.)"
    play sounds2 mmove 
    scene s4_5c41 with dissolve 
    mc "But where…"

    play sounds2 whoosh 
    scene s4_5ff20 
    pause 1.1
    play sounds3 mmove 
    scene s4_5ff21 
    mc "No, no— don’t you dare die on me, you hear?! Don’t you dare!"
    mc "Why isn’t the miasma working?!"
    scene s4_5ff22 with dissolve 
    a "..."
    a "It is."
    mc "But her condi—"
    scene s4_5ff28 with dissolve 
    a "The miasma is keeping her cells active. Without it, she’d already be dead."
    a "But it will keep spreading until it takes control."
    a "Your fight is only beginning."
    a "Don’t let it reach the rest of her body."
    scene s4_5ff27 with dissolve 
    mc "What? But you said—"
    a "It’s a virus, not a cure."
    mc "Then how?"
    a "The lighter."
    a "Seal the infected tissue before it spreads farther."
    play sounds2 mmove 
    play sounds3 ligther1
    scene s4_5ff23 with dissolve 
    mc "Now?"
    a "Cauterize the wound."
    mc "..."
    scene s4_5ff24 with dissolve 
    mc "You’re kidding me..."
    a "..."
    mc "Make her suffer even more?! What, you think I’m a sadist?!"
    scene s4_5ff25 with dissolve 
    a "You kept her alive."
    scene s4_5ff26 with dissolve 
    mc "That’s torture!"
    scene s4_5ff25 with dissolve 
    a "You took that risk."
    a "Now see it through."
    scene s4_5ff24 with dissolve 
    mc "...Damn it."
    scene black with dissolve 
    k "AAAAAAAAAAAAAAA..."
    "A scream of burning agony and sheer terror split the air."
    $ persistent.chapter_act4_5_scene += 1

# Сцена 3.
label story05_5_3:
    stop music fadeout 0.5
    stop music1 fadeout 2.2
    scene black with dissolve 
    pause 3.2

    scene black with dissolve
    pause 5.2
    show act4s3 with dissolve
    pause 1.5
    show act4s3_1 with dissolve
    pause 2.1
    scene black with dissolve
    pause 1.2

    scene s4_5c70 with dissolve 
    show act4_s7 with dissolve 
    "Several hours later."
    
    scene s4_5c42 with dissolve 
    mc "(Her screams… and now she’s just lying there, asleep…)"
    mc "(It’s… calming. But is she better? Worse? I can’t stop overthinking it.)"
    pause 1.1
    mc "(All I can do is wait. Let her rest.)"
    play sounds2 knifeput
    mc "(And then what?)"
    scene s4_5c43 with dissolve 
    play sounds4 squeezi1
    mc "Arkh…"
    mc "(You threw yourself into that abyss without thinking.)"
    mc "(Yeah. We’re alive.)"
    mc "(For now.)"
    play sounds2 bint1
    scene s4_5c44 with dissolve 
    mc "(No food. Barely any water. If we stay here, we’re dead.)"
    mc "(But we can’t leave either. And even if we could, where to?)"
    play sounds4 squeezi2
    mc "Mm… come on…"
    scene s4_5c45 with dissolve 
    mc "(Done.)"
    play sounds2 knifeput
    scene s4_5c46 with dissolve 
    pause 0.7
    play sounds3 mmove 
    scene s4_5c47 with dissolve 
    pause 0.8
    play sounds4 tablesq 
    scene s4_5c48 with dissolve 
    mc "Still second-guessing your decision?"
    mc "Don’t. We’re past that."
    scene s4_5c49 with dissolve 
    a "After analyzing the situation…"
    a "For the first time, I don’t know what to tell you."
    mc "What about our location? Do you know where we are?"
    scene s4_5c50 with dissolve 
    a "Hard to say precisely."
    pause 0.6
    a "Looks like an old elven colony. According to my estimates, it’s still operational."
    play sounds2 stepler
    scene s4_5c51 with dissolve 
    mc "…Damn."
    scene s4_5c53 with dissolve 
    mc "You’re sure?" 
    play sounds2 stepler
    mc "Another fight would be a terrible idea."
    mc "Especially with Kali in this state."
    play sounds2 stepler
    scene s4_5c55 with dissolve 
    a "Elves are a peaceful people. They won’t strike first."
    scene s4_5c53 with dissolve 
    mc "Did you forget? We fought the elven Empress just hours ago."
    mc "And we were the ones defending ourselves."
    play sounds2 stepler
    scene s4_5c54 with dissolve 
    a "Her methods… were an exception."
    mc "..."
    play sounds4 tablesq 
    play sounds3 mmove 
    scene s4_5c56 with dissolve 
    mc "(I need to scout the area.)"
    mc "(If possible, find food… and somewhere better.)"
    scene s4_5c57 with dissolve 
    mc "(And at the same time, leaving her alone…)"
    play sounds3 mmove 
    scene s4_5c58 with dissolve 
    pause 0.9
    scene s4_5c59 with dissolve 
    mc "She’s burning up."
    scene s4_5c58 with dissolve 
    a "Her body is fighting the miasma."
    a "That’s a good sign."
    mc "I hope so."
    play sounds3 mmove 
    scene s4_5c60 with dissolve 
    k "…no… I don’t want to…"
    k "die…"
    play sounds3 clench 
    scene s4_5c61 with dissolve 
    mc "Easy. Easy."
    mc "It’s alright. You’re doing fine."
    scene s4_5c62 with dissolve 
    mc "You will."
    mc "I promise."
    scene s4_5c64 with dissolve 
    pause 1.1
    scene s4_5c63 with dissolve 
    mc "An elven colony, then…"
    mc "Tell me, could they help us?"
    scene s4_5c64 with dissolve 
    a "The probability is extremely low."
    a "But not zero, if we play this right."
    
    scene black with dissolve 
    "A few minutes later."
    scene s4_5ff46 with dissolve 
    keep3 "That was reckless."
    scene s4_5ff47 with dissolve 
    mc "You think?"
    scene s4_5ff46 with dissolve 
    keep3 "Ripping it out of your head wasn’t rational."
    scene s4_5ff47 with dissolve 
    mc "Her life was on the line."
    scene s4_5ff46 with dissolve 
    keep3 "..."
    scene s4_5ff48 with dissolve 
    keep3 "Next time, think it through."
    keep3 "I’d rather not cease to exist along with you."
    mc "(Since we’re on the subject… how does a tiny chip like that hold so much power?)"
    scene s4_5ff49 with dissolve 
    keep3 "The power isn’t in the chip. It only removes the limiter."
    scene s4_5ff50 with dissolve 
    pause 1.1
    scene s4_5ff51 with dissolve 
    mc "(Elaborate.)"
    scene s4_5ff56 with dissolve 
    keep3 "Your body is a weapon."
    keep3 "Not metaphorically."
    keep3 "Not theoretically."
    keep3 "Literally."
    scene s4_5ff52 with dissolve 
    keep3 "From head to toe, you’re packed with implants."
    mc "(And the chip keeps them in check. Am I right?)"
    scene s4_5ff53 with dissolve 
    keep3 "They’re afraid you might become a problem."
    scene s4_5ff54 with dissolve 
    mc "Different world. Same methods."
    mc "Almost funny."
    mc "So without the chip… the implants are useless?"
    scene s4_5ff55 with dissolve 
    keep3 "..."
    keep3 "Yes."
    scene s4_5ff54 with dissolve 
    mc "I see."
    mc "And there’s no way around the restrictions?"
    scene s4_5ff56 with dissolve 
    keep3 "There are ways."
    keep3 "But they aren’t rational."
    keep3 "And you wouldn’t be able to use them freely."
    scene s4_5ff57 with dissolve 
    keep3 "Slowly. Step by step. Your body is destroying itself."
    keep3 "Using them only accelerates the process."
    scene s4_5ff58 with dissolve 
    pause 2.1
    scene s4_5ff59 with dissolve 
    mc "Power always comes at a cost… doesn’t it?"
    scene s4_5ff58 with dissolve 
    keep3 "There are alternatives."
    keep3 "The Federation simply doesn’t need them."
    keep3 "Or more precisely, they aren’t cost-effective."
    scene s4_5ff61 with dissolve 
    mc "Meaning?"
    scene s4_5ff60 with dissolve 
    keep3 "Two factors."
    keep3 "Not financially viable."
    keep3 "And…"
    scene s4_5ff58 with dissolve 
    keep3 "The elves are the only ones capable of reinstalling implants."
    keep3 "And relations with them… are strained."
    scene s4_5ff59 with dissolve 
    mc "I figured."


    play sounds3 mmove 
    scene s4_5c65 with dissolve 
    mc "(Ammo’s intact. Count…)"
    mc "(Not great. One magazine.)"
    play sounds4 rustling2 
    scene s4_5c66 with dissolve 
    mc "You sure leaving her alone is a good idea?"
    a "Her survival contradicts my logic entirely."
    a "You’ll have to decide that one yourself."
    play sounds3 mmove 
    scene s4_5c67 with dissolve 
    mc "Figures."
    scene s4_5c68 with dissolve 
    mc "(Then let’s move.)"
    stop sounds1 fadeout 2.5

    scene black with dissolve 
    play sounds2 closedoor1
    play sound windscene loop fadein 2.0 volume 0.5
    pause 1.2
    play music s45c3mcscene fadein 9.2
    play sounds walkingwater loop fadein 1.2 volume 0.2
    pause 3.2 

    scene s4_5c72 with dissolve 
    mc "Beautiful…"
    a "Ruins and overgrowth."
    a "There’s nothing beautiful about decay."
    mc "Depends how you look at it."
    stop sounds fadeout 0.5
    scene s4_5c75 with dissolve 
    mc "(No signs of life. Hard to believe anyone’s been—)"
    a "You still have the implant?"
    scene s4_5c76 with dissolve 
    mc "Yeah. Why?"
    play sounds2 mmove 
    scene s4_5c77 with dissolve 
    a "Don’t use it. Elves don’t tolerate implants."
    mc "Why not?"
    scene s4_5c79 with dissolve 
    a "Just advice."
    mc "(What changed him? He’s… unusually talkative.)"
    scene s4_5c78 with dissolve 
    mc "Noted."
    play sounds walkingwater loop fadein 1.2 volume 0.2
    scene s4_5c80 with dissolve 
    pause 0.8
    scene s4_5c81 with dissolve 
    pause 0.8
    scene s4_5c82 with dissolve 
    mc "(An elven colony… so not Earth.)"
    mc "(Which means the Gate experiment failed?)"
    scene s4_5c83 with dissolve 
    mc "White mask... No. What should I call you?"
    keep3 "Third."
    keep3 "Names mean nothing to us."
    scene s4_5c85 with dissolve 
    mc "Strange customs."
    mc "Back to the point, the gate."
    mc "Something went wrong, didn’t it? This isn’t the Abyss. And it’s definitely not Earth."
    scene s4_5c86 with dissolve 
    keep3 "We were displaced in time. Not speculation. Fact."
    keep3 "The question is, {b}when.{/b}"
    scene s4_5c88 with dissolve 
    mc "That bad?"
    keep3 "Very. If we plan on getting out."
    scene s4_5c87 with dissolve 
    pause 0.7
    scene s4_5c89 with dissolve 
    pause 0.6
    stop sounds
    scene s4_5c98 with dissolve 
    mc "What about the statues? Can they tell us anything?"
    keep3 "I’m a Keeper. Not omniscient."
    mc "What’s the difference? You always sounded all-knowing to me."
    scene s4_5c90 with dissolve 
    keep3 "..."
    keep3 "Going to war, would you take a sword, or a book?"
    scene s4_5c99 with dissolve 
    mc "Depends what you’re planning to do there. Doesn’t it?"
    pause 0.7
    keep3 "A fair point."
    keep3 "And your answer, no."
    keep3 "I’m not all-knowing. I’m a weapon."
    scene s4_5c97 with dissolve 
    mc "(A statue of a girl. Strange ruins.)"
    mc "(Nothing useful.)"
    play sounds2 mmove 
    scene s4_5c91 with dissolve 
    pause 0.8
    scene s4_5c92 with dissolve 
    mc "(If there’s nothing here, I should go higher.)"
    mc "(Wait. Dead end?)"
    scene s4_5c97 with dissolve 
    mc "(And here too.)"
    scene s4_5c94 with dissolve 
    mc "..."
    scene s4_5c95 with dissolve 
    mc "Purely theoretical, what are the odds there’s no way out?"
    keep3 "..."
    scene s4_5c94 with dissolve 
    keep3 "The fact we survived unstable gates at all was already a miracle."
    play sounds2 mmove
    scene s4_5c97 with dissolve 
    mc "(Time to check something.)"
    play sounds3 ha
    scene s4_5c100 with dissolve 
    pause 0.9
    scene s4_5c101 with dissolve 
    "Analysis complete. Optimal route constructed."
    scene s4_5c102 with dissolve 
    keep3 "Implants."
    mc "I know. Still."
    play sounds2 mmove 
    play sounds3 running 
    scene s4_5c103 with dissolve 
    pause 1.2
    play sounds3 mcjump3 
    scene s4_5c104 with dissolve 
    pause 0.8
    play sounds2 mcjump4 volume 5.3
    scene s4_5c105 with vpunch 
    pause 1.1
    scene s4_5c106 with dissolve 
    pause 0.9
    play sounds3 mcjump3
    scene s4_5c107 with dissolve 
    mc "Let’s—"
    play sounds2 mcjump4
    play sounds4 hit2
    scene s4_5c108 with vpunch 
    mc "(Got it.)"
    play sounds3 clench
    scene s4_5c109 with dissolve 
    pause 0.9
    play sounds2 mmove 
    scene s4_5c110 with dissolve 
    pause 0.8
    scene s4_5c111 with dissolve 
    mc "(So maybe it’s not completely hopeless.)"
    mc "I see a passage beyond the rocks."
    scene s4_5c112 with dissolve 
    mc "But how do I get there?" 
    mc "No, wrong question."
    mc "How do I get there {b}with Kalestra…{/b}"
    scene s4_5c119 with dissolve 
    keep3 "Still haven’t changed your mind?"
    mc "Sounds like you’re hoping I will. Personal dislike?"
    keep3 "No comment."
    stop music fadeout 3.3
    play sounds2 ha 
    scene s4_5c120 with dissolve 
    "Threat detected. Enemy at seven o’clock."
    play music1 dream1 fadein 5.4
    scene s4_5c121 with dissolve 
    mc "(Just what I needed.)"
    play sounds walkingwater loop fadein 1.2 volume 0.2

    scene s4_5c122 with dissolve 
    pause 0.8 
    scene s4_5c123 with dissolve 
    mc "(Alone. With flowers? …What the hell is this?)"
    stop sounds 
    scene s4_5c124 with dissolve 
    Go "..."
    scene s4_5c125 with dissolve 
    Go "{font=Cybertron.otf}You are as radiant as you were the day we parted, Viola.{/font} \n(You are as radiant as you were the day we parted, Viola.)"
    scene s4_5c126 with dissolve 
    mc "(What language is that? Third, I need you.)"
    scene s4_5c127 with dissolve 
    keep3 "Ancient Elvish. I’ve never heard it spoken aloud before."
    mc "Do you understand him?"
    keep3 "Enough. It’s reserved for the highest circles of power."
    scene s4_5c128 with dissolve 
    mc "So he’s important."
    mc "Lucky us…"
    play sounds2 mmove 
    scene s4_5c129 with dissolve 
    Go "{font=Cybertron.otf}So it is…{/font} \n(So it is…)"
    scene s4_5c130 with dissolve 
    Go "{font=Cybertron.otf}Forgive our new guests. They did not know what they were doing.{/font} \n(Forgive our new guests. They did not know what they were doing.)"
    scene s4_5c131 with dissolve 
    keep3 "He knows we’re here."
    mc "Wh— The implant?"
    keep3 "That too. But not only that."
    scene s4_5c132 with dissolve 
    keep3 "He’s… strange."
    mc "(Strange? No. He’s unsettling.)"
    play sounds2 mmove 
    scene s4_5c134 with dissolve 
    pause 0.8
    scene s4_5c133 with dissolve
    Go "{font=Cybertron.otf}May I inquire, honored ones… from where do you hail?{/font} \n(May I inquire, honored ones… from where do you hail?)"
    scene s4_5c135 with dissolve 
    keep3 "Advice. Do not attempt to harm him. Under any circumstances."
    scene s4_5c136 with dissolve 
    mc "(As if I could.)"
    scene s4_5c137 with dissolve 
    mc "..."
    scene s4_5c139 with dissolve 
    Go "{font=Cybertron.otf}Ah, do not be afraid. I come in peace.{/font} \n(Ah, do not be afraid. I come in peace.)"
    play sounds2 mmove 
    scene s4_5c140 with dissolve 
    mc "You speak our language?"
    Go "(Human?)" 
    Go "So you are human. Forgive my manners."
    play sounds2 mmove 
    scene s4_5c133 with dissolve 
    Go "But with all due respect… would you kindly lower your weapon, monsieur?"
    scene s4_5c134 with dissolve 
    mc "I can’t."
    Go "..."
    scene s4_5c133 with dissolve 
    Go "You and that girl… you are not of this time. Correct?"
    scene s4_5c134 with dissolve 
    mc "(How—? No. Don’t react. Keep your face still.)"
    mc "(You don’t know what he wants. Don’t give him anything.)"
    scene s4_5c138 with dissolve 
    Go "I can offer you shelter."
    mc "..."
    scene s4_5c133 with dissolve 
    mc "And why the generosity?"
    Go "You required it. And I aid those in need."
    scene s4_5c140 with dissolve 
    mc "Guarantees?"
    Go "My word."
    mc "A life balanced on your word? That’s thin."
    Go "It is all I possess. That… and my life. Though I doubt you came seeking that."
    scene s4_5c141 with dissolve 
    pause 0.8
    scene s4_5c140 with dissolve 
    mc "Lead the way."
    stop music1 fadeout 2.5
    scene black with dissolve 
    pause 3.3

    play sounds walkingwater loop fadein 1.2 volume 0.2
    scene s4_5c142 with dissolve 
    mc "(Can’t stray more far away from Kali. And at the same time, I have no choice.)"
    mc "(Just have to believe she’ll be fine…)"
    scene s4_5c143 with dissolve 
    mc "(First, deal with this.)"
    play sounds2 ha 
    "Analysis: Two entities. Three o’clock."
    scene s4_5c144 with dissolve 
    mc "(An ambush?!)"
    scene s4_5c145 with dissolve 
    mc "No… doesn’t feel like it."
    play sounds2 ha 
    scene s4_5c146 with dissolve 
    "Analysis complete. Elves. No hostile intent detected."
    mc "(Curious, maybe?)"
    scene s4_5c147 with dissolve 
    mc "(No… those eyes.)"
    mc "(They’re afraid.)"
    scene s4_5c148 with dissolve 
    Go "Forgive us for not receiving you with proper honors."
    Go "The persecution of my people has… intensified."
    play sounds2 mmove 
    scene s4_5c149 with dissolve 
    Go "And seeing you escort me at gunpoint does little to ease tensions."
    Go "So I ask, do not mistake their actions for insult."
    scene s4_5c150 with dissolve 
    mc "(He doesn’t look hostile. Quite the opposite.)"
    mc "(Almost painfully courteous.)"
    mc "(Which is worse.)"
    mc "(If he wanted me dead, I’d already be bleeding out.)"
    mc "(So killing me isn’t the objective.)"
    play sounds2 mmove 
    scene s4_5c151 with dissolve 
    mc "(Fine. I’ll lower the aggression.)"
    mc "(But not my guard.)"
    scene s4_5c152 with dissolve 
    pause 1.2
    play sounds2 mmove 
    scene s4_5c154 with dissolve 
    Go "Thank you… for that sliver of trust."
    play sounds3 ha
    play music1 inquisition fadein 0.5
    scene s4_5c156 with dissolve 
    "Critical threat detected!"
    scene s4_5c157 
    pause 0.7
    play sounds swordswing
    scene s4_5c155 
    pause 0.9
    play sounds2 punch1
    scene s4_5c158 with vpunch 
    pause 1.1
    play sounds3 punch1
    scene s4_5c159 with vpunch 
    pause 0.8
    play sounds2 mmove 
    scene s4_5c161
    pause 0.8
    scene s4_5c162 with dissolve 
    mc "Don’t."
    mc "Move."
    play sounds2 waterfall
    scene s4_5c160 with vpunch 
    sel "Arkh—!"
    Go "Lá istalyë tenno… \n(You never learn…)"
    scene s4_5c163 with dissolve 
    mc "You—"
    scene s4_5c164 with dissolve 
    sel "Man cenich na nin, adan fael? \n(What are you staring at, human?)"
    play sounds2 ha 
    play sounds3 glitchfear
    scene s4_5c165 with glitch 
    "Critical threat detected!"
    scene s4_5c166 with dissolve 
    mc "(Yong? That uniform—)"
    mc "(What the hell is going on?)"
    play sounds2 mmove 
    scene s4_5c167 with dissolve 
    pause 0.8
    scene s4_5c168 with dissolve 
    Go "I deeply apologize for this misunderstanding."
    Go "Please, forgive my daughter’s foolishness."
    Go "And if possible… refrain from turning her head into liquid pulp."
    scene s4_5c169 with dissolve 
    mc "If I did, I’d be next. Wouldn’t I?"
    scene s4_5c168 with dissolve 
    Go "I sincerely hope you do not force my hand."
    scene s4_5c169 with dissolve 
    pause 0.6
    mc "Call off your guards."
    scene s4_5c168 with dissolve 
    Go "Guarantees?"
    scene s4_5c169 with dissolve 
    mc "My word."
    mc "That’s how this works, right?"
    Go "..."
    play sounds2 mmove 
    scene s4_5c167 with dissolve 
    pause 0.8
    play sounds3 glitchfear
    scene s4_5c170 with glitch 
    mc "(He… kept it. He actually kept his word.)"
    mc "(I still don’t buy it. But what about her?)"
    mc "(That’s Selvaria. No doubt.)"
    mc "(If I kill her now—)"
    play sounds2 mmove 
    scene s4_5c171 with dissolve 
    mc "(I die with her.)"
    mc "(Betray my principles, again.)"
    mc "(But save the galaxy.)"
    mc "..."
    play sounds2 mmove 
    stop music1 fadeout 6.8
    scene s4_5c172 with dissolve 
    mc "(No.)"
    mc "(Too many variables.)"
    play sounds2 mmove 
    scene s4_5c173 with dissolve 
    mc "(I just hope this doesn’t become the decision I regret most.)"
    play sounds3 mmove 
    play sounds4 waterfall 
    scene s4_5c174 with dissolve 
    pause 1.1
    scene s4_5c176 with dissolve 
    sel "Ú-berio nin na dîn, adan dûr! \n(Don’t you dare touch me with your filthy hands, human.)"
    scene s4_5c177 with dissolve 
    mc "(Wait… I can understand her? The implant?)"
    keep3 "(Exactly.)"
    mc "Bold words… for someone who was face-down in the dirt a moment ago."
    scene s4_5c176 with dissolve 
    sel "Mi maeth oen aen, er oen… \n(In a proper duel, one on one, I would—)"
    scene s4_5c177 with dissolve 
    Go "(whispering) Ce i dhûr nîn veleg… \n(You are my undoing…)"
    Go "Selv. Basta na i gwaith. \n(Selv. Enough.)"
    Go "Ce dagor danna. \n(You lost. Accept it with dignity.)"
    Go "Telio i chîr a bado ennas. \n(End this circus.)"
    play sounds2 mmove 
    scene s4_5c178 with dissolve 
    sel "I thûr lín a i nîf lín… \n(You and your precious principles…)"
    sel "Bado hen na chen. \n(Keep them to yourself.)"
    scene s4_5c179 with dissolve
    sel "(whispering) Sui nedhannen veleg… \n(How far we’ve fallen…)"
    sel "(whispering) I hen cûr na adan bân. \n(That he bows this low before an ordinary mortal.)"
    Go "..."
    play sounds3 mmove 
    scene s4_5c168 with dissolve
    Go "My apologies."
    Go "Would you kindly wait for me here?"
    scene s4_5c169 with dissolve 
    mc "Do we have a choice?"
    scene s4_5c168 with dissolve
    Go "No."
    scene s4_5c169 with dissolve 
    pause 2.1
    scene s4_5c168 with dissolve 
    Go "Had you agreed from the beginning… we might have avoided this awkwardness."

    scene black with dissolve 
    "Few minutes later."

    play music schemingw fadein 3.3
    play sounds2 whoosh
    scene s4_5c184 with CropMove(time=0.1, mode='slideleft')
    pause 1.1
    play sounds2 whoosh 
    scene s4_5c180 with CropMove(time=0.1, mode='slideright')
    pause 1.7
    play sounds2 whoosh 
    scene s4_5c182 with CropMove(time=0.1, mode='slideup')
    mc "(whispering) They’re afraid."
    mc "(And at the same time… curiosity’s winning.)"
    play sounds2 whoosh 
    scene s4_5c183 with dissolve
    keep3 "It always does with them."
    keep3 "They’ve never been able to resist something new."
    play sounds3 mmove 
    play sounds2 whoosh
    scene s4_5c184 with CropMove(time=0.1, mode='slideleft')
    pause 1.1
    scene s4_5c185 with dissolve
    mc "Like that elven scientist, hm?"
    keep3 "..."
    keep3 "His sector wasn’t under my jurisdiction."
    stop music fadeout 1.7
    pause 1.2
    Go "Please. This way."
    scene s4_5c186 with dissolve 
    "Elven Village."
    play sounds walkingwater loop fadein 1.2 volume 0.2
    scene s4_5c189 with dissolve 
    mc "(Empty. Too empty.)"
    mc "(And the smoke… thick. Bitter. Hard to breathe.)"
    mc "Forgive me. I can’t go any farther."
    scene s4_5c187 with dissolve 
    Go "Is something… displeasing you?"
    mc "(I’ve gone too far from Kalestra. And if—)"
    scene s4_5c157 with dissolve 
    mc "I need to return."
    mc "I have to make sure she’s alright."
    Go "Ah. Your companion."
    stop sounds 
    play music1 backgroundsus fadein 0.7
    scene s4_5c156 with dissolve
    Go "My guards have already seen to her."
    mc "What—"
    play sounds2 mmove 
    scene s4_5c162 
    Go "Do not concern yourself."
    Go "She is in relative safety."
    mc "I didn’t ask you to do that."
    scene s4_5c152 with dissolve
    Go "..."
    play sounds2 mmove 
    scene s4_5c168 with dissolve
    Go "Please, do not misunderstand me."
    Go "A human child with a hole in her chest… filled with miasma."
    scene s4_5c162 with dissolve
    Go "At best, that is poor etiquette."
    Go "At worst… a declaration of war."
    Go "Anyone else in my position would have eliminated you on the spot."
    mc "(Third. Credibility?)"
    keep3 "(whispering) You saw what happened to the Federation."
    keep3 "He’s not lying."
    play sounds3 mmove 
    scene s4_5c150 with dissolve
    mc "(So what is this, then?)"
    mc "(We’re hostages?)"
    keep3 "(whispering) No. You’re a curiosity."
    keep3 "His new toy."
    scene s4_5c149 with dissolve
    mc "(Curiosity…?)"
    keep3 "(whispering) Yes. Don’t give him everything."
    keep3 "Mystery is leverage. It’s how we stay alive."
    scene s4_5c156 with dissolve
    mc "So you’re saying… she’s safe?"
    mc "Fine."
    play sounds4 mmove 
    scene s4_5c153 with dissolve
    Go "Thank you for your understanding."
    scene s4_5c188 with dissolve
    mc "(I folded too quickly.)"
    mc "(Hooked on his civility like an amateur.)"
    keep3 "(whispering) Let that be your lesson."
    scene s4_5c190 with dissolve
    pause 4.3
    stop sound fadeout 0.5 
    stop music1 fadeout 5.5
    $ persistent.chapter_act4_5_scene += 1
    

# Сцена 4.
label story05_5_4:
    stop music fadeout 0.5
    scene black with dissolve 
    pause 2.2
    play music s45c4mcscene fadein 5.5 
    play sounds1 windinhouse fadein 0.5 loop volume 0.4 
    scene s4_5c196 with dissolve
    pause 3.2
    scene s4_5c204 with dissolve
    mc "(That feeling again.)"
    mc "(Tight chest. Measured air.)"
    mc "(Like I’m back in Astoria’s office, being dissected without a blade.)"
    play sounds2 mmove 
    scene s4_5c197 with dissolve
    Go "So."
    Go "Why did Astoria send her hounds to me?"
    scene s4_5c198 with dissolve
    mc "How long have you known?"
    scene s4_5c199 with dissolve
    pause 2.1
    scene s4_5c200 with dissolve
    pause 1.1
    scene s4_5c201 with dissolve
    Go "Allow me to introduce myself properly."
    Go "Goremilion Aeliren Taer-Sylv."
    scene s4_5c200 with dissolve
    pause 1.1
    scene s4_5c223 with dissolve
    pause 2.1
    scene s4_5c222 with dissolve
    mc "The Elven Emperor himself. I assume."
    scene s4_5c223 with dissolve
    pause 0.8
    scene s4_5c224 with dissolve
    Go "..."
    scene s4_5c225 with dissolve
    Go "Emperor…"
    Go "Interesting choice of words."
    Go "You are the first to call me that."
    scene s4_5c223 with dissolve
    mc "(What?)"
    mc "(But Selvaria was called Empress. So either—)"
    play sounds3 glitchfear
    scene s4_5c220 with glitch 
    keep3 "(whispering) Bad news."
    keep3 "(whispering) We’ve been thrown back 97 years."
    mc "..."
    scene s4_5c218 with dissolve
    Go "You are no ordinary young man."
    scene s4_5c224 with dissolve
    pause 1.1
    scene s4_5c226 with dissolve
    pause 1.2
    scene s4_5c240 with dissolve
    Go "Especially your companion."
    Go "The Third Keeper. Am I correct?"
    scene s4_5c219 with dissolve
    keep3 "I underestimated him."
    scene s4_5c220 with dissolve
    pause 1.2
    scene s4_5c221 with dissolve
    mc "What exactly do you know about us?"
    scene s4_5c220 with dissolve
    Go "Enough to let you live."
    scene s4_5c229 with dissolve
    pause 1.2
    scene s4_5c227 with dissolve
    pause 1.2
    scene s4_5c228 with dissolve
    Go "In trying to save this girl… you attempted to go to the gate"
    scene s4_5c233 with dissolve
    Go "And failed."
    Go "Why?"
    scene s4_5c229 with dissolve
    pause 2.1
    scene s4_5c235 with dissolve
    Go "Did something interfere."
    scene s4_5c234 with dissolve
    Go "Or perhaps...someone."
    scene s4_5c229 with dissolve
    pause 1.1
    scene s4_5c220 with dissolve
    pause 1.1
    scene s4_5c221 with dissolve
    mc "Astoria asked us to meet you."
    mc "She said you could help."
    scene s4_5c229 with dissolve
    pause 2.1
    scene s4_5c231 with dissolve
    pause 0.7
    scene s4_5c232 with dissolve
    Go "I’m pleased we understand one another."
    scene s4_5c200 with dissolve
    mc "Tell me."
    mc "Have you ever closed an activated Gate?"
    scene s4_5c201 with dissolve
    Go "What’s the catch?"
    scene s4_5c200 with dissolve
    mc "Hypothetical."
    pause 2.1
    scene s4_5c229 with dissolve
    pause 2.1
    scene s4_5c230 with dissolve
    Go "Yes."
    stop music fadeout 11.3
    scene s4_5c227 with dissolve
    pause 0.7
    scene s4_5c196 with dissolve
    Go "I will ensure she survives."
    Go "Nothing more."
    Go "Whether she remains the same hum—"
    scene s4_5c227 with dissolve
    mc "That’s enough."
    scene s4_5c231 with dissolve
    pause 0.8
    scene s4_5c232 with dissolve
    Go "Would you care for a walk?"
    stop sounds1 
    

    scene black with dissolve 
    pause 1.2
    play sounds2 closedoor1
    play sound windscene loop fadein 2.0 volume 0.5
    play music1 s45c5gocscene fadein 5.5
    pause 2.2

    scene s4_5c207 with dissolve
    Go "By nature, we elves are… inquisitive."
    Go "We have always sought to understand how this world is constructed."
    scene s4_5c209 with dissolve
    Go "And at times… that curiosity strayed beyond what was permitted."

    scene s1b15 with dreamyzoom
    show memoryframe
    Mi "Proof that lines were crossed, mistakes made, and debts paid. Paid in blood."
    hide memoryframe
    scene s1b17 with dissolve
    show memoryframe
    Mi "The former leader of our faction, who..." 
    hide memoryframe

    scene s4_5c208 with linearblur
    mc "That scientist."
    Go "Yes, my grandfather."

    scene s4_5d1 with dissolve
    mc "What did he do… exactly?"
    play sounds2 mmove 
    scene s4_5d2 with dissolve
    pause 1.2
    scene s4_5d3 with dissolve
    Go "He attempted to access the Astreon System."
    pause 0.5
    scene s4_5d4 with dissolve
    mc "(whispering) And… what is that?"
    scene s4_5d3 with dissolve
    pause 1.1
    scene s4_5d5 with dissolve
    Go "A tragedy."
    scene s4_5bb10 with dreamyzoom
    pause 1.1
    Go "For our entire people."
    Go "From that moment on… we became enemies of the galaxy."
    scene s4_5bb11 with dissolve
    pause 4.2
    scene s4_5bb12 with dissolve
    pause 4.2
    scene s4_5d4 with linearblur
    mc "Why?"
    scene s4_5d3 with dissolve
    pause 2.2 
    scene s4_5d1 with dissolve
    keep3 "There are rules in this galaxy."
    keep3 "Lines that are not to be crossed"
    scene s4_5d6 with dissolve
    keep3 "One of them states: What has happened… must be paid for."
    scene s4_5d8 with dissolve
    keep3 "They broke that rule."

    keep3 "They went against time itself."
    keep3 "And in return… all of us paid for their mistake."
    scene s4_5d6 with dissolve
    pause 1.1
    scene s4_5d7 with dissolve
    mc "None of us are without sin."
    keep3 "..."

    play sounds3 clothess 
    scene s4_5d24 with dissolve
    pause 0.9
    scene s4_5d23 with dissolve
    Go "What do you see?"
    scene s4_5d9 with dissolve
    pause 2.2
    mc "A Gate."
    Go "Days. Weeks. Years. Decades… Time kept moving."
    scene s4_5d11 with dissolve
    Go "And with it… our curiosity grew."
    scene s4_5d10 with dissolve
    pause 1.1
    play sounds2 mmove 
    scene s4_5d12 with dissolve
    pause 0.7
    scene s4_5d13 with dissolve
    Go "Long lives are a blessing. {w=0.7}And a curse."
    Go "When you live long enough… meaning begins to rot."
    scene s4_5d14 with dissolve
    pause 1.2
    scene s4_5d15 with dissolve
    pause 0.6
    scene s4_5d19 with dissolve
    Go "So many of us cling to research."
    Go "To discovery."
    Go "To prying open doors that should remain closed."
    scene s4_5d3 with dissolve
    Go "My grandfather was no exception."
    Go "He believed that uncovering the truth of the Gates would let us step beyond the limits of the possible."
    scene s4_5d2 with dissolve
    Go "..."
    scene s4_5d5 with dissolve
    Go "What he didn’t know…"
    Go "Was about the price."
    scene s4_5bb15 with dreamyzoom 
    Go "None of us did."
    Go "So he activated the Gate."
    play sounds3 warptravaling fadein 0.6 loop
    scene s4_5d111 with dissolve
    Go "And time stopped."
    scene s4_5d113 with dissolve
    pause 1.1
    scene s4_5d114 with dissolve
    Go "Not metaphorically."
    Go "Literally."
    scene s4_5d115 with dissolve
    Go "The world… froze."
    play sounds2 mmove 
    scene s4_5d116 with dissolve
    Go "Like someone pressed pause."
    scene s4_5d117 with dissolve
    pause 1.6
    stop sounds3 fadeout 0.4
    scene s4_5d16 with dissolve
    Go "...and then."
    scene s4_5d17 with dissolve
    pause 2.2
    scene s4_5d18 with dissolve
    Go "In the next second…"
    scene s4_5bb14 with dreamyzoom
    Go "My father. My mother. My friends."
    scene s4_5bb16 with dissolve
    Go "Gone."
    scene s4_5d18 with dissolve
    Go "(whispering) Vanished…"
    Go "(whispering) Half of our race."
    Go "(whispering) Half of galaxy."
    Go "(whispering) In a single heartbeat."
    scene s4_5d19 with dissolve
    mc "How…?"
    keep3 "Payment."
    keep3 "For power."
    scene s4_5d20 with dissolve
    pause 1.1
    scene s4_5d21 with dissolve
    keep3 "We didn’t realize…"
    play sounds3 clench 
    scene s4_5d22 with dissolve
    pause 1.1
    scene s4_5bb13 with dreamyzoom 
    keep3 "The Gates were still tethered to the System."
    keep3 "(That was our mistake.)"
    pause 3.4
    

    scene s4_5d26 with dissolve
    Go "Answer me this."
    Go "Why is the blood of the Ancients required to activate a Gate?"
    scene s4_5d25 with dissolve
    mc "It’s the only viable energy source."
    scene s4_5d27 with dissolve
    pause 0.9
    Go "Correct."
    Go "But why?"
    scene s4_5d28 with dissolve
    Go "Because it consumes life."
    Go "To spare your own."
    scene s4_5d29 with dissolve
    mc "..."
    pause 2.3
    mc "Then answer me something."
    mc "If you had stood in his place…"
    mc "Would you have chosen differently?"
    scene s4_5d28 with dissolve
    Go "Knowing the whole truth?"
    scene s4_5d27 with dissolve
    pause 0.9
    Go "Yes."
    Go "…Or at least, I would like to believe so."
    scene s4_5d19 with dissolve
    mc "..."
    mc "Even if the lives of those you love depended on it?"
    Go "There are rules."
    pause 0.5
    scene s3dd20 with dreamyzoom 
    show memoryframe 
    mc "Rules are easy when you’re not the one losing someone."
    hide memoryframe
    
    
    # пауза, Горем отворачивается от мс 
    scene s4_5d25 with dissolve
    pause 2.2
    scene s4_5d26 with dissolve
    Go "So that is what this is about…"
    scene s4_5d25 with dissolve
    mc "She wants her sister back."
    scene s4_5d27 with dissolve
    Go "She knows the risks."
    scene s4_5d19 with dissolve
    pause 1.1
    scene s4_5b192 with dreamyzoom 
    am "Go. Find Gorem."
    am "I’ll handle the rest."
    
    scene s4_5d19 with dissolve
    pause 1.1
    mc "I don’t think she understands them."
    mc "Not really."
    scene s4_5d28 with dissolve
    Go "Did she grow afraid of her own choices?"
    scene s4_5d29 with dissolve
    mc "Maybe."
    mc "Or maybe…"

    scene s4_f139 with dreamyzoom 
    pause 1.1
    scene s4_f140 with dissolve  
    L "Astoria and I are trying to choose the one..."
    L "Where everyone keeps what matters to them."

    scene s4_5d19 with dissolve
    pause 1.1
    mc "There’s still something human left in her."
    mc "(whispering) I hope so."
    stop music1 fadeout 3.2
    
    play music ambient01 fadein 3.3
    play sounds2 whoosh 
    scene s4_5bb19 with CropMove (time=0.1, mode='slideleft')
    elf "Aran nín, thang veleg dâf! \n(Your Highness, we have a problem!)"
    Go "Man danna? \n(What happened?)"
    elf "I sell, hi— \n(The girl, she—)"
    play sounds2 mmove 
    play sounds3 whoosh 
    scene s4_5bb18 
    pause 2.2

    scene black 
    stop sounds fadeout 0.5
    stop sound fadeout 0.5
    play sounds1 windinhouse fadein 0.5 loop volume 0.4 
    pause 2.1 

    
    play sounds3 nve 
    scene s4_5d31 with dissolve
    pause 4.1
    play sounds2 mmove 
    scene s4_5d30 
    ketr "Ánin… ú-aníron baded… \n(Please… I don’t want to die…)"
    k "..."
    
    scene s4_5d45 with dissolve
    play sounds3 closedoor1
    pause 1.7
    play sounds2 mmove 
    scene s4_5d46 with dissolve
    elf "An i lû i echant... \n(When she woke up...)"
    elf "Hîr i naur glam a dantha Ketrin na gîl. \n(She grabbed a shard of glass and immediately took Ketrin hostage.)"
    play sounds2 mmove 
    scene s4_5d47 with dissolve
    pause 0.8
    scene s4_5d32 with dissolve
    Go "Drego i peng. \n(Lower your weapons.)"
    play sounds2 mmove 
    scene s4_5d33 with dissolve
    pause 0.7
    scene s4_5d39 with dissolve
    mc "Easy…"
    mc "They’re not your enemy—"
    stop music fadeout 4.3 
    play music1 mirielwalk fadein 7.5
    scene s4_5d40 with dissolve
    pause 1.4
    play sounds2 whoosh 
    play sounds3 running
    scene s4_5d34 
    pause 0.8
    scene s4_5d35 with dissolve
    pause 1.2
    play sounds3 hug2 
    scene s4_5d36 with vpunch
    mc "Good-"
    play sounds2 mmove 
    scene s4_5d38 with dissolve
    k "You’re… alive."
    scene s4_5d37 with dissolve
    pause 1.1
    mc "Yeah."
    mc "I am."
    
    scene s4_5d41 with dissolve
    Go "Drego. \n(Leave us.)" 
    Go "A tiro na Ketrin. \n(And see to Ketrin.)"
    elf "Nae, Aran nín. \n(Yes, Your Highness.)"
    play sounds3 glitchfear
    scene s4_5d42 with glitch
    pause 1.1 
    play sounds2 footstep2 
    scene s4_5d48 with dissolve
    elf "(whispering) Losto. Ce danna maer. \n(It’ll pass. You did well. You held steady.)"
    scene s4_5d49 with dissolve
    Go "Maer gwaith. \n(Good work.)"
    ketr "Mm…"
    scene s4_5d50 with dissolve
    elf "Tol. \n(Come.)"
    scene s4_5d51 with dissolve
    pause 1.1
    play sounds2 closedoor1 
    play sounds4 mmove 
    scene s4_5d43 with dissolve
    pause 2.1
    scene s4_5d44 with dissolve
    Go "We’ll continue later."
    play sounds3 closedoor1 

    scene black with dissolve 
    "Few minutes later."

    scene s4_5d52 with dissolve
    pause 3.2
    scene s4_5d53 with dissolve
    mc "How do you feel?"
    scene s4_5d54 with dissolve
    k "Well, I can joke."
    k "Brain’s a little scrambled though."
    k "If it wasn’t for the hole in my chest, I’d say I’m fantastic."
    play sounds3 mmove 
    scene s4_5d56 with dissolve
    pause 1.1
    scene s4_5d55 with dissolve
    k "On the bright side…"
    k "I’ve got one extra hole now."
    scene s4_5d56 with dissolve
    mc "You’re serious?"
    scene s4_5d57 with dissolve
    play sounds3 kalestralaugh2
    pause 2.1
    play sounds4 clothess 
    scene s4_5d58 with dissolve
    k "Knew you’d love that one."
    scene s4_5d59 with dissolve
    pause 1.2
    scene s4_5d60 with dissolve
    mc "(whispering) You never change…"
    scene s4_5d59 with dissolve
    k "Oh, look at that face."
    k "All broody and tragic."
    k "Is that supposed to be charming?"
    scene s4_5d60 with dissolve
    mc "I didn’t say that."
    play sounds3 mmove 
    scene s4_5d61 with dissolve
    k "(mocking his voice) Don’t die. I won’t let you die."
    k "God, you should’ve seen your face."
    play sounds4 mmove 
    scene s4_5d62 with dissolve
    k "What was that expression?"
    k "You looked like the world was ending."
    scene s4_5d63 with dissolve
    pause 2.2
    scene s4_5d64 with dissolve
    mc "Time was measured in seconds."
    scene s4_5d65 with dissolve
    mc "Managing my emotions on top of that…"
    mc "Wasn’t exactly feasible."
    scene s4_5d66 with dissolve
    mc "..."
    play sounds4 mmove 
    scene s4_5d67 with dissolve
    pause 0.7
    scene s4_5d68 with dissolve
    pause 0.7
    play sounds3 mmove 
    scene s4_5d67 with dissolve
    pause 0.7
    scene s4_5d69 with dissolve
    k "Hey… [mc]?"
    scene s4_5d70 with dissolve
    mc "Hm?"
    scene s4_5d71 with dissolve
    k "Thanks."
    scene s4_5d72 with dissolve
    pause 1.1
    scene s4_5d73 with dissolve
    pause 1.1
    scene s4_5d74 with dissolve
    mc "You’re welcome."
    play sounds2 mmove 
    scene s4_5d75 
    k "Congratulations."
    k "You’ve secured third place."
    k "In the ranking of the most important people in my life."
    scene s4_5d76 with dissolve
    mc "I’m honored."
    mc "What’s the prize?"
    scene s4_5d77 with dissolve
    pause 0.9
    play sounds2 clothess 
    scene s4_5d78 with dissolve
    pause 0.8
    scene s4_5d79 with dissolve
    k "Haven’t decided yet."
    scene s4_5d72 with dissolve
    pause 1.1
    scene s4_5d80 with dissolve
    mc "Sorry I…"
    mc "Disfigured you—"
    scene s4_5d81 with dissolve
    k "I like it."
    k "Makes me feel like I matter to someone."
    k "Like someone was actually afraid to lose me."
    stop music1 fadeout 3.2
    scene s4_5d82 with dissolve
    pause 2.1
    scene s4_5d83 with dissolve
    k "(whispering) Where are we?"
    scene s4_5d84 with dissolve
    mc "Still working on that."
    mc "There’s a strong chance we were thrown backward."
    mc "In time."
    scene s4_5d86 with dissolve
    k "(whispering) Wasn’t it a little early to trust them?"
    scene s4_5d85 with dissolve
    mc "I wasn’t given much of a choice."
    mc "But they haven’t shown aggression."
    scene s4_5d83 with dissolve
    k "Which somehow makes it worse."
    scene s4_5d84 with dissolve
    mc "They saved you."
    mc "That earns them… a fraction of trust."
    scene s4_5d82 with dissolve
    pause 2.1
    scene s4_5d81 with dissolve
    k "Alright. If you say so."
    k "Just… don’t lose your head over them."
    scene s4_5d86 with dissolve
    pause 0.9
    scene s4_5d87 with dissolve
    pause 0.9
    scene s4_5d85 with dissolve
    mc "Want to look around?"
    scene s4_5d88 with dissolve
    k "Sure."
    k "But first, I need new clothes."
    scene s4_5d89 with dissolve
    k "And a bath."
    pause 1.1
    k "Want to check if I smell?"
    scene s4_5d90 with dissolve
    mc "I’ll pass."
    stop sounds1 fadeout 0.5 

    scene black with dissolve 
    play sound windscene loop fadein 2.0 volume 0.2
    pause 3.2   
    play music undertow fadein 4.3
    scene s4_5d92 with dissolve
    pause 2.1
    keep3 "These lands once shone brighter than stars."
    keep3 "Now it’s rubble and ghosts."
    keep3 "Looking at it… you start wondering."
    keep3 "What exactly are we living for?"
    mc "Philosophy? I thought you preferred numbers and probability curves."
    scene s4_5d91 with dissolve
    keep3 "Science answers ‘how.’ Philosophy asks why ‘how’ is possible at all."
    mc "Mm."
    scene s4_5d94 with dissolve
    mc "And we’re still short on answers."
    scene s4_5d93 with dissolve
    keep3 "..."
    keep3 "Knowing what you know now."
    keep3 "Would you have chosen differently?"
    scene s4_5d94 with dissolve
    mc "So it didn’t just get under Gorem’s skin."
    mc "It got under yours too."
    scene s4_5d93 with dissolve
    keep3 "I require data."
    keep3 "For protocol."
    scene s4_5d94 with dissolve
    mc "Would I chase after Lora again?"
    mc "Without hesitation."
    mc "But…"
    mc "I would’ve left Olivia and Norman at home."
    mc "Dragging them into this…"
    mc "That was my mistake."
    scene s4_5d93 with dissolve
    keep3 "You would jeopardize the overall success rate."
    keep3 "For two lives."
    pause 0.6
    keep3 "You truly are irrational."
    scene s4_5d94 with dissolve
    mc "Human."
    mc "We’re built that way."
    play sounds2 closedoor1 
    scene s4_5d95 with dissolve
    k "Talking to that shady voice in your head again?"
    mc "Helps me stay sane."
    play sounds3 mmove 
    scene s4_5d96 with dissolve
    mc "Where did you get the clothes?"
    k "The pointy-eared hospitality committee left me a few options."
    k "But enough about that."
    k "Well?"
    play sounds4 mmove  
    scene s4_5d97 with dissolve
    mc "It suits you."
    play sounds2 rustling2 
    scene s4_5d98 with dissolve
    pause 1.1
    scene s4_5d99 with dissolve
    k "I’ll take that."
    k "Now."
    k "Let’s figure out how to get out of here."
    scene s4_5d100 with dissolve
    mc "Eager for another hole in your chest?"
    play sounds2 clothess 
    scene s4_5d101 with dissolve
    k "Oh, screw you."
    stop music fadeout 4.3
    play music1 s45c6mcxkascene fadein 3.2
    play sounds2 walkingwater fadein 3.3
    scene s4_5d102 with dissolve
    k "(half-singing)"
    k "You know… I was thinking."
    k "What about our little runaways?"
    mc "No idea."
    mc "But I’d like to believe they’re still breathing."
    k "That’s the spirit."
    scene s4_5d103 with dissolve
    k "But one thing’s bothering me."
    k "Why didn’t Selvaria finish you?"
    k "You’re not exactly a legendary hero."
    mc "Astoria intervened."
    scene s4_5d104 with dissolve
    k "The young Lady, I understood."
    k "We were… aligned."
    play sounds2 mmove 
    k "But the Lady?"
    k "Her motives were always a riddle to me."
    play sounds3 clothess 
    scene s4_5d105 with dissolve
    k "I still don’t get why she didn’t deal with that blonde."
    mc "Since when does a member of the Inquisition question her superiors?"
    scene s4_5d106 with dissolve
    k "Ah."
    k "I’ve been suspended from the Inquisition."
    pause 1.2
    play sounds2 mmove 
    mc "Wait. What?"
    k "Oh. I didn’t mean—"
    play sounds3 whoosh  
    scene s4_5d107 with dissolve
    k "..."
    stop music1 fadeout 4.3
    play music s45c7mirielscene fadein 4.5
    scene s4_5d108 with dissolve
    k "That was Miriel."
    k "Wasn’t it?"
    scene s4_5d109 with dissolve
    mc "No doubt."
    play sounds2 mmove 
    scene s4_5d110 with dissolve
    pause 1.1
    mc "After her."

    
    play sounds2 whoosh 
    play sounds3 heels1
    scene s4_5d181 with CropMove (time=0.1, mode='slideleft')
    pause 2.1
    play sounds4 footstep2 
    play sounds2 whoosh 
    scene s4_5d180 with CropMove (time=0.1, mode='slideleft')
    pause 1.8
    scene s4_5d178 
    pause 1.1
    scene s4_5d179 with dissolve
    mc "What did you mean… by distancing?"
    k "Hm?"
    k "Oh. You mean the Inquisition."
    play sounds2 clothess 
    scene s4_5d182 with dissolve
    k "Because of this."
    k "The moment you shoved that thing into my body…"
    k "You made me a problem."
    play sounds3 footstep1 
    scene s4_5d183 with dissolve
    mc "How?"
    k "Miasma’s outlawed."
    play sounds2 footstep1 
    scene s4_5d184 with dissolve
    k "If we go back, they’ll drag me in for purification."
    k "And if they can’t carve it out…"
    k "Execution."
    mc "..."
    play sounds2 clothess
    scene s4_5d185 with dissolve
    k "Relax. I’m not blaming you."
    k "You did save my life."
    k "(whispering) So now take responsibility for it."
    scene s4_5d186 with dissolve
    mc "I will."
    play sounds1 running 
    play sounds3 mmove 
    play sounds4 whoosh 
    scene s4_5d187 
    mc "Details later."
    play sounds2 whoosh 
    scene s4_5d188 with CropMove (time=0.1, mode='slideleft')
    pause 2.2
    play sounds3 running 
    scene s4_5d189 
    pause 1.2
    play sounds2 mcjump3
    scene s4_5d190 with vpunch 
    pause 1.2 
    play sounds3 mcjump4
    scene s4_5d191 with vpunch 
    pause 1.2
    play sounds3 heels1
    scene s4_5d118 with dissolve
    pause 1.2
    play sounds3 mmove 
    scene s4_5d119 with dissolve
    pause 1.1
    scene s4_5d120 with dissolve
    Mi "Man aníroch? \n(What do you want?)"
    play sounds3 ha
    scene s4_5d119 with dissolve
    "Analysis complete: Elvish. Simplified dialect."
    mc "(Third… can the implant translate my words?)"
    keep3 "(It’s not a magic wand. Don’t get greedy.)"
    play sounds2 mmove 
    scene s4_5d150 with dissolve
    mc "We come in peace."
    Mi "..."
    play sounds3 clothess 
    scene s4_5d151 with dissolve
    k "Ahem."
    scene s4_5d152 with dissolve
    k "Pedir ú-dagorim. \n(He says we’re not here to fight.)"
    play sounds2 mmove 
    scene s4_5d153 with dissolve
    mc "(whispering) Since when do you speak Elvish?"
    scene s4_5d154 with dissolve
    k "(whispering) Remember my sister? Half-elf. She taught me."
    scene s4_5d143 with dissolve
    Mi "Tolen o i fuin a i dúath? \n(Following footprints from the shadows?)"
    scene s4_5d144 with dissolve
    k "Ú-tholin o i fuin. \n(From the shadows? We weren’t hiding.)"
    k "Ach… no adab, penged nîn. \n(But… call it habit, pointy-ears.)"
    scene s4_5d143 with dissolve
    Mi "Penged… \n(Pointy-ears…)"
    Mi "Manen istach i lam nîn? \n(How do you know our language?)"
    scene s4_5d144 with dissolve
    k "Ú. Si i lû nín peded. Sui bain, ú? \n(No. Our turn now. Fair’s fair, right?)"
    scene s4_5d159 with dissolve 
    mc "(She looks the same.)"
    mc "(Moves the same.)"
    mc "(Still… I need to be sure.)"
    scene s4_5d162 with dissolve
    mc "Your name is Miriel. Isn’t it?"
    scene s4_5d163 with dissolve
    k "Miriel. Ce i hên hen? \n(Miriel. That you?)"
    scene s4_5d169 with dissolve 
    Mi "..."

    scene s2ff13 with dreamyzoom
    show memoryframe
    "Miriel memory"
    mc "You’re carrying too much on your shoulders, Mi…"

    scene s4_5d173 with dissolve 
    Mi "(What just happened…?)"

    scene s4_5d144 with dissolve
    pause 1.1
    scene s4_5d143 with dissolve
    Mi "Nae. \n(Yes.)"
    scene s4_5d122 with dissolve
    Mi "Pedin adlant. \n(I’ll ask again.)"
    Mi "Man aníroch o nin si? \n(What do you want?)"
    play sounds2 mmove 
    scene s4_5d123 with dissolve
    mc "(We ran into her.)"
    mc "(Now what?)"
    mc "(Ninety-seven years between us.)"
    mc "(Of course she wouldn’t know me yet.)"
    scene s4_5d155 with dissolve
    mc "We need to talk."
    k "Ped- \n(He sa-)"
    play sounds3 clothess 
    scene s4_5d156 with dissolve 
    pause 1.1
    scene s4_5d157 with dissolve 
    Mi "You."
    Mi "Speak."
    scene s4_5d158 with dissolve 
    pause 1.1
    scene s4_5d147 with dissolve
    mc "..."
    scene s4_5d146 with dissolve
    mc "We’re looking for information."
    scene s4_5d147 with dissolve
    Mi "About what?"
    scene s4_5d146 with dissolve
    mc "About this world."
    scene s4_5d124 with dissolve
    Mi "Why me?"
    scene s4_5d125 with dissolve
    mc "A man I know, Yong."
    mc "He said you’re the best."
    mc "(He says it ninety-seven years from now.)"
    mc "(Close enough.)"
    scene s4_5d126 with dissolve
    pause 1.1 
    scene s4_5d129 with dissolve
    pause 1.1 
    scene s4_5d126 with dissolve
    mc "And the only one here I can trust."
    scene s4_5d127 with dissolve
    pause 1.1
    scene s4_5d130 with dissolve
    pause 1.1
    scene s4_5d127 with dissolve
    mc "(whispering) Even if you’re not her yet."
    play sounds2 mmove 
    scene s4_5d131 with dissolve
    mc "And—"
    k "(whispering) Hey, old man."
    k "(whispering) We’re surrounded."
    scene s4_5d132 with dissolve
    mc "(whispering) I know."

    scene s2ff6 with dreamyzoom 
    show memoryframe
    "[mc] memory"
    Mi "Home..."
    scene s2ff7 with dissolve
    Mi "What makes a place… {w=0.5}a real home?"
    Mi "For me… {w=0.5}it’s the people."

    scene s4_5d133 with dissolve 
    mc "(She knew exactly where she was leading us…)"
    mc "(And still brought us here.)"
    mc "(To protect herself?)"
    mc "(Or to show us something?)"
    play sounds2 whoosh 
    play sounds3 mmove 
    scene s4_5d135 with CropMove (time=0.1, mode='slideright')
    pause 2.1
    play sounds2 whoosh 
    scene s4_5d136 with CropMove (time=0.1, mode='slideleft')
    elf " Telin o i gwaith hen \n(I’m done with this.)"
    elf "Aeg tolach, a badach. \n(Make one move and you’re dead.)"
    scene s4_5d148 with dissolve
    mc "(I see.)"
    mc "(Until we earn the others’ trust, she won’t help us.)"
    scene s4_5d149 with dissolve
    mc "(That’s what you’re meaning, isn’t it?)"
    scene s4_5d136 with dissolve
    k "(whispering) Her eyes. I’ll handle it."
    mc "(whispering) Don’t do anything stupid."
    play sounds2 walkingwater fadein 3.3
    scene s4_5d137 with dissolve
    k "(whispering) She’s scared. Her eyes keep darting."
    k "(whispering) She’s never killed before."
    k "(whispering) I’m sure she won’t sh—"
    play sounds2 scar1 
    scene s4_5d138 with vpunch
    pause 1.1
    scene s4_5d139 with dissolve
    mc "..."
    scene s4_5d140 with dissolve
    mc "(whispering) They’re serious."
    scene s4_5d141 with dissolve
    mc "(whispering) Don’t provoke them."
    mc "(whispering) We need trust. Not blood."
    pause 2.1
    play sounds2 clothess
    scene s4_5d142 
    k "(whispering) You saved my life once."
    k "(whispering) Let’s see if luck still favors us."
    scene s4_5d143 with dissolve
    Mi "You seem to know me."
    Mi "But I know nothing about you."
    play sounds2 mmove 
    scene s4_5d165 with dissolve
    pause 1.1
    scene s4_5d164 with dissolve
    Mi "And though I am curious where you came from…"
    scene s4_5d165 with dissolve
    pause 0.8
    scene s4_5d166 with dissolve
    pause 1.5
    scene s4_5d167 with dissolve
    Mi "Please… leave."
    scene s4_5d168 with dissolve
    pause 1.3
    scene s4_5d145 with dissolve
    k "So… what now?"
    k "Didn’t see that coming."
    scene s4_5d148 with dissolve
    mc "(Hidden from prying eyes.)" 
    mc "(Miriel looks like she walked out of a court… the others?)" 
    mc "(Like they were dragged in off the street.)"
    scene s4_5d149 with dissolve
    mc "(And the implants…)"
    mc "(Third?)"
    scene s4_5d130 with dissolve
    keep3 "(They’re outcasts.)"
    keep3 "(Even among their own, they find no shelter.)"
    scene s4_5d155 with dissolve
    mc "Outcasts, right?"
    pause 1.1
    mc "Give us what we need to know and I’ll make things better for you."
    scene s4_5d170 with dissolve
    Mi "You—"
    scene s4_5d169 with dissolve
    pause 1.1
    scene s4_5d171 with dissolve
    pause 0.7
    scene s4_5d172 with dissolve
    pause 0.7
    scene s4_5d173 with dissolve
    pause 1.2
    scene s4_5d175 with dissolve
    Mi "No. Please. Just leave us."
    scene s4_5d174 with dissolve
    k "(whispering) Well… that went down in flames."
    play sounds2 mmove 
    scene s4_5d176 with dissolve
    mc "(Whispering) You think so?"
    mc "(Whispering) I’d say the opposite."
    scene s4_5d177 with dissolve
    mc "(Whispering) The seed’s been planted."
    stop music fadeout 5.4
    scene black with dissolve 
    mc "(Now we wait.)"
    $ persistent.chapter_act4_5_scene += 1
    
# Сцена 5
label story05_5_5:
    stop music fadeout 0.5
    scene black with dissolve 
    pause 2.2 

    play music1 s45c8worldsceneshortversion fadein 5.4
    play sounds2 mmove 
    play sounds3 footstep2 
    scene s4_5e1 with dissolve
    pause 1.1
    scene s4_5e2 with dissolve
    mc "Kali?"
    k "Hm?"
    scene s4_5e3 with dissolve
    mc "Where does this hatred of implants come from?"
    k "Hatred? Pfft…"
    k "They don’t just dislike them."
    k "They despise them. Down to the marrow."
    mc "And yet… they still use them."
    play sounds2 clothess 
    scene s4_5e6 with dissolve
    k "Not all of them. Not even close."
    k "And the ones who do? It’s not because life’s been kind to them, old man."
    k "Speaking of which… what was that little performance with Miriel about?"
    play sounds2 mmove 
    scene s4_5e7 with dissolve
    mc "(Whispering) Because of Gorem."
    mc "(Whispering) When the head of the Federation lets you walk away without a real reason."
    mc "(Whispering) That’s never a good sign."
    play sounds2 mmove 
    scene s4_5e9 with dissolve
    mc "(Whispering) Which means we need allies. Just in case." 
    mc "(Whispering) Even if it’s a pair of elven outcasts."
    play sounds2 mmove 
    scene s4_5e10 with dissolve
    pause 1.1
    scene s4_5e11 with dissolve
    pause 1.1
    scene s4_5e10 with dissolve
    k "…Yeah. Can’t argue with that."
    play sounds3 waterfall_second fadein 2.4 loop volume 0.1
    scene s4_5e12 with dissolve
    pause 2.3
    scene s4_5e13 with dissolve
    k "Still, you know elves are officially classified as a strategic resource, right?"
    play sounds2 mmove 
    scene s4_5e14 with dissolve
    mc "Strategic?"
    play sounds1 clothess  
    scene s4_5e15 with dissolve
    k "Most Federation worlds can’t grow food."
    k "And without food… well."
    k "You can guess the rest."
    play sounds2 mmove 
    scene s4_5e19 with dissolve
    k "That’s where the elves come in. Their sensitivity."
    k "You’ve noticed all the green here, haven’t you?"
    k "Now tell me… when was the last time you saw a living tree in the Federation?"
    scene s4_5e20 with dissolve
    mc "..."
    k "Exactly."
    scene s4_5e16 with dissolve
    mc "And what does that have to do with implants?"
    k "No idea why some of them still use them."
    k "But I do know this—"
    k "Implants sever their bond with nature."
    play sounds2 footstep2 
    scene s4_5e17 with dissolve
    k "And for an elf…"
    k "That’s worse than dea—"
    stop music1 fadeout 5.4
    play music s45c4mcscene fadein 4.4
    scene s4_5e18 with dissolve
    elf "Tírad vaeth a danna am dâd adan amarth. \n(We received a report about two suspicious individuals.)"
    elf "Pedith istath lín. Si, aníron hen. \n(Identification. Now.)"
    k "A man ce i thain hen? \n(And who exactly are you supposed to be?)"
    play sounds2 ha 
    scene s4_5e22 with dissolve
    elf "Istath lín, si. \n(Identification.)"
    "Analysis complete: F.E.B. operatives."
    play sounds4 mmove 
    play sounds2 clothess 
    scene s4_5e23 
    elf "Thathar i gwaith naneth! \n(Implant signatures detected!)"
    elf "Peng aen! \n(Arm up!)"
    k "(whispering) …So. What’s the play?"
    play sounds4 clench 
    scene s4_5e28 with dissolve
    pause 1.1
    scene s4_5e29 with dissolve
    pause 0.7
    scene s4_5e27 with dissolve
    pause 0.5
    k "Hey, [mc]…"
    k "Don’t hate me for this."
    scene s4_5e30 with dissolve
    mc "Don’t you—"
    play sounds4 systemnotification
    play sounds1 voiceimplant 
    scene s4_5e31 
    pause 1.2
    play sounds whoosh 
    play sounds4 glitchfear
    scene s4_5e32 with glitch
    pause 1.1
    play sounds2 mmove 
    play sounds1 whoosh 
    scene s4_5e33
    pause 1.1
    play sounds2 punch1 
    scene s4_5e35 with vpunch 
    k "What the—"
    scene s4_5e37 
    pause 0.2
    scene s4_5e36 
    pause 0.2
    scene s4_5e37 
    pause 0.2
    scene s4_5e36 with dissolve
    mc "What exactly were you thinking?"
    k "She was half a breath away from pulling the trigger."
    scene s4_5e38 with dissolve 
    mc "They’re just doing their job."
    scene s4_5e41 with dissolve
    pause 1.1
    scene s4_5e42 with dissolve
    pause 1.1
    scene s4_5e40 with dissolve
    mc "Gather their weapons, and-"
    mc "Tell them we’ll go with them."
    mc "Peacefully."
    k "..."
    scene s4_5e39 with dissolve
    k "Tolith nin na i hîr lín. \n(Take us to your superior.)"
    k "Ú-beriam. \n(We won’t resist.)"
    scene s4_5e41 with dissolve
    pause 1.1
    scene s4_5e48 with dissolve
    mc "(This draws too much attention.)"
    scene s4_5e41 with dissolve
    pause 0.5
    scene s4_5e42 with dissolve
    pause 1.1
    scene s4_5e47 with dissolve
    mc "(A misstep. I should’ve anticipated this.)"
    elf "I peng nîn? \n(Our weapons?)"
    scene s4_5e43 with dissolve
    k "A no dan i dagor nin a chen? Ú. \n(So you can shoot us with them? Please.)"
    k "Istach gohestel? \n(Ever heard of guarantees?)"
    k "Hey, old man. What about the guns?"
    play sounds2 mmove 
    scene s4_5e44 with dissolve
    mc "Keep it. We’ll sort it out later."
    scene s4_5e45 with dissolve
    mc "(We need to leave.)"
    scene s4_5e46 with dissolve
    mc "(And fast.)"
    stop sounds2 fadeout 0.5
    stop sounds3 fadeout 0.5 
    stop sounds1 fadeout 0.5
    stop sounds fadeout 0.5
    stop sound fadeout 0.5
    stop music fadeout 1.5 
    
    scene black with dissolve 
    pause 3.1

    play sounds roomambient fadein 3.3 volume 0.4 loop
    play sound towers fadein 3.3 volume 0.7 loop 
    play sounds2 chaircrack volume 0.5
    scene s4_5e49 with dissolve 
    "A couple of minutes later. Police station."
    scene s4_5e50 with dissolve 
    pause 0.6
    scene s4_5e49 with dissolve 
    pause 0.6
    mc "(Fourteen minutes. They’re taking their time.)"
    scene s4_5e51 with dissolve 
    k "Hey, old man."
    k "Something’s been bugging me."
    k "Why do you avoid killing?"
    play music s45c9mcmemoryscene fadein 25.4
    scene s4_5e52 with dissolve 
    pause 1.1
    scene s4_5e53 with dissolve 
    pause 2.1
    k "What?"
    k "Why are you looking at me like that?"
    play sounds2 mmove 
    play sounds2 bodytap 
    scene s4_5e55 with dissolve 
    pause 0.7
    scene s4_5e54 with dissolve 
    pause 0.7
    scene s4_5e55 with dissolve 
    mc "(Avoid?)"
    mc "Tell me something…"
    play sounds2 mmove 
    scene s4_5e54 with dissolve 
    pause 0.7
    play sounds4 rustling2 
    scene s4_5e55 with dissolve 
    pause 0.7
    scene s4_5e54 with dissolve 
    pause 0.7
    scene s4_5e56 with dissolve 
    mc "Have you ever heard a man scream…"
    mc "with his lungs torn open?"
    play sounds2 mmove 
    scene s4_5e59 with dissolve 
    pause 0.1
    scene s4_5e60 with dissolve 
    pause 0.1
    play sounds4 rustling2  
    scene s4_5e59 with dissolve 
    pause 0.1
    scene s4_5e60 with dissolve 
    pause 0.1
    scene s4_5e61 with dissolve 
    mc "Beg you to shoot him…"
    mc "with half his tongue hanging loose—"
    scene s4_5ff1 with dreamyzoom  
    c "Commander, plea—"
    scene s4_5e59 with dissolve 
    pause 0.1
    scene s4_5e60 with dissolve 
    pause 0.1
    play sounds2 mmove 
    scene s4_5e59 with dissolve 
    pause 0.1
    scene s4_5e60 with dissolve 
    pause 0.1
    scene s4_5e59 with dissolve 
    pause 0.1
    play sounds4 clench 
    scene s4_5e62 with dissolve 
    mc "(whispering) …and in return—"
    play sounds2 punch1
    scene s4_5e63 with vpunch  
    pause 1.1
    mc "..."
    scene s4_5e64 with dissolve 
    mc "(whispering) …a medal for bravery."
    mc "Posthumous."
    scene s4_5e66 with dissolve 
    pause 1.1
    scene s4_5e65 with dissolve 
    mc "One day you’re a hero."
    mc "A savior."
    mc "And the next moment?"
    mc "You’re a penniless headcase with a shattered future."
    play sounds2 mmove 
    play sounds3 tablesq
    scene s4_5e67 with dissolve 
    k "..."
    scene s4_5e68 with dissolve 
    k "If you’re fishing for sympathy, you picked the wrong girl."
    play sounds2 mmove 
    scene s4_5e69 with dissolve 
    k "But yeah."
    k "I get it."
    scene s4_5e73 with dissolve 
    pause 1.1
    scene s4_5e74 with dissolve 
    pause 1.1 
    scene s4_5e75 with dissolve 
    mc "Why the sudden interest?"
    scene s4_5e70 with dissolve 
    mc "Last I checked, you cared more about moral compasses than old ghosts."
    scene s4_5e71 with dissolve 
    k "No comment."
    scene s4_5e72 with dissolve 
    pause 2.1
    scene s4_5e71 with dissolve 
    k "But you didn’t hesitate with the mutants."
    scene s4_5e73 with dissolve 
    pause 2.1
    play sounds2 mmove 
    play sounds3 clothess  
    scene s4_5e77 with dissolve  
    mc "When it’s a monster in front of you…"
    mc "it’s easier to pull the trigger."
    scene s4_5e76 with dissolve 
    k "Even knowing they used to be human?"
    pause 1.1
    scene s4_5ff33 with dreamyzoom
    c "...Th—" 
    "He tries to speak, but only a wet rasp escapes."
    c "...mmndr..."
    scene s4_5ff34 with dissolve 
    mc "..."
    play sounds1 scar1 
    scene s4_5ff35 with vpunch 
    mc "..."
    scene s4_5ff36 with dissolve 
    cj "Why did you kill my dad?!"
    cj "You`re monster!"
    scene s4_5e76 with dreamyzoom 
    pause 1.1
    play sounds2 mmove 
    play sounds3 bodytap  
    scene s4_5e78 with dissolve  
    mc "Yes."
    play sounds3 dooropen1
    scene s4_5e79 with dissolve  
    y "Drego si. Nín beria i gwaith hen o si. \n(You’re dismissed. I’ll take it from here.)"
    mc "(That voice… No. It can’t be. Yong?)"
    play sounds2 mmove 
    scene s4_5e82 with dissolve  
    k "(whispering) I don’t believe it. The Chaplain? What the hell is he doing—"
    mc "(whispering) Remember. We’re in the past."
    mc "(whispering) That’s not the man we knew."
    play sounds3 doorclose
    scene s4_5e80 with dissolve  
    pause 1.1
    scene s4_5e81 with dissolve  
    y "Well."
    y "This is unexpected."
    y "What happened to the Gate?"
    stop music fadeout 5.5
    play music1 season4act21 fadein 5.5 
    scene s4_5e86 with dissolve  
    mc "(He knows?)"
    k "Wait- you know about it?"    
    k "How?"
    scene s4_5e85 with dissolve  
    mc "Kali. Not another word."
    scene s4_5e84 with dissolve  
    mc "(Straight to the Gate.)"
    mc "(Testing us? Showing his hand? Or baiting?)"
    mc "If you know who we are…"
    mc "then you already know about the Gate."
    scene s4_5e83 with dissolve  
    y "Clever."
    scene s4_5e87 with dissolve  
    y "A young woman mentioned you spoke my name."
    y "Why?"
    scene s4_5e88 with dissolve   
    mc "(So Miriel’s in contact with him. Even now.)"
    scene s4_5e86 with dissolve
    pause 1.1 
    scene s4_5e85 with dissolve    
    mc "When are you letting us go?"
    scene s4_5e87 with dissolve  
    y "When I have answers."
    scene s4_5e88 with dissolve  
    mc "Then you should speak to Gorem."
    mc "We’re his guests."
    mc "And he’s… something of an emperor around here."
    scene s4_5e89 with dissolve   
    mc "(Will you correct me… or let that slide?)"
    scene s4_5e87 with dissolve  
    y "He… doesn’t hold authority here."
    y "Especially when it comes to those who aren’t from this time."
    scene s4_5e85 with dissolve  
    mc "I see."
    mc "About the girl."
    mc "I wanted her support."
    mc "I used your name to get it."
    scene s4_5e86 with dissolve  
    y "You didn’t hesitate."
    mc "(His tone shifted.)"
    play sounds2 glitchfear
    scene s4_5e90 with glitch  
    keep3 "He carries something from outside the cycle."
    keep3 "The same marks we do."
    keep3 "He knows."
    scene s4_5e91 with dissolve  
    mc "(Yet he acts as if he doesn’t.)"
    mc "(What are you hiding?)"

    scene s2f111 with dreamyzoom 
    show memoryframe
    y "The enemy is already among us."
    y "One wrong step… "
    mc "(whispering) …and you’ll find a knife in your back."
    scene s4_5e88 with dissolve   
    pause 1.6
    mc "(whispering) Will you help us?"
    scene s4_5e83 with dissolve  
    y "Come."
    
    play sounds2 closedoor1
    scene s4_5e92 with dissolve
    pause 1.7
    play sounds2 mmove 
    scene s4_5e93 with dissolve  
    k "Hey, old man… what was that conversation?"
    scene s4_5e94 with dissolve
    mc "(whispering) We’re being watched."
    play sounds3 mmove 
    scene s4_5e95 with dissolve 
    k "(whispering) Since when?"
    scene s4_5e97 with dissolve
    mc "(whispering) Don’t know."
    mc "(whispering) But if I had to guess? Since the very beginning."
    play sounds3 clothess  
    scene s4_5e101 with dissolve
    k "(whispering) And him?"
    scene s4_5e100 with dissolve
    mc "(whispering) He’s under the same pressure."
    mc "(whispering) Careful with every word."
    scene s4_5e102 with dissolve
    k "(whispering) I hate this political chess nonsense."
    k "(whispering) Everyone smiling. No one saying what they mean."
    stop music1 fadeout 5.5 
    scene s4_5e99 with dissolve
    y "Inside."
    play sounds2 dooropen1
    stop sound fadeout 0.5
    stop sounds fadeout 0.5
    scene black with dissolve 
    pause 1.1
    play sounds3 closedoor1
    pause 2.1 
    play sound roomemptyambience1 fadein 0.6 loop 
    play sounds2 mmove 
    scene s4_5e103 with dissolve
    y "Make yourselves at home."
    y "No one should be listening here."
    scene s4_5e104 with dissolve
    k "(whispering) Gods… smells like a rat bloated and burst in here."
    play sounds3 mmove 
    play sounds2 slurping
    scene s4_5e106 with dissolve
    pause 1.1
    scene s4_5e107 with dissolve
    pause 1.1
    scene s4_5e105 with dissolve
    y "And?"
    y "What happened?"
    play sounds2 mmove 
    scene s4_5e108 with dissolve
    mc "So you don’t know?"
    y "Only fragments."
    y "Echoes from past lives."
    mc "Then…"
    scene black with dissolve 
    pause 2.2
    play sounds nightc fadein 5.5 loop volume 0.5
    play sounds1 female_snore volume 0.1
    scene s4_5e109 with dissolve
    mc "And that’s how we ended up here."
    scene s4_5e110 with dissolve
    pause 2.1
    play sounds2 slurping 
    scene s4_5e111 with dissolve
    y "(whispering) Why didn’t it work…"
    play sounds2 mmove 
    scene s4_5e112 with dissolve
    pause 1.3
    mc "Can I ask you something?"
    scene s4_5e125 with dissolve
    y "Go on."
    scene s4_5e126 with dissolve
    mc "What’s the point?"
    scene s4_5e112 with dissolve
    pause 1.3
    scene s4_5e113 with dissolve
    y "Look to your left."
    y "What do you see?"
    scene s4_5e110 with dissolve
    pause 1.3
    scene s4_5e109 with dissolve
    mc "What’s the trick?"
    scene s4_5e112 with dissolve
    pause 1.3
    play sounds2 mmove 
    play sounds3 slurping 
    scene s4_5e111 with dissolve
    pause 1.3
    play sounds3 putcup
    scene s4_5e114 with dissolve
    y "How is she different from us?"
    pause 1.1
    y "She, and so many others, never had the chance to change their future."
    play sounds2 mmove 
    play music s45c10yongscene fadein 5.5
    scene s4_5e115 with dissolve
    y "It all began the moment Eldrindor activated the Gate."
    scene s4_5e127 with dissolve
    mc "Eldrindor?"
    scene s4_5e126 with dissolve
    y "The scientist every elf curses."
    scene s4_5e127 with dissolve
    mc "Gorem’s grandfather."
    scene s4_5e125 with dissolve
    y "Yes."
    y "He was the one who launched the Gate System."
    scene s4_5e109 with dissolve
    mc "And half the galaxy vanished."
    mc "Gorem mentioned that."
    play sounds2 clench 
    scene s4_5e114 with dissolve
    pause 1.1
    play sounds3 slurping 
    play sounds4 mmove volume 0.4 
    scene s4_5e111 with dissolve
    pause 1.1
    scene s4_5e112 with dissolve
    pause 1.1
    scene s4_5e113 with dissolve
    y "Good."
    y "Then answer me this."
    y "What did the System actually do?"
    scene s4_5e112 with dissolve
    mc "They teleport."
    scene s4_5e113 with dissolve
    y "Those are the Gates. I’m asking about the system that links them."
    scene s4_5e112 with dissolve
    mc "It stopped time."
    mc "For a few seconds."
    scene s4_5e113 with dissolve
    y "Half a second."
    y "At the cost of half a galaxy?"
    scene s4_5e131 with dissolve
    y "An absurd price…"
    y "for half a second."
    scene s4_5e129 with dissolve
    mc "Paying in lives is absurd to begin with."
    scene s4_5e128 with dissolve
    pause 1.1
    play sounds3 putcup
    scene s4_5e114 with dissolve
    y "Perhaps."
    y "But the time freeze was only the visible consequence."
    y "The real function was something else."

    y "It created a cycle."
    y "The Gate established a fixed point in the universe, a boundary we cannot cross."
    scene s4_5e125 with dissolve
    y "It stripped everyone of choice."
    y "Future. Past. Doesn’t matter."
    y "Everything begins at one point…"
    y "and ends the same way."
    scene s4_5e129 with dissolve
    mc "Wait."
    mc "You’re saying us being here… was planned?"
    scene s4_5e128 with dissolve
    y "That’s the difference."
    y "We can’t break the principle."
    y "But you can."
    scene s4_5e129 with dissolve
    mc "Can I?"
    mc "And what makes you so certain?"
    scene s4_5e132 with dissolve
    y "Because you’re here."
    scene s4_5e133 with dissolve
    mc "What are you—"
    scene s4_5e125 with dissolve
    y "Astoria relives the loss of her sister."
    y "Evreliya walks into the same tomb again and again."
    y "Selvaria keeps killing her father."
    y "And Lora…"
    y "She keeps trying to keep you alive."
    scene s4_5e139 with dissolve
    mc "(So all my wife’s suffering was… for nothing?)"
    scene s4_5e140 with dissolve
    mc "How?"
    scene s4_5e139 with dissolve
    y "Motives change."
    y "The outcome doesn’t."
    y "What’s needed is power from outside the cycle."
    scene s4_5e138 with dissolve
    mc "So that’s why I matter."
    mc "I can break the cycle."
    scene s4_5e137 with dissolve
    y "There were 378 attempts before you."
    y "But somehow you’ve made it further than any of them."
    scene s4_5e139 with dissolve
    mc "Three hundred seventy-eight…"
    scene s4_5e140 with dissolve
    "A strained, humorless laugh."
    mc "That’s cruel."
    mc "And how many of those were mine?"
    y "..."
    y "All of them."
    scene s4_5e128 with dissolve
    pause 2.1
    scene s4_5e129 with dissolve
    mc "…again?"
    scene s4_5e125 with dissolve
    y "They were all you."
    y "Every single one."
    scene s4_5e131 with dissolve
    mc "Cruel."
    y "You think so?"
    y "Many of us would give anything for a fate like yours."
    y "To forget what we were."
    scene s4_5e136 with dissolve
    mc "And Lora?"
    mc "She’s like me."
    mc "So why didn’t she—"
    scene s4_5e125 with dissolve
    y "Because of Evrelia."
    y "And her power."
    mc "(whispering) I don’t understand…"
    scene s4_5e131 with dissolve
    y "The Abyss is a consequence of the Gate."
    y "Gain immortality there…"
    y "and you lose the ability to leave the cycle."
    y "She’s no different from the rest of us."
    scene s4_5e109 with dissolve
    mc "Then I’ll ask two questions."
    mc "First, what do you want from me?"
    y "Break the cycle."
    mc "Second, what guarantees do I have?"
    play sounds2 clench 
    scene s4_5e114 with dissolve
    pause 1.1
    play sounds3 slurping 
    play sounds4 mmove volume 0.4 
    scene s4_5e111 with dissolve
    pause 1.1
    scene s4_5e112 with dissolve    
    pause 1.2
    scene s4_5e113 with dissolve
    y "None."
    play sounds2 mmove 
    scene s4_5e139 with dissolve
    mc "(So all her suffering…)"
    mc "(Every attempt to save me. To save Norman.)"
    mc "(Pointless?)"
    mc "(And Astoria’s attempts…)"
    scene s4_5e140 with dissolve
    mc "(whispering) Immortality?"
    mc "(whispering) Sounds more like eternal imprisonment."
    scene s4_5e109 with dissolve
    mc "How long has this been going on?"
    scene s4_5e112 with dissolve    
    pause 1.2
    play sounds3 slurping 
    play sounds4 mmove volume 0.4 
    scene s4_5e111 with dissolve
    pause 1.2
    scene s4_5e112 with dissolve    
    y "..."
    scene s4_5e129 with dissolve    
    mc "I see."
    mc "Then I refuse."
    scene s4_5e112 with dissolve    
    pause 1.2
    play sounds3 slurping 
    play sounds4 mmove volume 0.4 
    scene s4_5e111 with dissolve
    pause 1.2
    scene s4_5e113 with dissolve    
    y "Are you certain?"
    y "You don’t have a choice."
    scene s4_5e112 with dissolve    
    mc "If I’m destined to die either way, what’s the point?"
    mc "You made me a hero."
    play sounds3 slurping 
    play sounds4 mmove volume 0.4 
    scene s4_5e111 with dissolve
    mc "Put a banner in my hands and told me to save the world."
    play sounds2 mmove 
    scene s4_5e112 with dissolve  
    mc "Never once asking if I wanted the role."
    mc "That’s before we even talk about how you treated me."
    play sounds3 putcup
    scene s4_5e114 with dissolve
    y "..."
    scene s4_5e115 with dissolve
    y "You’re a man of principles."
    y "Am I right?"
    scene s4_5e129 with dissolve
    mc "I like to think so."
    scene s4_5e128 with dissolve
    y "I saved your life."
    y "Now it’s your turn to save mine."
    scene s4_5e130 with dissolve
    mc "..."
    scene s4_5e139 with dissolve
    mc "(I don’t like this idea, but refusing won’t change anything.)"
    mc "(And he’s right… I’m alive because of him.)"
    scene s4_5e140 with dissolve
    mc "Then I want your full support."
    scene s4_5e109 with dissolve
    mc "No games."
    mc "No schemes."
    mc "A clear plan."
    mc "Everything on the table."
    pause 1.1
    y "Agreed."
    stop music fadeout 3.2
    scene s4_5e116 with dissolve
    mc "Kali."
    mc "Your thoughts?"
    mc "I know you’re not asleep. Stop pretending."
    play sounds2 mmove 
    scene s4_5e117 with dissolve
    pause 1.1
    scene s4_5e118 with dissolve
    pause 1.1
    scene s4_5e119 with dissolve
    k "..."
    play sounds2 clothess 
    scene s4_5e120 with dissolve
    pause 2.1
    scene s4_5e122 with dissolve
    k "How long have you known?"
    scene s4_5e121 with dissolve
    mc "You snore."
    mc "Did you know?"
    scene s4_5e122 with dissolve
    k "I’ll keep that in mind."
    scene s4_5e123 with dissolve
    k "You’re starting to freak me out."
    k "First Federation leaders call you friend."
    k "Now a Chaplain."
    k "You’ve got a real talent for getting powerful people on your side."
    scene s4_5e124 with dissolve
    y "There’s a celebration in the camp tonight."
    y "Care to join us?"
    stop music fadeout 0.5 
    stop sounds fadeout 1.1
    stop sound fadeout 1.1
    scene black with dissolve 
    mc "We’ll be there."
    mc "But first..."
    mc "We make sure we’re not followed."
    pause 4.1
    $ persistent.chapter_act4_5_scene += 1
    

# Сцена 6. 
label story05_5_6:
    stop music fadeout 0.5
    play music1 s45c3mcscene fadein 15.1
    play sound windscene loop fadein 2.0 volume 0.5
    scene black with dissolve 
    pause 0.8
    "The road to the camp was quiet."
    play sounds walkingwater loop fadein 1.2 volume 0.2
    scene s4_5ff62 with dissolve
    "For a while they walked in silence."
    pause 1.1
    mc "Kali? About those other worlds… do you know anything?"
    scene s4_5ff64 with dissolve
    k "Knowledge?"
    play sounds2 whoosh 
    scene s4_5ff65 with CropMove(time=0.1, mode='slideleft')
    k "I prefer meat and spectacle to libraries."
    play sounds3 whoosh 
    scene s4_5ff67 with CropMove(time=0.1, mode='slideleft')
    pause 1.1
    scene s4_5ff68 
    k "But even I have heard the stories."
    play sounds2 whoosh
    play sounds3 mmove  
    scene s4_5ff69 with CropMove(time=0.1, mode='slideright')
    mc "I'd appreciate it."
    scene s4_5ff70 with dissolve
    k "Ew… don't do that, old man."
    k "Politeness looks strange on you."
    scene s4_5ff72 with dissolve
    k "But fine."
    k "People say reality doesn't move in one straight line."
    play sounds3 mmove 
    scene s4_5ff74 with dissolve
    k "Every major choice leaves another world behind."
    scene s4_5ff73 with dissolve
    mc "Parallel worlds."
    play sounds3 mmove 
    scene s4_5ff75 with dissolve
    k "If you like big words."
    k "Different choices."
    k "Different wars."
    k "Different endings."
    play sounds2 mmove 
    scene s4_5ff76 with dissolve
    k "That’s everything I know."
    mc "Not much to go on."
    scene s4_5ff77 with dissolve
    k "It’s what there is."
    scene s4_5ff78 with dissolve
    pause 1.1
    play sounds3 glitchfear
    scene s4_5ff79 with glitch
    keep3 "Most beings live their entire lives without ever realizing the truth."
    keep3 "To them, their world is the only one that exists."
    play sounds3 mmove 
    scene s4_5ff80 with dissolve
    mc "(No chance to change it…)"
    keep3 "They don’t need one."
    scene s4_5ff81 with dissolve
    mc "(Why—)"
    pause 1.1 

    scene s4_5e131 with dreamyzoom
    show memoryframe with dissolve
    y "Many of us would give anything for a fate like yours."
    y "To forget what we were."
    hide memoryframe

    scene s4_5ff83 with dissolve
    mc "(…Because of the memories.)"
    scene s4_5ff82 with dissolve
    keep3 "Correct."
    keep3 "When you live the same life over and over without knowing it’s repeating…"
    keep3 "you’re perfectly satisfied."
    scene s4_5ff84 with dissolve
    mc "(That’s… disturbing.)"
    keep3 "Only if you know about it."
    keep3 "Otherwise it’s just… life."
    play sounds3 mmove 
    scene s4_5ff85 with dissolve
    mc "(But how did they even appear? Where did they—)"
    keep3 "From the moment time itself began."
    keep3 "Time is a fabric. Threads are the fibers it’s woven from."
    scene s4_5ff86 with dissolve
    mc "(Haven’t felt this stupid trying to understand something in a long time…)"
    play sounds3 mmove 
    scene s4_5ff90 with dissolve
    keep3 "..."
    keep3 "Do you?"
    play sounds2 clothess  
    scene s4_5ff91 with dissolve
    keep3 "Think back on your life."
    
    scene s0k83 with dreamyzoom
    show memoryframe with dissolve
    keep3 "The first major break in the cycle happened when you decided to go after Lora."
    hide memoryframe
    scene s0p12 with dreamyzoom
    show memoryframe with dissolve
    keep3 "The second came when you ended up on the Ark."
    keep3 "Together, they forced the cycle to branch."
    keep3 "A branch changes the road. The fixed point still decides where the cycle closes."
    hide memoryframe

    scene s4_5ff82 with dissolve
    mc "(Different roads. Same wall.)"
    mc "(Major shifts… So the small ones don’t matter?)"
    scene s4_5ff84 with dissolve
    keep3 "Every change affects the outcome."
    keep3 "Some simply carry more weight."
    play sounds3 mmove 
    scene s4_5ff85 with dissolve
    keep3 "But every shift has consequences."
    keep3 "Every outcome leads to a different moment."
    scene s4_5ff86 with dissolve
    mc "(So these are… literally all possible versions of my life?)"
    keep3 "Yes."
    play sounds3 mmove 
    scene s4_5ff87 with dissolve
    k "You good?"
    scene s4_5ff88 with dissolve
    pause 1.1
    scene s4_5ff89 with dissolve
    mc "Yeah. I’m fine. Don’t worry."
    scene s4_5ff87 with dissolve
    k "Talking to that keeper again, huh…"
    k "Well. Whatever."
    k "Not my place to tell you what to do."
    k "Anyway, how much farther?"
    scene s4_5ff87 with dissolve
    mc "No idea."
    mc "Yong’s supposed to meet us somewhere up ahead."
    mc "After that, he’ll take us to the camp."
    stop music1 fadeout 5.5
    scene s4_5ff88 with dissolve
    pause 1.1
    scene s4_5ff87 with dissolve
    k "Got it."
    scene black with dissolve 
    pause 2.1

    play music s45c11elfscene fadein 5.4 volume 0.5
    play sound windscene loop fadein 2.0 volume 0.5
    scene s4_5f1 with dissolve
    "The Outcasts’ Camp."
    scene s4_5f2 with dissolve
    y "Here we are."
    scene s4_5f3 with dissolve
    y "Two rules."
    y "No mention of slavery."
    y "And nothing about implants."
    play sounds2 clothess 
    scene s4_5f4 with dissolve
    mc "What about Gorem?"
    play sounds3 mmove 
    scene s4_5f5 with dissolve
    y "Make that three."
    y "Don’t mention His Highness."
    scene s4_5f6 with dissolve
    pause 1.1
    scene s4_5f7 with dissolve
    pause 1.1
    scene s4_5f8 with dissolve
    pause 1.1
    play sounds3 mmove 
    scene s4_5f9 with dissolve
    y "And… a word."
    scene s4_5f10 with dissolve
    k "(whispering) Something’s off about him."
    scene s4_5f11 with dissolve
    mc "You think?"
    mc "To me, he feels more open now."
    mc "In his own way, sure… but still."
    scene s4_5f10 with dissolve
    k "It’s all crap, old man. My gut says something’s wrong here."
    scene s4_5f11 with dissolve
    mc "Wait here."
    mc "I’ll see what he wants."
    scene s4_5f12 with dissolve
    k "Yeah."
    scene s4_5f13 with dissolve
    pause 1.1
    play sounds3 mmove 
    scene s4_5f18 with dissolve
    y "(whispering) I know you’re desperate to go back."
    y "(whispering) To make sure they’re alright."
    y "(whispering) I have a way… but—"
    scene s4_5f17 with dissolve
    pause 1.1
    scene s4_5f18 with dissolve
    y "It’ll take time."
    y "And permission."
    scene s4_5f19 with dissolve
    mc "Is this about the anomaly rifts?"
    scene s4_5f17 with dissolve
    pause 1.1
    scene s4_5f18 with dissolve
    y "Yes."
    y "Miriel will explain how they work."
    scene s4_5f17 with dissolve
    pause 2.1
    scene s4_5f19 with dissolve
    mc "So… you’re in charge here?"
    play sounds3 mmove 
    scene s4_5f20 with dissolve
    pause 2.1
    scene s4_5f21 with dissolve
    y "More like I watch over them."
    y "Make sure they don’t hurt themselves… or anyone else."
    mc "Then how did you convince them to let us in?"
    play sounds3 mmove 
    scene s4_5f22 with dissolve
    y "It wasn’t my doing."
    y "Miriel made the first move."
    y "Smoke?"
    scene s4_5f23 with dissolve
    mc "I’ll pass."
    mc "Not the right place."
    scene s4_5f24 with dissolve
    pause 2.1
    play sounds3 mmove 
    scene s4_5f25 with dissolve
    mc "So… Miriel."
    mc "Why?"
    scene s4_5f18 with dissolve
    y "Somehow…"
    y "she remembered another life."
    y "Not all of it."
    y "Just the one where you existed."
    play sounds3 mmove 
    scene s4_5f26 with dissolve
    mc "How?"
    play sounds2 footstep2  
    scene s4_5f27 with dissolve
    pause 1.1
    scene s4_5f28 with dissolve
    y "[mc]?"
    scene s4_5f29 with dissolve
    mc "..."
    scene s4_5f30 with dissolve
    y "No. It’s nothing."
    y "Get some rest."
    scene s4_5f32 with dissolve
    mc "Wait."
    mc "Say what you were going to say."
    play sounds3 mmove 
    scene s4_5f34 with dissolve
    pause 1.1
    scene s4_5f33 with dissolve
    y "One question."
    y "What is hope?"
    scene s4_5f34 with dissolve
    mc "Why the sudden philosophy?"
    pause 1.1
    scene s4_5f33 with dissolve
    y "Why do you keep moving forward?"
    y "What… drives you?"
    scene s4_5f37 with dissolve
    pause 1.1
    scene s4_5f36 with dissolve
    mc "Protect what’s mine."
    mc "And to survive."
    scene s4_5f37 with dissolve
    pause 1.1
    scene s4_5f35 with dissolve
    pause 2.1 
    scene s4_5f36 with dissolve
    mc "What?"
    mc "You expecting something profound?"
    scene s4_5f37 with dissolve
    y "That’s your entire motivation?"
    scene s4_5f36 with dissolve
    mc "Isn’t that enough?"
    scene s4_5f34 with dissolve
    mc "When a lion grows weak, the pride casts him out."
    mc "He’s left alone."
    mc "No allies. No shelter."
    mc "And still…"
    mc "They don’t die of old age."
    mc "They die fighting."
    scene s4_5f36 with dissolve
    mc "Struggle is life."
    mc "Stop fighting and you’re already dead."
    mc "That’s all there is to it."
    scene s4_5f34 with dissolve
    pause 1.1
    scene s4_5f33 with dissolve
    y "What’s a lion?"
    play sounds3 mmove 
    scene s4_5f38 with dissolve
    mc "What—"
    scene s4_5f39 with dissolve
    mc "You know what? Forget it."
    scene s4_5f34 with dissolve
    pause 1.2
    scene s4_5f33 with dissolve
    y "Get some rest."
    play sounds3 mmove 
    scene s4_5f40 with dissolve
    pause 1.1
    scene s4_5f41 with dissolve
    mc "(Rest…)"
    mc "(Like that’s something I can afford.)"
    scene s4_5f42 with dissolve
    pause 1.2
    
    play sounds3 footstep2  
    scene s4_5f43 with dissolve
    mc "You okay?"
    scene s4_5f44 with dissolve
    k "Hm? Oh, it’s you, old man."
    k "Yeah, I’m fine."
    scene s4_5f45 with dissolve
    mc "Enjoying it?"
    scene s4_5f46 with dissolve
    k "Nah. I’m more interested in watching him."
    scene s4_5f47 with dissolve
    pause 1.1
    scene s4_5f46 with dissolve
    k "So… what were you whispering about?"
    scene s4_5f47 with dissolve
    mc "That obvious?"
    play sounds2 whoosh 
    scene s4_5f48 with dissolve
    k "Two old men whispering behind everyone’s backs?"
    k "The whole camp noticed."
    scene s4_5f49 with dissolve
    pause 1.6
    scene s4_5f50 with dissolve
    mc "How’s your wound?"
    play sounds2 mmove  
    scene s4_5f51 with dissolve
    k "Honestly?"
    k "Like shit. I’ll live, but it hurts like hell."
    pause 1.1
    play sounds2 whoosh  
    scene s4_5f52
    mc "Take it off. I need to check how it—"
    play sounds3 mmove  
    scene s4_5f53 with dissolve
    k "No."
    scene s4_5f54 with dissolve
    mc "I’ve already seen it, so—"
    scene s4_5f55 with dissolve
    mc "(She’s red. Is she… embarrassed? No, wait, what am I doing?)"
    scene s4_5f56 with dissolve
    k "Others are watching."
    scene s4_5f58 with dissolve
    pause 1.1
    scene s4_5f57 with dissolve
    mc "(Not even trying to hide it.)"
    pause 1.1
    scene s4_5f55 with dissolve
    mc "But… that never bothered you before. What changed?"
    scene s4_5f56 with dissolve
    k "No means no."
    play sounds2 glitchfear
    scene s4_5f59 with glitch 
    keep3 "It’s the miasma."
    scene s4_5f60 with dissolve
    mc "(Care to elaborate?)"
    keep3 "The implants used to dull emotions completely."
    scene s4_5f62 with dissolve
    keep3 "But once you damaged them, that effect stopped working."
    keep3 "What you see now is the result."
    mc "(Maybe. Or maybe there’s more to it.)"
    play sounds3 mmove  
    scene s4_5f61 with dissolve
    mc "Listen. I’m responsible for you."
    mc "And I need to know if you’re alright."
    pause 1.1
    scene s4_5f62 with dissolve
    mc "Alright." 
    mc "We’ll find somewhere more private."
    k "..."
    play sounds3 mmove  
    scene s4_5f63 with dissolve
    k "Thanks, old man."
    play sounds2 footstep2   
    scene s4_5f64 with dissolve
    Mi "I… overheard that you were having some trouble."
    scene s4_5f65 with dissolve
    Mi "And… I could show you a place."
    scene s4_5f66 with dissolve
    pause 0.6
    scene s4_5f67 with dissolve
    pause 0.6
    scene s4_5f65 with dissolve
    Mi "(whispering) If you’d like."
    scene s4_5f68 with dissolve
    mc "…Alright."
    scene s4_5f69 with dissolve
    Mi "Then… follow me."
    play sounds3 mmove 
    scene s4_5f71 with dissolve
    pause 1.1
    mc "So… what’s the occasion?"
    scene s4_5f70 with dissolve
    Mi "It is… our annual day of remembrance. We honor those who perished in the tragedy."
    mc "You mean El— …your Highness’s grandfather?"
    scene s4_5f72 with dissolve
    Mi "Yes."
    Mi "The deeds of our progenitor, Eldrindor."
    scene s4_5f73 with dissolve
    k "Funny. I don’t see much mourning."
    k "More like celebration."
    k "Looks strange."
    scene s4_5f74 with dissolve
    Mi "Tears won’t bring the dead back."
    Mi "And I don’t think they’d want to see their loved ones weep."
    Mi "So we celebrate."
    Mi "We remember with life, not sorrow."
    scene s4_5f73 with dissolve
    k "I’ve heard of that. Still feels odd."
    scene s4_5f76 with dissolve
    Mi "If you prefer tears, that’s your choice."
    Mi "We chose a different path."
    play sounds3 clench 
    scene s4_5f78 with dissolve
    elf "YEE-HEE-HEY!"
    play sounds2 punch1 
    scene s4_5f79 with vpunch 
    pause 1.1
    play sounds2 mmove 
    scene s4_5f80 with dissolve
    Mi "Reyka, Leila, you alright?"
    play sounds2 whoosh   
    scene s4_5f81 
    elf "All good!"
    pause 1.1
    play sounds2 mmove 
    scene s4_5f87 with dissolve
    mc "Sorry… if her words hit a nerve."
    scene s4_5f88 with dissolve
    Mi "N-no, it’s alright. For us… it’s an old wound."
    Mi "But… about that promise—"
    scene s4_5f84 with dissolve
    mc "That was just an off—"
    mc "(Wait… she refused back then… and now…?)"
    pause 1.1
    mc "So… you agreed?"
    play sounds3 clothess 
    scene s4_5f85 with dissolve
    Mi "After what you said about your bond with my teacher…"
    Mi "I went to see him."
    Mi "He… explained the bigger picture."
    Mi "I agreed."
    mc "I see."
    Mi "But how exactly do you plan to improve our situation?"
    play sounds2 mmove 
    scene s4_5f86 with dissolve
    mc "(…And what am I supposed to say to that?)"
    mc "I’ll be honest with you. I was acting on the fly."
    scene s4_5f87 with dissolve
    mc "I didn’t really have a plan, but before facing Gorem, I wanted allies."
    mc "Then… together, we could figure something out."
    scene s4_5f89 with dissolve
    mc "That was the idea."
    scene s4_5f88 with dissolve
    Mi "Just as I thought…"
    play sounds3 laughmir
    scene s4_5f90 with dissolve
    pause 1.1
    scene s4_5f91 with dissolve
    Mi "You really aren’t that different from how my teacher described you."
    play sounds2 whoosh 
    scene s4_5f104 with CropMove(time=0.1, mode='slideleft')
    mc "(She’s… laughing?)"
    k "(whispering) You seeing this too?"
    scene s4_5f103 with dissolve
    mc "(whispering) Yeah… like spotting a unicorn."
    k "(whispering) A what?"
    play sounds2 clothess
    scene s4_5f105 with dissolve
    mc "(whispering) Horse with a horn."
    scene s4_5f106 with dissolve
    k "(whispering) A hors—"
    play sounds2 mmove 
    scene s4_5f107 with dissolve
    mc "(whispering) Forget it."
    scene s4_5f91 with dissolve
    Mi "Why are you both staring?"
    scene s4_5f92 with dissolve
    mc "You have a beautiful smile."
    scene s4_5f93 with dissolve
    Mi "..."
    play sounds2 whoosh 
    scene s4_5f94 with CropMove(time=0.1, mode='slideup')
    Mi "Wha— I— No! That’s… embarrassing."
    scene s4_5f95 with dissolve
    pause 1.2
    play sounds2 mmove 
    scene s4_5f96 with dissolve
    mc "Can I ask you something?"
    scene s4_5f97 with dissolve
    mc "How… did you remember us?"
    play sounds2 mmove 
    scene s4_5f98 with dissolve
    Mi "..."
    scene s4_5f99 with dissolve
    Mi "When you began following me… something felt strange."
    Mi "Like we had met before."
    scene s4_5f100 with dissolve
    pause 1.1
    scene s4_5f99 with dissolve
    Mi "Even though I was seeing you for the first time…" 
    Mi "It felt wrong."
    Mi "I knew bringing you to the camp was reckless… but the feeling wouldn’t leave me."
    scene s4_5f101 with dissolve
    pause 1.1
    scene s4_5f102 with dissolve
    Mi "And then…"
    Mi "When you said my name…"
    Mi "Everything just… went foggy."
    Mi "…and fragments of memory began to surface."
    scene s4_5f101 with dissolve
    pause 1.1
    scene s4_5f102 with dissolve
    mc "And you believed right away?"
    scene s4_5f101 with dissolve
    Mi "Not completely."
    Mi "I thought maybe it was just my imagination…"
    Mi "But after speaking with my teacher…"
    Mi "(whispering) …yes."
    scene s4_5f94 with CropMove(time=0.1, mode='slideup')
    Mi "I-in any case, we’re here."
    scene s4_5f96 with dissolve
    Mi "Straight ahead, then left. You’ll find the infirmary there."
    Mi "I… should go warn the others."
    Mi "And see if I can find something for you."
    mc "Thanks, Mir."
    Mi "Don’t mention it."

    scene black with dissolve 
    pause 2.1
    "A moment later, inside the camp’s infirmary."

    scene s4_5g33 with dissolve
    k "So… how is it?"
    scene s4_5g34 with dissolve
    mc "Hard to say."
    mc "Looks better than before."
    scene s4_5g33 with dissolve
    k "You know, old man… I’ve been thinking."
    scene s4_5g34 with dissolve
    mc "Oh? About what?"
    play sounds2 mmove 
    scene s4_5g35 with dissolve
    k "How fragile we really are."
    k "Just one blow, and I was gone."
    k "Funny, isn’t it?"
    k "Years of training… and it all means nothing."
    mc "Sometimes there are limits you simply can’t push past."
    play sounds2 clench 
    scene s4_5g36 with dissolve
    k "Hey, hey."
    k "Aren’t you supposed to be encouraging me?"
    scene s4_5g37 with dissolve
    mc "I could."
    mc "But I doubt that’s what you need."
    k "..."
    mc "You’re scared."
    scene s4_5g39 with dissolve
    k "And if I am?" 
    k "So what?"
    scene s4_5g38 with dissolve
    mc "People treat fear of death like it’s a flaw."
    mc "“You’re a coward,” they say."
    mc "But there’s nothing wrong with valuing your life."
    scene s4_5g39 with dissolve
    k "Easy for you to sa—"
    play sounds2 whoosh  
    scene s4_5g40 with CropMove(time=0.1, mode='slideright')
    k "Ah~~"
    "A soft breath escapes her."
    scene s4_5g41 with dissolve
    mc "What I see… is a frightened girl."
    mc "Someone who’s afraid to open up to others."
    scene s4_5g42 with dissolve
    pause 2.1
    scene s4_5g43 with dissolve
    k "Oh, screw you."
    play sounds2 mmove 
    scene s4_5g44 with dissolve
    mc "..."
    k "Why’d you go quiet?"
    mc "You have a lot of scars."
    k "Oh, I know."
    k "Ugly, right?"
    play sounds2 rustling2 
    scene s4_5g45 with dissolve
    mc "I’ve told you what I think of them."
    k "You’re a damn weirdo if you find them attractive, old man."
    scene s4_5g46 with dissolve
    mc "Maybe."
    mc "But every scar is a memory."
    mc "A story."
    mc "Experience."
    mc "Nothing to be ashamed of."
    scene s4_5g47 with dissolve
    k "(Afraid? What nonsense. I’m an Inquisitor. I don’t feel fear!)"
    scene s4_5g48 with dissolve
    k "(And yet… I’m sitting here naked in front of him.)"
    k "(And he’s not even looking at me like a woman.)"
    scene s4_5g49 with dissolve
    k "(What’s the catch? What does he get out of this?)"
    k "(No… I don’t want him looking at me like that.)"
    play sounds2 whoosh  
    scene s4_5g50 with CropMove(time=0.1, mode='slideright')
    k "(It’s… uncomfortable.)"
    scene s4_5g51 with dissolve
    mc "Something wrong?"
    scene s4_5g52 with dissolve
    k "Just… thought you’d jump me."
    k "Not… this."
    scene s4_5g51 with dissolve
    mc "Sometimes simple care can do more than anything else."
    scene s4_5g53 with dissolve
    k "Hmph…"
    mc "(Her worldview’s not that different from Olivia’s. Both expect a trap in even the simplest kindness…)"
    scene s4_5g54 with dissolve
    mc "(Because opening up is terrifying.)"
    play sounds2 whoosh  
    scene s4_5g55 with CropMove(time=0.1, mode='slideup')
    play sounds3 clothess 
    mc "You need rest."
    mc "So relax at the festival tonight."
    play sounds2 mmove 
    scene s4_5g56 with dissolve
    mc "I’ll handle the rest."
    scene s4_5g57 with dissolve
    pause 1.1
    play sounds2 mmove 
    scene s4_5g58 with dissolve
    mc "Alright?"
    play sounds3 footstep2 
    scene s4_5g59 with dissolve
    k "Mhm..."

    scene s4_5g60 with dissolve
    Mi "How is she?"
    mc "Better."
    scene s4_5g61 with dissolve
    Mi "I’m glad to hear that."
    scene s4_5g62 with dissolve
    mc "So… how are things here?"
    scene s4_5g61 with dissolve
    Mi "The camp has mostly accepted your presence."
    Mi "There were a few objections, but I handled them."
    scene s4_5g62 with dissolve
    mc "Thanks, Mir."
    Mi "..."
    scene s4_5g65 with dissolve
    mc "Something bothering you?"
    scene s4_5g64 with dissolve
    Mi "How did you—"
    scene s4_5g65 with dissolve
    k "Your face gives you away."
    Mi "..."
    scene s4_5g63 with dissolve
    Mi "I… would like to know more about you."
    Mi "But I also understand this may not be the right moment."
    scene s4_5g65 with dissolve
    k "Why not?"
    k "We’ve got plenty of time."
    scene s4_5g66 with dissolve
    Mi "Because of the ceremonial dance."
    Mi "Speaking of which… would you like to join?"
    scene s4_5g67 with dissolve
    k "I don’t really care either way. If the old man’s in, so am I."
    k "What do you say?"
    scene s4_5g68 with dissolve
    mc "Why not?"
    scene s4_5g69 with dissolve
    Mi "But… you’ll need to change your clothes."
    Mi "I understand you came here with good intentions, but to the others, you’re still outsiders."
    scene s4_5g70 with dissolve
    mc "Just clothes?"
    mc "Or anything else?"
    scene s4_5g71 with dissolve
    Mi "Under no circumstances are you to draw your weapon."
    Mi "No matter what happens… please don’t."
    Mi "That’s my promise to the camp."
    scene s4_5g72 with dissolve
    mc "..."
    mc "Even if my life’s at risk?"
    scene s4_5g71 with dissolve
    Mi "I’ll handle it."
    scene s4_5g72 with dissolve
    mc "Alright."
    play sounds2 footstep2  
    "([mc] steps away to change.)"

    scene s4_5g73 with dissolve
    k "Tell me, pointy-ears… what is really going on?"
    scene s4_5g74 with dissolve
    Mi "I don’t see what you mean."
    scene s4_5g73 with dissolve
    k "You could’ve taken his weapon."
    k "Why didn’t you?"
    Mi "..."
    scene s4_5g75 with dissolve
    k "Got me thinking." 
    k "You sure you can protect us?"
    scene s4_5g76 with dissolve
    mc "We’re not children."
    mc "We can handle ourselves."
    play sounds2 mmove 
    play sounds3 footstep2 
    scene s4_5g78 with dissolve
    b "..."
    scene s4_5g77 with dissolve
    mc "What?"
    scene s4_5g78 with dissolve
    k "Pointy-ears… I’ll give you this, you’ve got great taste."
    Mi "Yes. Thank you."
    
    scene black with dissolve 
    pause 4.3
    "A moment later, they stepped out of the infirmary, making their way toward the center of the camp.."

    scene s4_5g21 with dissolve
    pause 1.1
    k "Why the long face? We’re at a festival, at least pretend to smile."
    scene s4_5g22 with dissolve
    mc "I am happy."
    scene s4_5g21 with dissolve
    k "My ass you are."
    k "Talk. What’s wrong? You were fine a minute ago."
    mc "..."
    scene s4_5g4 with dissolve
    mc "The thought that I ran off and left them there…"
    mc "It won’t leave me alone."
    mc "Feels… wrong."
    scene s4_5g5 with dissolve
    k "We’re all in the same boat."
    k "Only difference, you don’t have a hole in your chest."
    play sounds2 mmove 
    scene s4_5g6 with dissolve
    k "You know… you should try it sometime. It really changes how you see things."
    scene s4_5g7 with dissolve
    mc "Funny, coming from you."
    scene s4_5g6 with dissolve
    k "I admit, you’re a bad influence."
    k "Before, I’d charge straight into the slaughter without thinking."
    k "Now…"
    k "I still do, just with a thought."
    scene s4_5g7 with dissolve
    mc "Progress—"
    scene s4_5g6 with dissolve
    k "You okay?"
    play sounds2 clothess 
    scene s4_5g8 with dissolve
    pause 1.1
    scene s4_5g9 with dissolve
    pause 1.1
    scene s4_5g10 with dissolve
    k "…Damn. She’s practically naked."
    play sounds2 bells1
    scene s4_5g2 with dissolve
    pause 1.1
    scene s4_5g3 with dissolve
    mc "Didn’t think that would surprise you."
    k "Old man, anyone would be surprised."
    k "You’ve seen how modest pointy-ears usually dresses."
    k "Now compare that to {b}this."
    play sounds2 clothess 
    scene s4_5g11 with dissolve
    mc "Don’t forget, we’re still in the past."
    k "Which makes it even more interesting."
    k "People don’t just flip their worldview like that."
    play sounds1 bells2 volume 0.1
    scene s4_5g12 with dissolve
    mc "Didn’t expect to see you like this…"
    scene s4_5g13 with dissolve
    Mi "Is something wrong?"
    scene s4_5g12 with dissolve
    mc "You’re always so reserved… but right now there’s none of that left."
    scene s4_5g13 with dissolve
    Mi "I don’t understand."
    scene s4_5g17 with dissolve
    k "Your outfit, pointy-ears. It barely covers anything."
    Mi "Does it?"
    Mi "Everything essential is concealed."
    scene s4_5g16 with dissolve
    mc "If you’re comfortable, who are we to judge?"
    mc "But… what is this?"
    Mi "We only wear it on special occasions."
    Mi "It’s a tradition passed down from ancient times."
    play sounds2 bells1
    scene s4_5g18 with dissolve
    pause 1.1
    play sounds3 mmove 
    scene s4_5g19 with dissolve
    k "Sounds like your ancestors were just perverts."
    scene s4_5g20 with dissolve
    Mi "People see what troubles their own hearts."
    Mi "They were pure of spirit."
    Mi "Unlike you, pervert."
    play sounds3 mmove 
    scene s4_5g14 with dissolve
    Mi "You are guests here. So as I respect your culture…"
    Mi "please respect mine."
    scene s4_5g15 with dissolve
    mc "(She’s right. Who am I to judge another culture?)"
    mc "You’re right. That was tactless of us."
    scene s4_5g14 with dissolve
    Mi "I’m glad to hear that."
    Mi "Enjoy yourselves, I need to check on something."
    play sounds2 bells3
    scene s4_5g21 with dissolve
    k "(whispering) “Pervert”?"
    k "(whispering) Hearing that from her… must’ve hit a nerve."
    scene s4_5g22 with dissolve
    mc "Next time, choose your words more carefully."
    mc "Last thing we need is to damage relations with her."
    mc "It wasn’t the outfit that surprised you."
    mc "It was how open she was."
    scene s4_5g21 with dissolve
    k "..."
    k "I’m not promising anything."
    scene s4_5g23 with dissolve
    k "So, what now?"
    k "I’m bored."
    scene s4_5g24 with dissolve
    mc "Sounds like they’re having trouble."
    scene s4_5g25 with dissolve
    elf "Ú-istam si. Hi dîr tolatha erchir. Garo nin i FEB hi danna. \n(We don’t know, she should’ve arrived by now. We’re worried the FEB may have taken her.)"
    elf "Rau veleg danna o lû si… \n(They’ve been getting more aggressive lately…)"
    scene s4_5g27 with dissolve
    Mi "An i sen angen nin i mereth hen veleg. \n(That’s exactly why we need this festival.)"
    Mi "Ae ú-badam hen… rand veleg danna na nin. \n(Without it… problems may arise.)"
    scene s4_5g28 with dissolve
    elf "Mir, melin chen, ach… \n(Mir, I love you, but…)"
    elf "Ú-beria i narn oen nin an i lû hen. \n(Instruments alone won’t carry us.)"
    scene s4_5g27 with dissolve
    Mi "Tegil nin beria hen oen. \n(Then we’ll have to.)"
    scene s4_5g28 with dissolve
    elf "..."
    elf "Nae… badam. \n(Alright.)"
    play sounds2 mmove 
    scene s4_5g29 with dissolve
    mc "Hey, is everything okay?"
    scene s4_5f108 with dissolve
    Mi "It’s fine. I’ll handle it."
    Mi "But thank you."
    mc "..."
    scene s4_5f109 with dissolve
    mc "Kali?"
    scene s4_5f108 with dissolve
    k "Hm?"
    scene s4_5f109 with dissolve
    mc "You used to be an ido—"
    scene s4_5f110 with dissolve
    k "No."
    scene s4_5f109 with dissolve
    mc "Why not?"
    scene s4_5f110 with dissolve
    k "That was a long time ago."
    k "And they wouldn’t approve."
    k "These pointy-ears barely like their own kind. What makes you think they’d welcome someone like me?"
    scene s4_5f112 with dissolve
    mc "You won’t know unless you try."
    scene s4_5f111 with dissolve
    k "..." 
    scene s4_5f113 with dissolve
    pause 1.1
    play sounds2 bodytap
    scene s4_5f114 with dissolve
    mc "Come on, I’m curious to hear how good you really were."
    play sounds3 mmove
    scene s4_5f115 with dissolve
    k "If I embarrass myself, I’m dragging you down with me."
    scene s4_5f116 with dissolve
    mc "(That’s the spirit.)"
    play sounds2 systemnotification
    scene s4_5f117 with dissolve
    keep3 "(Don’t forget why we’re here.)"
    mc "(If I had the option to go back, I would.)"
    keep3 "(I know.)"
    scene s4_5f118 with dissolve
    keep3 "(And keep your weapon on you. I don’t like the atmosphere here.)"
    mc "(Why?)"
    keep3 "(Call it a feeling.)"
    scene s4_5f120 with dissolve
    mc "(Didn’t know implants had feelings.)"
    keep3 "(I’m not an implant.)"
    mc "(Then what are you? You’re in my head.)"
    keep3 "..."
    scene s4_5f118 with dissolve
    keep3 "(You don’t have sufficient clearance.)"
    mc "Suit yourself."
    Mi "…Are you sure?"
    play sounds2 footstep2 
    scene s4_5g30 with dissolve
    k "Wasn’t my idea."
    k "All the applause goes to the old man."
    k "Go on, refuse already, and I’ll return to him looking tragic, making sure to mention how awful you all are."
    scene s4_5g31 with dissolve
    Mi "Why not give it a try?"
    scene s4_5g30 with dissolve
    k "You’re kidding, right?"
    k "Do you see what I am?"
    k "Human."
    k "Hu-man."
    scene s4_5g31 with dissolve
    Mi "Better that… than a ruined festival."
    play sounds2 mmove 
    scene s4_5g32 with dissolve
    k "You’re actually insane…"
    scene s4_5f152 with dissolve
    k "(Then again, I’m no better.)"
    k "(A singer? Me?)"
    play sounds2 bodytap
    scene s4_5f153 with dissolve
    k "(For the past few decades all I’ve done is tear bodies apart.)"
    k "(And now… after all this time… they’re asking me to sing?)"
    stop music fadeout 2.1
    scene s4_5f154 with dissolve
    pause 1.1
    scene s4_5f153 with dissolve
    pause 1.1
    scene s4_5f155 with dissolve
    k "(Hah… guess it’s been a while since I’ve humiliated myself.)"
    scene s4_5f156 with dissolve
    k "(Doesn’t matter. The old man wanted to see what I can do?)"
    scene s4_5f157 with dissolve
    k "(Oh… I’ll show him.)"
    k "(I’ll give it everything.)"
    scene s4_5f158 with dissolve
    k "Ready for some fun?!"
    play music1 kalising fadein 5.5 
    scene s4_5f159 with dissolve
    k "(Just don’t choke at the last second…)"
    play sounds3 clench 
    scene s4_5f160 with dissolve
    pause 1.1
    scene s4_5f161 with dissolve
    pause 1.1
    scene s4_5f162 with dissolve
    pause 1.1
    scene s4_5f161 with dissolve
    k "(Don’t choke...)"
    scene s4_5f163 with dissolve
    "A fragile melody finds its way out of her."
    # 

    scene s4_5f116 with dissolve
    mc "(You know, Third… I was thinking what’s it like when your fate is already decided?)"
    play sounds2 systemnotification
    scene s4_5f164 with dissolve
    keep3 "(You mean the system?)"
    mc "(Yeah. {w=0.6}Imagine staking your whole life on something you love…)" 
    mc "(…and never knowing all your efforts were meaningless.)"

    play sounds2 whoosh 
    play sounds4 bells1 
    play sounds1 handclap2
    scene s4_5f123 with CropMove(time=0.1, mode='slideright')
    keep3 "(You humans are strange creatures.)"
    keep3 "(Always looking for meaning in such simple things.)"
    mc "(You think so?)"
    play sounds3 whoosh 
    play sounds4 bells1 
    play sounds1 bells2 volume 0.1 fadein 1.1 loop 
    scene s4_5f122 with CropMove(time=0.1, mode='slideleft')
    pause 1.1
    play sounds2 whoosh 
    play sounds4 bells1 
    scene s4_5f124 with CropMove(time=0.1, mode='slideright')
    mc "(There’s value in the little things.)"
    keep3 "(Little things don’t defend a galaxy.)"
    play sounds3 bells1 
    play sounds handclap2 
    scene s4_5g2 
    pause 1.1
    scene s4_5f125 with dissolve
    mc "(A galaxy? That’s quite an ambition.)"
    mc "(Fine. Then answer me this, if you don’t get to choose how to live your own life…)"
    scene s4_5f126 with dissolve
    mc "(…doesn’t that make the galaxy the author of your fate?)"
    mc "(And if you were given the choice {w=0.5}wouldn’t that give you the right to shape the galaxy’s fate in return?)"
    keep3 "..."
    play sounds3 bells1 
    play sounds handclap2 
    scene s4_5f127 with dissolve
    keep3 "(That makes no sense.)"
    mc "(Exactly.)"
    play sounds2 whoosh 
    scene s4_5f128 with CropMove(time=0.1, mode='slideright')
    mc "(Then just… live.)"
    play sounds2 clench 
    play sounds2 whoosh 
    scene s4_5f129 with CropMove(time=0.1, mode='slideleft')
    Mi "Will you dance with me?"
    scene s4_5f130 with dissolve
    mc "(And the rest…)"
    scene s4_5f131 with dissolve
    mc "I don’t know if—"
    Mi "Just trust me." 
    play sounds2 footstep1 
    play sounds4 mmove 
    scene s4_5f132 with dissolve
    pause 1.1 
    scene s4_5f134 with dissolve
    pause 1.1 
    play sounds2 whoosh 
    play sounds handclap2 
    scene s4_5f135 with CropMove(time=0.1, mode='slideright')
    mc "(Let it be what it will.)"
    scene s4_5f136 with dissolve
    pause 1.1
    play sounds2 bells1 
    scene s4_5f137 with dissolve
    mc "Why me?"
    play sounds2 whoosh 
    play sounds handclap2 
    scene s4_5f138 with CropMove(time=0.1, mode='slideright')
    Mi "(whispering) You looked… too sad."
    scene s4_5f139 with dissolve
    Mi "(whispering) And… I wanted to cheer you up."
    play sounds2 whoosh 
    scene s4_5f140 with CropMove(time=0.1, mode='slideleft')
    mc "(whispering) Others are staring at us. Are you sure this won’t cause trouble?"
    play sounds handclap2 
    scene s4_5f141 with dissolve
    Mi "(whispering) For us, dance is more than celebration. It’s a symbol."
    play sounds2 whoosh 
    scene s4_5f142 with CropMove(time=0.1, mode='slideright')
    Mi "(whispering) The elves trust me. And this is how I show that I trust you."
    play sounds2 bells1 
    play sounds2 whoosh 
    scene s4_5f143 with CropMove(time=0.1, mode='slideleft')
    Mi "(whispering) It’s my way of protecting you."
    scene s4_5f144 with dissolve
    mc "That’s too much honor for someone like me."
    play sounds3 whoosh 
    play sounds2 bells1 
    scene s4_5f146 with CropMove(time=0.1, mode='slideup')
    Mi "(whispering) I don’t even know why myself."
    scene s4_5f147 with dissolve
    Mi "(whispering) Maybe it’s the memories… or perhaps the promise."
    scene s4_5f150 with dissolve
    Mi "(whispering) Funny, isn’t it?"
    Mi "(whispering) Others follow me… and yet I’m the one believing in something so foolish."
    scene s4_5f151 with dissolve
    pause 1.1
    scene s4_5f148 with dissolve
    Mi "(whispering) Tell me… {w}what will I become in the future?"
    scene s4_5f149 with dissolve
    mc "Why ask that now?"
    scene s4_5f145 with dissolve
    Mi "(whispering) In those memories… I saw things I shouldn’t have."
    scene s4_5f146 with dissolve
    Mi "(whispering) My future."
    pause 1.1
    scene s4_5f144 with dissolve
    Mi "(whispering) I’m afraid…"

    $ persistent.chapter_act4_5_scene += 1
    play sound mouseclick
    show pause 
    n "Yo!"
    n "Thats all for now."
    pause 1.1
    pause 1.1 


    