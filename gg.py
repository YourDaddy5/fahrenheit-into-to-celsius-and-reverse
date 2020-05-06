what = input("1)Из цельсия в фаренгейт,2)из фраренгейт в цельсия. 1 или 2? ")
if what =='1' or what == 1:

    tmp = int(float(input('Введите градусы цельсия: ')))
    res = (tmp * 9/5) + 32
    print(tmp, 'по цельсию равно', res, 'по фаренгейту')

elif what == '2' or what == 2:
    tmp = int(float(input('Введите градусы фаренгейта: ')))
    res = (tmp - 32) * 5/9
    print(tmp , 'по фаренгейту равно',res, 'по цельсию')

else:
    print('Введите 1 или 2')
    