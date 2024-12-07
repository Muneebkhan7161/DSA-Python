print("=== Lists ===")
number_list = [10, 20, 30, 40, 50, 60, 70]
number_list.append(80)  
number_list.remove(20) 
print("List after operations:", number_list)
number_list.reverse()
print(number_list)  

print("=== Tuples ===")
numbres = (1, 2, 3, 4, 5)
print("Tuple:", numbres)
print("Accessing element at index 3:", numbres[3]) 

print("=== Dictionaries ===")
my_dict = {
    "name": "Muhammad",
    "age": 26,
    "city": "karachi"
}
my_dict["age"] = 26  
my_dict["job"] = "Devops Engineer"
del my_dict["city"]  
print("Dictionary after operations:", my_dict)
print("Keys:", list(my_dict.keys()))  
print("Values:", list(my_dict.values()))  

print("=== Sets ===")
sets_numbers = {1, 2, 3, 4, 5}
sets_numbers.add(6)  
sets_numbers.discard(3)  
sets_numbers.update([7, 8, 9])  

print("Set after operations:", sets_numbers)
print ("Checking if 5 is in set:", 5 in sets_numbers)