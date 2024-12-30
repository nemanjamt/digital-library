from fpdf import FPDF
import requests
import json

# Učitavanje ZAP izvještaja iz JSON fajla
try:
    with open("/app/full-scan/reports/zap_report.json", "r") as file:
        full_scan_zap_data = json.load(file)
except FileNotFoundError:
    print("Greška: JSON fajl 'full-scan-zap-report.json' nije pronađen.")
    exit()
except json.JSONDecodeError:
    print("Greška: Neispravan JSON format u fajlu 'full-scan-zap-report.json'.")
    exit()

try:
    with open("/app/api-scan/reports/zap_report.json", "r") as file:
        api_scan_zap_data = json.load(file)
except FileNotFoundError:
    print("Greška: JSON fajl 'zap_report.json' nije pronađen.")
    exit()
except json.JSONDecodeError:
    print("Greška: Neispravan JSON format u fajlu 'full-scan-zap-report.json'.")
    exit()

try:
    with open("/app/dependency-check/dependency-check-report.json", "r") as file:
        dependency_data = json.load(file)
except FileNotFoundError:
    print("Greška: JSON fajl 'dependency-check-report.json' nije pronađen.")
    exit()
except json.JSONDecodeError:
    print("Greška: Neispravan JSON format u fajlu 'dependency-check-report.json'.")
    exit()

# Konfiguracija za API poziv
url = "http://sonarqube:9000/api/hotspots/search"
params = {
    "projectKey": "digital-library",
    "status": "TO_REVIEW"
}
auth = ("admin", "admin")  # Korisničko ime i lozinka

try:
    # API poziv za dobavljanje podataka
    response = requests.get(url, params=params, auth=auth)

    # Provera statusnog koda
    if response.status_code != 200:
        print(f"Greška pri pozivu API-ja: {response.status_code}")
        print(response.text)
        exit()

    # Parsiranje odgovora
    data = response.json()

    # Provera da li ima hotspotova u odgovoru
    if not data.get("hotspots"):
        print("Nema dostupnih hotspotova.")
        exit()

    # Generisanje PDF-a
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Dodavanje naslova za SonarQube izveštaj
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="SonarQube Report - Security HotSpots", ln=True, align='C')
    pdf.ln(10)

    # Iteracija kroz hotspotove i dodavanje detalja
    pdf.set_font("Arial", size=12)
    for idx, hotspot in enumerate(data["hotspots"], start=1):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=f"Hotspot {idx}", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Key: {hotspot['key']}", ln=True)
        pdf.cell(200, 10, txt=f"Component: {hotspot['component']}", ln=True)
        pdf.cell(200, 10, txt=f"Status: {hotspot['status']}", ln=True)
        pdf.cell(200, 10, txt=f"Line: {hotspot['line']}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Message: {hotspot['message']}")
        pdf.cell(200, 10, txt=f"RuleKey: {hotspot['ruleKey']}", ln=True)
        pdf.ln(5)  # Razmak nakon svakog hotspot-a

    # Dodavanje naslova za ZAP Alerts
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Full Scan ZAP Report - Alerts", ln=True, align='C')
    pdf.ln(10)


    full_scan_alerts = [alert for site in full_scan_zap_data.get("site", []) for alert in site.get("alerts", [])]
    
    api_alerts = [alert for site in api_scan_zap_data.get("site", []) for alert in site.get("alerts", [])]
    # Iteracija kroz ZAP alerte i dodavanje detalja
    for idx, alert in enumerate(full_scan_alerts, start=1):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=f"Alert  {str(alert['name'])}", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"PluginID: {str(alert['pluginid'])}", ln=True)
        pdf.cell(200, 10, txt=f"Risk code: {str(alert['riskcode'])}", ln=True)
        pdf.cell(200, 10, txt=f"Confidence: {str(alert['confidence'])}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Risk description: {str(alert['riskdesc'])}")
        pdf.ln(5)  # Razmak nakon svakog alerta
    
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="API Scan ZAP Report - Alerts", ln=True, align='C')
    pdf.ln(10)

    for idx, alert in enumerate(api_alerts, start=1):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=f"Alert  {str(alert['name'])}", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"PluginID: {str(alert['pluginid'])}", ln=True)
        pdf.cell(200, 10, txt=f"Risk code: {str(alert['riskcode'])}", ln=True)
        pdf.cell(200, 10, txt=f"Confidence: {str(alert['confidence'])}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Risk description: {str(alert['riskdesc'])}")
        pdf.ln(5)  # Razmak nakon svakog alerta

    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Dependency check - vulnerabilities", ln=True, align='C')
    pdf.ln(10)

    vulnerabilities = []
    for dependency in dependency_data.get("dependencies", []):
        for vulnerability in dependency.get("vulnerabilities", []):
            vulnerabilities.append({
            "dependency": dependency.get("fileName", "N/A"),
            "name": vulnerability.get("name", "N/A"),
            "severity": vulnerability.get("severity", "N/A"),
            "description": vulnerability.get("description", "N/A"),
            "cwe": vulnerability.get("cwe", "N/A"),
            "cvssScore": vulnerability.get("cvssScore", "N/A")
            })
    
    if not vulnerabilities:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Nisu pronađene ranjivosti u ovom izveštaju.", ln=True, align='L')
    else:
    # Iteracija kroz ranjivosti i dodavanje u PDF
        for idx, vuln in enumerate(vulnerabilities, start=1):
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(200, 10, txt=f"Vulnerability {idx}", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Dependency: {vuln['dependency']}", ln=True)
            pdf.cell(200, 10, txt=f"Name: {vuln['name']}", ln=True)
            pdf.cell(200, 10, txt=f"Severity: {vuln['severity']}", ln=True)
            pdf.cell(200, 10, txt=f"CVSS Score: {vuln['cvssScore']}", ln=True)
            pdf.cell(200, 10, txt=f"CWE: {vuln['cwe']}", ln=True)
            pdf.multi_cell(0, 10, txt=f"Description: {vuln['description']}")
            pdf.ln(5)
    

    # Čuvanje PDF-a
    pdf.output("/app/reports/REPORT.pdf")
    print("PDF generisan: Security_Hotspots_and_ZAP_Alerts_Report.pdf")

except requests.exceptions.RequestException as e:
    print("Greška pri pozivu API-ja:")
    print(e)

except Exception as e:
    print("Greška prilikom generisanja PDF-a:")
    print(e)