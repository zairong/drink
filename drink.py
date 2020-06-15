import os
#讀取檔案            
def read_file(filename):
    drink =[]
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            drink.append([name, price])
    return drink


#輸入品項
def drink_input(drink):
    while True :
        name = input('輸入飲料名稱:')
        if name == 'q':
            break
        price = input('輸入價格:')
        drink.append([name, price])
    return drink

#寫入新品
def write_file(filename, drink):
    with open(filename, 'w', encoding= 'utf-8') as f:
        f.write('商品,價格\n')
        for p in drink:
            f.write(p[0] + ',' + p[1] + '\n' )
#印出商品及價格
def print_file(drink):
    for p in drink:
        print(p[0], '的價格是', p[1])
def print_tab():
	print('---------------------')
def main():
    filename = 'drink.csv'
    if os.path.isfile(filename):
        print('有此檔案')
        drink = read_file(filename)
    else:
        print('無此檔案')
    print_file(drink)
    drink = drink_input(drink)
    write_file('drink.csv', drink)
    print_tab()
    print_file(drink)
main()

