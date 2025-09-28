import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.linear_model import LinearRegression
import numpy as np

# 日本語フォント設定（WindowsならMS Gothic）
rcParams['font.family'] = 'MS Gothic'

# 🎯 アプリタイトルと説明
st.title("💰 AI家計簿予測アプリ")
st.write("このアプリでは、過去の支出データをもとに **未来の家計支出を予測** します！📈")
st.info("👉 CSVをアップロードすると「月ごとの支出合計」と「未来3か月の予測」が表示されます！")

# CSVアップロード
uploaded_file = st.file_uploader("家計簿CSVをアップロードしてください", type="csv")

if uploaded_file:
    # データ読み込み
    df = pd.read_csv(uploaded_file)

    # 必要なカラムチェック
    expected_cols = ["月", "食費", "交通", "交際", "趣味", "合計"]
    if not all(col in df.columns for col in expected_cols):
        st.error("❌ CSVに必要なカラム（'月','食費','交通','交際','趣味','合計'）が含まれていません！")
    else:
        # グラフ（実績）
        st.subheader("📊 月ごとの支出（実績）")
        fig, ax = plt.subplots()
        ax.plot(df["月"], df["合計"], label="実績", marker="o", color="blue")
        ax.set_xlabel("月")
        ax.set_ylabel("支出額（円）")
        ax.legend()
        st.pyplot(fig)

        # AI予測（単純な線形回帰）
        X = np.arange(len(df)).reshape(-1, 1)
        y = df["合計"].values
        model = LinearRegression()
        model.fit(X, y)

        # 未来3か月予測
        future_X = np.arange(len(df), len(df) + 3).reshape(-1, 1)
        future_preds = model.predict(future_X)

        # 未来の月データ
        last_month = pd.to_datetime(df["月"].iloc[-1], format="%Y-%m")
        future_months = pd.date_range(
            start=last_month + pd.offsets.MonthBegin(1),
            periods=3,
            freq="MS"
        ).strftime("%m月")

        future_df = pd.DataFrame({"月": future_months, "合計": future_preds})
        all_data = pd.concat([df[["月", "合計"]], future_df])

        # 実績＋予測グラフ
        st.subheader("🔮 支出予測（実績＋未来3か月）")
        fig, ax = plt.subplots()
        ax.plot(df["月"], df["合計"], label="実績", marker="o", color="blue")
        ax.plot(future_df["月"], future_df["合計"], label="予測", marker="x", linestyle="--", color="red")
        ax.set_xlabel("月")
        ax.set_ylabel("支出額（円）")
        ax.legend()
        st.pyplot(fig)

        # テキストで予測結果を表示
        st.success(f"✨ 予測結果: 次の3か月の支出は **{int(future_preds.mean()):,}円前後** になると予測されます！")
