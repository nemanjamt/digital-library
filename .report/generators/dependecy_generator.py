from fpdf import FPDF
from generators.common import HTMLTextExtractor as html_te

class DependencyCheckSectionGenerator:
    def __init__(self, dependencies: list):
        self.dependencies = dependencies

    def generate(self, pdf: FPDF):
        # Keep only dependencies that have vulnerability list
        vulnerable_deps = [d for d in self.dependencies if d.get("vulnerabilities")]

        if not vulnerable_deps:
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="No vulnerable dependencies found.", ln=True)
            return

        for idx, dep in enumerate(vulnerable_deps, start=1):
            file_name = dep.get("fileName", "Unknown File")
            file_path = dep.get("filePath", "Unknown Path")

            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(0, 10, f"Dependency {idx}: {file_name}", ln=True)

            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 6, f"Path: {file_path}")
            pdf.ln(1)

            for vuln in dep.get("vulnerabilities", []):
                name = vuln.get("name", "CVE-Unknown")
                severity = vuln.get("severity", "UNKNOWN").capitalize()
                desc = html_te.strip_html(vuln.get("description", ""))
                references = vuln.get("references", [])

                pdf.set_font("Arial", style="B", size=10)
                pdf.cell(0, 6, f"Vulnerability: {name}", ln=True)
                pdf.set_font("Arial", size=10)
                pdf.cell(0, 6, f"Severity: {severity}", ln=True)
                if desc:
                    pdf.multi_cell(0, 6, f"Description: {desc}")

                for ref in references:
                    url = ref.get("url")
                    if url:
                        pdf.set_font("Arial", style="I", size=9)
                        pdf.multi_cell(0, 5, f"Reference: {url}")

                pdf.ln(4)

            pdf.ln(6)
