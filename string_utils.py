def split_before_each_uppercases(formula):
    if not formula:
        return []
    start = 0
    split_formula = []
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula{start:1])
            start=1
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    digit_location=1
    while digit_location<len(formula) and not formula[digit_location].isdigit():
        digit_location+=1
        if digit_location==len(formula):
          return formula,1
        
    return formula[:digit_location],int(formula[digit_location:])


