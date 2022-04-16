import sys
import time

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


def test5():
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc5)):
        print("Tesiting " + str(i + 1))
        for j in range(len(testvalues5)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc5[i], variable5_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues5[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc5[i], testvalues5[j])
            reduction=reduction +(len(tree.used_nodes)/((2**6)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc5[j])
                print(testvalues5[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print(creation_time)
    print(use_time)
    print(whole_time)
    reduction=reduction/32
    print(100-reduction)
    print(incorrect_tree)

def test9():
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc9)):
        print("Tesiting " + str(i + 1))
        for j in range(len(testvalues9)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc9[i], variable9_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues9[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc9[i], testvalues9[j])
            reduction=reduction +(len(tree.used_nodes)/((2**10)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc9[j])
                print(testvalues9[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print(creation_time)
    print(use_time)
    print(whole_time)
    reduction=reduction/512
    print(100-reduction)
    print(incorrect_tree)

def test13():
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc13)):
        print("Tesiting " + str(i + 1))
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
    print(creation_time)
    print(use_time)
    print(whole_time)
    reduction=reduction/8192
    print(100-reduction)
    print(incorrect_tree)

def test14():
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc14)):
        print("Tesiting " + str(i + 1))
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
    print(creation_time)
    print(use_time)
    print(whole_time)
    reduction=reduction/16384
    print(100-reduction)
    print(incorrect_tree)

def test15():
    creation_time = 0
    use_time = 0
    incorrect_tree = 0
    time1 = time.time()
    reduction=0
    for i in range(len(testBfunc15)):
        print("Tesiting " + str(i + 1))
        for j in range(1000):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc15[i], variable15_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1

            use_t1 = time.time()

            tree_result = tree.use(testvalues15[j])

            use_t2 = time.time()
            use_time =use_time+ use_t2 - use_t1
            evaluate_result = evaluate(testBfunc15[i], testvalues15[j])
            reduction=reduction +(len(tree.used_nodes)/((2**16)-1))
            if tree_result != evaluate_result:
                print("Tree was incorrect")
                print(testBfunc15[j])
                print(testvalues15[i])
                break
    time2 = time.time()
    whole_time = time2 - time1
    print(creation_time)
    print(use_time)
    print(whole_time)
    reduction=reduction/1000
    print(100-reduction)
    print(incorrect_tree)

#test5()
#test9()
#test13()
#test14()
#test15()
