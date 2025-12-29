from decimal import Decimal
mistake_list=[]
file = open('purchases.txt')
path = [line.strip().split(';') for line in file]
def read_purchases(path):
    my_list = []
    global mistake_list
    for line in path:
        if len(line) != 5:
            mistake_list.append(line)
        else:
            if any(i.isalpha() for i in line[3]) or line[3] == '':
                mistake_list.append(line)
            elif float(line[3]) < 0:
                mistake_list.append(line)
            else:
                if any(x.isalpha() for x in line[4]) or line[4] == '':
                    mistake_list.append(line)
                elif float(line[4]) <= 0:
                    mistake_list.append(line)
                else:
                    continue
    for line_right in path:
        if line_right not in mistake_list:
            right_dict = {}
            right_dict['YYYY-MM-DD'] = line_right[0]
            right_dict['category'] = line_right[1]
            right_dict['name'] = line_right[2]
            right_dict['price'] = line_right[3]
            right_dict['quality'] = line_right[4]
            my_list.append(right_dict)
    file.close()
    return my_list


my_dict = read_purchases(path)

def count_errors(path):
    return len(path)


cnt_mistakes = count_errors(mistake_list)


def total_spent(purchases):
    sum = 0
    for line in purchases:
        sum += float(Decimal(line['price']) * Decimal(line['quality']))
    return sum


spent = total_spent(my_dict)

category_list = {}


def spent_by_category(purchases):
    global category_list
    category_list = list(set([line['category'] for line in purchases]))
    sum_list = [0 for _ in range(len(category_list))]
    sum_dict = {}
    for i in range(len(category_list)):
        for line in purchases:
            if line['category'] == category_list[i]:
                sum_list[i] += float((Decimal(line['price'])) * (Decimal(line['quality'])))
    for i in range(len(sum_list)):
        sum_dict[category_list[i]] = sum_list[i]
    return sum_dict


sum_of_category = spent_by_category(my_dict)

def top_n_expensive(purchases, n=3):
    sorted_purchases = sorted(purchases, key=lambda purchases: float(Decimal(purchases['price']) * Decimal(purchases['quality'])),
                              reverse=True)
    list_top = []
    for i in range(n):
        list_top.append(
            f'{sorted_purchases[i]['name']}: {float(Decimal(sorted_purchases[i]['price']) * Decimal(sorted_purchases[i]['quality']))}')
    return list_top


top_n = top_n_expensive(my_dict)


def write_report(purchases, errors, mistakes, total_spent, spent_category, top, out_path):
    with open(out_path, 'w') as file:
        file.write(f'Валидные строки: {str(purchases)}\n')
        file.write(f'Ошибочные строки: {str(errors)}\n')
        file.write(f'Количество ошибочных строк: {str(mistakes)}\n')
        file.write(f'Общая сумма трат: {str(total_spent)}\n')
        file.write(f'По следующим категориям потрачено: {str(spent_category)}\n')
        file.write(f'Топ 3 Покупок по тратам: {str(top)}\n')

print(my_dict)
print(mistake_list)
print(cnt_mistakes)
print(spent)
print(sum_of_category)
print(top_n)