# save as frontend.py
import streamlit as st
import requests
from PIL import Image
import os

st.title("Clothes Recommendation System")

uploaded_file = st.file_uploader("Upload photo of cloth you desire to buy", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Photo", use_column_width=True)

    if st.button("Get Recommendations"):
        # Reset file pointer before reading
        uploaded_file.seek(0)
        # Read file bytes
        file_bytes = uploaded_file.read()
        files = {"file": (uploaded_file.name, file_bytes, uploaded_file.type)}
        with st.spinner("Finding similar clothes..."):
            response = requests.post("http://127.0.0.1:8000/recommend", files=files)

        if response.status_code == 200:
            data = response.json()
            st.subheader("Top-5 Similar Clothes")
            cols = st.columns(5)
            for idx, (path, score) in enumerate(zip(data["top5_paths"], data["scores"])):
                filename = os.path.basename(path)
                local_path = os.path.join("content", "images_compressed", filename)
                if not os.path.exists(local_path):
                    cols[idx].warning(f"Not found:\n{filename}")
                    continue
                try:
                    file_size = os.path.getsize(local_path)
                    if file_size == 0:
                        cols[idx].warning(f"Empty:\n{filename}")
                        continue
                    img = Image.open(local_path)
                    cols[idx].image(img, caption=f"{score:.2f}", use_column_width=True)
                except Exception as e:
                    cols[idx].warning(f"Error:\n{filename}")
        else:
            st.error("Error fetching recommendations")
