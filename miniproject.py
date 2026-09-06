
pt_list ={} #Creates and empty string to populate pt list
specimen_list = {}
tests_list = {}


def user_guide():#Function for navigating the user to the menu option that they have chosen
    menu_sel = input('Please select one of the following options: ')
    if menu_sel == '1':
        SR_reg()
    elif menu_sel == '2':
        test_reg()
    elif menu_sel == '3':
        search()
    elif menu_sel == '4':
        add_on()
    else:
        print('invalid selection')
        while menu_sel !='1' and menu_sel !='2' and menu_sel !='3' and menu_sel !='4':
                menu_sel = input('Please select from options 1,2,3,4 ')
                if menu_sel == '1':
                    SR_reg()
                elif menu_sel == '2':
                    test_reg()
                elif menu_sel == '3':
                    search()
                elif menu_sel == '4':
                    add_on()

        


def SR_reg():#Purpose of this function is to create patient profiles
    while True:
        print("Please enter the following patient details")
        pt_name = input('Full Name: ')
        pt_dob = input('Date of Birth: ')
        pt_ur = input("UR: ")

        pt_list[pt_ur] = {'name':pt_name, 
                    'dob':pt_dob,}
        reset = input ('Press 1 to register another patient or 2 to save and return to the main menu: ')
        print(pt_list)
        if reset == '1':
            continue
        elif reset == '2':
            break
    menu()


def test_reg():
    ur = input(" Please enter the patient's UR number: ")
    for finder in pt_list:
        if finder == ur:
            specimen_num = input(int('How many specimens did you recieve? '))
            for indiv_spec in specimen_num:
                spec_type = input('Please specify each specimen type ')
                specimen_list.append(spec_type)
                print(specimen_list)







    
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
    print('=====================================')
    print('1. Patient Registration')
    print('2. Test Registration')
    print('3. Search')
    print('4. Add-on tests')
    user_guide()

menu()