import re
diction = {}
try:
    f = open('input.txt', 'r')
    s = f.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
lines = s.split('\n')
for line in lines:
    line = re.sub(r'[^a-zA-Z0-9:,]', '', line)
    name = line.split(':')[0]
    subjects = line.split(':')[1]
    subject_list = subjects.split(',')
    diction.update({name: subject_list})
res = {}
for name, subjects in diction.items():
    for subject in subjects:
        if subject not in res:
            res[subject] = []
        res[subject].append(name)
requested_name = input("Enter the name of the discipline you are interested in")
print(res[requested_name])




