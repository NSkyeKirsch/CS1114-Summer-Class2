show = "Breaking Bad"

print(len(show))

var = show[3:8]  # string slicing
print("show[3:8] ==", var)

new_var = show[3:]
print("show[3:] ==", new_var)
print("show[:5] ==", show[:5])
print("show[2:10:3] ==", show[2:10:3])
print("show[::3] ==", show[::3])

print()

print("show[-1:-7] ==", show[-1:-7], "         <-- Nothing!!!")
print("show[-1:-7:-1] ==", show[-1:-7:-1])
print("show[::-1] ==", show[::-1])

# id of a variable / object
print(id(show))  # <--- prints where in the memory it is

new_show = show

print(id(show), id(new_show))

print()

for some_letter in show:
    print(some_letter, end="...")
print()

for index in range(0, len(show)):  # using indexing, you can print same thing
    print(show[index], end="...")
print()

