# ⚖️ BMI Calculator

A simple and interactive **Python-based BMI Calculator** that calculates a user's **Body Mass Index (BMI)** based on their weight and height.

The application also classifies the calculated BMI into categories such as **Underweight, Normal, Overweight, and Obese**, while providing input validation and error handling.

---

## 📌 Project Overview

This project was developed as part of the **Python Programming Virtual Internship at Oasis Infobyte**.

The application accepts the user's weight in kilograms and height in meters, calculates their BMI, and displays the corresponding BMI category.

It also includes input validation, exception handling, and an option to perform multiple BMI calculations within the same program session.

---

## ✨ Features

* ⚖️ Calculate BMI using weight and height
* 📏 Accept height in meters
* 🏋️ Accept weight in kilograms
* 🧮 Calculate BMI using the standard formula
* 📊 Classify BMI into different categories
* ⚠️ Handle invalid and non-numeric input
* 🚫 Prevent zero or negative values
* 🔁 Allows users to perform multiple calculations
* 🛡️ Uses exception handling for input errors
* 🖥️ Simple and interactive command-line interface

---

## 🧠 How It Works

The BMI calculation process follows a simple flow:

```text
👤 User
   ↓
⚖️ Enter Weight
   ↓
📏 Enter Height
   ↓
🧮 Calculate BMI
   ↓
📊 Determine BMI Category
   ↓
📋 Display Result
   ↓
🔁 Calculate Again or Exit
```

The program first takes the user's weight and height as input.

It then calculates BMI using the formula:

```text
BMI = Weight (kg) / Height² (m)
```

The calculated BMI is then compared against predefined ranges to determine the corresponding category.

---

## 📐 BMI Categories

The application uses the following BMI ranges:

| BMI Range   | Category    |
| ----------- | ----------- |
| Below 18.5  | Underweight |
| 18.5 - 24.9 | Normal      |
| 25 - 29.9   | Overweight  |
| 30 or above | Obese       |

> 📌 These categories are used as general BMI classifications in the application.

---

## 🛠️ Technologies Used

* 🐍 Python 3
* 🧮 Arithmetic Operations
* 🧠 Conditional Statements
* 🔄 `while` Loop
* 🧩 Functions
* 🛡️ Exception Handling
* ⌨️ User Input
* 🔢 Type Conversion

---

## 📚 Python Concepts Practiced

This project helped reinforce the following Python concepts:

* Variables and data types
* User input using `input()`
* Type conversion using `float()`
* Arithmetic operators
* Functions and parameters
* `return` statements
* `if`, `elif`, and `else`
* `while` loops
* `try-except`
* `ValueError`
* Boolean conditions
* Comparison operators
* `continue`
* `break`
* Formatted strings using f-strings
* Number formatting using `.2f`

---

## 🎯 Example

```text
========== BMI CALCULATOR ==========

Enter your weight in kg: 65
Enter your height in meters: 1.70

Your BMI is: 22.49
Category: Normal

Do you want to calculate again? (y/n): n

Thank you for using the BMI Calculator!
```

> 📊 The BMI result is displayed up to two decimal places for better readability.

---

## ⚠️ Input Validation

The program handles several invalid situations, including:

* ❌ Non-numeric weight input
* ❌ Non-numeric height input
* ❌ Zero weight or height
* ❌ Negative weight or height

For example:

```text
Enter your weight in kg: abc

Invalid input. Please enter numeric values.
```

The program uses `try-except` to prevent unexpected termination when the user enters invalid numeric data.

It also checks that weight and height are greater than zero before performing the calculation.

---

## 🔄 Multiple BMI Calculations

Users can perform multiple BMI calculations without restarting the program.

After displaying the result, the application asks:

```text
Do you want to calculate again? (y/n):
```

Choosing `y` starts another calculation, while any other response exits the application.

---

## 🧩 Project Structure

```text
Python-Task2-BMICalculator/
│
├── bmi.py
├── README.md
├── bmi_demo.mp4
│
└── screenshots/
    ├── bmi_calculator_start.png
    ├── bmi_result.png
    └── invalid_input.png
```

📸 The `screenshots/` folder contains screenshots showing the application's functionality and output.

🎥 `bmi_demo.mp4` contains the recorded demonstration of the application running end-to-end.

---

## ▶️ How to Run

### 1️⃣ Open the project

Open the project folder in **Visual Studio Code** or another Python-compatible IDE.

### 2️⃣ Open the terminal

Navigate to the project directory.

### 3️⃣ Run the program

```bash
python bmi.py
```

### 4️⃣ Enter your details

Enter your weight in kilograms and height in meters when prompted.

The program will calculate and display your BMI and corresponding category.

---

## 🎓 Internship Task

**Track:** Python Programming
**Task:** Task 2 - BMI Calculator
**Internship:** Oasis Infobyte Python Programming Virtual Internship

---

## 👨‍💻 Author

**Binayak Mukherjee**

---

## 🚀 Project Highlights

This project demonstrates practical use of Python for building a small interactive command-line application with:

⚖️ BMI Calculation
🧮 Mathematical Operations
🧠 Conditional Logic
🧩 Functions
🔄 Iteration
🛡️ Input Validation
⚠️ Exception Handling
📊 Result Classification

---
