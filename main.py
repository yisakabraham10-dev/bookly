from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
async def read_root():
    return{"message": "Hello world"}

    
