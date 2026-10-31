# 🛡️ UPI Scam Shield - Backend & AI Fraud Detection Engine

An intelligent, real-time security backend built to protect users from payment fraud, phishing links, and malicious QR codes during UPI transactions.

---

## 🌟 Key Features

* **🤖 Machine Learning Risk Scoring:** Leverages an **XGBoost Classifier** to analyze key transaction features (amount, hour of day, VPA age, transaction velocity) and calculate real-time fraud probability scores (0%–100%).
* **⚡ Rule Engine Guardrails:** Evaluates deterministic behavioral rules to immediately flag high-velocity transfers or suspicious new recipient accounts.
* **🔍 QR Code Inspector & Phishing Detector:** Decodes scanned QR code payment payloads and analyzes embedded links for malicious phishing URLs.
* **🚀 FastAPI Backend:** High-performance asynchronous REST API exposed publicly via `ngrok` for seamless web and mobile client integration.

---

## 👤 Team Member Contribution: Member 3 (AI/ML Developer)

As the **AI/ML Developer**, my primary responsibilities and technical implementations include:

* **Machine Learning Model Development:** Trained and deployed the `XGBoost` model (`upi_fraud_model.pkl`) for real-time transaction scoring.
* **Behavioral Pattern Analysis:** Engineered transaction risk detection routines to identify rapid-fire transfer spikes and anomaly vectors.
* **QR & Link Inspection Module:** Implemented `qr_inspector.py` to decode QR payload contents and inspect URLs for spoofed domain structures.
* **Risk Categorization & Human-Readable Output:** Designed logic to translate raw probability scores into actionable risk levels (**LOW**, **MEDIUM**, **HIGH**) paired with detailed risk explanations for the end user.

---

## 📁 Repository Structure

```text
upi.python/
│-- main.py              # FastAPI server & route handles
│-- train_model.py       # XGBoost model training script
│-- rule_engine.py       # Rule-based behavioral check engine
│-- qr_inspector.py      # QR code decoder & link inspection module
│-- upi_fraud_model.pkl  # Serialized XGBoost model binary
│-- README.md            # Project documentation