# 🏥 Conduit Sample Data Generator

Generate professional medical admission documents with realistic sample data for testing healthcare software systems.

---

## 📋 Prerequisites

Before you begin, you'll need Python installed on your system.

### Check if Python is Already Installed

Open your terminal and run:

```bash
python --version
```

or

```bash
python3 --version
```

If you see a version number (3.8 or higher), you're good to go! Skip to [Setup](#-setup).

---

## 🐍 Installing Python

### macOS

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

### Windows

**Option 1: Download from Python.org (Recommended)**

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3.x installer for Windows
3. Run the installer
4. ⚠️ **Important:** Check "Add Python to PATH" during installation
5. Click "Install Now"

**Option 2: Using Microsoft Store**

1. Open Microsoft Store
2. Search for "Python 3.12" (or latest version)
3. Click "Get" to install

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Linux (Fedora/RHEL)

```bash
sudo dnf install python3 python3-pip
```

---

## 🚀 Setup

### 1️⃣ Clone or Download This Repository

```bash
cd /path/to/your/projects
git clone <repository-url>
cd conduit-sample-data-generator
```

Or download and extract the ZIP file, then navigate to the folder.

---

### 2️⃣ Create a Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.

**macOS/Linux:**

```bash
python3 -m venv venv
```

**Windows:**

```bash
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

> 💡 **Note:** If you get a PowerShell execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

You should see `(venv)` appear at the beginning of your terminal prompt, indicating the virtual environment is active.

---

### 4️⃣ Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- `reportlab` - Professional PDF generation library

---

## 🎯 Running the Generator

### Generate an Admission Document

```bash
python generate_admission_documents.py
```

**Output:**
- ✅ Creates `Admission_Document_Sample.pdf` in the current directory
- 📄 Professional 2-3 page medical admission document
- 👤 Realistic patient data with cardiac admission scenario

---

## 📄 What's Generated

Each run generates a **completely unique** admission document with fully randomized data:

### 🎲 Randomized Personal Information
- **Patient Demographics** - Random names (male/female), ages (55-90), DOBs
- **Full SSN** - Complete 9-digit Social Security Number (XXX-XX-XXXX format)
- **Medical Record Number** - Unique MRN for each patient
- **Insurance** - Random mix of Medicare, Medicaid, and commercial insurance
- **Hospital Information** - Random hospital names, addresses, phone/fax numbers
- **Emergency Contacts** - Randomized family members with phone numbers and emails

### 🏥 Randomized Medical Data
- **Admission Information** - Type, source, attending physician, room assignment
- **Vital Signs** - Randomized BP, HR, temperature, RR, SpO2, pain levels
- **Diagnoses** - Random primary diagnoses (cardiac, respiratory, neuro, sepsis) with appropriate secondary conditions
- **Allergies** - 2-4 random allergies with reactions (highlighted in yellow alert box)
- **Medications** - 4-7 randomized medications appropriate to patient conditions
- **Laboratory Results** - Randomized CBC, metabolic panel, cardiac markers, lipid panel
- **Diagnostic Studies** - Varied ECG and chest X-ray findings
- **Physical Examination** - Randomized physical exam findings
- **Assessment & Plan** - Initial treatment plan
- **Code Status** - Random code status (Full Code, DNR, DNR/DNI)
- **Social & Functional History** - Random living situations, occupations, smoking/alcohol history

### 📅 Dynamic Dates
All dates are generated relative to **today's date**, so documents never look stale or outdated.

**Every time you run the script, you get a completely different patient with unique data!**

---

## 🛠️ Customization

To modify the generated documents, edit `generate_admission_documents.py`:

- **Patient data** - Change demographics, diagnoses, medications
- **Styling** - Adjust colors, fonts, spacing in the style definitions
- **Content sections** - Add or remove sections as needed
- **Date offsets** - Use `get_relative_date()` function for dynamic dates

---

## 🧹 Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment:

```bash
deactivate
```

---

## 🆘 Troubleshooting

### "Python command not found"
- Make sure Python is installed and added to your PATH
- Try using `python3` instead of `python`

### "pip command not found"
- Try `python -m pip` or `python3 -m pip` instead

### "Permission denied" errors on macOS/Linux
- Don't use `sudo` with pip when in a virtual environment
- Make sure your virtual environment is activated

### PDF not generating
- Verify reportlab installed: `pip list | grep reportlab`
- Check for error messages in the terminal output

### Module import errors
- Ensure virtual environment is activated (look for `(venv)` in prompt)
- Reinstall dependencies: `pip install -r requirements.txt`

---

## 📝 Requirements

- Python 3.8 or higher
- reportlab 4.0.7
- Faker 24.0.0

---

## 📧 Support

For issues or questions, please contact the development team or open an issue in the repository.

---

## 📜 License

This project is for internal testing purposes only. Contains no real patient data (HIPAA compliant - all data is fictitious).

---

**Happy Testing! 🎉**