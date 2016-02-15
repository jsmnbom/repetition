# Code for scene 1, including the code for the poster minigame at the beginning of the game

label scene01:
    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Serene-Separations-Soundtrack.ogg", loop=True, fadein=1)
    with Fade(0.5, 1.0, 0.5)

    centered "{size=+10}Let me tell you a story.{/size}"
    centered "{size=+10}{cps=*0.25}Ah...{/cps} But where do I start?{/size}"
    centered "{size=+10}I suppose I should start with my name.{/size}"
    centered "{size=+10}I am [name] SURNAME.{/size}"

    show book sensei_and_me
    $ renpy.pause(5)
    "I have been living with my sensei for as long as I remember.{w} While he might not be family, he is the only person I have left."

    show book flames
    $ renpy.pause(5)
    "I barely remember my parents. They went away when I was little...{w} Sensei never wanted to tell me about them, other than that they were supposedly heroes.{w} I believe him."

    show book home
    $ renpy.pause(5)
    "And in their absence, he has cared for me in his mountaintop home. He has taught me everything I know.{w} While his house might seem out of the way at first, it is actually a technological heaven.{w} He specialises in a subject known as \“Communication and IT\”."

    "He really is an amazing person!{cps=1}...{/cps} Or should I say \“was\”.."

    hide book with dissolve
    centered "{size=+10}This is where my story begins.{/size}"
    
    "I opened my eyes slowly. Sunlight streamed in from the windows."

    scene sensei_room with dissolve
    show me with dissolve

    "This was weird... Sensei would usually have woken me by now."
    "I looked around in confusion. The room was exactly like I had left it, when I had gone to bed.{w} But sensei was nowhere in sight."
    "I found the kettle that we usually use for boiling water.{w} It was completely cold."
    "I was about to walk away when I noticed a small slip of paper."

    me "Wait, is that..?"

    "I picked it up{nw}"
    show overlay sensei_letter at top with dissolve
    extend ", reading over each word carefully."

    "As I read over the words, I could not help but despair.{w} The outside world sounded like a dangerous place, filled with mystery and horror. But then,{w} I thought back to my sensei's words.."

    hide overlay

    scene sensei_room_flashback
    with flash
    show sensei with dissolve
    sensei "With the power of communication/IT we can do {i}everything!{/i}"
    hide sensei with dissolve
    scene sensei_room
    with flash

    "With a look of determination in my eyes, I grabbed my bag and packed only the things of utmost necessity."

    scene mountains
    with door_trans
    $ renpy.sound.play("sound/fx/door_close.ogg")

    "As I closed the door behind me and looked at the mountains stretching out before me, I felt an ounce of regret."

    menu:
        "Go back and stay?"
    
        "No! Go on an adventure!":
            jump __adventure
    
        "Yeah... No place is better than home.":
            jump __back_home

label __back_home:
    "With a sigh of resignation, I turned back towards the house.\n"
    scene sensei_room
    with door_trans
    $ renpy.sound.play("sound/fx/door_close.ogg")
    extend "Walking back inside, I slammed the door behind me."
    me "I suppose... I couldn't do it after all."

    "I looked at the companion cube on the floor."

    me "But you still love me... Right?"
    show cubey cubey at left with dissolve:
        yoffset -50
        zoom 0.3
    cubey "I will love you forever! So now, don't go running off again... Don't... {w}Be... {w}Naughty."
    "I gave the companion cube worried glances, as I slowly backed away."
    show cubey cubey at left:
        yoffset -50
        zoom 0.3
        1.0
        linear 0.3 zoom 0.35
        1.0
        linear 0.3 zoom 0.40
        1.0
        linear 0.3 zoom 0.45
    "The cube seemed to move towards me, getting ever so slightly closer, every time I blinked."

    "The companion cube was getting awfully close now. A hollow noise resounded as my back hit the wall."
    cubey "Nowhere to go, nowhere to go, nowhere to go..."
    $ die(0)
    "No one was close enough to hear my screams."
    jump you_dead

label __adventure:
    $ renpy.sound.play("sound/fx/door_close.ogg")
    "With a sigh, I slammed the door shut behind me, and looked towards the horizon.{w} The journey before me would be long and arduous, but I knew that I had no choice. It was my fate."

    scene cliffs with fade_scene
    
    $ renpy.pause(5)

    scene town town with fade_scene

    me "Oh, wow... It feels like I've been walking for days!"
    "I looked at the city rising up before me, my entire body aching from a long and tiring walk.{w} At least, that was what my body told me. My map told a different story."
    me "I should find a place to rest..."
    "I looked around at the houses gathered. Many of them had lights on behind the windows, though most of them had their curtains down. The streets were entirely empty, except for a few bottles lying about, and a stray cat every once in a while. A tumbleweed would not be misplaced."

    me "I wonder where all the people are?"

    scene mansion ext with fade_scene
    "Walking a bit further down the road, revealed a pompous-looking house with the sign “Mayor” above the entrance. {w}A confused-looking frog was standing by the entrance, looking at a piece of paper on the wall while mumbling to himself. {nw}"

    show froggy hi with dissolve
    extend "The frog suddenly seemed to notice me, and waved me over."

    show froggy hi_talking with dissolve

    $ renpy.sound.play("sound/fx/First Call.ogg")

    froggy "Greetings!{w} Salutations!{w} Might I ask who you are, and what you are doing here?"

    show me at left
    show froggy hi_talking at right with move

    me "Uh... Yeah... Hi. My name is [name]! I'm really just passing by, though I would like to know if you have any places to stay?"
    froggy "I am glad to make your acquaintance, [name]!"
    froggy talking "I am called Froggy! I am the mayor of this small town." #this one?
    froggy "Being a small town as this is, I can't say that we have any hotels or the likes. Sorry to disappoint you."
    me "No, it's okay. I suppose I should be on my way, then?"
    froggy "W-wait a second! Actually, there is something I could use a second opinion on. Would you mind staying for a bit, helping out a mayor in need?"

    menu:
        "Help Mayor Froggy?"
        "No":
            jump __no_help
        "Yes":
            jump __postermm_start

label __no_help:
    me "Actually, I'm... Rather busy at the moment! If you wouldn't mind, I need to be on my way."
    froggy displeased "That's a shame. I hope nothing bad happens to you on your journey, though."

    scene town walk

    "I turned my back towards the mayor, and started walking out of the town. Since it was a small town, the walk wasn't very far."

    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Unity.ogg", loop=True, fadein=1)
    scene forest start
    with Fade(0.5, 1.0, 0.5)

    "At the edge of the city, a large forest stretched out before me. The thick crowns cast solid shadows on the ground, making it harder to see, but not impossible. A small forest path twisted its way between the trees."
    "I started walking along the forest path, enjoying the gentle breeze that whistled through the trees.{w} The path slowly grew more unclear, until it dwindled down into several smaller animal paths."

    scene forest dark
    "As I got further into the woods, I finally had to admit that I was lost. The large canopy had grown thicker, letting even less light come through the countless leaves. The wind that had earlier been nice and refreshing, suddenly felt harsh and prickly on my skin."
    "My ears suddenly picked up on a very low sound. Something that sounded almost like... A growl?..."
    "Looking around in confusion, I searched for the source of the sound. Surely it couldn't have been my imagination?"

    "As the leaves of a bush rustled to my right, I whipped my head in that direction. {nw}"
    show wolves at right with dissolve
    extend "Out of the bush appeared five large, black wolves, snarling menacingly, with their teeth bared, and their eyes fixed on me."
    show me at left with dissolve
    me "E-... Easy now... I'm sure we can work this out, yes...?"
    "My plea was answered by a sharp bark from the foremost wolf, followed up by barks from the four others behind it. {w}I was about to turn around and make a run for it, when the wolves finally decided to jump at me."
    me "B-... Blood?... Is this... My blood?..."
    me "AAARRGGGHHHHH"
    $ die(1)
    "The woods were finally filled with silence."
    jump you_dead
    

label __postermm_start:
    $ postermm_points = 0
    $ __postermm_done = {}

    froggy "I am glad to hear it, [name]."
    froggy "See, I have been working on a campaign to reduce the number of bottles and cans lying about. Sadly, the people in this village don't seem to care much about their mayor! Or the environment, for that matter."
    me "So what do you want me to do?"
    froggy "Well, I was thinking of making a promotional poster, to raise awareness about the impending doom, that comes from littering bottles everywhere!"
    "I raised an eyebrow at the Mayor, but didn't feel the need to inquire further about the matter. He took the poster from the wall, and raised it in front of me."

    show overlay shitty_poster

    $ renpy.music.stop(fadeout=5)
    $ renpy.music.queue("sound/music/Freddys-Menagerie.ogg", loop=True, fadein=5)

    froggy "So what do you think?"

    hide overlay

    menu:
        "How does the poster look?"
        "It looks amazing!":
            jump __postermm_amazing
        "It needs some work...":
            froggy talking "What would you say is wrong?"
            jump __postermm_wrong
        "It's fucking terrible!":
            jump __postermm_shit
        "Let me see the poster again please.":
            jump __postermm_show


label __postermm_amazing:
    me "It looks fantastic! That has to be the best promotional poster I've ever seen!"
    froggy "Really? You think so? I suppose I should print a couple of thousand posters then, and hang them about. Thanks for the help!"
    me "No problem!"
    "As I waved to him and walked towards the edge of the village, I felt a bit of doubt. Had I chosen the right thing?"
    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Not-As-It-Seems.ogg", loop=True, fadein=1)
    scene forest dark
    with Fade(0.5, 1.0, 0.5)

    "As I approached the forest, the air felt overwhelmingly humid. Small insects and lizards were scurrying around on the forest floor, as I took a weary step forwards.{w} It didn't feel directly hostile. The forest was simply so full of life that it itself felt alive."
    "The trees were swaying in the gentle wind that seemed to blow through the crowns, though barely a breeze could be felt on the forest floor. The rustling of leaves almost made it seem like the trees were having a conversation."
    "While I was following the forest path, looking up at the sky, I suddenly tripped."
    me "Aa-... Huh?"
    "I used my hands to soften the blow, as I looked behind me to see what I tripped over. {w}I couldn't see anything large enough to trip over."
    me "That's... Weird."
    "While mumbling to myself, I got up again and dusted off my palms and knees. {w}Were.. Those trees always so close?"
    "Suddenly, something gripped my ankle tightly. {w}Looking back in fright, I found a mossy root protruding from the ground, coiled around my ankle like a snake. {w}I tried kicking out with my leg to shake it off, but the root adamantly held its ground."
    "As I was distracted by the stubborn root, a second one shot out of the ground and fastened my right wrist. I raised my left hand to try and get it off of me, but the moment I was about to grab it, a third root shot out of the ground and entangled my left wrist too."
    "Fighting futilely against the roots, I could do nothing but look as large network of roots slowly entangled my entire body. An especially thick one lazily burst out of the ground next to me, wrapping itself around my stomach before going back into the earth. {w}It's grip slowly tightened as it dragged me downwards, forcing the air out of my lungs, as the earth slowly swallowed me whole."
    $ die(1)
    "Not even a trace was left."
    jump you_dead


label __postermm_wrong:
    menu:
        "(select a category)"
        "The heading" if (not 'heading' in __postermm_done):
            $ __postermm_done['heading'] = True
            jump __postermm_heading
        "The typography" if not 'typography' in __postermm_done:
            $ __postermm_done['typography'] = True
            jump __postermm_typography
        "The colours" if not 'colours' in __postermm_done:
            $ __postermm_done['colours'] = True
            jump __postermm_colours
        "The text in general" if not 'text' in __postermm_done:
            $ __postermm_done['text'] = True
            jump __postermm_text
        "AIDA" if not 'aida' in __postermm_done:
            $ __postermm_done['aida'] = True
            jump __postermm_aida
        "Nothing, if you fix those errors it's fine." if postermm_points != 0:
            jump __postermm_done
        "Let me see the poster again please.":
            jump __postermm_show


label __postermm_shit:
    froggy "The mayor's eye spasmed a bit, as he stared at me with malice."
    froggy murderous "You... What? How dare you say that to me, the mighty mayor?!"

    "I quickly backed off, as a red aura started to envelop the mayor."
    froggy "We don't... Use swear words here... It's against the law!"
    "As those deep red eyes caught mine, I found that I could no longer move a muscle. As I stood there, helpless, he walked towards me."
    froggy "Do you know what happens to lawbreakers in town, hmm?"
    "The mayor was now close enough, that I could feel the stinging red aura, slowly peeling away my skin."
    show overlay red_haze with dissolve
    froggy "You may never utter a swearword again."
    $ die(1)
    froggy "Have you never heard of constructive criticism?"
    hide overlay
    jump you_dead    


label __postermm_heading:
    menu:
        "What's wrong with the heading?"
        "It's too big":
            froggy talking "Do you think so? I certainly have trouble seeing it as it is, at least without glasses. But I am sure that you're more qualified to say so than I."
            $ postermm_points -= 1
        "It's too small":
            froggy "Yes, I suppose it could be a bit larger. We really want the message to stand out, to attract more people!"
            $ postermm_points += 1
        "You should totally use WordArt! It's the professional choice!":
            froggy "What did you say? Well.. I suppose I do have word, but are you truly sure about this? It looks like something my grandson would do."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_typography:
    menu:
        "What's wrong with the typography?"
        "The body text should be always without serifs.":
            froggy "Are you sure about that? I think it puts a bit of strain on the eyes, but I suppose you know best."
            $ postermm_points -= 1
        "You should use a fancy cursive font!":
            froggy "Wouldn't that be hard to read? People shouldn't have to strain their eyes to read the message."
            $ postermm_points -=1
        "You should use the same font for all of text.":
            froggy "Yes... I suppose I see what you mean by that. The text by the pricing is definitely a different font."
            $ postermm_points +=1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_colours:
    menu:
        "What's wrong with the colours?"
        "The colour of the body shouldn't match the background. It makes it difficult to distinguish.":
            froggy "Yes, I suppose you're right. It {i}is{/i} quite hard to read. I just really like green."
            $ postermm_points += 1
        "The white background is a tad bit boring. How about making it red?":
            froggy "Are you sure? Red seems quite stressing for the eyes, and a bit aggressive. We don't want to scare people away!"
            $ postermm_points -= 1
        "Black font colour is a bit boring. Try pink!":
            froggy "While it is a pretty colour and all, wouldn't that be difficult to see?.. Oh, well, I suppose you know best."
            $ postermm_points -= 1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_text:
    menu:
        "What's wrong with the text?"
        "It's full of grammatical errors and spelling errors!":
            froggy "Oh?.. Well, I wasn't quite sure how to spell a lot of these things, and I didn't bother to look the words up in a dictionary. {w}I'll have my secretary check through this."
            $ postermm_points += 1
        "The First Letter In Every Word Should Be Capitalized.":
            froggy "What, isn't that what they do in Germany or something?"
            $ postermm_points -= 1
        "This text is missing exclamation points!!1!":
            froggy "What now? Why did you add that number at the end of your sentence?"
            $ postermm_points -=1
        "Let me see the poster again please.":
            jump __postermm_show
    jump __postermm_back


label __postermm_aida:
    me "Did you use the AIDA model to create this?"
    froggy "Ai-what now? Ai desu?"
    me "No, no, it's a communication model."

    menu:
        "So what is this so-called AIDA model?"
        "Action-Interest-Disire-Action":
            froggy "Action twice? That seems wrong"
            $ postermm_points -= 1
        "Attention-Ideas-Disinterest-Action":
            froggy "Why would I want someone to be disinterested?"
            $ postermm_points -= 1
        "Another-Invisible-Dragon-Attack":
            froggy "Dragon attack? Where?"
            $ postermm_points -= 1
        "Attention-Interest-Desire-Action":
            froggy "Now that you mention it, I do think I've heard of that somewhere before. I could probably ask my secretary to do something with that."
            $ postermm_points +=1
    jump __postermm_back

label __postermm_back:
    "Anything else wrong with this poster?"

    menu:
        "Yes":
            froggy "What else is wrong with it then?"
            jump __postermm_wrong
        "No, it's fine now":
            froggy "Let's take a look at it, then..."
            jump __postermm_done
        "Let me see the poster again please.":
            jump __postermm_show

label __postermm_done:
    "DEBUG: You scored [postermm_points] points :)"
    
    if postermm_points <= 2:
        jump __postermm_lose
    elif postermm_points > 2 and postermm_points <= 4:
        froggy "Well I guess it turned out alright. It is definitely better than it was before! {w}This campaign might not turn out to be be a total failure after all."
        jump __beforespeech
    elif postermm_points >= 5:
        froggy "This.. This is much better than I thought it could be! {w}This is sure to attract lots of people. Thank you very much!"
        jump __beforespeech
    
    return

label __postermm_lose:
    me "So?.. What do you think?"
    "Mayor Froggy tilted his head as he stared at the poster with something that might have been disgust."
    froggy "Well, uhh, I'd say the results are.. Debatable."
    "I frowned slightly. Had I not done my best to make this campaign a success? Of course I knew the importance of helping the environment. {w}The mayor coughed lightly, bringing my attention back to him."
    froggy "I think we should call it a day, then. "
    "I nodded my head, looking at the front door.{w} Just as I was about to exit the room, however.."

    $ renpy.music.stop(fadeout=5)
    $ renpy.music.queue("sound/music/Volatile-Reaction.ogg", loop=True, fadein=5)

    "Mayor Froggy and I both turned immediately, as a shrill shriek abruptly came from behind us. {w}We both stood there for a while, looking for the source of the ear-piercing sound."
    "Another shriek echoed, turning both of our attention to the discarded poster. {w}It.. Didn't look like a poster anymore.{w} Instead, what used to be a terrible poster had turned into a terrifying paper monster, with sharp teeth and an even sharper voice."
    "I covered my ears as what appeared to be a mouth opened to shriek once again."
    me "What is that even?"
    froggy "It would seem to be the poster. But hey, what's the worst it can do, give us p-paper cuts?"
    "The mayor attempted to make a joke, but his unsure voice made it sound more like a failed attempt at seeming brave. In reality, the frog was trembling in place. The poster seemed to glare at us - or at least, that was what it would have done, had it eyes."
    "Still, what's the worst a single poster can do?"
    "I instantly regretted that thought, as more prototype posters rose up behind the first one, the next more hideous than the previous, all having terrifying voices to match. They seemed to rip themselves apart, to form new, more spiky versions of themselves."
    "I ran towards the door in a final attempt at getting away, when I noticed that we had been surrounded. Several poster monsters stood in the way and hissed at me before I could even get close to the door."
    "All of them slowly move closer in their own bizarre ways, as me and mayor Froggy moved closer together."
    froggy "I suppose th-this.. Would be a fitting time for last words.."
    me "......"
    "No regrets?.. If only things had gone differently.."
    me "Who knows.. In another universe, we might be happy right now."
    "The mayor gulped and nodded, as the poster monsters had finally grown bored of waiting. Moving right next to us, they piled on top of each other, until we were covered in sharp paper spikes. I could feel the many paper cuts all over my body, stinging, slowly giving off blood as they were bleeding me dry."
    $ die(1)
    "What a mess. Someone would have to clean this up later."
    jump you_dead


label __postermm_show:
    show overlay shitty_poster

    froggy "Here you go."

    hide overlay

    $ renpy.rollback(force=True, checkpoints=2)

label __beforespeech:
    froggy "Now that that has been sorted out.. Phew, that really was a day's work or two! You've really saved me, [name]."
    me "No, no, it's okay. Like I said, my sensei taught me to always help those in need."
    "Sounds like you have a very wise sensei!"
    "I winced slightly at the mayor's words, though I didn't correct his assumption. It wasn't relevant for the mayor to know. {w}Barely noticing my hesitation, the mayor continued."
    froggy "Now we just need to print a couple of thousands of these! I can feel the success already!"
    "I raised an eyebrow at the mayor, that suddenly seemed very self-absorbed, as he ranted on."
    froggy "Come, my minion! Advance! You shall help me hang up the posters!"
    me "But we don't even have the posters yet! We only just figured out what to change about them!"
    "The frog tilted his head, pondering for a while, before a light bulb suddenly went off in his head."
    froggy "Oh, but how could I forget? Hurry, to my secretary!"

    scene black
    with fade
    centered "{size=+10}Two hours later...{/size}"
    scene mansion ext
    with fade
    
    "I stood outside an office door a while later, looking out at the streets through an open window. There were still as few people on the streets as there had been when I arrived, but the sun was dangerously close to the horizon. If I didn't get out of the town soon, I would have to go through the thick woods on the north side of the town in almost complete darkness."
    "As the door creaked, I turned my head to see the mayor walk out of his secretary's office with a large stack of posters."
    froggy "Minion! Take half, and follow me!"
    "As he loaded half the stack of posters onto me, I watched him kick the door open and walk off. I wanted to facepalm, had I not been holding a large stack of posters. Also, when did he decide that I'm his minion?! You can't just decide that on your own!"
    me "Oh, well... Doesn't look like I have a say in the matter."
    "I hurried after the mayor, that didn't even look back to check whether I was following or not."

    scene town square
    with fade_scene

    "I finally caught up to the mayor, who was standing in the middle of an open plaza, looking expectantly at me. The street lights were still off, even though it was getting dark, but the remaining sunlight was bright enough that I could still properly see my surroundings."
    froggy "Finally, you come. Now, let's hang up posters everywhere. I don't want anyone to miss them."
    "I nodded meekly at the mayor. He then pulled a tape dispenser from his pocket, somehow balancing the stack of posters on only one of his arms, and handed it to me."
    froggy "If you take the north part of city, I'll take the south part."
    me "Alright. I'm not sure I can find my way around here, though..."
    froggy "I'm sure you'll manage! Let's meet up here again when we're done."
    "I nodded at the mayor, and looked around the plaza."
    me "If the sun is over there, then that must mean... This is north"

    scene town streets evening
    with fade_scene

    "I chose a direction, and walked along the road, taping the posters to the street lamps every time I came across one."
    "As I walked along the many houses, I couldn't help but feel slightly creeped out by the emptiness of the streets, coupled with the diminishing sunlight."
    "The sound of a trash can falling over suddenly startled me, as I froze in place, looking for the perpetrator.{w}.....{w}\nFew moments later, a black cat ran across the streets. I breathed out in relief. For a moment, I had been afraid of something unfortunate happening to me. Deciding that I didn't want to spend longer than absolutely necessary in these empty streets, I finished hanging up posters as fast as possible.
    "

    scene black
    with fade
    centered "{size=+10}A thousand posters, and bit of running, later...{/size}"
    scene town square dark
    with fade

    me "*pant* *pant*"
    "The mayor looked at me with a confused glance."
    froggy "You look like you ran from something. Are you feeling alright?"
    "I raised a hand, signaling for him to wait a moment, my chest heaving heavily. I really wasn't used to running."
    "A couple of minutes later, having finally regained my breath, I raised my head."
    me "Are we... Done now?"
    froggy "Indeed we are! Now, let us go back to my mansion and have a cup of tea, doesn't that sound nice?"
    "I looked down at my weary feet and sighed."
    me "I suppose sitting down for a moment would be nice..."
    froggy "Then it's decided! Hop along, now. No time for dallying."
    "I slumped my shoulders, and walked after the mayor, back to his mansion."
    scene mansion livingroom
    with fade_scene
    "As we were sipping tea, the mayor suddenly spoke."
    froggy "So, [name], it has been a long day. Seeing as I have taken so much of your time, you would be welcome to stay a night in my mansion. And then you can also help me with the competition tomorrow. What do you say?"

    menu:
        "Stay with Mayor Froggy?"
        "Yes! I'd love to stay a night in your mansion!":
            jump __stay
        "No, I think I should be on my way.":
            if postermm_points >= 5:
                $ village_dead = True
                jump __almost_end
            else:
                jump __wolfsquad
                return
label __stay:
    "Next morning comes after this."
    if postermm_points >= 5:
        jump __too_sucessful
    else:
        jump __not_quite

label __wolfsquad:
    #me "No, I think I should get going." -- I just realised that the button says this and that it probably shouldn't be said twice.
    froggy "Really? What a shame. I would have liked to have you stay for another day. But if you insist... I suppose I have to let you go."
    "I nodded, and went out the front door. The street lights were on, making it easier to navigate. It wouldn't be that easy once I got to the forest though. But I had stayed in one place long enough, and it was time to move on."

    $ renpy.music.stop(fadeout=1)
    $ renpy.music.queue("sound/music/Unity.ogg", loop=True, fadein=1)
    scene forest dark
    with fade_scene

    "The chilly forest didn't seem directly hostile. The low moonlight was just enough for me to see where I was going."
    "The light liked to play tricks on my imagination. Sometimes I had to stop and stare at a thing to make sure it wasn't a dangerous monster out to eat me."
    "The rustling leaves and chilly wind didn't help my imagination, as the forest that was actually quite peaceful quickly turned into a hellish swamp out to imprison me and kill me. The trees seemed to grow thorns, and I thought I could see yellow eyes between the bushes, observing me intently."
    "A deep growl interrupted my thoughts, as I froze in place."
    me "Was that my imagination?..."
    "One of the bushes seemed to glow a faint red colour. I rubbed my eyes, still not sure whether this was all something I had imagined."
    "A glowing red shape crept out of the bushes, snarling at me menacingly."
    me "I don't think this is my imagination anymore..."
    "The shape resembled that of a wolf, but it was coated in a malicious, red aura. It wore a collar with the nametag \"fluffy\" on it. A couple of wolves bearing the same red aura followed behind it, all of them glaring at me."
    me "Oh no! It's the mayor's wolf squad! It looks like he really didn't like me leaving..."
    "The foremost wolf barked at me, staring me in the eyes. I gulped, as I stepped slowly backwards. Rationally, I knew that it was impossible to get away from the mayor's wolf squad. Instinctally, however, there was nothing I'd rather do than run."
    "So I ran."
    "I turned my back to the wolves, and ran as fast as I could. {w}I could hear their shallow panting as they chased after me, only a few steps behind."
    "As I turned my head to see how far behind me they were, my foot was caught under a root."
    "My panicked breathing intensified as I crawled away, too much in a hurry to even think about standing up. The wolves had slowed down to walking tempo. They knew that it was game over for me. I knew it too."
    me "Please!.."
    "I knew it was useless, but I couldn't help but beg. The wolves finally decided that they had grown tired of me, though, and pounced. Teeth tore into skin. Claws ripped at flesh."
    $ die(0)
    "My sorry remains were never found."
    jump you_dead

label __too_sucessful:
    scene mansion ext
    "Now we go back to the mansion and sleep. Stuff happens!"
    froggy "The campaign is going so incredibly well!"
    froggy "Perhaps even {i}too{/i} well"
    jump __dragon_eat

label __not_quite:
    froggy "The campaign is not going quite as well as I was hoping."
    froggy "Sure you fixed all the errors with that poster?"
    jump __end


label __dragon_eat:
    scene town square people
    show magenta mad at right
    show overlay flames with dissolve

    "Oh no! A dragon!"

    "You dead :/"

    return

label __almost_end:
    "This is very important to have in here. Totally. Actually, it's just flavour text. Think of the replayability!"
    jump __end

label __end:
    #If village dead then hear dragon in distance
    # The music "Take a chance could maybe work here? or maybe the travelling scene earlier?"
    "I left the village to continue my journey..."
    "But in reality, J totally misunderstood what I wanted to do with this last part, so I'll have to rewrite it when I write the rest. {w}Yay!"
    jump scene02