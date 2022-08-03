import streamlit as st
import pandas as pd
import json

import plotly.express as px
import plotly.graph_objects as go

## Layout
st.set_page_config(layout="wide")

## Judul
st.title("Fenomena Balita Stunting dan Potensinya Sebagai CSR")

## Intro
st.write("""<div style="text-align: justify;">

Sempat ramai di sosial media kita pernyataan ketua dewan pengarah BRIN, Ibu Megawati Soekarnoputri, terkait rasa herannya dengan para Ibu di Indonesia yang menggunakan minyak goreng.
Terlepas dari kontroversi di akhir Maret 2022 tersebut, tahukah kamu bahwa agenda yang dihadiri Ibu Megawati sebenarnya membahas tentang fenomena balita stunting di Indonesia?
Meminjam dari situs BKKBN<sup>[1]</sup>, <b>stunting adalah kekurangan gizi pada bayi di 1000 hari pertama kehidupan yang berlangsung lama dan menyebabkan terhambatnya perkembangan otak dan tumbuh kembang anak</b>.
Masalah stunting penting untuk diselesaikan, karena berpotensi <b>mengganggu potensi sumber daya manusia dan berhubungan dengan tingkat kesehatan, bahkan kematian anak</b>.
Pada umumnya, <b>stunting dapat diidentifikasi dari tinggi badan yang kurang dari nilai standar nasional</b>. 

</div>""", unsafe_allow_html=True)

st.write('')

st.write("""<div style="text-align: justify;">

Di sisi lain, sebuah perusahaan tentu tidak dapat dipisahkan dari keadaan masyarakat di sekitarnya. <b>Perusahaan yang diterima oleh masyarakat sekitar dan pemerintah akan lebih mudah menjalankan aktivitas bisnisnya</b>.
Selain itu, perusahaan juga memiliki pekerja yang sebagian besarnya adalah manusia sehingga nilai kemanusiaan tidak dapat dipisahkan dari pekerjaan. 
Pada umumnya, perusahaan memiliki kewajiban memberdayakan masyarakat sekitar melalui <i> Corporate Social Responsibility </i> yang telah diatur oleh undang-undang.
Dari kedua hal itu, <b>tulisan ini akan menunjukkan bahwa fenomena stunting di Indonesia memiliki potensi sebagai objek <i>Corporate Social Responsibility</i> atau <i>Community Development</i></b> menggunakan metode deduktif.
Sebagai permulaan, mari kita lihat kondisi yang terjadi saat ini.

</div>""", unsafe_allow_html=True)

st.write('---')
#----------------------------------------------------------------------------------------------------
## Map 1
st.header('Kondisi di Indonesia')
st.write("""<div style="text-align: justify;">

Peta di bawah menunjukkan sebaran kasus stunting di 34 provinsi<sup>[2]</sup> pada tahun 2021. <b>Warna yang semakin kuning mengindikasikan angka stunting yang semakin tinggi</b>. Melihat peta sebaran tersebut, daerah dengan prevalensi terbesar didominasi oleh daerah timur Indonesia.
Prevalensi stunting terbesar berada di di Provinsi Nusa Tenggara Timur, yakni sebesar 37.8%. Artinya, <b>sepertiga jumlah balita di Nusa Tenggara Timur mengalami stunting</b>.
Daerah lain di Indonesia juga tidak memperlihatkan kondisi yang begitu baik. Sebagai perbandingan, standar batas WHO untuk angka stunting adalah 20%.

</div>""", unsafe_allow_html=True)

with open("indonesia-prov.geojson") as response:
    geo = json.load(response)
kamus = pd.read_csv("kamus.csv")
kamus = dict(zip(kamus['provinsi'].str.upper(), kamus['kode']))
df = pd.read_csv("peta-sebaran.csv")
df_mod = df.copy()
df_mod = df_mod.iloc[:,0:2]
df_mod['kode'] = df_mod['provinsi'].apply(lambda x: kamus.get(x))

map1_1,map1_2,map1_3 = st.columns([2,3,1])
with map1_1:
    st.write('')
with map1_2:
    st.markdown('##### Sebaran Kasus Stunting Tahun 2021')
with map1_3:
    st.write('')

m1 = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=df_mod['kode'],
        z=df_mod["2021"],
        colorscale="cividis",
        marker_opacity=0.5,
        marker_line_width=0.5
    )
)
m1.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=3.5,
    mapbox_center={"lat": -2, "lon": 118},
    width=900,
    height=350
)
m1.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(m1, use_container_width=True)
st.markdown('---')

## ------------------------------------------------------------------------------------------
## Korelasi stunting dan aspek kehidupan
st.header("Suatu Permasalahan Strategis")
st.write("""<div style="text-align: justify;">
Fenomena stunting di Indonesia dirasa identik dengan beberapa aspek kehidupan, seperti tingginya angka kemiskinan dan rendahnya angka pendidikan.
Namun, perasaan tidaklah cukup berdasar untuk mengkaji fenomena stunting lebih lanjut. Oleh karena itu, dilakukan analisis korelasi. <b>Nilai korelasi dari setiap aspek dapat dilihat pada <i>metric</i> di bawah</b>.
Nilai korelasinya berada pada kategori lemah hingga <i>moderate</i>. Meskipun korelasinya tidak kuat, nilai dari <i>p-value</i> menunjukkan bahwa ketiga aspek memiliki hubungan yang signifikan secara statistik dengan angka stunting.
Artinya, <b>stunting tidak hanya dipengaruhi oleh satu aspek saja, melainkan berkaitan dengan banyak aspek kehidupan masyarakat</b>.
Hal tersebut membuat fenomena stunting menjadi suatu <b>permasalahan yang strategis untuk diselesaikan</b>. 
</div>""", unsafe_allow_html=True)

st.markdown('\n')

c2_col1, c2_col2, c2_col3, c2_col4 = st.columns([2,2,2,2])
with c2_col1:
    st.markdown('##### Persentase Korelasi:')
with c2_col2:
    st.metric('Stunting & Pendidikan', '-50%')
    #st.markdown('---')
with c2_col3:
    st.metric('Stunting & Sosial', '45%')
    #st.markdown('---')
with c2_col4:
    st.metric('Stunting & Ekonomi', '36%')
    #st.markdown('---')

st.write('---')

c2_col7, c2_col8, c2_col9= st.columns([2.2,2,2])
with c2_col7:
    st.subheader('Melihat Korelasi Lebih Dekat')
with c2_col8:
    aspek_dummy = st.selectbox('Aspek',("Ekonomi", "Sosial", "Pendidikan"))
    aspek_dict = {"Ekonomi": "stunting-ekonomi.csv",
                    "Sosial": "stunting-sosial.csv",
                    "Pendidikan": "stunting-pendidikan.csv"}
    aspek = aspek_dict[aspek_dummy]
with c2_col9:
    year = st.selectbox('Tahun',(2015,2016,2017,2018, 2019, 2021))

c2_col5, c2_col6= st.columns([2,4])
with c2_col5:
    st.write("""<div style="text-align: justify;">
    Aspek sosial diwakilkan oleh persentase perempuan berusia 20-24 tahun yang hidup bersama sebelum umur 18 tahun.
    Aspek ekonomi diwakilkan oleh persentase penduduk yang berada di bawah garis kemiskinan. Sementara itu, aspek pendidikan diwakilkan 
    oleh angka siswa yang menuntaskan wajib sekolah 12 tahun<sup>[3]</sup>. 
    <b>Angka stunting dan salah satu aspek diplot pada grafik di kanan untuk menunjukkan pola naik dan turun yang seragam ataupun berlawanan</b>.
    Pada tahun 2020, pandemi covid berada pada puncaknya, sehingga survei kasus stunting di Indonesia tidak dilakukan. Namun angkanya diprediksi bernilai 26%
    </div>""", unsafe_allow_html=True)

with c2_col6:
    stunting_aspek = pd.read_csv(aspek)
    stunting_aspek_year = stunting_aspek[stunting_aspek['tahun']==year]
    c2 = px.line(stunting_aspek_year,
                x="provinsi",
                y=["prevalensi", aspek_dummy.lower()],
                color_discrete_sequence=['blue', 'yellow'],
                markers=True)

    ## title=dict(text=f"Prevalensi Stunting dan Aspek {aspek_dummy}", font=dict(size=20)),
    c2.update_layout(
                xaxis_title="34 Provinsi",
                yaxis_title="Prevalensi",
                legend_title="Keterangan",
                title_x=0.47,
                width=700,
                height=350,
                margin=dict(l=10, r=10, t=10, b=10),
                legend=dict(x=.1, y=1, traceorder='normal')
    )
    newnames = {"prevalensi": "Stunting", aspek_dummy.lower(): aspek_dummy}
    c2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                        legendgroup = newnames[t.name],
                                        hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                        )
                    )
    c2.update_xaxes(showticklabels=False)
    st.plotly_chart(c2, use_container_width=False)

st.markdown('---')

#---------------------------------------------------------------------------------------------------
## Usaha Pemerintah
st.header('Usaha Pemerintah')

c3_col1, c3_col2 = st.columns([2,4])

with c3_col1:

    st.write("""<div style="text-align: justify;">
    Pemerintah telah berkomitmen untuk menurunkan angka stunting di Indonesia sejak tahun 2018 melalui <b>program intervensi gizi</b>. Selain telah menerbitkan Peraturan Presiden No 72 tahun 2021.
    <b>Presiden Joko Widodo juga menargetkan angka stunting turun menjadi 14% pada tahun 2024</b>. Melihat data dari Pemantauan Status Gizi (PSG) tahun 2015 hingga 2018
    dan Studi Status Gizi (SSGI) tahun 2019 hingga 2021, target tersebut terlihat cukup realistis. Pada gambar dibawah, terlihat adanya <i>trend</i> yang menurun secara konsisten sejak awal tahun 2019.
    Hal ini dapat <strong>mengindikasikan keberhasilan program intervensi gizi yang telah dilakukan oleh pemerintah</strong>.
    </div>""", unsafe_allow_html=True)

with c3_col2:
    overall = pd.read_csv("overall-trend.csv")

    c3 = px.line(overall,
                x="tahun",
                y="prevalensi",
                color='sumber',
                color_discrete_sequence=["black", "#5000B9"],
                markers=True)
    c3.add_bar(x=overall.loc[0:3,'tahun'], y=overall.loc[0:3,'prevalensi'],
                marker=dict(color="#949494"), width=0.5, showlegend=False)
    c3.add_bar(x=overall.loc[4:,'tahun'], y=overall.loc[4:,'prevalensi'],
                marker=dict(color="#51A2D5"), width=0.5, showlegend=False)
    c3.update_layout(title=dict(text="Angka Stunting di Indonesia", font=dict(size=20)),
                xaxis_title="Tahun",
                yaxis_title="Prevalensi",
                legend_title="Sumber Data",
                title_x=0.52,
                width=700,
                height=350,
                margin=dict(l=10, r=10, t=30, b=10),
                showlegend=True, 
                legend=dict(x=0.745, y=1, traceorder='normal'),
                yaxis_range=[20,33]
                )

    st.plotly_chart(c3, use_container_width=False)

st.markdown("---")

#--------------------------------------------------------------------------------------
st.header('Kolaborasi dan Manfaat')

st.write("""<div style="text-align: justify;">

Pemerintah telah membuka kesempatan bagi pihak ketiga seperti swasta, akademisi, media, dan komunitas untuk turut ikut serta menurunkan angka stunting lewat <b>program kemitraan</b>.
Beberapa perusahaan seperti Danone dan Mayora terlibat dalam usaha penurunan stunting pada skala nasional bersama instansi pemerintah terkait. Program kemitraan memiliki beberapa opsi kegiatan yang dapat dilaksanakan oleh pihak ketiga sesuai dengan profil dan kapasitas pihak ketiga.
Pada gambar di bawah dapat dilihat <b>5 aksi yang paling banyak dilakukan oleh perusahaan</b><sup>[4]</sup>. Pelatihan dan peningkatan layanan posyandu menjadi aksi yang paling banyak dilakukan. Pelatihan mencakup pelatihan kader dan kewirausahaan, sedangkan layanan posyandu mencakup pemeriksaan kesehatan.

</div>""", unsafe_allow_html=True)

kegiatan = pd.read_csv('count-kegiatan.csv')
kegiatan_mod = kegiatan.sort_values(by='jumlah', ascending=False)
kegiatan_mod = kegiatan_mod.head(5)
c4_1 = px.bar(kegiatan_mod, x='jumlah', y='aksi', orientation='h',
        color='group', color_discrete_map={'satu':'#7586DF', 'dua':'#949494', 'tiga':'#C6C6C6'})
c4_1.update_layout(yaxis=dict(autorange="reversed"),
    xaxis_title="Jumlah Perusahaan",
    yaxis_title="",
    width=800,
    height=280,
    showlegend=False,
    bargap=0.05,
    margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(c4_1, use_container_width=False)
st.markdown('---')

col4_1, col4_2 = st.columns([3,5])

with col4_2:
    st.write("""<div style="text-align: justify;">
    <b>Pelaksanaan CSR terkait fenomena balita stunting dapat meningkatkan citra baik perusahaan</b>.
    Tinjau kasus pada PT Mayora Indah. Dampak dari pelaksanaan CSR terkait fenomena balita stunting dapat dibandingkan dengan pelaksanaan CSR yang telah dilakukan oleh PT Mayora Indah berupa program bedah rumah.
    Untuk meninjau perbandingan tersebut, pada gambar di kiri disajikan perbandingan publikasi media lewat mesin pencarian Google.
    Jumlah artikel yang membahas CSR fenomena balita stunting dibandingkan dengan CSR bedah rumah.
    Kedua program CSR tersebut menjadi bahasan yang ramai pada rentang pertengahan tahun 2020 hingga 2022. <b>Hasil ini mengindikasikan bahwa pelaksanaan CSR balita stunting lebih banyak diberi perhatian/eksposur oleh media dibandingkan CSR bedah rumah</b>.
    </div>""", unsafe_allow_html=True)

with col4_1:
    news = pd.read_csv('news-bersih.csv')
    news['percent'] = round(news['angka pencarian']/news['total']*100,2)
    c4_2 = px.bar(news, x='keterangan', y='percent', text='percent',
            color='keterangan', color_discrete_map={'stunting':'#7586DF', 'bedah rumah':'#949494'})
    c4_2.update_layout(
        xaxis_title="",
        yaxis_title="Jumlah Hasil Pencarian",
        width=400,
        height=280,
        showlegend=False,
        bargap=0.05,
        margin={"r": 10, "t": 5, "l": 0, "b": 0},
        yaxis_range=[0,100])
    c4_2.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    c4_2.update_traces(width=0.5)
    st.plotly_chart(c4_2, use_container_width=False)

st.markdown('---')

#----------------------------------------------------------------------------------------------------
st.header('Intisari')

st.markdown("""
**Secara umum**, pemaparan di atas memberikan *insight* sebagi berikut:
- Fenomena stunting merupakan permasalahan multi-aspek yang nyata dan mendapat banyak perhatian sehingga menjadi bahasan yang strategis
- Permasalahan stunting dapat diatasi melalui langkah-langkah dan kebijakan yang tepat oleh pemerintah bersama dengan elemen-elemen masyarakat
Selain itu, **fenomena stunting juga memiliki potensi sebagai objek *Corporate Social Responsibility* atau *Community Development***.
Potensi tersebut antara lain:
- Meningkatkan kepercayaan publik dan citra baik perusahaan, mengingat fenomena stunting merupakan bahasan strategis
- Memperluas potensi pengembangan bisnis dan jaringan di pemerintahan, mengingat terbukanya ruang kolaborasi bersama pemerintah
""")

st.header('Sumber dan Referensi')

st.markdown("""
1. BKKBN https://www.bkkbn.go.id/berita-indonesia-cegah-stunting
2. Litbangkes https://www.litbang.kemkes.go.id/buku-saku-hasil-studi-status-gizi-indonesia-ssgi-tahun-2021/
3. Badan Pusat Statistik, Tujuan Pembangunan Berkelanjutan, Kesetaraan Gender, dan Pendidikan Berkualitas https://www.bps.go.id
4. Kementerian Sekretariat Negara, Sekretariat Wakil Presiden https://stunting.go.id/
""")
