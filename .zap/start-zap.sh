#!/bin/sh

# Run ZAP API scan
echo "############################################"
echo "Starting ZAP API scan"
python zap-api-scan.py \
    -t http://digital-library-app:3000/openapi.json \
    -f openapi \
    -g gen_file_api_scan \
    -r reports/digital-library-app_api-scan_report_$(date +%Y_%m_%d_%H_%M).html 2>> error_api_scan.log
api_scan_exit=$?
echo "ZAP API scan completed"
echo "############################################"
# Run ZAP Full scan
echo "Starting ZAP Full scan"
python zap-full-scan.py \
    -r reports/digital-library-app_full-scan_report_$(date +%Y_%m_%d_%H_%M).html \
    -t http://digital-library-app:3000/ \
    -g gen_file_full_scan 2>> error_full_scan.log
full_scan_exit=$?
echo "ZAP Full scan completed"
echo "############################################"

# Exit the container with the appropriate status
if [ $api_scan_exit -ne 0 ] || [ $full_scan_exit -ne 0 ]; then
    echo "One or both scans failed."
    exit 1
else
    echo "Both scans completed successfully."
    exit 0
fi
