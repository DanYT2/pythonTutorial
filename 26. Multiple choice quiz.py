qn_prompts = [
    'What colour are apples?\n (a) Red/Green\n (b) Purple\n (c) Orange\n\n',
    'What colour are bananas?\n (a) Teal\n (b) Magenta\n (c) Yellow\n\n',
    'What colour are strawberries?\n (a) Yellow\n (b) Red\n (c) Blue\n\n'
]


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


qns = [
    Question(qn_prompts[0], 'a'),
    Question(qn_prompts[1], 'c'),
    Question(qn_prompts[2], 'b')
]


def run_test(questions):
    score = 0
    for qn in questions:
        answer = input(qn.prompt)
        if answer == qn.answer:
            score += 1
    print(f'You got {str(score)} out of {str(len(questions))} correct')


run_test(qns)
