def diamond_selection_order(diamonds, i, j):
    if abs(i-j) == 1:
        result = []
        result.append(max(diamonds[i], diamonds[j]))
        return result
    elif i == j:
        result = []
        result.append(diamonds[i])
        return result
    else:
        if diamonds[i+1] > diamonds[j]:
            low_1 = i + 2
            high_1 = j
        else:
            low_1 = i + 1
            high_1 = j - 1

        if diamonds[i] > diamonds[j-1]:
            low_2 = i + 1
            high_2 = j -1
        else:
            low_2 = i
            high_2 = j - 2

        result_1 = diamond_selection_order(diamonds, low_1, high_1)
        result_2 = diamond_selection_order(diamonds, low_2, high_2)

        if diamonds[i] + sum(result_1) > diamonds[j] + sum(result_2):
            result_1.append(diamonds[i])
            return result_1
        else:
            result_2.append(diamonds[j])
            return result_2

diamonds = [12, 20, 1, 2, 9]
    
result = diamond_selection_order(diamonds, 0, len(diamonds) - 1)
result.reverse()
print(result)
