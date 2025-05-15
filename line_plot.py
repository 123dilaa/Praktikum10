import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# nama Anggota
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #d13661;
        font-size: 36px;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        margin-bottom: 30px;
    }

    .box {
        background-color: #ffe0f0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(214, 51, 132, 0.2);
        width: 70%;
        margin: 0 auto;
    }

    .anggota {
        font-size: 20px;
        font-weight: 500;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul
st.markdown('<div class="title"> Daftar Nama Anggota Kelompok</div>', unsafe_allow_html=True)

# Daftar nama dalam box
st.markdown(
    """
    <div class="box">
        <div class="anggota">1. Wulan Ramadani</div>
        <div class="anggota">2. Siti Fadila Siregar</div>
        <div class="anggota">3. Zahra Pahrani</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Sampel data
months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 30, 45, 50, 60, 55, 65, 70,   77, 90]
product_B_sales = [15, 20, 25, 30, 35, 8, 12, 18, 22, 25, 20,12]

# Streamlit layout
st.title('Visuali Penjualan Produk')
st.sidebar.header('Pengaturan Grafik')
option = st.sidebar.selectbox(
    "Pilih Tipe Visualisasi",
    ("Line Plot", "Kustomisasi Line Plot", "Garis Berbeda untuk Menunjukkan Trend", "Subplot")
)

# Fungsi Line Plot standar
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig)

# Fungsi Line Plot dengan kustomisasi
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle='-.', marker='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Fungsi untuk menampilkan garis tren
def trend_lines_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A Trend', linestyle='--', color='blue')
    ax.plot(months, product_B_sales, label='Product B Trend', linestyle='-.', color='red')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Fungsi untuk menampilkan dua subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot untuk Product A
    axs[0].plot(months, product_A_sales, label='Product A', color='blue', marker='o')
    axs[0].set_title('Penjualan Produk A Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot untuk Product B
    axs[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
    axs[1].set_title('Penjualan Produk B Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

# Menjalankan visualisasi berdasarkan pilihan pengguna
if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()
