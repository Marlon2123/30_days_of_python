#examples of data tipe

i = 10
f = 1.3
c = 3-4j
s = "Hello World"
b = True
l = ["Hola", "Hello", "chao", "bye"]
t = ("Hola", "Hello", "chao", "bye")
s = {"Hola", "Hello", "chao", "bye"}
d = {
    "hi_spa": "Hola",
    "hola_eng": "Hello",
    "bye_esp": "chao",
    "chao_eng": "bye"
}
print( i, f, c, s, b, l, t, s, d)



import math


#Euclidian distance

#between (2, 3) and (10, 8)

x_1 = 2
y_1 = 3

x_2 = 10
y_2 = 8

distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

print(distance)