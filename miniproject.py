
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
        reset = input ('Press 1 to register another patient or 2 to save and return to the main menu: ') #If the user wishes to create another patient profile the function will continue if the user wishes to return to the main menu they will press 2 and this will break the while loop and menu() function will be called.
        if reset == '1':
            continue
        elif reset == '2':
            break
    menu()

#The purpose of the test_reg() is to allow the user to register tests that the doctor has requested for a particular patient
def test_reg():
    while True: #while True code is used to allow the user to register tests for multiple patients
        ur = input(" Please enter the patient's UR number: ")
        if ur in pt_dict: #This if statment will check to see whether the patient exists within the program.
                specimen_num = int(input('How many specimens did you recieve? '))
                specimens_list = [] #Here we create an empty specimen so that all specimens or tests can be grouped together
                tests_list = [] #Lists are placed within the function so that with each registration they are emptied.
                #In this for statment we are asking what type of specimen the user has recieved and  what tests have been ordered for it
                #Then we are performing quality checks on it to ensure that it is suitable for testing i.e. blood tubes are filled, and fully labelled
                for specimens in range(specimen_num):
                    spec_type = input(f'Please specify specimen {specimens + 1} ')
                    spec_test = input(f'Please enter all tests requested on the {spec_type} tube ')
                    check_1 = input ('Is the tube adequately filled? (Y or N)')
                    check_2 = input ('Is the tube fully labelled? (Y or N)')
                    #These boolean statments provide the user with instruction of what to do with each possible outcome.
                    #If the outcome does not require a recollect then the tests are added to the tests dictionary
                    if check_1 == 'N' and check_2 == 'N':
                        print('Organise specimen recollection')
                    elif check_1 == 'N' and check_2 == 'Y':
                        print('Consult with senior scientist')
                        tests_list.append(spec_test)
                        tests_dict[ur] = tests_list
                    elif check_1 == 'Y' and check_2 == 'N':
                        print('Call nurse to label tube')
                        tests_list.append(spec_test)
                        tests_dict[ur] = tests_list
                    else:
                        tests_list.append(spec_test)
                        tests_dict[ur] = tests_list
        
                #The following boolean statments allow for the user to enter another patient or to return to the main menu
                reset = input('To register tests for another patient please enter 1 to return to the main menu press 2 ')
                if reset == '1':
                    continue
                elif reset =='2':
                    break

        else: #if the patient does not exist in the program the user will be prompted to complete patient registration and the SR_reg() function is called.
            print('Patient does not exist. Please complete patient registration')
            SR_reg()
    menu()
    
def search():
    ur = input("Please Enter the Patient's UR: ")
    if ur in pt_dict:
        pass


    else:
        print('Patient does not exist. Please complete patient registration')
        SR_reg()
        

#   Patient Detais
#========================
# Name: 
# DOB: 
#UR: 
# Tests registered: 
# Tubes collected: 
#=========================


#Creates a menu so that the user can pick which function to invoke
def menu(): 
    print('====================================')
    print('          Specimen Menu               ') 
    print('=====================================')
    print('1. Patient Registration')
    print('2. Test Registration')
    print('3. Search')
    user_guide()

menu()