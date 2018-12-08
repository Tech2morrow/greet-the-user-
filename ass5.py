import datetime
currentTime = datetime.datetime.now()

def printing(b):
    d = "\t"
    c = b +d+ a
    print(c)


def update(a):

    if currentTime.hour < 12:
        printing('Good morning.')
    elif 12 <= currentTime.hour < 18:
        printing('Good afternoon.')
    else:
        printing('Good evening.')



a=input("Enter your Name : ")

update(a)
