#importing packages
import numpy as np
import matplotlib.pyplot as plt

def St_Pradaox_Game(n_simulations):
    res = 0
    arr1 = []
    arr2=[]
    for i in range(n_simulations):
        
        coin = 1
        heads_so_far = 0
        
        while coin == 1:
            #creating bionomial distribution for flip
            coin = np.random.binomial(1, 0.5)
            #if coin toss is = 1, then we keep going and
            # count the # of consecutive tails
            if coin == 1:
                heads_so_far += 1
        
        #we enter this when we break our streak
        # if we get more than 1 head...
        
            #...we calculate our winnings
        new_res = 2 ** (heads_so_far+1)
        #and append it to our running total for the simulation
        res += new_res
        #and append the instance to a list
        arr1.append(new_res)
        arr2.append(res / len(arr1))

  
    arr1 = np.array(arr1, dtype=np.int32)
    print("Total Winnings:", res)
    print("Expected Winnings:", res / n)
    print("Median Winnings:", np.median(arr1), "\n")

    bins = np.bincount(arr1)
    unique = np.unique(arr1)

    for u in unique:
        print("Won ${}: {} times".format(u, bins[u]))

    plt.plot(arr2)
    plt.title(str(n_simulations) +" Runs")
    plt.xlabel('Runs')
    plt.ylabel('Average Earnings')
    

#driver code
n = 100000
St_Pradaox_Game(n)
