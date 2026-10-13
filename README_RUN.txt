# How to Run the Full Project

1. Start the backend API:
   - Open a terminal in backend/
   - Run: python -m uvicorn main:app --reload

2. Open the web app:
   - Open frontend/exam.html in your browser

3. Simulate streaming pipeline:
   - Open a terminal in streaming/
   - Run: python streaming_pipeline.py

4. Run ML evaluation:
   - Open a terminal in ml/
   - Run: python evaluate.py

5. Use GenAI assistant:
   - Open a terminal in genai/
   - Run: python assistant.py
   - Example query: Identify students at risk of failing

# Notes
- All data is stored in backend/responses.json and ml/analytics.json
- For production, replace file storage with a real database and use Kafka for streaming
