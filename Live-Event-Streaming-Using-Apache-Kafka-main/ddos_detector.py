import json
import time
import threading
from collections import defaultdict
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
THRESHOLD = 5  # Requests per time window
TIME_WINDOW_SECONDS = 10  # Time window for detection
CHECK_INTERVAL = 5  # Check every 5 seconds

# Email Configuration - UPDATED WITH YOUR EMAIL
EMAIL_ENABLED = True  # Set to False to disable email alerts
SMTP_SERVER = "smtp.gmail.com"  # For Gmail: smtp.gmail.com
SMTP_PORT = 587  # For Gmail: 587
SENDER_EMAIL = "mk.ibrar.dar@gmail.com"  # YOUR email address
SENDER_PASSWORD = "xuctuohdnphjkgmm"  # You need to generate this from Gmail
RECIPIENT_EMAIL = "mk.ibrar.dar@gmail.com"  # Send alerts to your email

# Store for alerts
last_alerts = {}
alert_history = []
last_email_time = {}  # Track last email sent per IP to avoid spam
email_cooldown_seconds = 300  # Send email for same IP every 5 minutes max

def send_email_alert(ip, count, severity, attack_details):
    """Send email alert for DDoS attack"""
    if not EMAIL_ENABLED:
        return False
    
    # Check cooldown for this IP
    current_time = time.time()
    if ip in last_email_time:
        if current_time - last_email_time[ip] < email_cooldown_seconds:
            print(f"[✉️] Email skipped for {ip} - cooldown active")
            return False  # Skip email if in cooldown
    
    try:
        # Create email message
        subject = f"🚨 DDoS ALERT: Attack detected from {ip}"
        
        # Create HTML email body
        body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .alert {{ background-color: #ff2d55; color: white; padding: 10px; border-radius: 5px; }}
                .details {{ background-color: #f0f0f0; padding: 15px; border-radius: 5px; margin-top: 10px; }}
                .warning {{ color: #ff2d55; font-weight: bold; }}
                .ip-box {{ background-color: #000; color: #00e5ff; padding: 10px; font-family: monospace; font-size: 16px; }}
            </style>
        </head>
        <body>
            <div class="alert">
                <h2>🚨 DDoS Attack Detected!</h2>
            </div>
            <div class="details">
                <h3>Attack Details:</h3>
                <p><strong>🖥️ Source IP:</strong> <span class="ip-box">{ip}</span></p>
                <p><strong>📊 Request Count:</strong> {count} requests in {TIME_WINDOW_SECONDS} seconds</p>
                <p><strong>⚠️ Severity:</strong> <span style="color: #ff2d55; font-weight: bold;">{severity}</span></p>
                <p><strong>⏰ Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>🎯 Threshold:</strong> {THRESHOLD} requests per {TIME_WINDOW_SECONDS} seconds</p>
                <p><strong>📈 Attack Rate:</strong> {count/TIME_WINDOW_SECONDS:.1f} requests/second</p>
            </div>
            <div class="details">
                <h3>🛡️ Recommended Actions:</h3>
                <ul>
                    <li><strong>Immediate:</strong> Block IP <code>{ip}</code> immediately</li>
                    <li><strong>Rate Limiting:</strong> Enable rate limiting for suspicious traffic</li>
                    <li><strong>Monitor:</strong> Check for additional attack patterns</li>
                    <li><strong>Firewall:</strong> Review and update firewall rules</li>
                </ul>
            </div>
            <div class="details">
                <h3>📊 Attack Statistics:</h3>
                <p>• Total attacks detected in this session: {len([a for a in alert_history if a.get('status') == 'ATTACK'])}</p>
                <p>• Unique attacking IPs: {len(set([a.get('ip') for a in alert_history if a.get('status') == 'ATTACK']))}</p>
            </div>
            <p><small>This is an automated alert from your DDoS Shield System. Please investigate immediately.</small></p>
            <hr>
            <p><small>DDoS Shield | Real-time Protection System</small></p>
        </body>
        </html>
        """
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        # Send email
        print(f"[✉️] Sending email alert to {RECIPIENT_EMAIL}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        # Update last email time
        last_email_time[ip] = current_time
        
        print(f"[✅] Email alert sent successfully to {RECIPIENT_EMAIL} for IP {ip}")
        return True
        
    except Exception as e:
        print(f"[❌] Failed to send email: {e}")
        return False

def save_alert(ip, count, status, severity):
    """Save alert to alerts.json file"""
    alert = {
        "ip": ip,
        "count": count,
        "status": status,
        "severity": severity,
        "timestamp": str(datetime.now())
    }
    
    # Add to alert history
    alert_history.append(alert)
    
    # Read existing alerts
    try:
        with open("alerts.json", "r") as f:
            alerts = []
            for line in f:
                line = line.strip()
                if line:
                    try:
                        alerts.append(json.loads(line))
                    except:
                        pass
    except FileNotFoundError:
        alerts = []
    
    # Add new alert
    alerts.append(alert)
    
    # Keep only last 500 alerts
    if len(alerts) > 500:
        alerts = alerts[-500:]
    
    # Write back
    with open("alerts.json", "w") as f:
        for alert in alerts:
            f.write(json.dumps(alert) + "\n")
    
    return alert

def analyze_traffic():
    """Analyze traffic logs and detect attacks"""
    global last_alerts
    
    try:
        with open("logs.json", "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return
    
    if not logs:
        return
    
    # Get current time
    now = datetime.now()
    cutoff_time = now - timedelta(seconds=TIME_WINDOW_SECONDS)
    
    # Filter logs within time window
    recent_logs = []
    for log in logs:
        try:
            log_time = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
            if log_time > cutoff_time:
                recent_logs.append(log)
        except:
            recent_logs.append(log)
    
    # Count requests per IP
    ip_count = defaultdict(int)
    for log in recent_logs:
        ip = log.get("source_ip", "unknown")
        ip_count[ip] += 1
    
    # Check each IP against threshold
    current_alerts = {}
    for ip, count in ip_count.items():
        if count > THRESHOLD:
            status = "ATTACK"
            severity = "HIGH"
            current_alerts[ip] = {"count": count, "status": status}
            save_alert(ip, count, status, severity)
            
            # Send email alert for new attacks
            if ip not in last_alerts or last_alerts[ip]["count"] != count:
                print(f"\n{'='*60}")
                print(f"[!] 🚨 ALERT: {ip} → {count} requests in {TIME_WINDOW_SECONDS}s | ATTACK DETECTED")
                print(f"{'='*60}")
                # Send email notification
                send_email_alert(ip, count, severity, f"Detected {count} requests in {TIME_WINDOW_SECONDS} seconds")
    
    last_alerts = current_alerts

def detection_loop():
    """Run detection continuously"""
    print("="*60)
    print("🛡️ DDoS Shield - Detection Engine")
    print("="*60)
    print(f"[*] Threshold: {THRESHOLD} requests per {TIME_WINDOW_SECONDS} seconds")
    print(f"[*] Check interval: Every {CHECK_INTERVAL} seconds")
    print(f"[*] Email alerts: {'ENABLED' if EMAIL_ENABLED else 'DISABLED'}")
    print(f"[*] Alert recipient: {RECIPIENT_EMAIL}")
    print("="*60)
    print("\n[*] Detection engine started. Monitoring for attacks...\n")
    
    while True:
        try:
            analyze_traffic()
            time.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:
            print("\n[*] Detection stopped")
            break
        except Exception as e:
            print(f"[!] Detection error: {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    detection_loop()