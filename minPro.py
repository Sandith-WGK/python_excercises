def get_top_student(subject:str,dataset:dict):
    max_mark = 0
    m_name = None

    for name,mark in dataset.items():
        if mark > max_mark:
            max_mark = mark
            m_name = name

    return max_mark,m_name        

def get_marks(record:tuple):
    return record[1]


lines = None

with open('info.txt') as file:
    lines = file.readlines()

if not lines:
    print("Something went wrong, file is empty")
    exit()

marks_lines = lines[1:]

subject_marks = {}
student_marks = {}

for line in marks_lines:
    entries = line.split(',')

    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    prev_marks = student_marks.get(name, 0)
    student_marks[name] = prev_marks + marks


    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

#print(student_marks)
messages = []
marks_list = [(name,marks)for name,marks in student_marks.items()]
marks_list.sort(key=get_marks,reverse=True)
top = marks_list[0]
msgs = f"Top student is {top[0]} with {top[1]} marks."
print(msgs)
messages.append(msgs)
#print(subject_marks)

for subject,dataset in subject_marks.items():
    marks,name = get_top_student(subject,dataset)
    msg =f"{subject} max mark is {marks} and got by {name}."
    print(msg)
    messages.append(msg)

with open('result.txt','w') as output_file:
    for msg in messages:
        output_file.write(msg)
        output_file.write('\n')

