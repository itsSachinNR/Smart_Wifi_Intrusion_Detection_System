# 🏗️ System Architecture — Smart WiFi Intrusion Detection System

---

## 📌 Overview

The Smart WiFi Intrusion Detection System follows a **modular pipeline architecture**, where each component performs a specific task in processing and analyzing WiFi events.

The system is designed to be:
- Simple  
- Scalable  
- Easy to understand  

---

## 🔄 Architecture Flow  
    
    +----------------------+
    |   Data Generation    |
    | (generate_data.py)   |
    +----------+-----------+
               |
               ↓
    +----------------------+
    |     Data Storage     |
    |   (events.json)      |
    +----------+-----------+
               |
               ↓
    +----------------------+
    |      Detector        |
    |   (detector.py)      |
    | - Score calculation  |
    | - Reason detection   |
    +----------+-----------+
               |
               ↓
    +----------------------+
    |       Alerts         |
    |    (alerts.py)       |
    | - Risk classification|
    | - Summary generation |
    +----------+-----------+
               |
               ↓
    +----------------------+
    |     Presentation     |
    |  (app.py + HTML UI)  |
    | - Displays results   |
    +----------+-----------+
               |
               ↓
    +----------------------+
    |   Report Generator   |
    | (report_generator.py)|
    | - Creates report.txt |
    +----------------------+

    
---

## 🧩 Components Description

### 1️⃣ Data Generation (`generate_data.py`)
- Generates simulated WiFi events  
- Includes:
  - device MAC  
  - signal strength  
  - event type  
- Stores output in `events.json`

---

### 2️⃣ Data Storage (`events.json`)
- Central dataset for the system  
- Contains all WiFi activity logs  
- Used as input for detection  

---

### 3️⃣ Detector Module (`detector.py`)
- Core logic of the system  
- Calculates:
  - Risk score  
  - Reasons for suspicion  

#### 🔍 Parameters analyzed:
- Failed login attempts  
- Signal strength  
- Event type  
- Device identity  
- Location  

---

### 4️⃣ Alerts Module (`alerts.py`)
- Converts score → risk level  
- Generates structured alert objects  
- Maintains summary of:
  - HIGH risk  
  - MEDIUM risk  
  - LOW risk  

---

### 5️⃣ Web Interface (`app.py + templates`)
- Built using Flask  
- Provides:
  - Home page (`index.html`)  
  - Results page (`result.html`)  

#### Features:
- Displays:
  - Device details  
  - Risk level  
  - Reasons  
- Interactive UI  

---

### 6️⃣ Report Generator (`report_generator.py`)
- Generates `report.txt`  
- Contains:
  - All alerts  
  - Reasons  
  - Final summary  

---

## 🧠 Data Flow Explanation

1. Data is generated using `generate_data.py`  
2. Stored in `events.json`  
3. Detector processes events → calculates score + reasons  
4. Alerts module assigns risk levels  
5. Results are displayed via Flask UI  
6. Report is generated for analysis  

---

## 🎯 Design Advantages

- ✅ Modular structure  
- ✅ Easy to extend  
- ✅ Clear separation of concerns  
- ✅ Beginner-friendly design  
- ✅ Supports future upgrades  

---

## 🔮 Future Enhancements

- Real-time packet capture  
- Machine learning-based detection  
- Dashboard analytics  
- Email/SMS alerts  
- Integration with network devices  

---

## 📌 Conclusion

This architecture ensures a clean separation between data processing, analysis, and presentation, making the system efficient, scalable, and easy to maintain.
