# import statements.
<<<<<<< HEAD
from globals import friends,Spy
from termcolor import colored
from spy_details import spy
# add new friends.
import re
def add_friend():
    new_friend =Spy(" "," ",0,0.0,False)
    tempcheck=True#temporary variable
    #Validation Using Regex
    patternsalutation='^Mr|Ms$'
    patternname='^[A-Za-z][A-Za-z\s]+$'
    patternage='^[0-9]+$'
    patternrating='^[0-9]+\.[0-9]$'
    #Validating Each Values Using Regular Expression
    while tempcheck:
        salutation = raw_input("Mr. or Ms.? : ")
        if (re.match(patternsalutation, salutation) != None):
            tempcheck = False
        else:
            print colored("Enter Again!",'red')
    tempcheck=True
    while tempcheck:
        new_friend.Name=raw_input("Enter Name: ")
        if(re.match(patternname,new_friend.Name)!=None):
            tempcheck=False
        else:
            print colored("Enter Again!!!!",'red')

    # concatenation.
    new_friend.Name = salutation + "."+new_friend.Name
    tempcheck=True
    while tempcheck:
        new_friend.Age = raw_input("Age?")
        if (re.match(patternage, new_friend.Age) != None):
            tempcheck = False
            new_friend.Age=int(new_friend.Age)
        else:
            print colored("Enter Again!!!!",'red')
    tempcheck=True #temporary variable
    while tempcheck:
        new_friend.Rating = raw_input("Spy rating?")
        if (re.match(patternrating, new_friend.Rating) != None):
            tempcheck = False
            new_friend.Rating=float(new_friend.Rating)
        else:
            print colored("Enter Again!!!!",'red')
    # validating input:: AGE and RATING,i.e.,
    #Age b/w 12 and 50
    #Rating b/w 0.0 to 5.0
    #Friends Rating must be greater than or equal to User Rating
    if new_friend.Rating <= 5.0 and new_friend.Age > 12 and new_friend.Age < 50 and new_friend.Rating>=spy.Rating:
        # add_friend
        friends.append(new_friend)
        print colored("Friend Added",'green')
    else:
        print colored("Sorry invalid entry!!!!",'red')
    # returning number of friends
    return len(friends)
=======
from globals import friends


# add new friends.
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation']= raw_input("Are they Mr. or Ms.?: ")

    # concatination.
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(raw_input("Age? "))

    new_friend['rating'] = float(raw_input("Spy rating? "))

    # users input validations
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    # returning total no of friends.
    return len(friends)
>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39
