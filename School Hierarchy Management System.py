class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Principal(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    
    def display_details(self):
        super().display_details()
        print(f"Designation: Principal")
        print(f"School: {self.school}")
    
    def principal_method(self):
        print("This is the unique method for the Principal class.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_details(self):
        super().display_details()
        print(f"Designation: Teacher")
        print(f"Subject: {self.subject}")
    
    def teacher_method(self):
        print("This is the unique method for the Teacher class.")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def display_details(self):
        super().display_details()
        print(f"Designation: Student")
        print(f"Grade: {self.grade}")
    
    def student_method(self):
        print("This is the unique method for the Student class.")


def main():
    principals = []
    teachers = []
    students = []

    principals.append(Principal("Elon Musk", 45, "Harvard School"))
    teachers.append(Teacher("Bill Gates", 56, "Mathematics"))
    students.append(Student("Jhon Manuel Igdalino", 18, 13))

    while True:
        print("\nSchool Hierarchy System")
        print("1. Create a new Principal")
        print("2. Create a new Teacher")
        print("3. Create a new Student")
        print("4. Display all Principals")
        print("5. Display all Teachers")
        print("6. Display all Students")
        print("7. Perform role-specific action")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter Principal's name: ")
            age = int(input("Enter Principal's age: "))
            school = input("Enter school name: ")
            principals.append(Principal(name, age, school))
            print(f"Principal {name} added successfully!")

        elif choice == '2':
            name = input("Enter Teacher's name: ")
            age = int(input("Enter Teacher's age: "))
            subject = input("Enter subject taught: ")
            teachers.append(Teacher(name, age, subject))
            print(f"Teacher {name} added successfully!")

        elif choice == '3':
            name = input("Enter Student's name: ")
            age = int(input("Enter Student's age: "))
            grade = int(input("Enter Student's grade: "))
            students.append(Student(name, age, grade))
            print(f"Student {name} added successfully!")

        elif choice == '4':
            if not principals:
                print("No Principals to display.")
            else:
                for principal in principals:
                    print("\n--- Principal Details ---")
                    principal.display_details()

        elif choice == '5':
            if not teachers:
                print("No Teachers to display.")
            else:
                for teacher in teachers:
                    print("\n--- Teacher Details ---")
                    teacher.display_details()

        elif choice == '6':
            if not students:
                print("No Students to display.")
            else:
                for student in students:
                    print("\n--- Student Details ---")
                    student.display_details()

        elif choice == '7':
            print("\nSelect role to perform action:")
            print("1. Principal")
            print("2. Teacher")
            print("3. Student")
            role_choice = input("Enter role choice (1-3): ")

            if role_choice == '1' and principals:
                for i, principal in enumerate(principals):
                    print(f"{i+1}. {principal.name}")
                idx = int(input("Select Principal by number: ")) - 1
                if 0 <= idx < len(principals):
                    principals[idx].principal_method()
                else:
                    print("Invalid selection.")

            elif role_choice == '2' and teachers:
                for i, teacher in enumerate(teachers):
                    print(f"{i+1}. {teacher.name}")
                idx = int(input("Select Teacher by number: ")) - 1
                if 0 <= idx < len(teachers):
                    teachers[idx].teacher_method()
                else:
                    print("Invalid selection.")

            elif role_choice == '3' and students:
                for i, student in enumerate(students):
                    print(f"{i+1}. {student.name}")
                idx = int(input("Select Student by number: ")) - 1
                if 0 <= idx < len(students):
                    students[idx].student_method()
                else:
                    print("Invalid selection.")

            else:
                print("No roles of that type exist or invalid choice.")

        elif choice == '8':
            print("Exiting School Hierarchy System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()