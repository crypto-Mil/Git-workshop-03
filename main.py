import alex, Emil, louise, niclas

name = input ("Vad heter du? ")

print(name)

if name.lower() == "alex":
    pass
elif name.lower() == "emil":
    pass
elif name.lower() == "louise":
    louise.print_hello()
elif name.lower() == "niclas":
    niclas.hello_niclas()
elif name.lower() == "pasta":
    louise.fav_food()
elif name.lower() == "coke":
    niclas.drink()