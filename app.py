import streamlit as st
from zoneinfo import ZoneInfo
import datetime
import os

# --- デバッグフラグ ---
# ここをTrue/Falseで切り替える
DEBUG = os.environ.get('DEBUG_OPTION', False)
# --------------------

# --- ヘルパー関数 ---
def is_lunch_time():
    # ローカルだと上手くいくが、Streamlit.ioにデプロイするとNG
    # jst = pytz.timezone('Asia/Tokyo')
    # now_jst = datetime.datetime.now(jst).time()
    # zoneifoを使う方法
    jst = ZoneInfo("Asia/Tokyo")
    now_jst = datetime.datetime.now(jst).time()
    start_time = datetime.time(11, 0)
    end_time = datetime.time(14, 0)
    if DEBUG:
        return True
    else :
        return start_time <= now_jst < end_time


jst = ZoneInfo("Asia/Tokyo")
now_jst = datetime.datetime.now(jst)
st.write(f"現在の日本時間: {now_jst}")

if is_lunch_time():
    st.write(f"ランチタイムだよ")
else:
    st.wirte(f"ランチタイムじゃないよ")