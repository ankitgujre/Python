# sum of list

a = [10,20,30]
# print(sum(a))
total = sum(a)
print(total)

# using for loop

total = 0

for i in a:
    total += i
    
print(total)

# using while loop

# find max and min value

a = [4, 7, 1, 9]
print(max(a))
print(min(a))

# using for loop

max_val = a[0]
min_val = a[0]

for i in a:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
        
print(max_val, min_val)