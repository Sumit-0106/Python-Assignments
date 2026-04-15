import streamlit as st
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

st.set_page_config(page_title="Trading Bot", layout="centered")

st.title("📈 Binance Futures Trading Bot")
st.write("Place BUY/SELL orders easily")

# Inputs
symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox("Side", ["BUY", "SELL"])

order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])

quantity = st.number_input("Quantity", min_value=0.0001, value=0.001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=1.0)

# Button
if st.button("Place Order 🚀"):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        st.info("Placing order...")

        order = place_order(symbol, side, order_type, quantity, price)

        st.success("✅ Order Placed Successfully!")

        st.write("### 📊 Order Details")
        st.write(f"Order ID: {order['orderId']}")
        st.write(f"Status: {order['status']}")
        st.write(f"Executed Qty: {order['executedQty']}")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")