def my_func(num_iters, initial, second):
    if num_iters == 0:
        print("Nothing to iterate")
        return "Dont iterate"
    
    counter = 0
    while initial > 0 and counter < 10:
        initial += second
        counter += 1
    else:
        if counter == 10:
            return "counter is 10"
        else:
            return "initial is {}".format(initial)
