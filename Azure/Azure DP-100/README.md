# Azure DP-100 Project Repository Overview

This repository showcases practical and certification-aligned projects developed using **Microsoft Azure Machine Learning**, reflecting real-world data science workflows required in the **DP-100: Designing and Implementing a Data Science Solution on Azure** exam. Each project was crafted with an emphasis on reproducibility, scalability, and technical rigor—ideal for both academic and enterprise applications.

---

## 🔗 Projects

### 🧊 [Project 1 - Ice Cream Sales Forecasting](./Project-1/)
An end-to-end regression solution using Azure ML to forecast ice cream sales based on temperature data. It includes:

- A manual ML pipeline built with **Azure ML Designer**
- An automated experiment with **Azure AutoML** for model selection, hyperparameter tuning, and performance comparison
- Key outputs tracked using **MLflow** and reproducible environments via **Conda/YAML**

**Skills Demonstrated:**
- Azure ML Pipelines
- AutoML Experimentation
- Data Preprocessing & Regression
- MLflow Tracking and Evaluation

---

### 🤖 [Project 2 - Scientific RAG Chatbot Using Azure AI Foundry](./Project-2/)
This innovative project implements a **Retrieval-Augmented Generation (RAG)** chatbot using **Azure AI Foundry** and vector embeddings. It enables question answering from **three peer-reviewed scientific articles** on AI and blockchain.

- Built using **Azure Cognitive Search**, **LangChain**, and **GPT-4 via Azure OpenAI**
- Document processing and chunking of PDFs
- Result validation via Azure AI Playground with contextual screenshots

**Skills Demonstrated:**
- Vector Embedding + RAG Architecture
- AI Document Intelligence
- Azure OpenAI & LangChain Integration
- Scientific Data Extraction & NLP

---

## 🚀 Why This Stands Out

### 🎯 **Certification-Oriented**
Each project reflects critical competencies required for the **DP-100 certification**, including model development, evaluation, and deployment in cloud environments.

### 🌐 **Industry-Relevant Topics**
- Demand forecasting with climate data
- Scientific AI chatbots for legal, healthcare, or academic scenarios
- Blockchain for AI transparency—highly aligned with **EU AI Act** and future compliance needs

### 🧠 **Technical Rigor**
- End-to-end ML lifecycle: from dataset ingestion to prediction & monitoring
- Versioned models (`model.pkl`, `MLmodel`)
- Conda-based reproducibility with `conda.yaml` and `requirements.txt`

### 🛠 **Tools & Stack**
- Microsoft Azure ML Studio
- Azure AutoML + MLflow
- Azure AI Foundry (Chat Playground)
- Cognitive Search, LangChain, GPT-4
- Python, Scikit-Learn, XGBoost

### 💼 **Business-Ready Architecture**
- Suitable for real-world deployment via Azure Container Instances or AKS
- Clear outputs and metrics for stakeholders
- PDF-based data pipelines usable in internal knowledge management, research, or compliance bots

---

## 📁 Repository Structure

```
Azure-DP-100/
├── Project-1/              # Ice Cream Forecasting (AutoML + Manual)
│   └── README.md
├── Project-2/              # RAG Chatbot from Scientific Papers
│   └── README.md
└── README.md               # This overview file
```

---

## 📘 Summary of Skills Demonstrated

- Azure ML Designer and AutoML
- Model Evaluation and Deployment
- Azure OpenAI and LangChain RAG Framework
- Scientific Data NLP & Vector Embedding
- MLflow Logging, Conda Environments, YAML Packaging

> This repository was created as part of preparation for the **Microsoft Certified: Azure Data Scientist Associate (DP-100)** certification.

**Author:** André Luiz Cardoso  
**Date:** May 10, 2025  
**Tagline:** *Bridging AI, cloud, and research into real-world applications.*
