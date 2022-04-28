target = 9
options = [3, 2, 1]
combos = []


def change(temp, num, i):
    # VERY IMPORTANT: Must duplicate list or temp will
    # remain the same regardless if the recursive call has ended.
    temp = temp.copy()

    num -= options[i]
    if num >= 0:
        temp[i] += 1

    # Base Cases (2)
    if num == 0:
        # Check for duplicates
        if temp not in combos:
            combos.append(temp)
        return
    if num < 0:
        return

    change(temp, num, 0)
    change(temp, num, 1)
    change(temp, num, 2)


change([0,0,0], target, 0)

print("------------------ Result ------------------")
print("Target  = " + str(target))
print("Options = ", end="")
print(options, end="\n\nCombos:\n")
for com in combos:
    print(com)


print("\n\n------------------ Proof ------------------")
print("Combination \tCoins\t\tTotal")
for com in combos:
    com_added = [x*y for x,y in zip(com, options)]
    com_sum = sum(com_added)
    print(com, end="  *  ")
    print(options, end="  =  ")
    print(com_added, end="  ->  ")
    print(com_sum)