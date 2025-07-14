from generators.pdf_generator import PDFGenerator
from generators.zap_generator import ZapSectionGenerator
from generators.dependecy_generator import DependencyCheckSectionGenerator
from generators.sonarqube_generator import SonarQubeSectionGenerator
import json
import requests

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
        dependency_data = dependency_data.get("dependencies", [])
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
    #   # API poziv za dobavljanje podataka
    # response = requests.get(url, params=params, auth=auth)

    # # Provera statusnog koda
    # if response.status_code != 200:
    #     print(f"Greška pri pozivu API-ja: {response.status_code}")
    #     print(response.text)
    #     exit()

    # # Parsiranje odgovora
    # data = response.json()

    # # Provera da li ima hotspotova u odgovoru
    # if not data.get("hotspots"):
    #     print("Nema dostupnih hotspotova.")
    #     exit()
    # print(data)

    # Generators
    pdf_gen = PDFGenerator(language='en')
    full_zap_gen = ZapSectionGenerator(scan_data=full_scan_zap_data)
    api_zap_gen = ZapSectionGenerator(scan_data=full_scan_zap_data)
    #sonar_gen = SonarQubeSectionGenerator(issues=data)
    dependency_gen = DependencyCheckSectionGenerator(dependencies=dependency_data)

    #Register section generators
    #pdf_gen.add_part(sonar_gen.generate, title=pdf_gen.translate['sonarqube_title'])
    pdf_gen.add_part(full_zap_gen.generate, title=pdf_gen.translations['zap_full_scan_title'])
    pdf_gen.add_part(api_zap_gen.generate, title=pdf_gen.translations['zap_api_scan_title'])
    pdf_gen.add_part(dependency_gen.generate, title=pdf_gen.translations['dependency_check_title'])
    pdf_gen.generate("/app/reports/REPORT.pdf")
    print("Report generated")

except Exception as e:
    print("Greška prilikom generisanja PDF-a:")
    print(e.with_traceback())
