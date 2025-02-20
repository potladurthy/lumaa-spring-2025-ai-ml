# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation


# Movie Recommendation System  

## 📌 Overview  

This project is a concised implementation of a **content-based recommendation system** to suggest movies according to user preferences given a query input from the user. The recommedation system designed is based on the open-source vector database `chromadb`. Although the implementation is non trvial, it is functional and can be used as a starting point for more complex recommendation systems. Precisely, the implementation is based on the following steps:
1) The dataset of movies (containing summaries or movie plots) is extracted and converted into an embedding vector to store in our vector database. To make this process more controallable, we can specify the number of data points (subset of the entire movies dataset) to be stored in the database.
2) To make the retrieval process more robust additonal filtering is applied to the database using metadata like genre. For each movie, the genre of the movie is passed as metadata to the vector database.
3) The user query is first converted into an embedding vector, then the query is procesed for any specific genres which is attached as the metadata for the query embedding to retrieve similar embeddings from the database.
4) The retrieved embeddings are then decoded and the corresponding movie titles along with scores and returned.

## Dataset  
The Dataset [Wikipedia-movie-plots]('https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots') is used for the purpose of demonstration. 
The csv file needs to be downloaded inot the local folder where the script runs or atleast have the path where the csv files exists. Manual download is the quickest and easiest option to get the dataset.


# Instructions to reproduce the results

### **Install Dependencies**  
Since this project is implemented in a **Jupyter Notebook (`.ipynb`)**, install the required libraries directly using the following command in a new cell:  
```
! pip install chromadb
! pip install sentence_transformers 
! pip install --upgrade huggingface_hub==0.26.0
! pip install numpy , pandas
! pip install nltk
! pip install textdistance
```
**Note**: huggingface_hub may require python versions of <=3.11. Make sure to install the correct version of python.

### **Create the Database**  
- **RecommendMovies** class is implemented that serve as an abstraction providing control over the database creation and retrieval process.
- **Usage:** ```recommender = RecommendMovies(movies_df_path='wiki_movie_plots_deduped.csv',num_rows=1000)```
- The class takes in the path to the csv file and the number of rows to be stored in the database.
    - **movies_df_path:** Path to the csv file containing the movie dataset.
    - **num_rows:** Number of rows to be stored in the database. (In the avove example 1000 rows from the csv are randomly sampled are stored in the database).

**Note**: Please be patient until the database is created. For 1000 rows it should approximately take aroud 1-2 min. Since the database creation involves converting each movie summary into an embedding vector, calculating metadata and storing it in the database, it is expected to take some time.

### **Query the Database**
- **recommend_movies** method is implemented to query the database and retrieve the most similar movies to the user query. 
- **Usage:** ```recommender.recommend_movies(query='I love thrilling action movies set in space, with a comedic twist', num_movies=20)```
- The method takes in the user query and the number of movies to be retrieved from the database.
    - **query:** User query to be used for retrieving the most similar movies from the database.
    - **num_movies:** Number of movies to be retrieved from the database. (In the above example 20 movies are retrieved from the database). This parameter is used to control the number of movies to be retrieved from the database.

### **Output**
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Genre</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>922</th>
      <td>Morons from Outer Space</td>
      <td>comedy|science_fiction</td>
      <td>1.255919</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Love Camp 7</td>
      <td>thriller</td>
      <td>1.309459</td>
    </tr>
    <tr>
      <th>1209</th>
      <td>Pixels</td>
      <td>animation|comedy</td>
      <td>1.339994</td>
    </tr>
    <tr>
      <th>1362</th>
      <td>Little Big Shot</td>
      <td>comedy</td>
      <td>1.363855</td>
    </tr>
    <tr>
      <th>632</th>
      <td>Sex &amp; Fury</td>
      <td>action</td>
      <td>1.373893</td>
    </tr>
    <tr>
      <th>1345</th>
      <td>Valentine's Day</td>
      <td>comedy|romance</td>
      <td>1.378675</td>
    </tr>
    <tr>
      <th>1702</th>
      <td>Meet the Spartans</td>
      <td>comedy</td>
      <td>1.382560</td>
    </tr>
    <tr>
      <th>1391</th>
      <td>An Alan Smithee Film: Burn Hollywood Burn</td>
      <td>comedy</td>
      <td>1.383018</td>
    </tr>
    <tr>
      <th>1170</th>
      <td>A Dandy in Aspic</td>
      <td>spy|thriller</td>
      <td>1.393913</td>
    </tr>
    <tr>
      <th>1360</th>
      <td>Hellzapoppin'</td>
      <td>comedy|musical</td>
      <td>1.405572</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Hotel California</td>
      <td>action|comedy</td>
      <td>1.417168</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Gaily, Gaily</td>
      <td>comedy</td>
      <td>1.425991</td>
    </tr>
    <tr>
      <th>880</th>
      <td>Way...Way Out</td>
      <td>comedy</td>
      <td>1.447291</td>
    </tr>
    <tr>
      <th>294</th>
      <td>Rings</td>
      <td>horror|thriller</td>
      <td>1.447655</td>
    </tr>
    <tr>
      <th>1922</th>
      <td>Lost in a Harem</td>
      <td>comedy</td>
      <td>1.451891</td>
    </tr>
    <tr>
      <th>426</th>
      <td>The Terror of Tiny Town</td>
      <td>comedy|western</td>
      <td>1.454976</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Angst</td>
      <td>comedy</td>
      <td>1.457326</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Hotel Chelsea</td>
      <td>thriller</td>
      <td>1.463649</td>
    </tr>
    <tr>
      <th>600</th>
      <td>Shadows and Fog</td>
      <td>comedy</td>
      <td>1.464689</td>
    </tr>
    <tr>
      <th>831</th>
      <td>Chhalia</td>
      <td>action</td>
      <td>1.468545</td>
    </tr>
  </tbody>
</table>
</div>

## **Video Demonstration**
[Video](https://drive.google.com/file/d/1C7fRpwvTrHanYUf4Iys9IE1q_L5F70uH/view?usp=sharing )


