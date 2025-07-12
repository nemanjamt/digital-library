# digital-library
A project intended for the university course Cyber Security. Developed proof of concept pipeline will be described next.

Use following command to start test application and security pipeline: <br>
```bash
docker-compose -f .deploy/docker-compose.yml up
```

## Application documentation
Full documentation can be found inside .docs folder, where each of the pipeline stage is described in detail.

## Intial setup after first run

### SonarQube and SonarScanner
After starting Docker Compose and completing the pipeline, the message in the console should look like this
![image](https://github.com/user-attachments/assets/21606ffe-fd5b-464f-804c-f8053af9e306)

#### Accessing SonarQube's web user interface
We can visit address http://localhost:9000 in browser with credentials <br>
- **username:** admin <br>
- **password:** admin <br>

and then change default password <br> <br>
After that we can visit *http://localhost:9000/dashboard?id=digital-library* for overview of scan or
use API GET request with credentials on path: <br> *http://localhost:9000/api/measures/component?component=digital-libraryt&metricKeys=ncloc,complexity,coverage,bugs,vulnerabilities,code_smells*
<br><br>
The following image presents an overview of the analysis report <br>
![image](https://github.com/user-attachments/assets/fec193d6-3036-48f3-8f50-d80d36a09e41)
<br><br><br>
Details about code smells<br>
![image](https://github.com/user-attachments/assets/bfaabb82-ef2f-4c0d-9a77-4be87f9a1310)


<br><br><br>
Details about security hotspots<br>
![image](https://github.com/user-attachments/assets/4c5abbe1-96d9-4afc-9bf5-86e8bb6dbc35)

<br><br><br>
API response <br>
![image](https://github.com/user-attachments/assets/67b148ff-a7f5-4865-a682-45ca6d55f1b1)
<br><br><br>

### ZAP <br>
After running the pipeline for the first time config files will be generated for ZAP API and Full scan which can be tailored to your need. Files inside .zap folder called gen_file_<type_of_scan> contain default rules which ZAP tool folows. Feel free to adjust them as needed.
ZAP is run automatically when the API is started in docker container and it generates report after the scan in HTML format like on following image <br>
![image](https://github.com/user-attachments/assets/0794d236-5ba3-4cf0-9d25-7786de35f242)

