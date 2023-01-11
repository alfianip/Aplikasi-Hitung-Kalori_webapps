import streamlit as st

st.set_page_config(
    page_title="Hitung Kalori",
    page_icon="👋",
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media3.cgtrader.com/variants/UrP4w93L59AoLUzqnhufXjpX/40073f86dea5cc27b3e46b911284f10ff35833da74046da55f55f229c8993de7/Image0001.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
st.write("# Welcome to Aplikasi Hitung Kalori👋")
   


st.markdown("""
Aplikasi hitung kalori merupakan alat hitung yang akan membantu kamu 
untuk mengetahui kebutuhan kalori harianmu !_ :pizza:""")



st.title("""
:avocado:_Aplikasi Hitung Kalori_:spaghetti:
""")

jeniskelamin= st.selectbox(
    'Jenis Kelamin',
    ('Perempuan','Laki - Laki'))
usia=st.number_input("Usia",0)
beratbadan= st.number_input(" Berat Badan (Kg)", 0)
tinggibadan= st.number_input(" Tinggi Badan (cm)", 0)
Hitung = st.button("Hitung Kalori")
if jeniskelamin =='Perempuan':
    kalori=655+(9.6*beratbadan)+(1.8*tinggibadan)-(4.7*usia)
    st.write("Hasil kalori adalah ",kalori,"KKal")
elif jeniskelamin =='Laki - Laki':
    kalori=66.5+(13.7*beratbadan)+(5*tinggibadan)-(6.8*usia)
    st.write("Kalori harian yang dibutuhkan adalah ",kalori,"KKal")
    


