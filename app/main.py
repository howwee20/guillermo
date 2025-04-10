from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
import uvicorn # Keep for local running if needed, but not used by Docker CMD
from typing import List # Good practice to import List explicitly
import io # Needed to read UploadFile content

# Initialize the FastAPI app
app = FastAPI(
    title="Guillermo API",
    description="API for multivariate pattern discovery (WIP)",
    version="0.1.0" # Example version
)

# --- ROOT ENDPOINT ---
# Add this function to handle requests to the base URL
@app.get("/")
async def read_root():
    """Provides a simple welcome message for the API root."""
    return {"message": "Welcome to Guillermo API! Use the /analyze endpoint to submit data."}

# --- EXISTING ANALYZE ENDPOINT ---
# Keep your existing /analyze endpoint
@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    """
    Placeholder endpoint to upload a file and get basic info.
    Replace with actual analysis logic later.
    """
    try:
        # Read the uploaded file content directly using io.BytesIO
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))

        # Simulate analysis - replace with real logic later
        # Example: Return basic info about the dataframe
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        mean_values = df.select_dtypes(include=[np.number]).mean().to_dict() # Calculate means

        summary = {
            "filename": file.filename,
            "columns": df.columns.tolist(),
            "shape": df.shape,
            "numeric_columns": numeric_cols,
            "mean_values (numeric only)": mean_values # Example summary stat
        }
        return JSONResponse(content=summary)

    except Exception as e:
        # Return a proper error response
        return JSONResponse(content={"error": f"Failed to process file: {str(e)}"}, status_code=500)

# --- LOCAL DEVELOPMENT RUNNER ---
# This block allows running locally with `python app/main.py`
# It's ignored when running via the Docker CMD `uvicorn main:app...`
if __name__ == "__main__":
    # Defaults for local run, Render uses CMD settings
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
