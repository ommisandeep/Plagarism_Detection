import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📚 CopyCatcher ")
st.write("Upload student assignments and check for plagiarism.")

# Teacher sets plagiarism threshold
threshold = st.slider("Set Similarity Threshold", 0.0, 1.0, 0.7)

# File Upload
uploaded_files = st.file_uploader("Upload Assignments (TXT Only)", accept_multiple_files=True, type=["txt"])

if uploaded_files:
    st.success(f"{len(uploaded_files)} assignments uploaded!")

    # Read files
    texts = [file.read().decode("utf-8") for file in uploaded_files]
    student_names = [file.name for file in uploaded_files]

    # TF-IDF embedding
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Cosine Similarity Calculation
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Detect Plagiarism
    results = []
    for i in range(len(student_names)):
        for j in range(i + 1, len(student_names)):
            similarity_score = similarity_matrix[i][j]
            if similarity_score >= threshold:
                results.append((student_names[i], student_names[j], round(similarity_score, 2)))

    # Display results
    if results:
        st.warning("⚠️ Plagiarism Detected!")
        df = pd.DataFrame(results, columns=["Student 1", "Student 2", "Similarity Score"])
        st.dataframe(df)
    else:
        st.success("✅ No plagiarism detected!")
