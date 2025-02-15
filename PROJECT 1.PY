"""dear sir/madam, i was not having the clarity to code in oops or normally, 
so i did them both this file consists the code using object oriented programing"""

import random as r # importing random libary
import string as string # impoting string libary
class User():
 def username_generator(self,choice):
    adj_list=[ "Cool","Fast", "Happy", "Smart", "Strong", "Brave", "Funny", "Kind", "Lucky","Nice"] # the random adjectives used in the project
    noun_list=["Pikachu","Charizard","Bulbasaur","Squirtle","Jigglypuff","Gengar", "Snorlax", "Lucario","Eevee","Gyarados"] # the random nouns i used in the project(as i am a fan of anime i used some random pokemon names please don't mind)
    a=r.choice(adj_list) # picks one adjective randomly
    y=r.choice(noun_list) # picks one noun randomly
    u=(a+" "+y) # Concatenation of adjective and noun to create a normal username
    z=(u+str(r.randrange(1,99,1))) # concatenation of normal username and random number picked between 1 to 99 using randrange
    o=r.choice(string.punctuation) # concatenation of normal username and random punctuation marks(special characters)
    pos=r.randint(0,len(u)-1)
    t=u[:pos]+o+u[pos:]
  

    if choice.upper() =="N": # if the user selects to add number
     return(z)
    elif choice.upper() == "S": # if the user selects to add special character
     return(t)
    elif choice.upper()== "B": # if the user selects to add both special characters and numbers
     return(t+str(r.randrange(1,99,1)))
    elif choice.upper()=="NONE": # if the user selests none if give the normal username
     return(u)
    else : # if the user's input is none of the above the it's invaild
     print(" Invalid input! Please enter N, S, B, or NONE.")    
    
user_choice=input("please enter your customization: N= only number,S= only special characters, B=both, none=NONE") # takes user's input
username=User()
new_username=username.username_generator(user_choice)
print(new_username)
with open("random usernames.txt","a") as file: # creates and a new text file and adds text to it
    file.write(f"\n{new_username}") # writes to the createdtext file
    print("Username saved successfully to 'random usernames.txt'") # the final output message
    