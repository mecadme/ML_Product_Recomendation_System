import streamlit as st
import translators as ts
import nltk   
import pickle

def sentiment():

    nltk.download('stopwords')
    nltk.download('rslp')
    nltk.download('punkt')
    nltk.download('wordnet')

    filename='datasets/model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    with open('datasets/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    def Preprocessing(text):
        stemmer = nltk.stem.RSLPStemmer()
        text = text.lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
        stopwords = set(nltk.corpus.stopwords.words('portuguese'))
        stopwords.remove('não')
        stopwords.remove('nem')
        words = [stemmer.stem(i) for i in text.split() if not i in stopwords]
        return (" ".join(words))

    def translation(text):
        translated=ts.translate_text(text,'google', to_language= 'pt')
        return translated

    def new_prediction(text):
        vectorized_text = vectorizer.transform([text])
        pred = loaded_model.predict(vectorized_text)
        return pred    

    st.title("Sentiment Analysis!")

    # Create a text box and store the entered text in a variable
    text = st.text_input("Enter the comment that you want to analyze 👇")
    # Display the entered text
    if text:
        # Display the analysis
        if(new_prediction(Preprocessing(translation(text)))[0] == "positive"):
            st.subheader("Your comment is: :green[Positive]")
        else:
            st.subheader("Your comment is: :red[Negative]")