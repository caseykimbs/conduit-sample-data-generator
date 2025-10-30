# 🏥 Conduit Sample Data Generator

Generate professional medical documents with realistic sample data for testing healthcare admissions software systems.

## 📚 What This Generates

This tool creates **two types** of realistic medical documents:

### 1️⃣ **Hospital Admission Documents**
Comprehensive patient admission assessments from major hospitals (UCLA, Stanford, Hoag, etc.)

### 2️⃣ **Medication Orders**
Patient medication lists from physician offices and pharmacies

---

## 📋 Prerequisites

Before you begin, you'll need **Python 3.8 or higher** installed on your system.

### ✅ Check if Python is Already Installed

Open your terminal/command prompt and run:

**macOS/Linux:**
```bash
python3 --version
```

**Windows:**
```bash
python --version
```

If you see a version number (3.8 or higher), skip to [Setup](#-setup).

---

## 🐍 Installing Python

### 🍎 macOS

**Option 1: Using Homebrew (Recommended)**

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

**Option 2: Download from Python.org**

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3.x installer for macOS
3. Run the installer and follow the prompts

---

### 🪟 Windows

**Option 1: Download from Python.org (Recommended)**

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3.x installer for Windows
3. Run the installer
4. ⚠️ **IMPORTANT:** Check ✅ "Add Python to PATH" during installation
5. Click "Install Now"

**Option 2: Using Microsoft Store**

1. Open Microsoft Store
2. Search for "Python 3.12" (or latest version)
3. Click "Get" to install

---

### 🐧 Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Fedora/RHEL:**
```bash
sudo dnf install python3 python3-pip
```

---

## 🚀 Setup

### 1️⃣ Navigate to Project Directory

Open your terminal/command prompt and navigate to this folder:

**macOS/Linux:**
```bash
cd /Users/caseykimball/Documents/Conduit/dev/conduit-sample-data-generator
```

**Windows:**
```cmd
cd C:\path\to\conduit-sample-data-generator
```

---

### 2️⃣ Create a Virtual Environment

A virtual environment keeps project dependencies isolated.

**macOS/Linux:**
```bash
python3 -m venv venv
```

**Windows:**
```cmd
python -m venv venv
```

---

### 3️⃣ Activate the Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

> 💡 **PowerShell Error?** If you get an execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

✅ You should see `(venv)` at the beginning of your terminal prompt.

---

### 4️⃣ Install Dependencies

With your virtual environment activated:

```bash
pip install -r requirements.txt
```

This installs:
- 📄 `reportlab` - Professional PDF generation
- 🎲 `faker` - Realistic fake data generation

---

## 🎯 Running the Generators

### 🏥 Generate Hospital Admission Documents

```bash
python generate_admission_documents.py
```

**Output:**
- 📁 Saves to: `/Users/caseykimball/Documents/sample_docs/`
- 📄 Filename: `{Hospital}-{LastName},{FirstName}.pdf`
- 📝 Example: `Hoag-Smith,John.pdf`

**What's Included:**
- ✅ Patient demographics (name, DOB, MRN, SSN)
- ✅ Admission information & chief complaint
- ✅ Vital signs, diagnoses, allergies, medications
- ✅ Lab results & diagnostic studies
- ✅ **Clinical flags** (🔴 red, 🟡 yellow, 🟢 green)
- ✅ **Functional assessment** (Section GG scores, BIMS scores)
- ✅ **Therapy services** (PT, OT, ST)
- ✅ **Equipment needs** (DME)
- ✅ **Transfer guidelines** (toileting, bathing, mobility)
- ✅ Immunizations, follow-up appointments
- ✅ Social history, advance directives

**🗓️ Dates:** Admission date is **7 days in the future** from today

---

### 💊 Generate Medication Orders

```bash
python generate_medication_orders.py
```

**Output:**
- 📁 Saves to: `/Users/caseykimball/Documents/sample_docs/`
- 📄 Filename: `{Institution}-new-meds.pdf`
- 📝 Example: `CVS-new-meds.pdf` or `Newport-new-meds.pdf`

**What's Included:**
- ✅ Current medications (3-6 maintenance meds)
- ✅ New medication orders (2-4 new prescriptions)
- ✅ Discontinued medications (sometimes included)
- ✅ Prescriber information (name, NPI)
- ✅ Institution (physician office or pharmacy)
- ✅ Medication details: dose, instructions, refills

**🗓️ Dates:** Current date for new orders

**🏢 Sources:** Randomly selects from:
- 👨‍⚕️ Physician offices (Newport Beach Primary Care, Orange County Family Medicine, etc.)
- 💊 Pharmacies (CVS, Walgreens, Rite Aid, Costco, etc.)

---

## 📂 Output Location

All documents are saved to:
```
/Users/caseykimball/Documents/sample_docs/
```

The directory is created automatically if it doesn't exist.

---

## 🎲 Randomization Features

### Every Document is Unique!

**Admission Documents:**
- 🏥 25 realistic CA/CO hospitals
- 👤 Random patient demographics (age 55-90)
- 🩺 4 diagnosis categories with appropriate conditions
- 💊 Randomized medication lists
- 🚩 Clinical flags (green, yellow, red)
- 🏋️ Therapy needs and functional scores
- 🛏️ Equipment and transfer requirements

**Medication Orders:**
- 👨‍⚕️ 12 physician offices + 10 pharmacies
- 💊 14 current medication options
- 🆕 13 new medication options
- ⛔ 6 discontinued medication options
- 🎲 Random prescriber names with NPIs

---

## 🛠️ Customization

### Modify Hospital Lists

Edit `generate_admission_documents.py` around line 251:
```python
hospital_names = [
    "Your Hospital Name",
    # Add more hospitals...
]
```

### Modify Medication Lists

Edit `generate_medication_orders.py`:
- Line 37: Current medications
- Line 58: New medications
- Line 85: Discontinued medications

### Change Output Directory

Both scripts accept an `output_dir` parameter:
```python
generate_admission_document(output_dir="/your/custom/path")
```

---

## 🧹 When You're Done

Deactivate the virtual environment:

```bash
deactivate
```

---

## 🆘 Troubleshooting

### ❌ "Python command not found"
- Verify Python is installed: Try `python3` instead of `python`
- **Windows:** Make sure "Add Python to PATH" was checked during installation

### ❌ "pip command not found"
- Try: `python -m pip` or `python3 -m pip`

### ❌ "Permission denied" (macOS/Linux)
- Don't use `sudo` with pip in a virtual environment
- Ensure virtual environment is activated

### ❌ PDF not generating
- Check reportlab is installed: `pip list | grep reportlab`
- Look for error messages in terminal

### ❌ Module import errors
- Make sure `(venv)` appears in your terminal prompt
- Reinstall: `pip install -r requirements.txt`

### ❌ PowerShell execution policy error (Windows)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📦 Dependencies

```
reportlab>=4.0.7
faker>=24.0.0
```

Automatically installed via `requirements.txt`

---

## 🏥 Sample Hospital Names

**Admission Documents Use:**
- Hoag Hospital
- UCLA Medical Center
- Stanford Hospital
- UCSF Medical Center
- Cedars-Sinai Medical Center
- UCHealth University of Colorado Hospital
- Denver Health Medical Center
- And 18 more...

**Medication Orders Use:**
- Newport Beach Primary Care
- Orange County Family Medicine
- CVS Pharmacy #4529
- Walgreens Pharmacy #8721
- And 18 more...

---

## 🔒 Privacy & Compliance

✅ **100% Fictitious Data** - All patient information is computer-generated
✅ **HIPAA Compliant** - No real patient data is used
✅ **Safe for Testing** - Perfect for development and QA environments

---

## 📧 Support

For questions or issues, contact the Conduit development team.

---

## 📜 License

This project is for internal testing purposes only. All data is fictitious and generated for software testing.

---

## 🎉 Quick Start Summary

```bash
# 1. Navigate to folder
cd /path/to/conduit-sample-data-generator

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Generate documents!
python generate_admission_documents.py
python generate_medication_orders.py

# 6. Find your PDFs in:
# /Users/caseykimball/Documents/sample_docs/
```

---

**Happy Testing! 🎉**
