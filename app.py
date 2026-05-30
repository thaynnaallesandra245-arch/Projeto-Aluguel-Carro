import streamlit as st
from datetime import datetime 


st.sidebar.image("logo.png")
st.sidebar. title("locadora de carro")

carro = st.sidebar.selectbox("selecione o carro que deseja alugar:",["bmw","evoque","onix","porsche" ])

st.image(f"{carro}.png")

valores_diarias = {"bmw":4000, "porsche":5000, "onix":300, "evoque":7000}
valor_diaria = valores_diarias.get(carro)

st.subheader(f"{carro} - diária: R$ {valores_diarias[carro]}")
data_retirada = st.date_input("selecione o dia da retirada:", datetime.now (), datetime.now())
data_devolução = st.date_input("selecione a data de retirada",data_retirada,data_retirada)

if st.button("alugar"):
   dias =(data_devolução - data_retirada).days

   valor_total = valor_diaria * dias

st.write(f"carro escolhido **[carro]**")
st.metric("total do aluguel", f"R$ {valor_total:. 2f}")
st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)


st.feedback("stars")
st.text_area("Deixe um comentário: ")
if st.button("Comentar"):
    st.balloons()