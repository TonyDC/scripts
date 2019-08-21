import sys
import json
from pprint import pprint

import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code, region_code_for_number, NumberParseException

# Function definitions


def get_country_cca2(phone_number: str) -> str:
    """
    Retrieves the alpha-2 country code from the phone number

    Parameters:
    phone_number (int): The phone number tfrom which the country code is to be extracted

    Returns:
    str: the alpha-2 country code corresponding to the supplied phone number

    Throws:
    NumberParseException: the supplied phone number is invalid
    """
    number_obj = phonenumbers.parse(phone_number, None)

    return region_code_for_country_code(number_obj.country_code)


def build_country_map(file_path: str) -> dict:
    """
    Retrieves the alpha-2 country code from the phone number

    Parameters:
    file_path (str): the path to the JSON file containing the country informatino

    Returns:
    dict: a dictionary containing information of the countries, indexed by the alpha-2 country code

    Throws:
    The underlying libraries may throw exceptions that are not documented here
    """
    country_map = {}

    with open(file_path) as json_file:
        country_list = json.load(json_file)

        for entry in country_list:
            entry_indicative = entry["alpha-2"].upper()
            country_map[entry_indicative] = entry

    return country_map


# Main program cycle

country_map = build_country_map("country-list.json")

if __name__ == "__main__":
    while True:
        try:
            phone_number = input("Phone number (Ctrl+D to exit): ")
            country_entry = country_map.get(
                get_country_cca2(phone_number).upper())
            if country_entry is None:
                print("Country not found")
            else:
                print("CCA 2: {}\nCCN 3: {}\n".format(
                    country_entry["alpha-2"], country_entry["country-code"]))
        except NumberParseException:
            print("Invalid phone number\n")
        except (EOFError, KeyboardInterrupt):
            print("\n\nExit")
            sys.exit(0)
