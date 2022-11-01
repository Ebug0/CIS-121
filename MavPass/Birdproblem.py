upper = 200
test = 1
run = 2


print("start")
while (run <= upper):
    test = 1
    offspring = 0
    while (test<=run):
        if(run%test == 0 and test !=1):
            offspring += 1
        test +=1 

    print(f"Bird {run} has {offspring} offspring")
    run +=1

