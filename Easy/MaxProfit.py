
# Space Complexity: O(1) --> No extenr,al data structures are required
# Time Complexity: O(n) ---> Single pass over the array, scales linearlly as problem size icnreases

def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 1 or len(prices) == 0:
        return 0
    if len(prices) == 2:
        if prices[1] <= prices[0]:
            return 0
        else:
            return prices[1] - prices[0]

    sm = 1
    bm = 0
    profit = 0
    while sm < len(prices):
        if prices[sm] <= prices[bm]:
            bm = sm

        if sm == bm:
            sm = sm + 1

        if sm < len(prices) and prices[sm] - prices[bm] > profit:
            profit = prices[sm] - prices[bm]

        if sm < len(prices) and prices[sm] <= prices[bm]:
            bm = sm

        sm = sm + 1

    return profit