from fpdf import FPDF
import requests
import json

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

    print(data)
    print("DATA")
    print("======================")
    # Provera da li ima hotspotova u odgovoru
    if not data.get("hotspots"):
        print("Nema dostupnih hotspotova.")
        exit()

    # Generisanje PDF-a
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Dodavanje naslova
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

    # Čuvanje PDF-a
    pdf.output("/app/reports/Security_Hotspots_Report.pdf")
    print("PDF generisan: Security_Hotspots_Report.pdf")

except requests.exceptions.RequestException as e:
    print("Greška pri pozivu API-ja:")
    print(e)

except Exception as e:
    print("Greška prilikom generisanja PDF-a:")
    print(e)
