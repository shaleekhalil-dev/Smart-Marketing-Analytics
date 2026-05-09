from fpdf import FPDF
import os

class MarketingPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Marketing Sentiment & ROI Strategic Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_marketing_pdf_report():
    pdf = MarketingPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    # 1. الرؤية الاستراتيجية
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Strategic Marketing Philosophy", 0, 1)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, (
        "Modern marketing transcends simple transactions. This report evaluates the "
        "synergy between financial investment (ROAS) and customer satisfaction (Sentiment). "
        "By identifying high-performing channels with positive emotional resonance, we "
        "ensure sustainable growth and brand loyalty."
    ))
    pdf.ln(5)

    # 2. المنهجية المالية والنفسية
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Financial & Sentiment Methodology", 0, 1)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, (
        "The system analyzes 300 data points across various channels. Financial efficiency "
        "is measured through Return on Ad Spend (ROAS), while customer sentiment is "
        "categorized using an automated NLP classification model."
    ))
    pdf.ln(5)

    # 3. التحليل المرئي - كفاءة القنوات
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "3. Channel Efficiency & Sentiment Breakdown", 0, 1)
    
    if os.path.exists('figures/channel_roas.png'):
        pdf.image('figures/channel_roas.png', x=20, w=160)
        pdf.ln(2)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, "Chart 1: Comparison of ROAS across marketing channels.", 0, 1, 'C')

    pdf.add_page()

    # 3. التحليل المرئي - توزيع المشاعر
    if os.path.exists('figures/sentiment_breakdown.png'):
        pdf.image('figures/sentiment_breakdown.png', x=20, w=160)
        pdf.ln(2)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, "Chart 2: Qualitative analysis of customer sentiment per channel.", 0, 1, 'C')

    # 4. التوصيات الاستراتيجية للنمو
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "4. Strategic Directives for Growth", 0, 1)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, (
        "- Reallocate budget from low-ROI channels to high-sentiment platforms.\n"
        "- Optimize 'Negative' clusters by refining marketing messaging and customer support.\n"
        "- Implement real-time sentiment tracking to preemptively address brand risks."
    ))

    output_path = 'outputs/Marketing_Sentiment_Strategic_Report.pdf'
    pdf.output(output_path)
    print(f"Strategic Marketing PDF generated successfully at: {output_path}")

if __name__ == "__main__":
    create_marketing_pdf_report()