student_basic_info = [
    (1, "6662118001", " 张三 "),
    (2, "6662118002", " 李四 "),
    (3, "6662118051", " 王五 "),
    (4, "6662118052", " 赵六 ")
]
student_class_info = [
    ("6662118001", " 计算机 201 班 "),
    ("6662118002", " 计算机 202 班 "),
    ("6662118051", " 计算机 202 班 "),
    ("6662118052", " 计算机 203 班 ")
]
L = [student_basic_info[a]+(student_class_info [a][1],) for a in range(0,4)]
for info in L:
    print(info)