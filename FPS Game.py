

print("\n\t ❤️‍🩹 Mission: Undead Siege!🧊\n")

ask = input("Would you like to start?👺->>> ").upper()
if "Y" in ask:
    pass
else:
    exit()

print("Welcome To The Gulag!💀")
print("If You Survive, You Earn Your Freedom!🕊️")

name = input("Your Name ->>> ").title()
age = int(input("Your Age ->>> " ))

health = 20

def game():

    print("Be Careful... You're Teleported To A Haunted Place...")
    print("You'll Have Some Course of Action To Proceed With!")
    print("Wisely Choose Your Decisions & Avoid Getting Killed!")
    teleport = input("You Are Now Inside Gulag!👺 \nHere's Your First Choice: (Left\Right)->>> ").upper()
    if "R" in teleport:
        print("Well Done! You Are Now At The Control Room!🛎️")
        
        gun = input("You Have Full Acess To Any Gun You Want!💥\nType Your Gun Selection! ->>> ").upper()
        print(f"Good Job! Use Your Fav {gun} Wisely To Slay Down Enemies!☠️\nDon't Do Anything Stupid!⛔ Stay Alert!⚠️")

        uav = input("You Have Two Types of UAV To Choose Between!🗺️\nNormal UAV ->>> Shows Enemy Location on The Map!✅\nCounter UAV ->>> Hides Your Location on Enemy Map!⛔\nYour Choice ->>> ").upper()

        if "C" in uav:
            print("Ah SH#T! The Enemy Has Spotted The UAV!🥶\nDon't Be Scared! They Can't Know Your Location!😎\nRun Away From Here As Fast As You Can!🏃‍♂️💨")
            
            run_choose = input("You Are Now Out of Gulag!🥶\nBecareful This Place is Haunted!☠️\nWould you like to Head towards East or West?🧭\nYour Choice ->>> ").upper()

            if "W" not in run_choose:

                landmines = input("Oh No!😧You Entered A Place With Full of Land Mines!💣\nWould You Like To Hide Here or Risk Your Life?☠️\nYour Choice --> ").upper()

                if "H" in landmines:
                    print("Well, You Tried To Hide But The Enemies Killed You...😵")
                
                else:
                    ziz = input("Be Careful This is Full of Danger!⛔\nWould you like to go straight into the Land Mines Area or walk away in a ZigZag pattern?\n Your Choice ->>> ").upper()

                    if "Z" in ziz:
                        print("Thank God!🕊️ You Got Lucky & Passed The Mine Path!💪\nBut you got your knee fractured while jumping around and lost 5 Health!⛔")
                    
                        runorheal = input("The Enemies Might Still Be Chasing You!😧\n And Your Radar is now Visible!👀\nThey Might Be Tracking You!\nWould you like to go North towards the Ocean🌊 or hide in a Warehouse at South!🗺️(North/South)\nYour Choice ->>> ").upper()

                        if runorheal == "NORTH":
                            print("Well, you ran too close to the ocean and the tsunami got you dead ☠️")
                        
                        else:
                            sneak = input(f"You Are Now Hiding On A Warehouse But Unfortunately It's the Enemey's Base!🥶\nWould you like to Kill them with your {gun} or sneak away from here?🏃‍♂️💨 (Kill/Sneak)\nYour Choice ->>> ").upper()

                            if sneak == "KILL":
                                ammo = ("Well Done! You Killed 3 of Your Enemies!😈\nYou Lost 5 Health🔰 & You Are Out Of Ammo!⛔ Would you like to fight them with your barehands?\nYour Choice ->>> ").upper()
                                
                                if "Y" in ammo:
                                    jump = input("That's Great!👀 You Managed To Kill All of the Enemies!✅\nBut The Main Boss is still somewhere in this Warehouse!😧\nOh No! He Has Shot A Bulled Towards You!🥶\nYou Have To Dodge The Bullet! You Got Only One Chance! Jump Towards Left or Right\n Your Choice ->>> ").upper()

                                    if jump == "LEFT":

                                        point = input("Congrats!🥳 You Jumped To The Left & Got A Gun!🚀\nYou Are Now Pointing It To His Face!😟\nType [shoot] to Shoot The Head of that BITCH!😈\n ->>> ").upper()

                                        if point == "SHOOT":

                                            print("Mission Accomplished Good Work!🎉🎊")
                                else:
                                    print("Not Fighting Was A Really Bad Choice!😟\nThey Showed No Mercy on You!\nThey Tied You Up And Burried You Alive!☠️")
                            
                            else:
                                print("You Tried To Sneak Out But They Saw And Shot You!☠️")

                    else:
                        print("Oops! You Stepped On A Mine & Your Body Exploded...😵")
            
            else:
                print("You Ran Towards West! But Got Killed in a Truck Accident!☠️🚒🚛")



        else:
            print("Holy Jeez! The Enemy Has Traced Your Location!🥶\nWould You Like To Run or Fight With The Enemies?")
            run_fight = input("Your Choice ->>> ").upper()
            
            if "F" in run_fight:
                print("Well, You Fought With The Enemies But They Were Too Strong!💪\n You Got Killed...")
            
            else: 
                print("Well, You Tried To Run But The Enemies Shot You On Your Legs!🦵\nYou Lost 10 Health!⛔\nDon't Worry! You Still Have 10 Health Left!🔰")

                run_heal = input("Oh No! The Enemies Might Still Be Chasing You!🥶\nYou're Bleeding Badly! Would You Like To Hide & Heal 💘 or Run?🏃‍♂️💨\nYour Choice ->>> ").upper()
                 
                if "R" in run_heal:
                    print("Your Tried To Run But Died From Over-Bleeding... 🩸")

                else:
                    print("The Enemies Didn't Spot You!⛔\nBut You Got Bitten By A Snake!🐍\nYou Have 5 Health Left! There is a Hospital Nearby!🏥\nWould you like to Treat Yourself🔰 or Keep on Hiding Here?🥶")

                    aid_hide = input("Your Choice ->>> ").upper()

                    if "H" in aid_hide:
                        print("The Vemon of Snake Was Really Poisonous!🤢\nYou Died...😵")
                    
                    else: 
                        print(f"The Hospital Was Attacked By Your Enemies!🥶\nYou Tried To Kill Them With Your {gun}!🗡️\nBut They Were Too Powerful.💪 You Were Killed...🪦")


    else:
        print("Oops!😵 You Got Shot By A Pyscho Killer...")
        print(f"Your Health ->>> 0")
    

if age >= 18:
    print(f"Captain {name.split().pop(0)}, You're Ready To Slayy!😎")
    game()
elif age >=13:
    print(f"Aw OH! {name.split().pop(0)}, You're Quite Young!\nPlease, Play With Supervision!🥶")
    game()
else:
    print(f"{name.split().pop(0)}, Sorry You Are Too Young To Slay!👶🍼")



    
