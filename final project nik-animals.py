nik_animals = ["zebra","elephant","monkey","gorilla"]
def adding (new_animal):
        for i in range(4):
                new_animal=(input("enter animal name:"))
                nik_animals.append(new_animal)
def deleting (delete_animal):
        delete_animal=(input("name an animal to delete:"))
        a= nik_animals.index(delete_animal)
        del nik_animals[a]

def changing (change_animal):
        change_animal=(input("wich an animal do you want to change?:"))
        change_animal2=(input("what is the new animals name?"))
        b= nik_animals.index(change_animal)
        nik_animals[b]=change_animal2 

def Show (show):
        show=print(nik_animals)

while True:
        c=input("what do you want to do?")
        if c=="out":
                print("were closed come next time!")
                break
        elif c=="add":
                adding(nik_animals)
        elif c=="delete":
                delete(nik_animals)
        elif c=="change":
                changing(nik_animals)
        elif c=="show":
                Show(nik_animals)

        else:
                print("unvalid")


