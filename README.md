# SentinelIQ | Real-Time AI Incident Station 🛰️

SentinelIQ is an Applied AI platform engineered to aggregate, vectorize, and analyze emergency incidents in the Waterberg region, South Africa.

### 🛠️ Core Capabilities
* **Automated Data Ingestion**: ETL pipeline using `NewsAPI` to process real-time news articles.
* **RAG Architecture**: Retrieval-Augmented Generation system designed to ground LLM responses in verified local news data.
* **Geospatial Intelligence**: `Leaflet.js` dashboard for real-time spatial monitoring.
* **Production API**: High-performance **FastAPI** backend with automated data validation.

### 🔧 Tech Stack
* **Backend**: Python, FastAPI, Pydantic, Uvicorn
* **Frontend**: JavaScript (ES6+), HTML5/CSS3, Leaflet.js
* **Infrastructure**: Production deployment on Render (API) and GitHub Pages (UI)
