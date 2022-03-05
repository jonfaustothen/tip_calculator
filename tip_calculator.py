# Creating function that prints "thinking computer" display on terminal to separate user experience
def computing():
    return("\n........//( o )//........//( o )//........\n.................//>>//...................\n.............vvvvvvvvvvvvvvv..............\n")

# Creating while loop to allow user to re-enter script at the end
while True:
# Introduce program to user:
    print("\nHello! And welcome to The Tip Calculator! \n\nThis program will help you determine how much you should tip for your meal.\n")

# Let's ask the user for the cost of the meal
    def cost_of_meal():
        while True:
            cost_of_meal_entry = (input("How much was the cost of your meal? \n$"))
            try:
                float(cost_of_meal_entry)
                if float(float(cost_of_meal_entry)) > 0:
                    return (float(cost_of_meal_entry))
            except ValueError: # This try/except allows user to try again if they do not enter an integer/float, or quit.
                retry = input("\nThis is not a valid numerical amount. Please try again or Type 'q' to quit.\n")
                if retry == 'q':
                    print("Good Bye!")
                    quit()
             
    cost = float(cost_of_meal()) #cost is variable for return of function cost_of_meal
    print(f"\nThanks! Let's first figure out how much tax is due for ${cost}.")

# A "thinking computer" allows user to "see" program is calculating
    print(computing())

# Defining variables for taxes, rounded to two decimal places
    tax = float(format((cost * 0.1), ".2f"))
    cost_of_meal_w_tax = format((cost * 1.1), ".2f")

# Using format function to format returns with two decimal places
    print(f"It looks like you're dining in an expensive city.  Your tax rate is 10% there, and so your tax for this meal is ${tax}, which brings your total before tip to ${cost_of_meal_w_tax}. Now let's figure out how much to tip. (This calculator will determine your tip on the cost of the meal, before taxes).\n")#Using 10% as tax rate for simplicity

# Asking user for number of people at dinner
    num_people = int(input("How many people shared this meal with you? (If you ate by yourself, enter '1').\n"))

# Creating function for Sample Tip Rates
    def sample_tip_rate (i):
        rate = float(i) / 100
        sample_tip = float(format(((cost / num_people) * rate), ".2f"))
        print(f"At {i}%, the tip would be: ${sample_tip}.")

# Printing sample tip calculations based on common percentages given
    print("\nBelow is how much each person should contribute towards the tip based on the cost of the food for various rates:\n")
    sample_tip_rate(15)
    sample_tip_rate(20)
    sample_tip_rate(25)

# Creating function with multiple variables to calculate tip to be contributed by each person
    def cost_per_person(num_people):
        user_tip_percentage = float(input("\nWhat _____% would you like to tip?\n"))
        user_tip_rate = user_tip_percentage / 100
        total_tip = float(format((cost * user_tip_rate), ".2f"))
        user_tip_per_person = format(((cost / num_people) * user_tip_rate), ".2f")
        grand_total = float(format((cost + total_tip + tax), ".2f"))
        total_per_person = float(format((grand_total / num_people), ".2f"))
        print(computing())
        print(f"\nThe total tip will be {total_tip}, and each person will need to contibute ${user_tip_per_person} towards the tip.  Below is a breakdown of your total costs:\nCost of Meal      =    ${cost}\nTip               =    ${total_tip}\nTax               =    ${tax}\nTotal             =    ${grand_total}.\n\nThe share of the total price per person is: ${total_per_person}.")
    cost_per_person(num_people)

    if input('\nDo you want to enter another tip (y/n?\n') == 'n':
        print('\nGood Bye!')
        break