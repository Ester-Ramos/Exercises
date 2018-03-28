def max_profit(prices):
    """Given an array with prices of a given stock per day, if you are
    only permited to complete one transaction (buy one and sell one share of stock), design an algorithm to find the maximum profit
    Example:
    input = [7,1,5,3,6,4]
    output = 5
    """
    #My first attempt at the problem:
    #corner cases
    if prices == [] or prices == None:
        return 0

    #I am looking for an interval where there's a minimum in the left and a maximum in the right. To do this I create two functions: one that slices the list in the first min, and another that slices the list in the firts max
    def profit_right(prices):
        while prices.index(max(prices))< prices.index(min(prices)):

            if prices.index(min(prices)) == len(prices)-1:
                return 0
            prices = prices[prices.index(min(prices)):]
        return max(prices) - min(prices)

    def profit_left(prices):

        while prices.index(max(prices))< prices.index(min(prices)):

            if prices.index(max(prices)) == 0:
                return 0
        prices = prices[:prices.index(max(prices))+1]
        return max(prices) - min(prices)


    return max(profit_right(prices), profit_left(prices))

def max_profit_redux(prices):
    """second attempt at the problem. Another way is to always look for the min and the difference between each point and said min. And finally keeping the maximun difference"""

    if prices == [] or prices == None:
        return 0
        
    min_here = prices[0]
    max_diff = 0
    for num in prices:
        min_here = min(min_here, num)
        max_diff = max(num - min_here, max_diff)
    return max_diff
