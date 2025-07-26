class chatbook:
    
    __user_id = 0
    
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Default user'
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value
                
        
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
     
    def menu(self):
        user_input = input("""Welcome to chatbook! How would you like to proceed?
                           1. press 1 to signup
                           2. press 2 to login
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any ket to exit
                           
                             """)
        if user_input =='1':
            self.signup()
        if user_input == '2':
            self.signin()
        if user_input == '3':
            self.my_post()
        if user_input == '4':
            self.message_friend()
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
        print("\n")
        self.menu()
            
    def my_post(self):
        if self.loggedin == True:
           post = input("Write your message -> ")
           print(f"You have posted: \"{post}\"")
        else:
            print("Please login first by pressing 2.")
    
        print("\n")
        self.menu()

        
    def message_friend(self):
        if self.loggedin  == True:
            post = input("write your message here ->")
            friend = input("whom to send the message ->")
            print(f"you have sent your message {friend}")
        else:
            print("please signin first to post something")
        print("\n")
        self.menu()
                
             
                                                                                               
user1 = chatbook()
    
    
                
        