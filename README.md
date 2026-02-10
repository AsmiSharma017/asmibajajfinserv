# Chitkara Qualifier 1 API - Asmi Sharma

**Student:** Asmi Sharma  
**Email:** asmi1548.be23@chitkara.edu.in  
**Exam Date:** 10 Feb 2026  
**Status:** COMPLETE - All endpoints working

## API Endpoints

| Method | Endpoint | Description | Example Response |
|--------|----------|-------------|------------------|
| `GET` | `/health` | Health check | `{"is_success":true,"official_email":"asmi1548.be23@chitkara.edu.in"}` |
| `POST` | `/bfhl` | Multi-function API (fibonacci, prime, lcm, hcf, AI) | `{"is_success":true,"official_email":"asmi1548.be23@chitkara.edu.in","data":[0,1,1,2,3,5,8]}` |

## Test Cases (All Passed)

| Input | Expected Output |
|-------|-----------------|
| `{"fibonacci":7}` | `[0,1,1,2,3,5,8]` |
| `{"prime":[2,4,7,9,11]}` | `[2,7,11]` |
| `{"lcm":[12,18,24]}` | `72` |
| `{"hcf":[24,36,60]}` | `12` |
| `{"AI":"What is capital of Maharashtra?"}` | `"Mumbai"` |

## Live Deployment

**Base URL:** https://asmibajajfinserv.vercel.app  
**Health Check:** https://asmibajajfinserv.vercel.app/health  
**BFHL API:** https://asmibajajfinserv.vercel.app/bfhl  (post)

## Tech Stack

- **Runtime:** Node.js + Express.js
- **AI:** Google Gemini API (with fallback)
- **Deployment:** Vercel (Auto-deploy from GitHub)
- **Security:** CORS headers enabled



## Local Setup

```bash
git clone https://github.com/AsmiSharma017/asmibajajfinserv.git
cd asmibajajfinserv
npm install
npm start
