# 🎓 Online Examination System - Complete Setup & Running Guide

## ✅ Project Status
Your complete scalable online examination system is **READY TO RUN**!

---

## 📦 What's Included

### ✓ Backend API (FastAPI)
- Exam delivery endpoints
- Student response ingestion
- CORS-enabled for frontend communication
- JSON-based data persistence
- **Status:** Running on http://localhost:8000

### ✓ Student Web Interface
- Beautiful, responsive exam portal
- Real-time question delivery
- 5-minute timer
- Form validation & submission
- **File:** `frontend/exam.html`

### ✓ Faculty Dashboard
- Analytics visualization
- GenAI query interface
- Performance statistics
- Detailed student reports
- **File:** `frontend/faculty_dashboard.html`

### ✓ ML Evaluation Pipeline
- Automated scoring
- Anomaly detection
- At-risk student identification
- Performance statistics
- **File:** `ml/evaluate.py`

### ✓ GenAI Assistant
- Natural language query processing
- Risk identification
- Anomaly reporting
- Summary generation
- **File:** `genai/assistant.py`

---

## 🚀 How to Run Everything

### **Option 1: Quick Demo (Immediate Results)**

Run this command in your project root to see the entire system working:

```bash
C:/Users/Reyash/AppData/Local/Programs/Python/Python39/python.exe demo.py
```

**What You'll See:**
- Sample exam loaded
- 3 student responses simulated
- ML evaluation results
- GenAI assistant responses

---

### **Option 2: Full System (4 Components)**

#### **Terminal 1: Backend API** (START FIRST)
```bash
cd backend
C:/Users/Reyash/AppData/Local/Programs/Python/Python39/python.exe -m uvicorn main:app --reload
```
✓ **Result:** API available at `http://localhost:8000`

#### **Terminal 2: Student Web Interface** (After Backend Starts)
```
1. Double-click: frontend/exam.html
   OR
2. Open in browser: file:///C:/Users/Reyash/Desktop/examination%20mini%20project/frontend/exam.html
```

✓ **Steps:**
- Enter Student ID: `STU001`
- Enter Name: `John Doe`
- Answer 3 questions
- Submit exam

#### **Terminal 3: ML Evaluation**
```bash
cd ml
C:/Users/Reyash/AppData/Local/Programs/Python/Python39/python.exe evaluate.py
```
✓ **Result:** Generates `ml/analytics.json` with results

#### **Terminal 4: GenAI Assistant**
```bash
cd genai
C:/Users/Reyash/AppData/Local/Programs/Python/Python39/python.exe assistant.py
```
✓ **Try These Queries:**
```
Ask a question (or 'quit' to exit): Identify students at risk
Ask a question (or 'quit' to exit): Show anomalies
Ask a question (or 'quit' to exit): Summary report
Ask a question (or 'quit' to exit): Average performance
```

#### **Terminal 5 (Optional): Faculty Dashboard**
```
Double-click: frontend/faculty_dashboard.html
```
- View real-time analytics
- Ask questions via web interface

---

## 📊 Sample Exam Included

The system comes with a ready-to-use sample exam:

| Question | Options | Answer |
|----------|---------|--------|
| What is the capital of France? | Paris, London, Berlin, Rome | Paris |
| 2 + 2 = ? | 3, 4, 5, 6 | 4 |
| Which planet is red? | Earth, Mars, Jupiter, Venus | Mars |

---

## 📁 Key Files Generated

After running the system, you'll find:

### `backend/responses.json`
Stores all student answers:
```json
{
  "sample": [
    {
      "student_id": "STU001",
      "answers": {"q1": "Paris", "q2": "4", "q3": "Mars"}
    }
  ]
}
```

### `ml/analytics.json`
Stores evaluation results:
```json
{
  "sample": [
    {
      "student_id": "STU001",
      "score": 3,
      "percentage": 100.0,
      "at_risk": false,
      "anomaly": false
    }
  ]
}
```

---

## 🔌 API Endpoints

### Create/Get Exam
```bash
GET http://localhost:8000/exam/sample
```

### Submit Response
```bash
POST http://localhost:8000/response
Content-Type: application/json

{
  "student_id": "STU001",
  "exam_id": "sample",
  "answers": {
    "q1": "Paris",
    "q2": "4",
    "q3": "Mars"
  }
}
```

### Get All Responses
```bash
GET http://localhost:8000/responses/sample
```

### API Documentation
```
http://localhost:8000/docs       (Swagger UI)
http://localhost:8000/redoc      (ReDoc)
```

---

## 🎯 Workflow Example

### Complete Workflow (5 minutes)

1. **Open Terminal 1** → Start Backend
   ```
   cd backend
   python -m uvicorn main:app --reload
   ```
   ✓ Wait for "Uvicorn running on..."

2. **Open Terminal 2** → Open Frontend
   ```
   frontend/exam.html in your browser
   ```

3. **Take Exam as Student**
   - ID: STU001
   - Name: John Doe
   - Answer questions
   - Click Submit

4. **Open Terminal 3** → Run ML Evaluation
   ```
   cd ml
   python evaluate.py
   ```

5. **Open Terminal 4** → Query with GenAI
   ```
   cd genai
   python assistant.py
   ```
   - Ask: "Identify students at risk"

6. **Faculty Dashboard** (Optional)
   ```
   frontend/faculty_dashboard.html
   ```

---

## ⚙️ Configuration Options

### Change Exam Duration (in seconds)
**File:** `frontend/app.js` (Line 73)
```javascript
startTimer(300);  // Change 300 to desired seconds
```

### Change Pass Mark (out of 3)
**File:** `ml/evaluate.py` (Line 13)
```python
PASS_MARK = 2  # Change to desired value
```

### Change API Port
**File:** Terminal command
```bash
python -m uvicorn main:app --port 9000 --reload
```

---

## 🐛 Troubleshooting

### "Connection Refused" Error
**Solution:** Make sure backend is running (Terminal 1)
```bash
cd backend
python -m uvicorn main:app --reload
```

### "Module not found" Error
**Solution:** Install packages
```bash
pip install -r backend/requirements.txt
pip install -r ml/requirements.txt
```

### No Analytics in Dashboard
**Solution:** 
1. Submit at least one exam response first
2. Run `python ml/evaluate.py`
3. Check that `ml/analytics.json` was created

### Port 8000 Already in Use
**Solution:** Use a different port
```bash
python -m uvicorn main:app --port 8001 --reload
```
Then update `frontend/app.js`:
```javascript
const API_URL = 'http://localhost:8001';  // Change port
```

---

## 📚 File Structure

```
examination mini project/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── requirements.txt
│   └── responses.json          (auto-created)
├── frontend/
│   ├── exam.html               # Student exam interface
│   ├── faculty_dashboard.html  # Faculty interface
│   ├── app.js
│   └── style.css
├── ml/
│   ├── evaluate.py             # ML scoring & analysis
│   └── analytics.json          (auto-created)
├── genai/
│   └── assistant.py            # GenAI query processor
├── streaming/
│   └── streaming_pipeline.py
├── database/
│   └── setup.txt
├── demo.py                     # Full system demo
├── setup.bat                   # Windows setup script
└── README.md                   # This file
```

---

## 🔮 Advanced Usage

### Create Custom Exam via API

```bash
# POST to create new exam
curl -X POST http://localhost:8000/exam \
  -H "Content-Type: application/json" \
  -d '{
    "id": "math101",
    "title": "Mathematics Quiz",
    "questions": [
      {
        "id": "q1",
        "text": "What is 5 + 5?",
        "options": ["8", "10", "12", "15"],
        "answer": "10"
      }
    ]
  }'
```

### Automated Testing

```bash
# Run demo for automated testing
python demo.py
```

---

## 🎓 Learning Resources

### Understanding the Architecture

1. **API Layer** (`backend/main.py`)
   - FastAPI for REST endpoints
   - CORS enabled for frontend

2. **Streaming** (`streaming/streaming_pipeline.py`)
   - Watches for new responses
   - Processes in real-time

3. **ML Pipeline** (`ml/evaluate.py`)
   - Scores responses
   - Detects anomalies
   - Identifies at-risk students

4. **AI Assistant** (`genai/assistant.py`)
   - Natural language queries
   - Intelligent responses

---

## 📞 Support & Documentation

- **Main README:** `README.md` - Full technical documentation
- **API Docs:** `http://localhost:8000/docs` (when running)
- **Faculty Guide:** `frontend/faculty_dashboard.html`
- **Student Guide:** `frontend/exam.html`

---

## ✨ Summary

Your examination system is **100% ready to use**!

### Quick Start (Pick One):
1. **See it working immediately:** `python demo.py`
2. **Run full system:** Follow "Option 2" above (4 terminals)
3. **Faculty queries only:** `python genai/assistant.py`

### What the System Does:
✅ Delivers exams to students in real-time
✅ Ingests and stores responses via API
✅ Evaluates answers automatically
✅ Detects suspicious patterns
✅ Identifies at-risk students
✅ Answers faculty queries in natural language

---

**Happy Examining! 📚**

For detailed technical docs, see `README.md`.
