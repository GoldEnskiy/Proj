def twoSum(nums: int, target: int) -> int:
    for i in range(len(nums)): #Внешний цикл
        for j in range(len(nums)): #Внутренний цикл
            print(nums[i], ':', nums[j], nums[i]+nums[j]==target) #Для понятия, как циклы двигаются
            if i != j and nums[i] + nums[j] == target:
                '''
                Условие проверяет, что-бы число не суммировалось само с собой
                и равняется ли сумма двух чисел зачению target.
                '''
                result = f'{nums[i]} + {nums[j]} = {nums[i]+nums[j]}'
                return result
            
    return False # Возвращает False, если ни одна сумма чисел не возрвщает target число.

print(twoSum([1, 2, 3, 4], 7))