
thought = "Python is awesome"

big_thought = thought.upper()

print(big_thought)
print(thought)

# formatting!!!!!

date_str = "06/02/22"

print("The midterm will be on {}! thank you.".format(date_str))

print("The midterm will be on {:16s}! thank you.".format(date_str))

print("The midterm will be on {:<16s}! thank you.".format(date_str))
print("The midterm will be on {:>16s}! thank you.".format(date_str))
print("The midterm will be on {:^16s}! thank you.".format(date_str))

print()

print("{:<6.2f} is pi".format(3.1415927))  # < = left alignment,  6 = width,  .2 = 2 places of precision,  f = float

# a new way to do it that is better are f-strings!!!!
