basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

f_cnt = 0
n_cnt = 0
for key,val in basket_items.items():
    if key in fruits:
        f_cnt += val
    else:
        n_cnt += val
print('과일은 {}개이고, {}개는 과일이 아닙니다.'.format(f_cnt,n_cnt))