import pandas as pd
import numpy as np

def generate_marketing_data():
    np.random.seed(10)
    samples = 300
    
    channels = ['Social Media', 'Google Search', 'Email Marketing', 'Direct Access']
    reviews = [
        "Excellent product, exceeded my expectations!",
        "Poor quality and very slow delivery.",
        "Average experience, could be better.",
        "Amazing customer support and high quality.",
        "I regret buying this, it doesn't work as described.",
        "Value for money, highly recommended.",
        "The interface is confusing but the product is okay.",
        "Fast shipping but the packaging was damaged."
    ]
    
    data = {
        'CustomerID': range(1, samples + 1),
        'Channel': np.random.choice(channels, size=samples),
        'Review_Text': np.random.choice(reviews, size=samples),
        'Ad_Spend': np.random.uniform(50, 500, size=samples).round(2),
        'Purchase_Value': np.random.uniform(100, 1000, size=samples).round(2)
    }
    
    # محاكاة درجات المشاعر (Sentiment Score) 
    # سنقوم ببرمجتها لاحقاً في المعالج، لكن هنا نضع "تقييم النجوم" كمؤشر أولي
    data['Rating'] = np.random.randint(1, 6, size=samples)
    
    df = pd.DataFrame(data)
    df.to_csv('data/customer_marketing_data.csv', index=False)
    print("Marketing & Sentiment raw data generated successfully.")

if __name__ == "__main__":
    generate_marketing_data()