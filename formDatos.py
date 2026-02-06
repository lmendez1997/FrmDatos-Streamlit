import streamlit as st

st.title("Formulario de Registro Estudiantil IP-2026")

nombre = st.text_input("Nombre Completo")
edad = st.number_input("Edad", min_value=0, max_value=80)
carrera = st.selectbox("Carrera", ["Ingeniería en Sistemas", "Medicina", "Derecho", "Arquitectura", "Administración de Empresas"])
comentario = st.text_area("Comentarios Adicionales(opcional)")

if st.button("Enviar"):
    st.write("Datos registrados:")
    st.write(f"**Nombre completo** : {nombre}")
    st.write(f"**Edad** : {edad}")
    st.write(f"**Carrera seleccionada** : {carrera}")
    st.write(f"**Comentarios** : {comentario}")
    st.success("Formulario enviado con éxito")