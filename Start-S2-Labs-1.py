# Ryan Lugo: RJL 1/13/22

def count_e(string):

    # Setting a blank number for counting
    number_of_e = 0

    # If the value passed is a string then
    if type(string) == str:
        # For each item in the string
        for i,v in enumerate(string):
            # If the letter in the string matches e then
            if str.lower(v) == "e":
                # Add a + 1 to the "e" counter
                number_of_e += 1
    else:
        # Not a string statement
        print("This is not a string.")
    # Will return the amount of e's in the string
    return number_of_e

print(count_e("everyone"))