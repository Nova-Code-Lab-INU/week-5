class NovaMember:
    def __init__(self, name, member_id, evaluation_score):
        self.name = name
        self.member_id = member_id
        self.__evaluation_score = evaluation_score

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")


class NovaStudent(NovaMember):
    def __init__(self, name, member_id, evaluation_score, assigned_project):
        super().__init__(name, member_id, evaluation_score)
        self.assigned_project = assigned_project

    def execute_duty(self):
        print(f"Architecting the project: {self.assigned_project}... Status: In Progress.")


class NovaAdmin(NovaMember):
    def __init__(self, name, member_id, evaluation_score, access_level):
        super().__init__(name, member_id, evaluation_score)
        self.access_level = access_level

    def execute_duty(self):
        print(f"Security Protocol Active. Admin {self.name} is reviewing the system logs.")


student = NovaStudent("Jana", 101, 95, "AI Bot")
admin = NovaAdmin("Rahaf", 1, 100, "Full Control")

student.show_profile()
student.execute_duty()

admin.show_profile()
admin.execute_duty()

print(student.__evaluation_score)