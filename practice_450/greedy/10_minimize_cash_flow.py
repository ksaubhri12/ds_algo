from queue import PriorityQueue


def minimize_cash_flow(transactions, n):
    person_money_map = {}
    for i in range(0, n):
        for j in range(0, n):
            value_given = transactions[i][j]
            if value_given != 0:
                if i in person_money_map:
                    person_money_map[i] = person_money_map[i] + value_given
                else:
                    person_money_map[i] = value_given
                if j in person_money_map:
                    person_money_map[j] = person_money_map[j] - value_given
                else:
                    person_money_map[j] = -value_given
    giver_queue = PriorityQueue()
    receiver_queue = PriorityQueue()
    for key in person_money_map.keys():
        person_money = person_money_map[key]
        if person_money > 0:
            giver_queue.put((-person_money, person_money, key))
        elif person_money < 0:
            receiver_queue.put((person_money, person_money, key))

    result = [[]]

    while len(receiver_queue.queue) > 0 or len(giver_queue.queue) > 0:
        receiver_element = receiver_queue.get()
        give_element = giver_queue.get()
        receive_money = abs(receiver_element[1])
        give_money = abs(give_element[1])

        if receive_money > give_money:
            new_loan = give_money - receive_money
            transaction = [give_element[2], receiver_element[2], abs(give_money)]
            result.append(transaction)
            new_entry = (new_loan, new_loan, receiver_element[2])
            receiver_queue.put(new_entry)
        elif receive_money < give_money:
            new_loan = give_money - receive_money
            transaction = [give_element[2], receiver_element[2], abs(receive_money)]
            result.append(transaction)
            new_entry = (-new_loan, new_loan, give_element[2])
            giver_queue.put(new_entry)
        else:
            transaction = [give_element[2], receiver_element[2], abs(receive_money)]
            result.append(transaction)

    final_result_arr = [[0] * n for i1 in range(n)]

    for i in range(0, len(result)):
        trans = result[i]
        if len(result[i]) == 0:
            continue
        money = result[i][2]
        if money > 0:
            giver = result[i][0]
            receiver = result[i][1]
            giver_list = final_result_arr[giver]
            giver_list[receiver] = money

    return final_result_arr


def my_comparator(x):
    return -x


if __name__ == '__main__':
    trans_arr = [[0, 100, 0, 200], [0, 0, 300, 0], [0, 0, 0, 200], [0, 0, 0, 0]]
    print(minimize_cash_flow(trans_arr, 4))
    trans_arr = [[0, 2000, 4000], [0, 0, 3000], [0, 0, 0]]
    print(minimize_cash_flow(trans_arr, 3))
