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
            self.signup()
        if user_input == '2':
            self.signin()
        if user_input == '3':
            pass
        if user_input == '4':
            pass
        else:
            exit()
            
    def signup(self):
        email = input('enter your email_id ->')
        password = input('your password ->')
        self.username = email
        self.password = password
        print(f'Welcome {self.username}, you have successfully signed up!')
        self.menu()
        
    def signin(self):
        if self.username == " " and self.password == " ":
             print("please signup by pressing 1")
        else:
            username = input("enter your email id ->") 
            password = input("enter your password ->")
        if self.username == username and self.password == password:
           print("you have logged in successfully")
           self.loggedin = True
        else:
            print('please enter your credential correctly')
        self.menu()
            
     
        
                                                                                        
obj = chatbook()
    
    
                
        