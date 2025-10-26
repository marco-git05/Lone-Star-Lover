# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.default_text_cps = 20 #0-100 is accepted
define gui.text_size = 30

define s = Character("Silas")
define z = Character("Zephyr")
define mc = Character("[mcname]")
define eggs = ""

default s_affection = 0
default z_affection = 0

image bg black = "#000000"
image bg generic space = "backrounds/bg_generic_space.png"
image bg inside ship = "backrounds/bg_inside_ship.png"
image bg space station = "backrounds/bg_space_station.png"
image bg zephyr house outside = "backrounds/bg_zypher_house_outside.png"
image bg saloon = "backrounds/bg_saloon.png"
image bg street night = "backrounds/bg_street_night.png"
image bg street day = "backrounds/bg_street_day.png"
image bg zephyrs kitchen day = "backrounds/bg_zephyer_kitchen_day.png"
image bg zephyrs kitchen night = "backrounds/bg_zephers_kitchen_night.png"
image silas hotel = "backrounds/bg_silas_hotel.png"

# The game starts here.

label start:

    play music "audio/MainTheme.wav" volume 0.5

    label day_1:
        scene bg generic space with fade

        "{i}Gate A-11... Gate A-11... Ah! I see it now. Finally, I can have some peace far, far away from my office of misery.{/i}"
        "Narrator" "You let out a long yawn."
        "{i}It sucks that I had to wake up early still... I guess vacations still have their ups and downs despite being a form of relaxation. At least the flight will be long enough to catch some sleep before I land on Caeles Terra.{/i}"

        scene bg inside ship with fade

        "Narrator" "You make your way into the ship, quickly finding an available seat. \nA few grunts are let out as you stuff your luggage into the storage next to your new place of slumber for the upcoming handful of hours." 
        "Narrator" "The seat feels cozy as you sink into it and lose a battle against your heavy eyelids."

        stop music

        scene bg black with fade

        pause(3.0)
        
        scene bg inside ship with hpunch

        play music "audio/Conflict.wav" volume 0.5
        
        "Narrator" "WHAM! Your eyes suddenly open as your body lunges forward before getting caught in a seatbelt. Your heartbeat pounds in your ears as you take in your surroundings and question what is happening around you."
        "{i}Strange... I do not remember putting my seatbelt on... I do not even remember falling asleep! A flight attendant must have taken care of me shortly after I knocked out. Gosh, my torso hurts. Why did we land so harshly?{/i}"
        "Intercom" "\"APOLOGIES TO ALL GUESTS ON THE NEBULAE SPACELINES.\"\n\"DUE TO UNFORESEEN CIRCUMSTANCES, OUR PILOTS HAD TO MAKE AN EMERGENCY LANDING.\""
        "Intercom" "\"WE ASK ALL TRAVELERS TO CALMLY GATHER ANY CARRY-ON ITEMS THEY OWN AND TAKE THE CLOSEST EXIT. YOUR FLIGHT ATTENDANTS WILL THEN LEAD YOU TO THE SPACESHIP'S STORAGE UNIT, WHERE YOU WILL BE ALLOWED TO GRAB THE REST OF YOUR LUGGAGE.\""
        "Intercom" "\"WE URGE YOU ALL TO FIND ACCOMMODATIONS QUICKLY AS THIS FLIGHT'S STAFF DOES A ROUTINE MAINTENANCE AND REPAIR CHECK. THE ESTIMATED TIME OF COMPLETION WILL TAKE AROUND{w=0.5}.{w=0.5}.{w=0.5}.\"" 
        "Intercom" "\"THREE TO FIVE BUSINESS DAYS.\""
        "Narrator" "A collective groan and some exclaims emerge from people on board as you unbuckle your seatbelt and jump to your feet to collect all of your luggage."
        "Intercom" "\"OH, BEFORE I FORGET... \""
        "Intercom" "\"WELCOME TO RURIGENA TERRA!\""

        stop music

        scene bg space station with fade

        play music "audio/General Day.wav"

        "{i}Oh my... I should've expected to run into a stressful situation while going on vacation. God forbid I try to relax!{/i}"
        "Narrator" "You continue pushing through luggage before pulling the suitcase with your name out of the large pile."
        $ mcname = renpy.input("What is your name?", length = 32)
        mc "\"Ugh! When did this thing get so heavy?\""
        "{i}I don't even know where I am or where I could stay!{/i}"
        "Narrator" "You clasp your hands over your face and take a deep breath in an attempt to calm down." 
        "Narrator" "Suddenly, you overhear a couple's discussion nearby."
        "Woman" "\"Wow... I don't think a flight has been derailed by this planet in a loooong time!\""
        "Man" "\"Yeah, I think it was about ten years ago. I guess it was due for another surprise. Say, what was the name of the hotel we stayed at the last time this happened?\""
        "Woman" "\"I think it was called {b}The Wrangler Inn{/b}.\""
        "Woman" "\"Once we find all of our luggage, then we can head out. We have to hurry, though. The rooms fill up quickly over there. Do you remember how to get to the hotel?\""
        "Man" "\"Sure, we have to head towards {b}Calico Lane{/b}, and then from there we turn left to {b}Blossom Street{/b} before finally turning to-\"{nw}"
        "Woman" "\"Shhh! Lower your voice, other people might hear us! Just lead the way, there's no need to go over the directions right this second.\"" with vpunch
        "{i}Does it really only take three streets to get to {b}The Wrangler Inn{/b}? I do not know the last street, but maybe I can figure it out along the way. I should start leaving before anyone else does!{/i}"

        stop music

        scene bg street day with fade

        "Narrator" "You take your luggage and quickly walk away from the ship, keeping the street names in your mind. You find {b}Calico Street{/b} and hurry down the road as you start to run out of breath from the long walk."
        "Narrator" "Soon enough, you spot a sign on your left labeled {b}\"Blossom St.\"{/b}"

        mc "\"Finally!\""
        "Narrator" "You take a few seconds to catch your breath before dashing down {b}Blossom Street{/b}, your eyes angled downwards to make sure you don't step in any holes or trip on any bumps in the ground."
        "Narrator" "You keep pushing before suddenly realizing that your body is no longer moving forward. Your face collides with a black, denim barrier before you slam against the ground."
        mc "\"What in the world?\""
        
        show silas angry closed with dissolve
        play music "audio/Romantic.wav"

        "Narrator" "You turn over to your back before your eyes flutter open to look above you. A tall figure adorned in dark clothes stares down at you with an arm stretched out. You grab on and stand up before dusting yourself off."
        mc "{cps=35}\"I'm so sorry!\"{/cps}{nw}"
        mc "{cps=35}\"I didn't plan to be on this planet!\"{/cps}{nw}"
        mc "{cps=35}\"I was taking a flight to a different one!\"{/cps}{nw}"
        mc "{cps=35}\"And then all of a sudden my flight crashed here!\"{/cps}{nw}"
        mc "{cps=35}\"And now I am looking for a place to stay and-\"{/cps}{nw}"
        show silas angry open
        "???" "\"Enough.\"" 
        "???" "\"You should at least have some sense in you to look where you are going.\""

        menu:
            "???" "{cps=5000}\"You should at least have some sense in you to look where you are going.\"{/cps}"
            "\"Huh? But I was looking where I was going...\"":
                pass
            "\"...Can you at least help me figure out where to go from here?\"":
                pass
        
        "???" "\"Where are you heading?\""
        show silas angry closed
        mc "\"I'm going to The Wrangler Inn.\""
        "Narrator" "The man seems to ponder a bit before pointing to a street on the right."
        show silas angry open
        "???" "\"You walk, not run, all the way down and then you will see the inn at the very end of the street. Make sure to stay alert.\""
        show silas angry closed
        mc "\"Okay, got it. Thank you... uhm... What is your name?\""
        show silas default open
        s "\"You can call me Silas. What shall I call you?\""
        show silas default closed
        mc "\"My name is [mcname]\""
        show silas default open
        s "\"Well, [mcname], enjoy your stay.\""
        show silas default closed
        "You let out a small smile before heading off on your way to The Wrangler Inn. Silas disappears in the opposite direction."
        stop music
        hide silas default closed with easeoutleft
        "{i}What a strange encounter... That Silas... He seemed angry with me, yet caring at the same time?{/i}"
        "{i}This road seems awfully lonely. I sure hope he gave me the correct directions! Maybe the inn is just in an isolated area?... I really hope that is the case.{/i}"

        scene bg zephyr house outside with fade
        play music "audio/General Night.wav"

        "Narrator" "After walking a bit further, you see the end of the road without an inn accompanying it. You look around in a slight panic and only find the entrance to a farm up ahead."
        mc "\"Are you serious!? He really gave me the wrong directions? Is this some sort of prank, or does he really not know the way around his town!?\""
        mc "\"I have been walking for so long... By the time I walk back into town, the sun will set, and I will practically be stranded in the streets!\""
        "Narrator" "You take a moment to collect your thoughts and figure out what to do now."
        "{i}Well, someone has to be taking care of that farm... right? I really hope the farm owner is home or I will be doomed for tonight.{/i}"
        "Narrator" "You take your luggage and push open the gate to the farm. Herds of cattle and plentiful crops are seen on either side of you as you get closer and closer towards the door of the farmhouse."
        "Narrator" "You place three knocks on the door and wait for a few seconds before the door swings open. A puzzled man makes eye contact with you before greeting you with a smile."
        
        stop music

        show zephyr default open with dissolve

        play music "audio/Romantic.wav"

        "???" "\"Howdy! My name is Zephyr. You don't seem to be from 'round these parts. What can I call you, dear?\""

        show zephyr default closed

        menu:
            "???" "{cps=5000}\"Howdy! My name is Zephyr. You don't seem to be from 'round these parts. What can I call you, dear?\"{/cps}"
            "\"Uhm... Hello? My name is [mcname].\"":
                pass
            "\"Oh, howdy! My name is [mcname]!\"":
                pass

        show zephyr default open

        z "\"Well, [mcname], what brings you to town? Why did you come knocking on my door?\""

        show zephyr happy closed

        "Narrator" "The man leans against his door frame, giving a kind smile."

        mc "\"I was on my way to Caeles Terra for vacation before my ship crashed here.\""
        mc "\"I have nowhere to go, really, but I overheard a couple talking about a place called The Wrangler Inn.\""

        show zephyr angry closed
        "Narrator" "Zephyr grimaces a little at the mention of the inn."
        show zephyr default open
        z "\"That place is further in town... and it costs a pretty penny.\""

        show zephyr default closed
        menu:
            z "{cps=5000}\"That place is further in town... and it costs a pretty penny.\"{/cps}"
            "\"Well, it doesn't matter the cost, it's all I have.\"":
                pass
            "\"Oh no.... Do you have any other recommendations for where to stay?\"":
                pass

        show zephyr default open
        z "\"Lucky for you, I have a guest room I can offer to you for the duration of your stay.\""
        show zephyr happy open
        z "\"It's free of charge! Knowing that you are somewhere safe for the night is enough for me.\""

        show zephyr happy closed
        menu:
            z "{cps=5000}\"It's free of charge! Knowing that you are somewhere safe for the night is enough for me.\"{/cps}"
            "\"Oh... Well, thank you! I'll stay for tonight and be up and out of your way tomorrow night then.\"":
                pass
            "\"Thank you so, so much! I'm glad I won't have to walk in the streets after dark.\"":
                pass

        "Narrator" "Zephyr steps aside to let you in. His home is decorated with colorful, cozy furniture. Warm lighting surrounds you as you walk down the main hallway of the house and find your way to the guest bedroom."

        stop music 
        scene bg zephyrs kitchen night with fade
        "Narrator" "You let out a deep breath as your tense muscles finally relax."

        mc "I guess this is my room for the night. I shouldn’t unpack too much, only the necessities."

        "Narrator" "You take out the belongings you need for the night and change into comfy clothes to sleep in. As you are checking your phone for updates on your ship, a knock is heard at your door."

        mc "\"Come in!\""

        show zephyr default open with dissolve
        play music "audio/General Day.wav"
        "Narrator" "Zephyr enters the room holding a glass of warm milk and a soft, star-shaped pastry."

        z "\"I’m not sure if you have eaten yet, and I didn’t want to prepare a large meal for you since you need to rest up. I figured this would hold you ‘til the morning.\""

        show zephyr default closed
        mc "\"Thank you, Zephyr… this is very kind of you.\""

        show zephyr happy open
        z "\"My pleasure. Oh, by the way, how do you like your eggs in the morning?\""

        show zephyr happy closed
        menu:
            z "{cps=5000}\"My pleasure. Oh, by the way, how do you like your eggs in the morning?\"{/cps}"
            "Sunny side up.":
                $ eggs = "Sunny side up"
            "Scrambled.":
                $ eggs = "Scrambled"

        show zephyr default open
        z "\"Okay, got it. Sleep well, dear.\""

        hide zephyr with dissolve
        stop music

        "Narrator" "You take some time to enjoy your pastry and milk while scrolling through news about the spaceship crash on Rurigena Terra. After finishing your small meal, you turn off the light and slowly drift into a deep slumber."

        pause(2.0)

        # END DAY 1

    label day_2:
        scene bg day two transition with fade
        pause(3.0)

        scene bg black with fade
        "Narrator" "Warm sunlight fills your room as you wake up. Your eyes softly flutter open to find something yellow stuck to your forehead."
        "Narrator" "You gently remove it — it's a note that reads: {b}\"Good mornin’ darlin'! Breakfast is waiting for you in the kitchen. - Zephyr\"{/b}"
        "Narrator" "You smile before stretching and getting out of bed."


        scene bg zephyrs kitchen with fade
        "Narrator" "As you follow the scent into the kitchen, Zephyr is seen plating two meals."


        show zephyr default open with dissolve
        z "\"Mornin’, [mcname]! I made you some toast, sausage, and eggs. [eggs], just like you like them. Come sit and eat up! Oh, here’s a glass of juice, too.\""

        show zephyr default closed
        "Narrator" "He sets your plate and a shimmering pink drink in front of you."

        show zephyr default open
        z "\"Now, I reckon this drink is unfamiliar to you. Don’t be afraid of it; it’s made from fresh fruits from my garden! It’s full of vitamins, so it’s real good for you!\""

        show zephyr default closed
        "Narrator" "You smile at him before observing the drink. The juice smells slightly sweet as you put the rim of the cup to your lips and take a sip."
        "Narrator" "Zephyr watches you, fidgeting with his thumbs, while you take in the floral and fruity flavor of the drink."

        show zephyr default open
        z "\"So… What do you think?\""

        show zephyr default closed

        menu:
            z "{cps=5000}\"So… What do you think?\"{/cps}"
            "\"I’m not sure if this is my taste…\"":
                show zephyr angry open
                z "\"Oh! I’m sorry. I do own fruits from other planets, but I figured it’d be nice to show you something from here.\""
                z "\"Here, have some water instead.\""
                show zephyr default open
                z "\"Say, where do you come from?\""
                show zephyr default closed
            "\"It’s unique, but it reminds me of home.\"":
                show zephyr happy open
                z "\"Oh, really? That reminds me — I’ve been wondering about where you're from.\""
                show zephyr happy closed


        mc "\"I come from Earth.\""

        show zephyr default open
        z "\"Well, I’ll be! We rarely get Earth folk ‘round here nowadays.\""

        show zephyr default closed
        mc "\"Oh? Why is that?\""

        show zephyr sad open
        z "\"They just don’t appreciate our lifestyle. Our days move quicker here, but our hearts don’t. We don’t rush life. The planet gives us all we need — so we live slow and live well.\""

        show zephyr default closed
        mc "\"Wow… what a shock. Most of my life is practically given to a large screen, so it’s kind of surprising to hear your take on technology.\""

        show zephyr default open
        z "\"Hmm, I see. So what do you do on Earth?\""

        show zephyr default closed
        mc "\"I mainly work on a communications team for a large business. The pay is great, but the work can be insanely boring most of the time.\""
        mc "\"It’s the reason I took this trip, actually. I thought I’d have a chance to relax and enjoy a beachy scenery, it's what Caeles Terra is known for anyway.\""
        mc "\"But I guess the universe didn’t want me to have that just yet. Instead, I get to be stuck here.\""

        show zephyr sad closed
        "Narrator" "You notice that your mood has fallen flat, and you think Zephyr noticed too, since he stares at you with worry in his eyes. You quickly fix your posture and give a small smile."

        menu:
            "Narrator" "{cps=5000}You notice that your mood has fallen flat, and you think Zephyr noticed too, since he stares at you with worry in his eyes. You quickly fix your posture and give a small smile.{/cps}"

            "\"Although it isn’t too bad here, a vacation is still a vacation!\"":
                show zephyr default open
            "\"I don’t mind being here, though. After all, I got to meet you and stay at your lovely farm.\"":
                show zephyr happy open


        z "\"I’m glad you are enjoying it here, then. Have you had a chance to explore the town a bit?\""

        show zephyr default closed
        mc "\"Not really, I was mainly rushing to find the inn. I didn’t get a chance to visit any shops or restaurants.\""

        show zephyr default open
        z "\"Well, I think you should take some time to enjoy the town before your flight is ready. Please be back before sunset, though.\""

        hide zephyr with dissolve


        "Narrator" "You nod in acknowledgement before finishing up your meal. After you are done eating, you head back to your room to get ready for the day."

        scene bg black with fade

        "Narrator" "You open your phone."
        mc "\"Wow, there are still no updates on the ship. It’s all the same information repeated over and over and over. Maybe I should listen to Zephyr and go out to explore the town.\""
        "Narrator" "You grab a small bag to take any necessary belongings with you before heading out to town."

        scene bg street day with fade
        play music "audio/General Day.wav"

        "Narrator" "You stroll at a leisurely pace throughout the streets."
        mc "\"The town looks so beautiful now that I am not rushing around. I can actually take in the scenery and visit the businesses here.\""
        "Narrator" "One building catches your eye by surprise. The sign reads “Prickly Pear Saloon.”" 
        mc "\"I don’t think I’ve seen a saloon in a while… or at all! I can’t believe they have one here.\"" 
        "Narrator" "You head towards the saloon and walk inside."

        stop music
        scene bg saloon with fade
        play music "audio/Saloon.wav"

        "Narrator" "You take in the interior of the saloon. The lighting is dim and cozy, and many people are seen chatting and drinking at various tables inside." 
        "Narrator" "Your gaze finds its way to the bar stand and onto a familiar figure. You chuckle to yourself before getting closer to the man that caught your eye for the second time on this planet." 
        mc "“Silas?”"

        show silas default closed with dissolve
        "Narrator" "He takes a sip of his drink before turning around to face you."

        menu:
            "Narrator" "{cps=5000}He takes a sip of his drink before turning around to face you.{/cps}"
            "“Hey Silas! What are you doing here?”":
                show silas default open
                s "\"Just here to cool down from the day. Why are you here?\""
                show silas default closed
                mc "\"Uhm, well, I was just looking around the town, and I just wanted to take a look at this saloon before I head back to my place of stay before sundown.\""

            "“Thanks Silas… I really appreciated your directions…”":
                show silas default open
                s "\"Oh? Well… you're welcome.\""

        show silas default open
        s "\"...{w=0.5}Did you not stay at the Wrangler Inn last night? I dind't see you there when I went back.\""
        show silas default closed
        mc "\"Uh, well I was able to find a very nice farm where I could stay for the night actually~ no thanks to you.\""
        show silas angry open
        s "\"Whatever. At least I am glad you found somewhere to stay.\""

        show silas sad closed
        s "\"Sorry, I did not mean to sound so rude... Do you want to have some fun? We can play darts.\""
        show silas happy open
        mc "\"Um, sure, I would love to play some games!\""

        hide silas with dissolve
        "Narrator" "You and Silas start playing darts for a bit.{w=0.5}.{w=0.5}.{w=0.5} Silas is letting the you win."

        show silas default open
        s "\"Holy cow, how are you so good at darts?\""
        show silas default closed
        mc "\"Back on Earth I played darts with my friends, and I would always beat them when they would say they were better than me.\""
        show silas default open
        s "\"Well, let’s finish up this game with the final dart in my hand, with my eyes closed.\""
        show silas flustered closed
        "Narrator" "You can't help but laugh at his mistake and Silas gets flustered from his horrible miss."
        "Narrator" "You go to pick up the dart that Silas had missed from his final shot and try to return it to him."

        show silas default open
        s "\"You can keep the dart as a trophy of your win in beating me at darts.\""
        show silas default closed
        mc "\"Well, thank you for this trophy, I will cherish this memory with it.\""
        show silas happy open
        s "\"Hey, now that we're done with darts, do you want to go and have some more fun in exploring the town\""
        "Narrator" "You get a warm feeling in your chest at the thought of exploring around town with Silas."
        mc "\"Yeah! I would love to do that!\""

        stop music

        scene bg street night with fade

        show silas happy closed
        "Narrator" "As you and Silas are exploring the town, he slowly warms up to you."

        show silas happy open
        s "\"That was really fun, I am glad that I was able to show you the town before you continue on your way.\""

        show silas happy closed
        mc "\"Me too! But, it is getting dark, and I need to head back to the farm before the sun fully goes down.\""

        show silas angry closed
        "Narrator" "Silas's expression shifts, becoming more serious at the mention of the farm."

        show silas default open
        s "\"Oh, who’s farm were you staying at last night?\""

        show silas default closed
        mc "\"I stayed at Zephyr’s farm not too far from here.\""

        show silas angry closed
        pause(1.0)
        show silas default closed
        "Narrator" "A flicker of concern crosses Silas's face, but he masks it quickly."

        show silas sad open
        s "\"...{w=0.5}do you want me to walk you to Zephyr’s farm before dark?\""

        show silas happy closed
        mc "\"Yeah, I would appreciate that! Let’s go!\""

        scene bg zephyrs kitchen night with fade

        show silas default closed at left
        "Narrator" "You and Silas sit down at the dinner table while Zephyr sets the table with plates and silverware for the three of y’all. Zephyr then places a wide array of appetizing dishes in the center of the table for y’all to eat."

        show zephyr default open at right with easeinleft
        z "\"Here is food that I have prepared for y’all. It is a lot of grub, so it may be a little good that Silas came to eat with us, dear. Well enough jawing from me, go on and dig in!\""

        show zephyr default closed at right
        mc "\"What is that you made for us to eat, Zephyr?\""

        show zephyr happy open at right
        z "\"Well, I struggled when trying to figure out ya taste, so I made a few different dishes. I made some good ol’ Cowboy Stew, cornbread, Shootin’ Star Casserole, Cowboy Candy, and some good ol’ greens.\""

        show zephyr angry closed at right
        "Narrator" "They begin eating in tense silence. Zephyr watches Silas carefully from across the table, his grip tight on his fork. The mounting tension isn’t so visible to you as you dig into your meal and enjoy every bite."

        mc "\"This is delicious, Zephyr! Thank you for making enough for all of us.\""

        show zephyr flustered open at right
        z "\"Course, darlin! Anything for you.\""

    

    label zephyr:
        "Narrator" "You tuck your phone back into your pocket before heading inside Zephyr’s home. You make your way towards the kitchen and find Zephyr cleaning up the last bits of the large dinner he prepared for y’all."
        mc "\"Hey, uhm… Zephyr?\""

        "Narrator" "His head whips around to face you and gives you a smile."
        z "\"Oh hey there, darlin’! I’m glad to see ya came back. Ya got enough time to clear your head out there?\""

        mc "\"Yes, I did, thank you for giving me my space.\""

        z "\"Of course, dear. I’m so sorry for earlier, I don’t know what got into me back there. I guess I just don’t trust people like that Silas… especially when it comes to you, [mcname]. But that doesn’t mean I should lose my temper in front of ya and I’m truly so-\""

        "Narrator" "You cut him off before he has a chance to apologize again."
        mc "\"Look, Zephyr, I really need to tell you something.\""

        "Narrator" "He looks at you with concern."
        z "\"Oh no, what is it, darlin’?\""

        mc "\"Don’t worry, it’s nothing bad. I just want to inform you that the ship I took is now functioning. The repairs went by quickly, so I can continue my trip to Caeles Terra by tomorrow afternoon! Isn’t that great?\""

        "Narrator" "You look at him with a smile and anticipation in your eyes as you wait for his answer."
        "Narrator" "Zephyr gives you a smile, but his eyes tell a different story."

        z "\"Well… I’m glad the ship is workin’ now, but I’m sure gonna miss ya! Does your trip really leave that early?\""

        mc "\"Yes, it does.\""
        "Narrator" "His smile falls at your confirmation."

        z "\"Do ya really want to leave so soon?\""
        mc "\"Well, I kinda have no choice, Zephyr. I’m not too sure about when I would be able to fly to Caeles Terra again, or if I can return to Earth on time if I stay here longer.\""
        z "\"Would it really kill ya to spend your vacation here instead? You did mention earlier that you spend too much time looking at a screen on Earth. Wouldn’t it be nice to unwind over here where there are less screens and gadgets?\""
        "Narrator" "Zephyr waits on your response."
        "Narrator" "You give some time to the thought of staying."

        mc "Sure, a beachy environment would be very refreshing… but this planet feels like home. It reminds me of what life was like before Earth’s society felt the need to devote their lives to screens." 
        mc "It might be nice to stay here and enjoy the tranquility on Rurigena Terra." 
        mc "It seems I’d be staying here with free shelter and food too, which is a huge plus since I know I’d be spending absurd amounts of money at Caeles Terra."
        "Narrator" "You nod before speaking to Zephyr."
        mc "\"You’re right. I haven’t really appreciated the slow life enough, I don’t think I’ve really been given the chance to wind down in a while anyway. I’ll stay, but I can probably only continue my trip for the rest of the week.\""

        "Narrator" "Zephyr gives a huge smile, reaching to hold your hands in his."

        z "\"Well, I’m mighty pleased! I’ll be sure to show ya more hidden gems on this planet, [mcname]. We could even go on a horse ride together and see the true beauty of nature here!\""

        "Narrator" "He smiles before pulling your hands to his lips and planting two soft kisses above your knuckles. He lets go of your hands gently before standing up."

        z "\"Now, you should go on to the guest room and catch some shut-eye, sweetheart. It’s gettin’ late, and I want you to be well rested for tomorrow mornin’!\""

        "Narrator" "You nod and smile before wishing Zephyr a good night. Your cheeks feel rosy as you make your way to the guest bedroom and settle down for the night. Tired from an eventful day, you fall into a deep sleep almost immediately after your head hits the pillow."

        # END DAY 2

        z "\"Mornin’ sweetheart!\""
        "Narrator" "Zephyr exclaims as he sets a plate of breakfast and a different juice on the table for you."

        mc "\"Good morning, Zephyr!\""

        "Narrator" "You say back to him as you sit down with him at the kitchen table. You both engage in conversation while eating, talking about how y’all slept last night to the plans for later in the day. Silence hits the table here and there as y’all take a break from talking to eat."
        "Narrator" "In those moments, you think about how safe you feel in the decision you made. You feel warm and fuzzy while appreciating the fact that Zephyr brings new experiences to you while still making you feel at home."
        "Narrator" "The meal ends, and Zephyr cleans up the kitchen while you drink your juice and stare out at the farm from the kitchen window. You take a moment to slow down and admire the planet you will stay on for the rest of your trip."

        #ENDING 1
        return

    label silas:
        scene bg street day with fade

        "Narrator" "You tuck your phone back in your pocket before making the decision to head back into town." 
        "Narrator" "As you make your way through the rows of quaint buildings, you see the hotel Silas mentioned previously." 
        "Narrator" "As you walk up to the lobby, you spot Silas sitting on a beat up sofa looking a bit dejected."
        mc "\"Silas?\""

        "Narrator" "Turning to look towards the source of the noise, his face lights up at the sight of you."

        s "\"[mcname]! You came. Did stepping out for a minute clear your head and show you the right choice? I was beginning to think that oaf had won your heart. I’m glad you made the decision to join me.\""

        "Narrator" "You roll your eyes at Silas’s comment, heading over to where he is sitting"

        mc "\"Well I wouldn't call him that, but I did come to the realization that I am meant to travel.\"" 
        mc "\"While staying here for a bit would have been nice as the air is the cleanest I’ve found so far in my travels, I couldn't imagine myself leaving my life behind for what this planet holds.\""

        "Narrator" "Standing to meet you, Silas takes your hand and begins leading you to where you assume his room is located."
        s "\"Well I’m glad you came to that decision on your own. While I would love to travel with you, I would never want to force you into something that you know you wouldn’t like.\""

        "Narrator" "After a brief minute of walking, you arrive at the entrance to one of the units. Number 203. As Silas unlocks the door and steps in, you can’t help but smile at him with a fond look on your face."
        "Narrator" "As you settle into the hotel unit, Silus makes an effort to ensure you are comfortable in his temporary space. With a warm smile on his face, he settles beside you."

        s "\"Alright kitten, get a restful night’s sleep and we’ll head out early tomorrow morning, so that we can ensure that we don’t miss our flight out of here.\""

        # DAY 3

        "Narrator" "As the sun rises over the horizon with warm hues of pink and green. You and Silas awake to the sound of hotel goers meandering about the walkways outside the units and towns-folk bustling about the dirt paved roads."

        "Narrator" "Though the both of you would like a slow morning walking up, enjoying each other's company, you know that is not an option." 
        "Narrator" "As you quickly gather your belongings and head out the door with Silas by your side, you can’t help but smile up at the bright sky."
        "Narrator" "Entering the spaceport, you see the newly repaired ship waiting at the dock, new side paneling gleaming in the light."
        "Narrator" "As you and Silas begin boarding the ship, he takes your hand in his, glancing over with a cheery smile on his face. As you look forward to the horizon, you can’t help but wonder what your future has in store."

        # ENDING 2
        return

    return

