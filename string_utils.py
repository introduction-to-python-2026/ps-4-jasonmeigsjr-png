def split_before_each_uppercases(formula):
    if not formula:
        return []
    start = 0
    split_formula = []
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start=i
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    digit_location=-1
    for i in range(len(formula)):
        if fomula[i].isdigit():
            digit-location=i
            break
    if digit_location==-1:
        return formula,1
    pref=formula[:digit_location]
    p=digit_location
    while p<len(formula) and fomula[p].isdigit():
        p+=1
    num = int(formula[digit_location:p])
    return pref,num


