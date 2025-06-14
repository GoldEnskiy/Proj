def two_sum(nums: int, target: int) -> int:
    """
    Создаем хэш-таблицу, в которую будут записываться числа со списка с их индексом.

    Создаем цикл с функцией enumerate(), которая достает {индекс(i) : число(num)}.

    Внутри цикла for создаем переменную seccond_summand, которая хранит в себе значение target - num,
    благодаря этой формуле мы достаем второе число, с помощью которого получается target.

    Создаем само условие, проверяющее, есть ли в нашем хэше это самое условие, и если оно есть, 
    то мы возвращаем победный результат.

    В ином случае в нашу hash_map добавляется {num(число) : i(индекс)} и цикл повторяется,
    пока не пройдет по условию, либо ничего не вернет.

    """
    hash_map = {} # Сама хэш-таблица

    for i, num in enumerate(nums): # Достаем {индекс(i) : число(num)}.
        seccond_summand = target - num # Находим нужные числа в сумме дающих target.

        if seccond_summand in hash_map: # Проверям есть ли у нас число, для нашей суммы.
            return [hash_map[seccond_summand], i] # Победное возвращение индексов.
        
        hash_map[num] = i # Добавляем {число(num) : индекс(i)}.
    
    return [] # Возвращаем пустой список, если нету подходящих чисел.

print(two_sum([1, 3, 4, 2, 5], 9))