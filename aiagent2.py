import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create a sentiment analysis pipeline
sentiment_model = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Define your emoji dictionary with keywords
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😠",
    "skull": "💀",  # Roasting comments
    "party": "🎉",
    "cake": "🎂",
    "roast": "💀",
    "burn": "💀",
    "insult": "💀",
    "weight": "💀",
    "useless": "💀",
    "funny": "😂",
    "laugh": "😂",
    "cry": "😭",
    "excited": "🤩",
    "bored": "😐",
    "tired": "😴",
    "sick": "🤒",
    "confused": "😕",
    "surprised": "😲",
    "scared": "😱",
    "disgusted": "🤢",
    "cool": "😎",
    "wink": "😉",
    "thumbs_up": "👍",
    "thumbs_down": "👎",
    "clap": "👏",
    "fire": "🔥",
    "heart": "❤️",
    "broken_heart": "💔",
    "star": "⭐",
    "check": "✔️",
    "cross": "❌",
    "question": "❓",
    "exclamation": "❗",
    "sleeping": "😴",
    "thinking": "🤔",
    "celebrate": "🥳",
    "cheers": "🥂",
    "gift": "🎁",
    "money": "💰",
    "shopping": "🛍️",
    "food": "🍕",
    "drink": "🍹",
    "music": "🎶",
    "dance": "💃",
    "sports": "🏅",
    "travel": "✈️",
    "sun": "☀️",
    "moon": "🌙",
    "rain": "🌧️",
    "snow": "❄️",
    "cloud": "☁️",
    "lightning": "⚡",
    "earth": "🌍",
    "robot": "🤖",
    "alien": "👽",
    "ghost": "👻",
    "zombie": "🧟",
    "cat": "🐱",
    "dog": "🐶",
    "fish": "🐟",
    "bird": "🐦",
    "horse": "🐴",
    "monkey": "🐒",
    "bear": "🐻",
    "lion": "🦁",
    "tiger": "🐯",
    "elephant": "🐘",
    "panda": "🐼",
    "unicorn": "🦄",
    "dragon": "🐉",
    "dinosaur": "🦖",
    "ninja": "🥷",
    "pirate": "🏴‍☠️",
    "detective": "🕵️",
    "superhero": "🦸",
    "princess": "👸",
    "prince": "🤴",
    "king": "👑",
    "queen": "👸",
    "baby": "👶",
    "child": "👦",
    "adult": "👨",
    "old": "👴",
    "family": "👪",
    "friends": "👯",
    "team": "👥",
    "group": "👨‍👩‍👧‍👦",
    "couple": "👩‍❤️‍👨",
    "kiss": "💋",
    "hug": "🤗",
    "wave": "👋",
    "yes": "✅",
    "no": "❌",
    "maybe": "🤷",
    "sorry": "🙏",
    "thank_you": "🙏",
    "welcome": "👋",
    "good_luck": "🍀",
    "cheers": "🥂",
    "goodbye": "👋",
    "lit": "🔥",  # Gen Z slang
    "bet": "👌",  # Gen Z slang
    "cap": "🧢",  # Gen Z slang
    "no_cap": "✅",  # Gen Z slang
    "vibe": "🌈",  # Gen Z slang
    "savage": "😈",  # Gen Z slang
    "ghosting": "👻",  # Gen Z slang
    "simp": "💖",  # Gen Z slang
}

# Function to generate emojis based on text input
def generate_emojis(user_input):
    # Initialize an empty list to hold emojis
    emojis = []

    # Check for specific keywords in the user input
    for word in user_input.lower().split():
        if word in emoji_dict:
            emojis.append(emoji_dict[word])  # Add the corresponding emoji to the list

    # If no keywords match, analyze the sentiment of the user input
    if not emojis:
        sentiment = sentiment_model(user_input)[0]  # Call the sentiment model on user_input
        sentiment_label = sentiment['label']  # Get the sentiment label
        emojis.append(emoji_dict.get(sentiment_label.lower(), "🤔"))  # Default emoji for unknown sentiment

    return " ".join(emojis)  # Return the emojis as a string

# Streamlit UI
st.title("Emoji Generator AI Agent")
user_input = st.text_input("Type something:")

if st.button("Generate Emojis"):
    if user_input:
        response = generate_emojis(user_input)
        st.write("Generated Emoji:")
        st.write(response)
    else:
        st.warning("Please enter some text.")