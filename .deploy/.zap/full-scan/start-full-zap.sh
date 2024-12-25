#!/bin/sh
# Run ZAP Full scan
echo "Starting ZAP Full scan"
echo "############################################"
python zap-full-scan.py -r reports/digital-library-app_full-scan_report_$(date +%Y_%m_%d_%H_%M).html -t http://digital-library-app:3000/ -g gen_file_full_scan 2>> error_full_scan.log
echo "############################################"