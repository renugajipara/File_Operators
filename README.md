🏢 Employee Management System (OOP Wrapper Project)

📌 Project Overview

This project is a Python-based Employee Management System developed using Object-Oriented Programming (OOP) concepts.

The system allows users to:

Create Employees

Create Managers

Create Developers

Display employee details

Exit the system

The project demonstrates important OOP principles like:

Encapsulation

Inheritance

Method Overriding

Method Overloading (using default arguments)

Use of super()

Use of issubclass()


🎯 Objective

The goal of this project is to build an Employee Management System that models employee data and demonstrates core OOP concepts in Python.


🏗️ Project Structure
1️⃣ Employee Class (Base Class)

Attributes:

employee_id

name

age

salary

Features:

Constructor (__init__)

Destructor (__del__)

Getter and Setter methods

Private attributes for encapsulation

display() method to show employee details


2️⃣ Manager Class (Derived Class)

Inherits from Employee

Adds new attribute: department

Overrides display() method

Uses super() to call parent class constructor and methods


3️⃣ Developer Class (Derived Class)

Inherits from Employee

Adds new attribute: programming_language

Overrides display() method

Uses super() to call parent class constructor and methods


🧠 OOP Concepts Used
✅ Encapsulation

employee_id and salary are made private using __.

Getter and setter methods are provided.


✅ Inheritance

Manager and Developer inherit from Employee.


✅ Method Overriding

display() method is overridden in derived classes.


✅ Method Overloading

Constructor uses default arguments to allow multiple ways of creating objects.


✅ super()

Used to call parent class constructor and methods.


✅ issubclass()

Used to verify inheritance relationship.
