from fpdf import FPDF
from generators.common import HTMLTextExtractor as html_te

class SonarQubeSectionGenerator:
    def __init__(self, issues: list):
        self.issues = issues

    def generate(self, pdf: FPDF, t: dict):
        if not self.issues:
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="No SonarQube issues found.", ln=True)
            return

        for idx, issue in enumerate(self.issues, 1):
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(0, 10, f"Issue {idx}: {html_te.strip_html(issue.get('message', ''))}", ln=True)

            pdf.set_font("Arial", size=11)
            pdf.cell(0, 8, f"Rule: {issue.get('rule', '')}", ln=True)
            pdf.cell(0, 8, f"Severity: {issue.get('severity', '')}", ln=True)
            pdf.cell(0, 8, f"Component: {issue.get('component', '')}", ln=True)
            pdf.cell(0, 8, f"Line: {issue.get('line', '-')}", ln=True)
            pdf.multi_cell(0, 8, f"Description:\n{html_te.strip_html(issue.get('message', ''))}")

            pdf.ln(6)
