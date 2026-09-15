import ollama
question = input('What do you want to ask bleb? (Type quit to stop)')
def get_response(question):
    response = ollama.chat(
        model='llama3.2',
        messages = [{
            'role': 'user',
            'content': question
        }]
        )
    return('\n' + 'bleb: ' + response['message']['content'] + '\n')






