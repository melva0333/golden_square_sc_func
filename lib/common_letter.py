import string

def get_most_common_letter(text):
    text = "".join(char for char in text if char in string.ascii_letters)
    counter = {}
    # print(counter)
    for char in text:
        counter[char] = counter.get(char, 0) + 1
        # print(counter[char])
    most_common_letter = max(counter, key= counter.get)
    # letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    # print(letter)
    # print(counter.items())
    print(sorted(counter.items(), key=lambda item: item[1],reverse=True))
    return most_common_letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
