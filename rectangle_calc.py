print("----cool_step mod on----")

def cool_step():
    try:
        side1 = int(input("give aayat l. :")) # l = aayat ki lambai
        side2 = int(input("give aayat b. :")) # b = aayat ki chodai
        
        
        area = side1 * side2
        perimeter = 2 * (side1 + side2)
        
        
        print("aayat ka area is :", area)
        print("aayat ka perimeter is :", perimeter)
       
    except ValueError: 
        print("Please Enter valid integer ")

while True:
    cool_step()
    
    choise = input("Kay aap ishe repit karan chahate hai ? (Yes/No): ").lower()
    
    # .lower() लगाने से यूजर 'No' या 'no' कुछ भी लिखेगा तो कोड रुक जाएगा
    if choise.lower() == "yes":
    	cool_step()
    else:
    	print("--Good By-- \n cool_step mod off ")
    	break
    
     



