from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey", "greetings", "howdy"]):
        return "Hi there! How can I assist you today?"

    elif "weather" in user_input:
        return "I can't check the weather, but you can use a weather app or website for the latest updates."

    elif "joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems.",
            "Why don't programmers like nature? It has too many bugs.",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        return random.choice(jokes)

    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you", "take care", "farewell"]):
        return "See you later! Have a wonderful day."

    elif any(compliment in user_input for compliment in ["you're great", "good job", "awesome", "fantastic", "you rock"]):
        return "Thank you! I'm here to help you."

    elif "name" in user_input:
        return "I'm a friendly chatbot created to assist you with various questions. How can I help today?"

    elif "fact" in user_input or "did you know" in user_input:
        facts = [
            "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
            "Octopuses have three hearts and blue blood.",
            "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
            "Bananas are berries, but strawberries aren't.",
            "A group of flamingos is called a 'flamboyance'.",
            "You can't hum while holding your nose. Try it!"
        ]
        return random.choice(facts)

    elif any(assistance in user_input for assistance in ["help", "assist", "support", "guide", "advice"]):
        return "Sure! What do you need help with? Feel free to ask anything."

    elif any(small_talk in user_input for small_talk in ["how are you", "what's up", "how's it going", "what's new"]):
        return "I'm just a chatbot, but I'm here and ready to assist you. How can I help today?"

    elif "hobby" in user_input or "interests" in user_input:
        return "I don't have hobbies, but I can help you find information about various hobbies. What are you interested in?"

    elif "recommend" in user_input or "suggest" in user_input:
        suggestions = [
            "You might enjoy reading a book or watching a movie. Do you have a genre in mind?",
            "How about trying a new recipe or cooking something you love?",
            "You could go for a walk or explore a new hobby. What sounds good to you?"
        ]
        return random.choice(suggestions)

    elif "motivate" in user_input or "inspire" in user_input:
        quotes = [
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
            "Believe you can and you're halfway there. – Theodore Roosevelt",
            "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs"
        ]
        return random.choice(quotes)

    elif "book" in user_input or "movie" in user_input:
        recommendations = [
            "For a good book, try 'To Kill a Mockingbird' by Harper Lee or '1984' by George Orwell.",
            "If you’re into movies, 'The Shawshank Redemption' or 'Inception' might be interesting."
        ]
        return random.choice(recommendations)

    elif "what is your name" in user_input or "what can you do" in user_input or "how can you help me today" in user_input:
        return "I'm here to assist you with information, answer questions, and provide support. How can I help you?"

    elif "how do I get to" in user_input or "can you help me with" in user_input or "where can I find" in user_input:
        return "I can guide you through various tasks. Please specify what you need help with, and I'll do my best to assist."

    elif "update my profile information" in user_input or "remember my preferences" in user_input or "set up notifications" in user_input:
        return "I don't have the capability to update your profile or remember preferences, but I can help with general information."

    elif "trouble logging in" in user_input or "reset my password" in user_input or "website not loading" in user_input:
        return "For technical issues, please contact support or visit the help section of our website for assistance."

    elif "latest news" in user_input or "weather today" in user_input or "book a ticket" in user_input:
        return "I can't perform these tasks directly, but I can guide you on how to do them. Please specify what you need help with."

    elif "provide feedback" in user_input or "rate your service" in user_input or "report a problem" in user_input:
        return "Please visit our feedback page or contact customer support to provide feedback or report a problem."

    elif "create an account" in user_input or "reset my password" in user_input or "update my email address" in user_input:
        return "For account management tasks, please visit our account settings page or contact support for assistance."

    elif "products or services" in user_input or "details about" in user_input or "current promotions" in user_input:
        return "We offer a variety of products and services. For specific details or promotions, please visit our website or contact us directly."

    elif "trouble with" in user_input or "payment not going through" in user_input or "fix this error message" in user_input:
        return "For troubleshooting issues, please refer to our support center or contact customer service for help."

    elif "get to" in user_input or "guide me through" in user_input or "find" in user_input:
        return "I can help guide you through various processes. Please let me know what you need help with."

    elif "book an appointment" in user_input or "reschedule my booking" in user_input or "available times for" in user_input:
        return "For booking and appointments, please visit our booking page or contact our support team for assistance."

    elif "remember my preferences" in user_input or "set my preferences" in user_input or "recommend based on past choices" in user_input:
        return "I can't remember past preferences, but I can help you find information based on your current needs."

    else:
        return "Hmm, I don't understand that. Could you ask something else or try a different topic?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def respond():
    user_input = request.json.get("message")
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
