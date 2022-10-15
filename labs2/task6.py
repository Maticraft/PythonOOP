from task4 import min_max_avg
from task5 import split_list

# Function that returns the minimum and maximum of the negative and positive numbers from the tuple
def min_max_neg_pos(tpl):
    # Split the tuple to negative and positive numbers
    neg_tpl, pos_tpl = split_list(tpl)
    
    # Calculate the minimum and maximum of the negative numbers
    neg_min, neg_max, _ = min_max_avg(neg_tpl)
    
    # Calculate the minimum and maximum of the negative numbers
    pos_min, pos_max, _ = min_max_avg(pos_tpl)

    return neg_min, neg_max, pos_min, pos_max


tpl = (-1, -2, -3, -4, -5, 6, 7, 8, 9, 10)
neg_min, neg_max, pos_min, pos_max = min_max_neg_pos(tpl)
print("Min of negative numbers: ", neg_min)
print("Max of negative numbers: ", neg_max)
print("Min of positive numbers: ", pos_min)
print("Max of positive numbers: ", pos_max)