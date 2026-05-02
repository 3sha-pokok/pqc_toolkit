import streamlit as st
import json
import pandas as pd
import plotly.express as px
import os

# Page Configuration
st.set_page_config(
    page_title="PQC Migration Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)


def load_results(uploaded_file):
    """Parses uploaded JSON file into Python object."""
    try:
        if uploaded_file is not None:
            return json.load(uploaded_file)
        return None
    except Exception as e:
        st.error(f"Error parsing JSON: {e}")
        return None


def generate_sample_data():
    """Generates mock PQC scan results."""
    return [
        {"asset": "google.com", "type": "TLS", "algorithm": "RSA-2048",
         "risk_score": 7, "status": "Vulnerable",
         "recommendation": "Migrate to ML-KEM-768"},

        {"asset": "internal-vault.local", "type": "SSH",
         "algorithm": "ECDSA-P256", "risk_score": 5,
         "status": "Vulnerable",
         "recommendation": "Migrate to ML-DSA-65"},

        {"asset": "legacy-server.pem", "type": "File",
         "algorithm": "RSA-1024", "risk_score": 10,
         "status": "Critical",
         "recommendation": "Immediate replacement with ML-KEM"},

        {"asset": "modern-gateway.com", "type": "TLS",
         "algorithm": "X25519", "risk_score": 3,
         "status": "Warning",
         "recommendation": "Plan Hybrid X25519 + Kyber"},

        {"asset": "cloud-api.com", "type": "TLS",
         "algorithm": "RSA-4096", "risk_score": 6,
         "status": "Vulnerable",
         "recommendation": "Migrate to ML-KEM-1024"},
    ]


# Sidebar
st.sidebar.header("Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload Scan Results (JSON)", type="json")

if st.sidebar.button("Generate Sample Data"):
    sample_data = generate_sample_data()
    with open("sample_results.json", "w") as f:
        json.dump(sample_data, f)
    st.sidebar.success("Created sample_results.json!")


# Main UI
st.title("🛡️ Post-Quantum Migration Dashboard")
st.markdown("Visualize quantum risk exposure and migration planning.")

data = load_results(uploaded_file)

if data and len(data) > 0:
    df = pd.DataFrame(data)

    # Sidebar filter
    status_filter = st.sidebar.multiselect(
        "Filter by Status",
        options=df['status'].unique(),
        default=df['status'].unique()
    )

    df = df[df['status'].isin(status_filter)]

    # Metrics
    st.subheader("Key Risk Metrics")

    col1, col2, col3 = st.columns(3)

    total_assets = len(df)
    vuln_count = len(df[df['status'].isin(['Vulnerable', 'Critical'])])
    avg_risk = df['risk_score'].mean()

    col1.metric("Total Assets", total_assets)
    col2.metric(
        "Quantum Vulnerable",
        vuln_count,
        delta=f"{(vuln_count/total_assets)*100:.1f}%"
        if total_assets else "0%"
    )
    col3.metric("Average Risk Score", f"{avg_risk:.2f}/10")

    st.divider()

    # Charts
    st.subheader("Risk Distribution")

    viz_col1, viz_col2 = st.columns(2)

    with viz_col1:
        st.markdown("**Status Distribution**")
        fig_pie = px.pie(
            df,
            names='status',
            color='status',
            color_discrete_map={
                'Critical': '#ef4444',
                'Vulnerable': '#f97316',
                'Warning': '#eab308',
                'Safe': '#22c55e'
            }
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with viz_col2:
        st.markdown("**Risk Score per Asset**")
        fig_bar = px.bar(
            df,
            x='asset',
            y='risk_score',
            color='status',
            color_discrete_map={
                'Critical': '#ef4444',
                'Vulnerable': '#f97316',
                'Warning': '#eab308',
                'Safe': '#22c55e'
            }
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)

    # Action Plan
    st.subheader("🚀 Migration Action Plan")

    df_sorted = df.sort_values(by='risk_score', ascending=False)

    def risk_label(score):
        if score >= 8:
            return "🔴 Critical"
        elif score >= 5:
            return "🟠 High"
        elif score >= 3:
            return "🟡 Medium"
        else:
            return "🟢 Low"

    for _, row in df_sorted.iterrows():
        with st.expander(f"{row['asset']} | {row['algorithm']} | Risk {row['risk_score']}"):
            st.write(f"**Type:** {row['type']}")
            st.write(f"**Status:** {row['status']}")
            st.write(f"**Risk Level:** {risk_label(row['risk_score'])}")
            st.success(f"**Recommendation:** {row['recommendation']}")

    # Download report
    st.sidebar.download_button(
        "Download CSV Report",
        df.to_csv(index=False),
        "pqc_report.csv",
        "text/csv"
    )

else:
    st.info("Upload a results.json file to begin analysis.")
    st.image(
        "https://via.placeholder.com/800x400?text=Upload+Scan+Results+to+Begin",
        use_container_width=True
    )
