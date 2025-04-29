from functools import lru_cache

n = int(input())
def count_contains_digit_3(n: int) -> int:
    """
    Count numbers from 1 to n that contain digit '3'.
    Uses digit DP approach.
    """

    digits = list(map(int, str(n)))

    @lru_cache(None)
    def dp(pos: int, tight: bool, has_3: bool) -> int:
        if pos == len(digits):
            return int(has_3)  # Count if the number has 3
        limit = digits[pos] if tight else 9
        total = 0
        for d in range(0, limit + 1):
            total += dp(
                pos + 1,
                tight and (d == limit),
                has_3 or (d == 3)
            )
        return total

    return dp(0, True, False)

def count_contains_digit_3_and_div_3(n: int) -> int:
    """
    Count numbers from 1 to n that:
    - contain digit '3'
    - and are divisible by 3
    """

    digits = list(map(int, str(n)))

    @lru_cache(None)
    def dp(pos: int, tight: bool, has_3: bool, mod: int, leading_zero: bool) -> int:
        if pos == len(digits):
            return int(has_3 and mod == 0 and not leading_zero)

        limit = digits[pos] if tight else 9
        total = 0
        for d in range(0, limit + 1):
            total += dp(
                pos + 1,
                tight and (d == limit),
                has_3 or (d == 3),
                (mod * 10 + d) % 3 if not (leading_zero and d == 0) else 0,
                leading_zero and d == 0
            )
        return total

    return dp(0, True, False, 0, True)

def Nabeatu(n: int) -> int:
    count_div_3 = n // 3
    count_contains_3 = count_contains_digit_3(n)
    count_both = count_contains_digit_3_and_div_3(n)
    return count_div_3 + count_contains_3 - count_both


print(Nabeatu(n))