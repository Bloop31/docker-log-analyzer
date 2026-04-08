from fastapi import FastAPI, UploadFile, File, HTTPException
from collections import Counter

app = FastAPI()

@app.post("/analyze")
async def analyze_log(file: UploadFile = File(...)):
    try:
        content = await file.read()
        if not content:
            raise HTTPException(status_code=400, detail="Empty file")
        text = content.decode("utf-8", errors="ignore")
        lines = [line for line in text.split("\n") if line.strip()]
        num_lines = len(lines)
        error_count = sum(1 for line in lines if "error" in line.lower())
        words = text.split()
        most_common = Counter(words).most_common(1)
        return {
            "total_lines": num_lines,
            "error_lines": error_count,
            "most_common_word": most_common[0][0] if len(most_common) > 0 else None
        }
    except Exception as e:
        return {"error": str(e)}