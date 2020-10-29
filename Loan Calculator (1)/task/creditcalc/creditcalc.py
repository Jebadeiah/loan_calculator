import argparse
import math
import sys


def number_of_payments(payment, loan_principal, interest):
    if not interest:
        bad_par("num_interest")
    else:
        interest = interest / 12 / 100
    ret_val = math.log((payment / (payment - interest * loan_principal)), 1 + interest)
    return math.ceil(ret_val)


def monthly_payment(payments, loan_principal, interest):
    if not interest:
        bad_par("pay_interest")
    else:
        interest = interest / 12 / 100
    return (loan_principal * ((interest * math.pow(1 + interest, payments))
                              / (math.pow(1 + interest, payments) - 1)))


def principal_of_loan(payment, payments, interest):
    if not interest:
        bad_par("princ_interest")
    else:
        interest = interest / 12 / 100
    ret_val = payment / ((interest * math.pow(1 + interest, payments))
                         / (math.pow(1 + interest, payments) - 1))
    return math.floor(ret_val)


def differentiated_payment(payments, loan_principal, interest):
    if not interest:
        bad_par("diff_interest")
    else:
        interest = interest / 12 / 100
    odb = 0
    for rza in range(1, payments + 1):
        gza = math.ceil(loan_principal /
                        payments + interest * (loan_principal - (loan_principal * (rza - 1) / payments)))
        odb += gza
        print(f"Month {rza}: payment is {gza}")
    print(f"\nOverpayment = {int(odb - loan_principal)}!")


def bad_par(place):
    print(f"Incorrect parameters: {place}")
    sys.exit()


def overpayment(payment, payments, loan_principal):
    return int(payment * payments - loan_principal)


def main():
    parser = argparse.ArgumentParser(description='Calculate the different values of a loan.')
    parser.add_argument("-t", "--type", metavar='', type=str,
                        help='--type indicates the type of payment: "annuity"or "diff" (differentiated). If --type is '
                             'specified neither as "annuity" nor as "diff" or not specified at all, show the error '
                             'message.')
    parser.add_argument("-p", "--payment", metavar='', type=float,
                        help="--payment is the monthly payment amount. For --type=diff, the payment is different each "
                             "month, so we can't calculate months or principal, therefore a combination with --payment "
                             "is invalid, too.")
    parser.add_argument("-d", "--periods", metavar='', type=int,
                        help="--periods denotes the number of months needed to repay the loan. It's calculated based on"
                             "the interest, annuity payment, and principal.")
    parser.add_argument("-P", "--principal", metavar='', type=float,
                        help="--principal is used for calculations of both types of payment. You can get its value if "
                             "you know the interest, annuity payment, and number of months.")
    parser.add_argument("-i", "--interest", metavar='', type=float,
                        help="--interest is specified without a percent sign. Note that it can accept a floating-point "
                             "value. Our loan calculator can't calculate the interest, so it must always be provided. "
                             "These parameters are incorrect because --interest is missing.")
    args = parser.parse_args()

    if len(vars(args)) != 5:
        bad_par("Not enough values provided")
    else:
        if args.type == "annuity":
            if not args.payment:
                ret = math.ceil(monthly_payment(args.periods, args.principal, args.interest))
                print("Your annuity payment is {}!".format(ret))
                print("Overpayment = {}".format(overpayment(ret, args.periods, args.principal)))
            if not args.principal:
                ret = math.ceil(principal_of_loan(args.payment, args.periods, args.interest))
                print("The principal of your loan is {}!".format(ret))
                print("Overpayment = {}".format(overpayment(args.payment, args.periods, ret)))
            if not args.periods:
                ret = math.ceil(number_of_payments(args.payment, args.principal, args.interest))
                year, month = divmod(ret, 12)
                if ret <= 12.0:
                    if ret == 1:
                        print("It will take 1 month to repay this loan!")
                    else:
                        print("It will take {} months to repay this loan!".format(int(math.ceil(ret))))
                else:
                    if month == 0:
                        print("It will take {} years to repay this loan!".format(int(math.ceil(year))))
                    else:
                        print("It will take {} years and {} months to repay this loan!".format(
                            int(math.ceil(year)), int(math.ceil(month))))
                print("Overpayment = {}".format(overpayment(args.payment, ret, args.principal)))
        elif args.type == "diff":
            if args.payment:
                bad_par("Differential Payment")
            else:
                differentiated_payment(args.periods, args.principal, args.interest)

        else:
            bad_par("Type")


if __name__ == "__main__":
    main()
