
counter = 1


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

        


def SR_reg():#Purpose of this function is to create patient profiles
    while True:
        print("Please enter the following patient details")
        pt_name = input('Full Name: ')
        pt_dob = input('Date of Birth: ')
        pt_ur = input("UR: ")

        pt_details={'name':pt_name, 
                    'dob':pt_dob,
                    'UR':pt_ur}
        reset = input ('Press 1 to register another patient or 2 to save and return to the main menu: ')
        print(pt_details)
        if reset == '1':
            continue
        elif reset == '2':
            break
    menu()




def search():
    pass

def add_on():
    pass



#Create a menu for the entire program

#Create the following menu 
#
def menu():
    print('====================================')
    print('          Specimen Menu               ') 
    #print('  Please Select the following options')
    print('=====================================')
    print('1. Specimen Registration')
    print('2. Search')
    print('3. Add-on tests')
    user_guide()

menu()