# -*- coding: utf-8 -*-
import os, random
#Settings
dev=False
unlock_all_achievements=False
repeat_chapters=False
normal_clear=False
repeat_amount=25
chars_in_line=55
run_off=True
error_message=True
#Story Vars
begin=True
story_part1=False
story_part2=False
story_part3=False
story_part4=False
story_part5=False
story_part6=False
story_part7=False
story_part8=False
#Save file
#Save file extension (gsf) = Game Save File
path='\\Users\\brobi\\Desktop'
os.chdir(path)
version = '0.2.5'
def updates():
    print 'Current Version 0.2.5:'
    print '1. Added Machete and Pickaxe to sell.'
    print '2. Added Machete and Pickaxe to buy.'
    print '3. Edited the look of the loading page.'
    print '4. Added more enemy names.'
    print '5. Added gems in to the game.'
    print '6. Added a function called gems so user can see what gems they currently have.'
    print '7. Added loot crates for chapters.'
    print '8. You now start with 10.00$ instead of 3.76$'
    print '9. Organized Variables in code.'
    print '10. Collisseum is now implemented into the game. Cannot be accessed without dev mode yet.'
    print '11. You now start with 3 pickaxes instead of 1.'
    print '12. You now start with 2 machetes instead of 1.'
    print '13. Added a load funcion. Cannot be accessed without dev mode yet.'
    print '14. Added a experimental save function. Cannot be accessed without dev mode yet.'
    print '15. Added gems into the shop as a form of trading currency.'
    print '16. Added a new chapter.'
    print
    print 'Future updates:'
    print '1. Exploring will drain your battery over time.'
    print '2. Adding a new setting to stop letters from going off the screen.'
    print '3. Add a battle arena where no exploring is needed just fighting.'
    print '4. Add a form of currency for the shop, Or use trading.'
    print '5. Show all items in bag. Some items are missing.'
    print '6. Add a save function. EST: Version 0.3.0'
    skip = raw_input('Hit enter to exit:')
def next_update():
    print 'Things to do for update Version 0.2.5:'
    print '1. Think a gem trades. And maybe add them in. Not a big priority.'
    print '2. Talk about how the the collisseum will work. Will be accesed only through dev mode.'
    print '3. Give each enemys name a descrptive idea of who or what they are.'
    print '4. Start developement of save function. Will not be available to use until Version 0.3.0.'
    print ''
    print 'Optional Stuff:'
    print '1. Check for any spelling errors or mistakes.'
    print '2. Adjust timing for text to display on screen so user has time to read it.'
    print '3. Fancy up how menus look to the end user.'
    print '4. Add new items so they show in the bag when user opens it.'
    print '5. Come up with ideas for weapons in the game.'
    print '6. Test the shop for bugs. Mainly test buy and sell functions.'
    print '7. Make a list of new features to add in the game.'
    print '8. Test the attack function for any bugs. Little to no testing was done previously.'
    print '9. Add a setting to allow users to load a save file from a different version.'
def edit_chapters():
    global story_part1,story_part2,story_part3,story_part4,story_part5,story_part6,story_part7,story_part8
    print 'True = Unlocked'
    print 'False = Locked'
    print '(1)Begin:',str(begin)
    print '(2)Chapter 1:',str(story_part1)
    print '(3)Chapter 2:',str(story_part2)
    print '(4)Chapter 3:',str(story_part3)
    print '(5)Chapter 4:',str(story_part4)
    print '(6)Chapter 5:',str(story_part5)
    print '(7)Chapter 6:',str(story_part6)
    print '(8)Chapter 7:',str(story_part7)
    print '(9)Chapter 8:',str(story_part8)
    choice=raw_input('What number: ')
    if choice == "1":
        hi=True
        if begin==True:
            begin=False
            hi=False
        if begin==False:
            if hi==True:
                begin=True
    if choice == "2":
        hi=True
        if story_part1==True:
            story_part1=False
            hi=False
        if story_part1==False:
            if hi==True:
                story_part1=True
    if choice == "3":
        hi=True
        if story_part2==True:
            story_part2=False
            hi=False
        if story_part2==False:
            if hi==True:
                story_part2=True
    if choice == "4":
        hi=True
        if story_part3==True:
            story_part3=False
            hi=False
        if story_part3==False:
            if hi==True:
                story_part3=True
    if choice == "5":
        hi=True
        if story_part4==True:
            story_part4=False
            hi=False
        if story_part4==False:
            if hi==True:
                story_part4=True
    if choice == "6":
        hi=True
        if story_part5==True:
            story_part5=False
            hi=False
        if story_part5==False:
            if hi==True:
                story_part5=True
    if choice == "7":
        hi=True
        if story_part6==True:
            story_part6=False
            hi=False
        if story_part6==False:
            if hi==True:
                story_part6=True
    if choice == "8":
        hi=True
        if story_part7==True:
            story_part7=False
            hi=False
        if story_part7==False:
            if hi==True:
                story_part7=True
    if choice == "9":
        hi=True
        if story_part8==True:
            story_part8=False
            hi=False
        if story_part8==False:
            if hi==True:
                story_part8=True
def settings():
    for i in range(5):
        print
    global normal_clear, run_off, error_message, repeat_amount,chars_in_line
    if normal_clear==True:
        print '(1)Normal Screen Clean: Clear'
    if normal_clear==False:
        print '(1)Normal Screen Clean: Print Repeat'
    if run_off==True:
        print '(2)Screen Run Off Value:',chars_in_line,', Enabled'
    if run_off==False:
        print '(2)Screen Run Off Value:',chars_in_line,', Disabled'
    if error_message==True:
        print '(3)Error Messages: Enabled'
    if error_message==False:
        print '(3)Error Messages: Disabled'
    print '(4)Change File Path'
    print '\nCurrent Save File Path:'
    print '    Directory:',path
    print 'Print Repeat Info:'
    print '   Current Value:',repeat_amount
    print '(5)Change Print Repeat Value'
    check = raw_input('Choose a setting to change:')
    if check == "1":
        hi=True
        if normal_clear==True:
            normal_clear=False
            hi=False
        if normal_clear==False:
            if hi==True:
                normal_clear=True
    if check == "2":
        print '(1)Change Value\n(2)Enable/Disable'
        choice = raw_input("Choose one:")
        if choice == "1":
            try:
                chars_in_line=int(raw_input('What is the new value:'))
            except ValueError:
                if error_message==True:
                    print 'System message: ValueError'
                    print 'Reason: A number was not entered.'
                    print 'Please wait 2.5 seconds.'
                    choice=raw_input('Hit enter to continue:')
            choice=''
        if choice == "2":
            hi=True
            if run_off==True:
                run_off=False
                hi=False
            if hi==True:
                if run_off==False:
                    run_off=True
    if check == "3":
        hi=True
        if error_message==True:
            error_message=False
            hi=False
        if error_message==False:
            if hi==True:
                error_message=True
    if check == "4":
        print 'Enter your desired directory:'
        try:
            os.chdir(raw_input('Directory: '))
        except WindowsError:
            windows_error()
        print os.getcwd()
    if check == "5":
        try:
            repeat_amount=int(raw_input('What is the new value:'))
        except ValueError:
            if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                print 'Please wait 2.5 seconds.'
                skip=raw_input('Hit enter to continue:')
                skip=''
def screen_run(line_space):
    global run_off,chars_in_line
    if run_off==True:
        p=len(line_space)
        round(p)
        a=int(0)
        b=int(chars_in_line)
    while p>0:
        try:
            #print avalable
            if line_space[a]==" ":
                bg=line_space[a+1:b]
            if line_space[a] is not " ":
                bg=line_space[a:b]
            #print
            print (bg)
            a+=chars_in_line
            b+=chars_in_line
            p-=1
        except IndexError:
            break
def clear():
    global normal_clear,repeat_amount
    if normal_clear==True:
        os.system('clear')
    if normal_clear==False:
        for i in range(repeat_amount):
            print ''
if dev==True:
    print '(1)Quick Settings'
    print '(2)Version Info'
    print '(3)Update Info'
    print '(4)Edit chapters'
    help=raw_input('Choose an option or hit enter: ')
    if help == "1":
        settings()
    if help == "2":
        print (version)
    if help == "3":
        updates()
    if help == "4":
        edit_chapters()
clear()
password='123456'
if password=="123456":
    #Others
    battery_charger=False
    flashlight=False
    enemy=['Goblin','Karen','Bat','Skeleton','Zombie','Flip Phone','Youra the explora','No Cell Service','My Brother']
    current_enemy=''
    working_battery_charger=False
    skip=False
    one_time=False
    start=False
    attack=False #When true, user is under attack.
    health=0 #If 0, then no monster is present.
    victory_status=False
    total_wins=0
    seen_notes=0
    money=10.00 #Dollars
    charge_price=0.90 #Price to charge battery in shop
    charge_time=1.2 #Seconds
    custom_attack=False #Set to true to set attacks in collisseum mode and change vars (health, current_enemy) to your desired traits. Must do before game starts.
    #Items
    pickaxe=3
    machete=2
    sticks=2
    coal=2
    computer_chips=0
    wires=0
    good_batteries=5
    bad_batteries=2
    battery=5
    throwing_rocks=12
    spears=5
    torches=25
    #Weapon Damage
    throwing_rocks_damage=[7,15]
    spears_damage=[11,17]
    pickaxe_damage=[15,19]
    machete_damage=[17,23]
    #Item Usage
    flashlight_use=False #When true, user is using the item.
    throwing_rocks_use=False #When true, user is using the item.
    pickaxe_use=False #When true, user is using the item.
    machete_use=False #When true, user is using the item.
    spears_use=False #When true, user is using the item.
    torch_use=False #When true, user is using the item.
    no_light=False
    if dev==False:
        menu_open=False
        bag_open=False
    if dev==True:
        menu_open=True
        bag_open=True
    #Gems
    red_gem=0
    green_gem=0
    magenta_gem=0
    yellow_gem=0
    blue_gem=0
    #Buy
    coal_buy=2.10
    computer_chips_buy=8.40
    wires_buy=3.90
    good_batteries_buy=4.75
    bad_batteries_buy=3.00
    sticks_buy=1.25
    throwing_rocks_buy=1.25
    spears_buy=1.75
    torches_buy=0.70
    pickaxe_buy=2.10
    machete_buy=2.45
    #Sell
    coal_sell=1.50
    computer_chips_sell=5.00
    wires_sell=2.40
    good_batteries_sell=3.50
    bad_batteries_sell=2.15
    sticks_sell=1.00
    throwing_rocks_sell=1.25
    spears_sell=1.75
    torches_sell=0.70
    pickaxe_sell=2.10
    machete_sell=2.45
    #Achievements
    if unlock_all_achievements==False:
        let_the_battles_begin=False
        guts_and_glory=False
        i_have_the_power=False
        its_payday=False
        whicked_chronicle=False
    if unlock_all_achievements==True:
        let_the_battles_begin=True
        guts_and_glory=True
        i_have_the_power=True
        its_payday=True
        whicked_chronicle=True
    def collisseum():
        global custom_attack, current_enemy, health
        custom_attack=True
        try:
            health=int(raw_input('What is the enemys health: '))
        except ValueError:
            value_error()
        current_enemy=raw_input('What is the enemys name: ')
        clear()
        start_attack()
        custom_attack=False
        move_on=raw_input('Hit enter to exit: ')
    def loot_crate(number):
        global sticks, throwing_rocks, torches, spears, good_batteries, bad_batteries, pickaxe, machete
        if number == 1:
            print 'You got 4 sticks and 1 throwing rock.'
            sticks+=4
            throwing_rocks+=1
        if number == 2:
            print 'You got 2 torches.'
            torches+=2
        if number == 3:
            print 'You got 1 spear and 2 throwing rocks.'
            spear+=1
            throwing_rocks+=2
        if number == 4:
            print 'You got 2 good batteries and 2 bad batteries.'
            good_batteries+=2
            bad_batteries+=2
        if number == 5:
            print 'You got 1 pickaxe.'
            pickaxe+=1
        if number == 6:
            print 'You got 1 machete and 2 throwing rocks.'
            machete+=1
            throwing_rocks+=2
    def gem_collection():
        global red_gem, green_gem, magenta_gem, yellow_gem, blue_gem
        print 'Red:',red_gem
        print 'Green:',green_gem
        print 'Magenta:',magenta_gem
        print 'Yellow:',yellow_gem
        print 'Blue:',blue_gem
        move_on=raw_input('Hit enter to exit: ')
        clear()
    def achieve():
        global let_the_battles_begin, guts_and_glory, i_have_the_power, its_payday, whicked_chronicle
        print '(1)Check for pending achievements'
        print '(2)See your earned achievements'
        choice = raw_input('1 or 2: ')
        if choice == "1":
            print 'Checking for awards...'
            if total_wins>0:
                let_the_battle_beggin=True
            if money>19.99:
                its_payday=True
            if seen_notes>0:
                whicked_chronicle=True
        if choice == "2":
            clear()
            if let_the_battles_begin==True:
                print 'Let The Battles Begin: Win your first battle'
            if let_the_battles_begin==False:
                print '???: Win your first battle'
            print ''
            if guts_and_glory==True:
                print 'Guts and Glory: Unlock the Collisseum'
            if guts_and_glory==False:
                print '???: Unlock the Collisseum'
            print ''
            if i_have_the_power==True:
                print 'I Have The Power: Charge a battery'
            if i_have_the_power==False:
                print '???: Charge a battery.'
            print ''
            if its_payday==True:
                print "It's Payday Fellas!: Gain a total of 20$"
            if its_payday==False:
                print '???: Gain a total of 20$'
            print ''
            if whicked_chronicle==True:
                print 'Wicked Chronicle: Discover a note in the caves'
            if whicked_chronicle==False:
                print '???: Discover a note in the caves'
            print ''
        move_on=raw_input('Hit enter to exit: ')
        clear()
    def notes(number):
        global seen_notes
        seen_notes+=1
        if number==1:
            print "It's been three weeks since i've seen the day of light. I'm starting to loose my grip on reality. Food and water are hard to come by. I don't know how much longer I will survive. I'm sorry for what I did... Please Spare me!"
        if numebr==2:
            print "Day 22: I often find myself wondering about what has become of my family while I've been gone. This damned journey was a fools errand from the start."
        if number==3:
            print "Day 24: I found a strange environment today, a whole are of this cave covered head to toe in moss. Not super interesting, but definitley unusual."
        if numebr==4:
            print "Day 25: A small creature scurried past my feet today, seemingly able to speak, as i heard it say something about donuts as it hurried in the opposite direction of me. I tried to get it's attention, but it seemed to be unable to ear me, or simply ignoring me."
        if number==5:
            print "Day 26: Today might have been the worst day yet. This shambling monstrosity attaced me, and i was forced to fight it off with my bare hands. Futre reference, find rocks or somthing of the sort to throw at creatures in the future."
    def trade():
        global good_batteries, battery_charger, spears, throwing_rocks
        print 'Your trading options:'
        print '(1) 1 battery charger = 5 good batteries'
        print '(2) 4 throwing rocks = 1 spear'
        choice = raw_input('What are your trading: ')
        if choice == "1":
            if good_batteries<5:
                print 'You don\'t have enough charged batteries'
            if good_batteries>4:
                print 'You got 1 battery charger.'
                battery_charger=True
                good_batteries-=5
        if choice == "2":
            if spears<1:
                print 'You don\'t have enough spear(s)'
            if spears>0:
                print 'You got 4 throwing rocks.'
                throwing_rocks+=4
                spears-=1
    def non_function():
        clear()
        print 'This function has not yet been implemented. Sorry for the inconvience.'
        print 'If this is an error please contact me via github. Thank You!'
        move_on=raw_input('Hit enter to exit: ')
    def windows_error(topic):
        print "The system cannot find the file specified:",topic
        print 'Note: If you are not a developer please ignore this.'
    def value_error():
        global error_message
        if error_message==True:
            print 'System: ValueError. An incorrect input has been given.'
    def shop():
        global red_gem, green_gem, magenta_gem, yellow_gem, blue_gem, pickaxe_sell, machete_sell, pickaxe, machete, i_have_the_power, battery_charger, coal_sell, wires_sell, sticks_sell, spears_sell, torches_sell, computer_chips_sell, good_batteries_sell, bad_batteries_sell, throwing_rocks_sell, money, coal, wires, sticks, spears, torches, good_batteries, bad_batteries, computer_chips, throwing_rocks
        print 'Welcome to My shop.'
        print '\n(1)Sell\n(2)Trade\n(3)Buy\n(4)Charge Battery\n(5)Gems\n(6)Leave'
        choice = raw_input('What are you looking to do: ')
        if choice == "1":
            clear()
            print 'System: Price is per item. Not for the total.'
            print 'Item:             Price:'
            print '(1)Coal:          ',coal_sell
            print '(2)Wires:         ',wires_sell
            print '(3)Sticks:        ',sticks_sell
            print '(4)Spears:        ',spears_sell
            print '(5)Torches:       ',torches_sell
            print '(6)Computer Chips:',computer_chips_sell
            print '(7)Good Batteries:',good_batteries_sell
            print '(8)Bad Batteries: ',bad_batteries_sell
            print '(9)Throwing Rocks:',throwing_rocks_sell
            print '(10)Pickaxes:     ',pickaxe_sell
            print '(11)Machete:      ',machete_sell
            print '\nYour Balance:',money,'Dollar(s)'
            choice = raw_input('What would you like to sell: ')
            if choice == "1":
                if coal<1:
                    print 'You don\'t have any to sell.'
                if coal>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>coal:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<coal+1:
                            print '\nYour Reciept:'
                            print '  Coal Before Trans:',coal
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*coal_sell
                            coal-=choice
                            print '  Coal After Trans',coal
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(coal_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "2":
                if wires<1:
                    print 'You don\'t have any to sell.'
                if wires>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>wires:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<wires+1:
                            print '\nYour Reciept:'
                            print '  Wires Before Trans:',wires
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*wires_sell
                            wires-=choice
                            print '  Wires After Trans',wires
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(wires_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "3":
                if sticks<1:
                    print 'You don\'t have any to sell.'
                if sticks>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>sticks:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<sticks+1:
                            print '\nYour Reciept:'
                            print '  Sticks Before Trans:',sticks
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*sticks_sell
                            sticks-=choice
                            print '  Sticks After Trans',sticks
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(sticks_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "4":
                if spears<1:
                    print 'You don\'t have any to sell.'
                if spears>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>spears:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<spears+1:
                            print '\nYour Reciept:'
                            print '  Spears Before Trans:',spears
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*spears_sell
                            spears-=choice
                            print '  Spears After Trans',spears
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(spears_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "5":
                if torches<1:
                    print 'You don\'t have any to sell.'
                if torches>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>torches:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<torches+1:
                            print '\nYour Reciept:'
                            print '  Torches Before Trans:',torches
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*torches_sell
                            torches-=choice
                            print '  Torches After Trans',torches
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(torches_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "6":
                if computer_chips<1:
                    print 'You don\'t have any to sell.'
                if computer_chips>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>computer_chips:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<computer_chips+1:
                            print '\nYour Reciept:'
                            print '  Computer Chips Before Trans:',computer_chips
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*computer_chips_sell
                            computer_chips-=choice
                            print '  Computer Chips After Trans',computer_chips
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(computer_chips_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "7":
                if good_batteries<1:
                    print 'You don\'t have any to sell.'
                if good_batteries>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>good_batteries:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<good_batteries+1:
                            print '\nYour Reciept:'
                            print '  Good Batteries Before Trans:',good_batteries
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*good_batteries_sell
                            good_batteries-=choice
                            print '  Good Batteries After Trans',good_batteries
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(good_batteries_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "8":
                if bad_batteries<1:
                    print 'You don\'t have any to sell.'
                if bad_batteries>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>bad_batteries:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<bad_batteries+1:
                            print '\nYour Reciept:'
                            print '  Bad Batteries Before Trans:',bad_batteries
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*bad_batteries_sell
                            bad_batteries-=choice
                            print '  Bad Batteries After Trans',bad_batteries
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(bad_batteries_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "9":
                if throwing_rocks<1:
                    print 'You don\'t have any to sell.'
                if throwing_rocks>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>throwing_rocks:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<throwing_rocks+1:
                            print '\nYour Reciept:'
                            print '  Throwing Rocks Before Trans:',throwing_rocks
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*throwing_rocks_sell
                            throwing_rocks-=choice
                            print '  Throwing Rocks After Trans',throwing_rocks
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(throwing_rocks_sell)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "10":
                if pickaxe<1:
                    print 'You don\'t have any to sell.'
                if pickaxe>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>pickaxe:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<pickaxe+1:
                            print '\nYour Reciept:'
                            print '  pickaxes Before Trans:',pickaxe
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*pickaxe_sell
                            pickaxe-=choice
                            print '  Pickaxes After Trans',pickaxe
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(pickaxe)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "11":
                if machete<1:
                    print 'You don\'t have any to sell.'
                if machete>0:
                    try:
                        choice = int(raw_input('How many should I sell: '))
                        if choice>machete:
                            print 'I\'m sorry, but you don\'t have that many.'
                        if choice<machete+1:
                            print '\nYour Reciept:'
                            print '  pickaxes Before Trans:',machete
                            print '  Money Before Trans:',str(money)+'$'
                            money+=float(choice)*machete_sell
                            machete-=choice
                            print '  Pickaxes After Trans',machete
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(machete)+'$'
                            print '  Amount Sold:',choice
                    except ValueError:
                        value_error()
                choice =''
            move_on=raw_input('Hit enter to exit:')
        if choice == "3":
            clear()
            print 'System: Price is per item. Not for the total.'
            print 'Item:             Price:'
            print '(1)Coal:          ',coal_buy
            print '(2)Wires:         ',wires_buy
            print '(3)Sticks:        ',sticks_buy
            print '(4)Spears:        ',spears_buy
            print '(5)Torches:       ',torches_buy
            print '(6)Computer Chips:',computer_chips_buy
            print '(7)Good Batteries:',good_batteries_buy
            print '(8)Bad Batteries: ',bad_batteries_buy
            print '(9)Throwing Rocks:',throwing_rocks_buy
            print '(10)Pickaxes:     ',pickaxe_buy
            print '(11)Machete:      ',machete_buy
            print '\nYour Balance:',money,'Dollar(s)'
            choice = raw_input('What would you like to buy: ')
            if choice == "1":
                if money<coal_buy:
                    print 'You don\'t have enough money.'
                if money>coal_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<coal_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>coal_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Coal Before Trans:',coal
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*coal_buy
                            coal+=choice
                            print '  Coal After Trans',coal
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(coal_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "2":
                if money<wires_buy:
                    print 'You don\'t have enough money.'
                if money>wires_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<wires_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>wires_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Wires Before Trans:',wires
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*wires_buy
                            wires+=choice
                            print '  Wires After Trans',wires
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(wires_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "3":
                if money<sticks_buy:
                    print 'You don\'t have enough money.'
                if money>sticks_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<sticks_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>sticks_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Sticks Before Trans:',sticks
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*sticks_buy
                            sticks+=choice
                            print '  Sticks After Trans',sticks
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(sticks_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "4":
                if money<spears_buy:
                    print 'You don\'t have enough money.'
                if money>spears_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<spears_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>spears_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Spears Before Trans:',spears
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*spears_buy
                            spears+=choice
                            print '  Spears After Trans',spears
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(spears_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "5":
                if money<torches_buy:
                    print 'You don\'t have enough money.'
                if money>coaltorches_buy_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<torches_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>torches_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Torches Before Trans:',torches
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*torches_buy
                            torches+=choice
                            print '  Torches After Trans',torches
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(torches_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "6":
                if money<computer_chips_buy:
                    print 'You don\'t have enough money.'
                if money>computer_chips_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<computer_chips_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>computer_chips_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Computer Chips Before Trans:',computer_chips
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*computer_chips_buy
                            computer_chips+=choice
                            print '  Computer Chips After Trans',computer_chips
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(computer_chips_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "7":
                if money<good_batteries_buy:
                    print 'You don\'t have enough money.'
                if money>good_batteries_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<good_batteries_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>good_batteries_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Good Batteries Before Trans:',good_batteries
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*good_batteries_buy
                            good_batteries+=choice
                            print '  Good Batteries After Trans',good_batteries
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(good_batteries_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "8":
                if money<bad_batteries_buy:
                    print 'You don\'t have enough money.'
                if money>bad_batteries_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<bad_batteries_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>bad_batteries_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Bad Batteries Before Trans:',bad_batteries
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*bad_batteries_buy
                            bad_batteries+=choice
                            print '  Bad Batteries After Trans',bad_batteries
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(bad_batteries_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "9":
                if money<throwing_rocks_buy:
                    print 'You don\'t have enough money.'
                if money>throwing_rocks_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<throwing_rocks_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>throwing_rocks_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Throwing Rocks Before Trans:',throwing_rocks
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*throwing_rocks_buy
                            throwing_rocks+=choice
                            print '  BThrowing Rocks After Trans',throwing_rocks
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(throwing_rocks_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "10":
                if money<pickaxe_buy:
                    print 'You don\'t have enough money.'
                if money>pickaxe_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<pickaxe_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>pickaxe_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Throwing Rocks Before Trans:',pickaxe
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*pickaxe_buy
                            pickaxe+=choice
                            print '  BThrowing Rocks After Trans',pickaxe
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(pickaxe_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            if choice == "11":
                if money<machete_buy:
                    print 'You don\'t have enough money.'
                if money>machete_buy:
                    try:
                        choice = int(raw_input('How many do you need: '))
                        if money<machete_buy*float(choice):
                            print 'I\'m sorry, but you don\'t have that much money.'
                        if money>machete_buy*float(choice):
                            print '\nYour Reciept:'
                            print '  Throwing Rocks Before Trans:',machete
                            print '  Money Before Trans:',str(money)+'$'
                            money-=float(choice)*machete_buy
                            machete+=choice
                            print '  BThrowing Rocks After Trans',machete
                            print '  Money After Trans',str(money)+'$'
                            print '  Price Per Piece:',str(machete_buy)+'$'
                            print '  Amount Bought:',choice
                    except ValueError:
                        value_error()
                choice =''
            move_on=raw_input('Hit enter to exit:')
        if choice == "2":
            trade()
        if choice == "4":
            clear()
            print 'Price Per Battery:',charge_price
            print 'Charged/Good Batteries:',good_batteries
            print 'Discharged/Bad Batteries:',bad_batteries
            choice = raw_input('How many batteries do you need to charge: ')
            try:
                clear()
                if int(choice)*charge_price>money:
                    print 'You don\'t have enough money to charge',int(choice),'batteries.'
                if int(choice)>bad_batteries:
                    print 'You don\'t have that many. You have',bad_batteries,'discharges batteries.'
                if int(choice)<bad_batteries+1:
                    if int(choice)*charge_price<money+0.01:
                        print 'Charging...'
                        time.sleep(charge_time*int(choice))
                        good_batteries+=int(choice)
                        bad_batteries-=int(choice)
                        print 'Charged',int(choice),'batteries. You now have',good_batteries,'charged batteries.'
                        time.sleep(2.5)
                        i_have_the_power=True
            except:
                value_error()
        if choice == "5":
            p=True
            while p==True:
                clear()
                print 'What would you like to trade:'
                print 'Note: 1 gem  =  1 item'
                print '\n(1)Red Gems  -- Spears\n(2)Green Gems -- Rocks\n(3)Magenta Gems -- Bad Batttery\n(4)Yellow Gems -- Good Battery\n(5)Blue Gems -- Machetes'
                choice = raw_input('Which gem, (my gems) or (leave): ')
                if choice == "leave":
                    p=False
                if choice == "my gems":
                    clear()
                    gem_collection()
                if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
                    p=False
            if choice == "1":
                clear()
                if red_gem<1:
                    print 'Insufficent gems for trade.'
                if red_gem>0:
                    print 'You have',red_gem,'red gems'
                    choice = raw_input('How many would you like to trade: ')
                    try:
                        if red_gem<int(choice):
                            print 'You don\'t have thay many gems.'
                        if red_gem+1>int(choice):
                            spears+=int(choice)
                            red_gem-=int(choice)
                    except ValueError:
                        value_error()
            if choice == "2":
                clear()
                if green_gem<1:
                    print 'Insufficient gems for trade'
                if green_gem>0:
                    print 'You have',green_gem,'green gems.'
                    choice = raw_input('How many would you like to trade:')
                    try:
                        if green_gem<int(choice):
                            print 'You don\'t have that many gems.'
                        if green_gem+1>int(choice):
                            throwing_rocks+=int(choice)
                            green_gem-=int(choice)
                    except ValueError:
                        value_error()
            if choice == "3":
                clear()
                if magenta_gem<1:
                    print'Insufficient gems for trade'
                if magenta_gem>0:
                    print'You have',magenta_gem,'magenta gems'
                    choice = raw_input('How many would you like to trade')
                    try:
                        if magenta_gem<int(choice):
                            print 'You don\'t have enough gems'
                        if magenta_gem+1>int(choice):
                            bad_batteries+=1
                            magenta_gem-=1
                    except ValueError:
                        value_error()
            if choice == "4":
                clear()
                if yellow_gem<1:
                    print 'Insufficient gems for trade'
                if yellow_gem>0:
                    print 'You have',yellow_gem,'yellow gems.'
                    choice = raw_input('How many would you like to trade')
                    try:
                        if yellow_gem<int(choice):
                            print 'You don\'t have enough gems.'
                        if yellow_gem+1>int(choice):
                            good_batteries+=1
                            yellow_gem-=1
                    except ValueError:
                        value_error()
            if choice == "5":
                clear()
                if blue_gem<1:
                    print 'Insufficent gems for trade'
                if blue_gem>0:
                    print 'You have',blue_gem,'blue gems'
                    choice = raw_input('How many would you like to trade:')
                    try:
                        if blue_gem<int(choice):
                            print 'You don\'t have enoug gems.'
                        if blue_gem+1>int(choice):
                            machete+=1
                            blue_gem-=1
                    except ValueError:
                        value_error()
            choice = ''
            move_on=raw_input('Hit enter to exit: ')
        if choice == "6":
            print 'Have a Great day then! Hope to see you back.'
            time.sleep(1.5) #Adjust time as needed
        clear()
    def item_damage():
        global throwing_rocks_damage, spears_damage, pickaxe_damage, machete_damage
        print '  Throwing Rocks: '+str(throwing_rocks_damage[0])+'-'+str(throwing_rocks_damage[1])+' HP'
        print '          Spears: '+str(spears_damage[0])+'-'+str(spears_damage[1])+' HP'
        print '         Pickaxe: '+str(pickaxe_damage[0])+'-'+str(pickaxe_damage[1])+' HP'
        print '         Machete: '+str(machete_damage[0])+'-'+str(machete_damage[1])+' HP'
    def start_attack():
        global health, attack, throwing_rocks, victory_status, wires, torches, one_time, enemy, current_enemy, battery, custom_attack
        if custom_attack==False:
            count=len(enemy)
            rando=random.randint(0,count)
            current_enemy=enemy[rando]
            health=random.randint(25,50)
        if custom_attack==True:
            global health, current_enemy
        while health>0:
            attack=True
            print 'Enemy Name:', current_enemy
            print 'Enemy Health:',health,'HP'
            print '(1)Use item'
            print '(2)Attempt to run'
            choice=raw_input('Choose an option: ')
            if choice == "1":
                clear()
                open_bag()
            if choice == "2":
                chance=random.randint(0,2)
                if throwing_rocks>0:
                    if chance == 1:
                        print 'You got out with little to no harm. You did however loose 1 throwing rock.'
                        throwing_rocks-=1
                        health=0
                if throwing_rocks<1:
                    chance=0
                if chance == 0:
                    print 'You got out safe and sound. Nothing can stop you!'
                    health=0
                if chance == 2:
                    print 'The enemy stopped you moments before you tried to leave. He brought you back to fight.'
        health=0
        flashlight_use=False
        torch_use=False
        throwing_rocks_use=False
        attack=False
        one_time=False
        if victory_status==True:
            print 'You won! The enemy fell down without a doubt. You earnings are...'
            chance=random.randint(0,1)
            print 'You won',chance,'wires'
            wires+=chance
            chance=random.randint(0,2)
            print 'You won',chance,'torches'
            torches+=chance
            print 'You earned 25% battery for your flashlight.'
            battery+=25
            if battery>100:
                battery=100
        clear()
    def chapters():
        globals
        print 'True = Current Chapter'
        print 'Intro:',str(begin)
        print 'Chapter 1:',str(story_part1)
        print 'Chapter 2:',str(story_part2)
        print 'Chapter 3:',str(story_part3)
        print 'Chapter 4:',str(story_part4)
        print 'Chapter 5:',str(story_part5)
        print 'Chapter 6:',str(story_part6)
        print 'Chapter 7:',str(story_part7)
        print 'Chapter 8:',str(story_part8),' -- Not yet implemented'
        skip = raw_input('Hit enter to exit:')
    def open_menu():
        global menu_open, sticks, coal, torches, working_battery_charger, battery_charger, wires, computer_chips
        if menu_open==False:
            print 'Here you can do some crafting and see what you can do with certian items.\n'
            loop=True
            while loop == True:
                print '-Options-\nBuild\nleave\nCharge batteries'
                check = raw_input('Choose one: ').lower()
                if check == "build":
                    clear()
                    print '-Options-\nBattery charger\nTorches'
                    check = raw_input('Choose one: ').lower()
                    if check == "torches":
                        print 'You need 1 stick and 1 coal to make 4 torches.'
                        check = raw_input('(Yes/No)Would you like to make some: ').lower()
                        if check == "yes":
                            print 'Checking for items.'
                            time.sleep(.6)
                            print 'Checking for items..'
                            time.sleep(.6)
                            print 'Checking for items...'
                            time.sleep(.6)
                            if sticks>0:
                                if coal>0:
                                    print 'You made 4 sticks. It has been added to your backpack.'
                                    coal-=1
                                    sticks-=1
                                    torches+=4
                            if sticks<1:
                                print 'You need more sticks'
                            if coal<1:
                                print 'You need more coal'
                        if check == "no":
                            pass
                    if check == "battery charger":
                        clear()
                        print 'You will need a battery charger, 5 wires and 1 computer chip.'
                        check = raw_input('(Yes/No)Would you like to make it: ').lower()
                        if check == "yes":
                            if working_battery_charger==False:
                                if battery_charger==True:
                                    if wires>4:
                                        if computer_chips>0:
                                            print 'You now have a working battery charger.'
                                            working_battery_charger=True
                            if working_battery_charger==True:
                                print 'You already have one'
                            if working_battery_charger==False:
                                if battery_charger==False:
                                    print 'You don\'t have a battery charger'
                            if working_battery_charger==False:
                                if wires<5:
                                    print 'You don\'t have 5 wires'
                            if working_battery_charger==False:
                                if computer_chips<1:
                                    print 'You don\'t have enough computer chips.'
                if check == "leave":
                    loop=False
                if check == "charge batteries":
                    if working_battery_charger==True:
                        if bad_batteries>0:
                            print 'All you batteries are now good.'
                            good_batteries+=bad_batteries
                            bad_batteries=0
                            i_have_the_power=True
                        if bad_batteries<1:
                            print 'You don\'t have any discharged batteries'
                    if working_battery_charger==False:
                        print 'You need to make the battery charger.'
    def starting_stuff():
        global good_batteries, bad_batteries, battery, bag_open, flashlight
        #Reset of variables
        good_batteries=5
        bad_batteries=0
        battery=100
        bag_open=True
        #Adding some new characteristics
        flashlight=False
    def help_menu():
        global torches, throwing_rocks
        loop=True
        while loop == True:
            print '(1)Torches'
            print '(2)Flashlight'
            print '(3)Throwing rocks'
            print '(4)Battery'
            print '(5)My suit'
            print '(6)To move onto game'
            print "(7)My computer says 'clear' is not reconized..."
            check = str(raw_input('Which one: '))
            clear()
            if check == "1":
                print 'Narrator: You will start with ',str(torches),'. They are a one time use.'
                print 'You can use these to see and possibly find items you wouln\'t be able to'
                print 'find. Torches and the flashlight are used in the same way but are costly'
                print 'in their own way. When you use a torch, the amount you can use goes down'
                print 'by one. You can find more torches by exploring. Torches are not common'
                print 'to find.'
            if check == "2":
                print 'Narrator: You will not start with a flash light. You will need to find one.'
                print 'When you use the flash light it will absorb 5-10 percent of your battery'
                print 'each time. If you run out of battery you will need to change it in you'
                print 'backpack. The flash light will never break.'
            if check == "3":
                print 'Narrator: You will have ',str(throwing_rocks),' to start out. You can find more'
                print 'lying on the ground. They are very common to find. This is your starting weapon.'
                print 'As the game devolopes more weapons will be added. For now there are only rocks.'
                print 'And since that, rocks are the most powerful weapon of all right now. it will'
                print 'usually take aleast 2-3 rocks to defeat an enemy. Some time if you lucky only 1.'
            if check == "4":
                print 'Narrator: To check your battery percent type (%) when available. And to see how'
                print 'many you have check your backpack. The battery will be used for some thing. First,'
                print 'it will be used for your flashlight, then it will be used for ecolocation, and'
                print 'sometimes you will find a machine that needs to be powered by your suit.'
            if check == "5":
                print 'Narrator: You suit is the one that holds the batteries. It also holds you items.'
                print 'Since it makes no since to store things in a suit, we call the place holder a backpack.'
                print 'But, the suit will hold new technology you find and be able to reconize and reapir it.'
                print 'You suit comes with a repair tool, a analyizer, mini fridge, and many others. You will'
                print 'No need to wory about eating it is done between games.'
            if check == "6":
                loop=False
            if check == "7":
                print 'To fix this problem you will need to head to the settings page. To enter'
                print 'the settings page exit this space by typing (6) and then type settings.'
                print 'Then type (1). The problem should be fixed afterwards.'
    def count():
        print ('10%')
        time.sleep(.2)
        print ('20%')
        time.sleep(.2)
        print ('30%')
        time.sleep(.2)
        print ('40%')
        time.sleep(.2)
        print ('50%')
        time.sleep(.2)
        print ('60%')
        time.sleep(.2)
        print ('70%')
        time.sleep(.2)
        print ('80%')
        time.sleep(.2)
        print ('90%')
        time.sleep(.2)
        print ('100%')
        time.sleep(.2)
    def open_bag():
        global pickaxe, machete, machete_use, pickaxe_use, total_wins, spears, spears_use, one_time, victory_status, attack, health, bag_open, good_batteries, bad_batteries, torches, battery, throwing_rocks, battery_charger, computer_chips, wires, sticks, coal, throwing_rocks_use, flashlight_use, torch_use
        if bag_open == False:
            bag_open=True
            print '\nGame: While in your backpack type the number of the item to use it.'
            print 'Game: For this item we will switch the batteries\n'
            time.sleep(3)
        print '(1)Good Batteries: '+str(good_batteries)
        print '(2)Bad Batteries: '+str(bad_batteries)
        if torch_use==False and flashlight_use==False and one_time==False:
            print '(3)Torch: '+str(torches)
            print '(4)Flashlight: '+str(battery)
        if flashlight_use==True and torch_use==True:
            print '(3)Throwing_rocks: '+str(throwing_rocks)
            print '(4)Spears: '+str(spears)
            print '(5)Pickaxe: '+str(pickaxe)
            print '(6)Machete: '+str(machete)
        if flashlight_use==False and torch_use==False:
            print '(5)Throwing_rocks: '+str(throwing_rocks)
            print '(6)Spears: '+str(spears)
            print '(7)Pickaxe: '+str(pickaxe)
            print '(8)Machete: '+str(machete)
        if attack==False:
            print '(9)Collectable items'
            print '(10)Total wins'
            check = str(raw_input('\nType (leave) or enter item number to use: ')).lower()
        if attack == True:
            check = str(raw_input('What item will you use: ')).lower()
        if check =="10":
            if attack==False:
                print 'Total wins',total_wins
                move_on=raw_input('Hit enter to exit: ')
        if check == "9":
            if attack==False:
                if battery_charger==True:
                    print '(1)Battery charger:',str(battery_charger)
                    print '(2)Wires:',str(wires)
                    print '(3)Computer chips:',str(computer_chips)
                    print '(4)Sticks:',str(sticks)
                    print '(5)Coal:',str(coal)
        if check == "8":
            if attack==True and flashlight_use==False:
                if machete<1:
                    print 'System: You are out of ammo.'
                if machete>0:
                    machete_use=True
                    machete-=1
        if check == "7":
            if attack==True and flashlight_use==False:
                if pickaxe<1:
                    print 'System: You are out of ammo.'
                if pickaxe>0:
                    pickaxe_use=True
                    pickaxe-=1
        if check == "6":
            if attack==True and flashlight_use==False:
                if spears<1:
                    print 'System: You are out of ammo.'
                if spears>0:
                    spears_use=True
                    spears-=1
        if check == "5":
            if attack==True and flashlight_use==False:
                if throwing_rocks<1:
                    print 'System: You are out of ammo.'
                if throwing_rocks>0:
                    throwing_rocks_use=True
                    throwing_rocks-=1
        if check == "6":
            if attack==True and flashlight_use==True:
                if machete<1:
                    print 'System: You are out of ammo.'
                if machete>0:
                    machete_use=True
                    machete-=1
        if check == "5":
            if attack==True and flashlight_use==True:
                if pickaxe<1:
                    print 'System: You are out of ammo.'
                if pickaxe>0:
                    pickaxe_use=True
                    pickaxe-=1
        if check == "4":
            if attack==True and flashlight_use==True:
                if spears<1:
                    print 'System: You are out of ammo.'
                if spears>0:
                    spears_use=True
                    spears-=11
        if check == "3":
            if attack==True and flashlight_use==True:
                if throwing_rocks<1:
                    print 'System: You are out of ammo.'
                if throwing_rocks>0:
                    throwing_rocks_use=True
                    throwing_rocks-=1
        if check == "4":
            if one_time==False:
                flashlight_use=True
                torch_use=True
                battery-=5
        if check == "3":
            if one_time==False:
                torches-=1
                torch_use=True
                flashlight_use=True
        if check == "1":
            if good_batteries>0:
                good_batteries-=1
                bad_batteries+=1
                battery=100
                print 'Your new stats\n'
                print '(1)Good Batteries: '+str(good_batteries)
                print '(2)Bad Batteries: '+str(bad_batteries)
                print 'Battery: '+str(battery)
                print '\n'
            if good_batteries<1:
                print 'You don\'t have any charged batteries.'
            move_on=raw_input('Hit enter to exit: ')
        if check == "2":
            print 'Those are no good for now. Try again later.'
        if check == "leave":
            print 'Moving you on'
        clear()
        if attack == True:
            if machete_use==True:
                chance=random.randint(0,4)
                if chance == 0:
                    print 'You swing the blade with all your might. It slices off a good hunk of flesh from the target.'
                if chance == 1:
                    print 'You go for a simple but lethal stab. You miss the torso, but instead scrape the targets arm.'
                if chance == 2:
                    print 'You swing for the neck, like some kind of killer from a slasher flick. You slip on a patch of moss on the ground and instead slice a big gash across the foes torso.'
                if chance == 3:
                    print 'You wind up for a swing, which takes about 2 seconds, and release, slicing a huge gash on the enemies body.'
                if chance == 4:
                    print 'You swing wildly, like you\'re fighting for your life against a horde of enemies, even though its only one.'
                damage=random.randint(machete_damage[0],machete_damage[1])
                health-=damage
                print 'Damage Dealt: ',damage
                machete_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if pickaxe_use==True:
                chance=random.randint(0,4)
                if chance == 0:
                    print 'You swing for the enemies skull, or head like extrusion. There is a resounding crack, and you see a decently sized wound.'
                if chance == 1:
                    print 'You try to hit the ceiling to drop some rocks on the enemies head. You land a solid swing, but all the drops is a few pebbles. The enemy pities you, and hurts islf for you.'
                if chance == 2:
                    print 'You swing for the creatures ribs, hoping to break some bones. There\'s a loud crack sound, and the creature crumples over in pain.'
                if chance == 3:
                    print 'You step back a short distance, and taunt the enemy into charging. Once its close enough, you swing the flat side of the pick at its jaw, or other similar area, tossing it up and hitting its head on the ceiling.'
                if chance == 4:
                    print 'You club the enemy over the head with the handle of the pick. There\'s a decently sized lump left over.'
                damage=random.randint(pickaxe_damage[0],pickaxe_damage[1])
                health-=damage
                print 'Damage Dealt: ',damage
                pickaxe_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if spears_use==True:
                chance=random.randint(0,6)
                if chance == 0:
                    print 'You throw your long stick shaped object in the enemies direction. Hit! The enemy takes damage.'
                if chance == 1:
                    print 'You use all of your strength while ensuring your is stable to be able to throw the spear as hard as you can. Shoooosh... Goes through the air.'
                if chance == 2:
                    print 'You get ready to throw the spear... You trip on a rock and you just barely miss, still hitting the enemy though. Not all of your power was put through.'
                if chance == 3:
                    print 'You raise the spear to your side, to go for a stab. You get a running start, but stumble and stab the enemy in the foot. It yowls in pain, and takes damage.'
                if chance == 4:
                    print 'You try to swipe at the enemy with the pointy end, but grabbed the spear the wrong way, and instead hit it with the blunt end, doing slightly more damage.'
                if chance == 5:
                    print 'You go for a jump attack, but overestimated the actual height of the cavern, instead, hitting your head off the ceiling, damaging yourself instead. Idiot.'
                if chance == 6:
                    print 'You go to grab your spear, but feel nothing there. You hear a noise behind you and turn to investigate. You see a small dog running towards the enemy with the spear. you...hit it??'
                damage=random.randint(spears_damage[0],spears_damage[1])
                health-=damage
                print 'Damage Dealt: ',damage
                spears_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if throwing_rocks_use==True:
                chance=random.randint(0,6)
                if chance==0:
                    print 'You attack the enemy with a rock. He cried to his mommy afterwards.'
                if chance==1:
                    print 'You hurt the enemy with a small indistinct bolder. He felt nothing.'
                if chance==2:
                    print 'You penetrated the enemy with a big grain of sand. He doesn\'t care.'
                if chance==3:
                    print 'You assulted the enemy with a gray peble. He smacked you in the face.'
                if chance==4:
                    print 'You show the enemy how much you hate him. He broke in tears.'
                if chance==5:
                    print 'You used physics to move the peble towards him creating pain on the enemy.'
                if chance==6:
                    print 'You enflicted undesired actions onto your enemy. He doesn\'t like it.'
                damage=random.randint(throwing_rocks_damage[0],throwing_rocks_damage[1])
                health-=damage
                print 'Damage Dealt: ',damage
                throwing_rocks_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if flashlight_use==True or torch_use==True:
                if one_time==False:
                    chance=random.randint(0,6)
                    if chance == 0:
                        print 'You pull out your light and take a look around. You capture everything in your mind and use it to your full potential.'
                    if chance == 1:
                        print 'You grab your light and take a look at what you are battling. You see rotten flesh covering his bones, smells covering his shame, and pain covering his soul. You take a step back and turn your light off.'
                    if chance == 2:
                        print 'You pull out your light and take a look around. You try and see if there is anything useful lying around. You find 10 throwing rocks.'
                        throwing_rocks+=10
                    if chance == 3:
                        print 'You pull out a photon emmitter to survey the area. You find a very pointy and rude stick on the ground near you. You make contact with the tip and it instantly removes blood from your body. You gain 1 spear.'
                        spears+=1
                    if chance == 4:
                        print 'You pull out a neon green flashlight and survey the area. Its hard to tell what\'s around you due to the color.'
                    if chance == 5:
                        print 'You effortlessly aquire a flashlight from your...uhhh... inventory. The lens is slightly cracked, but you manage to see a small round creature sprint past you, muttering something about donuts.'
                    if chance == 6:
                        print 'You grab the glowing round cylinder off the ground. The energy storage container has lost it\'s will to live. You put the glowing round cylinder back on the ground.'
                    torch_use=True
                    flashlight_use=True
                    one_time=True
    def battery_bag():
        global battery
        print 'Battery: '+str(battery)
    import time
    if dev==True:
        skip=True
    if dev==False:
        print 'Skip setup -- (skip)'
        name=raw_input('Hello user, Enter your name: ').lower()
        if name=="brandon":
            skip=True
            dev=True
            menu_open=True
            bag_open=True
        if name=='skip':
            print '-Choose an option-'
            print 'bag'
            print 'count_var'
            print 'battery_percent'
            print 'start_game'
            print 'starting_stuff'
            print 'skip_intro'
            check = raw_input()
            if check == "skip_intro":
                skip=True
            if check == "starting_stuff":
                starting_stuff()
            if check == "start_game":
                start=True
            if check == "bag":
                open_bag()
            if check == "count_var":
                count()
            if check == "battery_percent":
                battery_bag()
    if skip==False:
        print 'Game will start soon.'
        time.sleep(3)
        print 'Game starting in 3'
        time.sleep(1)
        print 'Game starting in 2'
        time.sleep(1)
        print 'Game starting in 1'
        time.sleep(1)
        clear()
        print 'In some dark and stormy night. You and your parents live in a small house in the middle of the forest. You are frightened and scared.'
        time.sleep(6)
        print'Your parents tell you to stay in your room.'
        time.sleep(4)
        print 'You hear noises...'
        time.sleep(2)
        print 'Noises like no other.'
        time.sleep(4)
        print 'Then... You hear screams!'
        time.sleep(.9)
        print'...........!'
        time.sleep(3)
        clear()
        print 'Narrator: You\'ve been knocked out.'
        time.sleep(2)
        print 'Checking all systems...'
        count()
        time.sleep(1.3)
        print 'All systems check'
        time.sleep(2)
        clear()
        loop=True
        while loop==True:
            print'(Yes/No) Narrator: Are you okay: '
            check=raw_input().lower()
            if check == "yes" or check == "y":
                print 'Narrator: That\'s good to hear.'
                loop=False
            if check == "no" or check == "n":
                print 'Narrator: Well, um, you will get through it.'
                loop=False
        time.sleep(3.5)
        print 'System: Emergency, power supply running low!'
        print 'Battery: '+str(battery),'%'
        time.sleep(2.7)
        clear()
        print 'Narrator: Okay, we must gather some power.'
        time.sleep(.8)
        loop=True
        while loop==True:
            print 'Game: Type (bag) when available to open your backpack.'
            check = raw_input('Game: Open your bag: ').lower()
            if check == "bag":
                open_bag()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        clear()
        print 'System: Power supply, stable.'
        time.sleep(1.5)
        print 'System: To see your current battery percent type (%)'
        time.sleep(1.5)
        print 'Narrator: You better do what she says.'
        time.sleep(4)
        clear()
        loop=True
        while loop==True:
            print '\nGame: Type (%) when available to see your battery percentage.'
            check = raw_input('Game: Check battery percentage: ')
            if check == "%":
                clear()
                battery_bag()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        time.sleep(3)
        loop=True
        clear()
        while loop==True:
            print 'Okay now, to see app improvements type (updates).'
            check = raw_input('Game: Check the updates for this version: ').lower()
            if check == "updates" or check == "update":
                clear()
                updates()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        loop=True
        clear()
        while loop==True:
            print 'To see locked and unlocked chapters type (chapters).'
            check = raw_input('Game: Check your unlocked chapters: ').lower()
            if check == "chapters" or check == "chapter":
                clear()
                chapters()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        loop=True
        clear()
        while loop==True:
            print 'To change settings to your preference type (settings)'
            check = raw_input('Game: Open the settings page: ').lower()
            if check == "setting" or check == "settings":
                clear()
                settings()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        clear()
        print 'Narrator: Okay, you now know the basics, lets put you in the game.'
        time.sleep(4)
        print 'Game: Putting narrator to sleep...'
        time.sleep(3)
        print 'Narrator: Wait, what!'
        time.sleep(2)
        print 'Narrator: You can\'t do this... I feel... sleaspafajsdlle...'
        time.sleep(3.5)
        print 'Game: Narrator went to sleep'
        time.sleep(2.2)
        print 'Game: Game starting up...'
        time.sleep(2)
        clear()
        count()
        print'\nWelcome to <THE NEW GAME>'
        time.sleep(.5)
        print 'System: Booting up Narrator.'
        time.sleep(.5)
        print 'System: Booting up Narrator..'
        time.sleep(.5)
        print 'System: Booting up Narrator...'
        time.sleep(.5)
        print 'System: Booting up Narrator..'
        time.sleep(.5)
        print 'System: Booting up Narrator.'
        time.sleep(.5)
        print 'System: Booting up Narrator..'
        time.sleep(.5)
        print 'System: Booting up Narrator...'
        print '\n'
        time.sleep(1)
        clear()
        print 'Setting up items.'
        time.sleep(.5)
        print 'Setting up items..'
        time.sleep(.5)
        print 'Setting up items...'
        time.sleep(.5)
        print 'Setting up items..'
        time.sleep(.5)
        print 'Setting up items.'
        time.sleep(.5)
        print 'Setting up items..'
        time.sleep(.5)
        print 'Setting up items...'
        time.sleep(.5)
        clear()
        print 'Game: All systems check'
        time.sleep(.5)
        print 'Narrator: All systems check'
        time.sleep(.5)
        print 'System: All systems check'
        time.sleep(2.5)
        clear()
        print 'Narrator: Oh, I\'m back. Thank god.'
        time.sleep(1.8)
        print 'Narrator: So user. There are still some things to teach you.'
        time.sleep(3)
        print 'Narraror: But I\'ll let you choose the order. To start enter the number next to the item.'
        time.sleep(3)
        help_menu()
        time.sleep(1)
        clear()
        print '\nOne more thing. When available type (help) to go back to that list. More items will be added in future updates.'
        print 'Game loading.'
        time.sleep(.5)
        print 'Game loading..'
        time.sleep(.5)
        print 'Game loading...'
        time.sleep(.5)
        clear()
        count()
    if skip==True:
        clear()
    start=True
    if start==True:
        loop=True
        while loop == True:
            #starting_stuff()
            loop=True
            while loop == True:
                print 'Your options:'
                print 'Bag       Start     %'
                print 'Hints     Menu      Save'
                print 'Shop      Awards    Updates'
                print 'Chapters  Settings  Collisseum'
                print 'Damage    Gems      Load'
                print '\n'
                check = raw_input('Choose an option: ').lower()
                clear()
                if check == "load":
                    if dev==False:
                        non_function()
                    if dev==True:
                        works=False
                        try:
                            os.remove('Save.py')
                        except:
                            pass
                        try:
                            load=file('Save.gsf','r')
                            load.close()
                            works=True
                        except:
                            print "Could not find a save file."
                            print 'Current Path:',path
                        if works==True:
                            print 'Renaming File...'
                            os.rename("Save.gsf","Save.py")
                            time.sleep(2)
                            clear()
                            from Save import version_save
                            if version_save not in version:
                                print 'This save file is not compatible with this version.'
                            if version_save == version:
                                print 'File Renamed. Importing variables...'
                                from Save import *
                                time.sleep(2)
                                clear()
                                print 'Variables imported. Reverting file name...'
                                os.rename("Save.py","Save.gsf")
                                time.sleep(2)
                                clear()
                                print ('Removing Cached File...')
                                time.sleep(2)
                                clear()
                                try:
                                    os.remove("Save.pyc")
                                except WindowsError:
                                    windows_error('Save.pyc')
                                print 'System: Import successful'
                        move_on=raw_input('Hit enter to exit: ')
                if check == "save":
                    clear()
                    save=file('Save.gsf','w')
                    save.write('#*The New Game Save File*')
                    save.write('\ndev = '+str(dev))
                    save.write('\nunlock_all_achievements = '+str(unlock_all_achievements))
                    save.write('\nrepeat_chapters = '+str(repeat_chapters))
                    save.write('\nnormal_clear = '+str(normal_clear))
                    save.write('\nrepeat_amount = '+str(repeat_amount))
                    save.write('\nchars_in_line = '+str(chars_in_line))
                    save.write('\nrun_off = '+str(run_off))
                    save.write('\nerror_message = '+str(error_message))
                    save.write('\nbegin = '+str(begin))
                    save.write('\nstory_part1 = '+str(story_part1))
                    save.write('\nstory_part2 = '+str(story_part2))
                    save.write('\nstory_part3 = '+str(story_part3))
                    save.write('\nstory_part4 = '+str(story_part4))
                    save.write('\nstory_part5 = '+str(story_part5))
                    save.write('\nstory_part6 = '+str(story_part6))
                    save.write('\nstory_part7 = '+str(story_part7))
                    save.write('\nstory_part8 = '+str(story_part8))
                    save.write('\nflashlight = '+str(flashlight))
                    save.write('\nbattery_charger = '+str(battery_charger))
                    if version == "0.2.5":
                        save.write("\nenemy=['Goblin','Karen','Bat','Skeleton','Zombie','Flip Phone','Youra the explora','No Cell Service','My Brother']")
                    save.write("\ncurrent_enemy=''")
                    save.write('\nmoney = '+str(money))
                    save.write('\nworking_battery_charger = '+str(working_battery_charger))
                    save.write('\nskip = '+str(skip))
                    save.write('\none_time = '+str(one_time))
                    save.write('\nhealth = '+str(health))
                    save.write('\nstart = '+str(start))
                    save.write('\nattack = '+str(attack))
                    save.write('\nvictory_status = '+str(victory_status))
                    save.write('\nseen_notes = '+str(seen_notes))
                    save.write('\ntotal_wins = '+str(total_wins))
                    save.write('\ncharge_price = '+str(charge_price))
                    save.write('\ncharge_time = '+str(charge_time))
                    save.write('\ncustom_attack = '+str(custom_attack))
                    save.write('\npickaxe = '+str(pickaxe))
                    save.write('\nmachete = '+str(machete))
                    save.write('\nsticks = '+str(sticks))
                    save.write('\ncoal = '+str(coal))
                    save.write('\ncomputer_chips = '+str(computer_chips))
                    save.write('\nwires = '+str(wires))
                    save.write('\ngood_batteries = '+str(good_batteries))
                    save.write('\nbad_batteries = '+str(bad_batteries))
                    save.write('\nbattery = '+str(battery))
                    save.write('\nthrowing_rocks = '+str(throwing_rocks))
                    save.write('\nspears = '+str(spears))
                    save.write('\ntorches = '+str(torches))
                    save.write('\nflashlight_use = '+str(flashlight_use))
                    save.write('\nthrowing_rocks_use = '+str(throwing_rocks_use))
                    save.write('\npickaxe_use = '+str(pickaxe_use))
                    save.write('\nmachete_use = '+str(machete_use))
                    save.write('\nspears_use = '+str(spears_use))
                    save.write('\ntorch_use = '+str(torch_use))
                    save.write('\nno_light = '+str(no_light))
                    save.write("\nthrowing_rocks_damage=[7,15]")
                    save.write("\nspears_damage=[11,17]")
                    save.write("\npickaxe_damage=[15,19]")
                    save.write("\nmachete_damage=[17,23]")
                    save.write('\nred_gem = '+str(red_gem))
                    save.write('\ngreen_gem = '+str(green_gem))
                    save.write('\nmagenta_gem = '+str(magenta_gem))
                    save.write('\nyellow_gem = '+str(yellow_gem))
                    save.write('\nblue_gem = '+str(blue_gem))
                    save.write('\ncoal_buy = '+str(coal_buy))
                    save.write('\ncomputer_chips_buy = '+str(computer_chips_buy))
                    save.write('\nwires_buy = '+str(wires_buy))
                    save.write('\ngood_batteries_buy = '+str(good_batteries_buy))
                    save.write('\nbad_batteries_buy = '+str(bad_batteries_buy))
                    save.write('\nsticks_buy = '+str(sticks_buy))
                    save.write('\nthrowing_rocks_buy = '+str(throwing_rocks_buy))
                    save.write('\nspears_buy = '+str(spears_buy))
                    save.write('\ntorches_buy = '+str(torches_buy))
                    save.write('\npickaxe_buy = '+str(pickaxe_buy))
                    save.write('\nmachete_buy = '+str(machete_buy))
                    save.write('\ncoal_sell = '+str(coal_sell))
                    save.write('\ncomputer_chips_sell = '+str(computer_chips_sell))
                    save.write('\nwires_sell = '+str(wires_sell))
                    save.write('\ngood_batteries_sell = '+str(good_batteries_sell))
                    save.write('\nbad_batteries_sell = '+str(bad_batteries_sell))
                    save.write('\nsticks_sell = '+str(sticks_sell))
                    save.write('\nthrowing_rocks_sell = '+str(throwing_rocks_sell))
                    save.write('\nspears_sell = '+str(spears_sell))
                    save.write('\ntorches_sell = '+str(torches_sell))
                    save.write('\npickaxe_sell = '+str(pickaxe_sell))
                    save.write('\nmachete_sell = '+str(machete_sell))
                    save.write('\nlet_the_battles_begin = '+str(let_the_battles_begin))
                    save.write('\nguts_and_glory = '+str(guts_and_glory))
                    save.write('\ni_have_the_power = '+str(i_have_the_power))
                    save.write('\nits_payday = '+str(its_payday))
                    save.write('\nwhicked_chronicle = '+str(whicked_chronicle))
                    save.write('\n\n#Developers: Brandon Robinson, Albert Plummer')
                    save.write('\n#Github Page: github.com/sukadateam')
                    save.write('\n#Please report any bugs you encounter.')
                    save.write("\nversion_save = '0.2.5'")
                    save.close()
                    print 'Game saved.'
                    move_on=raw_input('Hit enter to exit: ')
                if check == "gems":
                    gem_collection()
                if check == "award" or check == "awards":
                    achieve()
                if check == "dev battle":
                    if dev==True:
                        start_attack()
                    if dev==False:
                        print 'Nice try. You are not in dev mode.'
                if check == "dev edit_chapters":
                    if dev==True:
                        edit_chapters()
                    if dev==False:
                        print 'Nice try. You are not in dev mode.'
                if check == "collisseum":
                    if guts_and_glory==True or dev==True:
                        collisseum()
                    if guts_and_glory==False and dev==False:
                        print 'You have not unlocked this yet.'
                        print 'This feature will not be unlocked until version 0.3.0.'
                        print 'To use this feature enable dev mode.'
                if check == "shop":
                    shop()
                    check=''
                if check == "damage":
                    item_damage()
                    check=''
                if check == "setting" or check == "settings":
                    settings()
                    check=''
                if check == "chapters" or check == "chapters":
                    chapters()
                    check=''
                if check == "updates" or check == "update":
                    updates()
                    check=''
                if check == "menu":
                    open_menu()
                    check=''
                if check == "bag":
                    open_bag()
                    check=''
                if check == "%":
                    battery_bag()
                    check=''
                if check == "hints":
                    print 'HINT: Taking left or right will lead you to the same place but you will gather different items'
                    print 'HINT: Taking a left takes 4 seconds to complete, a right takes 6 seconds to complete, forward is unknown'
                    print 'HINT: Traps take 50 of your energy'
                    print "HINT: If your energy hits 0% you are forced to leave the cave"
                    print 'HINT: A special passage has a chance to give you 25 energy'
                    print 'HINT: Every time you leave you must restart your adventure. You will not loose you stuff.'
                    print 'HINT: Leave cave and go back the ways you didn’t to make sure you have everything'
                    print '\nWhen you see this (*) you are allowed to type (bag) or (menu).'
                if check == "start":
                    skip_begin=False
                    if begin == True:
                        print 'Your first day of exploring is going to be your best. You enter'
                        print 'the cave and see that there are 2 sides to it. You can either go left'
                        print 'or you can go right. Which do you choose?'
                        print '\n'
                        battery_bag()
                        check = raw_input("(*)Left or Right: ").lower()
                        if check == "menu":
                            open_menu()
                        elif check == "bag":
                            open_bag()
                        elif check == "left":
                            clear()
                            print 'You take a left turn. You head straight for some time. While'
                            print 'doing so, you find a battery charger. It looks like it might'
                            print 'come in handy. But we can\'t use it till we find some parts.'
                            print 'Lets keep looking.'
                            battery_charger=True
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(4)
                            begin=False
                            story_part1=True
                        elif check == "right":
                            clear()
                            print 'You make a right turn. You head straight for some time. While'
                            print 'doing so, you find a wire on the ground. I looks like it might'
                            print 'be used for a battery charger, but I\'m not sure. Keep exploring'
                            print 'to find more things.'
                            wires+=1
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(4)
                            begin=False
                            story_part1=True
                        else:
                            pass
                    if skip_begin==True:
                        begin=False
                    if story_part1==True or repeat_chapters==True:
                        clear()
                        print 'You have 3 choices.'
                        print 'Left: Seems to be safe.'
                        print 'Straight: Seems to be a trap.'
                        print 'Right: Rumor has it, it\'s a special passage.'
                        check = raw_input('Forward, Left, Right: ').lower()
                        clear()
                        if check == "chapters" or check == "chapters":
                            chapters()
                        if check == "updates" or check == "update":
                            updates()
                        if check == "menu":
                            open_menu()
                        if check == "bag":
                            open_bag()
                        if check == "forward":
                            clear()
                            print 'You go forward farther into the cave. You walk very slowly with the'
                            print 'feeling of being sensed, You hear noises. POP. Out of nowhere. Your'
                            print 'battery explodes. You quickly change it out. You rush through the'
                            print 'cave to the end.'
                            good_batteries-=1
                            bad_batteries+=1
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(7.5)
                            story_part2=True
                            story_part1=False
                        if check == "left":
                            clear()
                            print 'You take a left and there seems to be nothing here. You keep going through.'
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(4)
                            story_part2=True
                            story_part1=False
                        if check == "right":
                            clear()
                            print 'You take a right and you walk for a bit. You look around and you see a battery'
                            print 'charger on the wall. It looks like it has power. You charge your current battery.'
                            print 'Your energy increases by 25%. You walk through the rest of the way.'
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(6)
                            story_part2=True
                            story_part1=False
                            battery+=25
                    if story_part2==True or repeat_chapters==True:
                        clear()
                        print 'You have 2 choices.'
                        print 'Left: Seems to be a trap.'
                        print 'Forward: Seems to be safe.'
                        check = raw_input('Left, Forward: ').lower()
                        clear()
                        if check == "chapters" or check == "chapters":
                            chapters()
                        if check == "updates" or check == "update":
                            updates()
                        if check == "menu":
                            open_menu()
                        if check == "bag":
                            open_bag()
                        if check == "left":
                            print 'You take a left. It seems to be a trap. You walk through carefully.'
                            print 'While you walk through you see a light shine. It looks to be shining'
                            print 'on an object. You go check it out. You got a closer look and find 2'
                            print 'more wires. You pick them up. You walk through the rest in hopes that'
                            print 'there are no traps.'
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(3)
                            story_part3=True
                            story_part2=False
                            wires+=2    
                        if check == "forward":
                            print 'You go forward through the cave. While you do so, you look at the'
                            print 'design of the cave. You find it interesting that the cave has some'
                            print 'beautiful colors. You take in all the details. But you find'
                            print 'something odd on the wall. It looks like a computer chip. You ask'
                            print 'yourself, why is there a computer chip in this cave. You try and'
                            print 'think about it but you soon come to realize you don’t know anything.'
                            print 'Anything about the cave or anything outside the cave in that matter.'
                            print 'You try and not think about it to hard and you move on to your \nadventure.'
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(3)
                            story_part3=True
                            story_part2=False
                            computer_chips+=1     
                    if story_part3==True or repeat_chapters==True:
                        clear()
                        print 'You have 2 choice.'
                        print 'Left: Seems to be safe.'
                        print 'Right: Seems to be safe.'
                        check = raw_input('Left, Right: ').lower()
                        clear()
                        if check == "chapters" or check == "chapters":
                            chapters()
                        if check == "updates" or check == "update":
                            updates()
                        if check == "menu":
                            open_menu()
                        if check == "bag":
                            open_bag()
                        if check == "left":
                            print 'You take a left. While you are walking down this way you think about things.'
                            print 'Like why are you even in these caves? What is the point? Then you think a'
                            print 'little harder. You realize you forgot why. You take a glance at the walls in'
                            print 'the caves. You think harder. And it finally comes to you. You are down here'
                            print 'to find the missing artifact.'
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(4)
                            story_part4=True
                            story_part3=False
                        if check == "right":
                            print 'You walk down the cave and find a stick on the ground. It seems to have a shape'
                            print 'of a torch. But we can’t make a torch without coal. So you pick it up thinking'
                            print 'it\’s useless but in hopes it will come in handy.'
                            print '\nMoving through the mines...'
                            if dev==False:
                                time.sleep(6)
                            story_part4=True
                            story_part3=False
                            sticks+=1
                    if story_part4==True or repeat_chapters==True:
                        clear()
                        print 'There doesn\'t seem to be an end to this passage. Maybe if we continue forward'
                        print 'we will eventually find something.' 
                        print 'Moving down the passage...'   
                        if dev==False:
                                time.sleep(6.5)
                        print 'You have been walking the same way for a while now. You feel like it will never end...'   
                        print 'Moving down the passage...'
                        if dev==False:
                                time.sleep(6.5)
                        print 'You eventually stumble apon an item laying on the ground. You pick it up and it'
                        print 'appears to be 2 fully charged batteries.'
                        good_batteries+=2
                        if dev==False:
                                time.sleep(5)
                        print '\nMoving through the mines...'
                        story_part5=True
                        story_part4=False
                    if story_part5==True or repeat_chapters==True:
                        clear()
                        print 'There seems to be 2 options. You can go Left or straight.'
                        print 'Straight: Seems to be safe.'
                        print 'Left: Seems to have a battery charger.'
                        check = raw_input('Left, Straight: ').lower()
                        clear()
                        if check == "chapters" or check == "chapters":
                            chapters()
                        if check == "updates" or check == "update":
                            updates()
                        if check == "menu":
                            open_menu()
                        if check == "bag":
                            open_bag()
                        if check == "left":
                            print 'You take a left and head down the passage. While walking you seem to find a'
                            print 'steep hill moving you farther down the cave. You continue moving and you start'
                            print 'to slip. You slide all the way down the hill and come to a stop. You get up and'
                            print 'check your surroundings. And doing so you find a battery charger.'
                            print 'Moving down the passage...'
                            story_part6=True
                            story_part5=False
                            battery_charger=True
                        if check == "straight":
                            print 'You head straight and find 2 wires. You pick them up and put them away, then you continue your adventure.'
                            wires+=2
                            print 'Moving down the passage...'
                            story_part6=True
                            story_part5=False
                    if story_part6==True or repeat_chapters==True:
                        clear()
                        print 'You venture farther down the tunnel and you eventually find yourself near a hostile enemy. You try and not make any sudden movements be he notices you before you can get out of the way. You find yourself in a fight. You can either fight him/her or come back some other time.'
                        print 'Narator: Just a suggestion, if you have less than 6 throwing rocks I would not reccomend attacking them just yet. Go buy some more or trade.'
                        print '\nYour choices:'
                        print '  (1)Fight Him/Her'
                        print '  (2)Come back later'
                        print 'Your weapons:'
                        print '  Throwing Rocks:',throwing_rocks
                        move_on=raw_input('Your choice: ')
                        clear()
                        start_attack()
                        if victory_status==True:
                            story_part6=False
                            story_part7=True
                            move_on=raw_input('Hit enter to exit: ')
                    if story_part7==True or repeat_chapters==True:
                        print 'After the encounter, you come across 3 more pathways, Left, Right, and Forward'
                        print' Left: Something shiny'
                        print' Right: Strange sound'
                        print' Forward: Sound of wind'
                        check = raw_input('Left, Right, or Forward').lower()
                        if check == 'left':
                            print('You go to the left, seeing a shiny spot down the path.')
                            print('Upon further inspection, you see that it is in fact a small piece of paper, caught in a ry of light.')
                            notes(1)
                            story_part7=False
                            story_part8=True
                        if check == 'forward':
                            print('You decide to follow the sound of the wind coming from the center path.')
                            print('As you continue down the path, you find a strange marking on the wall, that seems to be the source of the sound.')
                            print('You touch it, and find yourself in a small shop looking area.')
                            trade()
                            story_part7=False
                            story_part8=True
                        if check == 'right':
                            print('You decide to follow the strange noise coming from the right path.')
                            print('After walking a ways down the path, you come across a small pond, and spot a empty bottle on the bank of the pond.')
                            print('You fill it and put it in your inventory.')
                            story_part7=False
                            story_part8=True
                        print 'Moving down the passage...'
                        if dev==False:
                            time.sleep(2)
                    if story_part8==True or repeat_chapters==True:
                        print 'You feel compelled to take in your surroundings. Looking around and observing the details of the cave. The rough texture of the ichy walls. The imperfect shaping of the cave. Moss growing all around you. Dripping sounds from the sealling. Darkness surrounding you. You take all this in affect and accept that this is where you belong. Moving along the cave a sudden urge to rest arrisses and forces you to slow your every thought. Eventually putting you to sleep...'
                        print '\nSleeping...'
                        time.sleep(4.5)
                        print 'A glimmering light awakes your eyes. The thoughts of safety awake your every movement. Moving closer to it finding a loot crate. Sadness shows in your eyes. No rescue was here but there was some good stuff. The chest opens and the items are grabbed. Eventually moving farther into the tunnel.'
                        loot_crate(3)
                        move_on=raw_input('Hit enter to keep moving: ')
                        print 'Moving down the passage...'
                        time.sleep(4)
else:
    print 'wrong password'