import datetime


def teachers_day_greeting():
    today = datetime.date.today()
    
    teacher_name = input("Enter your teacher's name: ").strip()
    if not teacher_name:
        print("You didn't enter a name. Exiting...")
        return
    
    print("\n" + "="*50)
    print(f"🎉 Happy Teacher's Day, {teacher_name}! 🎉")
    print("="*50)
    
    heart = """
     **     **  
    ****   **** 
   ****** ****** 
    ***********  
     *********   
      *******    
       *****     
        ***      
         *       
    """
    print(heart)
    print(f"Dear {teacher_name},\n")
    print("Thank you for your guidance, patience, and inspiration.")
    print("You make learning a wonderful journey! 🌟")
    print(f"Date: {today.strftime('%d %B %Y')}")
    print("="*50)
    def generate_heart():
        import math

    # Loop over y coordinates of the heart
    for y in range(15, -15, -1):
        line = ""
        # Loop over x coordinates
        for x in range(-30, 30):
            # Normalize x and y to fit heart equation
            x_norm = x * 0.05
            y_norm = y * 0.1
            # Heart equation (Mathematical formula)
            equation = (x_norm**2 + y_norm**2 - 1)**3 - x_norm**2 * y_norm**3
            if equation <= 0:
                line += "*"
            else:
                line += " "
        print(line)


if __name__ == "__main__":
    teachers_day_greeting()
