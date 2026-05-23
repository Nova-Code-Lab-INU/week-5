# The Foundation: Encapsulation

class NovaMember:
    def __init__(self, name, member_id, evaluation_score):
        self.name = name
        self.member_id = member_id
        # Encapsulation: Using double underscores (__) to make it a Private Attribute
        self.__evaluation_score = evaluation_score

    def show_profile(self):
        print(f"--- Member Profile ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.member_id}")
        print("----------------------")

# The Hierarchy: Inheritance

class NovaStudent(NovaMember):
    def __init__(self, name, member_id, evaluation_score, assigned_project):
        # Inherit base features from NovaMember
        super().__init__(name, member_id, evaluation_score)
        self.assigned_project = assigned_project

    # Behavioral Intelligence: Polymorphism
    def execute_duty(self):
        print(f"Architecting the project: [{self.assigned_project}]... Status: In Progress.")

class NovaAdmin(NovaMember):
    def __init__(self, name, member_id, evaluation_score, access_level):
        # Inherit base features from NovaMember
        super().__init__(name, member_id, evaluation_score)
        self.access_level = access_level

    # Behavioral Intelligence: Polymorphism
    def execute_duty(self):
        print(f"Security Protocol Active. Admin [{self.name}] is reviewing the system logs.")

#  System Interaction (The Simulation) 

if __name__ == "__main__":
    # Instantiate Objects
    # Creating a student (teammate) and an admin (Lead/Instructor)
    student = NovaStudent("Ahmad", "S2024", 92, "AI Health Bot")
    admin = NovaAdmin("Dr. Qais", "A001", 100, "Full Control")

    # Demonstrate Inheritance: Calling show_profile() for both
    print("Testing Inheritance:")
    student.show_profile()
    admin.show_profile()

    # Demonstrate Polymorphism: Calling execute_duty()
    print("\nTesting Polymorphism:")
    student.execute_duty()
    admin.execute_duty()

    # Demonstrate Encapsulation: Attempt to print private attribute
    print("\nTesting Encapsulation:")
    try:
        # This will trigger an AttributeError
        print(student.__evaluation_score)
    except AttributeError:
        # EXPLANATION: This causes an error because '__evaluation_score' is private. 
        # In OOP, we encapsulate sensitive data to prevent direct access/modification 
        # from outside the class, ensuring system security and integrity.
        print("Error: Access Denied. Cannot access '__evaluation_score' directly from the main code.")