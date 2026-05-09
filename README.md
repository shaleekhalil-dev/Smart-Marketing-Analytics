# Smart Marketing & Sentiment ROI Analytics 📈

An automated strategic data system that integrates **Natural Language Processing (NLP)** for sentiment analysis with **Financial Business Intelligence (BI)**. This project analyzes customer reviews alongside advertising spend to optimize marketing ROI.

## 🎯 Strategic Purpose
In the digital age, understanding "why" a customer buys is as important as "what" they buy. This tool bridges that gap by:
- Categorizing customer feedback sentiment (Positive, Neutral, Negative).
- Calculating **ROAS (Return on Ad Spend)** to measure financial efficiency.
- Identifying brand risks through sentiment-to-revenue correlation.

## 🛠️ Tech Stack
- **Python 3.14+**
- **Data Engineering:** Pandas, NumPy
- **Visual Analytics:** Matplotlib, Seaborn (Correlation Heatmaps & ROI Charts)
- **Reporting:** FPDF2 & Python-docx for automated executive reports.

## 📂 Project Structure
- `data/`: Raw and processed marketing datasets.
- `figures/`: Sentiment distribution and ROAS performance visualizations.
- `outputs/`: Multi-format strategic reports (PDF, Word, Markdown).
- `run_all.py`: Orchestrates the entire data pipeline.

## 🚀 Quick Start
1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn fpdf2 python-docx