# 1).

class Counter():
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_value):
        pass

    def set_min(self, min_value):
        pass

    def step_up(self):
        self.current += 1

    def step_down(self):
        self.current -= 1

    def get_current(self):
        print(self.current)


counter = Counter()
counter.set_current(2)
counter.step_up()
counter.step_up()

counter.get_current()


# 2).

class Human:
    def __init__(self, gender, first_name, last_name, age):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age} years old\nGender:{self.gender}"


class Student(Human):
    def __init__(self, gender, first_name, last_name, age, record_book):
        super().__init__(gender, first_name, last_name, age)
        self.record_book = record_book

    def __str__(self):
        return f"Record Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        if all_students:
            return f"Group {self.number}:\n{all_students}"
        else:
            return f"Group {self.number} is empty."


st1 = Student("Male", "Steve", "Jobs", 30, "AN142")
st2 = Student("Female", "Liza", "Taylor", 25, "AN145")
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
gr.find_student("Jobs")
gr.find_student("Jobs2")  # None

gr.delete_student('Taylor')
gr.delete_student('Jobs')
print(gr)  # Only one student


# 3).

class Rectangle:
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Width and height must be numbers")
        self.width = width
        self.height = height

    def __str__(self):
        return f"Width: {self.width}\nHeight: {self.height}"


print(Rectangle(5, 3))


# 4).

class Temperature:
    def __init__(self, temp):
        if not isinstance(temp, (int, float)):
            raise TypeError("Temperature is not a number")
        self.temp = temp

    def to_fahrenheit(self):
        return f"Fahrenheit: {(self.temp * 1.8) + 32}"

    def to_kelvin(self):
        return f"Kelvin: {self.temp + 273.15}"


counter = Temperature("5")
printer1 = counter.to_fahrenheit()
printer2 = counter.to_kelvin()
print(printer1)
print(printer2)


# 5).

class User:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise ValueError("Name must be strings")
        if not isinstance(age, (int, float)):
            raise ValueError("Age must be numbers")
        self.name = name
        self.age = age

    def test_name(self):
        return f"Name: {self.name}"

    def test_age(self):
        return f"Age: {self.age}"


counter = User("Ann", "Five")
printer1 = counter.test_name()
printer2 = counter.test_age()
print(printer1)
print(printer2)


# 6).

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numbers")
        self.amount = amount
        if self.amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= self.amount
        return self.balance


counter = BankAccount(5000, "Denys Herzhyk")
printer1 = counter.withdraw(6000)
print(printer1)
