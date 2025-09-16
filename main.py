# save as app.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten, Dense
from sklearn.metrics.pairwise import cosine_similarity
import io

app = FastAPI()

# Load embeddings
store_embeddings = np.load("store_embeddings.npy")
store_image_paths = np.load("store_image_paths.npy", allow_pickle=True)

# Load embedding model
conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(150,150,3))
embedding_model = Sequential([conv_base, Flatten(), Dense(256, activation='relu')])

@app.get("/")
async def root():
    return {"message": "Welcome to the Image Recommendation API"}

@app.post("/recommend")
async def recommend(file: UploadFile = File(...)):
    contents = await file.read()
    img = image.load_img(io.BytesIO(contents), target_size=(150,150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    query_emb = embedding_model.predict(img_array)
    sims = cosine_similarity(query_emb, store_embeddings)[0]
    top5_idx = sims.argsort()[-5:][::-1]
    top5_paths = [store_image_paths[i] for i in top5_idx]
    top5_scores = sims[top5_idx].tolist()

    return JSONResponse(content={"top5_paths": top5_paths, "scores": top5_scores})
