import streamlit as st
from PIL import Image
st.title("Portafolio - Valery Ochoa")


url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("A continuación se muestran las applicaciones creadas como evidencia de asistencia a la clase de Computación Avanzada 8-10p.m.")
st.write(f"Enlace para aplicaciones y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("¿Qué fruta es más parecida?")
 image = Image.open('imagenes/img1.jpg')
 st.image(image, width=190)
 st.write("A partir del peso, diámetro y nivel de dulzor ingresados, el programa calcula la similitud con una lista de frutas conocidas (manzana, banano, naranja o pera) y muestra la coincidencia más cercana.") 
 url = "https://frutasapp-5jeu4vlbumawf452mfbzwk.streamlit.app/"
 st.write(f"App: [Enlace]({url})")

 st.subheader("Descenso de Gradiente Interactivo")
 image = Image.open('imagenes/img2.jpg')
 st.image(image, width=200)
 st.write("Aplicación en Streamlit para visualizar en tiempo real y en 3D cómo el descenso de gradiente encuentra el mínimo de una función. Permite ajustar parámetros como la tasa de aprendizaje e incluye un ejemplo práctico de regresión lineal.") 
 url = "https://appgradient-wpjq4eb77wgxzj49h8h2ey.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


