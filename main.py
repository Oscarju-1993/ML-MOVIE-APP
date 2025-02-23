import os
import pandas as pd
import joblib
from fastapi import FastAPI
from sklearn.metrics.pairwise import cosine_similarity

#  Definir la ruta base del proyecto dinámicamente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "data_set")

# Construir rutas de los archivos
dataset_path = os.path.join(DATASET_DIR, "movies_dataset_processed.parquet")
vectorizer_path = os.path.join(DATASET_DIR, "vectorizer.pkl")
matriz_reducida_path = os.path.join(DATASET_DIR, "matriz_reducida.pkl")

#  Verificar que los archivos existen antes de cargarlos
for file in [dataset_path, vectorizer_path, matriz_reducida_path]:
    if not os.path.exists(file):
        raise FileNotFoundError(f"El archivo {file} no existe. Verifica su ubicación.")

# Cargar modelos y datos
movies_df = pd.read_parquet(dataset_path)
vectorizer = joblib.load(vectorizer_path)
matriz_reducida = joblib.load(matriz_reducida_path)

#  Inicializar FastAPI
app = FastAPI()

#  Endpoint de prueba
@app.get("/")
def home():
    return {"message": "API de Recomendación de Películas en funcionamiento 🚀"}

# Endpoint: Recomendación de películas
@app.get("/recomendacion/{titulo}")
def recomendar_peliculas(titulo: str, num_recomendaciones: int = 5):
    titulo = titulo.lower()
    idx = movies_df.index[movies_df['title'].str.lower() == titulo].tolist()
    if not idx:
        return {"error": "Película no encontrada"}
    
    idx = idx[0]
    sim_scores = cosine_similarity(matriz_reducida[idx].reshape(1, -1), matriz_reducida)
    sim_scores = sorted(list(enumerate(sim_scores[0])), key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:num_recomendaciones+1]]

    recomendaciones = movies_df[['title', 'popularity']].iloc[movie_indices].to_dict(orient='records')
    return {"titulo": titulo, "recomendaciones": recomendaciones}

#  Endpoint: Cantidad de filmaciones por mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    cantidad = movies_df[movies_df['release_date'].dt.month_name(locale='es') == mes].shape[0]
    return {"mes": mes, "cantidad": cantidad}

# Endpoint: Cantidad de filmaciones por día
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    cantidad = movies_df[movies_df['release_date'].dt.day_name(locale='es') == dia].shape[0]
    return {"dia": dia, "cantidad": cantidad}

# Endpoint: Score de una película
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    movie = movies_df[movies_df['title'].str.lower() == titulo.lower()]
    if movie.empty:
        return {"error": "Película no encontrada"}
    return {"titulo": titulo, "año": int(movie['release_year'].values[0]), "score": float(movie['popularity'].values[0])}

# Endpoint: Votos de una película
@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    movie = movies_df[movies_df['title'].str.lower() == titulo.lower()]
    if movie.empty or movie['vote_count'].values[0] < 2000:
        return {"error": "Película no encontrada o con menos de 2000 votos"}
    return {"titulo": titulo, "votos_totales": int(movie['vote_count'].values[0]), "promedio_votos": float(movie['vote_average'].values[0])}

# Endpoint: Información sobre un actor
@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    peliculas_actor = movies_df[movies_df['actors'].str.contains(nombre_actor, case=False, na=False)]
    if peliculas_actor.empty:
        return {"error": "Actor no encontrado"}
    retorno_total = peliculas_actor['revenue'].sum()
    promedio_retorno = retorno_total / peliculas_actor.shape[0]
    return {"actor": nombre_actor, "cantidad_peliculas": peliculas_actor.shape[0], "retorno_total": retorno_total, "promedio_retorno": promedio_retorno}

#  Endpoint: Información sobre un director
@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    peliculas_director = movies_df[movies_df['director'].str.contains(nombre_director, case=False, na=False)]
    if peliculas_director.empty:
        return {"error": "Director no encontrado"}
    detalles = peliculas_director[['title', 'release_date', 'revenue', 'budget']].to_dict(orient='records')
    retorno_total = peliculas_director['revenue'].sum()
    return {"director": nombre_director, "retorno_total": retorno_total, "peliculas": detalles}

#  Para correr en local:
# uvicorn main:app --host 0.0.0.0 --port 10000