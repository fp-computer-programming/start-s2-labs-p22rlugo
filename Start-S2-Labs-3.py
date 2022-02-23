# Ryan Lugo: RJL 1/14/22

def comes_after(st, l): 
    # Empty str
    res=''
    # For each letter in it - 1 to find the next letter
    for i in range(len(st)-1):
        # If the val is == to the inputted value
        if st[i].lower()==l.lower():
            # If it's a alpha then
            if st[i+1].isalpha():
                # Add it
                res+=st[i+1]
    return res