import os
import re


class Person:
    moods=("happy","lazy","tired")
    def __init__(self, name, money, mood, healthRate ):
        self__name = name
        self__money = money
        self__mood = mood
        self__healthRate = healthRate

    def sleep(self,hours):
        try:
            if (hours == 7):
                self.__mood =Person.moods[0]
                print('The person is happy')
            elif(hours > 7):
                self.__mood =Person.moods[1]
                print('The person is lazy')
            elif (hours < 7):
                self.__mood =Person.moods[2]
                print('The person is tired')

        except:
            print("error you shoud enter number")

        finally:
            print("we git pearson mood")

    def eat(self,mealsNumber):
        try:
            if (mealsNumber == 3):
                self.healthRate = "100%"
                print('The person is 100% hth')
            elif (mealsNumber ==2):
                self.healthRate = "75%"
                print('The person is 75% hth')
            elif (mealsNumber ==1):
                self.healthRate = "50%"
                print('The person is 50% hth')
        except:
            print("error you shoud enter number")
        finally:
            print("we git pearson mood")


    def buy(self,itemNumber):
        try:
            self.money -= (itemNumber*10)
            print('The person  money', self.mony)
        except:
            print("error you shoud enter number")
        finally:
            print("we git pearson mood")






class Employee(Person):
    def __init__(self,id , car, email, salary, distanceToWork):
        super().__init__( name, money, mood, healthRate ):
        self.__salary=salary
        self.__id=id
        self.__car=car
        self.__email=email
        self.__distanceToWork=distanceToWork

    @staticmethod
    def send_mail(to, subject, msg, receiver_name):
        pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

        if (re.match(pattern, to)):
            emailto = open(f'Emaile to {to}', "w")
            if (emailto.writable()):
                emailto.writelines(["From: from@mail.com ", f"To: {to}"])
                emailto.writelines([f"Hi, Mohamed This is{subject} an email tamplate thanks"])
                if (emailto.readable()):
                    print(emailto.read())
            else:
                print('cannt write in file')
            emailto.close()
        else:
            print("error")


    #methods (work, drive, refuel, send_mail)
    def work(self,hours):
        try:
            if (hours == 7):
                self.__mood = Person.moods[0]
                print('The person is happy')
            elif (hours > 7):
                self.__mood = Person.moods[1]
                print('The person is lazy')
            elif (hours < 7):
                self.__mood = Person.moods[2]
                print('The person is tired')
        except:
            print("error you shoud enter number")

        finally:
            print("we git pearson work hours")

    def drive(self,distance):
        pass

    def refuel(self,gasAmount = 100):
        value=Car.getfuelRate()+gasAmount
        Car.setfuelRate(value)

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.__name=name
        self.__fuelRate=fuelRate
        self.__velocity=velocity

    def getfuelRate(self):
        return self.__fuelRate

    def setfuelRate(self,fuelRate):
        self.__fuelRate=fuelRate

    #methods (run, stop)
    def run (self, velocity, distance):

class Office:
    employees=["mahmoud","ahmed","mohamed"]
    def __init__(self,name, employees):
        self.__name=name
        self.__employees=employees[]

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        employee = self.get_employee(empId)
        if employee:
            self.employees.remove(employee)
            Office.employeesNum -= 1
            return True
        else:
            return False

    def deduct(self, empId, deduction):
        employee = self.get_employee(empId)
        if employee:
            employee.salary -= deduction
            return True
        else:
            return False

    def reward(self, empId, reward):
        employee = self.get_employee(empId)
        if employee:
            employee.salary += reward
            return True
        else:
            return False

    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if employee:
            targetHour = 9
            isLate = self.calculate_lateness(targetHour, moveHour, employee.distanceToWork, employee.car.velocity)
            if isLate:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        move_time = moveHour + time_needed
        if move_time > targetHour:
            return True
        else:
            return False

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num



