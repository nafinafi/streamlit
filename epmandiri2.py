import streamlit as st
import pandas as pd
import altair as alt
import datetime
import numpy as np
import plotly.express as px

#Root
nomor_list_1 = [1]
nomor_list_2 = [1,2]
nomor_list_3 = [1,2,3]
nomor_list_4 = [1,2,3,4]
nomor_list_5 = [1,2,3,4,5]
nomor_list_6 = [1,2,3,4,5,6]
nomor_list_7 = [1,2,3,4,5,6,7]

#Date Picker
startDateCol, endDateCol = st.columns(2)
with startDateCol: 
    start_date = st.date_input('Start date', datetime.date(2021, 1, 1))
with endDateCol:    
    end_date = st.date_input('End date', datetime.date(2021, 12, 31))
if start_date < end_date:
    pass
else:
    st.error('Error: End date must fall after start date.')

#DF
#df = pd.read_csv('result/sebaraniqpivot.csv')
##################################################################################

#Slide2
st.header("Executive Presentation")
st.write("- Informasi data para peserta / testee selama proses pengambilan data antara Firstasia Consultants - Bank Mandiri (Agustus - September 2023) - Gambaran sebaran data dari segi kognitif, aspek kepribadian AKHLAK, kompetensi Mandirian,  GRIT, dan Learning Agility")

#Slide3
dfsimpulan = pd.DataFrame(
    [
       {"produk": "P3K", "lulus": 4, "tidak_lulus": True},
       {"produk": "Pelaksana", "lulus": 5, "tidak_lulus": False},
       {"produk": "Kriya", "lulus": 3, "tidak_lulus": True},
   ]
)
edited_df = st.data_editor(dfsimpulan, hide_index=True)

#Slide4
st.header("Sebaran IQ")
#st.bar_chart(df)

#Slide5
dfakhlakp3k = pd.DataFrame(
    [
        {"rank": 1, "kategori": "Kompeten", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 4.07},
        {"rank": 2, "kategori": "Adaptif", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.48},
        {"rank": 3, "kategori": "Amanah", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.45},
        {"rank": 4, "kategori": "Kolaboratif", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.44},
        {"rank": 5, "kategori": "Harmonis", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.23},
        {"rank": 6, "kategori": "Loyal", "presentase kelulusan": 78, "skor minimum": 2, "rata-rata skor": 2.69},
    ]
)
st.data_editor(
    dfakhlakp3k, 
    column_config={
        "presentase kelulusan": st.column_config.ProgressColumn(
            "presentase kelulusan",
            help="Berapa orang yang lulus",
            format="%.2f %%",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)
#Slide6
dfakhlakpelaksana = pd.DataFrame(
    [
        {"rank": 1, "kategori": "Kompeten", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.85},
        {"rank": 2, "kategori": "Amanah", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.68},
        {"rank": 3, "kategori": "Kolaboratif", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.55},
        {"rank": 4, "kategori": "Harmonis", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.43},
        {"rank": 5, "kategori": "Adaptif", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.19},
        {"rank": 6, "kategori": "Loyal", "presentase kelulusan": 94, "skor minimum": 2, "rata-rata skor": 3.51},
    ]
)
st.data_editor(dfakhlakpelaksana,     
        column_config={
        "presentase kelulusan": st.column_config.ProgressColumn(
            "presentase kelulusan",
            format="%.2f %%",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)
#Slide7
dfkarakterp3k = pd.DataFrame(
    [
        {"rank": 1, "kompetensi": "Collaborative", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.44},
        {"rank": 2, "kompetensi": "Tough Learner", "presentase kelulusan": 98, "skor minimum": 3, "rata-rata skor": 4.07},
        {"rank": 3, "kompetensi": "Drive Execution", "presentase kelulusan": 85, "skor minimum": 3, "rata-rata skor": 3.92},
        {"rank": 4, "kompetensi": "Accountability", "presentase kelulusan": 78, "skor minimum": 3, "rata-rata skor": 3.46},
    ]
)
st.data_editor(dfkarakterp3k,     
        column_config={
        "presentase kelulusan": st.column_config.ProgressColumn(
            "presentase kelulusan",
            format="%.2f %%",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)
#Slide8
dfkarakterpelaksana = pd.DataFrame(
    [
        {"rank": 1, "kompetensi": "Drive Execution", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.87},
        {"rank": 2, "kompetensi": "Collaborative", "presentase kelulusan": 100, "skor minimum": 2, "rata-rata skor": 3.55},
        {"rank": 3, "kompetensi": "Tough Learner", "presentase kelulusan": 97, "skor minimum": 3, "rata-rata skor": 3.85},
        {"rank": 4, "kompetensi": "Accountability", "presentase kelulusan": 93, "skor minimum": 3, "rata-rata skor": 3.62},
    ]
)
st.data_editor(dfkarakterpelaksana,     
        column_config={
        "presentase kelulusan": st.column_config.ProgressColumn(
            "presentase kelulusan",
            format="%.2f %%",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)
#Slide9
dfkarakterkriya = pd.DataFrame(
    [
        {"rank": 1, "kemampuan": "Tempo Kerja", "presentase kelulusan": 90, "skor minimum": 2, "rata-rata skor": 3.40},
        {"rank": 2, "kemampuan": "Ketahanan Kerja", "presentase kelulusan": 90, "skor minimum": 2, "rata-rata skor": 3.65},
        {"rank": 3, "kemampuan": "Ketelitian", "presentase kelulusan": 84, "skor minimum": 2, "rata-rata skor": 3.48},
    ]
)
st.data_editor(dfkarakterkriya,     
        column_config={
        "presentase kelulusan": st.column_config.ProgressColumn(
            "presentase kelulusan",
            format="%.2f %%",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)
#Slide10
dfpie = px.data.tips()
fig1 = px.pie(dfpie, values='tip', names='day')
fig1

fig2 = px.pie(dfpie, values='tip', names='day')
fig2

#Slide11

#Slide12
st.header("Parameter Kelulusan P3K")

dfteskepribadianakhlakp3k = pd.DataFrame (
    [
        {"nomor": 1, "Core Value": "Amanah", "Nilai Minimum": 2},
        {"nomor": 2, "Core Value": "Kompeten", "Nilai Minimum": 2},
        {"nomor": 3, "Core Value": "Harmonis", "Nilai Minimum": 2},
        {"nomor": 4, "Core Value": "Loyal", "Nilai Minimum": 2},
        {"nomor": 5, "Core Value": "Adaptif", "Nilai Minimum": 2},
        {"nomor": 6, "Core Value": "Kolaboratif", "Nilai Minimum": 2},
    ]
)

st.data_editor(dfteskepribadianakhlakp3k, hide_index=True)

dfkompetensimandiriancharacteristicp3k = pd.DataFrame (
    [
        {"no": 1, "Core Value": "Tough Learner", "Nilai Minimum": 3},
        {"no": 2, "Core Value": "Collaboration", "Nilai Minimum": 2},
        {"no": 3, "Core Value": "Accountability", "Nilai Minimum": 3},
        {"no": 4, "Core Value": "Drive Execution", "Nilai Minimum": 3},
    ]
)

st.data_editor(dfkompetensimandiriancharacteristicp3k, hide_index=True)

dfkelulusanp3klainlainp3k = pd.DataFrame (
    [
        {"no": 1, "Core Value": "IQ Score", "Nilai Minimum": 95},
        {"no": 2, "Core Value": "GRIT", "Nilai Minimum": 2},
        {"no": 3, "Core Value": "Learning Agility", "Nilai Minimum": "Medium"},
    ]
)

st.data_editor(dfkelulusanp3klainlainp3k, hide_index=True)

#Slide13
dfparameterrendahp3k = pd.DataFrame (
    [
        {"Jumlah Parameter yang Tidak Lulus": 1, "Jumlah Peserta": 38, "Persentase": 21},
        {"Jumlah Parameter yang Tidak Lulus": 2, "Jumlah Peserta": 93, "Persentase": 50},
        {"Jumlah Parameter yang Tidak Lulus": 3, "Jumlah Peserta": 38, "Persentase": 21},
        {"Jumlah Parameter yang Tidak Lulus": 4, "Jumlah Peserta": 16, "Persentase": 9},
        {"Jumlah Parameter yang Tidak Lulus": 5, "Jumlah Peserta": 0, "Persentase": 0},
    ]
)

st.data_editor(dfparameterrendahp3k, hide_index=True)

dfparameterrendahp3k1 = pd.DataFrame (
    [
        {"Rank": 1, "Parameter": 25, "Persentase": 66},
        {"Rank": 2, "Parameter": 7, "Persentase": 18},
        {"Rank": 3, "Parameter": 5, "Persentase": 13},
        {"Rank": 4, "Parameter": 1, "Persentase": 3},
        {"Rank": 5, "Parameter": 0, "Persentase": 0},
    ]
)

st.data_editor(dfparameterrendahp3k1, hide_index=True)

#Slide14
st.header("Parameter Kelulusan Pelaksana")

#List
value_list_pelaksana_akhlak = ['Amanah','Kompeten','Harmonis','Loyal','Adaptif','Kolaboratif']
minimum_pelaksana_akhlak = [2,2,2,2,2,2]

value_list_pelaksana_mandirian = ['Tough Learner','Collaboration','Accountability','Drive Execution']
minimum_pelaksana_mandirian = [3,2,3,2]

value_list_pelaksana_lain = ['IQ Score','GRIT','Learning Agility']
minimum_pelaksana_lain = [95,3,'Medium']

st.subheader("Tes Kepribadian Akhlak")
df_value_list_pelaksana_akhlak = pd.DataFrame(data={'Nomor':nomor_list_6, 'Core Value':value_list_pelaksana_akhlak, 'Nilai Minimum':minimum_pelaksana_akhlak})
st.data_editor(df_value_list_pelaksana_akhlak, hide_index=True)

st.subheader("Kompetensi Mandirian Characteristics")
df_value_list_pelaksana_mandirian = pd.DataFrame(data={'Nomor':nomor_list_4, 'Core Value':value_list_pelaksana_mandirian, 'Nilai Minimum':minimum_pelaksana_mandirian})
st.data_editor(df_value_list_pelaksana_mandirian, hide_index=True)

st.subheader("Lain-lain")
df_value_list_pelaksana_lain = pd.DataFrame(data={'Nomor':nomor_list_3, 'Core Value':value_list_pelaksana_lain, 'Nilai Minimum':minimum_pelaksana_lain})
st.data_editor(df_value_list_pelaksana_lain, hide_index=True)

#Slide16
st.header("Parameter Kelulusan Kriya")

#List
value_list_kriya_kemampuan = ['Tempo Kerja','Ketelitian','Ketahanan Kerja']
minimum_kriya_kemampuan = [2,2,2]

value_list_kriya_lain = ['IQ Score']
minimum_kriya_lain = [95]

st.subheader("Tes Kemampuan")
df_value_list_kriya_kemampuan = pd.DataFrame(data={'Nomor':nomor_list_3, 'Kompetensi':value_list_kriya_kemampuan, 'Skor Minimum':minimum_kriya_kemampuan}) 
st.data_editor(df_value_list_kriya_kemampuan, hide_index=True)

st.subheader("Lain-lain")
df_value_list_kriya_lain = pd.DataFrame(data={'Nomor':nomor_list_1, 'Parameter':value_list_kriya_lain, 'Skor Minimum':minimum_kriya_lain})
st.data_editor(df_value_list_kriya_lain, hide_index=True)

#Slide17
st.header("Persebaran Parameter dengan Skor Terendah Kriya")

value_list_terendah_kriya1 = [113,50]
minimal_terendah_kriya1 = [69,31]

value_list_terendah_kriya2 = ['Tes Kemampuan','Skor IQ']
jumlah_terendah_kriya2 = [57,56]
minimal_terendah_kriya2 = [50,50]

df_value_list_terendah_kriya1 = pd.DataFrame(data={'Jumlah Parameter yang Tidak Lulus':nomor_list_2, 'Jumlah Peserta':value_list_terendah_kriya1, 'Persentase':minimal_terendah_kriya1})
st.data_editor(df_value_list_terendah_kriya1, hide_index=True)

df_value_list_terendah_kriya1 = pd.DataFrame(data={'Rank':nomor_list_2, 'Parameter':value_list_terendah_kriya2, 'Jumlah':jumlah_terendah_kriya2,'Persentase':minimal_terendah_kriya2})
st.data_editor(df_value_list_terendah_kriya1, hide_index=True)

#Slide18
st.header("Kesimpulan")

st.write("Kategori Peserta: P3K")
dfkesimpulanp3k = pd.DataFrame (
    [
        {"Kategori": "Kesimpulan", "Deskripsi": "Terlihat gambaran yang cukup normal antara jumlah lulus vs tidak lulus (53 % vs  47%)"},
        {"Kategori": "Hasil IQ", "Deskripsi": "Sebagian besar peserta memiliki standar kognisi sesuai atau lebih dari standar yang diterapkan (102)"},
        {"Kategori": "Akhlak", "Deskripsi": "Aspek AKHLAK dengan nilai terbaik adalah Kompeten dan Adaptif. Sedangkan yang bernilai terendah adalah Loyal. Namun, nilai rata-rata capaian lebih tinggi daripada nilai batas standar."},
        {"Kategori": "Mandirian", "Deskripsi": "Kompetensi dengan nilai average terbaik adalah Collaborative , sedangkan terendah adalah Accountability. Namun, nilai rata-rata capaian lebih tinggi daripada nilai batas standar."},
        {"Kategori": "Learning Agility", "Deskripsi": "Sebagian besar peserta (91%) memiliki level Learning Agility sesuai dan/atau di atas standar."},
        {"Kategori": "GRIT", "Deskripsi": "Sebagian besar peserta (82%) memiliki level Grit sesuai dan/atau di atas standar."},
        {"Kategori": "Nilai Akhir", "Deskripsi": "Peserta sebagian besar mendapat kesimpulan Tidak Lulus karena nilai GRIT yang tidak sesuai standar"},
    ]
)

st.data_editor(dfkesimpulanp3k, hide_index=True)

#Slide19
st.header("Kesimpulan")

st.write("Kategori Peserta: Pelaksana")
dfkesimpulanpelaksana = pd.DataFrame (
    [
        {"Kategori": "Kesimpulan", "Deskripsi": "Terlihat gambaran yang cukup normal antara jumlah lulus vs tidak lulus (60% vs 40%)."},
        {"Kategori": "Hasil IQ", "Deskripsi": "Sebagian besar peserta memiliki standar kognisi sesuai atau lebih dari standar yang diterapkan (107)."},
        {"Kategori": "Akhlak", "Deskripsi": "Aspek AKHLAK dengan nilai terbaik adalah Kompeten & Amanah. Sedangkan yang bernilai terendah adalah Loyal. Namun, nilai rata-rata capaian lebih tinggi daripada nilai batas standar."},
        {"Kategori": "Mandirian", "Deskripsi": "Kompetensi dengan nilai average terbaik adalah Drive Execution, sedangkan terendah adalah Accountability. Namun, nilai rata-rata capaian lebih tinggi daripada nilai batas standar."},
        {"Kategori": "Learning Agility", "Deskripsi": "Hampir semua peserta (79%) memiliki level Learning Agility sesuai dan/atau di atas standar."},
        {"Kategori": "GRIT", "Deskripsi": "Sebagian besar peserta (88%) memiliki level Grit sesuai dan/atau di atas standar."},
        {"Kategori": "Nilai Akhir", "Deskripsi": "Peserta sebagian besar mendapat kesimpulan Tidak Lulus karena nilai Learning Agility yang tidak sesuai standar."},
    ]
)

#Slide20
st.header("Kesimpulan")

st.write("Kategori Peserta: Kriya")
dfkesimpulanpelaksana = pd.DataFrame (
    [
        {"Kategori": "Kesimpulan", "Deskripsi": "Terlihat gambaran yang cukup normal antara jumlah lulus vs tidak lulus (58% vs 42%)."},
        {"Kategori": "Hasil IQ", "Deskripsi": "Sebagian besar peserta memiliki standar kognisi sesuai atau lebih dari standar yang diterapkan (101)."},
        {"Kategori": "Akhlak", "Deskripsi": "Aspek dengan capaian average terbaik adalah Tempo Kerja, sedangkan yang memiliki average terendah adalah Ketelitian. Namun, nilai rata-rata capaian lebih tinggi daripada nilai batas standar."},
        {"Kategori": "Nilai Akhir", "Deskripsi": "Peserta sebagian besar mendapat kesimpulan Tidak Lulus karena hasil Tes Kemampuan yang tidak sesuai standar."},
    ]
)

#Slide21
st.header("Rekomendasi/Tindak Lanjut")

st.subheader("Dari keseluruhan hasil Agustus - September, terlihat bentuk persebaran data yang sudah baik dan sebagian besar menyerupai tren data pada bulan-bulan sebelumnya. Hal ini membuat belum adanya tindak lanjut yang perlu dilakukan.")
