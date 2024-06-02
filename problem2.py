A = 10
B = 20
data = "There are {} students in the class, with {} who play at least one sport."
print(str(A)+str(B)+data)
print(data.format(A,B))
print(data.format(B,A))