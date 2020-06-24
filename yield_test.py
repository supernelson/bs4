#yield_test.py

def yield_test():
    print ("hello world")
    yield
    print ("end")
    
yield_test()

def square_numbers(nums):
    for i in nums:       
        yield (i*i)
    
    # for i in nums:
    #     print (a)
        # if len(nums) <= len(nums):
        #     print (next(i))

def old_squares(nums):
    for i in nums:
        print (i*i)

a = [1,6,8,0,2,3]
square_numbers = (square_numbers(a))
list(square_numbers)
