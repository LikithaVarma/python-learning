

with open("students.txt", "w") as f:
    f.write("likitha\n")
    f.write("rahul\n")
    f.write("ananya\n")
    
    
with open("students.txt", "r") as f:
    lines = f.readlines()
    clean = [line.strip() for line in lines]
    print(clean)
    
try:   
    with open("missing.txt", "r") as f:
            contents = f.read()
            print(contents)
except FileNotFoundError:
            print("File not found.")
            

try:   
    with open("students.txt", "a") as f:
            f.write("priya\n")
except FileNotFoundError:
            print("File not found.")
            

def save_results(filename,results):
    try:
        with open(filename, "w") as f:
            for result in results:
                f.write(result + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        

save_results("results.txt", ["Accuracy: 92%", "Precision: 88%", "Recall: 91%"])


with open("results.txt", "r") as f:
    print(f.read())