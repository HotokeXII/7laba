#лаботаторная работа №7
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def get_info(self):
        return f"Имя: {self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department
    def manage_project(self):
        return f"{self.name} управляет проектами в отделе {self.department}"
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Отдел: {self.department}"

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization
    def perform_maintenance(self):
        return f"{self.name} выполняет обслуживание в области {self.specialization}"
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Специализация: {self.specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        if not self.team:
            return f"{self.name} пока не имеет подчинённых."
        info = f"Команда {self.name}:\n"
        for emp in self.team:
            info += f"- {emp.get_info()}\n"
        return info
    def get_info(self):
        base_info = Manager.get_info(self)  # Вызов метода Manager
        return f"{base_info}, Специализация: {self.specialization}"

employee = Employee("Иван Золо", "001")
manager = Manager("Пи Дидди", "002", "реп индустрия")
technician = Technician("Паша Техник", "003", "треш контент")
tech_manager = TechManager("Егор Сплит", "004", "Яндекс", "Музыкант")

print(employee.get_info())  # пункт 1
print('-')
print(manager.get_info())   # пункт 2
print(manager.manage_project())
print('-')
print(technician.get_info())  # пункт 3
print(technician.perform_maintenance())
print('-')
print(tech_manager.get_info())  # пункт 4
print('-')
tech_manager.add_employee(employee)
tech_manager.add_employee(technician)
print(tech_manager.get_team_info())  # пункт 6
