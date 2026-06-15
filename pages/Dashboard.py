import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Churn Analytics",
        layout="wide"
        )
st.title("📊 Customer Churn Analytics Dashboard")
df = pd.read_csv(
            "WA_Fn-UseC_-Telco-Customer-Churn.csv"
            )

df["TotalCharges"] = pd.to_numeric(

df["TotalCharges"],
                    errors="coerce")
df["TotalCharges"].fillna(
df["TotalCharges"].median(),
                            inplace=True
                            )

                            # KPIs

total_customers = len(df)

churned = len(
                                df[df["Churn"] == "Yes"]
                                )

churn_rate = round(
                                    churned / total_customers * 100,
                                        2
                                        )

retention_rate = round(
                                            100 - churn_rate,
                                                2
                                                )
revenue = round(
                                                    df["TotalCharges"].sum(),
                                                        2
                                                        )

avg_monthly = round(
                                                            df["MonthlyCharges"].mean(),
                                                                2
                                                                )
col1,col2,col3,col4,col5 = st.columns(5)

col1.metric(
                                                                    "Customers",
                                                                        total_customers
                                                                        )
col2.metric(
                                                                            "Churn Rate",
                                                                                f"{churn_rate}%"
                                                                                )
col3.metric(
                                                                                    "Retention",
                                                                                        f"{retention_rate}%"
                                                                                        )

col4.metric(
                                                                                            "Revenue",
                                                                                                f"${revenue:,.0f}"
                                                                                                )
col5.metric(
                                                                                                    "Avg Monthly",
                                                                                                        f"${avg_monthly}"
                                                                                                        )
st.divider()

                                                                                                        # Row 2
c1,c2 = st.columns(2)
with c1:

                                                                                                            churn = df["Churn"].value_counts()

fig = px.pie(
                                                                                                                        names=churn.index,
                                                                                                                                values=churn.values,
                                                                                                                                        title="Customer Churn Distribution"
                                                                                                                                            )

st.plotly_chart(
                                                                                                                                                        fig,
                                                                                                                                                                use_container_width=True
                                                                                                                                                                    )
with c2:

                                                                                                                                                                        fig = px.histogram(
                                                                                                                                                                                df,
                                                                                                                                                                                        x="Contract",
                                                                                                                                                                                                color="Churn",
                                                                                                                                                                                                        title="Contract Type Analysis"
                                                                                                                                                                                                            )

st.plotly_chart(
                                                                                                                                                                                                                        fig,
                                                                                                                                                                                                                                use_container_width=True
                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                    # Row 3

c3,c4 = st.columns(2)
with c3:

                                                                                                                                                                                                                                        fig = px.histogram(
                                                                                                                                                                                                                                                df,
                                                                                                                                                                                                                                                        x="InternetService",
                                                                                                                                                                                                                                                                color="Churn",
                                                                                                                                                                                                                                                                        title="Internet Service vs Churn"
                                                                                                                                                                                                                                                                            )
                                                                                                                                                                                                                                        st.plotly_chart(
                                                                                                                                                                                                                                                                                        fig,
                                                                                                                                                                                                                                                                                                use_container_width=True
                                                                                                                                                                                                                                                                                                    )

with c4:

                                                                                                                                                                                                                                                                                                        fig = px.histogram(
                                                                                                                                                                                                                                                                                                                df,
                                                                                                                                                                                                                                                                                                                        x="PaymentMethod",
                                                                                                                                                                                                                                                                                                                                color="Churn",
                                                                                                                                                                                                                                                                                                                                        title="Payment Method vs Churn"
                                                                                                                                                                                                                                                                                                                                            )

st.plotly_chart(
                                                                                                                                                                                                                                                                                                                                                        fig,
                                                                                                                                                                                                                                                                                                                                                                use_container_width=True
                                                                                                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                                                                                                    # Row 4
c5,c6 = st.columns(2)

with c5:

                                                                                                                                                                                                                                                                                                                                                                        fig = px.box(
                                                                                                                                                                                                                                                                                                                                                                                df,
                                                                                                                                                                                                                                                                                                                                                                                        x="Churn",
                                                                                                                                                                                                                                                                                                                                                                                                y="MonthlyCharges",
                                                                                                                                                                                                                                                                                                                                                                                                        title="Monthly Charges Analysis"
                                                                                                                                                                                                                                                                                                                                                                                                        st.plotly_chart(
                                                                                                                                                                                                                                                                                                                                                                                                                        fig,
                                                                                                                                                                                                                                                                                                                                                                                                                                use_container_width=True
                                                                                                                                                                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                                                                                                                                                                    with c6:

                                                                                                                                                                                                                                                                                                                                                                                                                                        revenue_df = (
                                                                                                                                                                                                                                                                                                                                                                                                                                                df.groupby("Contract")
                                                                                                                                                                                                                                                                                                                                                                                                                                                        ["TotalCharges"]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                .sum()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        .reset_index()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                fig = px.bar(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        revenue_df,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                x="Contract",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        y="TotalCharges",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                title="Revenue by Contract"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        st.plotly_chart(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                fig,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        use_container_width=True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            # Row 5

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            fig = px.histogram(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                df,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x="tenure",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        color="Churn",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            title="Customer Tenure Distribution"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            st.plotly_chart(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                fig,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    use_container_width=True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    # Customer Data

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    st.subheader("Customer Dataset")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    st.dataframe(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        df.head(100),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                use_container_width=True)