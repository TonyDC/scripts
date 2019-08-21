def horse_position_equation(velocity: float, initial_position: float):
    # return lambda x: x * velocity + initial_position
    return lambda x: (x - initial_position) / velocity


def calculate_speed(horse_list: list, destination_point: int) -> float:
    max_time = max([
        horse_position_equation(v, p)(destination_point) for p, v in horse_list])
    return destination_point / max_time


def main():
    test_cases = int(input())

    for n_case in range(test_cases):
        destination_point, n_horses = map(int, input().split(" "))
        # List of pairs (initial position - km, maximum speed - km/h)
        horses = []

        for n_horse in range(n_horses):
            initial_pos, max_speed = map(int, input().split(" "))
            horses.append((initial_pos, max_speed))

        res = calculate_speed(horses, destination_point)

        print("Case #{0}: {1}".format(n_case + 1, res))


if __name__ == '__main__':
    main()
