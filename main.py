from prompts import create_prompt
from utils import get_ai_response

def main():
    print("🤖 Welcome to your AI Health Companion.")
    print("Type how you're feeling or what symptoms you're experiencing.")
    print("Type 'exit' anytime to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("\nAI: Take care of yourself, and don’t hesitate to check in again. You’ve got this 💙")
            break

        prompt = create_prompt(user_input)
        response = get_ai_response(prompt)
        print(f"\nAI: {response}\n")

if __name__ == "__main__":
    main()

