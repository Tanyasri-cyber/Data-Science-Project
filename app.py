
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset and model
df = pd.read_excel("helpdesk_processed_with_clusters.xlsx")
reg = joblib.load("reg_model.pkl")

st.title("📊 IT Support Ticket Resolution Dashboard")

# Show dataset
st.subheader("Ticket Dataset (Preview)")
st.dataframe(df.head())

# Plot resolution time by queue (Box Plot)
fig1 = px.box(df, x="queue", y="ResolutionTime", color="priority", title="Resolution Time by Queue & Priority")
st.plotly_chart(fig1)

# Staff workload (Stacked Bar)
fig2 = px.histogram(df, x="AssignedStaff", color="queue", barmode="stack", title="Workload by Staff & Queue")
st.plotly_chart(fig2)

# Heatmap: Avg Resolution Time by Staff vs Queue
st.subheader("⏱️ Average Resolution Time by Staff & Queue")
pivot_df = df.pivot_table(values="ResolutionTime", index="AssignedStaff", columns="queue", aggfunc="mean", fill_value=0)
fig3, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(pivot_df, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
st.pyplot(fig3)

# Bubble chart: Queue vs Avg Resolution Time
avg_df = df.groupby("queue").agg({"ResolutionTime": "mean", "Cluster": "count"}).reset_index()
fig4 = px.scatter(avg_df, x="queue", y="ResolutionTime", size="Cluster", title="Queue vs Avg Resolution Time (Bubble Size = Ticket Count)")
st.plotly_chart(fig4)

# Prediction section
st.subheader("🔮 Predict Resolution Time")
queue = st.selectbox("Queue", df["queue"].unique())
priority = st.selectbox("Priority", df["priority"].unique())
staff = st.selectbox("AssignedStaff", df["AssignedStaff"].unique())

input_data = pd.DataFrame([[queue, priority, staff]], columns=["queue", "priority", "AssignedStaff"])
pred_time = reg.predict(input_data)[0]

st.success(f"⏳ Predicted Resolution Time: {pred_time:.2f} minutes")
