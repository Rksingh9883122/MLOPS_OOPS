#from oops_project import chatbook
#user1 = chatbook()
#user1.name
#print(user1.name)
#print(user1._chatbook__name)


#getter & Setter
#print(user1.get_name())
#user1.set_name('agent x')
#print(user1.get_name())


# Assiging diffrent user ids
from oops_project import chatbook
user1 = chatbook()
print(user1.id)


## Using Static method 
chatbook.__user_id = (10)
user2 = chatbook()
print(user2.id)
# print(user1.user_id)

#user2 = chatbook()
#print(user2.user_id)

#user3 = chatbook()
#print(user3.user_id)

