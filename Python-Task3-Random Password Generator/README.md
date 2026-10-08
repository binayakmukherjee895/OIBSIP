# 🔐 Random Password Generator

A simple and interactive **Python-based Random Password Generator** that creates secure and randomized passwords based on the user's selected character types.

The application allows users to choose the password length and decide whether to include **uppercase letters, lowercase letters, numbers, and special characters**.

---

## 📌 Project Overview

This project was developed as part of the **Python Programming Virtual Internship at Oasis Infobyte**.

The application generates random passwords according to the user's requirements while ensuring that at least **two different character types** are selected.

It also includes input validation, exception handling, and an option to generate multiple passwords without restarting the program.

---

## ✨ Features

* 🔢 Choose the desired password length
* 🔠 Include uppercase letters (`A-Z`)
* 🔡 Include lowercase letters (`a-z`)
* 🔢 Include numbers (`0-9`)
* 🔣 Include special characters
* 🛡️ Requires at least two character types
* 🎲 Generates randomized passwords
* 🔀 Randomly shuffles generated characters
* ⚠️ Handles invalid input using exception handling
* 🔁 Allows users to generate multiple passwords
* ✅ Minimum password length validation

---

## 🧠 How It Works

The password generation process follows a simple flow:

```text
👤 User
   ↓
📏 Enter Password Length
   ↓
🔠 Select Character Types
   ↓
🧩 Build Character Pool
   ↓
🎲 Select Random Characters
   ↓
🔀 Shuffle Password
   ↓
🔐 Generated Password
```

The program first creates a character pool based on the user's selections. It then randomly selects characters from that pool until the required password length is reached.

The selected character types are also guaranteed to be represented in the generated password.

---

## 🛠️ Technologies Used

* 🐍 Python 3
* 🎲 `random` module
* 🔤 `string` module
* 🧩 Python Lists
* 🔄 Loops
* 🧠 Conditional Statements
* 🛡️ Exception Handling

---

## 📚 Python Concepts Practiced

This project helped reinforce the following Python concepts:

* Variables and data types
* User input using `input()`
* Type conversion using `int()`
* Boolean values (`True` / `False`)
* String methods such as `.lower()`
* String concatenation
* Lists and `.append()`
* Functions and parameters
* `if` statements
* `while` loops
* `continue` and `break`
* `try-except`
* `random.choice()`
* `random.shuffle()`
* `string.ascii_uppercase`
* `string.ascii_lowercase`
* `string.digits`
* `string.punctuation`
* `join()` for converting a list into a string

---

## 🎯 Example


========== RANDOM PASSWORD GENERATOR ==========

Enter password length (minimum 8): 12

Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
m7@Qx2#Lp9!A

Generate another password? (y/n): n

Thank you for using the Password Generator!
```

> 🔒 The generated password will be different each time because the characters are selected randomly.

---

## ⚠️ Input Validation

The program handles several invalid situations, including:

* ❌ Password length below 8
* ❌ Non-numeric password length
* ❌ Selecting fewer than two character types
* ❌ Invalid input during the program flow

Instead of terminating unexpectedly, the application displays a clear message and allows the user to try again.

---

## 🔄 Multiple Password Generation

Users can generate multiple passwords within the same program session.

After generating a password, the application asks:

```text
Generate another password? (y/n):
```

Choosing `y` starts the process again, while any other response exits the application.

---

## 📂 Project Structure


Python-Task3-RandomPasswordGenerator/
│
├── randompwdgen.py
├── README.md
├── random_pwd_gen_demo.mp4
│
└── screenshots/
    ├── password_generator_start.png
    ├── generated_password.png
    └── invalid_input.png


📸 The `screenshots/` folder contains screenshots showing the application's functionality and output.

🎥 `random_pwd_gen_demo.mp4` contains the recorded demonstration of the application running end-to-end.

---

## ▶️ How to Run

### 1️⃣ Open the project

Open the project folder in **Visual Studio Code** or another Python-compatible IDE.

### 2️⃣ Open the terminal

Navigate to the project directory.

### 3️⃣ Run the program

```bash
python randompwdgen.py
```

### 4️⃣ Follow the prompts

Enter the desired password length and select the character types you want to include.

---

## 🎓 Internship Task

**Track:** Python Programming
**Task:** Task 3 - Random Password Generator
**Internship:** Oasis Infobyte Python Programming Virtual Internship

---

## 👨‍💻 Author

**Binayak Mukherjee**

---

## 🚀 Project Highlights

This project demonstrates practical use of Python for building a small interactive command-line application with:

🎲 Randomization
🧠 Conditional logic
🧩 Functions
🔄 Iteration
🛡️ Input validation
⚠️ Exception handling
🔐 Password generation logic

---
