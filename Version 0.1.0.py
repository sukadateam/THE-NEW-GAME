# -*- coding: utf-8 -*-
import os
#Settings
all_chapters_unlocked=True
repeat_chapters=False
normal_clear=True
repeat_amount=25
chars_in_line=55
run_off=True
error_message=True
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
print 'Password: 123456'
password=raw_input('Enter password: ')
clear()
if password=="123456":
    if all_chapters_unlocked==True:
        begin=True
        story_part1=True
        story_part2=True
        story_part3=True
        story_part4=True
        story_part5=True
        story_part6=True
    if all_chapters_unlocked==False:
        begin=False
        story_part1=False
        story_part2=False
        story_part3=False
        story_part4=False
        story_part5=False
        story_part6=False
        story_part7=False
    working_battery_charger=False
    skip=False
    sticks=0
    coal=0
    computer_chips=0
    wires=0
    battery_charger=False
    good_batteries=5
    bad_batteries=0
    battery=5
    throwing_rocks=10
    torches=25
    torch_use=False
    flashlight_use=False
    throwing_rocks_use=False
    no_light=False
    menu_open=False
    bag_open=False
    start=False
    def updates():
        print 'Current Version 0.1.0:'
        print '1. You can no longer charge batteries if you have non that are currently discharged.'
        print '2. You can no longer change batteries if you don\'t have any that are charged.'
        print '3. skip_story is now skip_intro. This appears in app startup.'
        print '4. Created another chapter to the story. This is chapter 4.'
        print '5. Added a new option so user can see improvements to the application.'
        print '6. Added a new option so user can see their unlocked chapters.'
        print '7. Added a new option so user can change and tweak setting if a problem occurs or for their personal preference.'
        print '8. Fixed a couple of grammatical errors.'
        print
        print 'Dev updates:'
        print '1. Updated help_menu. Now has an option to tell the user how to solve a problem.'
        print '2. Added story_part6 and story_part7.'
        print '3. Implemented all_chapters_unlocked.'
        print '4. Implemented repeat_chapters. Experimental version.'
        print 
        print 'Future updates:'
        print '1. Exploring will drain your battery over time.'
        print '2. Adding a new setting to stop letters from going off the screen.'
        skip = raw_input('Hit enter to exit:')
    def chapters():
        print 'True=Unlocked, False=Locked'
        print 'Intro:',str(begin)
        print 'Chapter 1:',str(story_part1)
        print 'Chapter 2:',str(story_part2)
        print 'Chapter 3:',str(story_part3)
        print 'Chapter 4:',str(story_part4)
        print 'Chapter 5:',str(story_part5)
        print 'Chapter 6:',str(story_part6),'--Not yet implemented'
        skip = raw_input('Hit enter to exit:')
    def settings():
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
        print 'Print Repeat Info:'
        print ' Current Value:',repeat_amount
        print '(4)Change Print Repeat Value'
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
            try:
                repeat_amount=int(raw_input('What is the new value:'))
            except ValueError:
                if error_message==True:
                    print 'System message: ValueError'
                    print 'Reason: A number was not entered.'
                    print 'Please wait 2.5 seconds.'
                    skip=raw_input('Hit enter to continue:')
                    skip=''
    def open_menu():
        global menu_open, battery_charger, wires, computer_chips, working_battery_charger, good_batteries, bad_batteries
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
                        if bad_batteries<1:
                            print 'You don\'t have any discharged batteries'
                    if working_battery_charger==False:
                        print 'You need to make the battery charger.'
    def starting_stuff():
        global good_batteries, bad_batteries, battery, torches, flashlight, throwing_rocks
        #Reset of variables
        good_batteries=5
        bad_batteries=0
        battery=100
        bag_open=True
        #Adding some new characteristics
        flashlight=False
    def help_menu():
        global torches
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
    def count():
        print ('10%')
        time.sleep(.2)
        clear()
        print ('20%')
        time.sleep(.2)
        clear()
        print ('30%')
        time.sleep(.2)
        clear()
        print ('40%')
        time.sleep(.2)
        clear()
        print ('50%')
        time.sleep(.2)
        clear()
        print ('60%')
        time.sleep(.2)
        clear()
        print ('70%')
        time.sleep(.2)
        clear()
        print ('80%')
        time.sleep(.2)
        clear()
        print ('90%')
        time.sleep(.2)
        clear()
        print ('100%')
        time.sleep(.2)
        clear()
    def open_bag():
        global good_batteries, bad_batteries, bag_open, battery, torches, throwing_rocks, flashlight_use, torch_use, throwing_rocks_use,wires
        if bag_open == False:
            bag_open=True
            print '\nGame: While in your backpack type the number of the item to use it.'
            print 'Game: For this item we will switch the batteries\n'
            time.sleep(3)
        print '(1)Good Batteries: '+str(good_batteries)
        print '(2)Bad Batteries: '+str(bad_batteries)
        print '(3)Torch: '+str(torches)
        print '(4)Flashlight: '+str(battery)
        print '(5)Throwing_rocks: '+str(throwing_rocks)
        print '(6)Collectable items'
        check = str(raw_input('\nType (leave) or enter item number to use: '))
        if check == "6":
            if battery_charger==True:
                print '(1)Battery charger:',str(battery_charger)
                print '(2)Wires:',str(wires)
                print '(3)Computer chips:',str(computer_chips)
                print '(4)Sticks:',str(sticks)
                print '(5)Coal:',str(coal)
        if check == "5":
            throwing_rocks_use=True
            throwing_rocks-=1
        if check == "4":
            flashlight_use=True
            battery-=5
        if check == "3":
            torches-=1
            torch_use=True
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
        if check == "2":
            print 'Those are no good for now. Try again later.'
        if check == "leave":
            print 'Moving you on'
    def battery_bag():
        global battery
        print 'Battery: '+str(battery)
    import time
    print 'Skip setup -- (skip)'
    name=raw_input('Hello user, Enter your name').lower()
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
        print 'Narrator: You\'ve been nocked out.'
        time.sleep(2)
        print 'Checking all systems...'
        count()
        time.sleep(.4)
        print 'All systems check'
        time.sleep(2)
        clear()
        loop=True
        while loop==True:
            print'(Yes/No) Narrator: Are you okay: '
            check=raw_input().lower()
            if check == "yes":
                print 'Narrator: That\'s good to hear.'
                loop=False
            if check == "no":
                print 'Narrator: Well, um, you will get through it.'
                loop=False
        time.sleep(1.5)
        print 'System: Emergency, power supply running low!'
        print 'Battery: '+str(battery)
        time.sleep(1.2)
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
        time.sleep(2)
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
        while loop==True:
            print 'Okay now, to see app improvements type (updates).'
            check = raw_input('Game: Check the updates for this version:')
            if check == "updates" or check == "update":
                clear()
                updates()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        loop=True
        while loop==True:
            print 'To see locked and unlocked chapters type (chapters).'
            check = raw_input('Game: Check your unlocked chapters:')
            if check == "chapters" or check == "chapter":
                clear()
                chapters()
                loop=False
            else:
                print 'I didn\'t understand that. Say again...'
        loop=True
        while loop==True:
            print 'To change settings to your preference type (settings)'
            check = raw_input('Game: Open the settings page:')
            if check == "setting" or check == "setting":
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
        print 'Narrator: Oh, i\'m back. Thank god.'
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
    check = raw_input('Enter password or hit enter: ')
    if check == "123456":
        start=True
        clear()
    if start==False:
        print 'Sorry, but you do not have access to the full game right now. Please ask for access if trying to get in.'
        print 'If this is a mistake, then enable this through the developer options. Or enter the code.'
        print 'You may exit the game.'
        loop=True
        while loop==True:
            pass
    if start==True:
        loop=True
        while loop == True:
            starting_stuff()
            loop=True
            while loop == True:
                print 'Your options:'
                print '(bag) (%) (start)'
                print '(hints) (menu)'
                print '(chapters) (updates)'
                check = raw_input('Choose an option: ').lower()
                clear()
                if check == "chapters" or check == "chapters":
                    chapters()
                if check == "updates" or check == "update":
                    updates()
                if check == "menu":
                    open_menu()
                if check == "bag":
                    open_bag()
                if check == "%":
                    battery_bag()
                if check == "hints":
                    print 'HINT: Taking left or right will lead you to the same place but you will gather different items'
                    print 'HINT: Taking a left takes 4 seconds to complete, a right takes 6 seconds to complete, forward is unknown'
                    print 'HINT: Traps take 50 of your energy'
                    print 'HINT: If your energy hits 0% you are forced to leave the cave'
                    print 'HINT: A special passage has a chance to give you 25 energy'
                    print 'HINT: Every time you leave you must restart your adventure. You will not loose you stuff.'
                    print 'HINT: Leave cave and go back the ways you didn’t to make sure you have everything'
                    print '\nWhen you see this (*) you are allowed to type (bag) or (menu).'
                if check == "start":
                    if begin == False:
                        print 'You’re first day of exploring is going to be your best. You enter'
                        print 'the cave and see that there are 2 sides to it. You can either go left'
                        print 'or you can go right. Which do you choose?'
                        print '\n'
                        battery_bag()
                        check = raw_input("(*)Left or Right: ").lower()
                        if check == "menu":
                            open_menu()
                        if check == "bag":
                            open_bag()
                        if check == "left":
                            clear()
                            print 'You take a left turn. You head straight for some time. While'
                            print 'doing so, you find a battery charger. It looks like it might'
                            print 'come in handy. But we can’t use it till we find some parts.'
                            print 'Lets keep looking.'
                            battery_charger=True
                            print '\nMoving through the mines...'
                            time.sleep(4)
                            story_part1=True
                        if check == "right":
                            clear()
                            print 'You make a right turn. You head straight for some time. While'
                            print 'doing so, you find a wire on the ground. I looks like it might'
                            print 'be used for a battery charger, but I’m not sure. Keep exploring'
                            print 'to find more things.'
                            wires+=1
                            print '\nMoving through the mines...'
                            time.sleep(4)
                            story_part1=True
                    begin=True
                if story_part1==True:
                    if story_part2==False or repeat_chapters==True:
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
                            time.sleep(7.5)
                            story_part2=True
                        if check == "left":
                            clear()
                            print 'You take a left and there seems to be nothing here. You keep going through.'
                            print '\nMoving through the mines...'
                            time.sleep(4)
                            story_part2=True
                        if check == "right":
                            clear()
                            print 'You take a right and you walk for a bit. You look around and you see a battery'
                            print 'charger on the wall. It looks like it has power. You charge your current battery.'
                            print 'Your energy increases by 25%. You walk through the rest of the way.'
                            print '\nMoving through the mines...'
                            time.sleep(6)
                            story_part2=True
                            battery+=25
                if story_part2==True:
                    if story_part3==False or repeat_chapters==True:
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
                            time.sleep(3)
                            story_part3=True
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
                            time.sleep(3)
                            story_part3=True
                            computer_chips+=1     
                if story_part3==True:
                    if story_part4==False or repeat_chapters==True:
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
                            time.sleep(4)
                            story_part4=True
                        if check == "right":
                            print 'You walk down the cave and find a stick on the ground. It seems to have a shape'
                            print 'of a torch. But we can’t make a torch without coal. So you pick it up thinking'
                            print 'it\’s useless but in hopes it will come in handy.'
                            print '\nMoving through the mines...'
                            time.sleep(6)
                            story_part4=True
                            sticks+=1
                if story_part4==True:
                    if story_part2==False or repeat_chapters==True:
                        print 'There doesn\'t seem to be an end to this passage. Maybe if we continue forward'
                        print 'we will eventually find something.' 
                        print 'Moving down the passage...'   
                        time.sleep(6.5)
                        print 'You have been walking the same way for a while now. You feel like it will never end...'   
                        print 'Moving down the passage...'
                        time.sleep(6.5)
                        print 'You eventually stumble apon an item laying on the ground. You pick it up and it'
                        print 'appears to be 2 fully charged batteries.'
                        good_batteries+=2
                        time.sleep(5)
                        print '\nMoving through the mines...'
                        story_part5=True
                if story_part5==True:
                    if story_part6==False or repeat_chapters==True:
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
                            battery_charger=True
                        if check == "straight":
                            print 'You head straight and find 2 wires. You pick them up and put them away, then you continue your adventure.'
                            wires+=2
                            print 'Moving down the passage...'
                            story_part6=True
                if story_part6==True:
                    print 'This chapter is not yet completed.'
else:
    print 'wrong password'