# Examination System - Complete Functions Guide

## System Overview
The Examination System is a comprehensive online testing platform with three main components:
1. **Student Portal** - For taking exams
2. **Faculty Portal** - For viewing analytics and student performance
3. **System Control Panel** - For monitoring all running services

---

## Navigation Flow

### Landing Page (landing.html)
**Entry Point:** http://localhost/frontend/landing.html

**Purpose:** Portal selection interface that greets users and directs them to either Student or Faculty portal.

**UI Components:**
- Header with system title and tagline
- Two portal cards (Student & Faculty) with features listed
- Information section explaining system capabilities
- Footer with links to system status

**Functions:**
- None (static selection page)

**Navigation:**
- "Enter Student Portal" → exam.html
- "Enter Faculty Portal" → faculty_dashboard.html
- "System Status" → index.html

---

## STUDENT PORTAL (exam.html + app.js)

### Components & Functions

#### 1. **Test Selection View**
**File:** exam.html (test-selection-section)

**Purpose:** Display available published tests for students to choose from.

**Features:**
- List of available exams
- Test title, description, duration, and question count shown
- Click to select a test

**HTML Structure:**
```html
<div id="test-selection-section" class="card">
  <h2>Available Tests</h2>
  <div id="tests-list">
    <!-- Tests displayed here -->
  </div>
</div>
```

**JavaScript Function:**
```javascript
function selectTest(testId)
```
- **Purpose:** Switch from test selection to student login form
- **Input:** testId (string) - ID of the selected test
- **Process:** 
  - Store selectedTestId globally
  - Hide test selection section
  - Show login section

---

#### 2. **Student Login & Registration**
**File:** exam.html (login-section)

**Purpose:** Collect student information before starting exam.

**Required Fields:**
- Student ID (e.g., STU001)
- Student Name (e.g., John Doe)

**UI Input Elements:**
```html
<input id="student-id" type="text" placeholder="e.g., STU001" required />
<input id="student-name" type="text" placeholder="e.g., John Doe" required />
```

**JavaScript Functions:**

```javascript
async function startExam(e)
```
- **Purpose:** Initialize exam and load questions from backend
- **Input:** Event (form submission)
- **API Call:** GET `http://localhost:8000/exam/{selectedTestId}`
- **Process:**
  1. Get student ID and name from inputs
  2. Validate fields are not empty
  3. Fetch exam from backend API
  4. Render exam questions
  5. Start countdown timer
  6. Hide login section, show exam section
- **Error Handling:** Shows alert if connection fails

```javascript
function goBackToTests()
```
- **Purpose:** Return to test selection screen
- **Process:**
  - Show test selection section
  - Hide login section
  - Reset selectedTestId

---

#### 3. **Exam Display & Taking**
**File:** exam.html (exam-section)

**Purpose:** Display questions and collect student answers.

**Components:**
- Exam title
- Countdown timer (5 minutes for sample exam)
- Multiple-choice questions with radio buttons
- Submit button

**Rendered Structure:**
```html
<div id="exam-header">
  <h2 id="exam-title"></h2>
  <div class="timer">Time: <span id="timer">05:00</span></div>
</div>
<form id="exam-form">
  <div id="exam-content">
    <!-- Questions with options -->
  </div>
  <button type="submit">Submit Quiz</button>
</form>
```

**JavaScript Functions:**

```javascript
function renderExam()
```
- **Purpose:** Convert exam JSON data into HTML questions
- **Input:** Global `exam` object (from API response)
- **Process:**
  1. Set exam title
  2. Loop through questions array
  3. Create question divs with radio button options
  4. Inject into exam-content div
- **Output:** HTML form ready for user interaction

```javascript
function startTimer(seconds)
```
- **Purpose:** Countdown timer that auto-submits when time expires
- **Input:** seconds (number) - Duration in seconds (300 for 5 minutes)
- **Process:**
  1. Calculate minutes and seconds from remaining time
  2. Update timer display every 1 second
  3. Decrement counter
  4. When timer reaches 0:
     - Clear interval
     - Call submitExamAuto() to submit form
- **Display:** Updates `<span id="timer">` in real-time

```javascript
function submitExamAuto()
```
- **Purpose:** Auto-submit exam when time expires
- **Trigger:** Called when timer reaches 0
- **Process:**
  - Get exam form
  - Dispatch submit event
  - Triggers submitExam() function

---

#### 4. **Exam Submission**
**File:** app.js

**JavaScript Function:**

```javascript
async function submitExam(e)
```
- **Purpose:** Submit student answers to backend for evaluation
- **Input:** Event (form submission)
- **Process:**
  1. Prevent default form submission
  2. Stop the timer
  3. Collect all selected answers into answers object:
     ```javascript
     answers = {
       "q1": "Paris",
       "q2": "4",
       "q3": "Mars"
     }
     ```
  4. Make POST request to `http://localhost:8000/response`
  5. Send JSON with student_id, exam_id, and answers
  6. On success: Show result section
  7. On error: Show error message

**Request Body:**
```json
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

**Response:** Success message with submission details

---

#### 5. **Result Display**
**File:** exam.html (result-section)

**Purpose:** Show success message and submission summary.

**Displayed Information:**
- Success message with student name
- Student ID
- Exam title
- Number of questions answered
- Status: "Submitted and processing..."

**Button:** "Take Another Quiz" - Reloads page

---

#### 6. **Error Handling**
**File:** exam.html (error-section)

**Display Cases:**
- Server connection failure
- API errors
- Network timeouts

**Feature:** Shows error message and "Try Again" button to reload

---

## FACULTY PORTAL (faculty_dashboard.html)

### Components & Functions

#### 1. **Quick Statistics**
**File:** faculty_dashboard.html

**Displays:**
- Total Students (count)
- Average Score (percentage)
- At Risk Students (count)
- Anomalies Detected (count)

**UI Structure:**
```html
<div class="stat-box">
  <div class="number" id="stat-students">0</div>
  <div class="label">Total Students</div>
</div>
```

**JavaScript Function:**

```javascript
function loadStats()
```
- **Purpose:** Load and display student statistics
- **Process:**
  1. Update stat boxes with hardcoded values (currently simulated)
  2. Load detailed analytics data
  3. Populate analytics table with student results
- **Data Displayed:**
  - Student ID
  - Score (raw and percentage)
  - At Risk flag (Yes/No)
  - Anomaly detection (Yes/No)

---

#### 2. **GenAI Query Interface**
**File:** faculty_dashboard.html

**Purpose:** Allow faculty to query student analytics using natural language.

**Components:**
- Text input field for queries
- "Send" button
- Quick query buttons with pre-built queries:
  - "Which students are at risk?"
  - "Show anomalies"
  - "Average performance"
  - "Summary report"

**JavaScript Functions:**

```javascript
function submitQuery()
```
- **Purpose:** Process faculty query and generate response
- **Input:** Text from query input field
- **Process:**
  1. Get query text from input
  2. Call generateResponse(query)
  3. Display response in response-area div
  4. Show response section

```javascript
function generateResponse(query)
```
- **Purpose:** Parse Natural Language query and return analytics
- **Input:** query (string) - Faculty's question
- **Logic:** Keyword matching:
  - If query includes "at risk": Returns at-risk students list
  - If query includes "anomal": Returns detected anomalies
  - If query includes "average": Returns average performance
  - If query includes "summary": Returns overall report
  - Default: Generic help message
- **Output:** Formatted response text

```javascript
function setQuery(query)
```
- **Purpose:** Fill query input with quick query and submit
- **Input:** query (string) - Pre-built query text
- **Process:**
  1. Set input value to query
  2. Call submitQuery()

**Query Examples:**
| Query | Response |
|-------|----------|
| "Which students are at risk?" | Lists students with scores < 67% |
| "Show anomalies" | Lists students with suspicious patterns |
| "Average performance" | Shows class average and total students |
| "Summary report" | Provides overall exam statistics |

---

#### 3. **Detailed Analytics Table**
**File:** faculty_dashboard.html

**Display:** Comprehensive student result table with columns:
- Student ID
- Score (e.g., "3/3 (100%)")
- At Risk status (Yes/No)
- Anomaly detection (Yes/No)

**Color Coding:**
- Green text for negative flags (No risk, no anomaly)
- Red text for positive flags (At risk, anomaly detected)

**Function:**

```javascript
function loadStats()
```
- **Sub-task:** Build analytics table
- **Process:**
  1. Create table HTML with sample data
  2. Style rows with alternating background colors
  3. Color-code risk/anomaly cells
  4. Inject into analytics-display div

---

## SYSTEM CONTROL PANEL (index.html)

### Purpose
Monitor all running services and access documentation.

### Components & Functions

**No JavaScript functions required - purely informational page with links.**

#### Displayed Services:
1. **Backend API** - FastAPI server on port 8000
2. **Student Portal** - exam.html
3. **Faculty Dashboard** - faculty_dashboard.html
4. **ML Evaluation** - Automated scoring engine
5. **GenAI Assistant** - Natural language processor
6. **Data Storage** - JSON file persistence

#### Links Provided:
- API Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Start Exam: exam.html
- Faculty Dashboard: faculty_dashboard.html
- Sample Data table showing student results

---

## BACKEND API (main.py)

### Endpoints & Functions

#### 1. **GET /exam/{exam_id}**
**Purpose:** Retrieve exam questions for a specific exam

**Request:**
```
GET http://localhost:8000/exam/sample
```

**Response:**
```json
{
  "id": "sample",
  "title": "General Knowledge Quiz",
  "description": "Test your knowledge",
  "duration": 300,
  "questions": [
    {
      "id": "q1",
      "text": "What is the capital of France?",
      "options": ["Paris", "Lyon", "Marseille", "Nice"]
    }
  ]
}
```

#### 2. **POST /response**
**Purpose:** Submit student answers for evaluation

**Request:**
```json
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

**Response:**
```json
{
  "status": "success",
  "message": "Response recorded",
  "student_id": "STU001"
}
```

**Backend Process:**
1. Save response to backend/responses.json
2. Trigger ML evaluation pipeline
3. Update analytics in ml/analytics.json
4. Return success response

#### 3. **GET /responses/{exam_id}**
**Purpose:** Retrieve all responses for an exam

**Request:**
```
GET http://localhost:8000/responses/sample
```

**Response:**
```json
[
  {
    "student_id": "STU001",
    "exam_id": "sample",
    "answers": {...},
    "timestamp": "2026-02-23T10:30:00"
  }
]
```

---

## ML EVALUATION (evaluate.py)

### Functions

#### 1. **Scoring Function**
**Purpose:** Calculate student score based on correct answers

**Logic:**
- Hard-coded correct answers for sample exam
- Compare student answer with correct answer
- Award 1 point per correct answer
- Calculate percentage: (score / total_questions) * 100

**Sample Answers:**
- Q1 (Capital of France): "Paris"
- Q2 (2+2): "4"
- Q3 (Red planet): "Mars"

#### 2. **At-Risk Identification**
**Criteria:** Student score < 67%

**Example:**
- Score 0/3 (0%) = At Risk
- Score 2/3 (67%) = Not At Risk
- Score 1/3 (33%) = At Risk

#### 3. **Anomaly Detection**
**Detection Methods:**
- **all_correct:** Student answered all questions correctly (possibly cheating)
- **all_wrong:** Student answered all questions incorrectly (possibly not understanding)
- **all_same_answer:** Student selected same option for all questions

#### 4. **Analytics Output**
**File:** ml/analytics.json

**Structure:**
```json
{
  "exam_id": {
    "total_students": 3,
    "average_score": 66.7,
    "students": {
      "STU001": {
        "score": 3,
        "percentage": 100,
        "at_risk": false,
        "anomalies": []
      }
    }
  }
}
```

---

## GENAI ASSISTANT (assistant.py)

### Query Processing

**Supported Query Patterns:**

| Pattern | Response Type |
|---------|---------------|
| "at risk" | Lists students with scores < 67% |
| "anomal" | Lists detected anomalies |
| "average" OR "performance" | Calculates class average |
| "summary" OR "report" | Overall statistics |

**Process:**
1. Convert query to lowercase
2. Check for keyword matches
3. Query ml/analytics.json for data
4. Format and return response

**Example:**
```
Input: "Identify students at risk"
Output: "- Student STU002 (Score: 0/3 - 0%)"
```

---

## Database Structure

### backend/responses.json
**Purpose:** Store all submitted student answers

**Structure:**
```json
[
  {
    "student_id": "STU001",
    "exam_id": "sample",
    "answers": {
      "q1": "Paris",
      "q2": "4",
      "q3": "Mars"
    },
    "timestamp": "2026-02-23T10:30:00"
  }
]
```

### ml/analytics.json
**Purpose:** Store evaluation results and statistics

**Structure:**
```json
{
  "sample": {
    "total_students": 3,
    "average_score": 66.7,
    "students": {
      "STU001": {
        "name": "John Doe",
        "score": 3,
        "percentage": 100.0,
        "at_risk": false,
        "anomalies": []
      }
    }
  }
}
```

---

## Complete User Journey

### Student Journey:
1. Visit landing.html
2. Click "Enter Student Portal"
3. See available tests
4. Select "General Knowledge Quiz"
5. Enter Student ID and Name
6. Answer 3 questions within 5-minute timer
7. Submit exam
8. See success message

### Faculty Journey:
1. Visit landing.html
2. Click "Enter Faculty Portal"
3. View quick statistics (students, avg score, at-risk count, anomalies)
4. Use quick query buttons or type custom queries
5. See analytics responses about student performance
6. View detailed results table

---

## Configuration & Customization

### To Add New Exams:
Edit `backend/main.py`:
```python
exams["new-exam"] = {
    "id": "new-exam",
    "title": "Your Exam Title",
    "questions": [...]
}
```

### To Change Timer Duration:
Edit `frontend/app.js`:
```javascript
startTimer(600);  // 10 minutes instead of 5
```

### To Update Correct Answers:
Edit `ml/evaluate.py`:
```python
correct_answers = {
    "q1": "Your Answer",
    "q2": "Your Answer"
}
```

### To Modify At-Risk Threshold:
Edit `ml/evaluate.py`:
```python
at_risk = (score / total_questions) < 0.50  # 50% instead of 67%
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Server not responding" | Make sure backend is running: `python backend/main.py` |
| Student portal shows blank | Check browser console for API call errors |
| Analytics not updating | Run `python ml/evaluate.py` after submitting answers |
| Faculty dashboard no data | Ensure students have submitted exams first |

---

## Summary of Key Functions by File

### landing.html - 0 functions (static page)

### exam.html - 7 functions in app.js:
1. `selectTest(testId)` - Switch to login form
2. `goBackToTests()` - Return to test selection
3. `startExam(e)` - Load exam and start
4. `renderExam()` - Display questions
5. `startTimer(seconds)` - Countdown timer
6. `submitExam(e)` - Submit answers
7. `submitExamAuto()` - Auto-submit on timeout

### faculty_dashboard.html - 4 functions:
1. `selectTest(testId)` - Select test (reuses from exam)
2. `loadStats()` - Load and display statistics
3. `submitQuery()` - Process faculty query
4. `generateResponse(query)` - Generate query response
5. `setQuery(query)` - Set and submit quick query

### index.html - 1 function:
1. API connection check on page load

---

## API Summary

| Method | Endpoint | Purpose | Status |
|--------|----------|---------|--------|
| GET | /exam/{exam_id} | Get exam questions | ✓ Working |
| POST | /exam | Create new exam | ✓ Ready |
| POST | /response | Submit answers | ✓ Working |
| GET | /responses/{exam_id} | Get all responses | ✓ Working |
| GET | /docs | Interactive API docs | ✓ Available |

---

**Total Lines of Code:** ~800 (Frontend) + ~200 (Backend) + ~150 (ML)
**Total Functions:** 12+ core functions across all components
**Supported Features:** Test selection, Timer, Multi-choice questions, Auto-grading, Analytics, Anomaly detection, GenAI queries
