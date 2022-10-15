# Split the list basing on the given threshold value.
def split_list(lst, threshold = 0):
    return [x for x in lst if x < threshold], [x for x in lst if x >= threshold]


if __name__ == '__main__':
    print("Default threshold:")
    print(split_list([-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]))
    print("Threshold = 7:")
    print(split_list([-1, -2, -3, -4, -5, 6, 7, 8, 9, 10], 7))