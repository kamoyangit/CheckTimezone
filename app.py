import streamlit as st
from zoneinfo import ZoneInfo
import datetime

jst = ZoneInfo("Asia/Tokyo")
now_jst = datetime.datetime.now(jst)
st.write(f"現在の日本時間: {now_jst}")