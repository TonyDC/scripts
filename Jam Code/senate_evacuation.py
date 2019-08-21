def process_test_case(party_organization: list):
    sorted_party_organization = sorted(
        [(chr(ord('A') + i), int(x)) for i, x in enumerate(party_organization)], key=lambda x: x[1])
    res = []

    while len(sorted_party_organization) > 0:
        if len(sorted_party_organization) == 2:
            (party1_letter, party1_size), (party2_letter,
                                           party2_size) = sorted_party_organization
            if (party1_size == party2_size == 0):
                sorted_party_organization = []
            elif party1_size == party2_size:
                res.append(party1_letter + party2_letter)
                sorted_party_organization = [(party1_letter, party1_size - 1),
                                             (party2_letter, party2_size - 1)]
            continue

        party_name, party_size = sorted_party_organization.pop()
        res.append(party_name)
        if party_size > 1:
            sorted_party_organization.append((party_name, party_size - 1))
        sorted_party_organization = sorted(
            sorted_party_organization, key=lambda x: x[1])

    return res


def main():
    test_cases = int(input())

    for n_case in range(test_cases):
        n_parties = int(input())
        party_size = input().split(" ")
        res = process_test_case(party_size)

        print("Case #{0}: {1}".format(n_case + 1, " ".join(map(str, res))))


if __name__ == '__main__':
    main()
