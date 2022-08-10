import streamlit as st
import qrcode

st.title('QRコード自動生成アプリ')

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

url = st.text_input('QRコードを生成したいURL：')

if st.button('QRコード生成'):
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    st.image(img)