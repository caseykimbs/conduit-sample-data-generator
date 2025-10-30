"""
Medication Orders Sample Document PDF Generator
Generates professional medication order documents with randomized realistic sample data
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import datetime, timedelta
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker()

def generate_npi():
    """Generate a random 10-digit NPI"""
    return f"{random.randint(1000000000, 9999999999)}"

def get_relative_date(days_offset):
    """Generate relative date descriptions with actual date"""
    target_date = datetime.now() + timedelta(days=days_offset)
    date_str = target_date.strftime("%m/%d/%Y")
    return date_str

def get_current_medications():
    """Generate random current maintenance medications"""
    med_pool = [
        ("Lisinopril", "10mg", "tablet", "Take 1 tablet by mouth once daily", "high blood pressure", random.randint(3, 11)),
        ("Lisinopril", "20mg", "tablet", "Take 1 tablet by mouth once daily", "high blood pressure", random.randint(3, 11)),
        ("Metformin", "500mg", "tablet", "Take 1 tablet by mouth twice daily with meals", "diabetes", random.randint(3, 11)),
        ("Metformin", "1000mg", "tablet", "Take 1 tablet by mouth twice daily with meals", "diabetes", random.randint(3, 11)),
        ("Atorvastatin", "20mg", "tablet", "Take 1 tablet by mouth at bedtime", "high cholesterol", random.randint(3, 11)),
        ("Atorvastatin", "40mg", "tablet", "Take 1 tablet by mouth at bedtime", "high cholesterol", random.randint(3, 11)),
        ("Metoprolol", "50mg", "tablet", "Take 1 tablet by mouth twice daily", "heart condition", random.randint(3, 11)),
        ("Omeprazole", "20mg", "capsule", "Take 1 capsule by mouth once daily before breakfast", "acid reflux", random.randint(3, 11)),
        ("Levothyroxine", "75mcg", "tablet", "Take 1 tablet by mouth once daily on empty stomach", "thyroid condition", random.randint(3, 11)),
        ("Amlodipine", "5mg", "tablet", "Take 1 tablet by mouth once daily", "high blood pressure", random.randint(3, 11)),
        ("Gabapentin", "300mg", "capsule", "Take 1 capsule by mouth three times daily", "nerve pain", random.randint(3, 11)),
        ("Sertraline", "50mg", "tablet", "Take 1 tablet by mouth once daily", "depression/anxiety", random.randint(3, 11)),
        ("Aspirin", "81mg", "tablet", "Take 1 tablet by mouth once daily", "heart health", random.randint(3, 11)),
        ("Furosemide", "40mg", "tablet", "Take 1 tablet by mouth once daily in the morning", "fluid retention", random.randint(3, 11)),
    ]

    num_meds = random.randint(3, 6)
    return random.sample(med_pool, k=num_meds)

def get_new_medications():
    """Generate random new medication orders"""
    new_med_pool = [
        ("Amoxicillin", "500mg", "capsule", "Take 1 capsule by mouth three times daily for 10 days", "infection", 0),
        ("Azithromycin", "250mg", "tablet", "Take 2 tablets by mouth on day 1, then 1 tablet daily for 4 days", "bacterial infection", 0),
        ("Cephalexin", "500mg", "capsule", "Take 1 capsule by mouth four times daily for 7 days", "skin infection", 0),
        ("Prednisone", "20mg", "tablet", "Take 3 tablets by mouth once daily for 5 days", "inflammation", 0),
        ("Methylprednisolone", "4mg", "dose pack", "Take as directed per package instructions", "inflammation", 0),
        ("Loratadine", "10mg", "tablet", "Take 1 tablet by mouth once daily as needed", "allergies", random.randint(2, 5)),
        ("Cetirizine", "10mg", "tablet", "Take 1 tablet by mouth once daily as needed", "allergies", random.randint(2, 5)),
        ("Ondansetron", "4mg", "tablet", "Take 1 tablet by mouth every 8 hours as needed", "nausea", random.randint(1, 3)),
        ("Tramadol", "50mg", "tablet", "Take 1-2 tablets by mouth every 4-6 hours as needed", "pain", random.randint(0, 2)),
        ("Cyclobenzaprine", "10mg", "tablet", "Take 1 tablet by mouth at bedtime as needed", "muscle spasm", random.randint(1, 3)),
        ("Mupirocin", "2%", "ointment", "Apply thin layer to affected area twice daily for 10 days", "skin infection", 0),
        ("Fluticasone", "50mcg", "nasal spray", "Spray 2 sprays in each nostril once daily", "allergies", random.randint(2, 5)),
        ("Albuterol", "90mcg", "inhaler", "Inhale 2 puffs every 4-6 hours as needed", "breathing difficulty", random.randint(2, 5)),
    ]

    num_new = random.randint(2, 4)
    return random.sample(new_med_pool, k=num_new)

def get_discontinued_medications():
    """Generate random discontinued medications"""
    if random.random() > 0.6:  # 40% chance of having discontinued meds
        return []

    disc_med_pool = [
        ("Hydrochlorothiazide", "25mg", "tablet", "Replaced with different medication"),
        ("Ibuprofen", "800mg", "tablet", "No longer needed"),
        ("Simvastatin", "20mg", "tablet", "Changed to Atorvastatin"),
        ("Losartan", "50mg", "tablet", "Side effects - rash"),
        ("Pantoprazole", "40mg", "tablet", "Changed to Omeprazole"),
        ("Warfarin", "5mg", "tablet", "Switched to newer anticoagulant"),
    ]

    num_disc = random.randint(1, 2)
    return random.sample(disc_med_pool, k=num_disc)

def generate_medication_orders(filename=None, output_dir="/Users/caseykimball/Documents/sample_docs"):
    """Generate medication orders PDF document"""

    # Generate physician info
    physician_first = fake.first_name()
    physician_last = fake.last_name()
    physician_name = f"Dr. {physician_first} {physician_last}, MD"
    physician_npi = generate_npi()

    # Select prescribing institution (physicians offices or pharmacies)
    institution_type = random.choice(["physician", "pharmacy"])

    if institution_type == "physician":
        physician_offices = [
            "Newport Beach Primary Care",
            "Orange County Family Medicine",
            "Irvine Medical Associates",
            "Coastal Internal Medicine",
            "South Bay Family Practice",
            "Westwood Primary Care Group",
            "Beverly Hills Medical Center",
            "Santa Monica Physicians",
            "Pasadena Internal Medicine",
            "Denver Family Care",
            "Colorado Springs Medical Group",
            "Boulder Primary Care"
        ]
        institution = random.choice(physician_offices)
    else:
        pharmacies = [
            "CVS Pharmacy #4529",
            "Walgreens Pharmacy #8721",
            "Rite Aid Pharmacy #3156",
            "Costco Pharmacy #294",
            "Safeway Pharmacy #1847",
            "Vons Pharmacy #2634",
            "Target Pharmacy #1829",
            "Albertsons Pharmacy #5472",
            "Ralphs Pharmacy #3891",
            "King Soopers Pharmacy #728"
        ]
        institution = random.choice(pharmacies)

    # Generate dates
    new_meds_date = get_relative_date(0)  # Today

    # Generate medications - only new medications
    new_medications = get_new_medications()

    # Generate filename if not provided
    if filename is None:
        # Extract short institution name for filename
        institution_short = institution.split()[0]  # e.g., "Hoag" from "Hoag Medical Group"
        safe_name = f"{institution_short}-new-meds.pdf"
        filename = safe_name

    # Ensure output directory exists
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
        fontSize=18,
        textColor=colors.HexColor('#1a472a'),
        spaceAfter=6,
        alignment=TA_CENTER
    )

    institution_style = ParagraphStyle(
        'Institution',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12,
        alignment=TA_CENTER
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#1a472a'),
        spaceAfter=10,
        spaceBefore=12
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

    # HEADER
    elements.append(Paragraph("PATIENT MEDICATION ORDERS", title_style))
    elements.append(Paragraph(institution, institution_style))
    elements.append(Spacer(1, 0.3*inch))

    # NEW MEDICATION ORDERS
    elements.append(Paragraph("NEW MEDICATION ORDERS:", section_style))

    for idx, (med_name, dose, form, instructions, indication, refills) in enumerate(new_medications, 1):
        med_text = f"""<b>{idx}. {med_name} {dose} {form}</b><br/>
        {instructions} for {indication}<br/>
        <i>Prescribed: {new_meds_date} | Refills: {refills}</i>"""
        elements.append(Paragraph(med_text, normal_style))
        elements.append(Spacer(1, 0.1*inch))

    elements.append(Spacer(1, 0.3*inch))

    # SIGNATURE
    elements.append(Paragraph("_" * 60, normal_style))
    elements.append(Spacer(1, 0.1*inch))
    signature = f"""<b>{physician_name}</b><br/>
    NPI: {physician_npi}<br/>
    Signature: ______________________________<br/>
    Date: {new_meds_date}"""
    elements.append(Paragraph(signature, normal_style))
    elements.append(Spacer(1, 0.2*inch))

    # FOOTER
    footer_text = f"""<para align=center>
    <i>This is a computer-generated document. Please verify all medications with your healthcare provider.<br/>
    For questions, contact {institution}.<br/>
    Document ID: MED-{random.randint(100000, 999999)}-{datetime.now().strftime("%Y%m%d%H%M")}</i>
    </para>"""
    elements.append(Paragraph(footer_text, small_style))

    # Build PDF
    doc.build(elements)
    print(f"✓ Medication Orders PDF generated: {full_output_path}")
    print(f"  Prescriber: {physician_name}")
    print(f"  Institution: {institution}")
    print(f"  New Orders: {len(new_medications)}")
    return full_output_path


if __name__ == "__main__":
    # Generate the medication orders PDF
    output_file = generate_medication_orders()
    print(f"\nMedication orders document ready.")
    print(f"File location: {output_file}")
