#tkinter for GUI
import tkinter as tk

# Function to calculate the final grade
def calculate_grade():
    try:
        course = course_name_entry.get()
        if not course.strip(): #if user does not enter any course name
            result_label.config(text="Please enter the course name.")
            return

        total_weight = sum([float(weight_entry.get()) for weight_entry in weight_entries])
        if total_weight != 100: # to make sure that total weight is exactly 100
            result_label.config(text="Total weight must equal 100%.")
            return

        total_grade = 0
        for i in range(len(category_entries)):
            score = float(score_entries[i].get())
            weight = float(weight_entries[i].get()) / 100
            total_grade += score * weight

        # Determine letter grade and assign with color based on type of grade
        if total_grade >= 90:
            letter_grade = "A"
            color = "green"
        elif total_grade >= 80:
            letter_grade = "B"
            color = "lightgreen"
        elif total_grade >= 70:
            letter_grade = "C"
            color = "lightyellow"
        elif total_grade >= 60:
            letter_grade = "D"
            color = "lightcoral"
        else:
            letter_grade = "F"
            color = "red"

        # Display the result
        result_label.config(
            text=f"Your grade in {course} is {total_grade:.2f} ({letter_grade})",
            bg=color
        )
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Function that lets the user add a grade category such as assignments, quizzes, labs, exams, etc.
def add_category():
    row = len(category_entries) + 2

    tk.Label(root, text=f"Category {row - 1}:").grid(row=row, column=0, padx=5, pady=5)
    category_entry = tk.Entry(root, width=15)
    category_entry.grid(row=row, column=1, padx=5, pady=5)
    category_entries.append(category_entry)

    # Total Score
    score_entry = tk.Entry(root, width=10)
    score_entry.grid(row=row, column=2, padx=5, pady=5)
    score_entries.append(score_entry)

    # Weight
    weight_entry = tk.Entry(root, width=10)
    weight_entry.grid(row=row, column=3, padx=5, pady=5)
    weight_entries.append(weight_entry)

# To initialize the GUI application
root = tk.Tk()
root.title("Grade Calculator")

# To get the Course Name
tk.Label(root, text="Course Name:").grid(row=0, column=0, padx=5, pady=5)
course_name_entry = tk.Entry(root, width=30)
course_name_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

# Column Headers
tk.Label(root, text="Category").grid(row=1, column=1, padx=5, pady=5)
tk.Label(root, text="Total Score (out of 100)").grid(row=1, column=2, padx=5, pady=5)
tk.Label(root, text="Weight (%)").grid(row=1, column=3, padx=5, pady=5)

# Lists to store entries
category_entries = []
score_entries = []
weight_entries = []

# To add the first category
add_category()

# Buttons
tk.Button(root, text="Add Category", command=add_category).grid(row=100, column=0, padx=5, pady=20)
tk.Button(root, text="Calculate Grade", command=calculate_grade).grid(row=100, column=1, columnspan=3, padx=5, pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="white", width=40, height=3)
result_label.grid(row=101, column=0, columnspan=4, pady=10)

root.mainloop()
