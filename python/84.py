# Prog. 084
# Write a function to find the n-th number in newman conway sequence.

def get_newman_conway_number(n: int) -> int | None:
    if n <= 0:
        return None
    
    if n <= 2:
        return 1
    
    dp = [0] * n
    dp[0] = 1   # P(1)
    dp[1] = 1   # P(2)

    return _newman_conway_number_dp(n, dp)


def _newman_conway_number_dp(n: int, dp: list[int]) -> int | None:
    if dp[n - 1] != 0:
        return dp[n - 1]
    
    dp[n - 2] = _newman_conway_number_dp(n-1, dp)
    dp[n - 1] = _newman_conway_number_dp(dp[n - 2], dp) + _newman_conway_number_dp(n - dp[n - 2], dp)

    return dp[n - 1]


if __name__ == "__main__":
    print(get_newman_conway_number(12))

# P(n) = P(P(n - 1)) + P(n - P(n - 1))
# where,
# P(n) = n-th number in Newman Conway Sequence
# with P(1) = P(2) = 1
