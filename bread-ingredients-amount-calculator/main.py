# Ingredients amount from the original recipe
ORIGINAL_FLOUR_AMOUNT = 250
ORIGINAL_SUGAR_AMOUNT = 30
ORIGINAL_YEAST_AMOUNT = 3
ORIGINAL_SALT_AMOUNT = 2
ORIGINAL_MILK_AMOUNT = 170
ORIGINAL_UNSALTED_BUTTER_AMOUNT = 20

# Baking ratios
SUGAR_RATIO = ORIGINAL_SUGAR_AMOUNT / ORIGINAL_FLOUR_AMOUNT
YEAST_RATIO = ORIGINAL_YEAST_AMOUNT / ORIGINAL_FLOUR_AMOUNT
SALT_RATIO = ORIGINAL_SALT_AMOUNT / ORIGINAL_FLOUR_AMOUNT
MILK_RATIO = ORIGINAL_MILK_AMOUNT / ORIGINAL_FLOUR_AMOUNT
UNSALTED_BUTTER_RATIO = ORIGINAL_UNSALTED_BUTTER_AMOUNT / ORIGINAL_FLOUR_AMOUNT

baking_ratios = (SUGAR_RATIO, YEAST_RATIO, SALT_RATIO, MILK_RATIO, UNSALTED_BUTTER_RATIO)


# Calculates amount
def amount_calculator(user_flour_amount):
    calculated_amount_list = [user_flour_amount]
    for ratio in baking_ratios:
       calculated_amount= flour_amount * ratio
       calculated_amount_list.append(calculated_amount)
    return calculated_amount_list



# Main program
flour_amount = int(input("Enter the amount of flour you wanna use:\n"))

new_amount_list = amount_calculator(flour_amount)

print(f"- Flour: {new_amount_list[0]}g \n- Sugar: {new_amount_list[1]}g \n- Yeast: {new_amount_list[2]}g \n- Salt: {new_amount_list[3]}g \n- Milk: {new_amount_list[4]}ml \n- Unsalted butter: {new_amount_list[5]}g \n\nHappy Baking :)")