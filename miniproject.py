
pt_dict ={} #Creates and empty string to populate pt list
tests_dict = {}
specimen_list_dict = {}


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
        #Here I am creating a patient dictionary within a dictionary the first key would be the patient's unique medical record number (UR) and the secondary dictionary contains the patient's name and date of birth
        pt_dict[pt_ur] = {'name':pt_name,'dob':pt_dob,}
        reset = input ('Press 1 to register another patient or 2 to save and return to the main menu: ')
        print(pt_dict)
        if reset == '1':
            continue
        elif reset == '2':
            break
    menu()


def test_reg():
    while True:
        ur = input(" Please enter the patient's UR number: ")
        if ur in pt_dict:
                specimen_num = int(input('How many specimens did you recieve? '))
                specimens_list = []
                for specimens in range(specimen_num):
                    spec_type = input('Please specify each specimen type ')
                    new_specimen_list = specimens_list.append(spec_type)
                reset = input('To register another patient enter 1 to return to the main menu press 2 ')
                if reset == '1':
                    continue
                elif reset =='2':
                    break

        else:
            print('Patient does not exist. Please complete patient registration')
            SR_reg()
    menu()
    
def search():
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