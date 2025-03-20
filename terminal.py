import google.generativeai as genai #error
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Main chat loop
while True:

    # get user input from terminal
    user_input = input("\nEnter your question (or 'quit' to exit): ")
    
    #check if user wants to quit
    if user_input.lower() == 'quit':
        print("Thanks for chatting! Goodbye!")
        break
    # Generate response using user's input   
    response = model.generate_content(user_input)

    print("\nResponse:",response.text)