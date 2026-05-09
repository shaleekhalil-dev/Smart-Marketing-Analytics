import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_marketing_visuals():
    # تحميل البيانات المعالجة
    df = pd.read_csv('data/processed_marketing_data.csv')
    
    # ضبط السمة الجمالية للرسوم
    sns.set_theme(style="whitegrid")
    
    # 1. الرسم الأول: متوسط العائد على الإنفاق الإعلاني (ROAS) حسب القناة
    plt.figure(figsize=(10, 6))
    avg_roas = df.groupby('Channel')['ROAS'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_roas.index, y=avg_roas.values, palette='magma')
    plt.title('Average Return on Ad Spend (ROAS) per Marketing Channel')
    plt.ylabel('Mean ROAS (Revenue / Spend)')
    plt.xlabel('Marketing Channel')
    plt.savefig('figures/channel_roas.png')
    plt.close()
    
    # 2. الرسم الثاني: تحليل توزيع المشاعر لكل قناة (تراكمي)
    # نقوم بحساب عدد المراجعات لكل نوع مشاعر داخل كل قناة
    sentiment_dist = df.groupby(['Channel', 'Sentiment']).size().unstack().fillna(0)
    
    sentiment_dist.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#e74c3c', '#95a5a6', '#2ecc71'])
    plt.title('Customer Sentiment Composition by Channel')
    plt.ylabel('Number of Reviews')
    plt.xlabel('Marketing Channel')
    plt.legend(title='Sentiment Status')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('figures/sentiment_breakdown.png')
    plt.close()
    
    print("Marketing & Sentiment visualizations generated in figures/ folder.")

if __name__ == "__main__":
    create_marketing_visuals()