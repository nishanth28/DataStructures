#knapsack problem
#tougher ones
#dynamic programming and memoization

def rec_coin(target,coins):

    #default value is set to target
    min_coins = target

    #check to see if the target is in the coin
    if target in coins:
        return 1

    else:
        # for every coin value that is <=my target
        #grabbing all the coins for coins less that target

        for i in [c for c in coins if c<=target ]:

            #add a coin count and recursive
            num_coins = 1 + rec_coin(target-i,coins)

            #reset min if new number of coins is less than min
            if num_coins < min_coins:

                min_coins = num_coins



    return min_coins

# known_result = cache
def dynamic_coin(target,coins,known_results):

    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1

    #return unknown result if it happens to be greater than 1
    elif known_results[target]>0:
        return known_results[target]

    else:

        #for every coin value in target
        for i in [c for c in coins if c<=target]:

            num_coins = 1 + dynamic_coin(target-i,coins,known_results)

            if num_coins < min_coins:

                min_coins = num_coins

                #reset the known result
                known_results[target] = min_coins

    return min_coins


target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

print dynamic_coin(target,coins,known_results)
