# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.default_text_cps = 20 #0-100 is accepted
define gui.text_size = 30

define s = Character("Silas")
define z = Character("Zephyr")
define mc = Character("[mcname]")

default s_affection = 0
default z_affection = 0

image bg black = "#000000"
image bg generic space = "backrounds/bg_generic_space.png"
image bg inside ship = "backrounds/bg_inside_ship.png"
image bg space station = "backrounds/bg_space_station.png"
image zephyr house outside = "backrounds/bg_zypher_house_outside.png"

# The game starts here.

label start:

    label day_1:
        scene bg generic space with fade

        "{i}Gate A-11... Gate A-11... Ah! I see it now. Finally, I can have some peace far, far away from my office of misery.{/i}"
        "Narrator" "You let out a long yawn."
        "{i}It sucks that I had to wake up early still... I guess vacations still have their ups and downs despite being a form of relaxation. At least the flight will be long enough to catch some sleep before I land on Caeles Terra.{/i}"

        scene bg inside ship with fade

        "Narrator" "You make your way into the ship, quickly finding an available seat. \nA few grunts are let out as you stuff your luggage into the storage next to your new place of slumber for the upcoming handful of hours." 
        "Narrator" "The seat feels cozy as you sink into it and lose a battle against your heavy eyelids."

        scene bg black with fade

        pause(3.0)
        
        scene bg inside ship with hpunch
        
        "Narrator" "WHAM! Your eyes suddenly open as your body lunges forward before getting caught in a seatbelt. Your heartbeat pounds in your ears as you take in your surroundings and question what is happening around you."
        "{i}Strange... I do not remember putting my seatbelt on... I do not even remember falling asleep! A flight attendant must have taken care of me shortly after I knocked out. Gosh, my torso hurts. Why did we land so harshly?{/i}"
        "Intercom" "\"APOLOGIES TO ALL GUESTS ON THE NEBULAE SPACELINES.\"\n\"DUE TO UNFORESEEN CIRCUMSTANCES, OUR PILOTS HAD TO MAKE AN EMERGENCY LANDING.\""
        "Intercom" "\"WE ASK ALL TRAVELERS TO CALMLY GATHER ANY CARRY-ON ITEMS THEY OWN AND TAKE THE CLOSEST EXIT. YOUR FLIGHT ATTENDANTS WILL THEN LEAD YOU TO THE SPACESHIP'S STORAGE UNIT, WHERE YOU WILL BE ALLOWED TO GRAB THE REST OF YOUR LUGGAGE.\""
        "Intercom" "\"WE URGE YOU ALL TO FIND ACCOMMODATIONS QUICKLY AS THIS FLIGHT'S STAFF DOES A ROUTINE MAINTENANCE AND REPAIR CHECK. THE ESTIMATED TIME OF COMPLETION WILL TAKE AROUND{w=0.5}.{w=0.5}.{w=0.5}.\"" 
        "Intercom" "\"THREE TO FIVE BUSINESS DAYS.\""
        "Narrator" "A collective groan and some exclaims emerge from people on board as you unbuckle your seatbelt and jump to your feet to collect all of your luggage."
        "Intercom" "\"OH, BEFORE I FORGET... \""
        "Intercom" "\"WELCOME TO RURIGENA TERRA!\""

        scene bg space station with fade

        "{i}Oh my... I should've expected to run into a stressful situation while going on vacation. God forbid I try to relax!{/i}"
        "Narrator" "You continue pushing through luggage before pulling the suitcase with your name out of the large pile."
        $ mcname = renpy.input("\"What is your name?\"", length = 32)
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

        scene bg town day with fade

        "Narrator" "You take your luggage and quickly walk away from the ship, keeping the street names in your mind. You find {b}Calico Street{/b} and hurry down the road as you start to run out of breath from the long walk."
        "Narrator" "Soon enough, you spot a sign on your left labeled {b}\"Blossom St.\"{/b}"

        mc "\"Finally!\""
        "Narrator" "You take a few seconds to catch your breath before dashing down {b}Blossom Street{/b}, your eyes angled downwards to make sure you don't step in any holes or trip on any bumps in the ground."
        "Narrator" "You keep pushing before suddenly realizing that your body is no longer moving forward. Your face collides with a black, denim barrier before you slam against the ground."
        mc "\"What in the world?\""
        
        show silas angry closed with dissolve
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
            "Huh? But I was looking where I was going...":
                pass
            "...Can you at least help me figure out where to go from here?":
                $ s_affection += 1
        
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
        hide silas default closed with easeoutleft
        "{i}What a strange encounter... That Silas... He seemed angry with me, yet caring at the same time?{/i}"
        "{i}This road seems awfully lonely. I sure hope he gave me the correct directions! Maybe the inn is just in an isolated area?... I really hope that is the case.{/i}"

        scene zephyr house outside with fade
        "Narrator" "After walking a bit further, you see the end of the road without an inn accompanying it. You look around in a slight panic and only find the entrance to a farm up ahead."
        mc "Are you serious!? He really gave me the wrong directions? Is this some sort of prank, or does he really not know the way around his town!?"
        mc "I have been walking for so long… By the time I walk back into town, the sun will set, and I will practically be stranded in the streets!"
        "Narrator" "You take a moment to collect your thoughts after expressing your worries about your current situation."
        mc "Well, someone has to be taking care of that farm… right? I really hope the farm owner is home or I will be doomed for tonight."
        "Narrator" "You take your luggage and push open the gate to the farm. Herds of cattle and plentiful crops are seen on either side of you as you get closer and closer towards the door of the farmhouse."
        "Narrator" "You place three knocks on the door and wait for a few seconds before the door swings open. A puzzled man makes eye contact with you before greeting you with a smile."
        
        show zephyr default open with dissolve
        
        "???" "\"Howdy! My name is Zephyr. You don’t seem to be from ‘round these parts. What can I call you, dear?\""

        show zephyr default closed

        menu:
            "Uhm … Hello? My name is [mcname].":
                pass
            "Oh, howdy! My name is [mcname]!":
                pass

        show zephyr default open

        z "\"Well, [mcname], what brings you to town? Why did you come knocking on my door?\""

        show zephyr happy closed

        "Narrator" "The man leans against his door frame, giving a kind smile."

        mc "\"I was on my way to Caeles Terra for vacation before my ship crashed here.\""
        mc "\"I have nowhere to go, really, but I overheard a couple talking about a place called The Wrangler Inn.\""


    return
