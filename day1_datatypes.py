import copy

library = {
    "title": "Python Adventures",
    "authors": ["Alice", "Bob"]
}

# Shallow copy
shallow_library = copy.copy(library)

# Deep copy
deep_library = copy.deepcopy(library)

# Modify the nested list through the shallow copy
shallow_library["authors"].append("Charlie")

print("Original:", library)
print("Shallow Copy:", shallow_library)
print("Deep Copy:", deep_library)


# School program

# Tuple
exams = ("midterm", "final", "quiz")

# Set
students = {"Likitha", "Rahul", "Ananya"}

# Nested Dictionary
scores = {
    "Likitha": {"midterm": 85, "final": 100, "quiz": 90},
    "Rahul": {"midterm": 78, "final": 88, "quiz": 82},
    "Ananya": {"midterm": 92, "final": 95, "quiz": 89}
}

print("Likitha's midterm score:", scores["Likitha"]["midterm"])
print("All students:", list(scores.keys()))
print("Exam types:", exams)
