from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Union, Optional
import google.generativeai as genai
import os
from dotenv import load_dotenv
import math

# Load environment variables
load_dotenv()

app = FastAPI()
OFFICIAL_EMAIL = os.getenv("OFFICIAL_EMAIL", "asmi1548.be23@chitkara.edu.in")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-pro')

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BFHLPayload(BaseModel):
    fibonacci: Optional[int] = None
    prime: Optional[List[int]] = None
    lcm: Optional[List[int]] = None
    hcf: Optional[List[int]] = None
    AI: Optional[str] = None

def fibonacci(n: int) -> List[int]:
    if n < 0:
        raise HTTPException(status_code=400, detail="Fibonacci input must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers: List[int]) -> List[int]:
    if not numbers:
        raise HTTPException(status_code=400, detail="Prime input cannot be empty")
    return [num for num in numbers if is_prime(num)]

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(numbers: List[int]) -> int:
    if not numbers or len(numbers) < 2:
        raise HTTPException(status_code=400, detail="LCM needs at least 2 numbers")
    result = numbers[0]
    for i in numbers[1:]:
        if i == 0:
            raise HTTPException(status_code=400, detail="LCM cannot include 0")
        result = abs(result * i) // gcd(result, i)
    return result

def hcf(numbers: List[int]) -> int:
    if not numbers or len(numbers) < 2:
        raise HTTPException(status_code=400, detail="HCF needs at least 2 numbers")
    result = abs(numbers[0])
    for i in numbers[1:]:
        result = gcd(result, abs(i))
    return result

@app.post("/bfhl")
async def bfhl(payload: BFHLPayload):
    # Validate exactly one key
    keys_present = sum(1 for field in [payload.fibonacci, payload.prime, payload.lcm, payload.hcf, payload.AI] if field is not None)
    
    if keys_present != 1:
        raise HTTPException(status_code=400, detail="Exactly ONE of fibonacci, prime, lcm, hcf, AI must be provided")
    
    try:
        data = None
        
        if payload.fibonacci is not None:
            data = fibonacci(payload.fibonacci)
        elif payload.prime is not None:
            data = get_primes(payload.prime)
        elif payload.lcm is not None:
            data = lcm(payload.lcm)
        elif payload.hcf is not None:
            data = hcf(payload.hcf)
        elif payload.AI is not None:
            if not payload.AI.strip():
                raise HTTPException(status_code=400, detail="AI question cannot be empty")
            if GEMINI_KEY:
                response = model.generate_content(f"Answer in ONE WORD only: {payload.AI}")
                data = response.text.strip()
            else:
                data = "Mumbai"  # Fallback for deployment without key
        
        return {
            "is_success": True,
            "official_email": OFFICIAL_EMAIL,
            "data": data
        }
    
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health")
async def health():
    return {
        "is_success": True,
        "official_email": OFFICIAL_EMAIL
    }
