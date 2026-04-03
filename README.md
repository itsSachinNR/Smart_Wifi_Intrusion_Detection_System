#Smart wifi intrusion detection system 
## Project Workflow
Data → Detector → Alerts → Report

- Data: stores WiFi events
- Detector: calculates risk score and reasons
- Alerts: assigns risk level
- Report: summarizes results
  
## Example Output
Device: AA:BB:CC:11:22:33  
Score: 60  
Risk: HIGH  
Reason: multiple failed attempts, weak signal

## Detector Logic
The detector analyzes failed attempts, signal strength, and device identity to detect suspicious activity and assign a risk score.
