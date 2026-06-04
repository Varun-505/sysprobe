import psutil
import argparse
import os
from datetime import datetime

# ---------- SYSTEM INFO ----------

def cpu():
    return psutil.cpu_percent(interval=1)

def memory():
    mem = psutil.virtual_memory()
    return mem.percent

def disk():
    disk = psutil.disk_usage('/')
    return disk.percent

# ---------- PROCESS INFO ----------

def processes(limit=5):
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            procs.append(p.info)
        except:
            pass

    procs = sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)
    return procs[:limit]

# ---------- LOG ANALYSIS ----------

def analyze_logs(path="/var/log/syslog"):
    errors = []
    if not os.path.exists(path):
        return ["Log file not found"]

    with open(path, "r", errors="ignore") as f:
        for line in f:
            if "error" in line.lower() or "fail" in line.lower():
                errors.append(line.strip())

    return errors[:10]

# ---------- REPORT ----------

def generate_report():
    report = f"""
SYSTEM REPORT - {datetime.now()}
--------------------------
CPU Usage: {cpu()}%
Memory Usage: {memory()}%
Disk Usage: {disk()}%
"""
    return report

# ---------- CLI ----------

def main():
    parser = argparse.ArgumentParser(description="sysprobe - Linux System Monitor")

    parser.add_argument("--cpu", action="store_true")
    parser.add_argument("--memory", action="store_true")
    parser.add_argument("--disk", action="store_true")
    parser.add_argument("--processes", action="store_true")
    parser.add_argument("--logs", action="store_true")
    parser.add_argument("--report", action="store_true")

    args = parser.parse_args()

    if args.cpu:
        print("CPU:", cpu(), "%")

    elif args.memory:
        print("Memory:", memory(), "%")

    elif args.disk:
        print("Disk:", disk(), "%")

    elif args.processes:
        for p in processes():
            print(p)

    elif args.logs:
        logs = analyze_logs()
        for l in logs:
            print(l)

    elif args.report:
        print(generate_report())

    else:
        print("""
sysprobe commands:
--cpu
--memory
--disk
--processes
--logs
--report
""")

if __name__ == "__main__":
    main()