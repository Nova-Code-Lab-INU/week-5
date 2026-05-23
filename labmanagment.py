
# FINAL PROJECT NOVA CODE LAB MANAGEMENT

class NovaMember:

    def __init__(self, name, member_id, evaluation_score):
        self.name = name
        self.member_id = member_id

        self.__evaluation_score = evaluation_score

  
    def show_profile(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)

class NovaStudent(NovaMember):

    def __init__(self, name, member_id, evaluation_score, assigned_project):

        super().__init__(name, member_id, evaluation_score)

        self.assigned_project = assigned_project

    def execute_duty(self):
        print("Architecting the project:",
              self.assigned_project,
              "... Status: In Progress.")

class NovaAdmin(NovaMember):

    def __init__(self, name, member_id, evaluation_score, access_level):

        super().__init__(name, member_id, evaluation_score)

        self.access_level = access_level
      
    def execute_duty(self):
        print("Security Protocol Active. Admin",
              self.name,
              "is reviewing the system logs.")
# MAIN PROGRAM

student1 = NovaStudent(
    "Mohammad",
    "NS101",
    95,
    "AI Bot"
)

admin1 = NovaAdmin(
    "Ola",
    "AD500",
    100,
    "Full Control"
)

# Show Profiles
print("===== STUDENT PROFILE =====")
student1.show_profile()

print("\n===== ADMIN PROFILE =====")
admin1.show_profile()

# Execute Duties
print("\n===== DUTIES =====")
student1.execute_duty()
admin1.execute_duty()
