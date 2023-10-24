from math import ceil
from math import floor
from math import log
import argparse


def args_len(arguments) -> int:
    return len(list(filter(None, arguments)))


def check_args_negativity(arguments) -> bool:
    for elem in arguments:
        if type(elem) != str:
            if elem < 0:
                return False
    return True


def check_args(arguments) -> bool:
    if args_len(list(filter(None, list(arguments.values())))) == 4\
            and check_args_negativity(list(filter(None, arguments)))\
            and arguments["credit_interest"] is not None:
        if arguments["credit_type"] == "diff":
            if arguments["credit_payment"] is None:
                return True
            return False
        return True
    return False


def main():
    parser = argparse.ArgumentParser(prog="financial_assistant",
                                     description="Calculate diff and annuity type of credit.",
                                     usage="%(prog)s [type of credit] [credit principal]"
                                           " [periods of credit] [credit interest]")
    parser.add_argument("--type", help="type of credit", choices=["diff", "annuity"])
    parser.add_argument("--payment", help="credit monthly payment", type=float)
    parser.add_argument("--principal", help="credit principal", type=int)
    parser.add_argument("--periods", help="periods of credit", type=int)
    parser.add_argument("--interest", help="credit interest", type=float)
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.2@alpha')
    args = parser.parse_args()

    credit_type: str = args.type
    credit_principal: int = args.principal
    credit_periods: int = args.periods
    credit_interest: float = args.interest
    credit_payment: float = args.payment
    credit_overpayment: int = 0

    if not check_args({
        "credit_type": credit_type,
        "credit_principal": credit_principal,
        "credit_periods": credit_periods,
        "credit_interest": credit_interest,
        "credit_payment": credit_payment
    }):
        print("Incorrect parameters")
    else:
        i: float = (credit_interest / 100) / 12

        if credit_type == "diff":
            for m in range(1, credit_periods + 1):
                credit_payment: int = ceil(credit_principal / credit_periods
                                           + i * (credit_principal
                                                  - (credit_principal * (m - 1) / credit_periods)))
                credit_overpayment += credit_payment
                print(f"Month {m}: paid out {credit_payment}")

            credit_overpayment -= credit_principal
            print(f"Overpayment = {credit_overpayment}")

        else:  # credit_type == "annuity":
            if credit_payment is None:
                credit_payment: int = ceil(credit_principal * (i * (1 + i) ** credit_periods)
                                           / ((1 + i) ** credit_periods - 1))
                print(f"Your annuity payment = {credit_payment}!")
            elif credit_principal is None:
                credit_principal: int = floor(credit_payment * ((1 + i) ** credit_periods - 1)
                                              / (i * (1 + i) ** credit_periods))
                print(f"Your credit principal = {credit_principal}!")
            else:  # credit_periods is None
                credit_periods: int = ceil(log(credit_payment / (credit_payment - i * credit_principal), 1 + i))
                years_count = credit_periods // 12
                months_count = credit_periods % 12
                if years_count > 0 and months_count > 0:
                    if years_count == 1 and months_count > 1:
                        print(f"You need {years_count} year and {months_count} months to repay this credit!")
                    elif years_count > 1 and months_count == 1:
                        print(f"You need {years_count} years and {months_count} month to repay this credit!")
                    else:
                        print(f"You need {years_count} years and {months_count} months to repay this credit!")
                else:
                    if years_count == 0 and months_count > 0:
                        if months_count > 1:
                            print(f"You need {months_count} months to repay this credit!")
                        else:
                            print(f"You need {months_count} month to repay this credit!")
                    elif years_count > 0 and months_count == 0:
                        if years_count > 1:
                            print(f"You need {years_count} years to repay this credit!")
                        else:
                            print(f"You need {years_count} year to repay this credit!")
                    else:
                        print(f"You was already repaid this credit!")

            credit_overpayment = abs(int(credit_payment * credit_periods - credit_principal))
            print(f"Overpayment = {credit_overpayment}")


if __name__ == '__main__':
    main()
