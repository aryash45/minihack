# AI-POWERED SENTIMENT EMOJI GENERATOR
# Sentiment Analysis Emoji Generator

## 📌 Overview
The **Sentiment Analysis Emoji Generator** is a simple AI-powered tool that analyzes user input text and generates an emoji that best represents the sentiment behind the text. This project was developed as part of a mini hackathon.

## 🚀 Features
- 🔍 **Sentiment Analysis**: Detects whether the text is positive, negative, or neutral.
- 😊 **Emoji Representation**: Maps sentiment scores to corresponding emojis.
- ⚡ **Real-time Processing**: Instantly processes user input and provides feedback.
- 🎨 **Minimalistic UI**: Simple and user-friendly interface.

## 🛠️ Technologies Used
- **Python** (for backend processing)
- **Streamlit** (for the frontend UI)
- **Hugging Face Transformers** (for sentiment analysis)
- **BERT-based Model (Bitulert)** (for text classification)

## 🏗️ Setup & Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/sentiment-emoji-generator.git
   cd sentiment-emoji-generator
   ```
2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```sh
   streamlit run app.py
   ```
5. **Access the app**:
   The Streamlit app will open automatically in your browser.

## 🎯 Usage
1. Enter a sentence in the input box.
2. Click the "Analyze" button.
3. The app will process the sentiment using the Bitulert model and display an appropriate emoji based on the result:
   - 😊 Positive
   - 😐 Neutral
   - 😠 Negative

## 🔍 How It Works
1. The user inputs a sentence in the text box.
2. The input text is sent to a **BERT-based model (Bitulert)** hosted on **Hugging Face** for sentiment classification.
3. The model analyzes the sentiment and classifies it as **positive, neutral, or negative**.
4. Based on the classification, an appropriate emoji is selected.
5. The sentiment label and corresponding emoji are displayed on the Streamlit UI in real time.

## 💡 Future Improvements
- Add support for more languages.
- Enhance sentiment analysis using more advanced deep learning models.
- Integrate with social media platforms for live sentiment tracking.

## 📜 License
This project is licensed under the MIT License.

## 👨‍💻 Author
Developed by **Aryash Gupta** during a mini hackathon.

---

Feel free to contribute or suggest improvements!

