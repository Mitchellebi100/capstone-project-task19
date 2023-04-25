from datetime import date

# code of variables to store information
AssignedTo = ''
task = ''
AssignedDate = ''
DueDate = ''
TaskCompleted = ''
TaskDescription = ''




#Code to create an empty list
UserDetails = {}
TaskDict = {}
UsernamesList = []
PasswordList = []
TaskList = []

count = 1

with open('user.txt', 'r+') as file1:  # Open the user.txt file.
    for lines in file1:
        newline = lines.strip('\n')  
        SplitLine = newline.split(", ")  

        # code to add the user details into UsernamesList and PasswordList
        UsernamesList.append(SplitLine[0])
        PasswordList.append(SplitLine[1])

        # code to update the UserDetails info
        UserDetails['Username'] = UsernamesList
        UserDetails ['password'] = PasswordList

while True:
    # ====Login Section====

    # code to ask user to log in
    username = input('enter username: ')
    UserPassword = input('enter password: ')

    # code to see if the users username and password is correct
    
    if (username in UsernamesList) and (UserPassword in PasswordList):

        # code to ask user to select options from the menu
        while True:
            menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds - Display statics
        e - Exit
        : ''').lower()

            if menu == 'r':
                '''In this block you will write code to add a new user to the user.txt file
                - You can follow the following steps:
                    - Request input of a new username
                    - Request input of a new password
                    - Request input of password confirmation.
                    - Check if the new password and confirmed password are the same.
                    - If they are the same, add them to the user.txt file,
                    - Otherwise you present a relevant message.'''

                # code to register a new user with a username and password
                NewUsername = input('Enter the new username:')
                password = input('Enter the password:')
                ConfirmPassword = input('Confirm the password: ')

                # code to confirm the new users password
                if password == ConfirmPassword:

                    # code to add the user into the UsernamesList, PasswordList and UserDetails
                    UsernamesList.append( NewUsername)
                    PasswordList.append(ConfirmPassword)

                    # code to update the UserDetails
                    UserDetails['Username'] = UsernamesList
                    UserDetails['password'] = PasswordList

                    # code to open the user.txt file as file2
                    # code to add the new user details
                    with open('user.txt', 'w+') as file2:

                        # code to write the UserDetails using a for loop
                        for i in range(len(PasswordList)):
                            #  code to write the UserDetails into file2
                            file2.write(UserDetails['Username'][i] + ', ' + UserDetails['password'][i] + '\n')
                    print(f'The new user has been registered successfully. ')
                else:
                    print(f'The new user password does not match the confirmed password . ')
            elif menu == 'a':

                '''In this block you will put code that will allow a user to add a new task to task.txt file
                    - You can follow these steps:
                    - Prompt a user for the following:
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and
                    - the due date of the task.
                    - Then get the current date.
                    - Add the data to the file task.txt and
                    - You must remember to include the 'No' to indicate if the task is complete.'''

                # code to ask user about username and task information
                Username = input('Enter the new username: ')
                title_task = input('Enter the title of task: ')
                description = input('Enter the description of the task: ')
                DueDate = input('Enter the due date of the task: (e.g 2022-04-11)')
                TaskCompleted = input('Enter if the task is complete or Not: (Yes or No)')
                current_date = str(date.today())

                # code to udate the task list
                
                TaskList = [Username, task, TaskDescription, AssignedDate, DueDate, TaskCompleted]
                TaskDict[f'Task number {count} information: '] = TaskList

                # code to add information to the task.txt
                task_file = open('tasks.txt', 'w+')
                text = f"""{Username}, Register Users with taskManager.py, Use taskManager.py to add the username \nand passwords for all team members that will be using this program., '\n{current_date},\n{DueDate}, No \n{Username}, {title_task}, {description}, {current_date}, {DueDate},' {TaskCompleted}""".format(
                    Username, current_date, DueDate, Username, title_task, description, current_date, DueDate,
                    TaskCompleted)
                task_file.write('\n' + text)
                task_file.close()  # close file

                def reg_user():

                    run_register = True
                    found_user = False
                    with open("user.txt", "a+") as user_file:
                    while run_register:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    user_file.seek(0)
                    for line in user_file:
                    valid_user, valid_password = line.strip("\n").split(", ")
                    if username == valid_user.strip():
                    print("User already exists.")
                    found_user = True

                    if not found_user:
                    confirm = input("Please confirm password: ")
                    if confirm == password:
                    print("Saving user")
                    user_file.write(f"\n{username}, {password}")
                    user_file.seek(0)
                    run_register = False
                else:
                    print("Passwords do not match. Try again")
                    

            

            elif menu == 'va':
                '''In this block you will put code so that the program will read the task from task.txt file and
                    print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
                    You can do it in this way:
                    - Read a line from the file.
                    - Split that line where there is comma and space.
                    - Then print the results in the format shown in the Output 2 in L1T19 pdf
                    - It is much easier to read a file using a for loop.'''
                #  code to open the task file
                task_file = open('tasks.txt', 'r+')
                TaskDict = {}
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) == 6:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            AssignedTo = last_line[0]
                            AssignedDate = last_line[3]
                            DueDate = last_line[4]
                            TaskCompleted = last_line[-1]
                            TaskDescription = last_line[2]

                            # code to create a TaskList to store all the data
                            TaskList = [username, task, TaskDescription, AssignedDate, DueDate, TaskCompleted]
                text = f'''Task: {task}\nAssigned to: {AssignedTo}\nDate assigned: {AssignedDate}\nDue date: {DueDate}\nTask complete? {TaskCompleted}\nTask description: {TaskDescription}'''.format(task, AssignedTo, AssignedDate, DueDate, TaskCompleted,TaskDescription)

                TaskDict[f'Task number {count} information: '] = TaskList
                count += 1
                print(text)
                print(TaskDict)

            elif menu == 'vm':

                '''In this block you will put code the that will read the task from task.txt file and
                     print to the console in the format of Output 2 presented in the L1T19 pdf
                     You can do it in this way:
                        - Read a line from the file
                        - Split the line where there is comma and space.
                        - Check if the username of the person logged in is the same as the username you have
                        read from the file.
                        - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

                # code to open the task file.
                task_file = open('tasks.txt', 'r+')
                # code to create a count for number of tasks
                task_count = 0
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) % 6 == 0:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            AssignedTo = last_line[0]
                            AssignedDate = last_line[3]
                            DueDate = last_line[4]
                            TaskCompleted = last_line[-1]
                            TaskDescription = last_line[2]
                            TaskList = [AssignedTo, task, TaskDescription, AssignedDate, DueDate, TaskCompleted]
                # code to update the task_list to keep count 
                
                TaskDict[f'Task number {task_count} information: '] = TaskList

                for key in TaskDict :

                    #  code to update the count
                    task_count += 1
                    # code to check if the task is assigned to the user logged in
                    if username == (TaskDict[key][0]):
                        text = f''' Task {str(task_count)}: {str(TaskDict[key][1])}\n'Assigned to: {str(TaskDict[key][0])}'\n'Date assigned: {str(TaskDict[key][3])}'\n'Date: {str(TaskDict[key][4])}'\n'Task Complete? {str(TaskDict[key][5])}'\n'Task Description: {str(TaskDict[key][2])}'''
                        print(text)
                    else:
                        print('The username does not match the person form the file')

            elif menu == 'ds':
                task_file = open('tasks.txt', 'r+')
                TaskDict = {}
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) % 6 == 0:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            AssignedTo = last_line[0]
                            AssignedDate = last_line[3]
                            DueDate = last_line[4]
                            TaskCompleted = last_line[-1]
                            TaskDescription =  last_line[2]

                            # code to create a task_list to store all the above data
                            TaskList = [username, task, TaskDescription, AssignedDate, DueDate,TaskCompleted ]

                TaskDict[f'Task number {count} information: '] = TaskList
                count += 1

                total_user = len(UserDetails['Username'])
                print(f'The total users are: {total_user}')
                print(f'The total task {len(TaskDict)}')

            elif menu == 'e':
                print('Goodbye!!!')
                exit()
    else:
        print('The username and password is not registered ,please make sure you are registered : ')

file1.close()
