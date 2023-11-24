import pickle
import streamlit as st

model = pickle.load(open("estimasi_mobil_bmw.sav", "rb"))

st.title("prediksi harga mobil bekas by arya madiun")

year = st.number_input("Input tahun mobil")
mileage = st.number_input("Input km mobil")
tax = st.number_input("input pajak mobil")
mpg = st.number_input("input konsumsi BBM mobil")
engineSize = st.number_input("Input engine size")

predict = ""

if st.button("Prediksi Harga"):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write("estimasi harga mobil bekas dalam EURO : ", predict)
    st.write("estimasi harga mobil bekas dalam RUPIAH : ", predict * 19000)
