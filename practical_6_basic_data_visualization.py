import matplotlib.pyplot as plt

students = ["Asha", "Rahul", "Priya", "Amit", "Neha"]
marks = [85, 70, 90, 65, 80]

plt.figure(figsize=(8, 5))
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(students, marks, marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(students, marks)
plt.title("Student Marks - Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
