import random, sys, csv

file_name = "Learning Progress Tracker(Programs).csv"
program_count = 974

random.seed(0)
programs = list(range(program_count))
random.shuffle(programs)

n = int(sys.argv[1]) - 1

if n < 0:
    exit(1)

elif n >= len(programs):
    print("EOF")
    exit(0)

random_index = programs[n] + 1
python_file_name = f"{random_index}.py"
comments = []

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    
    for i in range(random_index + 1):
        comments = next(reader)

try:
    with open(python_file_name, "x") as file:
        for line in comments:
            file.write(f"# {line}\n")
    
    print(f"Created: {python_file_name}")

except FileExistsError:
    print(f"Exists: {python_file_name}")