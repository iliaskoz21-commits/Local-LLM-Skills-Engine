import ollama
import os
from dotenv import load_dotenv # <--- Προσθήκη

# Φόρτωση των ρυθμίσεων από το αρχείο .env
load_dotenv()

# Χρήση των ρυθμίσεων με εναλλακτικές (defaults) αν λείπει το αρχείο
MODEL_NAME = os.getenv("MODEL_NAME", "mistral:latest")
SKILLS_DIR = os.getenv("SKILLS_DIR", "skills")

def list_skills():
    # Φέρνει όλα τα .md αρχεία από το φάκελο skills
    if not os.path.exists("skills"):
        return []
    return [f for f in os.listdir("skills") if f.endswith(".md")]

def load_skill(skill_name):
    with open(f"skills/{skill_name}", "r", encoding="utf-8") as f:
        return f.read()

def main():
    print("═"*40)
    print("      CHOOSE YOUR MENTOR")
    print("═"*40)
    
    available_skills = list_skills()
    if not available_skills:
        print("No skills found in /skills folder!")
        return

    for i, skill in enumerate(available_skills):
        print(f"{i+1}. {skill.replace('.md', '')}")
    
    choice = int(input("\nSelect Skill (number): ")) - 1
    selected_skill_file = available_skills[choice]
    system_prompt = load_skill(selected_skill_file)
    
    print(f"\n✅ Loaded: {selected_skill_file}")
    
    messages = [{'role': 'system', 'content': system_prompt}]
    
    while True:
        user_input = input("\nΕσύ: ")
        if user_input.lower() in ['exit', 'quit']: break
        
        messages.append({'role': 'user', 'content': user_input})
        
        print("\nMistral: ", end="", flush=True)
        response = ollama.chat(model='mistral:latest', messages=messages, stream=True)
        
        full_response = ""
        for chunk in response:
            content = chunk['message']['content']
            print(content, end="", flush=True)
            full_response += content
        
        messages.append({'role': 'assistant', 'content': full_response})
        print("\n" + "-"*30)

if __name__ == "__main__":
    main()