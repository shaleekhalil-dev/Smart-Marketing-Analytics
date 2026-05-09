import pandas as pd

def analyze_sentiment(text):
    text = text.lower()
    positive_words = ['excellent', 'amazing', 'high quality', 'recommended', 'fast']
    negative_words = ['poor', 'regret', 'slow', 'confusing', 'damaged', 'not work']
    
    score = 0
    for word in positive_words:
        if word in text: score += 1
    for word in negative_words:
        if word in text: score -= 1
        
    if score > 0: return 'Positive'
    elif score < 0: return 'Negative'
    else: return 'Neutral'

def process_marketing_analytics():
    df = pd.read_csv('data/customer_marketing_data.csv')
    
    # 1. تطبيق تحليل المشاعر على النصوص
    df['Sentiment'] = df['Review_Text'].apply(analyze_sentiment)
    
    # 2. حساب العائد على الإنفاق الإعلاني (ROAS)
    # المعادلة: (قيمة المشتريات / الإنفاق الإعلاني)
    df['ROAS'] = (df['Purchase_Value'] / df['Ad_Spend']).round(2)
    
    # 3. تحليل القنوات: أي قناة تحقق أعلى رضا وأعلى عائد؟
    channel_analysis = df.groupby('Channel').agg({
        'ROAS': 'mean',
        'Rating': 'mean',
        'Sentiment': lambda x: (x == 'Positive').sum() / len(x) * 100
    }).rename(columns={'Sentiment': 'Positive_Percentage'})
    
    # 4. حفظ البيانات المحدثة والملخص
    df.to_csv('data/processed_marketing_data.csv', index=False)
    
    summary = f"""
    Marketing Sentiment & ROI Strategic Summary
    ==========================================
    Top Performing Channel (by ROAS): {channel_analysis['ROAS'].idxmax()}
    Highest Customer Satisfaction: {channel_analysis['Rating'].idxmax()}
    
    Channel Detailed Metrics:
    {channel_analysis.to_string()}
    """
    
    with open('outputs/marketing_analysis_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)
        
    print("Marketing data processed. Sentiment analyzed and ROI calculated.")

if __name__ == "__main__":
    process_marketing_analytics()