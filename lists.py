#Lists

#Task 1: Accessing a value
prog_languages = ['Javascript', 'Python','Java', 'Django', 'React']
print(prog_languages[1])

#Task 2: adding and changing values
instructors = ['Nevin', 'Mike', 'Jake', 'Dan', 'Megan']
print(instructors)
instructors.append('Dan')
instructors.append('James')
instructors.append('John-boy')
print(instructors)
instructors[3] = 'Danimal'
print(instructors)

#Task 3: popping a value
not_teaching = instructors.pop()
print(instructors)

#Task 4: removing a value
instructors.remove('Mike')
print(instructors)

#Task 5:looping over a list
list1 = ['fan', 'bull-', 'high-', 'barrel-o-', 'slap']
list2 = ['dango', 'rider', 'horse', 'monkeys', 'stick']

for number in range(len(list1)):
    print(list1[number] + list2[number])
# combination of two lists alternating elements -> print(list1[0] + list2[0])


#Task 6: list function

instructors2 = ['Nevin', 'Jake', 'Danimal', 'Megan', 'Dan', 'James']
new_instructor = input('Enter your name: ')
found = False

for name in instructors2:
    if new_instructor == name:
        found = True
        
if found == True:
    print('That name has been taken, provide a nickname')
else:
    print('That name is available')
    instructors2.append(new_instructor)
print(instructors2, len(instructors2))

#Bonus lists tasks
#Task 7
#concat method
destinations1 = ['Mexico', 'Germany']
destinations2 = ['Japan', 'Sweden', 'Switzerland']
print(destinations1 + destinations2)

#.append() 
destinations1 = ['Mexico', 'Germany']
destinations2 = ['Japan', 'Sweden', 'Switzerland']
for places in destinations2:
    destinations1.append(places)
print(destinations1)

#.extend 
destinations1 = ['Mexico', 'Germany']
destinations2 = ['Japan', 'Sweden', 'Switzerland']
destinations1.extend(destinations2)
print(destinations1)

#Task 8
#.append()
fav_vehicles = ['Subway', 'Tram', 'Bike']
my_fav_vehicles = []
for vehicles in fav_vehicles:
    my_fav_vehicles.append(vehicles)
print(my_fav_vehicles)

#.copy() 
fav_vehicles = ['Subway', 'Tram', 'Bike']
my_fav_vehicles = fav_vehicles.copy()
print(my_fav_vehicles)

#list(var) 
fav_vehicles = ['Subway', 'Tram', 'Bike']
my_fav_vehicles = list(fav_vehicles)
print(my_fav_vehicles)

#Task 9

#.sort()
fav_dishes = ['pozole', 'sopes', 'nigiri', 'aguachile', 'pulpo']
fav_dishes.sort()
print(fav_dishes)

fav_dishes = ['pozole', 'sopes', 'nigiri', 'aguachile', 'pulpo']
fav_dishes.sort(reverse = True)
print(fav_dishes)

fav_dishes = ['pozole', 'sopes', 'nigiri', 'aguachile', 'pulpo']
fav_dishes.reverse()
print(fav_dishes)

# loop
print('a' < 'b')
print('a' > 'b')

print('pozole' > 'sopes')

fav_dishes = ['pozole', 'sopes', 'nigiri','aguachile', 'pulpo']
sorted_list = []

for dish in fav_dishes:
    if fav_dishes[0] > fav_dishes[1]:
        new_dish = dish
        sorted_list.append(new_dish)
print(sorted_list)  

fav_dishes = ['pozole', 'sopes', 'nigiri','aguachile', 'pulpo']

for dish in range(0, len(fav_dishes) - 1):
    for new_dish in range(dish + 1, len(fav_dishes)):
        if(fav_dishes[dish] > fav_dishes[dish]):
            fav_dishes[dish], fav_dishes[new_dish] = fav_dishes[new_dish], fav_dishes[dish]
    print(fav_dishes)
print('Sorted list: ')
print(fav_dishes)