import random 
if __name__=="__main__":
   
   obj = random.Random()
   for index in range(10):
    aadhar_no = str(obj.randint(1000 , 9999)) + "" +\
                str(obj.randint(1000 , 9999)) + "" +\
                str(obj.randint(1000 , 9999)) 
    print(aadhar_no)
    
    arr_1 = list(range(0,101))
    print(arr_1)

    print("-" * 40)

    random.shuffle(arr_1)
    print(arr_1)

    students_list=["jack","lucy","Merry","william","Rani","Rohit","Roshni"]
    for index in range(3):
        student=random.choice(students_list)
        print(student)

    lot_no=list(range(1000,9999))    

    for index in range(3):
        num=random.choice(lot_no)
        print(num)