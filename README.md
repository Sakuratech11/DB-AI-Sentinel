# 🛡️ Secure AI Database Assistant (DB-AI-Sentinel)

An enterprise-ready, secure interface that enables natural language querying over relational databases using Large Language Models (LLMs), featuring a strict cybersecurity validation layer to prevent SQL injection, privilege escalation, and data leakage.

---

## 🚀 Overview

Integrating AI models directly with production databases poses severe security risks. **DB-AI-Sentinel** acts as an intelligent intermediary proxy:
1. Translates natural language requests into SQL queries via LLM API.
2. Sanitizes and validates the generated SQL against custom cybersecurity rules and Role-Based Access Control (RBAC).
3. Executes safe queries on the relational database and returns optimized results.

---

## 🛠️ Tech Stack & Skills Demonstrated

* **Database Management:** MariaDB / MySQL (Schema design, indexing, query optimization, triggers).
* **Cybersecurity (Cisco Principles):** Input sanitization, SQL injection prevention, RBAC, API key encryption, and audit logging.
* **Artificial Intelligence (Santander AI Frameworks):** LLM integration (Gemini / OpenAI API) for natural language to SQL translation.
* **Backend:** Python (FastAPI / SQLAlchemy).

---

## 📐 Architecture & Security Flow
### Security Guardrails Included:
* **Read-Only Enforcement:** Blocks `DROP`, `DELETE`, `ALTER`, and `TRUNCATE` commands for standard users.
* **Parameterization & Escaping:** Ensures queries adhere to prepared statement structures.
* **Audit Trail:** Logs every attempt and flagged query with timestamps into a secure log table.

---

## ⚡ Quick Start

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sakuratech11/DB-AI-Sentinel.git
   cd DB-AI-Sentinel
