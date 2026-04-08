# Log Analyzer API (Dockerized)

A lightweight, containerized **log analysis service** built with FastAPI.
This project demonstrates backend API development, file handling, and Docker-based deployment in a clean and reproducible setup.

---

## Overview

The Log Analyzer API allows users to upload plain text log files and extract key insights, including:

* Total number of log entries
* Number of error occurrences
* Most frequently occurring word

The application is designed to be simple, efficient, and easily deployable using Docker.

---

## Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python 3.11
* **Containerization:** Docker

---

## Project Structure

```
log-analyzer/
│
├── app/
│   └── main.py        # Core API logic
│
├── requirements.txt   # Dependencies
├── Dockerfile         # Container configuration
└── README.md
```

---

## Getting Started

### Prerequisites

* Docker installed and running

---

### Build the Docker Image

```bash
docker build -t log-analyzer .
```

---

### Run the Application

```bash
docker run -p 8000:8000 log-analyzer
```

---

### Access the API

Once the container is running, open:

http://localhost:8000/docs

This provides an interactive interface to test the endpoints.

---

## API Reference

### POST `/analyze`

Uploads a log file and returns analysis results.

#### Request

* Content-Type: `multipart/form-data`
* Field: `file` (text file)

#### Response

```json
{
  "total_lines": 4,
  "error_lines": 2,
  "most_common_word": "ERROR"
}
```

---

## Example

### Sample Input

```
INFO server started
ERROR database failed
INFO retrying
ERROR timeout
```

### Sample Output

```json
{
  "total_lines": 4,
  "error_lines": 2,
  "most_common_word": "ERROR"
}
```

---

## Error Handling

* Handles empty or invalid files
* Safely processes encoding issues
* Returns structured error responses

---

## Key Highlights

* Clean and minimal FastAPI implementation
* Fully containerized for portability
* Demonstrates practical file processing
* Easy to extend for real-world use cases

---

## Potential Enhancements

* Structured log parsing (JSON logs)
* Visualization dashboard for analytics
* Integration with databases (PostgreSQL, MongoDB)
* Real-time log ingestion
* Authentication and access control

---

## License

This project is open-source and available for educational and personal use.

---

## Author

Developed as a backend and Docker practice project to demonstrate practical software engineering skills.
