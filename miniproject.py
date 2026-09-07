
pt_dict ={} # creates and empty list so that each patient that is created in the SR_reg function can be accessed outside of the function
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
    else: #if the user enters a number that is not present they will be prompted to choose a menu item form 1-4. As there is a while loop this will continue until the user enters an acceptable option 
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



def SR_reg():# This function will create patient profiles which will later be used to register tests under
    while True:
        print("Please enter the following patient details")
        pt_name = input('Full Name: ')
        pt_dob = input('Date of Birth: ')
        pt_ur = input("UR: ") #UR number is a unique numerical patient identifier
        #Here I am creating a patient dictionary within a dictionary the first key would be the patient's unique medical record number (UR) and the secondary dictionary contains the patient's name and date of birth
        pt_dict[pt_ur] = {'name':pt_name,'dob':pt_dob,} #Here I am adding the patient details to the patient dictionary. Which will create a dictionary within a dictionary. The first key of the first dictionary is the patient's ur number and within that dicionary is another dictionary that contains the patient's name and dob
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
                tests_list = []
                for specimens in range(specimen_num):
                    spec_type = input(f'Please specify specimen {specimens + 1} ')
                    spec_test = input(f'Please enter all tests requested on the {spec_type} tube ')
                    check_1 = input ('Is the fube adequately filled? (Y or N)')
                    check_2 = input ('Is the tube fully labelled? (Y or N)')
                    if check_1 == 'N' and check_2 == 'N':
                        print('Organise specimen recollection')
                    elif check_1 == 'N' and check_2 == 'Y':
                        print('Consult with senior scientist')
                    elif check_1 == 'Y' and check_2 == 'N':
                        print('Call nurse to label tube')
                    else:
                        tests_list.append(spec_test)
                        tests_dict[ur] = tests_list
                    

                    specimens_list.append(spec_type)
                specimen_list_dict[ur] = specimens_list

                reset = input('To register tests for another patient please enter 1 to return to the main menu press 2 ')
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

def add_on():
    pass


#Creates a menu so that the user can pick which function to invoke
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