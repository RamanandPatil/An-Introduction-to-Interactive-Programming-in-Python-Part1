# http://www.codeskulptor.org/#user43_8ACAzH220v_0.py

# Testing template for name_to_number()

###################################################
# Copy and paste your definition of name_to_number() here
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return ("Please provide a valid name from: " + 
                "rock, Spock, paper, lizard and scissors")
    
###################################################
# Test calls to name_to_number()
print name_to_number("rock")
print name_to_number("Spock")
print name_to_number("paper")
print name_to_number("lizard")
print name_to_number("scissors")
print name_to_number("Scissors")



###################################################
# Output to the console should have the form:
# 0
# 1
# 2
# 3
# 4