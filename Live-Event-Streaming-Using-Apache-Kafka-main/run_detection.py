import subprocess
import threading
import time
import os
import signal
import sys

def run_capture():
    """Run the packet capture"""
    print("[*] Starting packet capture...")
    subprocess.run(["python", "capture.py"])

def run_detector():
    """Run the DDoS detector"""
    print("[*] Starting DDoS detector...")
    subprocess.run(["python", "ddos_detector.py"])

def run_dashboard():
    """Run the Streamlit dashboard"""
    print("[*] Starting dashboard...")
    subprocess.run(["streamlit", "run", "dashboard.py"])

if __name__ == "__main__":
    print("=" * 60)
    print("🛡️  DDoS Shield - Real-time Detection System")
    print("=" * 60)
    print("\nStarting all components...\n")
    
    # Clear old alert file to start fresh
    if os.path.exists("alerts.json"):
        os.remove("alerts.json")
        print("[✓] Cleared old alerts")
    
    # Start components in separate threads
    threads = []
    
    # Capture thread
    capture_thread = threading.Thread(target=run_capture, daemon=True)
    capture_thread.start()
    threads.append(capture_thread)
    print("[✓] Packet capture started")
    
    time.sleep(1)  # Give capture time to initialize
    
    # Detector thread
    detector_thread = threading.Thread(target=run_detector, daemon=True)
    detector_thread.start()
    threads.append(detector_thread)
    print("[✓] DDoS detector started")
    
    time.sleep(1)  # Give detector time to initialize
    
    # Dashboard thread
    dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
    dashboard_thread.start()
    threads.append(dashboard_thread)
    print("[✓] Dashboard started")
    
    print("\n" + "=" * 60)
    print("All components running!")
    print("Dashboard available at: http://localhost:8501")
    print("Press Ctrl+C to stop all components")
    print("=" * 60 + "\n")
    
    try:
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Shutting down...")
        sys.exit(0)