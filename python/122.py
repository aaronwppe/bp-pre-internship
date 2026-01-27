# Prog. 122
# Write a function to find nth smart number.


def get_smart_number(n: int):
    primes = [0] * 1000
    smart_number_count = -1

    for i in range(2, len(primes)):
        if primes[i] != 0:
            continue

        primes[i] = 1

        j = i * 2
        while j < len(primes):
            primes[j] -= 1

            if (primes[j] + 3) == 0:
                smart_number_count += 1
                if smart_number_count == n:
                    return j

            j += i

    raise ValueError("Out of range")


if __name__ == "__main__":
    print(get_smart_number(20))
