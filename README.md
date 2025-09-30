# Data-Science-Project

# IT Support Ticket Resolution Predictor

This project predicts the resolution time for IT support tickets and groups them into clusters for better analysis. 
It combines machine learning (regression) for prediction and unsupervised learning (clustering) for insights. 
A Streamlit dashboard is included to visualize and interact with the data.


## 📂 Project Flow

1. **Data Collection**

   * Input data comes from an IT helpdesk system containing ticket details such as queue, software, hardware, assigned staff, and resolution time.

2. **Data Preprocessing**

   * Missing values in the target column are removed.
   * Categorical fields are encoded into numeric values using Label Encoding.

3. **Clustering**

   * Ticket data is standardized and grouped into 3 clusters using KMeans.
   * Helps to identify patterns in ticket categories and resolution trends.

4. **Dashboard (Streamlit)**

   * Interactive visualizations of resolution times, clusters, and queues.
   * Users can upload new data and get prediction results.

## 📸 Sample Outputs

<img width="811" height="786" alt="image" src="https://github.com/user-attachments/assets/8cbb6872-138e-4116-83ed-3b94dfd5b6db" />

<img width="812" height="630" alt="image" src="https://github.com/user-attachments/assets/5027ea37-e712-428a-b2b6-9c3bc189dd42" />




## 🛠️ Dependencies

Install the following packages before running the project:

pip install streamlit pandas plotly scikit-learn seaborn matplotlib joblib openpyxl

## ▶️ How to Run

1. Clone or download this project.
2. Place your dataset (`helpdesk_with_user_staff.xlsx`) in the root folder.
3. Train the model and preprocess data:

   ```bash
   python app.py
   ```
4. Launch the dashboard:

   ```bash
   streamlit run app.py
   ```

---

