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

def generate_admission_document(filename=None):
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

    hospital_name = f"{fake.last_name().upper()} MEDICAL CENTER"

    # Generate filename if not provided
    if filename is None:
        # Format: LASTNAME_FIRSTNAME_MMDDYYYY.pdf
        safe_name = f"{last_name}_{first_name}_{datetime.now().strftime('%m%d%Y')}.pdf"
        # Remove any characters that might cause issues in filenames
        safe_name = safe_name.replace(" ", "_").replace(",", "")
        filename = safe_name

    # Create PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter,
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
        ["Admission Date:", get_relative_date(0), "Admission Time:", datetime.now().strftime("%H:%M")],
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
    elements.append(Paragraph("FUNCTIONAL STATUS", section_style))
    functional = f"""• <b>Baseline ADLs:</b> {random.choice(["Independent with all activities of daily living", "Requires assistance with bathing and dressing", "Independent with minimal assistance"])}<br/>
    • <b>Mobility:</b> {random.choice(["Ambulates independently without assistive device", "Uses walker for ambulation", "Uses cane for ambulation", "Wheelchair dependent"])}<br/>
    • <b>Cognition:</b> {random.choice(["Alert and oriented, manages own medications and finances", "Mild cognitive impairment", "Early dementia, requires assistance with complex tasks"])}<br/>
    • <b>Exercise Tolerance:</b> {random.choice(["Good baseline", "Decreased over past months", "Limited due to shortness of breath", "Sedentary lifestyle"])}"""
    elements.append(Paragraph(functional, normal_style))
    elements.append(Spacer(1, 0.3*inch))

    # SIGNATURE
    elements.append(Paragraph("_" * 50, normal_style))
    attending_npi = generate_npi()
    signature = f"""<b>{attending_dr}, FACC</b><br/>
    Attending Physician<br/>
    Date: {get_relative_date(0)} | Time: {datetime.now().strftime("%H:%M")}<br/>
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
    print(f"✓ PDF generated successfully: {filename}")
    print(f"  Patient: {full_name}")
    print(f"  MRN: {mrn}")
    print(f"  SSN: {ssn}")
    return filename


if __name__ == "__main__":
    # Generate the PDF with automatic filename
    output_file = generate_admission_document()
    print(f"\nDocument ready for admissions software testing.")
    print(f"File location: {output_file}")