def occurrence_sort(text):
    text_as_list = convert_to_list(text)

    for i in range(0, len(text)):
        for j in range(0, len(text)):
            if text.count(text_as_list[i]) < text.count(text_as_list[j]):
                temp = text_as_list[i]
                text_as_list[i] = text_as_list[j]
                text_as_list[j] = temp

    return text_as_list


def convert_to_list(text):
    text_as_list = []
    x = len(text)
    for i in range(0, x):
        text_as_list.append(text[i])
    return text_as_list
