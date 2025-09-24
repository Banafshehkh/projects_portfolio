import streamlit as st
import currencies
from currency_convertor import convert_currency, get_exchange_rate

st.title(":money_mouth_face: :zap: Currency Convertor")

st.markdown("""
This tool allows you to instantly convert amounts between different currencies 🌍.
Enter the amount and choose the currencies to see the result.
""")

currency_codes = list(currencies.MONEY_FORMATS.keys())
base_currency = st.selectbox('From Currency (Base):', currency_codes, index=currency_codes.index("USD"))
target_currency = st.selectbox('To Currency (Target):', currency_codes, index=currency_codes.index("CAD"))
amount = st.number_input("Enter the amount to convert:", value=0.0, min_value=0.0, step=0.01)


exchange_rate = get_exchange_rate(base_currency, target_currency)
convert_amount = convert_currency(amount, exchange_rate)
col1, col2, col3 = st.columns(3)
col1.metric(label="Base Currency", value=f"{amount} {base_currency}")
# right arrow
col2.markdown("<h1 style='text-align: center; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
col3.metric(label="Target Currency", value=f"{convert_amount:.2f} {target_currency}")


