from llama_cpp import Llama

# This is your actual model path
model_path = "/Users/kassum/.cache/gpt4all/mistral-7b-instruct-v0.1.Q4_0.gguf"
model = Llama(model_path=model_path, n_ctx=2048)

def get_ai_response(prompt):
    try:
        output = model(prompt, max_tokens=256, stop=["\nUser:", "\nAI:"])
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Oops! Something went wrong: {e}"
