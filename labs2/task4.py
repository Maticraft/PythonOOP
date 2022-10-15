# Function that calulates the minimum, maximum and average of the tuple
def min_max_avg(tpl):
    tpl_min = min(tpl)
    tpl_max = max(tpl)
    tpl_avg = sum(tpl)/len(tpl)
    return tpl_min, tpl_max, tpl_avg

if __name__ == '__main__':
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tpl_min, tpl_max, tpl_avg = min_max_avg(tpl)
    print("Min: ", tpl_min)
    print("Max: ", tpl_max)
    print("Avg: ", tpl_avg)
