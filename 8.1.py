personaldata = {"name" : "nadhifah chairunnisa",
                "NIM" : "L200184137",
                "address" : "sidoarjo, east java",
                "majors" : "International of Informatics Enginering",
                "faculty" : "FKI",
                "religion" : "islam",
                "hobby" : "reading"}
def name() :
    print (personaldata["name"])
def NIM() :
    print (personaldata["NIM"])
def address() :
    print (personaldata["address"])
def majors() :
    print (personaldata ["majors"])
def faculty() :
    print (personaldata ["faculty"])
def religion() :
    print (personaldata ["religion"])
def hobby() :
    print (personaldata ["hobby"])

def x() :
    print ( """ optin available :
-x display the choice
-1 display the name
-2 display the NIM
-3 display the address
-4 display the majors
-5 display the faculty
-6 display the religion
-7 display the hobby
-0 close the program""")
x()

while True:
    y = input("your choice: ")
    if y == "x" :
        x()
    elif y == "1":
        name ()
    elif y == "2" :
        NIM()
    elif y == "3" :
        address()
    elif y == "4" :
        majors ()
    elif y == "5" :
        faculty()
    elif y == "6" :
        religion ()
    elif y == "7" :
        hobby ()
    elif y == "0" :
        print ("The Program is Closed")
        break
    else  :
        print ("invalid")
