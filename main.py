# Enter amount to be calculated
original_load = int(input("Please enter a value for original_load: "))
while original_load < 1 or original_load > 250000:
    original_load = int(input("Invalid input. Please enter a value for original_load between 1 and 250000: "))

# Enter amount to be disbursed to loader
loader_disbursement = int(original_load * 0.95) # 95% of original_load
loader_disbursement = int(loader_disbursement)  # Convert loader_disbursement to zero decimal places integer


# Enter transaction type
def determine_transaction_type():
    """
    Prompts the user to choose between a mobile to mobile transaction or a till transaction.
    
    Returns:
        str: The chosen transaction type ('m' for mobile to mobile transaction or 't' for a till transaction).
    """
    transaction_type = input("Please choose between 'm' for mobile to mobile transaction or 't' for a till transaction: ")
    
    # Validate the user input
    while transaction_type not in ['m', 't']:
        transaction_type = input("Invalid input. Please choose between 'm' for money transaction or 't' for transfer transaction: " "\n\n")
    
    return transaction_type

# Calculate transaction charge
transaction_type = determine_transaction_type()

if transaction_type == 't':
    transaction_charge = 0
elif transaction_type == 'm':
    # Calculate transaction charge
    if 1 <= loader_disbursement <= 100:
        transaction_charge = 0
    elif 101 <= loader_disbursement <= 500:
        transaction_charge = 7
    elif 501 <= loader_disbursement <= 1000:
        transaction_charge = 13
    elif 1001 <= loader_disbursement <= 1500:
        transaction_charge = 23
    elif 1501 <= loader_disbursement <= 2500:
        transaction_charge = 33
    elif 2501 <= loader_disbursement <= 3500:
        transaction_charge = 53
    elif 3501 <= loader_disbursement <= 5000:
        transaction_charge = 57
    elif 5001 <= loader_disbursement <= 7500:
        transaction_charge = 78
    elif 7501 <= loader_disbursement <= 10000:
        transaction_charge = 90
    elif 10001 <= loader_disbursement <= 15000:
        transaction_charge = 100
    elif 15001 <= loader_disbursement <= 20000:
        transaction_charge = 105
    elif 20001 <= loader_disbursement <= 250000:
        transaction_charge = 108
    else:
        transaction_charge = 0  # Default charge if original_load is outside the specified ranges
else:
    transaction_charge = print("Enter valid transaction type to generate transaction charge.")  # Default charge if transaction_type is neither 'm' nor 't'

#Display amount to be disbursed to loader
print("Amount to Loader is KES", loader_disbursement, "at a transaction charge of KES", transaction_charge,"." "\n")


# Calculate amount to be disbursed to money bags
money_bag_disbursement = int(original_load) - int(loader_disbursement) - int(transaction_charge)
#Display amount to be disbursed to money bags
print("KES", money_bag_disbursement, "will be disbursed to the money bags.\n")

#Declare equal amount to be disbursed to money bag 1 and money bag 2
money_bag_1 = int(0.5 * money_bag_disbursement) # 50% of money_bag_disbursement
money_bag_2 = int(0.5 * money_bag_disbursement) # 50% of money_bag_disbursement

def money_bag_1_disbursement(): 
    if 1 <= money_bag_1 <= 100:
        money_bag_1_transaction_charge = 0
    elif 101 <= money_bag_1 <= 500:
        money_bag_1_transaction_charge = 7
    elif 501 <= money_bag_1 <= 1000:
        money_bag_1_transaction_charge = 13
    elif 1001 <= money_bag_1 <= 1500:
        money_bag_1_transaction_charge = 23
    elif 1501 <= money_bag_1 <= 2500:
        money_bag_1_transaction_charge = 33
    elif 2501 <= money_bag_1 <= 3500:
        money_bag_1_transaction_charge = 53
    elif 3501 <= money_bag_1 <= 5000:
        money_bag_1_transaction_charge = 57
    elif 5001 <= money_bag_1 <= 7500:
        money_bag_1_transaction_charge = 78
    elif 7501 <= money_bag_1 <= 10000:
        money_bag_1_transaction_charge = 90
    elif 10001 <= money_bag_1 <= 15000:
        money_bag_1_transaction_charge = 100
    elif 15001 <= money_bag_1 <= 20000:
        money_bag_1_transaction_charge = 105
    elif 20001 <= money_bag_1 <= 250000:
        money_bag_1_transaction_charge = 108
    else:
        money_bag_1_transaction_charge = 0  # Default charge if original_load is outside the specified ranges
    return money_bag_1_transaction_charge

money_bag_1_transaction_charge = money_bag_1_disbursement()


# Calculate money bag 1 disbursement
money_bag_1_disbursement = money_bag_1 - money_bag_1_transaction_charge
#Convert to zero decimal places
money_bag_1_disbursement = format(money_bag_1_disbursement, '.0f')

#Final amount to be disbursed to money bag 1
print("Money Bag 1 will receive KES", money_bag_1_disbursement, "with a transaction charge of KES", money_bag_1_transaction_charge,"." "\n")

# Final amount to be disbursed to money bag 2
print("Money Bag 2 will receive KES", money_bag_2, "at no extra charge." "\n")
    



 







