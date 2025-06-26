def get_top_student(subject:str,dataset:dict):
    max_mark = 0
    m_name = None

    for name,mark in dataset.items():
        if mark > max_mark:
            max_mark = mark
            m_name = name

    return max_mark,m_name        




lines = None

with open('info.txt') as file:
    lines = file.readlines()

if not lines:
    print("Something went wrong, file is empty")
    exit()

marks_lines = lines[1:]

subject_marks = {}

for line in marks_lines:
    entries = line.split(',')

    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

print(subject_marks)

for subject,dataset in subject_marks.items():
    marks,name = get_top_student(subject,dataset)
    msg =f"{subject} max mark is {marks} and got by {name}."
    print(msg)