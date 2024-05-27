student_list2 = ['andrew', 'chris', 'harshirt', 'lary', 'shubam']

def rondomFunction(students):
    first = student[0] #0(1)
    total = 0 #0(1)
    new_list = [] #0(1)
    
for student in students: # type: ignore
    total += 1 # type: ignore #0(n)
    new_list.append(student) # type: ignore #0(n)
    
print(new_list) # type: ignore #0(1)
return total  # type: ignore

print(rondomFunction(students)) #0(6 + 2n) => 0(n)