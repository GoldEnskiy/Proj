def two_sum(nums: int, target: int) -> int:
    left, right = 0, len(nums)-1 # Указатели списка
    nums.sort() # Сортировка списка, для работы указателями

    while left < right:
        """
        Указатели проходятся по списку с двух сторон.

        Если target меньше current_sum - сдвигается правый указатель к левому. Что-бы current_sum уменьшалась.
        
        Если target больше current_sum - сдвигается левый указатель к правому. Что-бы current_sum увеличивалась.

        """

        current_sum = nums[left] + nums[right]

        if current_sum == target: # Если сумма нашлась
            return [left, right]

        elif current_sum < target: # Увелечение current_sum
            left += 1
        else: # Уменьшение current_sum
            right -= 1
        
    return [] # Если нету суммы равной target

print(two_sum([1, 2, 3, 4], 7))