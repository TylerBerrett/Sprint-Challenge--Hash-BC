#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    for i, item in enumerate(weights):
        hash_table_insert(ht, item, i)

    answer = []

    for weight in weights:
        if hash_table_retrieve(ht, limit - weight):
            answer.append(hash_table_retrieve(ht, limit - weight))

    if len(answer) == 0:
        return None

    if answer[0] == answer[1]:
        answer[1] = 0

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")