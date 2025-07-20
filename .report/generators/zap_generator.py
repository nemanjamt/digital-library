from fpdf import FPDF
from generators.common import HTMLTextExtractor as html_te

class ZapSectionGenerator:
    def __init__(self, scan_data):
        self.scan_data = scan_data
        self.sites = scan_data.get("site",[])

    def generate(self, pdf: FPDF): 
        alerts_per_site = {
            site.get("@name", "unknown"): site.get("alerts", [])
            for site in self.sites
        }

        for site_name, alerts in alerts_per_site.items():
            if not alerts:
                continue

            pdf.set_font("Arial", style="B", size=13)
            pdf.cell(0, 10, f"Site: {site_name}", ln=True)
            pdf.ln(2)

            for idx, alert in enumerate(alerts, 1):
                title = html_te.strip_html(alert.get('name', 'Unknown'))
                severity = alert.get("riskdesc", "")
                confidence = alert.get("confidence", "")
                plugin_id = alert.get("pluginid", "")
                alert_ref = alert.get("alertRef", "")
                cwe = alert.get("cweid", "")
                wasc = alert.get("wascid", "")

                pdf.set_font("Arial", style="B", size=11)
                pdf.cell(0, 8, f"Alert {idx}: {title}", ln=True)

                pdf.set_font("Arial", size=10)
                pdf.cell(0, 6, f"Risk: {severity} | Confidence: {confidence} | PluginID: {plugin_id} | Ref: {alert_ref}", ln=True)
                if cwe and cwe != "-1":
                    pdf.cell(0, 6, f"CWE ID: {cwe}", ln=True)
                if wasc and wasc != "-1":
                    pdf.cell(0, 6, f"WASC ID: {wasc}", ln=True)

                desc = html_te.strip_html(alert.get("desc", ""))
                if desc:
                    pdf.multi_cell(0, 5, f"Description: {desc}")
                solution = html_te.strip_html(alert.get("solution", ""))
                if solution:
                    pdf.multi_cell(0, 5, f"Solution: {solution}")

                references = html_te.strip_html(alert.get("reference", ""))
                if references:
                    pdf.multi_cell(0, 5, f"References: {references}")

                # Compact instance listing
                instances = alert.get("instances", [])
                if instances:
                    pdf.set_font("Arial", style="I", size=9)
                    pdf.cell(0, 6, "Instances:", ln=True)
                    for i, inst in enumerate(instances[:3], 1):
                        uri = inst.get("uri", "")
                        method = inst.get("method", "")
                        param = inst.get("param")
                        evidence = inst.get("evidence")
                        otherinfo = html_te.strip_html(inst.get("otherinfo", ""))

                        line = f" - {uri} [{method}]"
                        if param:
                            line += f" param: {param}"
                        if evidence:
                            line += f" | evidence: {evidence}"
                        pdf.multi_cell(0, 5, line)
                        if otherinfo:
                            pdf.multi_cell(0, 5, f"   info: {otherinfo}")

                    if len(instances) > 3:
                        pdf.cell(0, 5, f"...and {len(instances) - 3} more instances", ln=True)

                pdf.ln(6)
            pdf.multi_cell(0, 6, f'{self.scan_data.get("@generated")} {self.scan_data.get("@programName")} - {self.scan_data.get("@version")}')
