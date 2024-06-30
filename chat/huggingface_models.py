

from transformers import pipeline

class HuggingFaceModel:
    def __init__(self):
        self.models = {
            'gpt2': 'gpt2',
            'distilgpt2': 'distilgpt2'
        }
    
    def generate_response(self, user_input, model_name, max_length=100):
        model = self.models.get(model_name, 'gpt2')
        generator = pipeline("text-generation", model=model)
        responses = generator(user_input, max_length=max_length, num_return_sequences=5, truncation=True)
        return responses[0]['generated_text']
