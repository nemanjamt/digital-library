# Pipeline overview
<br><br><br><br><br><br>
![image](https://github.com/user-attachments/assets/cda0b086-6a32-46ec-9109-16d2c7d1df2e)
<a id="english"></a>
Here is an overview of the pipeline along with the trust zones.
As we can see, the source code serves as both the input to the pipeline and as a trust zone, since it is executed on a separate server.
Many services run in parallel (e.g., dependency-check, build-sign), but some are executed sequentially (e.g., zap-scan, full-api-scan, SonarQube) due to their dependency on the digital-library service.
The report-generate service also waits for these to complete in order to generate the final report.
The signed software is shown on the other side of the trust boundary, as it could potentially be replaced or tampered with.

<a id="srpski"></a>
## Grafički prikaz pipeline-a

Na grafičkom prikazu pipeline-a se mogu uočiti servisi iz docker compose-a, izvorni kod kao ulaz u pipeline,
potpisani softver kao i granice povjerenja predstavljene za iste. Granice povjerenja su definisane za izvorni kod
zbog pokretanja istog na serveru koji bi mogao biti kompromitovan(a čitav pipeline se na primjer izvršio uredno)
ali i za potpisani softver koji bi mogao biti kompromitovan jer se šalje na produkciju i to bi bila posebna zona povjerenja
u odnosu na servise iz docker-compose-a ali i izvorni kod.
