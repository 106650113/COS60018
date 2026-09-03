
def user_guide():#Function for navigating the user to the menu option that they have chosen
    menu_sel = input('Please select one of the following options')
    if menu_sel == '1':
        SR_reg()
    elif menu_sel == '2':
        search()
    elif menu_sel == '3':
        add_on()
    else:
        print('invalid selection')
        while menu_sel !='1' and menu_sel !='2' and menu_sel !='3':
                menu_sel = input('Please select from options 1,2 or 3 ')
        if menu_sel == '1':
            SR_reg()
        elif menu_sel == '2':
            search()
        elif menu_sel == '3':
            add_on()

        








def SR_reg():
    print("Please enter the following patient details")
    input('Full Name: ')
    input('Date of Birth: ')
    input("UR: ")

def search():
    pass

def add_on():
    pass



#Create a menu for the entire program

#Create the following menu 
#
print('====================================')
print('          Specimen Menu               ') 
#print('  Please Select the following options')
print('=====================================')
print('1. Specimen Registration')
print('2. Search')
print('3. Add-on tests')
user_guide()
