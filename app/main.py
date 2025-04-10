from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
import uvicorn
from typing import List

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        # Simulate analysis — replace with real logic later
        summary = {
            "columns": df.columns.tolist(),
            "shape": df.shape,
            "mean_values": df.mean(numeric_only=True).to_dict()
        }
        return JSONResponse(content=summary)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
