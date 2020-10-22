import math


# -- These are just here to make an easy copypasta later in the code --
# principal = int(input("Please enter your loan principal:\n"))
# num_payments = int(input("Please enter the number of payments:\n"))
# payment_amount = int(input("Please enter your monthly payment amount:\n"))
# interest_rate = int(input("Please enter your interest rate:\n"))


def number_of_payments(payment, loan_principal, interest):
    interest = interest / 12 / 100
    ret_val = math.log((payment / (payment - interest * loan_principal)), 1 + interest)
    return math.ceil(ret_val)


# def monthly_payment(loan_principal, payments, interest):
#     interest = interest / 12 / 100
#     return (loan_principal * ((interest * ((1 + interest) ** payments))
#                                    / ((1 + interest) ** payments) - 1))


def monthly_payment(loan_principal, payments, interest):
    interest = interest / 12 / 100
    return (loan_principal * ((interest * math.pow(1 + interest, payments))
                              / (math.pow(1 + interest, payments) - 1)))


# def principal_of_loan(payments, payment, interest):
#     interest = interest / 12 / 100
#     return (payment / ((interest * (1 + interest) ** payments)
#                        / ((1 + interest) ** payments) - 1))


# def principal_of_loan(payments, payment, interest):
#     interest = interest / 12 / 100
#     ret_val = payment / ((interest * math.pow(1 + interest, payments))
#                           / (math.pow(1 + interest, payments)) - 1)
#     return math.floor(ret_val)

def principal_of_loan(payments, payment, interest):
    interest = interest / 12 / 100
    ret_val = payment / ((interest * math.pow(1 + interest, payments))
                         / (math.pow(1 + interest, payments) - 1))
    return math.floor(ret_val)


choice: str = input("""What would you like to calculate?\n
                  type 'n' for number of monthly payments,\n
                  type 'a' for the annuity monthly payment amount,\n 
                  type 'p' for the principal: \n""")

if choice.lower() == 'n':
    principal = float(input("Please enter your loan principal:\n"))
    payment_amount = float(input("Please enter your monthly payment amount:\n"))
    interest_rate = float(input("Please enter your interest rate:\n"))
    ret = number_of_payments(payment_amount, principal, interest_rate)
    year, month = divmod(ret, 12)
    if ret <= 12.0:
        if ret == 1:
            print("It will take 1 month to repay this loan")
        else:
            print("It will take {} months to repay this loan".format(int(math.ceil(ret))))
    else:
        print("It will take {} years and {} months to repay this loan".format(
            int(math.ceil(year)), int(math.ceil(month))))

if choice.lower() == 'a':
    principal = float(input("Please enter your loan principal:\n"))
    num_payments = float(input("Please enter the number of payments:\n"))
    interest_rate = float(input("Please enter your interest rate:\n"))
    ret = monthly_payment(principal, num_payments, interest_rate)
#    if ret > 0:
#        raise ValueError("Check your inputs, as the result came out negative.")
#    else:
    print("Your monthly bill is {}".format(int(math.ceil(ret))))

if choice.lower() == 'p':
    payment_amount = float(input("Please enter your monthly payment amount:\n"))
    num_payments = float(input("Please enter the number of payments:\n"))
    interest_rate = float(input("Please enter your interest rate:\n"))
    ret = principal_of_loan(num_payments, payment_amount, interest_rate)
#    if ret > 0:
#        raise ValueError("Check your inputs, as the result came out negative.")
#    elif ret == 0:
#        print("You're paid off!")
#    else:
    print("The principal of your loan is {}".format(ret))
