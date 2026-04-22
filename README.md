# 🎬 Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on user input. This project uses machine learning techniques to analyze movie data and recommend movies with similar features.

---

## 🚀 Live Demo

👉 https://movierecommender-k8dm4wxkfpbzkgtmnbunin.streamlit.app/


---

## 📌 About the Project

This project is a **Movie Recommender System** built using a content-based filtering approach.

The system recommends movies based on similarity between movies. When a user selects a movie, the system finds and displays movies that are most similar to it.

The similarity is calculated using features like:

* Movie genres
* Keywords
* Cast
* Crew

These features are combined and processed to create a similarity matrix, which helps in finding the closest matching movies.


## Tech Stack

This project is built using the following technologies:

* Python for backend logic and machine learning
* Pandas and NumPy for data processing
* Scikit-learn for vectorization and similarity calculation
* Pickle for saving trained models
* Streamlit for frontend and deployment
* TMDB dataset for movie data
* Used Api Integration for poster fetching 

---

## 🧠 How It Works

1. **Data Collection**
   Movie datasets are taken from TMDB which include details like title, genres, cast, crew, and keywords.

2. **Data Preprocessing**

   * Important features are selected
   * Data is cleaned and formatted
   * Features are combined into a single text format

3. **Feature Extraction**

   * Text data is converted into vectors using techniques like Count Vectorizer

4. **Similarity Calculation**

   * Cosine similarity is used to calculate similarity between movies

5. **Model Saving**

   * Processed data and similarity matrix are saved using pickle files

6. **Recommendation Logic**

   * When a user selects a movie, the system finds the most similar movies using the similarity matrix

7. **Frontend Integration**

   * User selects a movie
   * Recommendations are displayed dynamically

---

## 📂 Project Structure


movie-recommender/
│
├── data/
├── models/
├── app.py
├── movierecommender.ipynb
├── requirements.txt
├── .gitignore
└── README.md


## ⚠️ Note

Large dataset files and model files are not included in this repository due to size limitations.

You can use the original dataset from TMDB or any sample dataset to run the project.

---

## 🛠️ How to Run Locally

1. Clone the repository

git clone [https://github.com/your-username/movie-recommender.git](https://github.com/aarav11b16123-png/movierecommender.git)


2. Navigate to the project folder

cd movie-recommender

3. Install dependencies


pip install -r requirements.txt

4. Run the application

streamlit app.py


## 📈 Future Improvements

* Add collaborative filtering
* Improve UI using React
* Add user authentication
* Deploy on cloud (AWS / Render / Vercel)

<img width="1920" height="859" alt="Screenshot (1380)" src="https://github.com/user-attachments/assets/14fb17b5-6a37-422a-9ec9-36dcfe5491b7" />
  

## 👨‍💻 Author

Aarav Chaudhary

---

⭐ If you found this project useful, consider giving it a star!
