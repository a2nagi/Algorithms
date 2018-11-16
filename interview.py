student_course_pairs -> N
students -> M


student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"]
]

student_course_pairs_1 = [
    ["58", "Software Design"],
    ["94", "Economics"]
]

student_course_pairs_2 = [
    ["58", "Software Design"],
    ["94", "Economics"],
    ["99", "Physics"]   
]



def intersection(a, b):
    elements = {}
    for i in a:
        if i in elements:
            continue
        else:
            elements[i] = 1
     
    intersection = []
    for j in b:
        if j in elements:
            intersection.append(j)
    return intersection


def find_pairs(student_course_pairs):
    student_courses = {}
    for i in student_course_pairs:
        cur_course = i
        if cur_course[0] in student_courses:
            student_courses[cur_course[0]].append(cur_course[1])
        else:
            student_courses[cur_course[0]] = [cur_course[1]]
        
    # student -> course dict built
    
    key_array = []
    for key in student_courses:
        key_array.append(key)
    
    
    output_dict = {}
    for i in range (len(key_array)):
        cur_lst = student_courses[key_array[i]]
        for j in range(i+1,len(key_array)):       
           next_lst = student_courses[key_array[j]]
           intersection_lst = intersection(cur_lst, next_lst)
           build_key = key_array[i] + "," + key_array[j]
           output_dict[build_key] = intersection_lst
    
    return output_dict
                       
                    
find_pairs(student_course_pairs)      

# You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student has completed 50% of their academic program.

# Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

# Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their sequence of courses. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

# In this case, the order of the courses in the program is:
#     Software Design
#     Computer Networks
#     Computer Architecture
#     Data Structures
#     Algorithms
#     Foundations of Computer Science
#     Operating Systems

# Sample output 1:
#     "Data Structures"


prereqs_courses1 = [
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Operating Systems"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]

        
    

def prereqs(prereqs_courses):
    dict_courses = {}

    for i in prereqs_courses:
        cur_lst = i
        dict_courses[cur_lst[0]] = cur_lst[1]
    
    # built dict
    count = 0
    for i in dict_courses:
        count += 1
        
    prereq_dict ={}
    for key in dict_courses:
        anti_req = dict_courses[key]
        build_lst = []
        while(anti_req in dict_courses):
            build_lst.append(anti_req)
        prereq_dict[key] = build_lst
    
    for key in prereq_dict:
        curlength = len(prereq_dict[key])
        if curlength % 2 == 1
    
