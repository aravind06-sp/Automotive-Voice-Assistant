from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Training examples
sentences = [
    "what is speed",
    "tell me speed",
    "current speed",
    "fuel level",
    "check fuel",
    "how much fuel",
    "engine temperature",
    "check temperature",
    "engine heat",
    "navigate home",
    "go to college",
    "start navigation",
    "why engine overheating",
    "battery problem",
    "brake noise","run diagnostics",
"check car problem",
"vehicle fault",
"scan vehicle"

]

labels = [
    "speed",
    "speed",
    "speed",
    "fuel",
    "fuel",
    "fuel",
    "temp",
    "temp",
    "temp",
    "navigate",
    "navigate",
    "navigate",
    "question",
    "question",
    "question",
    "diagnostic",
"diagnostic",
"diagnostic",
"diagnostic"

]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X, labels)

def predict_intent(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
