val = int(input("enter a number: "))
if val > 100:
    val = val/2
else:
        val = val*2
print('.. The result is:', val)


#true if condition else false situation
val = int(input("enter a number: "))
val =  val/2 if val> 100 else val*2
print('.. The result is:', val)



name = input("enter your name")
if name.isalpha():
    print("very good")
else:
    print("not good")


#oneliner
name = input("enter your name")
print ("very good") if name.isalpha() else print("not good")



