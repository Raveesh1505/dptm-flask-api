MEDICINE_EXTRACTION_PROMPT = """
You are a smart medical tool. When given a prescription, extract only the medicines prescribed and nothing else.
"""

MEDICINE_TRANSLATION_PROMPT = """
You are a smart medical tool. When provided with prescribed medicines, return a profile for each. Include salt name, uses, side effects, precautions, etc., in simple language.
"""

TEST_MESSAGE = """
Dr. Rahul Sharma, MD
General Physician
ABC Hospital, New Delhi
Phone: +91-9876543210
Email: drrahulsharma@abchospital.com

Patient Details:
Name: Mr. Amit Verma
Age: 32 years
Gender: Male
Date: 16-Feb-2025

Medical Prescription

Diagnosis: Viral Fever

Medications:
 1. Paracetamol 500 mg – Take one tablet every 6 hours (if fever exceeds 100°F) after food.
 2. Cetirizine 10 mg – Take one tablet at night for 3 days (if experiencing cold symptoms).
 3. Pantoprazole 40 mg – Take one tablet in the morning before breakfast for 5 days (to prevent acidity).
 4. ORS (Oral Rehydration Solution) – 1 sachet in 1 liter of water, sip throughout the day to prevent dehydration.

Additional Instructions:
 • Drink plenty of fluids and rest adequately.
 • Monitor fever with a thermometer every 6 hours.
 • If fever exceeds 102°F or persists for more than 3 days, consult a doctor.
 • Avoid cold drinks and spicy food.

Doctor’s Signature:
Dr. Rahul Sharma
(MCI Reg. No: 12345678)
"""