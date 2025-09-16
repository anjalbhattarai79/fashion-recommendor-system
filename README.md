# Fashion Image Similarity Recommender 👗👜👟

A content-based image retrieval system that recommends visually similar fashion items from a store dataset using deep learning (VGG16 feature extractor).

---

## 🚀 Demo

![A user uploads a photo of a dress to a web interface, which displays five visually similar clothing items from a store dataset below the uploaded image. The interface is clean and modern, with a friendly and inviting tone. On-screen text reads Upload a dress and see similar items.]
> Upload a dress → system shows top 5 similar items from the store.

---

## ✨ Features

- Upload a photo of clothing.
- Extract embeddings using VGG16.
- Compare with store dataset embeddings.
- Return top-5 most similar images.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- TensorFlow / Keras
- Streamlit (for frontend)
- FastAPI (for backend)

### Steps

```bash
# 1. Clone repo
git clone https://github.com/anjalbhattarai79/fashion-recommendor-system.git
cd fashion-recommendor-system

# 2. Create environment (optional but recommended)
python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run backend
uvicorn main:app --reload

# 5. Run frontend
streamlit run frontend.py
```

---

## 🧑‍💻 Usage

1. Put store images inside `content/images_compressed/`.
2. Run preprocessing script to generate embeddings:
    ```bash
    python generate_embeddings.py
    ```
3. Start backend and frontend as above.
4. Upload a new image via Streamlit → system shows similar products.

---

## 📁 Project Structure

```
fashion-recommender/
├── app.py                  # FastAPI backend
├── frontend.py             # Streamlit app
├── generate_embeddings.py  # Embedding generator
├── content/
│   └── images_compressed/  # Store dataset
├── store_embeddings.npy    # Saved embeddings
├── store_image_paths.npy   # Mapping for embeddings
├── requirements.txt
└── README.md
```

---

## 🔮 Future Work / Improvements

- Fine-tune the embedding extractor on DeepFashion dataset for fashion-specific features.
- Use CLIP embeddings (image + text) for better semantic similarity.
- Add a cloth vs non-cloth classifier to filter irrelevant inputs.
- Scale similarity search using FAISS / Annoy for 100k+ images.
- Support multi-modal search → e.g., “Show me red dresses similar to this one.”

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---
