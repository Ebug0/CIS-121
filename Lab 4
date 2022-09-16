lower = 1
upper = int(input("please Input the upper bound to check: "))
test = 1
run = 1
sumofd = 0
devisor = False
perfect = 0
abundant = 0
deficient = 0

while (run <= upper):
    
    test = 1
    sumofd = 0
    print(f"run {run}")
    while (test<run):
        if(run%test == 0):
            sumofd += test
        test +=1 
    if (sumofd < run):
        deficient += 1    
    elif (sumofd > run):
        abundant += 1
    elif (sumofd == run):
        perfect += 1
    else:
        print("something wrong happened")
    run +=1
    
        
print(f"Between 1 and {upper} there are \n{deficient} deficient numbers")
print(f"{perfect} perfect numbers \n{abundant} abundant numbers")

