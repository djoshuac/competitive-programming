import math
from collections import namedtuple

Student = namedtuple('Student', ['p', 'a', 'b', 'd'])

def decide_on_remains(a_left, zero_left, b_left, spp):
    a_happ_GIV_a = sum(s.a * s.p for s in a_left)
    zero_happ_GIV_x = sum(s.a * s.p for s in zero_left)
    b_happ_GIV_b = sum(s.b * s.p for s in b_left)

    a_need = sum(s.p for s in a_left)
    zero_need = sum(s.p for s in zero_left)
    b_need = sum(s.p for s in b_left)

    if (a_need + zero_need + b_need > spp):
        return a_happ_GIV_a + zero_happ_GIV_x + b_happ_GIV_b
    else:
        a_happ_GIV_b = sum(s.b * s.p for s in a_left)
        b_happ_GIV_a = sum(s.a * s.p for s in b_left)
        return max(a_happ_GIV_a + zero_happ_GIV_x + b_happ_GIV_a, a_happ_GIV_b + zero_happ_GIV_x + b_happ_GIV_b)

def one_side(slices_per_pizza, students, get_value):
    total_happ = 0
    happ = 0
    slices = slices_per_pizza
    index = 0
    leftover = None
    for i, s in enumerate(students):
        h = get_value(s)
        p = s.p
        happ += p * h
        slices -= p

        if slices <= 0:
            total_happ += happ + slices * h
            happ = -slices * h
            slices = slices_per_pizza + slices
            index = i
            leftover = slices_per_pizza - slices

    if leftover is None:
        remain = students
    elif slices == slices_per_pizza:
        remain = []
    else:
        remain = students[index:]
        s = remain[0]
        remain[0] = Student(leftover, s.a, s.b, s.d)

    return total_happ, remain

def max_happiness(slices_per_pizza, students):
    a_students = [s for s in students if s.d > 0]
    a_students.sort(key=lambda s: -s.d)

    zero_left = [s for s in students if s.d == 0]

    b_students = [s for s in students if s.d < 0]
    b_students.sort(key=lambda s: s.d)

    a_happ, a_left = one_side(slices_per_pizza, a_students, lambda s: s.a)
    b_happ, b_left = one_side(slices_per_pizza, b_students, lambda s: s.b)

    total_happ = a_happ + b_happ + decide_on_remains(a_left, zero_left, b_left, slices_per_pizza)
    return total_happ

if __name__ == "__main__":
    s, slices = map(int, input().split())
    students = []
    for _ in range(s):
        p, a, b = map(int, input().split())
        students.append(Student(p, a, b, a - b))
    print(max_happiness(slices, students))
