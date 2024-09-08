from openai import OpenAI


class Chatbot:

    def __init__(self, system_prompt, model="gpt-4"):

        self.message_history = []
        self.client = OpenAI()
        self.model_name = model
        self.system_prompt = system_prompt
        self.temperature = 0.2
        self.message_history.append({"role": "system", "content": self.system_prompt})

    def query(self, content):
        self.message_history.append({"role": "user", "content": content})
        completion = self.client.chat.completions.create(
            model=self.model_name, messages=self.message_history
        )
        response = completion.choices[0].message.content
        self.message_history.append({"role": "assistant", "content": response})
        return response

    def clear_history(self):
        self.message_history = []
        self.message_history.append({"role": "system", "content": self.system_prompt})
        return "Chat history cleared."

    def clear_last_chat_and_response(self):
        """
        Remove the last human message + last AI message
        """
        self.message_history.pop()
        self.message_history.pop()
        return "Last message cleared."
