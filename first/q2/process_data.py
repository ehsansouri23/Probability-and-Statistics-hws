import pandas


def find(data_train):
    print("find")
    probability_a = 0.0
    probability_b = 0.0
    number_a = 0.0
    number_b = 0.0
    for p in range(1600):
        if data_train.values[p, 1593] == 1:
            probability_a = probability_a + 1
            number_a = number_a + 1
        elif data_train.values[p, 1593] == -1:
            probability_b = probability_b + 1
            number_b = number_b + 1
    probability_a = probability_a / 1600
    probability_b = probability_b / 1600
    return probability_a, number_a, probability_b, number_b


data_set_train = pandas.read_csv('train.csv', header=None)
data_set_test = pandas.read_csv('test.csv', header=None)

probability_a, number_a, probability_b, number_b = find(data_set_train)
print(probability_a)
print(number_a)
print(probability_b)
print(number_b)
