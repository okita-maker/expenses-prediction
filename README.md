# expenses-prediction
# 家計支出予測アプリ
https://expenses-prediction-mu69tdmauywmfw7pyigm6f.streamlit.app/

## 📌 プロジェクト概要
このアプリは家計簿データをもとに支出を可視化し、AI（線形回帰モデル）で未来の支出を予測する仕組みを実装しています。
本機能は「家計簿」だけでなく、売上予測・在庫予測・アクセス解析など、ビジネスシーンでも応用可能です。
データをアップロードするだけで誰でも使えるUIをStreamlitで構築し、クライアントや一般ユーザーが直感的に使える設計を意識しました。

## 🛠️ 使用技術
- Python
- Pandas
- Matplotlib
- Prophet
- Streamlit

## 📊 実行イメージ
予測結果は以下のように、実績と予測を色分けして表示します👇  

![予測グラフ](https://github.com/okita-maker/expenses-prediction/blob/57f376208bf050caabbc2d117f220348b96c1777/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-09-28%20232049.png)

## 💡 特徴
- 月ごとの支出データを入力するだけで簡単に予測可能  
- グラフは日本語ラベル付きで直感的に理解できる  
- 予測結果は文章でも表示され、ユーザーに伝わりやすい  

## 🚀 今後の改善ポイント
- 支出項目ごとの詳細分析機能を追加予定  
- Web公開（Streamlit Cloud or HuggingFace Spaces）を検討中
👉 まとめると、このアプリは 「自分の家計簿をアップロードすれば、未来の支出が予測できるAIアプリ」 です！
