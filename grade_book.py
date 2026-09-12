

gradebook = {} 

while True:
    print("\n1. Add Student")
    print("2. Add Grade")
    print("3. Show All")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("Student name: ").strip()
        if name in gradebook:
            print("Student already exists.")
        else:
            gradebook[name] = []
            print(f"{name} added.")

    elif choice == "2":
        name = input("Student name: ").strip()
        if name not in gradebook:
            print("Student not found.")
        else:
            try:
                grade = float(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    gradebook[name].append(grade)
                    print("Grade added.")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade.")

    elif choice == "3":
        if not gradebook:
            print("No students yet.")
        else:
            for name, grades in gradebook.items():
                avg = sum(grades) / len(grades) if grades else 0
                print(f"{name}: Grades={grades}, Avg={avg:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")



