📌 Proyecto de Recomendación de Películas con FastAPI

Este repositorio contiene un sistema de recomendación de películas basado en similitud de contenido, utilizando FastAPI para exponer la API, scikit-learn para procesamiento de texto y pandas para manejo de datos. También se implementa un ETL para transformar los datos de películas y optimizarlos para el modelo.

📂 Estructura del Proyecto

📦 ML-MOVIE-APP
 ┣ 📂 app_
 ┃ ┗ 📜 app.ipynb
 ┣ 📂 data_set
 ┃ ┣ 📂 processed
 ┃ ┃ ┣ 📜 credits.csv
 ┃ ┃ ┣ 📜 credits.parquet
 ┃ ┃ ┣ 📜 movies_dataset_etl.parquet
 ┃ ┃ ┣ 📜 movies_dataset_processed.parquet
 ┃ ┃ ┗ 📜 movies_final.parquet
 ┃ ┗ 📜 movies_dataset.csv
 ┣ 📂 env (Entorno virtual - NO subir a GitHub)
 ┣ 📂 notebooks
 ┃ ┗ 📜 eda.ipynb
 ┣ 📂 src
 ┃ ┣ 📜 etl_credits.ipynb
 ┃ ┣ 📜 etl_final.ipynb
 ┃ ┣ 📜 etl_movies.ipynb
 ┃ ┣ 📜 modelo.ipynb
 ┃ ┗ 📜 preprocess_movie.ipynb
 ┣ 📜 .gitattributes
 ┣ 📜 .gitignore
 ┣ 📜 main.py  (Código de la API en FastAPI)
 ┣ 📜 README.md  (Este archivo)
 ┣ 📜 requirements.txt  (Dependencias necesarias)

🚀 Instalación y Configuración

📌 1️⃣ Clonar el repositorio

git clone https://github.com/Oscarju-1993/ML-MOVIE-APP.git
cd ML-MOVIE-APP

📌 2️⃣ Crear y activar un entorno virtual

python -m venv env
# Activar en Windows
env\Scripts\activate
# Activar en macOS/Linux
source env/bin/activate

📌 3️⃣ Instalar dependencias

pip install -r requirements.txt

📌 4️⃣ Ejecutar el ETL para transformar los datos

python src/etl_final.ipynb

📌 5️⃣ Entrenar el modelo de recomendación

python src/modelo.ipynb

📌 6️⃣ Ejecutar la API con FastAPI

uvicorn main:app --reload

📡 Endpoints Disponibles en la API

📌 Recomendación de películas

GET /recomendacion/{titulo}

📌 Cantidad de filmaciones en un mes

GET /cantidad_filmaciones_mes/{mes}

📌 Score de una película

GET /score_titulo/{titulo}

📌 Votos de una película

GET /votos_titulo/{titulo}

📌 Información sobre un actor

GET /get_actor/{nombre_actor}

📌 Información sobre un director

GET /get_director/{nombre_director}

🔧 Tecnologías Utilizadas

Python 3.10+

FastAPI (para la API REST)

scikit-learn (para el modelo de recomendación)

pandas (para manipulación de datos)

nltk (para procesamiento de texto)

Joblib (para guardar el modelo)

Seaborn y Matplotlib (para análisis exploratorio de datos)

PyArrow (para manipulación eficiente de archivos Parquet)

📌 Autor

Oscarju-1993 - GitHub

📢 ¡Cualquier contribución o mejora es bienvenida! 🎬🚀