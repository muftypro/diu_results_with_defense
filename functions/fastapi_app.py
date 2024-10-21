from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
from mangum import Mangum

app = FastAPI()

# Enable CORS to allow communication with the frontend hosted on Netlify
origins = [
    "https://diu_results_with_defense.netlify.app"  # Replace with your actual Netlify site URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = 'http://software.diu.edu.bd:8006'

# Endpoint to fetch student results
@app.get("/results")
async def fetch_student_results(studentId: str):
    # Example of fetching results from the university API (can be modified)
    response = requests.get(f"{BASE_URL}/result", params={'studentId': studentId})
    return response.json()

# Endpoint to add defense result (optional)
@app.post("/add-defense")
async def add_defense(defenseCGPA: float):
    # Logic to handle defense CGPA addition
    return {"message": f"Defense result with CGPA {defenseCGPA} added successfully."}

# Wrap the FastAPI app with Mangum to handle Lambda requests
handler = Mangum(app)
