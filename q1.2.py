def get_input():
    total_cows = int(input(""))
    cow_str = input("")

    return total_cows, cow_str

def calc_lonely_cow(total_cows, cow_str):
    total_lonely_cow = 0
    #for offset in range(3, total_cows + 1):
    for offset in range(3, 60):
        for start_pos in range(0, total_cows):
            total_count_g = total_count_h = 0
            if start_pos + offset > total_cows:
                break
            for cur_index in range(start_pos, start_pos + offset):
                if cow_str[cur_index] == "G":
                    total_count_g += 1
                else:
                    total_count_h += 1

                if total_count_g >= 2 and total_count_h >= 2:
                    break
            if total_count_g == 1 or total_count_h == 1:
                total_lonely_cow += 1

    return total_lonely_cow


if __name__ == "__main__":
    total_cows, cow_str = get_input()
    #total_cows, cow_str = 5, "GHGHG"
    #total_cows, cow_str = 5, "GHGHG"
    print(calc_lonely_cow(total_cows, cow_str))
