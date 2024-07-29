from info_aqquiring import *

response = []

return_value = {
    'bom': 1,
    'boa': 1.1,
    'noite': 1.2,
    'tarde': 1.4,
    'dia': 1.3,
    'nome': 2,
    'meu': 2.1,
    'seu': 2.2,
    'é': 2.3,
    'qual': 2.4,
    'oi': 3,
    'olá': 3,
    'eu': 4,
    'me': 4.1,
    'chamo': 4.2,
    'debug': 5,
}


def formulateAwnser(prompt, question):
    global info_count
    response.clear()
    print(f'prompt: {prompt}')
    print(f'question: {question}')
    formated_question = ' '.join(question)
    print(f'formated: {formated_question}')
    if 3 in prompt:  # Cumprimentos
        response.append('Olá!')
    if 2 and 2.2 in prompt:  # Seu nome
        response.append('Prazer, meu nome é Astrogildo!')
    if 1 and 1.3 in prompt:  # bom dia
        response.append('Bom dia para você também!')
    if 1.1 and 1.2 in prompt:  # boa noite
        response.append('Boa noite para você também!')
    if 1.1 and 1.4 in prompt:  # boa tarde
        response.append('Boa tarde para você também!')
    if 4 and 4.1 and 4.2 in prompt:  # eu me chamo
        if user_data.get('nome') is None:
            last = len(question) - 1
            user_data['nome'] = question[last]
            response.append(f'Entendido, {user_data.get('nome')}')
        else:
            response.append(f'Seu nome não era {user_data.get('nome')}?')
    if 2 and 2.1 in prompt:  # meu nome
        if 2.4 in prompt:  # qual é meu nome
            if user_data.get('nome') is None:
                response.append('Eu não sei. Você pode me contar!')
            else:
                response.append(f'Seu nome é {user_data.get('nome')}')
        elif 2.4 not in prompt:  # meu nome é
            if user_data.get('nome') is None:
                last = str(question[len(question) - 1])
                user_data['nome'] = capitalize(last)
                response.append(f'Entendido, {user_data.get('nome')}')
            else:
                response.append(f'Seu nome não era {user_data.get('nome')}?')
    if 2.3 in prompt and 2 not in prompt:  # é (não relacionado ao nome)
        if 2.4 in prompt:  # qual é x
            short_question = shorten(question)
            if user_data.get(short_question) is not None:
                response.append(user_data.get(' '.join(question)))
            else:
                user_data[info_count] = short_question
                response.append(f'Eu não sei! Qual é?')
        else:  # x é x
            if question[0] == 'é':
                response.append(learn(question, 0))
            else:
                response.append(learn(question, 1))
            info_count += 1
    if 5 in prompt:
        print(user_data)
    print(f'response: {response}')
    return ' '.join(response)