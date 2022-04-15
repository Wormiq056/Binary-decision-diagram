import sys
import time

from BDD import BDD_tree as BDD

variable13_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
variable14_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
tree = BDD.BDD()


def evaluate(function, values):
    result = 0
    variable_values = {}
    for i in range(len(values)):
        variable_values[variable14_list[i]] = values[i]

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


testBfunc13 = []
testBfunc14 = []
testvalues13 = []
testvalues14 = []
testvalues8=[]
fail = []
fail_input=[]
with open("testData/testBfunc13.txt", "r") as file:
    testBfunc13 = file.read().split("\n")

with open("testData/testBfunc14.txt", "r") as file:
    testBfunc14 = file.read().split("\n")

with open("testData/testvalues13.txt", "r") as file:
    testvalues13 = file.read().split("\n")

with open("testData/testvalues14.txt", "r") as file:
    testvalues14 = file.read().split("\n")


with open("testData/testvalues8.txt", "r") as file:
    testvalues8 = file.read().split("\n")

def test13():
    creation_time = 0
    use_time = 0
    for i in range(5):
        print("Tesiting " + str(i))
        for j in range(len(testvalues13)):
            creation_t1 = time.time()  # zaciatocny cas

            tree = BDD.BDD()
            tree.create(testBfunc13[i], variable13_list)

            creation_t2 = time.time()
            creation_time += creation_t2 - creation_t1
            # print(tree.unique_nodes)
            use_t1 = time.time()

            tree_result = tree.use(testvalues13[j])

            use_t2 = time.time()
            use_time = use_t2 - use_t1
            evaluate_result = evaluate(testBfunc13[i], testvalues13[j])
            if tree_result != evaluate_result:
                print("lul")


    print(creation_time)
    print(use_time)


test13()
# print(fail_input)
# tree = BDD.BDD()
# tree.create("ICD!L!B+AEFGHJKM",['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
#
# print(tree.use("0000000001110"))
# print(evaluate("ICD!L!B+AEFGHJKM","0000000001110"))