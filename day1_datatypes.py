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