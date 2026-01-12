from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Performance Lab Backend")

# Enable CORS for our React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, we should specify the React URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "online", "message": "Performance Lab API is running"}

@app.get("/data")
async def get_performance_data():
    """Endpoint to simulate heavy data for testing optimization"""
    return [{"id": i, "value": f"Sample {i}"} for i in range(100)]