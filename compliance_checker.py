import streamlit as st
import pandas as pd
from fpdf import FPDF

st.set_page_config(page_title="Mini Compliance Checker", page_icon="✅", layout="centered")

st.title("🛡️ Mini Compliance Checker")
st.write("Quickly evaluate basic compliance with ISO 27001, PCI DSS, and FedRAMP controls.")

# Sample control data
controls = [
    {"Framework": "ISO 27001", "Control": "A.10.1", "Description": "Encryption of data at rest", "Expected": "Enabled"},
    {"Framework": "PCI DSS", "Control": "8.3", "Description": "MFA for administrative access", "Expected": "Enabled"},
    {"Framework": "FedRAMP", "Control": "AU-2", "Description": "Enable audit logging", "Expected": "Enabled"},
]

df = pd.DataFrame(controls)

st.write("### Enter your system configuration:")
encryption = st.selectbox("Is encryption enabled?", ["Enabled", "Disabled"])
mfa = st.selectbox("Is MFA enabled?", ["Enabled", "Disabled"])
logging = st.selectbox("Is audit logging enabled?", ["Enabled", "Disabled"])

# User input mapping
user_values = [encryption, mfa, logging]

# Evaluate compliance
results = []
score = 0

for i, row in df.iterrows():
    compliant = row["Expected"] == user_values[i]
    results.append("✅ Compliant" if compliant else "❌ Non-Compliant")
    if compliant:
        score += 1

df["Your Setting"] = user_values
df["Status"] = results

st.write("### Compliance Results:")
st.dataframe(df)

score_percent = (score / len(df)) * 100
st.metric(label="Compliance Score", value=f"{score}/{len(df)}", delta=f"{score_percent:.0f}%")

if score == len(df):
    st.success("✅ Fully Compliant! Great job.")
else:
    st.warning("⚠️ Partial Compliance – Review controls above.")

# --- PDF Generation ---
def generate_pdf(dataframe, score, score_percent):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Compliance Assessment Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Overall Score: {score}/{len(dataframe)} ({score_percent:.0f}%)", ln=True)
    pdf.ln(5)

    # Table header
    pdf.set_font("Arial", "B", 11)
    pdf.cell(30, 10, "Framework", 1)
    pdf.cell(30, 10, "Control", 1)
    pdf.cell(70, 10, "Description", 1)
    pdf.cell(30, 10, "Your Setting", 1)
    pdf.cell(30, 10, "Status", 1)
    pdf.ln()

    # Table data
    pdf.set_font("Arial", "", 10)
    for _, row in dataframe.iterrows():
        pdf.cell(30, 10, row["Framework"], 1)
        pdf.cell(30, 10, row["Control"], 1)
        pdf.cell(70, 10, row["Description"][:35], 1)
        pdf.cell(30, 10, row["Your Setting"], 1)
        pdf.cell(30, 10, row["Status"], 1)
        pdf.ln()

    return pdf.output(dest="S").encode("latin1")

# Button to download PDF
if st.button("📄 Generate Compliance Report (PDF)"):
    pdf_data = generate_pdf(df, score, score_percent)
    st.download_button(
        label="⬇️ Download Compliance Report",
        data=pdf_data,
        file_name="Compliance_Report.pdf",
        mime="application/pdf"
    )
