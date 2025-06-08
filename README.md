# ETL Sales Pipeline with Apache Airflow

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline using **Python** and **Apache Airflow**, orchestrated through **Docker**.

---

## 📁 Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/DavidOlmos03/etl_sales_pipeline.git
cd etl-sales-pipeline
```

### 2. Create and activate the Python virtual environment

#### 🔹 On Linux/macOS:

```bash
python3 -m venv ETL_sales
source ETL_sales/bin/activate
```

#### 🔹 On Windows (PowerShell):

```powershell
python -m venv ETL_sales
.\ETL_sales\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Airflow environment

> Make sure you are in the same directory as the `docker-compose.yaml` file.

### 4. Create required folders for Airflow logs and plugins

```bash
mkdir -p airflow/logs airflow/plugins
chmod -R 777 airflow/logs airflow/plugins
```

### 5. Initialize the Airflow database

```bash
docker compose run webserver airflow db init
```

### 6. Create an Airflow admin user (for development/testing)

```bash
docker compose run webserver airflow users create \
  --username test_admin \
  --password test_pass \
  --firstname Test \
  --lastname Admin \
  --role Admin \
  --email test_admin@example.com
```

💡 **Tip:** Use descriptive test credentials in local/dev environments and secure ones in production.

---

### 7. Start the Airflow services

```bash
docker compose up
```

This will launch the following services:
- Airflow webserver (access at `http://localhost:8080`)
- Scheduler
- Postgres (metadata DB)
- Other necessary components defined in `docker-compose.yaml`

---

## ✅ Access Airflow

Once services are running, open your browser and go to:

```
http://localhost:8080
```

Log in with the credentials:

- **Username:** `test_admin`
- **Password:** `test_pass`

---

## 📦 Project Structure (example)

```
.
├── airflow/
│   ├── dags/
│   ├── logs/
│   ├── plugins/ 
│   └── docker-compose.yaml
├── data/
├── requirements.txt
└── README.md
```

---

## 🛠️ Notes

- All Docker-related commands must be run from the directory containing `docker-compose.yaml`.
- For production use, replace test credentials and ensure secure file permissions.
- This setup is intended for development and testing purposes.

---

## 📧 Contact

For questions or contributions, feel free to open an issue or pull request.
