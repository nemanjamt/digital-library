#!/bin/sh
# Run ZAP API scan
echo "############################################"
echo "Starting ZAP API scan"
python zap-api-scan.py -r reports/digital-library-app_api-scan_report_$(date +%Y_%m_%d_%H_%M).html -t http://digital-library-app:3000/openapi.json -f openapi -g gen_file_api_scan  2>> error_api_scan.log
echo "############################################"