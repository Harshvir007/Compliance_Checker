Mini Cloud Compliance Checker

Overview

The Mini Cloud Compliance Checker is a lightweight compliance assessment tool that evaluates basic configuration controls against common information security frameworks, including ISO 27001, PCI DSS, and FedRAMP.

It is designed to simulate how compliance automation tools perform control verification and reporting in real-world enterprise environments. The project provides a web-based interface to collect configuration data and generates an automated compliance report in PDF format.

Key Features

Framework-based checks: Validates configurations against selected clauses from ISO 27001, PCI DSS, and FedRAMP.

Interactive UI: Built using Streamlit for quick and intuitive assessment.

Compliance Scoring: Calculates the percentage of compliant controls.

Automated PDF Reporting: Generates downloadable compliance reports summarizing control results.

Extensible Structure: Easily add new frameworks, controls, or input fields as needed.

Tech Stack

Language: Python 3.x

Framework: Streamlit

Libraries:

pandas – data handling and control evaluation

fpdf – PDF report generation

Installation

Clone the repository and install the required dependencies.

git clone https://github.com/yourusername/mini-cloud-compliance-checker.git
cd mini-cloud-compliance-checker
pip install -r requirements.txt


If you don’t have a requirements.txt, you can install dependencies manually:

pip install streamlit pandas fpdf

Usage

Run the application locally with:

streamlit run compliance_checker.py


Once started, open the local URL displayed in the terminal (typically http://localhost:8501) to access the interface.

Select your system’s configuration values (e.g., encryption, MFA, audit logging).

View the compliance results table and overall compliance score.

Generate and download the compliance report in PDF format.

Example Output

Compliance Score: 2/3 (66%)
Report Output:
The generated PDF includes:

Framework name

Control identifier

Control description

Your system configuration

Compliance status (Compliant/Non-Compliant)

File Structure
mini-cloud-compliance-checker/
│
├── compliance_checker.py      # Main application file
├── requirements.txt           # Dependencies list
└── README.md                  # Project documentation

Possible Enhancements

Integration with AWS or Azure APIs for real-time configuration retrieval.

Support for additional frameworks such as NIST 800-53 or HIPAA.

Persistent storage of assessments in a local database.

Role-based access control for multiple users.

Visualization dashboards for compliance trends.

Project Rationale

This project demonstrates practical understanding of compliance control evaluation and automation concepts used in security compliance workflows.
Although lightweight, it reflects the core logic found in enterprise-grade solutions used for continuous compliance monitoring and audit preparation.

License

This project is released under the MIT License. You are free to modify and distribute it with attribution.
