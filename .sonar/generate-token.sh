#!/bin/bash

set -e

SONARQUBE_URL="http://sonarqube:9000"
TOKEN_NAME="my-token"
SONAR_USER="admin"
SONAR_PASS="admin"
MAX_RETRIES=60
WAIT_SECONDS=5

echo "Waiting for SonarQube to be UP..."

for i in $(seq 1 "$MAX_RETRIES"); do
  RESPONSE=$(curl -s "$SONARQUBE_URL/api/system/status")
  if echo "$RESPONSE" | grep -q '"status":"UP"'; then
    echo "SonarQube is UP!"
    break
  fi

  echo "[$i/$MAX_RETRIES] SonarQube not ready yet — status: $RESPONSE"
  sleep "$WAIT_SECONDS"
done

echo "Checking for existing token '$TOKEN_NAME'..."
EXISTING_TOKEN_RESPONSE=$(curl -s -u $SONAR_USER:$SONAR_PASS "$SONARQUBE_URL/api/user_tokens/search")

if echo "$EXISTING_TOKEN_RESPONSE" | grep -q "\"name\":\"$TOKEN_NAME\""; then
  echo "Token '$TOKEN_NAME' already exists. Deleting..."
  curl -s -u $SONAR_USER:$SONAR_PASS -X POST "$SONARQUBE_URL/api/user_tokens/revoke" -d "name=$TOKEN_NAME"
fi

echo "Generating new token '$TOKEN_NAME'..."
TOKEN_RESPONSE=$(curl -s -u $SONAR_USER:$SONAR_PASS -X POST "$SONARQUBE_URL/api/user_tokens/generate" -d "name=$TOKEN_NAME")

TOKEN=$(echo "$TOKEN_RESPONSE" | grep -o '"token":"[^"]*"' | awk -F: '{print $2}' | tr -d '"')
if [ -z "$TOKEN" ]; then
  echo "Failed to generate token. Response: $TOKEN_RESPONSE"
  exit 1
fi
echo "Token generated successfully: $TOKEN_NAME"

export SONAR_TOKEN="$TOKEN"

echo "Running SonarScanner..."
/opt/sonar-scanner/bin/sonar-scanner -Dsonar.token="$TOKEN"
SCANNER_EXIT_CODE=$?

if [ $SCANNER_EXIT_CODE -eq 0 ]; then
  echo "SonarScanner completed successfully."
  touch /.done/sonarscanner.done
else
  echo "SonarScanner failed with exit code $SCANNER_EXIT_CODE."
  exit $SCANNER_EXIT_CODE
fi