from fastapi import FastAPI, HTTPException
from functools import lru_cache

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Ctrl T"}

# memoize
@lru_cache(maxsize=None, typed=False)
def magic_math(N: int) -> int:
    if N < 0:
        raise ValueError("N must be a non-negative integer.")
    if N == 0:
        return 0
    if N == 1:
        return 1
    return magic_math(N - 1) + magic_math(N - 2) + N


# to take inputs for different numbers
@app.get("/magic_math/{N}")
def calculate_magic_math(N: int):
    try:
        result = magic_math(N)
        return {"N": N, "magic_math": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
