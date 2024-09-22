from random import choice, randint

greeting = ['hi', 'hello', 'hey']
bye =['bye', 'see ya', 'later', 'leaving now']
roll_dice = ['roll dice', 'roll a dice']

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif any(keyword in lowered for keyword in greeting ):
        return 'Hello there!'
    elif any(keyword in lowered for keyword in bye):
        return 'See ya!'
    elif any(keyword in lowered for keyword in roll_dice):
        return f'You rolled : {randint(1,6)}'
    else:
        return choice(['I do not understand...', 'What are you talking about?', 'Do you mind rephrasing that?'])
