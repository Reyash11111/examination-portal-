# Online Examination System - Full Project

A scalable, real-time online examination system with automated evaluation, ML-based performance prediction, anomaly detection, and GenAI assistant for faculty queries.

## 📋 Features

✅ **Real-Time Test Delivery** - Responsive web interface for students  
✅ **API-Based Response Ingestion** - FastAPI backend for exam management  
✅ **Streaming Pipeline** - Real-time response processing  
✅ **Automated Evaluation** - Instant objective question grading  
✅ **ML Analytics** - Performance prediction & anomaly detection  
✅ **GenAI Assistant** - Natural language interface for faculty queries  
✅ **Data Analysis** - Comprehensive statistics and reporting  

## ☁️ AWS Cloud Integration

The system is now integrated with **AWS S3** for persistent cloud storage:
- 📤 **responses.json**: Automatically uploaded to S3 on every submission.
- 📤 **analytics.json**: Automatically uploaded to S3 after ML evaluation.

### Configuration
1. Open the `.env` file in the root directory.
2. Fill in your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `S3_BUCKET_NAME`.
3. The system will automatically use these credentials to sync data with the cloud.

---

## 🗂️ Project Structure

```
examination mini project/
├── backend/              # FastAPI server
│   ├── main.py
│   ├── requirements.txt
│   └── responses.json    (auto-generated)
├── frontend/             # Web interface
│   ├── exam.html
│   ├── app.js
│   └── style.css
├── ml/                   # Machine learning
│   ├── evaluate.py
│   ├── requirements.txt
│   └── analytics.json    (auto-generated)
├── genai/                # GenAI Assistant
│   ├── assistant.py
│   └── requirements.txt
├── streaming/            # Streaming pipeline
│   ├── streaming_pipeline.py
│   └── README.md
├── database/             # Database setup
│   ├── setup.txt
│   └── README.md
├── setup.bat             # Automated setup script
├── README_RUN.txt        # Running instructions
└── README.md             # This file
```

## 🚀 Quick Start

### Step 1: Automated Setup (Recommended)
```bash
# Run the setup script (Windows)
setup.bat
```

This will:
- Create a virtual environment
- Install all dependencies
- Provide instructions for running the system

### Step 2: Manual Setup (If needed)
```bash
# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate

# Install dependencies for each component
cd backend && pip install -r requirements.txt && cd ..
cd ml && pip install -r requirements.txt && cd ..
```

## 🎯 Running the Complete System

### Terminal 1: Start Backend API
```bash
cd backend
python -m uvicorn main:app --reload
```
The API will be available at: **http://localhost:8000**

### Terminal 2: Open Web Interface
```
Open: frontend/exam.html in your browser
Click "Start Exam" to test the student interface
```

### Terminal 3: Run ML Evaluation
```bash
cd ml
python evaluate.py
```
This evaluates student responses and detects anomalies.

### Terminal 4: Use GenAI Assistant
```bash
cd genai
python assistant.py
```
Try these queries:
- "Identify students at risk of failing"
- "Show anomalies"
- "What's the average performance"
- "Summary report"

## 📝 How It Works

### 1. Student Exam Flow
1. Student enters ID and name on the web interface
2. System loads exam questions from API
3. Student answers questions (5-minute timer)
4. Responses are submitted via API to backend
5. Responses are stored and logged for processing

### 2. Automated Evaluation
1. Responses are saved to `backend/responses.json`
2. ML evaluation script reads responses
3. Scores are calculated based on correct answers
4. Anomalies are detected (suspicious answer patterns)
5. Analytics are saved to `ml/analytics.json`

### 3. GenAI Assistant
1. Faculty queries are processed in natural language
2. System fetches data from analytics
3. Intelligent responses identify at-risk students, anomalies, etc.

## 🔑 Key Endpoints

### API Endpoints

**Get Exam**
```
GET /exam/{exam_id}
Returns: { id, title, questions[] }
```

**Submit Response**
```
POST /response
Body: { student_id, exam_id, answers }
Returns: { status: "received" }
```

**Get Responses**
```
GET /responses/{exam_id}
Returns: Array of student responses
```

## 📊 Sample Exam

The system comes with a sample exam (3 questions):
- **Q1**: What is the capital of France? (Answer: Paris)
- **Q2**: 2 + 2 = ? (Answer: 4)
- **Q3**: Which planet is known as the Red Planet? (Answer: Mars)

## 🔧 Configuration

### Pass Mark
Edit `ml/evaluate.py` to change the pass mark:
```python
PASS_MARK = 2  # Change to desired value (out of 3)
```

### API Port
Edit `backend/main.py` to change the port:
```bash
# Default: localhost:8000
python -m uvicorn main:app --port 8080 --reload
```

### Exam Duration
Edit `frontend/app.js` to change exam timer (in seconds):
```javascript
startTimer(300);  // Change 300 to desired seconds
```

## 📈 Data Files

### backend/responses.json
Stores all student responses:
```json
{
  "sample": [
    {
      "student_id": "STU123",
      "exam_id": "sample",
      "answers": { "q1": "Paris", "q2": "4", "q3": "Mars" }
    }
  ]
}
```

### ml/analytics.json
Stores evaluation results:
```json
{
  "sample": [
    {
      "student_id": "STU123",
      "score": 3,
      "total": 3,
      "percentage": 100.0,
      "at_risk": false,
      "anomaly": false
    }
  ]
}
```

## ⚠️ Troubleshooting

### API Connection Error
- Ensure backend is running: `python -m uvicorn backend.main:app --reload`
- Check port 8000 is not blocked
- Use correct IP if running on different machine

### Module Not Found
- Install missing packages: `pip install -r requirements.txt`
- Ensure you're in the correct directory
- Check Python version (3.9+ required)

### No Analytics Data
- Submit at least one exam response first
- Run `python ml/evaluate.py` to generate analytics
- Check `ml/analytics.json` exists

## 🎓 Example Workflow

1. **Start all components** (4 terminals as shown above)
2. **Take exam as student**:
   - Open frontend/exam.html
   - Enter ID: STU001, Name: John Doe
   - Answer questions
   - Submit
3. **Evaluate responses**:
   - Run `python ml/evaluate.py`
   - Check `backend/responses.json` and `ml/analytics.json`
4. **Query with GenAI**:
   - Run `python genai/assistant.py`
   - Ask: "Identify students at risk of failing"
   - View results

## 🔮 Future Enhancements

- Real database (MongoDB, PostgreSQL)
- Apache Kafka for streaming
- Advanced ML models (Random Forest, Neural Networks)
- OpenAI integration for GenAI
- User authentication
- Question image support
- Proctoring features
- Mobile app

## 📞 Support

For issues or questions:
1. Check logs in terminal output
2. Verify all components are running
3. Check file permissions
4. Ensure Python 3.9+ is installed

## 📄 License

This project is provided as-is for educational purposes.

---

**Happy Examining! 📚**
