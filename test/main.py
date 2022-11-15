<<<<<<< HEAD:test/main.py
import sys
import time
import random

from BDD import BDD_tree as BDD

variable5_list = ['A', 'B', 'C', 'D', 'E']
variable9_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
variable13_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
variable14_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']


variable15_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O']
def evaluate(function, values):
    result = 0
    variable_values = {}
    for i in range(len(values)):
        variable_values[variable15_list[i]] = values[i]

    function = function.split("+")
    for i in range(len(function)):
        temporary_result = 1
        for j in range(len(function[i])):
            if function[i][j] == "!":
                continue
            else:
                if function[i][j - 1] == "!":
                    current_value = variable_values.get(function[i][j])
                    if current_value == "1":
                        current_value = 0
                    else:
                        current_value = 1
                    temporary_result = temporary_result * current_value
                else:
                    temporary_result = temporary_result * int(variable_values.get(function[i][j]))
        result = result + temporary_result

    if result >= 1:
        return True
    else:
        return False

testBfunc5 = []
testBfunc9 = []
testBfunc13 = []
testBfunc14 = []
testBfunc15 = []
testvalues5 = []
testvalues9 = []
testvalues13 = []
testvalues14 = []
testvalues15 = []

with open("testData/testBfunc5.txt", "r") as file:
    testBfunc5 = file.read().split("\n")

with open("testData/testvalues5.txt", "r") as file:
    testvalues5 = file.read().split("\n")

with open("testData/testBfunc9.txt", "r") as file:
    testBfunc9 = file.read().split("\n")

with open("testData/testvalues9.txt", "r") as file:
    testvalues9 = file.read().split("\n")


with open("testData/testBfunc13.txt", "r") as file:
    testBfunc13 = file.read().split("\n")

with open("testData/testBfunc14.txt", "r") as file:
    testBfunc14 = file.read().split("\n")

with open("testData/testvalues13.txt", "r") as file:
    testvalues13 = file.read().split("\n")

with open("testData/testvalues14.txt", "r") as file:
    testvalues14 = file.read().split("\n")

with open("testData/testBfunc15.txt", "r") as file:
    testBfunc15 = file.read().split("\n")

with open("testData/testvalues15.txt", "r") as file:
    testvalues15 = file.read().split("\n")


#test with 5 unique variables as shown in documentation
def test5():
    print("********Starting test for 5 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0 #variable to store creation time of the tree
    use_time = 0 #variable to store use function time
    time1 = time.time()
    reduction=0 #variable to store reduction % of the tree
    for i in range(len(testBfunc5)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues5)):
            creation_t1 = time.time()  #

            tree = BDD.BDD()
            tree.create(testBfunc5[i], variable5_list) #creation of tree

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues5[j]) #using tree

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc5[i], testvalues5[j]) #getting evaluation of function
            reduction=reduction +(len(tree.used_nodes)/((2**6)-1))
            if tree_result != evaluate_result: #if tree was created inccorectly
                print("Tree was incorrect")
                print(testBfunc5[j])
                print(testvalues5[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time/100)+" seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time/100/32)+" seconds")
    print("Average time for using the tree function use()")
    print(str(use_time/100/32)+" seconds")
    print("Average reduction of the tree:")
    reduction=reduction/32
    print(str(100-reduction)+"%")

#test with 9 unique variables as shown in documentation
def test9():
    print("********Starting test for 9 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0 #variable to store creation time of the tree
    use_time = 0 #variable to store use function time
    time1 = time.time()
    reduction=0 #variable to store reduction % of the tree
    for i in range(len(testBfunc9)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues9)):
            creation_t1 = time.time()  #

            tree = BDD.BDD()
            tree.create(testBfunc9[i], variable9_list) #creation of tree

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues9[j]) #using tree

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc9[i], testvalues9[j]) #getting evaluation of function
            reduction=reduction +(len(tree.used_nodes)/((2**10)-1))
            if tree_result != evaluate_result: #if tree was created inccorectly
                print("Tree was incorrect")
                print(testBfunc9[j])
                print(testvalues9[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time/100)+" seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time/100/2**9)+" seconds")
    print("Average time for using the tree function use()")
    print(str(use_time/100/2**9)+" seconds")
    print("Average reduction of the tree:")
    reduction=reduction/2**9
    print(str(100-reduction)+"%")

#test with 13 unique variables as shown in documentation
def test13():
    print("********Starting test for 13 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc13)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues13)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc13[i], variable13_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues13[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc13[i], testvalues13[j])
            reduction=reduction +(len(tree.used_nodes)/((2**14)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc13[j])
                print(testvalues13[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time / 100) + " seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time / 100 / 2 ** 13) + " seconds")
    print("Average time for using the tree function use()")
    print(str(use_time / 100 / 2 ** 13) + " seconds")
    print("Average reduction of the tree:")
    reduction = reduction / 2 ** 13
    print(str(100 - reduction) + "%")

#test with 14 unique variables as shown in documentation
def test14():
    print("********Starting test for 14 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc14)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues14)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc14[i], variable14_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues14[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc14[i], testvalues14[j])
            reduction=reduction +(len(tree.used_nodes)/((2**15)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc14[j])
                print(testvalues14[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time / 100) + " seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time / 100 / 2 ** 14) + " seconds")
    print("Average time for using the tree function use()")
    print(str(use_time / 100 / 2 ** 14) + " seconds")
    print("Average reduction of the tree:")
    reduction = reduction / 2 ** 14
    print(str(100 - reduction) + "%")

#test with 15 unique variables as shown in documentation
def test15():
    print("********Starting test for 15 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc15)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(1000):
            creation_t1 = time.time()  # zaciatocny cas
            choice=random.choice(testvalues15)
            tree = BDD.BDD()
            tree.create(testBfunc15[i], variable15_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(choice)

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc15[i], choice)
            reduction=reduction +(len(tree.used_nodes)/((2**16)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc15[j])
                print(choice)
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time / 100) + " seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time / 100 / 1000) + " seconds")
    print("Average time for using the tree function use()")
    print(str(use_time / 100 / 1000) + " seconds")
    print("Average reduction of the tree:")
    reduction = reduction / 1000
    print(str(100 - reduction) + "%")

#test5()
#test9()
test13()
#test14()
#test15()
=======
import sys
import time
import random

from BDD import BDD_tree as BDD

variable5_list = ['A', 'B', 'C', 'D', 'E']
variable9_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
variable13_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
variable14_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']


variable15_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O']
def evaluate(function, values):
    result = 0
    variable_values = {}
    for i in range(len(values)):
        variable_values[variable15_list[i]] = values[i]

    function = function.split("+")
    for i in range(len(function)):
        temporary_result = 1
        for j in range(len(function[i])):
            if function[i][j] == "!":
                continue
            else:
                if function[i][j - 1] == "!":
                    current_value = variable_values.get(function[i][j])
                    if current_value == "1":
                        current_value = 0
                    else:
                        current_value = 1
                    temporary_result = temporary_result * current_value
                else:
                    temporary_result = temporary_result * int(variable_values.get(function[i][j]))
        result = result + temporary_result

    if result >= 1:
        return True
    else:
        return False

testBfunc5 = []
testBfunc9 = []
testBfunc13 = []
testBfunc14 = []
testBfunc15 = []
testvalues5 = []
testvalues9 = []
testvalues13 = []
testvalues14 = []
testvalues15 = []

with open("testData/testBfunc5.txt", "r") as file:
    testBfunc5 = file.read().split("\n")

with open("testData/testvalues5.txt", "r") as file:
    testvalues5 = file.read().split("\n")

with open("testData/testBfunc9.txt", "r") as file:
    testBfunc9 = file.read().split("\n")

with open("testData/testvalues9.txt", "r") as file:
    testvalues9 = file.read().split("\n")


with open("testData/testBfunc13.txt", "r") as file:
    testBfunc13 = file.read().split("\n")

with open("testData/testBfunc14.txt", "r") as file:
    testBfunc14 = file.read().split("\n")

with open("testData/testvalues13.txt", "r") as file:
    testvalues13 = file.read().split("\n")

with open("testData/testvalues14.txt", "r") as file:
    testvalues14 = file.read().split("\n")

with open("testData/testBfunc15.txt", "r") as file:
    testBfunc15 = file.read().split("\n")

with open("testData/testvalues15.txt", "r") as file:
    testvalues15 = file.read().split("\n")


#test with 5 unique variables as shown in documentation
def test5():
    print("********Starting test for 5 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0 #variable to store creation time of the tree
    use_time = 0 #variable to store use function time
    time1 = time.time()
    reduction=0 #variable to store reduction % of the tree
    for i in range(len(testBfunc5)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues5)):
            creation_t1 = time.time()  #

            tree = BDD.BDD()
            tree.create(testBfunc5[i], variable5_list) #creation of tree

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues5[j]) #using tree

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc5[i], testvalues5[j]) #getting evaluation of function
            reduction=reduction +(len(tree.used_nodes)/((2**6)-1))
            if tree_result != evaluate_result: #if tree was created inccorectly
                print("Tree was incorrect")
                print(testBfunc5[j])
                print(testvalues5[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time/100)+" seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time/100/32)+" seconds")
    print("Average time for using the tree function use()")
    print(str(use_time/100/32)+" seconds")
    print("Average reduction of the tree:")
    reduction=reduction/32
    print(str(100-reduction)+"%")

#test with 9 unique variables as shown in documentation
def test9():
    print("********Starting test for 9 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0 #variable to store creation time of the tree
    use_time = 0 #variable to store use function time
    time1 = time.time()
    reduction=0 #variable to store reduction % of the tree
    for i in range(len(testBfunc9)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues9)):
            creation_t1 = time.time()  #

            tree = BDD.BDD()
            tree.create(testBfunc9[i], variable9_list) #creation of tree

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues9[j]) #using tree

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc9[i], testvalues9[j]) #getting evaluation of function
            reduction=reduction +(len(tree.used_nodes)/((2**10)-1))
            if tree_result != evaluate_result: #if tree was created inccorectly
                print("Tree was incorrect")
                print(testBfunc9[j])
                print(testvalues9[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time/100)+" seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time/100/2**9)+" seconds")
    print("Average time for using the tree function use()")
    print(str(use_time/100/2**9)+" seconds")
    print("Average reduction of the tree:")
    reduction=reduction/2**9
    print(str(100-reduction)+"%")

#test with 13 unique variables as shown in documentation
def test13():
    print("********Starting test for 13 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc13)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues13)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc13[i], variable13_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues13[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc13[i], testvalues13[j])
            reduction=reduction +(len(tree.used_nodes)/((2**14)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc13[j])
                print(testvalues13[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time / 100) + " seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time / 100 / 2 ** 13) + " seconds")
    print("Average time for using the tree function use()")
    print(str(use_time / 100 / 2 ** 13) + " seconds")
    print("Average reduction of the tree:")
    reduction = reduction / 2 ** 13
    print(str(100 - reduction) + "%")

#test with 14 unique variables as shown in documentation
def test14():
    print("********Starting test for 14 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc14)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(len(testvalues14)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc14[i], variable14_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues14[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc14[i], testvalues14[j])
            reduction=reduction +(len(tree.used_nodes)/((2**15)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc14[j])
                print(testvalues14[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time / 100) + " seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time / 100 / 2 ** 14) + " seconds")
    print("Average time for using the tree function use()")
    print(str(use_time / 100 / 2 ** 14) + " seconds")
    print("Average reduction of the tree:")
    reduction = reduction / 2 ** 14
    print(str(100 - reduction) + "%")

#test with 15 unique variables as shown in documentation
def test15():
    print("********Starting test for 15 boolean functions with every possible argument combination********")
    print('\n')
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc15)):
        print("Testing is " + str(i + 1)+"% complete")
        for j in range(1000):
            creation_t1 = time.time()  # zaciatocny cas
            choice=random.choice(testvalues15)
            tree = BDD.BDD()
            tree.create(testBfunc15[i], variable15_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(choice)

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc15[i], choice)
            reduction=reduction +(len(tree.used_nodes)/((2**16)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc15[j])
                print(choice)
                break
    time2 = time.time()
    whole_time = time2 - time1
    print("\n")
    print("******Test results******")
    print("Average time to test every possible combination for 1 boolean function:")
    print(str(whole_time / 100) + " seconds")
    print("Averige time for creation of BDD tree:")
    print(str(creation_time / 100 / 1000) + " seconds")
    print("Average time for using the tree function use()")
    print(str(use_time / 100 / 1000) + " seconds")
    print("Average reduction of the tree:")
    reduction = reduction / 1000
    print(str(100 - reduction) + "%")

#test5()
#test9()
test13()
#test14()
#test15()
>>>>>>> 6d1ca5cf07360c553787305c0d70e6df9d7f4ba2:TestingProgram/main.py
