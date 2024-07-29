user_data = {}

info_count = 0


def learn(info, complete):
    if complete == 0:
        if user_data.get(info_count) is None:
            return f'O que {' '.join(info)}'
        elif user_data.get(user_data.get(info_count)) is None:
            subject = info
            del subject[0]
            user_data[user_data.get(info_count)] = ' '.join(subject)
            return 'Entendido!'
    elif complete == 1:
        subject = []
        reply = []
        is_subject = True
        for x in info:
            if x == 'é':
                info.remove(x)
                is_subject = False
            elif is_subject is True:
                subject.append(x)
            else:
                reply.append(x)
        user_data[' '.join(subject)] = 'Resposta'  # ' '.join(reply)
        return 'Entendido!'


def capitalize(string):
    name_letters = list(string)
    first_letter = name_letters[0].upper()
    name_letters[0] = first_letter
    return ''.join(name_letters)


def shorten(sentence):
    del sentence[0]
    del sentence[0]
    print(' '.join(sentence))
    return str(' '.join(sentence))


def strip_chars(string, char):
    striped = "".join(c for c in string if c not in char)
    print(striped)
    return striped