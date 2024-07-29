from respond import *


def getQuestion(question):
    prompt = []
    pre_prompt = []
    question = strip_chars(question, ',.!?()<>:;"[]{}-_=+@#$%¨&*')
    question = question.split(' ')
    print(question)
    for word in question:
        value = return_value.get(word)
        if value is None:
            pre_prompt.append(value)
        else:
            prompt.append(value)
    for i in pre_prompt:
        prompt.append(i)
    return formulateAwnser(prompt, question)