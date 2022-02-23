# Ryan Lugo: RJL 1/13/22

# Creating a last initials table
last_initials = ["B.", "D.", "H.", "E.", "G.", "G.", "H.", "R.", "M.", "L.", "I.", "I.", "N.", "N.", "O.", "P.", "P.", "X.", "T.", "S.", "S.", "P."]

# Creating a table for rows and names attached
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin" "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]


def add_initial(table,initials):

    # Counter being used for each of the tables
    counter = 0
    # The inside counter being used for each name
    ini_counter = 0

    # If the inputted value is a list then
    if type(table) == list:
        # While the counter for each big list is less than the length of the whole thing do
        while counter < len(rows):
            # Each big table inside
            for i,v in enumerate(table[counter]):
                # Each specific row
                rows[counter][i] = v + " " + initials[ini_counter]
                # When adding the one it finds the value in the table
                ini_counter += 1
                # Adding the + 1 to the total big counter after the for loop is done
            counter += 1
        # Repeats until the conditions are met
        

    else:
        # Print out that the inputted value is not a list
        print(table,"is not a list.")
    return

add_initial(rows,last_initials)

# Print out the modififed table/list
print(rows)