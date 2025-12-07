❓ Quiz Game — Python
📌 Overview

This project is a simple multiple-choice Quiz Game built in Python. The game displays questions one by one, takes user input, checks answers, and keeps track of the final score. It uses Object-Oriented Programming (OOP) for cleaner structure and separation of logic.

🎮 Gameplay

Program presents a question and 4 options

User selects an answer

Game checks correctness instantly

Final score is displayed at the end

🧩 Features

✔️ Pre-loaded set of quiz questions
✔️ Score tracking
✔️ User input validation
✔️ Looping through questions until quiz ends
✔️ Modular code structure with classes

🏗️ Technologies Used

Python

OOP (Object-Oriented Programming)

(Optional) External JSON/CSV file for questions

📂 Project Structure
📁 quiz-game
│
├── main.py          # Game engine & quiz loop
├── question_model.py # Question class
├── data.py          # Question data (list or JSON)
└── quiz_brain.py    # Quiz logic (checking answers & score)

🚀 How to Run

Install Python (if not installed)

Open terminal in project directory

Run:

python main.py

🔑 Key Concepts Learned

Creating and using classes and objects

Handling user input and validation

Managing loops and conditionals

Storing data in lists, dictionaries, or JSON

Designing clean, structured Python programs

🧠 Example Question Format
{
  "question": "What is the capital of France?",
  "options": ["Berlin", "Madrid", "Paris", "Rome"],
  "answer": "Paris"
}

🌟 Future Enhancements

🧾 Load questions from an API

🕹 GUI version using Tkinter

🏆 Save high scores

📊 Randomize question order

⏲ Add a timer for each question
