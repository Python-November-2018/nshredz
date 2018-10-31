x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ]. 
#print(x)
#x[1][0] = 15
#print(x)

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
#print(students)
#students[0]["last_name"] = 'Bryant'
#print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?
#for k,v in sports_directory.items():
#    print(f'{k} : {v}')

#sports_directory["soccer"][0] = 'Andres'

#for k,v in sports_directory.items():
#    print(f'{k} : {v}')

# For z, how would you change the value 20 to 30?
#print(z)
#z[0]["y"] = 30
#print(z)

# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.

students2 = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# use range to get the index number and use that to iterate the dict inside the list. to get these all on the same line i hardcoded first_name, last_name in an f string using the values. looping through and using keys() and values() method results with items on separate lines
# def iterateDictionary(list):
#     for i in range(len(list)):
#         print(f'first_name - {list[i]["first_name"]}, last_name - {list[i]["last_name"]}')
# iterateDictionary(students2)

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output
# def iterateDictionary2(key_name, list):
#     for i in range(len(list)):
#         print(list[i][key_name])
# iterateDictionary2('first_name', students2)

# 4. Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has. 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def dojoInfo(mydict):
    print(f'{len(mydict["locations"])} LOCATIONS')
    for i in range(len(mydict["locations"])):
        print(mydict["locations"][i])
    print("\n")
    print(f'{len(mydict["instructors"])} INSTRUCTORS')
    for i in range(len(mydict["instructors"])):
        print(mydict["instructors"][i])
dojoInfo(dojo)
