print("Welcome to the tip calculator!!!")
bill_amount = float(input("How much was the bill? "))
tip =  int(input("How much would you like to tip on this bill? 10, 12, 15, 20, or 25 percent? "))
number_of_people = int(input("How many people would you like to split the bill with? "))

bill_with_tip = tip / 100 * bill_amount + bill_amount
split_bill_amount = bill_with_tip / number_of_people
final_bill_with_tip = round(bill_with_tip)
final_per_person = round(split_bill_amount, 2)

print(f"The bill with tip added is going to be ${final_bill_with_tip}")
print(f"After tip each person will pay ${final_per_person}")