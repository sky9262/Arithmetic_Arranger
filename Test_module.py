import random
from arithmetic_arranger import arithmetic_arranger
import time

succ = 0
fail = 0

def test(total_number_of_test):
    start_time = time.time()
    # total_number_of_test = total_number_of_test

    def test(list_of_string):
        global succ, fail
        if "Error" not in str(arithmetic_arranger(list_of_string)):
            succ+=1
        else:
            fail+=1  
            print("Error when calling 'arithmetic_arranger()' with", list_of_string,"\nError reason ---->",arithmetic_arranger(list_of_string))


    n = random.randint(0,9999)
    list_of_string = []

    for i in range(0,total_number_of_test):
        list_of_string.append([f"{n} + {n}", f"{n} - {n}", f"{n} + {n}", f"{n} + {n}", f"{n} - {n}", f"{n} + {n}", f"{n} - {n}"])

    for i in range(0,len(list_of_string)):
        test(list_of_string[i])


    print(f"\n\n{total_number_of_test*'.'}","\n----------------------------------------------------------------------")
    print(f"Ran {total_number_of_test} tests in {(time.time() - start_time)} sec\nResult : Success-->{succ}  Failed-->{fail}.\n\nTested.")