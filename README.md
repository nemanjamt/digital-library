# digital-library
A project intended for the university course Cyber Security

Use following command to start application/pipeline: <br>
docker-compose -f .deploy/docker-compose.yml up


### SonarQube and SonarScanner
After starting Docker Compose and completing the pipeline, the message in the console should look like this
![image](https://github.com/user-attachments/assets/21606ffe-fd5b-464f-804c-f8053af9e306)

We can visit address http://localhost:9000 in browser with credentials <br>
username: admin <br>
password: admin <br>
and then change default password <br> <br>
After that we can visit http://localhost:9000/dashboard?id=digital-library 
<br><br>
The following image presents an overview of the analysis report <br>
![image](https://github.com/user-attachments/assets/fec193d6-3036-48f3-8f50-d80d36a09e41)
<br><br><br>
Details about code smells<br>
![image](https://github.com/user-attachments/assets/bfaabb82-ef2f-4c0d-9a77-4be87f9a1310)


<br><br><br>
Details about security hotspots<br>
![image](https://github.com/user-attachments/assets/4c5abbe1-96d9-4afc-9bf5-86e8bb6dbc35)

