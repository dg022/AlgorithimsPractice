def fruits_into_baskets(fruits):
    # TODO: Write your code here
    basket = {}
    maxBasket = 0

    start = 0
    for end in range(len(fruits)):
        if fruits[end] not in basket:
            basket[fruits[end]] = 0
        else:
            basket[fruits[end]] += 1

        while len(basket) > 2:
            maxBasket = max(maxBasket, end - start + 1)
            if basket[fruits[start]] == 0:
                del basket[fruits[start]]
            else:
                basket[fruits[start]] -= 1
            start += 1

    return max(maxBasket, end - start + 1)

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()