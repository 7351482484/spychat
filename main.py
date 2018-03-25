from spy_details import spy_name,spy_rating,spy_age#importing these vairables
print"hello buddy"#print hello buddy
print'let\'s get started'#getting started
def spy_chat(spy_name,spy_age,spy_rating):# defining the fucntion
    print'here are your options..'+spy_name
    show_menu=True
    while show_menu:
        spy_choice=input('what do you want to do \n 1.add stauts \n 2.add a friend \n 0.exit')
        if spy_choice==1:
            print 'add status'
        elif spy_choice==2:#elif for multiple conditions
            print'add a friend'
        elif spy_choice==0:
            show_menu=False
        else:
            print'invalid options...'
spy_exist=raw_input('are you a new user :Y/N')#asking whether new user or not
if spy_exist.upper()=='N':#when spy is old one
    print"welcome back  "+spy_name +'age :'+str(spy_age)+'spy rating'+str(spy_rating)#concating string with integer values
    spy_chat(spy_name,spy_age,spy_rating)#calling function
elif spy_exist.upper()=='Y':
     spy_name=raw_input('what is your spy name? \n ')
     print spy_name
if len(spy_name)>2:
    print'welcome  '+spy_name+' glad to have you back with us...'
    spy_salutation=raw_input('what should we call you Mr. or Mrs.. \n  ')
    if spy_salutation=='Mr.' or  spy_salutation=='Mrs.':
        spy_name=spy_salutation+'  '+spy_name
        print'alright    '+spy_name+'. i would like to know a little bit more about you... '
        spy_age=input('what is your age..? \n')
        if 12<spy_age<50:
            print'your age is correct....'
            spy_rating=input('what is your rating...? \n')
            if spy_rating>5.0:
                print'great spy...'
            elif 3.5<spy_rating<=5.0:
                print'average spy..'
            elif 2.5<spy_rating<=3.5:
                print"bad spy.."
            else:
                print'who hired you...'
            spy_online=True#to check spy is online
            print 'Authetication is completed'+ spy_name
            spy_chat(spy_name,spy_age,spy_rating)
        else:
            print'you are not eligible to be a spy...'
    else:
        print 'invalid salutation'
else:
    print 'oops '