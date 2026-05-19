#base class
class NovaMember:

    def __init__(self, name, member_id, evaluation_score):
        self.name = name
        self.member_id = member_id

        # private Attribute
        self.__evaluation_score = evaluation_score

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.member_id}")


# child classes
class NovaStudent(NovaMember):

    def __init__(self, name, member_id, evaluation_score, assigned_project):

        #inherit from parent class
        super().__init__(name, member_id, evaluation_score)

        self.assigned_project = assigned_project

class NovaAdmin(NovaMember):

    def __init__(self, name, member_id, evaluation_score, access_level): 
        
        #inherit from parent class
        super().__init__(name, member_id, evaluation_score)

        self.access_level = access_level

    def execute_duty(self):
        print(f"Security Protocols Active. Admin {self.name} is reviewing the system logs.")


#Objects
student1 = NovaAdmin("Marah", 101, 95, "AI bot")

admin1 = NovaAdmin("Ola", 500, 100, "Full Control")


#show_profile
student1.show_profile()
print()

admin1.show_profile()
print()

#execute_duty
student1.execute_duty()
admin1.execute_duty()

print()

#encapulation test
#this will cause an error because __evaluation_score is private and cannot be accessed directly
#print(student1.__evaluation_score)