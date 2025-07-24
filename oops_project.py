class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input("""Welcome to chatbook! How would you like to proceed?
                           1. press 1 to signup
                           2. press 2 to login
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any ket to exit""")
        if user_input =='1':
            pass
        if user_input == '2':
            pass
        if user_input == '3':
            pass
        if user_input == '4':
            pass
        else:
            exit()
            
        obj = chatbook()
    
                
        