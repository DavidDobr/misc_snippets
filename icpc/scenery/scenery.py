
# coding: utf-8

# In[24]:

from math import factorial
import sys


def can_make_pictures(IN):
    
    data = IN.readlines()
    
    data = map(lambda x: x.strip('\n'), data)
    data = filter(lambda x: len(x) > 0, data) # remove empty lines
    data = map(lambda x: list(map(int, x.split(' '))), data)
    data = list(data)
    
    # The first line of the input contains two integers n (1≤n≤10**4) and t (1≤t≤10**5)
    # where n is the number of desired photographs and t is the time you spend to take each photograph
    n, t = data[0]
    photos = data[1:]
    photos = sorted(photos, key=lambda x: x[0]) # sort by earliest time

    
    max_perms = factorial(n) # n lines can be arranged in factorial(n) ways
    cnt = 1

    while cnt <= max_perms:
        # T is the current global time
        T = 0
        for i in range(n):
            line = photos[i]
            a, b = line
            if T <= a:
                # if it's earlier than minimum time, we'll have to wait
                T = a + t
            elif T > a:
                # if it's later than earliest time, start right away
                T = T + t

            # check if can make (i)th picture
            if T <= b:
                #ok
                # if this is the last element and it passed the test,
                # then we can make the pictures! Otherwise, continue
                if i+1 == n:
                    return 'yes'
                    sys.exit()
                else:
                    pass
            elif T > b:
                # FAIL!
                # move current element to the start
                photos[0], photos[i] = photos[i], photos[0]
                break # kill the FOR loop

        cnt += 1

    # <-- this point is reached only if no permutations were successfull
    # therefor it is not possible to take all the pictures
    return 'no'


# run when compiler runs my script

if __name__ == "__main__":
    # read data from standard input
    print(can_make_pictures(sys.stdin))

