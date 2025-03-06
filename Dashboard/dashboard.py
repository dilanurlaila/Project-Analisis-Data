import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import run_clustering  
import os

# Debugging: Menampilkan path saat ini di terminal/log
print("Current working directory:", os.getcwd())  # Direktori kerja saat ini
print("File absolute path:", os.path.abspath(__file__))  # Path absolut dari script

# Menentukan path absolut ke folder script berjalan
hour_file_path = os.path.join("data", "hourly_rentals.csv")
day_file_path = os.path.join("data", "daily_rentals.csv")


# Judul Dashboard
st.title("📊 Dashboard Analisis Bike Sharing")

# Sidebar untuk memilih dataset
st.sidebar.header("Pilih Dataset")
dataset_option = st.sidebar.selectbox("Dataset", ["Hourly Rentals", "Daily Rentals"])

# Load dataset berdasarkan pilihan
if dataset_option == "Hourly Rentals":
    df = pd.read_csv(hour_file_path)
else:
    df = pd.read_csv(day_file_path)

# Tampilkan data
st.write("### Preview Dataset")
st.dataframe(df.head())

# Pilihan Analisis
st.sidebar.header("Pilih Analisis")
analysis_option = st.sidebar.selectbox("Analisis", ["Visualisasi Data", "Clustering"])

if analysis_option == "Visualisasi Data":
    st.write("## Tren Penyewaan Sepeda")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=df.index, y=df['cnt'], ax=ax)
    ax.set_title("Tren Penyewaan Sepeda")
    ax.set_xlabel("Waktu")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

    # Diagram 2: Penyewaan Berdasarkan Cuaca
    st.write("### 🔆 Penyewaan Berdasarkan Cuaca")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=df['weathersit'], y=df['cnt'], ax=ax1, palette="coolwarm")
    ax1.set_xlabel("Kondisi Cuaca")
    ax1.set_ylabel("Jumlah Peminjaman")
    ax1.set_title("Jumlah Peminjaman Berdasarkan Cuaca")
    st.pyplot(fig1)

    # Diagram 3: Penyewaan Berdasarkan Jam (untuk Hourly Rentals)
    if dataset_option == "Hourly Rentals":
        st.write("### ⏰ Penyewaan Sepeda Berdasarkan Jam")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.lineplot(x=df['hr'], y=df['cnt'], ax=ax2, marker='o', color="red")
        ax2.set_xlabel("Jam")
        ax2.set_ylabel("Jumlah Peminjaman")
        ax2.set_title("Jumlah Peminjaman Sepanjang Hari")
        st.pyplot(fig2)

elif analysis_option == "Clustering":
    st.write("## Hasil Clustering")
    cluster_fig = run_clustering()
    st.pyplot(cluster_fig)

st.write("🚀 Dibuat dengan Streamlit oleh Dila Nurlaila")