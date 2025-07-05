import tkinter as tk
from tkinter import ttk

# List of questions
questions = [
    "Do you have a fever?",
    "Do you have a cough?",
    "Are you sneezing?",
    "Do you have body pain?"
]
answers = []
current_question = [0]

# Diagnosis logic
def get_diagnosis():
    fever, cough, sneezing, pain = answers
    if fever and cough and pain:
        return "🦠 You might have the **Flu**."
    elif sneezing and not fever:
        return "🌿 You might have an **Allergy**."
    elif cough and not fever:
        return "🤧 You might have a **Common Cold**."
    else:
        return "❓ Unable to determine. Please consult a doctor."

# Update question with fade-in effect
def fade_in(text, i=0):
    if i == 0:
        question_label.config(text="")
    if i < len(text):
        question_label.config(text=question_label.cget("text") + text[i])
        root.after(30, lambda: fade_in(text, i + 1))

def show_question():
    if current_question[0] < len(questions):
        fade_in(questions[current_question[0]])
    else:
        result = get_diagnosis()
        question_label.config(text=result, fg="#FFFFFF", bg="#4B4453")
        yes_button.pack_forget()
        no_button.pack_forget()

def answer(val):
    answers.append(val)
    current_question[0] += 1
    show_question()

# GUI setup
root = tk.Tk()
root.title("Smart Medical Expert System")
root.geometry("500x300")
root.configure(bg="#282c34")

title_label = tk.Label(root, text="💡 Expert Diagnosis System", font=("Helvetica", 18, "bold"),
                       fg="#00ffd5", bg="#282c34")
title_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#ffffff",
                          bg="#282c34", wraplength=450, justify="center")
question_label.pack(pady=30)

# Styled buttons
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 12),
                padding=10)
style.map("TButton",
          foreground=[('active', '#282c34')],
          background=[('active', '#00ffd5')])

yes_button = ttk.Button(root, text="✅ Yes", style="TButton", command=lambda: answer(True))
no_button = ttk.Button(root, text="❌ No", style="TButton", command=lambda: answer(False))

yes_button.pack(pady=10)
no_button.pack(pady=5)

show_question()
root.mainloop()
