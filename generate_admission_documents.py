"""
Admissions Sample Document PDF Generator
Generates professional medical admission documents with fully randomized realistic sample data
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import datetime, timedelta
from faker import Faker
import random

# Initialize Faker
fake = Faker()

def generate_ssn():
    """Generate a random 9-digit SSN"""
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def generate_mrn():
    """Generate a random Medical Record Number"""
    return f"MRN-{random.randint(100000, 999999)}"

def generate_npi():
    """Generate a random 10-digit NPI"""
    return f"{random.randint(1000000000, 9999999999)}"

def get_relative_date(days_offset):
    """Generate relative date descriptions with actual date"""
    target_date = datetime.now() + timedelta(days=days_offset)
    date_str = target_date.strftime("%m/%d/%Y")

    if days_offset == 0:
        return f"Today ({date_str})"
    elif days_offset == -1:
        return f"Yesterday ({date_str})"
    elif days_offset == 1:
        return f"Tomorrow ({date_str})"
    else:
        return date_str

def get_insurance_type():
    """Randomly select insurance type"""
    options = [
        ("Medicare Part A & B", "AARP Supplemental"),
        ("Medicare Part A & B", "Humana Supplemental"),
        ("Medicaid", "None"),
        ("Blue Cross Blue Shield", "Delta Dental"),
        ("Aetna PPO", "VSP Vision"),
        ("United Healthcare", "None"),
        ("Cigna", "MetLife Dental")
    ]
    return random.choice(options)

def get_random_diagnosis():
    """Select random primary diagnosis with related secondary conditions"""
    diagnoses = {
        "cardiac": {
            "primary": "Acute coronary syndrome, suspected NSTEMI",
            "secondary": [
                "Hypertension, uncontrolled",
                "Type 2 Diabetes Mellitus with neuropathy",
                "Hyperlipidemia",
                "Chronic obstructive pulmonary disease (COPD)",
                f"Obesity (BMI {random.randint(28, 40)}.{random.randint(0, 9)})"
            ]
        },
        "respiratory": {
            "primary": "Acute respiratory failure, community-acquired pneumonia",
            "secondary": [
                "Chronic obstructive pulmonary disease (COPD)",
                "Hypertension",
                "Type 2 Diabetes Mellitus",
                "Congestive heart failure",
                "Atrial fibrillation"
            ]
        },
        "neuro": {
            "primary": "Acute ischemic stroke, left middle cerebral artery",
            "secondary": [
                "Hypertension, poorly controlled",
                "Atrial fibrillation",
                "Hyperlipidemia",
                "Type 2 Diabetes Mellitus",
                "Chronic kidney disease, Stage 3"
            ]
        },
        "sepsis": {
            "primary": "Severe sepsis, suspected urinary tract infection source",
            "secondary": [
                "Acute kidney injury",
                "Type 2 Diabetes Mellitus",
                "Hypertension",
                "Dementia",
                "Chronic urinary retention"
            ]
        }
    }
    return random.choice(list(diagnoses.values()))

def get_random_medications():
    """Generate random but realistic medication list"""
    med_pools = {
        "cardiac": [
            ("Metoprolol", "50 mg", "PO", "BID"),
            ("Lisinopril", "20 mg", "PO", "Daily"),
            ("Atorvastatin", "40 mg", "PO", "QHS"),
            ("Apixaban (Eliquis)", "5 mg", "PO", "BID"),
            ("Clopidogrel (Plavix)", "75 mg", "PO", "Daily"),
        ],
        "diabetes": [
            ("Metformin", "1000 mg", "PO", "BID"),
            ("Glipizide", "10 mg", "PO", "Daily"),
            ("Insulin glargine", "20 units", "SubQ", "QHS"),
        ],
        "respiratory": [
            ("Albuterol inhaler", "2 puffs", "Inhaled", "Q4-6H PRN"),
            ("Fluticasone/Salmeterol", "250/50 mcg", "Inhaled", "BID"),
        ],
        "common": [
            ("Gabapentin", "300 mg", "PO", "TID"),
            ("Omeprazole", "20 mg", "PO", "Daily"),
            ("Aspirin", "81 mg", "PO", "Daily"),
            ("Vitamin D3", "2000 IU", "PO", "Daily"),
        ]
    }

    # Select 4-7 random medications
    all_meds = []
    all_meds.extend(random.sample(med_pools["cardiac"], k=random.randint(1, 2)))
    all_meds.extend(random.sample(med_pools["diabetes"], k=random.randint(0, 2)))
    all_meds.extend(random.sample(med_pools["respiratory"], k=random.randint(0, 1)))
    all_meds.extend(random.sample(med_pools["common"], k=random.randint(1, 3)))

    return all_meds[:random.randint(4, 7)]

def get_random_allergies():
    """Generate random allergies"""
    allergies = [
        ("Penicillin", "Severe rash, hives"),
        ("Aspirin", "GI bleeding"),
        ("Sulfa drugs", "Severe rash"),
        ("Codeine", "Nausea, vomiting"),
        ("Latex", "Contact dermatitis"),
        ("Shellfish", "Anaphylaxis"),
        ("Morphine", "Respiratory depression"),
        ("Iodine contrast", "Hives, itching"),
    ]

    num_allergies = random.randint(2, 4)
    return random.sample(allergies, k=num_allergies)

def get_clinical_flags():
    """Generate clinical flags based on green/yellow/red categories"""
    flags = {"green": [], "yellow": [], "red": []}

    green_flags = [
        ("Hemodialysis", "MWF schedule at dialysis center"),
        ("IV Therapy", "Peripheral line, saline lock"),
        ("PICC Line", "Right arm PICC, placed {}, flushes per protocol"),
        ("Wound Care", "Stage 2 pressure ulcer sacrum, dressing changes daily"),
        ("Wound Care", "Surgical wound, staples intact, remove {}"),
        ("HIV/Hepatitis", "Hepatitis C positive, standard precautions"),
        ("Fractures", "Left hip fracture s/p ORIF, weight-bearing as tolerated"),
        ("Rehab Services", "PT/OT 5x week"),
        ("Pain Management", "Oxycodone 5mg q4-6h PRN, rates pain 6/10"),
        ("Ostomy", "Colostomy, patient managing independently"),
        ("Elopement Risk", "History of wandering, bed alarm in place"),
        ("Continuous O2", "2L NC continuous, baseline SpO2 88-92%"),
        ("Fall Risk", "Morse Fall Scale 65 - High risk, fall precautions"),
        ("CPAP", "BiPAP nightly for sleep apnea, good compliance")
    ]

    yellow_flags = [
        ("Peritoneal Dialysis", "CAPD 4 exchanges daily"),
        ("Psychiatric Diagnosis", "Major depressive disorder, stable on Sertraline"),
        ("Psychiatric Diagnosis", "Bipolar disorder, currently euthymic"),
        ("Substance Use History", "Alcohol use disorder, sober 6 months"),
        ("Tracheostomy", "Trach placed {}, requires suctioning q4h"),
        ("TPN", "Central line TPN, cycled overnight"),
        ("Chemotherapy", "Last cycle {}, due for next {}"),
        ("Enteral Feeding", "PEG tube, Jevity 1.5 at 75mL/hr"),
        ("Bariatric", "Weight 385 lbs, bariatric bed/equipment required"),
        ("Paraplegia", "T8 paraplegia, wheelchair dependent"),
        ("Infectious Disease", "MRSA colonization, contact precautions"),
        ("PCA Pump", "Dilaudid PCA for post-op pain management"),
        ("1:1 Supervision", "Required for safety, aggressive behaviors")
    ]

    red_flags = [
        ("Heparin Drip", "For DVT, PTT monitoring q6h"),
        ("Insulin Drip", "DKA protocol, glucose checks q1h"),
        ("Ventilator", "Vent-dependent, wean in progress"),
        ("Telemetry", "Continuous cardiac monitoring for arrhythmias"),
        ("Danger to Others", "History of assaultive behavior, 1:1 required")
    ]

    # Randomly select 2-4 green flags
    num_green = random.randint(2, 4)
    for flag_data in random.sample(green_flags, min(num_green, len(green_flags))):
        flags["green"].append(flag_data)

    # Randomly select 0-2 yellow flags
    if random.random() > 0.4:
        num_yellow = random.randint(1, 2)
        for flag_data in random.sample(yellow_flags, min(num_yellow, len(yellow_flags))):
            flags["yellow"].append(flag_data)

    # Rarely add red flags (0-1)
    if random.random() > 0.85:
        flag_data = random.choice(red_flags)
        flags["red"].append(flag_data)

    return flags

def get_dme_equipment():
    """Generate DME and equipment needs"""
    equipment = []
    base_items = random.sample([
        "Hospital bed with pressure-relieving mattress",
        "Bedside commode",
        "Raised toilet seat with grab bars",
        "Shower chair with back support",
        "Rolling walker with seat",
        "Standard walker",
        "Quad cane",
        "Wheelchair - manual, standard",
        "Oxygen concentrator - 2L continuous"
    ], k=random.randint(2, 4))
    return base_items

def generate_admission_document(filename=None, output_dir="/Users/caseykimball/Documents/sample_docs"):
    """Generate a complete admission document PDF with randomized data"""

    # Generate random patient data
    gender = random.choice(["M", "F"])
    if gender == "M":
        first_name = fake.first_name_male()
        prefix = "Mr."
    else:
        first_name = fake.first_name_female()
        prefix = "Ms." if random.random() > 0.5 else "Mrs."

    middle_name = fake.first_name()
    last_name = fake.last_name()
    full_name = f"{last_name}, {first_name} {middle_name}"

    # Generate age between 55-90
    age = random.randint(55, 90)
    birth_year = datetime.now().year - age
    birth_date = fake.date_of_birth(minimum_age=age, maximum_age=age)
    dob_str = birth_date.strftime("%m/%d/%Y")

    ssn = generate_ssn()
    mrn = generate_mrn()

    # Generate addresses and contact info
    patient_address = fake.address().replace("\n", ", ")
    hospital_address = f"{fake.building_number()} {fake.street_name()}"
    hospital_city = fake.city()
    hospital_state = fake.state_abbr()
    hospital_zip = fake.zipcode()
    hospital_phone = fake.phone_number()
    hospital_fax = fake.phone_number()

    # Generate insurance
    primary_ins, secondary_ins = get_insurance_type()

    # Generate physicians
    attending_dr = f"Dr. {fake.first_name()} {fake.last_name()}, MD"
    referring_dr = f"Dr. {fake.first_name()} {fake.last_name()}, MD"

    # Generate emergency contacts
    contact1_name = fake.name()
    contact1_relation = random.choice(["Spouse", "Daughter", "Son", "Sister", "Brother"])
    contact1_phone = fake.phone_number()
    contact1_email = fake.email()

    contact2_name = fake.name()
    contact2_relation = random.choice(["Son", "Daughter", "Sister", "Brother", "Niece", "Nephew"])
    contact2_phone = fake.phone_number()
    contact2_email = fake.email()

    # Generate medical data
    diagnosis = get_random_diagnosis()
    medications = get_random_medications()
    allergies = get_random_allergies()
    clinical_flags = get_clinical_flags()
    dme_equipment = get_dme_equipment()

    # Generate vital signs
    systolic = random.randint(135, 170)
    diastolic = random.randint(70, 100)
    hr = random.randint(75, 115)
    temp = round(random.uniform(97.5, 99.8), 1)
    rr = random.randint(16, 26)
    spo2 = random.randint(88, 96)
    o2_delivery = random.choice(["2L NC", "3L NC", "Room air", "4L NC"])
    pain = f"{random.randint(3, 9)}/10"

    weight_lbs = random.randint(140, 280)
    weight_kg = round(weight_lbs * 0.453592, 1)
    height_inches = random.randint(60, 76)
    height_feet = height_inches // 12
    height_remaining = height_inches % 12
    height_cm = round(height_inches * 2.54, 1)
    bmi = round((weight_kg / ((height_cm/100) ** 2)), 1)

    # Lab values
    wbc = round(random.uniform(6.5, 15.2), 1)
    hgb = round(random.uniform(10.5, 15.8), 1)
    hct = round(random.uniform(32.0, 47.5), 1)
    platelets = random.randint(150, 380)

    na = random.randint(135, 145)
    k = round(random.uniform(3.5, 5.2), 1)
    cl = random.randint(98, 108)
    co2 = random.randint(20, 28)
    bun = random.randint(15, 45)
    creatinine = round(random.uniform(0.9, 2.1), 1)
    glucose = random.randint(95, 245)
    egfr = random.randint(35, 75)

    # Room assignment
    floor = random.choice(["2A", "2B", "3A", "3B", "4A", "4B"])
    room = random.randint(201, 499)

    # Realistic US-based hospital names (California and Colorado focus)
    hospital_names = [
        "Hoag Hospital",
        "UCLA Medical Center",
        "Stanford Hospital",
        "UCSF Medical Center",
        "Cedars-Sinai Medical Center",
        "Scripps Memorial Hospital",
        "Sharp Memorial Hospital",
        "Sutter Health",
        "Kaiser Permanente",
        "Providence St. Joseph Hospital",
        "Huntington Hospital",
        "City of Hope",
        "Children's Hospital Los Angeles",
        "Keck Hospital of USC",
        "UC Irvine Medical Center",
        "UC San Diego Health",
        "Cottage Hospital",
        "Dignity Health",
        "UCHealth University of Colorado Hospital",
        "Denver Health Medical Center",
        "Presbyterian/St. Luke's Medical Center",
        "Porter Adventist Hospital",
        "Swedish Medical Center",
        "Sky Ridge Medical Center",
        "Exempla Good Samaritan Medical Center"
    ]

    hospital_name = random.choice(hospital_names)
    # Extract short name for filename (first word or two before separator)
    hospital_short = hospital_name.split()[0]

    # Generate filename if not provided
    if filename is None:
        # Format: HOSPITALNAME-LASTNAME,FIRSTNAME.pdf
        safe_name = f"{hospital_short}-{last_name},{first_name}.pdf"
        # Remove any characters that might cause issues in filenames
        safe_name = safe_name.replace(" ", "_")
        filename = safe_name

    # Ensure output directory exists
    import os
    os.makedirs(output_dir, exist_ok=True)

    # Construct full output path
    full_output_path = os.path.join(output_dir, filename)

    # Create PDF document
    doc = SimpleDocTemplate(full_output_path, pagesize=letter,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)

    elements = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=6,
        alignment=TA_LEFT
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=10,
        spaceBefore=12
    )

    subsection_style = ParagraphStyle(
        'SubsectionHeader',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=colors.HexColor('#333333'),
        spaceAfter=6,
        spaceBefore=8
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        leading=14
    )

    small_style = ParagraphStyle(
        'Small',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666')
    )

    alert_style = ParagraphStyle(
        'Alert',
        parent=styles['Normal'],
        fontSize=10,
        backColor=colors.HexColor('#fff3cd'),
        borderColor=colors.HexColor('#ffc107'),
        borderWidth=1,
        borderPadding=10
    )

    # HEADER
    elements.append(Paragraph(hospital_name, title_style))
    elements.append(Paragraph(f"{hospital_address} | {hospital_city}, {hospital_state} {hospital_zip}<br/>Phone: {hospital_phone} | Fax: {hospital_fax}", small_style))
    elements.append(Spacer(1, 0.2*inch))

    # Title
    title_text = "PATIENT ADMISSION ASSESSMENT"
    elements.append(Paragraph(f"<para align=center><b>{title_text}</b></para>", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))

    # PATIENT DEMOGRAPHICS
    elements.append(Paragraph("PATIENT DEMOGRAPHICS", section_style))

    demo_data = [
        ["Patient Name:", full_name, "Date of Birth:", f"{dob_str} ({age} years)"],
        ["Medical Record #:", mrn, "Gender:", "Male" if gender == "M" else "Female"],
        ["Admission Date:", get_relative_date(7), "Admission Time:", datetime.now().strftime("%H:%M")],
        ["Primary Insurance:", primary_ins, "Secondary Insurance:", secondary_ins],
        ["Social Security #:", ssn, "Marital Status:", random.choice(["Married", "Single", "Widowed", "Divorced"])]
    ]

    demo_table = Table(demo_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
    demo_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    elements.append(demo_table)
    elements.append(Spacer(1, 0.15*inch))

    # ADMISSION INFORMATION
    elements.append(Paragraph("ADMISSION INFORMATION", section_style))

    admission_type = random.choice(["Direct Admission", "Emergency Department", "Transfer from another facility", "Elective Admission"])
    chief_complaint = random.choice([
        "Chest pain, shortness of breath",
        "Difficulty breathing, fever",
        "Altered mental status",
        "Severe weakness, fever",
        "Abdominal pain, nausea",
        "Fall with injury"
    ])

    admission_data = [
        ["Admission Type:", admission_type, "Attending Physician:", attending_dr],
        ["Admission Source:", random.choice(["Emergency Department", "Direct Admission", "Transfer"]), "Referring Physician:", referring_dr],
        ["Chief Complaint:", chief_complaint, "Room Assignment:", f"{floor}-{room}"]
    ]

    admission_table = Table(admission_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
    admission_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    elements.append(admission_table)
    elements.append(Spacer(1, 0.15*inch))

    # DIAGNOSES
    elements.append(Paragraph("ADMITTING DIAGNOSES", section_style))
    elements.append(Paragraph("<b>Primary Diagnosis:</b>", subsection_style))
    elements.append(Paragraph(f"• {diagnosis['primary']}", normal_style))
    elements.append(Spacer(1, 0.1*inch))

    elements.append(Paragraph("<b>Secondary Diagnoses:</b>", subsection_style))
    diagnoses_text = "<br/>".join([f"• {d}" for d in diagnosis['secondary']])
    elements.append(Paragraph(diagnoses_text, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # ALLERGIES (Alert Box)
    allergy_lines = [f"• {allergy[0]} → {allergy[1]}" for allergy in allergies]
    allergy_text = "<b>⚠ ALLERGIES:</b><br/>" + "<br/>".join(allergy_lines)
    elements.append(Paragraph(allergy_text, alert_style))
    elements.append(Spacer(1, 0.15*inch))

    # VITAL SIGNS ON ADMISSION
    elements.append(Paragraph("VITAL SIGNS ON ADMISSION", section_style))

    vital_data = [
        ["BP", "HR", "Temp (°F)", "RR", "SpO2", "Pain Level"],
        [f"{systolic}/{diastolic}", str(hr), str(temp), str(rr), f"{spo2}% {o2_delivery}", f"{pain}"]
    ]

    vital_table = Table(vital_data, colWidths=[1.2*inch, 1*inch, 1.2*inch, 1*inch, 1.2*inch, 1.4*inch])
    vital_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f5f5f5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor('#dddddd')),
    ]))
    elements.append(vital_table)
    elements.append(Paragraph(f"<i>Weight: {weight_lbs} lbs ({weight_kg} kg) | Height: {height_feet}'{height_remaining}\" ({height_cm} cm) | BMI: {bmi}</i>", small_style))
    elements.append(Spacer(1, 0.15*inch))

    # ADMISSION MEDICATIONS
    elements.append(Paragraph("HOME MEDICATIONS (Patient Report)", section_style))

    med_data = [["Medication", "Dose", "Route", "Frequency", "Last Taken"]]
    for med in medications:
        last_taken = random.choice([
            get_relative_date(-1) + " AM",
            get_relative_date(-1) + " PM",
            get_relative_date(0) + " AM",
            f"{get_relative_date(0)} {datetime.now().strftime('%H:%M')}"
        ])
        med_data.append([med[0], med[1], med[2], med[3], last_taken])

    med_table = Table(med_data, colWidths=[1.5*inch, 1*inch, 0.8*inch, 1.2*inch, 1.8*inch])
    med_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f5f5f5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor('#dddddd')),
    ]))
    elements.append(med_table)
    elements.append(Spacer(1, 0.15*inch))

    # PAGE BREAK
    elements.append(PageBreak())

    # ADMISSION LABS
    elements.append(Paragraph("ADMISSION LABORATORY RESULTS", section_style))
    elements.append(Paragraph("<b>Complete Blood Count:</b>", subsection_style))
    elements.append(Paragraph(f"WBC: {wbc} K/µL | Hgb: {hgb} g/dL | Hct: {hct}% | Platelets: {platelets} K/µL", normal_style))
    elements.append(Spacer(1, 0.1*inch))

    elements.append(Paragraph("<b>Basic Metabolic Panel:</b>", subsection_style))
    elements.append(Paragraph(f"Na: {na} mEq/L | K: {k} mEq/L | Cl: {cl} mEq/L | CO2: {co2} mEq/L<br/>BUN: {bun} mg/dL | Creatinine: {creatinine} mg/dL | Glucose: {glucose} mg/dL | eGFR: {egfr} mL/min", normal_style))
    elements.append(Spacer(1, 0.1*inch))

    # Additional labs based on diagnosis type
    if "cardiac" in str(diagnosis):
        troponin = round(random.uniform(0.4, 2.5), 2)
        ck_mb = round(random.uniform(5.0, 15.0), 1)
        bnp = random.randint(200, 650)
        elements.append(Paragraph("<b>Cardiac Markers:</b>", subsection_style))
        elements.append(Paragraph(f"Troponin I: {troponin} ng/mL (elevated) | CK-MB: {ck_mb} ng/mL | BNP: {bnp} pg/mL", normal_style))
        elements.append(Spacer(1, 0.1*inch))

        total_chol = random.randint(180, 280)
        ldl = random.randint(100, 180)
        hdl = random.randint(30, 60)
        trig = random.randint(120, 280)
        elements.append(Paragraph("<b>Lipid Panel:</b>", subsection_style))
        elements.append(Paragraph(f"Total Cholesterol: {total_chol} mg/dL | LDL: {ldl} mg/dL | HDL: {hdl} mg/dL | Triglycerides: {trig} mg/dL", normal_style))

    elements.append(Spacer(1, 0.15*inch))

    # DIAGNOSTIC STUDIES
    elements.append(Paragraph("DIAGNOSTIC STUDIES", section_style))

    elements.append(Paragraph("<b>ECG Findings:</b>", subsection_style))
    ecg_findings = random.choice([
        f"Sinus tachycardia at {hr} bpm, ST-segment depression in leads V3-V6 (0.5-1mm), no acute ST elevation",
        f"Normal sinus rhythm at {hr} bpm, no acute ST-T wave changes",
        f"Atrial fibrillation with rapid ventricular response, rate {hr} bpm",
        "Sinus rhythm with frequent PVCs, no acute ischemic changes"
    ])
    elements.append(Paragraph(ecg_findings, normal_style))
    elements.append(Spacer(1, 0.1*inch))

    elements.append(Paragraph("<b>Chest X-Ray:</b>", subsection_style))
    xray_findings = random.choice([
        "Mild cardiomegaly, no acute infiltrates, no pulmonary edema, mild hyperinflation consistent with COPD",
        "Right lower lobe infiltrate concerning for pneumonia, no pleural effusion",
        "Bilateral pleural effusions, pulmonary vascular congestion",
        "Clear lung fields, normal cardiac silhouette, no acute findings"
    ])
    elements.append(Paragraph(xray_findings, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # PHYSICAL EXAMINATION
    elements.append(Paragraph("ADMISSION PHYSICAL EXAMINATION", section_style))

    elements.append(Paragraph("<b>General:</b> Alert, oriented x4, " + random.choice(["in moderate distress", "in no acute distress", "in mild distress", "appears ill"]), normal_style))
    elements.append(Paragraph("<b>HEENT:</b> Normocephalic, atraumatic, PERRLA, mucous membranes " + random.choice(["moist", "dry"]), normal_style))
    elements.append(Paragraph("<b>Cardiovascular:</b> " + random.choice(["Tachycardic", "Regular rate and rhythm", "Irregular rhythm"]) + ", " + random.choice(["no murmurs", "systolic murmur heard", "S3 gallop present"]) + ", peripheral pulses 2+ bilaterally", normal_style))
    elements.append(Paragraph("<b>Respiratory:</b> " + random.choice(["Clear to auscultation bilaterally", "Decreased breath sounds bilaterally", "Crackles at bases bilaterally", "Scattered wheezes"]) + ", respiratory effort " + random.choice(["normal", "labored", "increased"]), normal_style))
    elements.append(Paragraph("<b>Abdomen:</b> Soft, " + random.choice(["non-tender", "tender in RLQ", "diffusely tender"]) + ", non-distended, normoactive bowel sounds", normal_style))
    elements.append(Paragraph("<b>Extremities:</b> " + random.choice(["No edema", "1+ bilateral edema", "2+ bilateral lower extremity edema"]) + ", no cyanosis, warm and well-perfused", normal_style))
    elements.append(Paragraph("<b>Neurological:</b> Grossly intact, moving all extremities, " + random.choice(["no focal deficits", "left-sided weakness noted", "right-sided weakness noted"]), normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # ASSESSMENT AND PLAN
    elements.append(Paragraph("ASSESSMENT AND INITIAL PLAN", section_style))

    gender_full = "male" if gender == "M" else "female"
    plan = f"""{age}-year-old {gender_full} presenting with {chief_complaint.lower()}. Patient has multiple comorbidities including {', '.join(diagnosis['secondary'][:3]).lower()}. Will admit for close monitoring and medical management.<br/><br/>
    <b>Plan:</b><br/>
    • Continuous monitoring as appropriate<br/>
    • Serial labs and vital signs monitoring<br/>
    • Specialty consultation as needed<br/>
    • Medication reconciliation and adjustment<br/>
    • DVT prophylaxis per protocol<br/>
    • Fall precautions<br/>
    • Dietary modifications as appropriate<br/>
    • Social work/case management consultation<br/>
    • Physical/occupational therapy evaluation<br/>
    • Discharge planning to begin"""

    elements.append(Paragraph(plan, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # EMERGENCY CONTACTS
    elements.append(Paragraph("EMERGENCY CONTACTS", section_style))

    contact_data = [
        ["Primary Contact:", "Secondary Contact:"],
        [f"{contact1_name} ({contact1_relation})", f"{contact2_name} ({contact2_relation})"],
        [f"Phone: {contact1_phone}", f"Phone: {contact2_phone}"],
        [f"Email: {contact1_email}", f"Email: {contact2_email}"],
        [f"Relationship: {contact1_relation}", f"Relationship: {contact2_relation}"]
    ]

    contact_table = Table(contact_data, colWidths=[3.5*inch, 3.5*inch])
    contact_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(contact_table)
    elements.append(Spacer(1, 0.15*inch))

    # CODE STATUS
    elements.append(Paragraph("CODE STATUS & ADVANCE DIRECTIVES", section_style))
    code_status = random.choice(["Full Code", "DNR", "DNR/DNI"])
    code = f"""• <b>Code Status:</b> {code_status}<br/>
    • <b>Healthcare Proxy:</b> {contact1_name} ({contact1_relation})<br/>
    • <b>Advance Directive:</b> {"On file" if random.random() > 0.5 else "Verbal discussion completed"}<br/>
    • <b>POLST:</b> {"On file" if code_status != "Full Code" else "Not applicable at this time"}"""
    elements.append(Paragraph(code, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # SOCIAL HISTORY
    elements.append(Paragraph("SOCIAL HISTORY", section_style))

    living_situations = [
        "Lives alone in single-story home",
        "Lives with spouse in two-story home",
        "Lives with family members",
        "Lives in assisted living facility",
        "Lives with daughter"
    ]

    occupations = [
        "Retired teacher",
        "Retired electrician",
        "Retired nurse",
        "Retired accountant",
        "Retired factory worker",
        "Retired construction worker"
    ]

    tobacco_status = random.choice([
        f"Former smoker, {random.randint(15, 40)} pack-year history, quit {random.randint(1, 15)} years ago",
        "Current smoker, 1 pack per day",
        "Never smoker"
    ])

    alcohol_status = random.choice([
        "Social drinker, 2-3 drinks per week",
        "Denies alcohol use",
        "Occasional drinker, less than 1 drink per week"
    ])

    social = f"""• <b>Living Situation:</b> {random.choice(living_situations)}<br/>
    • <b>Occupation:</b> {random.choice(occupations)}<br/>
    • <b>Tobacco:</b> {tobacco_status}<br/>
    • <b>Alcohol:</b> {alcohol_status}<br/>
    • <b>Recreational Drugs:</b> Denies<br/>
    • <b>Support System:</b> {random.choice(["Family nearby and involved", "Limited support system", "Strong family support", "Lives independently with minimal support"])}"""
    elements.append(Paragraph(social, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # FUNCTIONAL STATUS
    elements.append(Paragraph("FUNCTIONAL STATUS & COGNITIVE ASSESSMENT", section_style))

    baseline_adl = random.choice(["Independent with all activities of daily living", "Requires assistance with bathing and dressing", "Independent with minimal assistance", "Requires extensive assistance with ADLs"])
    mobility_status = random.choice(["Ambulates independently without assistive device", "Uses walker for ambulation", "Uses cane for ambulation", "Wheelchair dependent", "Bedbound, requires 2-person assist for transfers"])
    cognition_status = random.choice(["Alert and oriented x4, manages own medications and finances", "Mild cognitive impairment, BIMS score 11", "Moderate impairment, requires cues for ADLs, BIMS score 8", "Early dementia, requires assistance with complex tasks"])

    functional = f"""• <b>Prior Level of Function:</b> {baseline_adl}<br/>
    • <b>Current Mobility:</b> {mobility_status}<br/>
    • <b>Cognitive Status:</b> {cognition_status}<br/>
    • <b>Exercise Tolerance:</b> {random.choice(["Good baseline", "Decreased over past months", "Limited due to shortness of breath", "Sedentary lifestyle"])}<br/>
    • <b>Communication:</b> {random.choice(["Clear verbal communication", "Hearing impaired - uses hearing aids", "Expressive aphasia noted", "Requires communication board"])}"""
    elements.append(Paragraph(functional, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # SECTION GG FUNCTIONAL ASSESSMENT
    if random.random() > 0.5:
        elements.append(Paragraph("<b>Section GG Functional Assessment (Admission Performance):</b>", subsection_style))
        gg_score_eating = random.choice(["06 - Independent", "05 - Setup/cleanup assistance", "04 - Supervision", "03 - Partial/moderate assistance"])
        gg_score_toileting = random.choice(["04 - Supervision", "03 - Partial/moderate assistance", "02 - Substantial/maximal assistance"])
        gg_score_transfer = random.choice(["03 - Partial/moderate assistance", "02 - Substantial/maximal assistance", "01 - Dependent"])
        gg_score_walking = random.choice(["04 - Supervision", "03 - Partial/moderate assistance", "02 - Substantial/maximal assistance", "01 - Dependent"])

        gg_assessment = f"""GG0130 Self-Care: Eating ({gg_score_eating}), Toileting hygiene ({gg_score_toileting})<br/>
        GG0170 Mobility: Bed-to-chair transfer ({gg_score_transfer}), Walking 10 feet ({gg_score_walking})<br/>
        <i>Note: Patient requires assist with lower body dressing due to hip precautions</i>"""
        elements.append(Paragraph(gg_assessment, normal_style))
        elements.append(Spacer(1, 0.15*inch))

    # PAGE BREAK
    elements.append(PageBreak())

    # THERAPY SERVICES & REHABILITATION NEEDS
    therapy_services = []
    if random.random() > 0.5:
        pt_freq = random.choice(["5x/week", "6x/week"])
        therapy_services.append(f"PT {pt_freq} - {random.choice(['Gait training', 'Transfer training', 'Strengthening'])}, using {random.choice(['walker', 'cane'])} with {random.choice(['supervision', 'minimal assist'])}")

    if random.random() > 0.6:
        ot_freq = random.choice(["3x/week", "5x/week"])
        therapy_services.append(f"OT {ot_freq} - ADL training, {random.choice(['dressing', 'bathing', 'grooming'])}")

    if random.random() > 0.7:
        therapy_services.append(f"ST 3x/week - {random.choice(['Dysphagia management, nectar-thick liquids', 'Cognitive therapy', 'Aphasia therapy'])}")

    if therapy_services:
        elements.append(Paragraph("THERAPY SERVICES", section_style))
        therapy_text = "<br/>".join([f"• {service}" for service in therapy_services])
        elements.append(Paragraph(therapy_text, normal_style))
        elements.append(Spacer(1, 0.15*inch))

    # CLINICAL FLAGS & SPECIAL CARE NEEDS
    has_flags = clinical_flags["green"] or clinical_flags["yellow"] or clinical_flags["red"]
    if has_flags:
        elements.append(Paragraph("CLINICAL FLAGS & SPECIAL CARE REQUIREMENTS", section_style))

        # Red flags (highest priority)
        if clinical_flags["red"]:
            for flag_name, flag_detail in clinical_flags["red"]:
                detail = flag_detail.format(get_relative_date(-5)) if '{}' in flag_detail else flag_detail
                elements.append(Paragraph(f"<b>🔴 {flag_name}:</b> {detail}", normal_style))

        # Yellow flags (moderate priority)
        if clinical_flags["yellow"]:
            for flag_name, flag_detail in clinical_flags["yellow"]:
                detail = flag_detail.format(get_relative_date(random.randint(-10, -3)), get_relative_date(random.randint(8, 15))) if flag_detail.count('{}') == 2 else (flag_detail.format(get_relative_date(-5)) if '{}' in flag_detail else flag_detail)
                elements.append(Paragraph(f"<b>🟡 {flag_name}:</b> {detail}", normal_style))

        # Green flags (routine monitoring)
        if clinical_flags["green"]:
            for flag_name, flag_detail in clinical_flags["green"]:
                detail = flag_detail.format(get_relative_date(random.randint(8, 14))) if '{}' in flag_detail else flag_detail
                elements.append(Paragraph(f"<b>🟢 {flag_name}:</b> {detail}", normal_style))

        elements.append(Spacer(1, 0.15*inch))

    # DME & EQUIPMENT NEEDS
    if dme_equipment:
        elements.append(Paragraph("EQUIPMENT NEEDS", section_style))
        dme_text = "<br/>".join([f"• {item}" for item in dme_equipment[:3]])  # Limit to 3 items
        elements.append(Paragraph(dme_text, normal_style))
        elements.append(Spacer(1, 0.15*inch))

    # TRANSFER GUIDELINES & CARE NEEDS
    elements.append(Paragraph("TRANSFER GUIDELINES & SPECIAL CARE NEEDS", section_style))
    transfer_toileting = random.choice(["Independent with bedside commode", "Requires 1-person assist to commode", "Requires 2-person assist, uses mechanical lift", "Uses brief, incontinent of bowel/bladder"])
    transfer_bathing = random.choice(["Shower with supervision", "Bed bath, requires assistance", "Shower chair with 1-person assist", "Mechanical lift required"])

    transfer_text = f"""• <b>Toileting:</b> {transfer_toileting}<br/>
    • <b>Bathing:</b> {transfer_bathing}<br/>
    • <b>Bed Mobility:</b> {random.choice(['Independent', 'Requires 1-person assist for repositioning', 'Requires 2-person assist, turn q2h for pressure relief'])}<br/>
    • <b>Transfers:</b> {random.choice(['Modified independent with walker', 'Stand-pivot transfer with 1-person assist', '2-person assist or mechanical lift required'])}<br/>
    • <b>Nutrition:</b> {random.choice(['Regular diet, self-feeds', 'Mechanical soft, nectar-thick liquids', 'Pureed diet, supervision required', 'PEG tube feeds - Jevity 1.5 at 75mL/hr'])}"""
    elements.append(Paragraph(transfer_text, normal_style))
    elements.append(Spacer(1, 0.15*inch))

    # RECENT IMMUNIZATIONS
    if random.random() > 0.5:
        elements.append(Paragraph("RECENT IMMUNIZATIONS", section_style))
        immunization_date1 = get_relative_date(random.randint(-90, -30))
        imm_text = f"""• Influenza - {immunization_date1}<br/>
        • Pneumococcal (PPSV23) - {get_relative_date(random.randint(-180, -91))}"""
        if random.random() > 0.5:
            covid_date = get_relative_date(random.randint(-120, -60))
            imm_text += f"<br/>• COVID-19 Booster - {covid_date}"
        elements.append(Paragraph(imm_text, normal_style))
        elements.append(Spacer(1, 0.15*inch))

    # UPCOMING APPOINTMENTS & FOLLOW-UP
    if random.random() > 0.3:
        elements.append(Paragraph("FOLLOW-UP APPOINTMENTS", section_style))
        appt_date1 = get_relative_date(random.randint(8, 14))
        appt_date2 = get_relative_date(random.randint(15, 25))

        specialties = ["Cardiology", "Orthopedics", "Neurology", "Wound Care", "Primary Care"]
        selected_specialties = random.sample(specialties, k=2)

        appointments = f"""• {selected_specialties[0]} - {appt_date1} at {random.choice(['9:00 AM', '10:30 AM', '2:00 PM'])}<br/>
        • {selected_specialties[1]} - {appt_date2} at {random.choice(['9:30 AM', '11:00 AM', '2:30 PM'])}"""
        if random.random() > 0.6:
            appointments += f"<br/>• Lab work (CBC, BMP) - Due {get_relative_date(random.randint(6, 10))}"

        elements.append(Paragraph(appointments, normal_style))
        elements.append(Spacer(1, 0.15*inch))

    # NUTRITIONAL STATUS (simplified, sometimes included)
    if random.random() > 0.6:
        elements.append(Paragraph("NUTRITION", section_style))
        meal_intake = random.choice(["75%", "60%", "50%"])
        nutrition = f"""• Diet: {random.choice(['Regular', 'Cardiac', 'Diabetic', 'Mechanical soft'])} - Intake {meal_intake}%<br/>
        • {random.choice([f'Weight stable', f'5% weight loss past 30 days', 'Supplements: Ensure BID'])}"""
        elements.append(Paragraph(nutrition, normal_style))
        elements.append(Spacer(1, 0.15*inch))

    elements.append(Spacer(1, 0.2*inch))

    # SIGNATURE
    elements.append(Paragraph("_" * 50, normal_style))
    attending_npi = generate_npi()
    signature = f"""<b>{attending_dr}, FACC</b><br/>
    Attending Physician<br/>
    Date: {get_relative_date(7)} | Time: {datetime.now().strftime("%H:%M")}<br/>
    NPI: {attending_npi}"""
    elements.append(Paragraph(signature, normal_style))
    elements.append(Spacer(1, 0.2*inch))

    # FOOTER
    footer_text = f"""<para align=center>
    This document contains confidential patient information protected under HIPAA.<br/>
    For questions regarding this admission, please contact the admitting physician or case management at {hospital_phone}.<br/>
    Document ID: ADM-{mrn.split('-')[1]}-{datetime.now().strftime("%Y%m%d%H%M")}
    </para>"""
    elements.append(Paragraph(footer_text, small_style))

    # Build PDF
    doc.build(elements)
    print(f"✓ PDF generated successfully: {full_output_path}")
    print(f"  Patient: {full_name}")
    print(f"  MRN: {mrn}")
    print(f"  SSN: {ssn}")
    return full_output_path


if __name__ == "__main__":
    # Generate the PDF with automatic filename
    output_file = generate_admission_document()
    print(f"\nDocument ready for admissions software testing.")
    print(f"File location: {output_file}")