def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill 
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
"""
En  maate aa kommentere
"""
#En annen maate aa kommentere

meal_cost = int(raw_input("How much did the meal cost? \n"))
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
"""print meal_cost
print tax(meal_cost)
print tip(meal_with_tax)"""

