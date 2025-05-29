import streamlit as st
from PIL import Image
import os
import deepl
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPL")

def translate_text(text, target_lang="EN-US"):
    auth_key = api_key  
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=target_lang)
    return result.text

st.title("VQA-DATASET GENERATOR")


os.makedirs("images", exist_ok=True)

file_uploaded = st.file_uploader("Upload multiple images", accept_multiple_files=True)
data = []

if file_uploaded:
    for idx, dx in enumerate(file_uploaded):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(Image.open(dx), caption=f"Gambar {idx + 1}", use_column_width=True)
        
        with col2:
            question = st.text_input("Pertanyaan:", key=f"q_{idx}")
            answer = st.text_input("Jawaban:", key=f"a_{idx}")
            
            if question != "" and answer != "":
                
                image_obj = Image.open(dx)
                image_filename = f"images/image_{idx}.png"
                image_obj.save(image_filename)

                data.append({
                    "image": image_filename,
                    "question": translate_text(question),
                    "answer": translate_text(answer)
                })

if st.button("Simpan ke CSV"):
    if data:
        df = pd.DataFrame(data)
        df.to_csv("data_vqa.csv", index=False)
        st.success("Data berhasil disimpan ke data_vqa.csv!")
    else:
        st.warning("Belum ada data yang bisa disimpan.")

