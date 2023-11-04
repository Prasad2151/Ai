from textblob import TextBlob

def detect_emotion(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Perform sentiment analysis
    sentiment = blob.sentiment.polarity

    # Determine the emotion based on sentiment
    if sentiment > 0.2:
        return "positive"
    elif sentiment < -0.2:
        return "negative"
    else:
        return "neutral"

while True:
    text = input("Enter a sentence or text: ")
    emotion = detect_emotion(text)
    print(f"The emotion of the text is: {emotion}")
