# 🛡️ OWASP ZAP Scanning

<a id="english"></a>

Two types of ZAP security scans are performed to analyze vulnerabilities in the app.

## 🔍 1. ZAP API Scan

**Command:**
```bash
python zap-api-scan.py \
  -r reports/digital-library-app_api-scan_report_<timestamp>.html \
  -J reports/zap_report.json \
  -t http://digital-library-app:3000/openapi.json \
  -f openapi \
  -g gen_file_api_scan
```

Targets the OpenAPI specification. Produces HTML and JSON reports. Logs errors to *error_api_scan.log*.

## 🌐 2. ZAP Full Scan
Command:

```bash
python zap-full-scan.py \
  -r reports/digital-library-app_full-scan_report_<timestamp>.html \
  -J reports/zap_report.json \
  -t http://digital-library-app:3000/ \
  -g gen_file_full_scan
```
Crawls and analyzes the full app endpoint. Generates HTML and JSON reports. Logs errors to *error_full_scan.log*.

<br>

# 🛡️ OWASP ZAP skeniranje

<a id="srpski"></a>

Dvostruko ZAP skeniranje se koristi za analizu bezbednosnih ranjivosti aplikacije.

## 🔍 1. ZAP API Skeniranje
Komanda:

```bash
python zap-api-scan.py \
  -r reports/digital-library-app_api-scan_report_<timestamp>.html \
  -J reports/zap_report.json \
  -t http://digital-library-app:3000/openapi.json \
  -f openapi \
  -g gen_file_api_scan
```  
Skenira OpenAPI specifikaciju aplikacije. Generiše HTML i JSON izveštaje. Greške se upisuju u *error_api_scan.log*.

## 🌐 2. ZAP Puno skeniranje
Komanda:

```bash
python zap-full-scan.py \
  -r reports/digital-library-app_full-scan_report_<timestamp>.html \
  -J reports/zap_report.json \
  -t http://digital-library-app:3000/ \
  -g gen_file_full_scan
```
Analizira celu aplikaciju kroz sve dostupne stranice. Generiše HTML i JSON izveštaje.Greške se upisuju u *error_full_scan.log*.

