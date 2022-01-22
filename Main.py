from flask import Flask, jsonify
x={
    "ablify":{"Name":"Ablify","Use":"Abilify is used to treat certain mental/mood conditions (such as depression, bipolar disorder, schizophrenia, Tourette's syndrome, and irritability associated with autistic disorder)"},
    "absorica":{"Name":"Absorica","Use":"This drug is used to treat severe cystic acne (also known as nodular acne)"},
    "acarbose":{"Name":"Acarbose","Use":"Acarbose medications are used for the treatment of Type 2 diabetes. This helps in lowering the blood sugar together with diet and exercise."},
    "acebutolol":{"Name":"Acebutolol","Use":"Acebutolol is used for treating high blood pressure and pulse irregularities (arrhythmia)"},
    "aceclofenac":{"Name":"Aceclofenac","Use":"Aceclofenac is used to relieve pain. It relieves pain and inflammation in conditions such as rheumatoid arthritis, ankylosing spondylitis, and osteoarthritis"},
    "acyclovir":{"Name":"Acyclovir","Use":"Acyclovir is an antiviral drug which slows the development and spread of the herpes virus. It won't cure herpes, but the symptoms of the infection can be diminished"},
    "adapalene":{"Name":"Adapalene","Use":"For the treatment of acne, this drug is used"},
    "adderall":{"Name":"Adderall","Use":"Adderall is used to treat attention deficit hyperactivity disorder"},
    "alcaftadine":{"Name":"Alcaftadine","Use":"This drug is used to prevent allergies from causing scratching in the eyes"},
    "aldactone":{"Name":"Aldactone","Use":"Aldactone is used to treat elevated blood pressure (hypertension), heart failure or hypokalemia (low potassium levels in the blood). Aldactone also treats fluid retention (edema)"},
    "aleve":{"Name":"Aleve","Use":"It is used in the treatment of a variety of pain conditions, including headaches, muscle aches, tendonitis, dental pain, and menstrual cramps. It also alleviates the pain, swelling, and stiffness associated with arthritis, bursitis, and gout attacks"},
    "alfacalcidol":{"Name":"Alfacalcidol","Use":"Alfacalcidol is a vitamin D supplement used to treat deficiency in conditions including hypocalcemia (low blood calcium levels), rickets (bone weakness), and others"},
    "allantoin":{"Name":"Allantoin","Use":"It is used as a moisturizer for the treatment of dry, rough, scaly, itchy skin and minor skin irritation like rashes, skin burns from radiation therapy"},
    "allopurinol":{"Name":"Allopurinol","Use":"Allopurinol is used for the treatment of gout and certain types of kidney stones"},
    "alprax":{"Name":"Alprax","Use":"Alprax Tablet is an effective medication used to treat panic attacks and anxiety disorders caused by depression"},
    "alprazolam":{"Name":"Alprazolam","Use":"Alprazolam is used to treat anxiety and panic disorders"},
    "altraday":{"Name":"Altraday","Use":"This drug is used to treat painful rheumatic conditions like osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis"},
    "ambien":{"Name":"Ambien","Use":"Zolpidem is used to treat certain sleep problems (insomnia) in adults"},
    "ambroxol":{"Name":"Ambroxol","Use":"This drug is used for the symptomatic treatment of tracheobronchitis, an infection that induces tracheal (windpipe) and pulmonary airway inflammation"},
    "amikacin":{"Name":"Amikacin","Use":"This medicine is used to prevent or treat a wide range of bacterial infections"},
    "aminophylline":{"Name":"Aminophylline","Use":"Aminophylline is used to prevent and treat asthma, chronic bronchitis, emphysema, and other lung disorders caused by wheezing, shortness of breath, and trouble breathing"},
    "amiodarone":{"Name":"Amiodarone","Use":"This medication is used for treating serious irregular heartbeats"},
    "amitiza":{"Name":"Amitiza","Use":"This medicine is being used to improve the symptoms of constipation"},
    "amitriptyline":{"Name":"Amitriptyline","Use":"To treat mood disorders such as depression, this drug is used"},
    "amoxicillin":{"Name":"Amoxicillin","Use":"Amoxicillin is used to treat bacterial infections, like tonsillitis, bronchitis, pneumonia, and infections in ear, nose, throat, skin, or urinary tract"},
    "anafortan":{"Name":"Anafortan","Use":"Anafortan is used in relieving symptoms such as severe stomach pain, bloating, cramps, etc."},
    "analgin":{"Name":"Analgin","Use":"Analgin is a pain-killer and anti-pyretic"},
    "anastrozole":{"Name":"Anastrozole","Use":"Anastrozole is used in conjunction with other therapies, such as surgery or radiation for the treatment of early breast cancer in postmenopausal women"},
    "alfuzosin":{"Name":"Alfuzosin","Use":" It is used to treat the signs and symptoms of benign prostate enlargement (benign prostatic hyperplasia or BPH)"},
    "apixaban":{"Name":"Apixaban","Use":"Apixaban is used to help prevent strokes and blood clots in people who are having atrial fibrillation and this disease is not caused by heart valve disease"},
    "aquasol":{"Name":"Aquasol","Use":"Aquasol is used for preventing low levels of vitamin in the people who don’t get enough of the vitamin from their diets"},
    "aripiprazole":{"Name":"Aripiprazole","Use":"Aripiprazole is a drug that is used to relieve the effects of schizophrenia. It's also used to treat symptoms of mania and depression in adults and children with bipolar disorder"},
    "aristozyme":{"Name":"Aristozyme","Use":"It is used for the treatment of biological process disorders, swelling within the abdomen, Starch degrading accelerator, Hiccups, and inflammation within the abdomen"},
    }
app=Flask(__name__)
@app.route('/teamnexus/q=<string:j>')
def hello_world(j):
    return x[j]
if __name__ == "__main__":
    app.run(debug=True)
