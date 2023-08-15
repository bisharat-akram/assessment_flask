import openai

class ChatGPTBotAPI:
    
    def __init__(self, openai_api_key):
        """ Initialze CHATGPT API """
        openai.api_key = openai_api_key
        self.prompts = []

    def create_prompt(self, prompt):
        """ Create prompt """
        self.prompts.append(prompt)

    def get_response(self, prompt_index):
        """ Get response from a saved prompt by using index """
        response = openai.Completion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": self.prompts[prompt_index]}])
        return response
        # return self.prompts

    def update_prompt(self, prompt_index, new_prompt):
        """ Update prompt by using index """
        self.prompts[prompt_index] = new_prompt

    def delete_prompt(self, prompt_index):
        """ Delete prompt by using index """
        del self.prompts[prompt_index]