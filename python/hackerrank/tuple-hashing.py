n = int(input())
input_vals = input().split()
tuples = map(int,input_vals)
t =tuple(tuples)
print(hash(t))