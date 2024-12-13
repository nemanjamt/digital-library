#!/bin/bash
curl -u admin:admin -X POST "http://sonarqube:9000/api/user_tokens/generate" \
    -d "name=my-token" | grep -o '"token":"[^"]*"' | awk -F: '{print $2}' | tr -d '"' > /usr/src/sonar_token.txt