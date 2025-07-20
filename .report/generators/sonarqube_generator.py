from fpdf import FPDF
from generators.common import HTMLTextExtractor as html_te
from datetime import datetime

class SonarQubeSectionGenerator:
    def __init__(self, hotspots: list):
        self.hotspots = hotspots

    def generate(self, pdf: FPDF):
        if not self.hotspots:
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="No SonarQube hotspots found.", ln=True)
            return

        for i, hs in enumerate(self.hotspots, 1):
            cleaned_message = html_te.strip_html(hs.get('message', ''))
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"{i}. {html_te.strip_html(cleaned_message[:80])}...", ln=True)

            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8,
                f"- File: {hs.get('component').split(':')[-1]}\n"
                f"- Line: {hs.get('line')}\n"
                f"- Risk: {hs.get('securityCategory').upper()} ({hs.get('vulnerabilityProbability')})\n"
                f"- Status: {hs.get('status').replace('_', ' ').title()}\n"
                f"- Rule: {hs.get('ruleKey')}\n"
                f"- Author: {hs.get('author')}\n"
                f"- Created: {format_date(hs.get('creationDate'))}\n"
                f"- Updated: {format_date(hs.get('updateDate'))}\n"
                f"- Description: {cleaned_message}"
            )
            pdf.ln(2)
            
def format_date(date_str: str) -> str:
    """Converts SonarQube ISO date to readable format."""
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%d-%m-%Y %H:%M")
    except Exception:
        return date_str or "N/A"