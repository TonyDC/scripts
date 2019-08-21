import math
import sys


def process_test_case(inf_limit: int, sup_limit: int, max_tries: int) -> None:
    for n_try in range(max_tries):
        guess = obtain_guess(inf_limit, sup_limit)
        response = exchange_response(guess)
        if response == "CORRECT":
            return
        elif response == "TOO_SMALL":
            inf_limit = guess + 1
        elif response == "TOO_BIG":
            sup_limit = guess - 1
        else:
            raise Exception("Bad output")


def obtain_guess(inf_limit: int, sup_limit: int) -> int:
    return math.ceil((inf_limit + sup_limit) / 2)


def exchange_response(guess: int) -> str:
    print(guess, flush=True)
    return input()


def main():
    test_cases = int(input())

    for n_case in range(test_cases):
        inf_limit, sup_limit = input().split(" ")
        max_tries = input()
        process_test_case(int(inf_limit) + 1, int(sup_limit), int(30))


main()
