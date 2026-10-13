#!/usr/bin/env python3
"""
Demonstration script for the Online Examination System
This script shows how to use all components together
"""

import json
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.main import exams
from ml.evaluate import evaluate_responses
from genai.assistant import answer_query

def demo_create_exam():
    """Demo: Create a custom exam"""
    print("\n" + "="*60)
    print("DEMO: Creating Custom Exam")
    print("="*60)
    
    # Exams are created via API, but here's how data flows
    print("Sample exam (already loaded):")
    if "sample" in exams:
        exam = exams["sample"]
        print(f"  ID: {exam.id}")
        print(f"  Title: {exam.title}")
        print(f"  Questions: {len(exam.questions)}")
        for q in exam.questions:
            print(f"    - {q.text}")

def demo_submit_responses():
    """Demo: Simulated student responses"""
    print("\n" + "="*60)
    print("DEMO: Simulating Student Responses")
    print("="*60)
    
    # Simulate 3 student responses
    responses_file = os.path.join(os.path.dirname(__file__), 'backend/responses.json')
    
    sample_responses = {
        "sample": [
            {
                "student_id": "STU001",
                "exam_id": "sample",
                "answers": {"q1": "Paris", "q2": "4", "q3": "Mars"}
            },
            {
                "student_id": "STU002",
                "exam_id": "sample",
                "answers": {"q1": "London", "q2": "3", "q3": "Venus"}
            },
            {
                "student_id": "STU003",
                "exam_id": "sample",
                "answers": {"q1": "Paris", "q2": "4", "q3": "Venus"}
            }
        ]
    }
    
    with open(responses_file, 'w') as f:
        json.dump(sample_responses, f, indent=2)
    
    print("✓ Created 3 sample student responses")
    print("  - STU001: All correct")
    print("  - STU002: All wrong")
    print("  - STU003: 2 correct, 1 wrong")

def demo_evaluate():
    """Demo: Run ML evaluation"""
    print("\n" + "="*60)
    print("DEMO: Running ML Evaluation")
    print("="*60)
    
    os.chdir(os.path.join(os.path.dirname(__file__), 'ml'))
    evaluate_responses()
    os.chdir('..')
    
    # Display analytics
    analytics_file = os.path.join(os.path.dirname(__file__), 'ml/analytics.json')
    if os.path.exists(analytics_file):
        with open(analytics_file, 'r') as f:
            analytics = json.load(f)
        
        print("\n✓ Evaluation Complete:")
        for exam_id, records in analytics.items():
            print(f"\n  Exam: {exam_id}")
            for rec in records:
                status = "✗ AT RISK" if rec['at_risk'] else "✓ PASS"
                anomaly = " | ⚠ ANOMALY" if rec['anomaly'] else ""
                print(f"    {rec['student_id']}: {rec['score']}/3 ({rec['percentage']:.1f}%) {status}{anomaly}")

def demo_genai_queries():
    """Demo: GenAI Assistant queries"""
    print("\n" + "="*60)
    print("DEMO: GenAI Assistant Queries")
    print("="*60)
    
    queries = [
        "Identify students at risk of failing",
        "Show anomalies",
        "Average performance",
        "Summary report"
    ]
    
    for query in queries:
        print(f"\nFaculty: {query}")
        response = answer_query(query)
        print(f"Assistant:\n{response}")
        print("-" * 50)

def main():
    """Run full demonstration"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  Online Examination System - Full Demonstration  ".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        demo_create_exam()
        demo_submit_responses()
        demo_evaluate()
        demo_genai_queries()
        
        print("\n" + "="*60)
        print("DEMO COMPLETE!")
        print("="*60)
        print("\n📊 Summary:")
        print("  ✓ Exam system initialized")
        print("  ✓ Student responses processed")
        print("  ✓ ML evaluation completed")
        print("  ✓ GenAI queries demonstrated")
        
        print("\n🚀 To run the full system:")
        print("  1. Terminal 1: cd backend && python -m uvicorn main:app --reload")
        print("  2. Terminal 2: Open frontend/exam.html in browser")
        print("  3. Terminal 3: cd ml && python evaluate.py")
        print("  4. Terminal 4: cd genai && python assistant.py")
        
        print("\n📚 Documentation: See README.md for detailed instructions")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
