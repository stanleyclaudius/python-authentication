print('=========')
print('  MENU  ')
print('=========')
print('1. Login')
print('2. Register')
print()

try:
    user_input = int(input('Choose menu: '))
    if user_input == 1:
        login_loop = True
        while login_loop:
            usernameList = []
            passwordList = []
            
            usernameFile = open('username.txt', 'r')
            checkUsername = usernameFile.readlines()
            for i in range(len(checkUsername)):
                usernameList.append(checkUsername[i].strip())
            usernameFile.close()

            passwordFile = open('password.txt', 'r')
            checkPassword = passwordFile.readlines()
            for i in range(len(checkPassword)):
                passwordList.append(checkPassword[i].strip())
            passwordFile.close()

            print()
            user_username = input('Input your username: ')
            user_password = input('Input your password: ')

            curUsername = ''
            curUserID = ''
            for i in range(len(usernameList)):
                usernameList[i] = usernameList[i].split('_')
                if usernameList[i][1] == user_username:
                    curUsername = user_username
                    curUserID = usernameList[i][0]
                else:
                    curUsername = curUsername
                    curUserID = curUserID

            if curUsername != '':
                for i in range(len(passwordList)):
                    passwordList[i] = passwordList[i].split('_')
                    if passwordList[i][0] == curUserID:
                        if passwordList[i][1] == user_password:
                            print()
                            print('Login success!')
                            logout_error = True
                            while logout_error:
                                try:
                                    logout_menu = int(input('Enter 1 to logout: '))
                                    if logout_menu == 1:
                                        curUsername = ''
                                        curUserID = ''
                                        print('You have been logout!')
                                        login_loop = False
                                        logout_error = False
                                    else:
                                        print('Logout failed!')
                                except:
                                    print('Logout failed!')
                        else:
                            print('Credentials not found!')
            else:
                print('Credentials not found!')
            
    elif user_input == 2:
        regis_loop = True
        while regis_loop:
            print()
            
            openUsernameList = open('username.txt', 'r')
            showOpenUsernameList = openUsernameList.readlines()
            showOpenUsernameListLength = len(showOpenUsernameList)
            openUsernameList.close()

            openPasswordList = open('password.txt', 'r')
            showOpenPasswordList = openPasswordList.readlines()
            showOpenPasswordListLength = len(showOpenPasswordList)
            openPasswordList.close()
            
            user_username = input('Input your username: ')
            user_password = input('Input your password: ')
            user_password_confirmation = input('Re-type your password: ')

            if user_password == user_password_confirmation:
                if len(user_password) >= 8:
                    valid_username_check = True
                    used_username = []
                    
                    for i in range(showOpenUsernameListLength):
                        showOpenUsernameList[i] = showOpenUsernameList[i].strip()
                        used_username.append(showOpenUsernameList[i])
                        
                    for i in range(len(used_username)):
                        used_username[i] = used_username[i].split('_')
                        if used_username[i][1] == user_username:
                            valid_username_check = False
                        else:
                            valid_username_check = valid_username_check

                    if valid_username_check == True:
                        usernameFile = open('username.txt', 'a')
                        passwordFile = open('password.txt', 'a')
                                    
                        usernameCounter = showOpenUsernameListLength + 1
                        if usernameCounter <= 0:
                            usernameFile.write(str(usernameCounter) + '_' + user_username)
                        else:
                            usernameFile.write(str(usernameCounter) + '_' + user_username + '\n')
                            usernameFile.close()

                        passwordCounter = showOpenPasswordListLength + 1
                        if passwordCounter <= 0:
                            passwordFile.write(str(passwordCounter) + '_' + user_password)
                        else:
                            passwordFile.write(str(passwordCounter) + '_' + user_password + '\n')
                            passwordFile.close()

                        print()
                        print('Account has been created!')
                        regis_loop = False
                    else:
                        print('Account has been used before!')
                else:
                    print('Password should be at least 8 characters!')
            else:
                print('Password confirmation does not match!')
    else:
        print('Menu Not Found!')
except:
    print('Choose menu by number!')
