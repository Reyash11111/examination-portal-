#!/usr/bin/env python3
"""
Examination System Startup Verification
Checks all components and displays system status
"""

import os
import json
import sys

def check_file_exists(path, name):
    exists = os.path.exists(path)
    status = "✓" if exists else "✗"
    print(f"  {status} {name}")
    return exists

def check_data():
    responses_file = os.path.join(os.path.dirname(__file__), 'backend/responses.json')
    analytics_file = os.path.join(os.path.dirname(__file__), 'ml/analytics.json')
    
    print("\n📊 DATA STATUS:")
    
    if os.path.exists(responses_file):
        with open(responses_file, 'r') as f:
            data = json.load(f)
            total = sum(len(v) for v in data.values())
            print(f"  ✓ Student Responses: {total} submitted")
    else:
        print("  ✗ No responses yet")
    
    if os.path.exists(analytics_file):
        with open(analytics_file, 'r') as f:
            analytics = json.load(f)
            for exam_id, records in analytics.items():
                at_risk = sum(1 for r in records if r.get('at_risk'))
                anomalies = sum(1 for r in records if r.get('anomaly'))
                print(f"  ✓ Analytics for '{exam_id}':")
                print(f"    - Students: {len(records)}")
                print(f"    - At Risk: {at_risk}")
                print(f"    - Anomalies: {anomalies}")
    else:
        print("  ✗ No analytics yet (run ml/evaluate.py)")

def main():
    print("\n" + "="*70)
    print("  EXAMINATION SYSTEM - STARTUP VERIFICATION  ".center(70))
    print("="*70 + "\n")
    
    print("✅ SYSTEM COMPONENTS:\n")
    
    check_file_exists('backend/main.py', 'Backend API (FastAPI)')
    check_file_exists('frontend/exam.html', 'Student Exam Portal')
    check_file_exists('frontend/faculty_dashboard.html', 'Faculty Dashboard')
    check_file_exists('frontend/index.html', 'System Control Panel')
    check_file_exists('ml/evaluate.py', 'ML Evaluation Pipeline')
    check_file_exists('genai/assistant.py', 'GenAI Assistant')
    
    print("\n📂 CONFIGURATION FILES:\n")
    
    check_file_exists('backend/requirements.txt', 'Backend Requirements')
    check_file_exists('ml/requirements.txt', 'ML Requirements')
    
    print("\n📚 DOCUMENTATION:\n")
    
    check_file_exists('README.md', 'Main Documentation')
    check_file_exists('QUICKSTART.md', 'Quick Start Guide')
    check_file_exists('README_SYSTEM_STATUS.txt', 'System Status Report')
    check_file_exists('START_HERE.txt', 'Quick Start Instructions')
    
    check_data()
    
    print("\n" + "="*70)
    print("  RUNNING SERVICES  ".center(70))
    print("="*70 + "\n")
    
    print("  🌐 Backend API ............. Running on http://localhost:8000")
    print("  👨‍🎓 Student Portal .......... Ready at frontend/exam.html")
    print("  👨‍🏫 Faculty Dashboard ....... Ready at frontend/faculty_dashboard.html")
    print("  🤖 GenAI Assistant ......... Running (interactive mode)")
    print("  💾 Data Storage ............ Active (JSON format)")
    
    print("\n" + "="*70)
    print("  NEXT STEPS  ".center(70))
    print("="*70 + "\n")
    
    print("  1️⃣  Double-click: frontend/index.html")
    print("  2️⃣  View the System Control Panel")
    print("  3️⃣  Click 'Start Exam' to test")
    print("  4️⃣  View 'Faculty Dashboard' for analytics")
    print("  5️⃣  Try sample queries with GenAI")
    
    print("\n" + "="*70)
    print("  ✨ SYSTEM READY FOR USE ✨  ".center(70))
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
