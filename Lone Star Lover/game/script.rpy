# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.default_text_cps = 20 #0-100 is accepted
define gui.text_size = 30

define s = Character("Silus")
define z = Character("Zephyr")

default s_affection = 0
default z_affection = 0


# The game starts here.

label start:

    label day_1:
        scene bg airport day with fade 

        "MC" "Gate A11... Gate A11... Ah! I see it now. Finally, I can have some peace far, far away from my office of misery."
        "You let out a long yawn."
        "MC" "It sucks that I had to wake up early still... I guess vacations still have their ups and downs despite being a form of relaxation. At least the flight will be long enough to catch some sleep before I land on Caeles Terra."

        scene bg spaceship day with fade

        "You make your way into the ship, quickly finding an available seat. \nA few grunts are let out as you stuff your luggage into the storage next to your new place of slumber for the upcoming handful of hours." 
        "The seat feels cozy as you sink into it and lose a battle against your heavy eyelids."

        scene bg black with fade

        pause(3.0)
        
        scene bg spaceship day with hpunch
        
        "WHAM! Your eyes suddenly open as your body lunges forward before getting caught in a seatbelt. Your heartbeat pounds in your ears as you take in your surroundings and question what is happening around you."
        "MC" "Strange... I do not remember putting my seatbelt on... I do not even remember falling asleep! A flight attendant must have taken care of me shortly after I knocked out. Gosh, my torso hurts. Why did we land so harshly?"
        "Intercom" "\"APOLOGIES TO ALL GUESTS ON THE NEBULAE SPACELINES.\"\n\"DUE TO UNFORESEEN CIRCUMSTANCES, OUR PILOTS HAD TO MAKE AN EMERGENCY LANDING.\""
        "Intercom" "\"WE ASK ALL TRAVELERS TO CALMLY GATHER ANY CARRY-ON ITEMS THEY OWN AND TAKE THE CLOSEST EXIT. YOUR FLIGHT ATTENDANTS WILL THEN LEAD YOU TO THE SPACESHIP'S STORAGE UNIT, WHERE YOU WILL BE ALLOWED TO GRAB THE REST OF YOUR LUGGAGE.\""
        "Intercom" "\"WE URGE YOU ALL TO FIND ACCOMMODATIONS QUICKLY AS THIS FLIGHT'S STAFF DOES A ROUTINE MAINTENANCE AND REPAIR CHECK. THE ESTIMATED TIME OF COMPLETION WILL TAKE AROUND{w=0.5}.{w=0.5}.{w=0.5}.\"" 
        "Intercom" "\"THREE TO FIVE BUSINESS DAYS.\""
        "A collective groan and some exclaims emerge from people on board as you unbuckle your seatbelt and jump to your feet to collect all of your luggage."
        "Intercom" "\"OH, BEFORE I FORGET... \""
        "Intercom" "\"WELCOME TO RURIGENA TERRA!\""

        scene bg lugagge unit with fade

        "MC" "Oh my... I should've expected to run into a stressful situation while going on vacation. God forbid I try to relax!"
        "You continue pushing through luggage before pulling your suitcase out of the large pile."
        "MC" " I don't even know where I am or where I could stay!"
        "You clasp your hands over your face and take a deep breath in an attempt to calm down." 
        "Suddenly, you overhear a couple's discussion nearby."
        "Woman" "\"Wow... I don't think a flight has been derailed by this planet in a loooong time!\""
        "Man" "\"Yeah, I think about ten years ago. I guess it was due for another surprise. Say, what was the name of the hotel we stayed at the last time this happened?\""
        "Woman" "\"I think it was called {b}The Wrangler Inn{/b}.\""
        "Woman" "\"Once we find all of our luggage, then we can head out. We have to hurry, though. The rooms fill up quickly over there. Do you remember how to get to the hotel?\""
        "Man" "\"Sure, we have to head towards {b}Calico Lane{/b}, and then from there we turn left to {b}Blossom Street{/b} before finally turning to-\""
        "Woman" "\"Shhh! Lower your voice, other people might hear us! Just lead the way, there's no need to go over the directions right this second.\"" with hpunch
        "MC" "Does it really only take three streets to get to The Wrangler Inn? I do not know the last street, but maybe I can figure it out along the way. I should start leaving before anyone else does!"

        scene bg town day with fade

        "You take your luggage and quickly walk away from the ship, keeping the street names in your mind. You find {b}Calico Street{/b} and hurry down the road as you start to run out of breath from the long walk."
        "Soon enough, you spot a sign on your left labeled {b}\"Blossom St.\"{/b}"

        "MC" "\"Finally!\""
        "You take a few seconds to catch your breath before dashing down {b}Blossom Street{/b}, your eyes angled downwards to make sure you don't step in any holes or trip on any bumps in the ground."
        "You keep pushing before suddenly realizing that your body is no longer moving forward. Your face collides with a black, denim barrier before you slam against the ground."
        



    return
