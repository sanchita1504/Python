#Enter Name and percentage Marks in a Dictionary and Display Info.

student={}
name=input("Enter the student name: ")
marks=float(input("Enter percentage marks: "))

student["Name"]=name
student["Percentage"]=marks

print("\nStudent Information")
print(student)

#Find the no. of occurences of each letter in a string

s = input("Enter a string: ")

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)


# Find the no. of occurences of each vowel in a string

s = input("Enter a string: ")

vowels = "aeiou"
count = {}

for ch in s.lower():
    if ch in vowels:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

print(count)

#Accept Student names and matrks, store in a dictionary and display marks by student name

students = {}

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

search = input("Enter the student name to find marks: ")

if search in students:
    print(search, "scored", students[search], "marks")
else:
    print("Student not found")


#Print a tabular Comparison of python collections

print("-" * 100)
print(f"{'Feature':<25}{'List':<15}{'Tuple':<15}{'Set':<15}{'Dictionary':<20}")
print("-" * 100)

print(f"{'Syntax':<25}{'[]':<15}{'()':<15}{'{}':<15}{{key: value}}")
print(f"{'Ordered':<25}{'Yes':<15}{'Yes':<15}{'No':<15}{'Yes'}")
print(f"{'Mutable':<25}{'Yes':<15}{'No':<15}{'Yes':<15}{'Yes'}")
print(f"{'Allows Duplicates':<25}{'Yes':<15}{'Yes':<15}{'No':<15}{'Keys: No'}")
print(f"{'Indexing':<25}{'Yes':<15}{'Yes':<15}{'No':<15}{'By Key'}")
print(f"{'Key-Value Pair':<25}{'No':<15}{'No':<15}{'No':<15}{'Yes'}")
print(f"{'Example':<25}{'[1,2,3]':<15}{'(1,2,3)':<15}{'{1,2,3}':<15}{'{1:100}'}")

print("-" * 100)
