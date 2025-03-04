import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"what is artificial intelligence?",
        ["Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and learn.",]
    ],
    [
        r"how does machine learning work?",
        ["Machine learning works by using algorithms to analyze data, learn from it, and make predictions or decisions based on that data.",]
    ],
    [
        r"what are neural networks?",
        ["Neural networks are a set of algorithms modeled after the human brain that are designed to recognize patterns.",]
    ],
    [
        r"what is deep learning?",
        ["Deep learning is a subset of machine learning that uses neural networks with many layers to analyze various factors of data.",]
    ],
    [
        r"quit",
        ["Thank you for chatting with me about artificial intelligence. Have a great day!"]
    ],

]

# Create a chatbot instance
def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
