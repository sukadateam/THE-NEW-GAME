#c:\Python27\python.exe "Version 0.2.9.py"
# -*- coding: utf-8 -*-
import os, random, time, sys
try:
    n = list(sys.argv)
    print ('Argument:',n[1])
    time.sleep(1)
except:
    pass
#Game setup
path='\\Users\\brobi\\Desktop\\Current_Version'
os.chdir(path)
version = '0.2.9'
story_amount=12
#possible inputs
bag_input=['bag','bags','storage','backpack','purse']
start_input=['start','begin','commence']
menu_input=['menu','home','home menu','title','title screen']
hints_input=['hints','hint','info']
battery_input=['%','battery','battery percent','percent']
update_input=['updates','update','bugs','patch notes','release note','patch release notes']
chapter_input=['chapters','chapter','story','stories']
settings_input=['settings','setting','options','option']
damage_input=['damage','damage dealt']
shop_input=['shop','trade','sell','buy','trading center']
battle_input=['battle','fight']
awards_input=['award','awards','achievements']
gems_input=['gems','gem','gem collection']
save_input=['save','keep']
load_input=['load','stock','fill']
dev_mode_input=['dev mode','dev_mode','developer mode']
dev_battle_input=['dev battle','developer battle']
dev_edit_chapter=['dev edit_chapters','developer edit_chapters','dev edit chapters','developer edit chapters']
load_settings_input=['load settings.dev', 'load settings']
sleep_input=['sleep','tired','sleeping','rest','nap','slumber','doze','snooze']
clear_cache_input=['clear cache','remove cache','erase cache']
stats_input=['stats','stat','statistics','information','figures']
exit_dev_mode_input=['exit dev mode','exit developer mode']
practice_input=['practice','test','work out','exercise']
load_beta_vars_input=['load beta vars','load beta var']
calendar_input=['calendar','days','day']
time_travel_input=['time travel']
buildings_input=['building','buildings']
generators_input=['generator','generators','power','energy']
show_all_vars_input=['show all vars','show all var','show all variables','show all variable']
var_count_input=['var count','vars count','variables count','variable count']
edit_var_input=['edit var','edit vars','edit variable','edit variables']
yes_input=['yes','y','correct',"that's right",'yup','indeed','sure','of course','yah']
no_input=['no','nope','negative','nah','naw','nay','no way','nae','never','not at all','by no means']
error_message_skip=False
try:
    from error_stuff import *
except:
    error_message_skip=True
#Important --- Important
save_not_found=False
works=False
try:
    os.rename("Save.py","Save.gsf")
except:
    pass
try:
    os.remove('Save.pyc')
except:
    pass
try:
    load=open('Save.gsf','r')
    load.close()
    works=True
except:
    print("Could not find a save file with the extension: .gsf")
    print('Current Path:',path)
if works==True:
    os.rename("Save.gsf","Save.py")
    from Save import version_save
    if version_save not in version:
        print('This save file is not compatible with this version.')
        os.rename("Save.py","Save.gsf")
    if version_save == version:
        from Save import *
        os.rename("Save.py","Save.gsf")
        try:
            os.remove("Save.pyc")
        except WindowsError:
            pass
def show_error():
    if error_message==True:
      print('\n\n\n-------------(ERROR)-------------')
      ex, ex_value, ex_traceback = sys.exc_info()
      ex=str(ex)
      ex=ex[8:len(ex)-2]
      if ex=="ValueError": value_error(ex_value)
      elif ex=="WindowsError": windows_error(ex_value)
      elif ex=="KeyboardInterrupt": keyboard_interrupt()
      elif ex=="NameError": name_error(ex_value)
      elif ex=="MemoryError": memory_error()
      elif ex=="AssertionError": assertion_error(ex_value)
      elif ex=="AttributeError": attribute_error(ex_value)
      elif ex=="EOFError": eof_error()
      elif ex=="ImportError": import_error(ex_value)
      elif ex=="ModuleNotFoundError": module_not_found(ex_value)
      elif ex=="IndexError": index_error(ex_value)
      elif ex=="KeyError": key_error(ex_value)
      elif ex=="OverflowError": over_flow_error(ex_value)
      elif ex=="IndentationError": indentation_error(ex_value)
      elif ex=="TabError": tab_error(ex_value)
      elif ex=="SystemError": system_error(ex_value)
      else: unknown_error(ex_value)
      move_on=input('Hit enter to exit: ')
if works==False:
    save_not_found=True
    print('A save file is required to continue.')
    print('Would you like to create one')
    choice=input('Yes or No: ').lower()
    if choice == "yes" or choice == "y":
        clear()
        print('This game cannot create one yet from nothing. If you need a save file please visit my github.')
        print('A fix for this is comming soon. Please be patient.')
        print('github.com/sukadateam/THE-NEW-GAME')
        input('Hit enter to quit: ')
        print('The game will now give an error.')
        time.sleep(3)
        close
    else:
        print('Sorry. You cannot continue. The game will now give an error.')
        time.sleep(3)
        close
if save_not_found==True:
    #Settings
    skip_check=True
    dev=False
    unlock_all_achievements=False
    repeat_chapters=False
    normal_clear=False
    repeat_amount=50
    chars_in_line=55
    run_off=True
    error_message=True
    allow_older_savefile=False
    #Days
    day_lock1=False
    day_lock2=False
    day_lock3=False
    day_lock4=False
    day_lock5=False
    day_lock6=False
    day_lock7=False
    day_lock8=False
    day_lock9=False
    day_lock10=False
    day_lock11=False
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
    story_part9=False
    story_part10=False
    story_part11=False
    story_part12=False
    #Cave cords
    cave_cord1=['52, 61, 30', False] #Lost person
    #Save file extension (gsf) = Game Save File
class variables():
    def show_buy():
        try:
            global buy_count, current_vars
            list_show=[]
            a=0
            for i in range(buy_count):
                p=True
                while p==True:
                    x=current_vars[a]
                    b=len(x)
                    n=x[b-4:b]
                    if n == "_buy":
                        print (x)
                        p=False
                    a+=1
        except:
            show_error()
    def show_sell():
        try:
            global sell_count, current_vars
            list_show=[]
            a=0
            for i in range(sell_count):
                p=True
                while p==True:
                    x=current_vars[a]
                    b=len(x)
                    n=x[b-5:b]
                    if n == "_sell":
                        print (x)
                        p=False
                    a+=1
        except:
            show_error()
    def story(output):
        global current_vars,story_amount
        a=0
        full=False
        output.append('begin')
        b=1
        p=True
        while p==True:
            c='story_part'+str(b)
            for i in range(len(current_vars)):
                if a>len(current_vars)-1:
                    a=0
                    b+=1
                if b>story_amount:
                    p=False
                if current_vars[a]==c:
                    output.append(c)
                    b+=1
                    a=0
                    break
                else:
                    a+=1
                if i==len(current_vars):
                    full=True
            if full==True:
                p=False
    def remove(var,sub):
        try:
            globals()[var]-=sub
        except:
            pass
    def add(var,add):
        try:
            globals()[var]+=add
        except:
            pass
    def edit(var,other):
        globals()[var]=other
        print(var,'=', globals()[var])
    def clean_vars():
        global current_vars, count_vars
        try: current_vars.remove('__annotations__')
        except: pass
        try: current_vars.remove('__builtins__')
        except: pass
        try: current_vars.remove('__cached__')
        except: pass
        try: current_vars.remove('__doc__')
        except: pass
        try: current_vars.remove('__file__')
        except: pass
        try: current_vars.remove('__loader__')
        except: pass
        try: current_vars.remove('__name__')
        except: pass
        try: current_vars.remove('__package__')
        except: pass
        try: current_vars.remove('__spec__')
        except: pass
        try: count_vars=len(current_vars)
        except: pass
    def show():
        global count, current_vars
        print('Vars count: ',count_vars)
        print (current_vars)
    def convert(var):
        print ('(1)str\n(2)int\n(3)float\n(4)bool')
        choice=input('Choose a conversion: ')
        if choice == "str" or choice == '1':
            try:
                var=str(var)
            except:
                print('System: Conversion could not be completed.')
        if choice == "int" or choice == '2':
            try:
                var=int(var)
            except:
                print('System: Conversion could not be completed.')
        if choice == "float" or choice == '3':
            try:
                var=float(var)
            except:
                print('System: Conversion could not be completed.')
        if choice == "bool" or choice == '4':
            try:
                var=bool(var)
            except:
                print('System: Conversion could not be completed.')
    def explain():
        global current_vars,count_count_vars
        for i in range(count_vars):
            print(current_vars[i],'=',globals()[current_vars[i]])
def updates():
    print('Current Version 0.2.9')
    print('1. Converted code from python 2 to python 3.')
    print('2. Added extra chapters to chapters page.')
    print('3. Added exceptions incase settings.dev is messed up.')
    print('4. Added 2 new weapons. Frying pans and Daggers.')
    print('5. Fixed a problem where shop would give the wrong item name on your receipt after selling something.')
    print('6. Updated save function with new variables.')
    print('7. Updated damage function with new weapons.')
    print('8. Updated shop with new weapons.')
    print('9. Updated sleep with new prices.')
    print('10. Working on making functions more adaptive for new items. Easier to introduce new items and requires less code to do so.')
    print('11. Fixed several problems with the bag.')
    print('12. Shop is now adaptive to easily add new items. Other function to do the same are on the way.')
    print('13. Added several new functions which will be worked on through out the game. No designated time for completion yet.')
    print('14. Added a new developer tool. This one is a fun one.')
    print('15. Added new ways to use certian functions.')
    print('16. Chapters function is now adaptive.')
    print('17. Removed dev lock on save and load functions.')
    print('18. Implemented error_stuff.py file into program.')
    print('')
    print('Things to do next: ')
    print('1. Decide if possible inputs stays in this file or gets moved to another file.')
    print('2. Find a use for command arguments.')
    print('3. Add buy_count and sell_count to create new save')
    skip = input('Hit enter to exit:')
def next_update():
    print('Things to do for update Version 0.2.8:')
    print('1. Think a gem trades. And maybe add them in. Not a big priority.')
    print('2. Talk about how the the collisseum will work. Will be accesed only through dev mode.')
    print('3. Either rewrite hints or delete it.')
    print('')
    print('Optional Stuff:')
    print('1. Check for any spelling errors or mistakes.')
    print('2. Come up with ideas for weapons in the game.')
    print('3. Make a list of new features to add in the game.')
    print('4. Add a setting to allow users to load a save file from a different version.')
def edit_chapters():
    global story_part1,story_part2,story_part3,story_part4,story_part5,story_part6,story_part7,story_part8,story_part9,story_part10,story_part11,story_part12,begin
    print('True = Unlocked')
    print('False = Locked')
    print('(1)Begin:',str(begin))
    print('(2)Chapter 1:',str(story_part1))
    print('(3)Chapter 2:',str(story_part2))
    print('(4)Chapter 3:',str(story_part3))
    print('(5)Chapter 4:',str(story_part4))
    print('(6)Chapter 5:',str(story_part5))
    print('(7)Chapter 6:',str(story_part6))
    print('(8)Chapter 7:',str(story_part7))
    print('(9)Chapter 8:',str(story_part8))
    print('(10)Chapter 9:',str(story_part9))
    print('(11)Chapter 10:',str(story_part10))
    print('(12)Chapter 11:',str(story_part11))
    print('(13)Chapter 12:',str(story_part12))
    choice=input('What number: ')
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
    if choice == "10":
        hi=True
        if story_part9==True:
            story_part9=False
            hi=False
        if story_part9==False:
            if hi==True:
                story_part9=True
    if choice == "11":
        hi=True
        if story_part10==True:
            story_part10=False
            hi=False
        if story_part10==False:
            if hi==True:
                story_part10=True
    if choice == "12":
        hi=True
        if story_part11==True:
            story_part11=False
            hi=False
        if story_part11==False:
            if hi==True:
                story_part11=True
    if choice == "13":
        hi=True
        if story_part12==True:
            story_part12=False
            hi=False
        if story_part12==False:
            if hi==True:
                story_part12=True
def settings():
    for i in range(5):
        print()
    global normal_clear, run_off, error_message, repeat_amount,chars_in_line,allow_older_savefile
    if normal_clear==True:
        print('(1)Normal Screen Clean: Clear')
    if normal_clear==False:
        print('(1)Normal Screen Clean: Print Repeat')
    if run_off==True:
        print('(2)Screen Run Off Value:',chars_in_line,', Enabled')
    if run_off==False:
        print('(2)Screen Run Off Value:',chars_in_line,', Disabled')
    if error_message==True:
        print('(3)Error Messages: Enabled')
    if error_message==False:
        print('(3)Error Messages: Disabled')
    if allow_older_savefile==True:
        print('(4)Allow Older Save File: Enabled')
    if allow_older_savefile==False:
        print('(4)Allow Older Save File: Disabled')
    print('(5)Change File Path')
    print('(6)Change Print Repeat Value')
    print('\nCurrent Save File Path:')
    print('    Directory:',path)
    print('Print Repeat Info:')
    print('   Current Value:',repeat_amount)
    check = input('Choose a setting to change:')
    if check == "1":
        hi=True
        if normal_clear==True:
            normal_clear=False
            hi=False
        if normal_clear==False:
            if hi==True:
                normal_clear=True
    if check == "2":
        print('(1)Change Value\n(2)Enable/Disable')
        choice = input("Choose one: ")
        if choice == "1":
            try:
                chars_in_line=int(input('What is the new value: '))
            except:
                show_error()
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
        hi=True
        if allow_older_savefile==True:
            allow_older_savefile=False
            hi=False
        if hi==True:
            allow_older_savefile=True
    if check == "5":
        print('Enter your desired directory:')
        try:
            os.chdir(input('Directory: '))
        except:
            show_error()
        print(os.getcwd())
    if check == "6":
        try:
            repeat_amount=int(input('What is the new value:'))
        except:
            show_error()
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
            else:
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
            print('')
def sleep(num):
    global dev
    if dev==False:
        time.sleep(num)
if dev==True:
    clear()
    no1=False
    no2=False
    try:
        os.rename('settings.dev','settings.py')
        from settings import *
    except:
        no1=True
    try:
        os.rename('settings.py','settings.dev')
    except:
        pass
    if no1==True:
        try:
            os.rename('settings.dev','settings.py')
            from settings import *
            os.rename('settings.py','settings.dev')
        except:
            pass
    try:
        os.remove('settings.pyc')
    except:
        clear()
    print('(1)Quick Settings')
    print('(2)Version Info')
    print('(3)Update Info')
    print('(4)Edit chapters')
    print('(5)Settings.dev')
    help=input('Choose an option or hit enter: ')
    if help == "1":
        settings()
    if help == "2":
        print (version)
    if help == "3":
        updates()
    if help == "4":
        edit_chapters()
    if help == "5":
        try:
            clear()
            print('Test Battle:',str(dev_battle))
            print('Edit Chapters:',str(dev_edit_chapters))
            print('Free Stuff:',str(dev_give_stuff))
            print('Name of Dev:',name)
            print('Beta var:',str(beta_var))
            print('Skip check:',str(skip_check))
            move_on=input("Hit enter to exit: ")
        except:
            pass
try:
    if beta_var==True:
        try:
            from beta_vars import *
        except:
            pass
except:
    pass
clear()
password='123456'
if password=="123456":
    if save_not_found==True:
        #Others
        battery_charger=False
        flashlight=False
        enemy=['Goblin','Karen','Bat','Skeleton','Zombie','Put Name Here','Crab Rave','No Cell Service','Gertie','Jimmy','Gage']
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
        frying_pan=0
        dagger=0
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
        frying_pan_damage=[11,15]
        dagger_damage=[17, 23]
        #Item Usage
        flashlight_use=False #When true, user is using the item.
        throwing_rocks_use=False #When true, user is using the item.
        pickaxe_use=False #When true, user is using the item.
        machete_use=False #When true, user is using the item.
        spears_use=False #When true, user is using the item.
        torch_use=False #When true, user is using the item.
        frying_pan_use=False #When true, user is using the item.
        dagger_use=False #When true, user is using the item.
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
        buy_count=13
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
        frying_pan_buy=0
        dagger_buy=0
        #Sell
        sell_count=13
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
        frying_pan_sell=0
        dagger_sell=0
        #Achievements
        if unlock_all_achievements==False:
            let_the_battles_begin=False
            guts_and_glory=False
            i_have_the_power=False
            its_payday=False
            whicked_chronicle=False
            keep_it_moving=False
        if unlock_all_achievements==True:
            let_the_battles_begin=True
            guts_and_glory=True
            i_have_the_power=True
            its_payday=True
            whicked_chronicle=True
            keep_it_moving=True
    clear()
    def level_check():
        global xp, level
        try:
            check=False
            while xp>49:
                level+=1
                xp-=50
                check=True
            if check==True:
                print('Level increased.')
                time.sleep(3)
        except:
            print('System: Unabled to check level.')
    def stats():
        global dev, level, xp, strength
        if dev==True:
            global beta_var, level, xp
            print('Player Level:',str(level))
            print('Current XP:',str(xp))
            print('Player Strength: ',str(strength))
            move_on=input('Hit enter to exit: ')
        if dev==False:
            non_function()
    def clear_cache():
        global dev
        if dev==True:
            try:
                os.remove('settings.pyc')
                print('System: Removed settings.pyc file')
            except:
                print('System: settings.pyc file could not be found.')
            try:
                os.remove('Save.pyc')
                print('System: Removed Save.pyc file')
            except:
                print('System: Save.pyc file could not be found.')
            move_on=input('Hit enter to exit: ')
    def collisseum():
        global custom_attack, current_enemy, health
        custom_attack=True
        print("Welcome to the Battle Arena.")
        print('Your Rules. Your Game. Your Power.')
        print('Good luck soldier!')
        print()
        try:
            health=int(input('How much health does the enemy have: '))
        except:
            show_error()
        current_enemy=input('What will the enemies name be: ')
        clear()
        start_attack()
        custom_attack=False
        move_on=input('Hit enter to exit: ')
    def loot_crate(number):
        global sticks, throwing_rocks, torches, spears, good_batteries, bad_batteries, pickaxe, machete
        if number == 1:
            print('You got 4 sticks and 1 throwing rock.')
            sticks+=4
            throwing_rocks+=1
        if number == 2:
            print('You got 2 torches.')
            torches+=2
        if number == 3:
            print('You got 1 spear and 2 throwing rocks.')
            spears+=1
            throwing_rocks+=2
        if number == 4:
            print('You got 2 good batteries and 2 bad batteries.')
            good_batteries+=2
            bad_batteries+=2
        if number == 5:
            print('You got 1 pickaxe.')
            pickaxe+=1
        if number == 6:
            print('You got 1 machete and 2 throwing rocks.')
            machete+=1
            throwing_rocks+=2
    def gem_collection():
        global red_gem, green_gem, magenta_gem, yellow_gem, blue_gem
        print('Red:',red_gem)
        print('Green:',green_gem)
        print('Magenta:',magenta_gem)
        print('Yellow:',yellow_gem)
        print('Blue:',blue_gem)
        move_on=input('Hit enter to exit: ')
        clear()
    def achieve():
        global let_the_battles_begin, guts_and_glory, i_have_the_power, its_payday, whicked_chronicle
        print('(1)Check for pending achievements')
        print('(2)See your earned achievements')
        choice = input('1 or 2: ')
        if choice == "1":
            print('Checking for awards...')
            sleep(1)
            if total_wins>0:
                let_the_battle_beggin=True
            elif money>19.99:
                its_payday=True
            elif seen_notes>0:
                whicked_chronicle=True
            else:
                print('You unlocked no new rewards.')
        if choice == "2":
            clear()
            if let_the_battles_begin==True:
                print('Let The Battles Begin: Win your first battle')
            if let_the_battles_begin==False:
                print('???: Win your first battle')
            print('')
            if guts_and_glory==True:
                print('Guts and Glory: Unlock the Collisseum')
            if guts_and_glory==False:
                print('???: Unlock the Collisseum')
            print('')
            if i_have_the_power==True:
                print('I Have The Power: Charge a battery')
            if i_have_the_power==False:
                print('???: Charge a battery.')
            print('')
            if its_payday==True:
                print("It's Payday Fellas!: Gain a total of 20$")
            if its_payday==False:
                print('???: Gain a total of 20$')
            print('')
            if whicked_chronicle==True:
                print('Wicked Chronicle: Discover a note in the caves')
            if whicked_chronicle==False:
                print('???: Discover a note in the caves')
            print('')
            if keep_it_moving==True:
                print('Keep it moving: Unlock chapter 10')
            if keep_it_moving==False:
                print('???: Unlock chapter 10')
            print('')
        move_on=input('Hit enter to exit: ')
        clear()
    def notes(number):
        global seen_notes
        seen_notes+=1
        if number==1:
            print("It's been three weeks since I've seen the day of light. I'm starting to lose my grip on reality. Food and water are hard to come by. I don't know how much longer I will survive. I'm sorry for what I did... Please Spare me!")
        if number==2:
            print("Day 22: I often find myself wondering about what has become of my family while I've been gone. This damned journey was a fool's errand from the start.")
        if number==3:
            print("Day 24: I found a strange environment today, a whole area of this cave covered head to toe in moss. Not super interesting, but unusual.")
        if number==4:
            print("Day 25: A small creature scurried past my feet today, seemingly able to speak, as I heard it say something about donuts as it hurried in the opposite direction of me. I tried to get its attention, but it seemed to be unable to hear me, or simply ignoring me.")
        if number==5:
            print("Day 26: Today might have been the worst day yet. This shambling monstrosity attacked me, and I was forced to fight it off with my bare hands. Future reference, find rocks or something of the sort to throw at creatures in the future.")
        if number==6:
            print("You: Commander this is agent 7. We need backup. I repeat! WE NEED BACKUP! Can you hear me, commander?...")
            print("Commander: Yis Io CaN, meeat uus at the bassee...")
            print("Narrator: Silence fills the air.")
            print("You: Sir! Sir! Looks like we are on our own.")
        if number==7:
            print("I finally created a device to be able to help us coordinate these tunnels. This will help us get out.")
        if number==8:
            print("I'm experiencing problems with the device. It won't turn on anymore. It seems to have lost charge. If I can find any way of charging it then I could escape.")
        if number==9:
            print("There is no way of charging this device. I give up! I will keep this device hidden in a loot_crate. Hopefully, this will help someone one day.")
        if number==10:
            print("I have been in here for 100 days. There is no way out. Please, anyone, who finds these notes come to save me. Again my coordinates are 52, 61, 30.")
    def trade():
        global good_batteries, battery_charger, spears, throwing_rocks
        print('Your trading options:')
        print('(1) 1 battery charger = 5 good batteries')
        print('(2) 4 throwing rocks = 1 spear')
        choice = input('What are your trading: ')
        if choice == "1":
            if good_batteries<5:
                print('You don\'t have enough charged batteries')
            if good_batteries>4:
                print('You got 1 battery charger.')
                battery_charger=True
                good_batteries-=5
        if choice == "2":
            if spears<1:
                print('You don\'t have enough spear(s)')
            if spears>0:
                print('You got 4 throwing rocks.')
                throwing_rocks+=4
                spears-=1
    def non_function():
        clear()
        print('This function has not yet been implemented. Sorry for the inconvience.')
        print('If this is an error please contact me via github. Thank You!')
        move_on=input('Hit enter to exit: ')
    def shop():
        global current_vars
        global frying_pan_buy, frying_pan_sell, frying_pan, dagger_buy, dagger_sell, dagger, red_gem, green_gem, magenta_gem, yellow_gem, blue_gem, pickaxe_sell, machete_sell, pickaxe, machete, i_have_the_power, battery_charger, coal_sell, wires_sell, sticks_sell, spears_sell, torches_sell, computer_chips_sell, good_batteries_sell, bad_batteries_sell, throwing_rocks_sell, money, coal, wires, sticks, spears, torches, good_batteries, bad_batteries, computer_chips, throwing_rocks, battery
        print('Welcome to My shop.')
        print('\n(1)Sell\n(2)Trade\n(3)Buy\n(4)Charge Battery\n(5)Gems\n(6)Leave')
        choice = input('What are you looking to do: ')
        if choice == "1":
            clear()
            print('System: Price is per item. Not for the total.')
            print('Item:             Price:')
            print('(1)Coal:          ',coal_sell)
            print('(2)Wires:         ',wires_sell)
            print('(3)Sticks:        ',sticks_sell)
            print('(4)Spears:        ',spears_sell)
            print('(5)Torches:       ',torches_sell)
            print('(6)Computer Chips:',computer_chips_sell)
            print('(7)Good Batteries:',good_batteries_sell)
            print('(8)Bad Batteries: ',bad_batteries_sell)
            print('(9)Throwing Rocks:',throwing_rocks_sell)
            print('(10)Pickaxes:     ',pickaxe_sell)
            print('(11)Machete:      ',machete_sell)
            print('(12)Frying pans:  ',frying_pan_sell)
            print('(13)Daggers:      ',dagger_sell)
            print('\nYour Balance:',money,'Dollar(s)')
            error_some=False
            try:
                choice = int(input('What would you like to sell: '))
            except:
                show_error()
                error_some=True
            try:
                amount=int(input('How much would you like to sell: '))
            except:
                show_error()
                error_some=True
            list1=['coal','wires','sticks','spears','torches','computer_chips','good_batteries','bad_batteries','battery','throwing_rocks','pickaxe','machete','frying_pan','dagger']
            list2=['coal_sell','wires_sell','sticks_sell','spears_sell','torches_sell','computer_chips_sell','good_batteries_sell','bad_batteries_sell','throwing_rocks_sell','pickaxe_sell','machete_sell','frying_pan_sell','dagger_sell']
            clear()
            if error_some==False:
                save_amount=amount
                choice-=1
                if globals()[list1[choice]]>amount-1 and amount>0:
                    money+=globals()[list2[choice]]*amount
                    globals()[list1[choice]]-=round(save_amount)
                    globals()[list1[choice]]=round(globals()[list1[choice]])
                    money=round(money,2)
                    print('You now have:',globals()[list1[choice]],list1[choice])
                    print('Your current balance:',money)
                else:
                    print('You don\'t have enough',list1[choice])
            move_on=input('Hit enter to exit:')
        if choice == "3":
            clear()
            print('System: Price is per item. Not for the total.')
            print('Item:             Price:')
            print('(1)Coal:          ',coal_buy)
            print('(2)Wires:         ',wires_buy)
            print('(3)Sticks:        ',sticks_buy)
            print('(4)Spears:        ',spears_buy)
            print('(5)Torches:       ',torches_buy)
            print('(6)Computer Chips:',computer_chips_buy)
            print('(7)Good Batteries:',good_batteries_buy)
            print('(8)Bad Batteries: ',bad_batteries_buy)
            print('(9)Throwing Rocks:',throwing_rocks_buy)
            print('(10)Pickaxes:     ',pickaxe_buy)
            print('(11)Machete:      ',machete_buy)
            print('(12)Frying pans:  ',frying_pan_buy)
            print('(13)Daggers:      ',dagger_buy)
            print('\nYour Balance:',money,'Dollar(s)')
            error_some=False
            try:
                choice = int(input('What would you like to buy: '))
            except:
                show_error()
                error_some=True
            try:
                amount=int(input('How much would you like to buy: '))
            except:
                show_error()
                error_some=True
            list1=['coal','wires','sticks','spears','torches','computer_chips','good_batteries','bad_batteries','battery','throwing_rocks','pickaxe','machete','frying_pan','dagger']
            list2=['coal_buy','wires_buy','sticks_buy','spears_buy','torches_buy','computer_chips_buy','good_batteries_buy','bad_batteries_buy','throwing_rocks_buy','pickaxe_buy','machete_buy','frying_pan_buy','dagger_buy']
            clear()
            if error_some==False:
                save_amount=amount
                choice-=1
                if globals()[list2[choice]]*amount<money+0.01:
                    money-=globals()[list2[choice]]*amount
                    globals()[list1[choice]]+=round(save_amount)
                    globals()[list1[choice]]=round(globals()[list1[choice]])
                    money=round(money,2)
                    print('You now have:',globals()[list1[choice]],list1[choice])
                    print('Your current balance:',money)
                else:
                    print('You don\'t have enough money.')
            move_on=input('Hit enter to exit:')
        if choice == "2":
            clear()
            trade()
        if choice == "4":
            clear()
            print('Price Per Battery:',charge_price)
            print('Charged/Good Batteries:',good_batteries)
            print('Discharged/Bad Batteries:',bad_batteries)
            choice = input('How many batteries do you need to charge: ')
            try:
                clear()
                if int(choice)*charge_price>money:
                    print('You don\'t have enough money to charge',int(choice),'batteries.')
                if int(choice)>bad_batteries:
                    print('You don\'t have that many. You have',bad_batteries,'discharges batteries.')
                if int(choice)<bad_batteries+1:
                    if int(choice)*charge_price<money+0.01:
                        print('Charging...')
                        time.sleep(charge_time*int(choice))
                        good_batteries+=int(choice)
                        bad_batteries-=int(choice)
                        print('Charged',int(choice),'batteries. You now have',good_batteries,'charged batteries.')
                        time.sleep(2.5)
                        i_have_the_power=True
            except:
                show_error()
        if choice == "5":
            p=True
            while p==True:
                clear()
                print('What would you like to trade:')
                print('Note: 1 gem  =  1 item')
                print('\n(1)Red Gems  -- Spears\n(2)Green Gems -- Rocks\n(3)Magenta Gems -- Bad Batttery\n(4)Yellow Gems -- Good Battery\n(5)Blue Gems -- Machetes')
                choice = input('Which gem, (my gems) or (leave): ')
                if choice == "leave" or choice == "exit":
                    p=False
                if choice == "my gems" or choice == "my_gems" or choice == "gems":
                    clear()
                    gem_collection()
                if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
                    p=False
            if choice == "1":
                clear()
                if red_gem<1:
                    print('Insufficent gems for trade.')
                if red_gem>0:
                    print('You have',red_gem,'red gems')
                    choice = input('How many would you like to trade: ')
                    try:
                        if red_gem<int(choice):
                            print('You don\'t have thay many gems.')
                        if red_gem+1>int(choice):
                            spears+=int(choice)
                            red_gem-=int(choice)
                    except:
                        show_error()
            if choice == "2":
                clear()
                if green_gem<1:
                    print('Insufficient gems for trade')
                if green_gem>0:
                    print('You have',green_gem,'green gems.')
                    choice = input('How many would you like to trade:')
                    try:
                        if green_gem<int(choice):
                            print('You don\'t have that many gems.')
                        if green_gem+1>int(choice):
                            throwing_rocks+=int(choice)
                            green_gem-=int(choice)
                    except:
                        show_error()
            if choice == "3":
                clear()
                if magenta_gem<1:
                    print('Insufficient gems for trade')
                if magenta_gem>0:
                    print('You have',magenta_gem,'magenta gems')
                    choice = input('How many would you like to trade')
                    try:
                        if magenta_gem<int(choice):
                            print('You don\'t have enough gems')
                        if magenta_gem+1>int(choice):
                            bad_batteries+=1
                            magenta_gem-=1
                    except:
                        show_error()
            if choice == "4":
                clear()
                if yellow_gem<1:
                    print('Insufficient gems for trade')
                if yellow_gem>0:
                    print('You have',yellow_gem,'yellow gems.')
                    choice = input('How many would you like to trade')
                    try:
                        if yellow_gem<int(choice):
                            print('You don\'t have enough gems.')
                        if yellow_gem+1>int(choice):
                            good_batteries+=1
                            yellow_gem-=1
                    except:
                        show_error()
            if choice == "5":
                clear()
                if blue_gem<1:
                    print('Insufficent gems for trade')
                if blue_gem>0:
                    print('You have',blue_gem,'blue gems')
                    choice = input('How many would you like to trade:')
                    try:
                        if blue_gem<int(choice):
                            print('You don\'t have enoug gems.')
                        if blue_gem+1>int(choice):
                            machete+=1
                            blue_gem-=1
                    except:
                        show_error()
            choice = ''
            move_on=input('Hit enter to exit: ')
        if choice == "6":
            print('Have a Great day then! Hope to see you back.')
            time.sleep(1.5) #Adjust time as needed
        clear()
    def item_damage():
        global throwing_rocks_damage, spears_damage, pickaxe_damage, machete_damage
        print('Throwing Rocks: '+str(throwing_rocks_damage[0])+'-'+str(throwing_rocks_damage[1])+' HP')
        print('Spears: '+str(spears_damage[0])+'-'+str(spears_damage[1])+' HP')
        print('Pickaxe: '+str(pickaxe_damage[0])+'-'+str(pickaxe_damage[1])+' HP')
        print('Machete: '+str(machete_damage[0])+'-'+str(machete_damage[1])+' HP')
        print('Frying pan: '+str(frying_pan_damage[0])+'-'+str(frying_pan_damage[1])+' HP')
        print('Dagger: '+str(dagger_damage[0])+'-'+str(dagger_damage[1])+' HP')
    def start_attack():
        global health, attack, throwing_rocks, victory_status, wires, torches, one_time, enemy, current_enemy, battery, custom_attack
        victory_status=False
        if custom_attack==False:
            count=len(enemy)-1
            rando=random.randint(0,count)
            current_enemy=enemy[rando]
            health=random.randint(25,50)
        while health>0:
            attack=True
            if dev==True:
                if beta_var==True:
                    print('Your Level: '+str(level))
                    print('Your Experience: '+str(xp)+'\n')
            print('Enemy Name:', current_enemy)
            print('Enemy Health:',health,'HP')
            print('(1)Use item')
            print('(2)Attempt to run')
            choice=input('Choose an option: ')
            clear()
            if choice == "1":
                open_bag()
            if choice == "2":
                chance=random.randint(0,2)
                if throwing_rocks>0:
                    if chance == 1:
                        print('You got out with little to no harm. You did however loose 1 throwing rock.')
                        throwing_rocks-=1
                        health=0
                if throwing_rocks<1:
                    chance=0
                if chance == 0:
                    print('You got out safe and sound. Nothing can stop you!')
                    health=0
                if chance == 2:
                    print('The enemy stopped you moments before you tried to leave. He brought you back to fight.')
        health=0
        flashlight_use=False
        torch_use=False
        throwing_rocks_use=False
        attack=False
        one_time=False
        if victory_status==True:
            try:
                xp+=random.randint(15,30)
            except:
                pass
            print('You won! The enemy fell down without a doubt. You earnings are...')
            chance=random.randint(0,1)
            print('You won',chance,'wires')
            wires+=chance
            chance=random.randint(0,2)
            print('You won',chance,'torches')
            torches+=chance
            print('You earned 25% battery for your flashlight.')
            battery+=25
            if battery>100:
                battery=100
        move_on=input('Hit enter to exit: ')
        clear()
    def chapters():
        global hi, error_message_skip
        #Start of show options
        print('True = Current Chapter')
        print('(1)Intro:',globals()[hi[0]])
        a=2
        b=1
        for i in range(len(hi)-1):
            print('('+str(a)+')Chapter '+str(b)+':',globals()[hi[i+1]])
            a+=1
            b+=1
        #End of show options
        list2=''
        error_some=False
        try:
            exit_choice=False
            choice=input('Which chapter or exit: ')
            if choice == "exit":
                exit_choice=True
                error_some=True
            if exit_choice==False:
                choice=int(choice)
                if choice>1:
                    list2='story_part'+str(choice-1)
                if choice==1:
                    list2='begin'
        except:
            if error_message_skip==False:
                show_error()
            error_some=True
        if error_some==False:
            choice-=1
            p=True
            a=1
            while p==True:
                try:
                    globals()[hi[a]]=False
                    a+=1
                except:
                    p=False
            try:
                globals()[hi[0]]=False
            except:
                pass
            globals()[list2]=True
        skip = input('Hit enter to exit:')
    def open_menu():
        global menu_open, sticks, coal, torches, working_battery_charger, battery_charger, wires, computer_chips
        if menu_open==False:
            print('Here you can do some crafting and see what you can do with certian items.\n')
        loop=True
        while loop == True:
            print('-Options-\nBuild\nleave\nCharge batteries')
            check = input('Choose one: ').lower()
            clear()
            if check == "build":
                print('-Options-\nBattery charger\nTorches')
                check = input('Choose one: ').lower()
                if check == "torches":
                    print('You need 1 stick and 1 coal to make 4 torches.')
                    check = input('(Yes/No)Would you like to make some: ').lower()
                    if check == "yes":
                        print('Checking for items.')
                        time.sleep(.6)
                        print('Checking for items..')
                        time.sleep(.6)
                        print('Checking for items...')
                        time.sleep(.6)
                        if sticks>0:
                            if coal>0:
                                print('You made 4 sticks. It has been added to your backpack.')
                                coal-=1
                                sticks-=1
                                torches+=4
                        if sticks<1:
                            print('You need more sticks')
                        if coal<1:
                            print('You need more coal')
                    if check == "no":
                        pass
                if check == "battery charger":
                    clear()
                    print('You will need a battery charger, 5 wires and 1 computer chip.')
                    check = input('(Yes/No)Would you like to make it: ').lower()
                    if check == "yes":
                        if working_battery_charger==False:
                            if battery_charger==True:
                                if wires>4:
                                    if computer_chips>0:
                                        print('You now have a working battery charger.')
                                        working_battery_charger=True
                        if working_battery_charger==True:
                            print('You already have one')
                        if working_battery_charger==False:
                            if battery_charger==False:
                                print('You don\'t have a battery charger')
                        if working_battery_charger==False:
                            if wires<5:
                                print('You don\'t have 5 wires')
                        if working_battery_charger==False:
                            if computer_chips<1:
                                print('You don\'t have enough computer chips.')
            if check == "leave":
                loop=False
            if check == "charge batteries":
                    if working_battery_charger==True:
                        if bad_batteries>0:
                            print('All you batteries are now good.')
                            good_batteries+=bad_batteries
                            bad_batteries=0
                            i_have_the_power=True
                        if bad_batteries<1:
                            print('You don\'t have any discharged batteries')
                    if working_battery_charger==False:
                        print('You need to make the battery charger.')
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
            print('(1)Torches')
            print('(2)Flashlight')
            print('(3)Throwing rocks')
            print('(4)Battery')
            print('(5)My suit')
            print('(6)To move onto game')
            print("(7)My computer says 'clear' is not reconized...")
            check = str(input('Which one: '))
            clear()
            if check == "1":
                print('Narrator: You will start with ',str(torches),'. They are a one time use.')
                print('You can use these to see and possibly find items you wouln\'t be able to')
                print('find. Torches and the flashlight are used in the same way but are costly')
                print('in their own way. When you use a torch, the amount you can use goes down')
                print('by one. You can find more torches by exploring. Torches are not common')
                print('to find.')
            if check == "2":
                print('Narrator: You will not start with a flash light. You will need to find one.')
                print('When you use the flash light it will absorb 5-10 percent of your battery')
                print('each time. If you run out of battery you will need to change it in you')
                print('backpack. The flash light will never break.')
            if check == "3":
                print('Narrator: You will have ',str(throwing_rocks),' to start out. You can find more')
                print('lying on the ground. They are very common to find. This is your starting weapon.')
                print('As the game devolopes more weapons will be added. For now there are only rocks.')
                print('And since that, rocks are the most powerful weapon of all right now. it will')
                print('usually take aleast 2-3 rocks to defeat an enemy. Some time if you lucky only 1.')
            if check == "4":
                print('Narrator: To check your battery percent type (%) when available. And to see how')
                print('many you have check your backpack. The battery will be used for some thing. First,')
                print('it will be used for your flashlight, then it will be used for ecolocation, and')
                print('sometimes you will find a machine that needs to be powered by your suit.')
            if check == "5":
                print('Narrator: You suit is the one that holds the batteries. It also holds you items.')
                print('Since it makes no since to store things in a suit, we call the place holder a backpack.')
                print('But, the suit will hold new technology you find and be able to reconize and reapir it.')
                print('You suit comes with a repair tool, a analyizer, mini fridge, and many others. You will')
                print('No need to wory about eating it is done between games.')
            if check == "6":
                loop=False
            if check == "7":
                print('To fix this problem you will need to head to the settings page. To enter')
                print('the settings page exit this space by typing (6) and then type settings.')
                print('Then type (1). The problem should be fixed afterwards.')
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
        global frying_pan, frying_pan_use, dagger, dagger_use, pickaxe, machete, machete_use, pickaxe_use, total_wins, spears, spears_use, one_time, victory_status, attack, health, bag_open, good_batteries, bad_batteries, torches, battery, throwing_rocks, battery_charger, computer_chips, wires, sticks, coal, throwing_rocks_use, flashlight_use, torch_use
        if bag_open == False:
            bag_open=True
            print('\nGame: While in your backpack type the number of the item to use it.')
            print('Game: For this item we will switch the batteries\n')
            time.sleep(3)
        print('(1)Good Batteries: '+str(good_batteries))
        print('(2)Bad Batteries: '+str(bad_batteries))
        if torch_use==False and flashlight_use==False and one_time==False:
            print('(3)Torch: '+str(torches))
            print('(4)Flashlight: '+str(battery))
        if flashlight_use==True and torch_use==True:
            print('(3)Throwing_rocks: '+str(throwing_rocks))
            print('(4)Spears: '+str(spears))
            print('(5)Pickaxe: '+str(pickaxe))
            print('(6)Machete: '+str(machete))
            print('(7)Frying pan:'+str(frying_pan))
            print('(8)Dagger:'+str(dagger))
        if flashlight_use==False and torch_use==False:
            print('(5)Throwing_rocks: '+str(throwing_rocks))
            print('(6)Spears: '+str(spears))
            print('(7)Pickaxe: '+str(pickaxe))
            print('(8)Machete: '+str(machete))
            print('(9)Frying pan: '+str(frying_pan))
            print('(10)Dagger: '+str(dagger))
        if attack==False:
            print('(10)Other items')
            print('(11)Total wins')
            check = str(input('\nType (leave) or enter item number to use: ')).lower()
        if attack == True:
            check = str(input('What item will you use: ')).lower()
        if check =="11":
            if attack==False:
                print('Total wins',total_wins)
                move_on=input('Hit enter to exit: ')
        if check == "10":
            if attack==False:
                if battery_charger==True:
                    print('Battery charger:',str(battery_charger))
                print('Wires:',str(wires))
                print('Computer chips:',str(computer_chips))
                print('Sticks:',str(sticks))
                print('Coal:',str(coal))
                move_on=input('Hit enter to exit: ')
        if check == "8":
            if attack==True and flashlight_use==False:
                if machete<1:
                    print('System: You are out of ammo.')
                if machete>0:
                    machete_use=True
                    machete-=1
        if check == "7":
            if attack==True and flashlight_use==True:
                if frying_pan<1:
                    print('System: You are out of ammo.')
                if frying_pan>0:
                    frying_pan-=1
                    frying_pan_use=True
        if check == "9":
            if attack==True and flashlight_use==False:
                if frying_pan<1:
                    print('System: You are out of ammo.')
                if frying_pan>0:
                    frying_pan-=1
                    frying_pan_use=True
        if check == "8":
            if attack==True and flashlight_use==True:
                if dagger<1:
                    print('System: You are out of ammo.')
                if dagger>0:
                    dagger-=1
                    dagger_use=True
        if check == "10":
            if attack==True and flashlight_use==False:
                if dagger<1:
                    print('System: You are out of ammo.')
                if dagger>0:
                    dagger-=1
                    dagger_use=True
        if check == "7":
            if attack==True and flashlight_use==False:
                if pickaxe<1:
                    print('System: You are out of ammo.')
                if pickaxe>0:
                    pickaxe_use=True
                    pickaxe-=1
        if check == "6":
            if attack==True and flashlight_use==False:
                if spears<1:
                    print('System: You are out of ammo.')
                if spears>0:
                    spears_use=True
                    spears-=1
        if check == "5":
            if attack==True and flashlight_use==False:
                if throwing_rocks<1:
                    print('System: You are out of ammo.')
                if throwing_rocks>0:
                    throwing_rocks_use=True
                    throwing_rocks-=1
        if check == "6":
            if attack==True and flashlight_use==True:
                if machete<1:
                    print('System: You are out of ammo.')
                if machete>0:
                    machete_use=True
                    machete-=1
        if check == "5":
            if attack==True and flashlight_use==True:
                if pickaxe<1:
                    print('System: You are out of ammo.')
                if pickaxe>0:
                    pickaxe_use=True
                    pickaxe-=1
        if check == "4":
            if attack==True and flashlight_use==True:
                if spears<1:
                    print('System: You are out of ammo.')
                if spears>0:
                    spears_use=True
                    spears-=11
        if check == "3":
            if attack==True and flashlight_use==True:
                if throwing_rocks<1:
                    print('System: You are out of ammo.')
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
                print('Your new stats\n')
                print('(1)Good Batteries: '+str(good_batteries))
                print('(2)Bad Batteries: '+str(bad_batteries))
                print('Battery: '+str(battery))
                print('\n')
            if good_batteries<1:
                print('You don\'t have any charged batteries.')
            move_on=input('Hit enter to exit: ')
        if check == "2":
            print('Those are no good for now. Try again later.')
        if check == "leave":
            print('Moving you on')
        clear()
        if attack == True:
            if dagger_use==True:
                chance=random.randint(0,2)
                if chance==0:
                    print('You swing your dagger out of your pocket and sprint towards the enemy giving him a harsh shock of force in the thigh. He halls down and gets back up almost immediatly.')
                if chance==1:
                    print('You prepare to throw the dagger... Swoosh... Hit. The enemy falls down and glances at you with the sense; is that all you got?')
                if chance==2:
                    print('You run at the enemy. Stabbing him several times in the chest. Your dagger breaks and you return to your stance.')
                damage=random.randint(dagger_damage[0],dagger_damage[1])
                health-=damage
                print('Damage Dealt: ',damage)
                dagger_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if frying_pan_use==True:
                chance=random.randint(0,2)
                if chance==0:
                    print('You dive in for a swing at the enemy. Smacking it across the face. He feels a little pinch but that\'s it.')
                if chance==1:
                    print('You charge your swing attack with the frying pan. Pulling your arm as far back as possible... A blissful sound sweeps the air... Then, smack!')
                if chance==2:
                    print('You decide to take the old mom route and use the frying pan. Teaching the enemy a lesson results in him being more pissed.')
                damage=random.randint(frying_pan_damage[0],frying_pan_damage[1])
                health-=damage
                print('Damage Dealt: ',damage)
                frying_pan_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if machete_use==True:
                chance=random.randint(0,4)
                if chance == 0:
                    print('You swing the blade with all your might. It slices off a good hunk of flesh from the target.')
                if chance == 1:
                    print('You go for a simple but lethal stab. You miss the torso, but instead scrape the targets arm.')
                if chance == 2:
                    print('You swing for the neck, like some kind of killer from a slasher flick. You slip on a patch of moss on the ground and instead slice a big gash across the foes torso.')
                if chance == 3:
                    print('You wind up for a swing, which takes about 2 seconds, and release, slicing a huge gash on the enemies body.')
                if chance == 4:
                    print('You swing wildly, like you\'re fighting for your life against a horde of enemies, even though its only one.')
                damage=random.randint(machete_damage[0],machete_damage[1])
                health-=damage
                print('Damage Dealt: ',damage)
                machete_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if pickaxe_use==True:
                chance=random.randint(0,4)
                if chance == 0:
                    print('You swing for the enemies skull, or head like extrusion. There is a resounding crack, and you see a decently sized wound.')
                if chance == 1:
                    print('You try to hit the ceiling to drop some rocks on the enemies head. You land a solid swing, but all the drops is a few pebbles. The enemy pities you, and hurts islf for you.')
                if chance == 2:
                    print('You swing for the creatures ribs, hoping to break some bones. There\'s a loud crack sound, and the creature crumples over in pain.')
                if chance == 3:
                    print('You step back a short distance, and taunt the enemy into charging. Once its close enough, you swing the flat side of the pick at its jaw, or other similar area, tossing it up and hitting its head on the ceiling.')
                if chance == 4:
                    print('You club the enemy over the head with the handle of the pick. There\'s a decently sized lump left over.')
                damage=random.randint(pickaxe_damage[0],pickaxe_damage[1])
                health-=damage
                print('Damage Dealt: ',damage)
                pickaxe_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if spears_use==True:
                chance=random.randint(0,6)
                if chance == 0:
                    print('You throw your long stick shaped object in the enemies direction. Hit! The enemy takes damage.')
                if chance == 1:
                    print('You use all of your strength while ensuring your is stable to be able to throw the spear as hard as you can. Shoooosh... Goes through the air.')
                if chance == 2:
                    print('You get ready to throw the spear... You trip on a rock and you just barely miss, still hitting the enemy though. Not all of your power was put through.')
                if chance == 3:
                    print('You raise the spear to your side, to go for a stab. You get a running start, but stumble and stab the enemy in the foot. It yowls in pain, and takes damage.')
                if chance == 4:
                    print('You try to swipe at the enemy with the pointy end, but grabbed the spear the wrong way, and instead hit it with the blunt end, doing slightly more damage.')
                if chance == 5:
                    print('You go for a jump attack, but overestimated the actual height of the cavern, instead, hitting your head off the ceiling, damaging yourself instead. Idiot.')
                if chance == 6:
                    print('You go to grab your spear, but feel nothing there. You hear a noise behind you and turn to investigate. You see a small dog running towards the enemy with the spear. you...hit it??')
                damage=random.randint(spears_damage[0],spears_damage[1])
                health-=damage
                print('Damage Dealt: ',damage)
                spears_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if throwing_rocks_use==True:
                chance=random.randint(0,6)
                if chance==0:
                    print('You attack the enemy with a rock. He cried to his mommy afterwards.')
                if chance==1:
                    print('You hurt the enemy with a small indistinct bolder. He felt nothing.')
                if chance==2:
                    print('You penetrated the enemy with a big grain of sand. He doesn\'t care.')
                if chance==3:
                    print('You assulted the enemy with a gray peble. He smacked you in the face.')
                if chance==4:
                    print('You show the enemy how much you hate him. He broke in tears.')
                if chance==5:
                    print('You used physics to move the peble towards him creating pain on the enemy.')
                if chance==6:
                    print('You enflicted undesired actions onto your enemy. He doesn\'t like it.')
                damage=random.randint(throwing_rocks_damage[0],throwing_rocks_damage[1])
                health-=damage
                print('Damage Dealt: ',damage)
                throwing_rocks_use=False
                if health<1:
                    victory_status=True
                    total_wins+=1
            if flashlight_use==True or torch_use==True:
                if one_time==False:
                    chance=random.randint(0,6)
                    if chance == 0:
                        print('You pull out your light and take a look around. You capture everything in your mind and use it to your full potential.')
                    if chance == 1:
                        print('You grab your light and take a look at what you are battling. You see rotten flesh covering his bones, smells covering his shame, and pain covering his soul. You take a step back and turn your light off.')
                    if chance == 2:
                        print('You pull out your light and take a look around. You try and see if there is anything useful lying around. You find 10 throwing rocks.')
                        throwing_rocks+=10
                    if chance == 3:
                        print('You pull out a photon emmitter to survey the area. You find a very pointy and rude stick on the ground near you. You make contact with the tip and it instantly removes blood from your body. You gain 1 spear.')
                        spears+=1
                    if chance == 4:
                        print('You pull out a neon green flashlight and survey the area. Its hard to tell what\'s around you due to the color.')
                    if chance == 5:
                        print('You effortlessly aquire a flashlight from your...uhhh... inventory. The lens is slightly cracked, but you manage to see a small round creature sprint past you, muttering something about donuts.')
                    if chance == 6:
                        print('You grab the glowing round cylinder off the ground. The energy storage container has lost it\'s will to live. You put the glowing round cylinder back on the ground.')
                    torch_use=True
                    flashlight_use=True
                    one_time=True
    def battery_bag():
        global battery
        print('Battery: '+str(battery)+'%')
    import time
    current_vars=list(dir())
    count_vars=0
    variables.clean_vars()
    if dev==True:
        skip=True
        bag_open=True
    if dev==False:
        print('Skip setup -- (skip)')
        name=input('Hello user, Enter your name: ').lower()
        if name=="brandon":
            skip=True
            dev=True
            menu_open=True
            bag_open=True
        if name=='skip':
            skip=True
            print('-Choose an option-')
            print('bag')
            print('count_var')
            print('battery_percent')
            print('start_game')
            print('starting_stuff')
            check = input('To skip hit enter: ')
            if check == "":
                skip=True
                bag_open=True
                menu_open=True
            if check == "starting_stuff":
                starting_stuff()
            if check == "start_game":
                start=True
            if check == "bag":
                open_bag()
            if check == "count_var":
                count()
                print('Test Complete!')
                time.sleep(1)
            if check == "battery_percent":
                battery_bag()
    if skip==False:
        print('Game will start soon.')
        time.sleep(3)
        print('Game starting in 3')
        time.sleep(1)
        print('Game starting in 2')
        time.sleep(1)
        print('Game starting in 1')
        time.sleep(1)
        clear()
        print('In some dark and stormy night. You and your parents live in a small house in the middle of the forest. You are frightened and scared.')
        time.sleep(6)
        print('Your parents tell you to stay in your room.')
        time.sleep(4)
        print('You hear noises...')
        time.sleep(2)
        print('Noises like no other.')
        time.sleep(4)
        print('Then... You hear screams!')
        time.sleep(.9)
        print('...........!')
        time.sleep(3)
        clear()
        print('Narrator: You\'ve been knocked out.')
        time.sleep(2)
        print('Checking all systems...')
        count()
        time.sleep(1.3)
        print('All systems check')
        time.sleep(2)
        clear()
        loop=True
        while loop==True:
            print('(Yes/No) Narrator: Are you okay: ')
            check=input().lower()
            if check == "yes" or check == "y":
                print('Narrator: That\'s good to hear.')
                loop=False
            if check == "no" or check == "n":
                print('Narrator: Well, um, you will get through it.')
                loop=False
        time.sleep(3.5)
        print('System: Emergency, power supply running low!')
        print('Battery: '+str(battery),'%')
        time.sleep(2.7)
        clear()
        print('Narrator: Okay, we must gather some power.')
        time.sleep(.8)
        loop=True
        while loop==True:
            print('Game: Type (bag) when available to open your backpack.')
            check = input('Game: Open your bag: ').lower()
            if check == "bag":
                open_bag()
                loop=False
            else:
                print('I didn\'t understand that. Say again...')
        clear()
        print('System: Power supply, stable.')
        time.sleep(1.5)
        print('System: To see your current battery percent type (%)')
        time.sleep(1.5)
        print('Narrator: You better do what she says.')
        time.sleep(4)
        clear()
        loop=True
        while loop==True:
            print('\nGame: Type (%) when available to see your battery percentage.')
            check = input('Game: Check battery percentage: ')
            if check == "%":
                clear()
                battery_bag()
                loop=False
            else:
                print('I didn\'t understand that. Say again...')
        time.sleep(3)
        loop=True
        clear()
        while loop==True:
            print('Okay now, to see app improvements type (updates).')
            check = input('Game: Check the updates for this version: ').lower()
            if check == "updates" or check == "update":
                clear()
                updates()
                loop=False
            else:
                print('I didn\'t understand that. Say again...')
        loop=True
        clear()
        while loop==True:
            print('To see locked and unlocked chapters type (chapters).')
            check = input('Game: Check your unlocked chapters: ').lower()
            if check == "chapters" or check == "chapter":
                clear()
                chapters()
                loop=False
            else:
                print('I didn\'t understand that. Say again...')
        loop=True
        clear()
        while loop==True:
            print('To change settings to your preference type (settings)')
            check = input('Game: Open the settings page: ').lower()
            if check == "setting" or check == "settings":
                clear()
                settings()
                loop=False
            else:
                print('I didn\'t understand that. Say again...')
        clear()
        print('Narrator: Okay, you now know the basics, lets put you in the game.')
        time.sleep(4)
        print('Game: Putting narrator to sleep...')
        time.sleep(3)
        print('Narrator: Wait, what!')
        time.sleep(2)
        print('Narrator: You can\'t do this... I feel... sleaspafajsdlle...')
        time.sleep(3.5)
        print('Game: Narrator went to sleep')
        time.sleep(2.2)
        print('Game: Game starting up...')
        time.sleep(2)
        clear()
        count()
        print('\nWelcome to <THE NEW GAME>')
        time.sleep(.5)
        print('System: Booting up Narrator.')
        time.sleep(.5)
        print('System: Booting up Narrator..')
        time.sleep(.5)
        print('System: Booting up Narrator...')
        time.sleep(.5)
        print('System: Booting up Narrator..')
        time.sleep(.5)
        print('System: Booting up Narrator.')
        time.sleep(.5)
        print('System: Booting up Narrator..')
        time.sleep(.5)
        print('System: Booting up Narrator...')
        print('\n')
        time.sleep(1)
        clear()
        print('Setting up items.')
        time.sleep(.5)
        print('Setting up items..')
        time.sleep(.5)
        print('Setting up items...')
        time.sleep(.5)
        print('Setting up items..')
        time.sleep(.5)
        print('Setting up items.')
        time.sleep(.5)
        print('Setting up items..')
        time.sleep(.5)
        print('Setting up items...')
        time.sleep(.5)
        clear()
        print('Game: All systems check')
        time.sleep(.5)
        print('Narrator: All systems check')
        time.sleep(.5)
        print('System: All systems check')
        time.sleep(2.5)
        clear()
        print('Narrator: Oh, I\'m back. Thank god.')
        time.sleep(1.8)
        print('Narrator: So user. There are still some things to teach you.')
        time.sleep(3)
        print('Narraror: But I\'ll let you choose the order. To start enter the number next to the item.')
        time.sleep(3)
        help_menu()
        time.sleep(1)
        clear()
        print('\nOne more thing. When available type (help) to go back to that list. More items will be added in future updates.')
        print('Game loading.')
        time.sleep(.5)
        print('Game loading..')
        time.sleep(.5)
        print('Game loading...')
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
            start_check=True
            loop=True
            while loop == True:
                try:
                    if skip_check==False:
                        if start_check==False:
                            level_check()
                            clear()
                        if start_check==True:
                            print('System check in progress. Please wait...')
                            time.sleep(3)
                            print('Checking level...')
                            time.sleep(1.5)
                            level_check()
                            clear()
                            start_check=False
                except:
                    pass
                print('Your options:')
                print('Bag       Start     %')
                print('Hints     Menu      Save')
                print('Shop      Awards    Updates')
                print('Chapters  Settings  Battle')
                print('Damage    Gems      Load')
                print('Sleep     Stats     Practice')
                print('Other')
                if dev==False:
                    print('-------(Dev Mode)-------')
                if dev==True:
                    print('-----(Exit Dev Mode)-----')
                    print() 
                    print('Dev Tools:')
                    print('clear_cache')
                    print('dev_battle')
                    print('dev edit_chapters')
                    print('load settings.dev')
                    print('load beta_vars.py')
                    print('show all_vars')
                    print('show buy')
                    print('show sell')
                    print('var count')
                    print('edit var')
                print('')
                check = input('Choose an option: ').lower()
                hey=check
                if len(check)>0:
                    if check[len(hey)-1]==" ":
                        check=check[0:len(hey)-1]
                    elif check[len(hey)-1]=="_":
                        check=check.replace("_","")
                    else:
                        if "_" in check:
                            check=check.replace("_"," ")
                clear()
                if check == "other":
                    print('Note: Most or all of these functions are either not complete or have not been started.')
                    print('Your options:')
                    print('Buildings')
                    print('Generators')
                    print('Calendar')
                    print('Time travel')
                    check = input('Choose an option: ').lower()
                if check == "show sell":
                    if dev==True:
                        variables.show_sell()
                        move_on=input('Hit enter to exit: ')
                if check == "show buy":
                    if dev==True:
                        variables.show_buy()
                        move_on=input('Hit enter to exit: ')
                if check in edit_var_input:
                    non_function()
                if check in var_count_input:
                    variables.show()
                if check in show_all_vars_input:
                    if dev==True:
                        variables.clean_vars()
                        variables.explain()
                        move_on=input('\nHit enter to exit: ')
                if check in generators_input:
                    print("Note: Feature not yet set")
                    print("\nFeature idea:")
                    print("Make sure your bulding have sufficient power for daily lives.")
                    move_on=input('Hit enter to exit: ')
                if check in buildings_input:
                    print("Note: Feature not yet set")
                    print("\nFeature idea:")
                    print("You can build your own city.")
                    move_on=input('Hit enter to exit: ')
                if check in time_travel_input:
                    print("Note: Feature not yet set")
                    print('\nFeature idea:')
                    print("You can travel to other days in the year using this feature.")
                    move_on=input('Hit enter to exit: ')
                if check in calendar_input:
                    clear()
                    if dev==False:
                        non_function()
                    if dev==True:
                        choice=True
                        been='You have already been here.'
                        print("Enter the name of the day you heard of.")
                        day=input('Type a day to earn rewards: ').lower()
                        days=['nocobot','peachflame','novonoid','wetchop','vasco','yodacloud','looplab','nalpure','zestpond','checknology','fireshine']
                        rewards=['frying_pan','dagger','throwing_rocks','spears','mechete','pickaxe']
                        if day in days:
                            a1=len(days)
                            a2=False
                            a3=0
                            for i in range(a1):
                                if day == days[i].lower():
                                    a2=True
                                    a3=i
                            clear()
                            a5='day_lock'+str(a3+1)
                            if globals()[a5]==True:
                                print('You already visited this day.')
                            if globals()[a5]==False:
                                send_var=rewards[a3]
                                variables.add(send_var,3)
                                print('You earned',3,send_var)
                                globals()[a5]=True
                        move_on=input('Hit enter to exit: ')
                if check in load_beta_vars_input:
                    try:
                        if beta_var==True:
                            try:
                                from beta_vars import *
                                print('Imported beta_vars')
                                time.sleep(1.5)
                            except:
                                print('beta_vars.py file could not be found.')
                                time.sleep(1.5)
                    except:
                        pass
                if check in practice_input:
                    #This function will allow users to work on their strength to allow more damage with select weapons in battle.
                    if dev==True:
                        print("Sorry Dev. I haven't done this yet.")
                        move_on=input('Hit enter to exit: ')
                    if dev==False:
                        non_function()
                if check in exit_dev_mode_input:
                    choice = input('Are you sure: ').lower()
                    clear()
                    if choice in yes_input:
                        print('System: Settings have been altered.')
                        dev=False
                    else:
                        print('System: Settings have not been altered.')
                if check in stats_input:
                    stats()
                    clear()
                if check in clear_cache_input:
                    clear_cache()
                if check in sleep_input:
                    if dev==False:
                        non_function()
                    if dev==True:
                        print('Sleeping...')
                        sleep(4)
                        up_down=random.uniform(-2,2)
                        if up_down<0:
                            print('Prices have gone down',round(up_down,2))
                            coal_buy-=round(up_down,2)
                            coal_sell-=round(up_down,2)
                            computer_chips_buy-=round(up_down,2)
                            computer_chips_buy-=round(up_down,2)
                            wires_buy-=round(up_down,2)
                            wires_sell-=round(up_down,2)
                            good_batteries_buy-=round(up_down,2)
                            good_batteries_sell-=round(up_down,2)
                            bad_batteries_buy-=round(up_down,2)
                            bad_batteries_sell-=round(up_down,2)
                            sticks_buy-=round(up_down,2)
                            sticks_sell-=round(up_down,2)
                            throwing_rocks_buy-=round(up_down,2)
                            throwing_rocks_sell-=round(up_down,2)
                            spears_buy-=round(up_down,2)
                            spears_sell-=round(up_down,2)
                            torches_buy-=round(up_down,2)
                            torches_sell-=round(up_down,2)
                            pickaxe_buy-=round(up_down,2)
                            pickaxe_sell-=round(up_down,2)
                            machete_buy-=round(up_down,2)
                            machete_sell-=round(up_down,2)
                            frying_pan_sell-=round(up_down,2)
                            frying_pan_buy-=round(up_down,2)
                            dagger_buy-=round(up_down,2)
                            dagger_sell-=round(up_down,2)
                        if up_down>0:
                            print('Prices have gone up',round(up_down,2))
                            coal_buy+=round(up_down,2)
                            coal_sell+=round(up_down,2)
                            computer_chips_buy+=round(up_down,2)
                            computer_chips_buy+=round(up_down,2)
                            wires_buy+=round(up_down,2)
                            wires_sell+=round(up_down,2)
                            good_batteries_buy+=round(up_down,2)
                            good_batteries_sell+=round(up_down,2)
                            bad_batteries_buy+=round(up_down,2)
                            bad_batteries_sell+=round(up_down,2)
                            sticks_buy+=round(up_down,2)
                            sticks_sell+=round(up_down,2)
                            throwing_rocks_buy+=round(up_down,2)
                            throwing_rocks_sell+=round(up_down,2)
                            spears_buy+=round(up_down,2)
                            spears_sell+=round(up_down,2)
                            torches_buy+=round(up_down,2)
                            torches_sell+=round(up_down,2)
                            pickaxe_buy+=round(up_down,2)
                            pickaxe_sell+=round(up_down,2)
                            machete_buy+=round(up_down,2)
                            machete_sell+=round(up_down,2)
                            frying_pan_sell+=round(up_down,2)
                            frying_pan_buy+=round(up_down,2)
                            dagger_buy+=round(up_down,2)
                            dagger_sell+=round(up_down,2)
                        if up_down==0:
                            print('No price change.')
                        move_on=input('Hit enter to exit: ')
                if check in load_settings_input:
                    if dev==True:
                        clear()
                        try:
                            os.rename('settings.dev','settings.py')
                            from settings import *
                            os.rename('settings.py','settings.dev')
                            print('Imported settings dev file.')
                        except:
                            print('Could not find dev file.')
                        try:
                            os.remove('settings.pyc')
                        except:
                            print('Settings.pyc cache not found.')
                        print('(1)Quick Settings')
                        print('(2)Version Info')
                        print('(3)Update Info')
                        print('(4)Edit chapters')
                        print('(5)Settings.dev')
                        help=input('Choose an option or hit enter: ')
                        if help == "1":
                            settings()
                        if help == "2":
                            print (version)
                        if help == "3":
                            updates()
                        if help == "4":
                            edit_chapters()
                        if help == "5":
                            try:
                                clear()
                                print('Test Battle:',str(dev_battle))
                                print('Edit Chapters:',str(dev_edit_chapters))
                                print('Free Stuff:',str(dev_give_stuff))
                                print('Repeat Amount:',str(repeat_amount))
                                print('Name of Dev:',name)
                                move_on=input("Hit enter to exit: ")
                            except:
                                pass
                if check in dev_mode_input:
                    print('Do you want to enter dev mode. You can not reverse this desicion without restarting or editing the save file.')
                    choice = input('Yes or No: ').lower()
                    if choice in yes_input:
                        dev=True
                        print('Dev Mode is now activated. Enjoy!')
                        time.sleep(1.5)
                    else:
                        print('Okay. Dev Mode is not activated. Returing you to the game.')
                        sleep(2)
                    clear()
                if check in load_input:
                    works=False
                    try:
                        os.rename("Save.py","Save.gsf")
                        print('System Error: Renamed Save file')
                    except:
                        pass
                    try:
                        os.remove('Save.pyc')
                        print('System Error: Removed Save.pyc')
                    except:
                        pass
                    try:
                        load=open('Save.gsf','r')
                        load.close()
                        works=True
                    except:
                        print("Could not find a save file with the extension: .gsf")
                        print('Current Path:',path)
                    if works==True:
                        print('Renaming File...')
                        os.rename("Save.gsf","Save.py")
                        time.sleep(2)
                        clear()
                        from Save import version_save
                        if version_save not in version:
                            print('This save file is not compatible with this version.')
                            time.sleep(2.5)
                            print("Reverting file name...")
                            os.rename("Save.py","Save.gsf")
                        if version_save == version:
                            print('File Renamed. Importing variables...')
                            from Save import *
                            time.sleep(2)
                            clear()
                            print('Variables imported. Reverting file name...')
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
                            print('System: Import successful')
                    move_on=input('Hit enter to exit: ')
                    clear()
                if check in save_input:
                    clear()
                    save=open('Save.gsf','w')
                    save.write('#Move this file to the same directory of the game.')
                    save.write('\n#*Game Save File*')
                    save.write('\ndev = '+str(dev))
                    save.write('\nunlock_all_achievements = '+str(unlock_all_achievements))
                    save.write('\nrepeat_chapters = '+str(repeat_chapters))
                    save.write('\nnormal_clear = '+str(normal_clear))
                    save.write('\nrepeat_amount = '+str(repeat_amount))
                    save.write('\nchars_in_line = '+str(chars_in_line))
                    save.write('\nrun_off = '+str(run_off))
                    save.write('\nerror_message = '+str(error_message))
                    save.write('\nbegin = '+str(begin))
                    save.write('\nday_lock1 = '+str(day_lock1))
                    save.write('\nday_lock2 = '+str(day_lock2))
                    save.write('\nday_lock3 = '+str(day_lock3))
                    save.write('\nday_lock4 = '+str(day_lock4))
                    save.write('\nday_lock5 = '+str(day_lock5))
                    save.write('\nday_lock6 = '+str(day_lock6))
                    save.write('\nday_lock7 = '+str(day_lock7))
                    save.write('\nday_lock8 = '+str(day_lock8))
                    save.write('\nday_lock9 = '+str(day_lock9))
                    save.write('\nday_lock10 = '+str(day_lock10))
                    save.write('\nday_lock11 = '+str(day_lock11))
                    save.write('\nstory_part1 = '+str(story_part1))
                    save.write('\nstory_part2 = '+str(story_part2))
                    save.write('\nstory_part3 = '+str(story_part3))
                    save.write('\nstory_part4 = '+str(story_part4))
                    save.write('\nstory_part5 = '+str(story_part5))
                    save.write('\nstory_part6 = '+str(story_part6))
                    save.write('\nstory_part7 = '+str(story_part7))
                    save.write('\nstory_part8 = '+str(story_part8))
                    save.write('\nstory_part9 = '+str(story_part9))
                    save.write('\nstory_part10 = '+str(story_part10))
                    save.write('\nstory_part11 = '+str(story_part11))
                    save.write('\nstory_part12 = '+str(story_part12))
                    save.write('\ncave_cord1 = [\''+str(cave_cord1[0])+'\', '+str(cave_cord1[1])+']')
                    save.write('\nflashlight = '+str(flashlight))
                    save.write('\nbattery_charger = '+str(battery_charger))
                    save.write("\nenemy=['Goblin','Karen','Bat','Skeleton','Zombie','Put Name Here','Crab Rave','No Cell Service','Gertie','Jimmy','Gage']")
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
                    save.write('\nfrying_pan = '+str(frying_pan))
                    save.write('\ndagger = '+str(dagger))
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
                    save.write('\nfrying_pan_use = '+str(frying_pan_use))
                    save.write('\ndagger_use = '+str(dagger_use))
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
                    save.write('\nbuy_count = '+str(buy_count))
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
                    save.write('\nfrying_pan_buy = '+str(frying_pan_buy))
                    save.write('\ndagger_buy = '+str(dagger_buy))
                    save.write('\nsell_count = '+str(sell_count))
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
                    save.write('\nfrying_pan_sell = '+str(frying_pan_sell))
                    save.write('\ndagger_sell = '+str(dagger_sell))
                    save.write('\nlet_the_battles_begin = '+str(let_the_battles_begin))
                    save.write('\nguts_and_glory = '+str(guts_and_glory))
                    save.write('\ni_have_the_power = '+str(i_have_the_power))
                    save.write('\nits_payday = '+str(its_payday))
                    save.write('\nwhicked_chronicle = '+str(whicked_chronicle))
                    save.write('\nkeep_it_moving = '+str(keep_it_moving))
                    save.write('\n\n#Developers: Brandon Robinson, Albert Plummer')
                    save.write('\n#Github Page: github.com/sukadateam')
                    save.write('\n#Please report any bugs you encounter.')
                    save.write('\nallow_older_savefile = '+str(allow_older_savefile))
                    save.write("\nversion_save = '"+version+"'")
                    save.write('\n#Please do not change the version_save variable. It may cause crashes.')
                    save.write('\n#Instead change allow_older_savefile to True. Uppercase the T and rue is lowercase.')
                    save.write('\n#Please note. Changing to dev mode and back can cause problems. Please choose one or the other.')
                    save.close()
                    print('Game saved.')
                    print('Current Path:',path)
                    move_on=input('Hit enter to exit: ')
                if check in gems_input:
                    gem_collection()
                if check in awards_input:
                    achieve()
                if check in dev_battle_input:
                    try:
                        if dev_battle==True:
                            start_attack()
                        if dev_battle==False:
                            print('Nice try. You are not in dev mode.')
                    except:
                        pass
                if check in dev_edit_chapter:
                    try:
                        if dev_edit_chapters==True:
                            edit_chapters()
                        if dev_edit_chapters==False:
                            print('Nice try. You are not in dev mode.')
                    except:
                        pass
                if check in battle_input:
                    if guts_and_glory==True or dev==True:
                        collisseum()
                    if guts_and_glory==False and dev==False:
                        non_function()
                if check in shop_input:
                    shop()
                    check=''
                if check in damage_input:
                    item_damage()
                    move_on=input('Hit enter to exit: ')
                    check=''
                if check in settings_input:
                    settings()
                    check=''
                    clear()
                if check in chapter_input:
                    hi=[]
                    variables.story(hi)
                    chapters()
                    check=''
                if check in update_input:
                    updates()
                    check=''
                if check in menu_input:
                    open_menu()
                    check=''
                if check in bag_input:
                    open_bag()
                    check=''
                if check in battery_input:
                    battery_bag()
                    time.sleep(2)
                    clear()
                    check=''
                if check in hints_input:
                    print('HINT: Taking left or right will lead you to the same place but you will gather different items')
                    print('HINT: Taking a left takes 4 seconds to complete, a right takes 6 seconds to complete, forward is unknown')
                    print('HINT: Traps take 50 of your energy')
                    print("HINT: If your energy hits 0% you are forced to leave the cave")
                    print('HINT: A special passage has a chance to give you 25 energy')
                    print('HINT: Every time you leave you must restart your adventure. You will not loose you stuff.')
                    print('HINT: Leave cave and go back the ways you didn’t to make sure you have everything')
                    print('\nWhen you see this (*) you are allowed to type (bag) or (menu).')
                    move_on=input('Hit enter to exit: ')
                    clear()
                if check in start_input:
                    skip_begin=False
                    if begin == True:
                        print('Your first day of exploring is going to be your best. You enter')
                        print('the cave and see that there are 2 sides to it. You can either go left')
                        print('or you can go right. Which do you choose?')
                        print('\n')
                        battery_bag()
                        check = input("(*)Left or Right: ").lower()
                        if check == "menu":
                            open_menu()
                        elif check == "bag":
                            open_bag()
                        elif check == "left":
                            clear()
                            print('You take a left turn. You head straight for some time. While')
                            print('doing so, you find a battery charger. It looks like it might')
                            print('come in handy. But we can\'t use it till we find some parts.')
                            print('Lets keep looking.')
                            battery_charger=True
                            print('\nMoving through the mines...')
                            sleep(4)
                            begin=False
                            story_part1=True
                        elif check == "right":
                            clear()
                            print('You make a right turn. You head straight for some time. While')
                            print('doing so, you find a wire on the ground. I looks like it might')
                            print('be used for a battery charger, but I\'m not sure. Keep exploring')
                            print('to find more things.')
                            wires+=1
                            print('\nMoving through the mines...')
                            sleep(4)
                            begin=False
                            story_part1=True
                        else:
                            pass
                    if skip_begin==True:
                        begin=False
                    if story_part1==True or repeat_chapters==True:
                        clear()
                        print('You have 3 choices.')
                        print('Left: Seems to be safe.')
                        print('Straight: Seems to be a trap.')
                        print('Right: Rumor has it, it\'s a special passage.')
                        check = input('Forward, Left, Right: ').lower()
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
                            print('You go forward farther into the cave. You walk very slowly with the')
                            print('feeling of being sensed, You hear noises. POP. Out of nowhere. Your')
                            print('battery explodes. You quickly change it out. You rush through the')
                            print('cave to the end.')
                            good_batteries-=1
                            bad_batteries+=1
                            print('\nMoving through the mines...')
                            sleep(7.5)
                            story_part2=True
                            story_part1=False
                        if check == "left":
                            clear()
                            print('You take a left and there seems to be nothing here. You keep going through.')
                            print('\nMoving through the mines...')
                            sleep(4)
                            story_part2=True
                            story_part1=False
                        if check == "right":
                            clear()
                            print('You take a right and you walk for a bit. You look around and you see a battery')
                            print('charger on the wall. It looks like it has power. You charge your current battery.')
                            print('Your energy increases by 25%. You walk through the rest of the way.')
                            print('\nMoving through the mines...')
                            sleep(6)
                            story_part2=True
                            story_part1=False
                            battery+=25
                    if story_part2==True or repeat_chapters==True:
                        clear()
                        print('You have 2 choices.')
                        print('Left: Seems to be a trap.')
                        print('Forward: Seems to be safe.')
                        check = input('Left, Forward: ').lower()
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
                            print('You take a left. It seems to be a trap. You walk through carefully.')
                            print('While you walk through you see a light shine. It looks to be shining')
                            print('on an object. You go check it out. You got a closer look and find 2')
                            print('more wires. You pick them up. You walk through the rest in hopes that')
                            print('there are no traps.')
                            print('\nMoving through the mines...')
                            sleep(3)
                            story_part3=True
                            story_part2=False
                            wires+=2    
                        if check == "forward":
                            print('You go forward through the cave. While you do so, you look at the')
                            print('design of the cave. You find it interesting that the cave has some')
                            print('beautiful colors. You take in all the details. But you find')
                            print('something odd on the wall. It looks like a computer chip. You ask')
                            print('yourself, why is there a computer chip in this cave. You try and')
                            print('think about it but you soon come to realize you don’t know anything.')
                            print('Anything about the cave or anything outside the cave in that matter.')
                            print('You try and not think about it to hard and you move on to your \nadventure.')
                            print('\nMoving through the mines...')
                            sleep(3)
                            story_part3=True
                            story_part2=False
                            computer_chips+=1     
                    if story_part3==True or repeat_chapters==True:
                        clear()
                        print('You have 2 choice.')
                        print('Left: Seems to be safe.')
                        print('Right: Seems to be safe.')
                        check = input('Left, Right: ').lower()
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
                            print('You take a left. While you are walking down this way you think about things.')
                            print('Like why are you even in these caves? What is the point? Then you think a')
                            print('little harder. You realize you forgot why. You take a glance at the walls in')
                            print('the caves. You think harder. And it finally comes to you. You are down here')
                            print('to find the missing artifact.')
                            print('\nMoving through the mines...')
                            sleep(4)
                            story_part4=True
                            story_part3=False
                        if check == "right":
                            print('You walk down the cave and find a stick on the ground. It seems to have a shape')
                            print('of a torch. But we can’t make a torch without coal. So you pick it up thinking')
                            print('it\’s useless but in hopes it will come in handy.')
                            print('\nMoving through the mines...')
                            sleep(6)
                            story_part4=True
                            story_part3=False
                            sticks+=1
                    if story_part4==True or repeat_chapters==True:
                        clear()
                        print('There doesn\'t seem to be an end to this passage. Maybe if we continue forward')
                        print('we will eventually find something.') 
                        print('Moving down the passage...')   
                        sleep(6.5)
                        print('You have been walking the same way for a while now. You feel like it will never end...')   
                        print('Moving down the passage...')
                        sleep(6.5)
                        print('You eventually stumble apon an item laying on the ground. You pick it up and it')
                        print('appears to be 2 fully charged batteries.')
                        good_batteries+=2
                        sleep(5)
                        print('\nMoving through the mines...')
                        story_part5=True
                        story_part4=False
                    if story_part5==True or repeat_chapters==True:
                        clear()
                        print('There seems to be 2 options. You can go Left or straight.')
                        print('Straight: Seems to be safe.')
                        print('Left: Seems to have a battery charger.')
                        check = input('Left, Straight: ').lower()
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
                            print('You take a left and head down the passage. While walking you seem to find a')
                            print('steep hill moving you farther down the cave. You continue moving and you start')
                            print('to slip. You slide all the way down the hill and come to a stop. You get up and')
                            print('check your surroundings. And doing so you find a battery charger.')
                            print('Moving down the passage...')
                            sleep(4)
                            story_part6=True
                            story_part5=False
                            battery_charger=True
                        if check == "straight":
                            print('You head straight and find 2 wires. You pick them up and put them away, then you continue your adventure.')
                            wires+=2
                            print('Moving down the passage...')
                            sleep(4)
                            story_part6=True
                            story_part5=False
                    if story_part6==True or repeat_chapters==True:
                        clear()
                        print('You venture farther down the tunnel and you eventually find yourself near a hostile enemy. You try and not make any sudden movements be he notices you before you can get out of the way. You find yourself in a fight. You can either fight him/her or come back some other time.')
                        print('Narator: Just a suggestion, if you have less than 6 throwing rocks I would not reccomend attacking them just yet. Go buy some more or trade.')
                        move_on=input('Hit enter to start battle: ')
                        clear()
                        start_attack()
                        if victory_status==True:
                            story_part6=False
                            story_part7=True
                        print('Moving down the passage...')
                        sleep(4)
                    if story_part7==True or repeat_chapters==True:
                        print('After the encounter, you come across 3 more pathways, Left, Right, and Forward')
                        print(' Left: Something shiny')
                        print(' Right: Strange sound')
                        print(' Forward: Sound of wind')
                        check = input('Left, Right, or Forward: ').lower()
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
                        print('Moving down the passage...')
                        sleep(2)
                        clear()
                    if story_part8==True or repeat_chapters==True:
                        print('You feel compelled to take in your surroundings. Looking around and observing the details of the cave. The rough texture of the ichy walls. The imperfect shaping of the cave. Moss growing all around you. Dripping sounds from the sealling. Darkness surrounding you. You take all this in affect and accept that this is where you belong. Moving along the cave a sudden urge to rest arrisses and forces you to slow your every thought. Eventually putting you to sleep...')
                        print('Sleeping...')
                        sleep(4.5)
                        print('A glimmering light awakes your eyes. The thoughts of safety awake your every movement. Moving closer to it finding a loot crate. Sadness shows in your eyes. No rescue was here but there was some good stuff. The chest opens and the items are grabbed. Eventually moving farther into the tunnel.')
                        loot_crate(3)
                        move_on=input('Hit enter to keep moving: ')
                        print('Moving down the passage...')
                        sleep(4)
                        story_part9=True
                        story_part8=False
                        clear()
                    if story_part9==True or repeat_chapters==True:
                        print('After spending so much time in the caves you start to feel tired. You take a few hours to relax and get some rest.')
                        sleep(1.5)
                        print('Sleeping...')
                        sleep(3)
                        print('You wake up and find it hard to move. Going back to sleep hoping you are just sleep deprived.')
                        sleep(1.5)
                        print('Sleeping...')
                        sleep(3)
                        print('Waking up one more time and a sense of pain rushes to your head. Ignoring the pain, you continue down the passage...')
                        move_on=input('Hit enter to keep moving: ')
                        print('Moving down the passage...')
                        sleep(4)
                        story_part10=True
                        story_part9=False
                        keep_it_moving=True
                        clear()
                    if story_part10==True or repeat_chapters==True:
                        print('You continue to suffer from bodily pain, but trying to ignore it your keep moving...')
                        print('Moving down the passage...')
                        sleep(2)
                        print('An hour goes by without a sense of recognation. Moving father down the path you find your self in a pickle. Not with rick but with an enemy.')
                        move_on=input('Hit enter to start battle: ')
                        clear()
                        start_attack()
                        if victory_status==True:
                            story_part10=False
                            story_part11=True
                        clear()
                    if story_part11==True or repeat_chapters==True:
                        print("The battle ended and you take another rest. Making sure it's not for more than 30 mins.")
                        print('sleeping...')
                        sleep(2.5)
                        print("After waking up you feel great. No pain anywhere. So you deside to continue forward...")
                        sleep(3.5)
                        print('A note lays on the ground just feet ahead. Moving toward the piece of paper to pick it up. It reads...\n')
                        notes(2)
                        time.sleep(5)
                clear()
else:           
    print('wrong password')
