import math

#Day 2: 30 Days of python programming

#EXERCISE 1

first_name = "Marlon"
last_name = "Rivera"
full_name = "Marlon Gabriel Rivera Martinez"
country = "Italy"
city = "venice"
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False
this, is_another, person,edad, casada = "esta", "es", "Laura", 26, False 

#EXERCISE 2

type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(this)
type(is_another)
type(person)
type(edad)
type(casada)


print(len(first_name))
print(len(last_name))
dife = len(first_name) - len(last_name)
print(f"there is no difference in the length of both my name: {dife}")


num_one = 5
num_two = 4

total = num_one + num_two

diff = num_two - num_two

product = num_two * num_one

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

# the radius of a circle is 30 meters
PI = 3.14159

area_of_circle = PI * math.pow(30, 2)
circum_of_circle = 2 * PI * 30

#input return a string and we need an real number so math.pow can work
radius = input("please give me a radius: ")
#so we transform it with the built-in function int()
transform = int(radius)
area_calculated = PI * math.pow(transform, 2)


print(f"the area of 30 meter radius circle is: {area_of_circle}")
print(f"the circumference of a 30 meter radius circle is: {circum_of_circle}")
print("----------------------------")
print(f"the area of the circle that you gave me is: {area_calculated}")



name_user = input(f"please enter you name: ")
last_user = input(f"please enter your last name: ")
country_user = input("please enter your country of citizenchip: ") 
age_user = input(f"please enter your age: ")

print(f"here it is the info that you gave me: {name_user}, {last_name}, {country_user}, {age_user}")