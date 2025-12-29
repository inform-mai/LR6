from main import *

def testing_valid():
    my_list = [['2025-06-09', 'super', 'bow', '20.1', '12'], ['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
               ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20'],
               ['2025-12-20', 'power', 'lower', '0', '12'], ['2025-08-08', 'yelka', 'derevo', '8.6', '10'],
               ['2021-12-12', 'metal', 'olovo', '123', '1']]
    assert read_purchases(my_list) == [{'YYYY-MM-DD': '2025-06-09', 'category': 'super', 'name': 'bow',
                                       'price': '20.1', 'quality': '12'}, {'YYYY-MM-DD': '2025-12-20',
                                                                          'category': 'power', 'name': 'lower',
                                                                          'price': '0', 'quality': '12'}, {
        'YYYY-MM-DD': '2025-08-08', 'category': 'yelka', 'name': 'derevo', 'price': '8.6', 'quality': '10'}, {
        'YYYY-MM-DD': '2021-12-12', 'category': 'metal', 'name': 'olovo', 'price': '123', 'quality': '1'}]

def testing_mistakes():
    my_list = [['2025-06-09', 'super', 'bow', '20.1', '12'], ['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
               ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20'],
               ['2025-12-20', 'power', 'lower', '0', '12'], ['2025-08-08', 'yelka', 'derevo', '8.6', '10'],
               ['2021-12-12', 'metal', 'olovo', '123', '1']]
    mistake_list = [['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
                    ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20']]
    right_list = read_purchases(my_list)
    assert all(right_line not in mistake_list for right_line in right_list)
    print(mistake_list)

def testing_cnt_mistakes():
    my_list = [['2025-06-09', 'super', 'bow', '20.1', '12'], ['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
               ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20'],
               ['2025-12-20', 'power', 'lower', '0', '12'], ['2025-08-08', 'yelka', 'derevo', '8.6', '10'],
               ['2021-12-12', 'metal', 'olovo', '123', '1']]
    mistake_list = [['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
                    ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20']]
    cnt_mistakes = count_errors(mistake_list)
    assert cnt_mistakes == 3

def testing_totalsum():
    my_list = [['2025-06-09', 'super', 'bow', '20.1', '12'], ['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
               ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20'],
               ['2025-12-20', 'power', 'lower', '0', '12'], ['2025-08-08', 'yelka', 'bow', '8.6', '10'],
               ['2021-12-12', 'metal', 'olovo', '123', '1']]
    right_list = read_purchases(my_list)
    assert total_spent(right_list) == 450.2

def testing_category():
    my_list = [['2025-06-09', 'super', 'bow', '20.1', '12'], ['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
               ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20'],
               ['2025-12-20', 'power', 'lower', '0', '12'], ['2025-08-08', 'yelka', 'bow', '8.6', '10'],
               ['2021-12-12', 'super', 'olovo', '123', '1']]
    right_list = read_purchases(my_list)
    category_sum = spent_by_category(right_list)
    assert category_sum == {'super':364.2, 'power': 0, 'yelka': 86}

def testing_top_n():
    my_list = [['2025-06-09', 'super', 'bow', '20.1', '12'], ['2025-06-08', 'slovo', 'lobik', 'lovalova', '1'],
               ['2025-06-07', 'lov', 'vol', '20', 'hyper'], ['2025-06-07', '12', '20'],
               ['2025-12-20', 'power', 'lower', '0', '12'], ['2025-08-08', 'yelka', 'bow', '8.6', '10'],
               ['2021-12-12', 'super', 'olovo', '123', '1']]
    right_list = read_purchases(my_list)
    right_top_n = top_n_expensive(right_list)
    assert right_top_n == [f'bow: {241.2}',f'olovo: {123.0}',f'bow: {86.0}']


