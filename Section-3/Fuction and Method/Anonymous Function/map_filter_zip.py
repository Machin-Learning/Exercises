from functools import reduce

# filter(function, iterable)
marks = [76,84,56,12,40,80,95]

def marks_check(li):
    if li > 50:
        return True
    else:
        return False

# ls_checked = list(filter(marks_check, marks))
ls_checked = list(filter(lambda li:li > 50, marks))
print(ls_checked)

# map(func, iter1)

score_list = [430,312,214,403,336,469]

def score_marks(li):
    ans = (li*100)/500
    return ans

# marks_list =list(map(score_marks, score_list))
marks_list = list(map(lambda li:(li*100/500), score_list))

print(marks_list)

# zip(iter1)
stu_name = ["muzmmil","mudassir","khalid","zeeshan","amar"]
mark_ls = [74,98,45,65,78]

zipped_ls = zip(stu_name,mark_ls)

zipped_ls = list(zipped_ls)

student_name,student_marks = zip(*zipped_ls)
print(list(student_name))
print(list(student_marks))

#Even or Odd

lst = [10,2,33,45,89,2]

even = list(filter(lambda c:c%2==0, lst))

print(even)

odd = list(filter(lambda c:c%2!=0, lst))
print(odd)


#Double using map

ls = [2,3,4,5,6,7,8]

double_ls = list(map(lambda x:x*2, ls))
print(double_ls)

#reduce 

lsr = [5,10,15,20]

result = reduce(lambda x,y:x+y, lsr)
print(result)
