grade=int(input("Enter your marks: "))

if(grade>=90):
    print("Grade: A")
elif(80>=grade<90):
    print("Grade: B")
elif(grade>=70&grade<80):
    print("Grade: C")
elif(grade>=60&grade<70):
    print("Grade: D")
else:
    print("Grade: F")