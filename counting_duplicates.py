def duplicate_count(text):
    count = [0] * 26
    result = 0
    for i in text:
        letter_index = ord(i.lower()) - 97
        if count[letter_index] >= 2:
            continue
        count[letter_index] += 1
        if count[letter_index] >= 2:
            result += 1
    return result

print(duplicate_count("strng"))
