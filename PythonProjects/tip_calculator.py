# tip calculator with 3 options

payment_total_with_dollarsign = input("How much need to pay to restaurant?\n")
payment_total_int = float(payment_total_with_dollarsign.replace("$",""))

tip_option1 = payment_total_int * 0.1
tip_option2 = payment_total_int * 0.15
tip_option3 = payment_total_int * 0.2

print("Select the most suitable tip option for you. Type 1 for Tip 1, Type 2 for Tip 2 and Type 3 for Tip 3.")


tip_choice = int(input(f"First tip option: ${tip_option1:0.2f}\nSecond tip option: ${tip_option2:0.2f}\nThird tip option: ${tip_option3:0.2f}.\n"))
print(f"You have selected to pay Tip {tip_choice}.")