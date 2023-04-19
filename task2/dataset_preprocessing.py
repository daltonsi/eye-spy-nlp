import pandas as pd
import re
from collections import Counter

SOURCE_PATH = '/home/daltonsi/eye-spy-nlp/source_data/mtsamples_opthamal.csv'



LABEL_MAPPINGS = {
    'SUBJECTIVE': 'SUBJECTIVE',
    'CHIEF COMPLAINT': 'SUBJECTIVE',
    'REASON FOR VISIT': 'SUBJECTIVE',
    'HISTORY OF PRESENT ILLNESS': 'SUBJECTIVE',
    'PLAN': 'PLAN',
    'PLANS': 'PLAN',
    'ASSESSMENT': 'PLAN',
    'IMPRESSION': 'PLAN',
    'ANESTHESIA': 'ANESTHESIA',
    'ANESTHESIA TYPE': 'ANESTHESIA',
    'OBJECTIVE': 'OBJECTIVE',
    'EYE EXAM': 'OBJECTIVE',
    'PHYSICAL EXAMINATION': 'OBJECTIVE',
    'OCULAR FINDINGS': 'OBJECTIVE',
    'VISUAL ACUITY': 'OBJECTIVE',
    'FINDINGS': 'OBJECTIVE',
    'IMPLANTS': 'OBJECTIVE',
    'HISTORY': 'HISTORY',
    'DOB': 'HISTORY',
    'FAMILY HISTORY': 'HISTORY',
    'SOCIAL HISTORY': 'HISTORY',
    'PAST SURGICAL HISTORY': 'HISTORY',
    'PAST OCULAR HISTORY': 'HISTORY',
    'PAST MEDICAL HISTORY': 'HISTORY',
    'MEDICATION': 'MEDICATION',
    'MEDICATION HISTORY': 'MEDICATION',
    'MEDICATIONS': 'MEDICATION',
    'ALLERGIES': 'ALLERGIES',
    'PROCEDURE': 'PROCEDURE',
    'PROCEDURES': 'PROCEDURE',
    'OPERATIVE PROCEDURE': 'PROCEDURE',
    'OPERATIONS PERFORMED': 'PROCEDURE',
    'OPERATIVE TECHNIQUE': 'PROCEDURE',
    'OPERATIVE PROCEDURES': 'PROCEDURE',
    'TITLE OF OPERATION': 'PROCEDURE',
    'PROCEDURE PERFORMED': 'PROCEDURE',
    'PROCEDURE IN DETAIL': 'PROCEDURE',
    'DESCRIPTION OF OPERATION': 'PROCEDURE',
    'PROCEDURE DETAILS': 'PROCEDURE',
    'DESCRIPTION OF THE OPERATION': 'PROCEDURE',
    'DESCRIPTION OF PROCEDURE': 'PROCEDURE',
    'OPERATIVE PROCEDURE IN DETAIL': 'PROCEDURE',
    'OPERATION': 'PROCEDURE',
    'PROCEDURE NOTE': 'PROCEDURE',
    'OPERATION PERFORMED': 'PROCEDURE',
    'NAME OF PROCEDURE': 'PROCEDURE',
    'COMPLICATIONS': 'COMPLICATIONS',
    'INDICATIONS FOR OPERATION': 'DIAGNOSIS',
    'INDICATIONS FOR PROCEDURE': 'DIAGNOSIS',
    'PREOPERATIVE DIAGNOSIS': 'DIAGNOSIS',
    'PREOPERATIVE DX': 'DIAGNOSIS',
    'INDICATIONS FOR SURGERY': 'DIAGNOSIS',
    'PREOP DIAGNOSIS': 'DIAGNOSIS',
    'POSTOPERATIVE DX': 'DIAGNOSIS',
    'POSTOPERATIVE DIAGNOSIS': 'DIAGNOSIS',
    'PREOPERATIVE DIAGNOSES': 'DIAGNOSIS',
    'PREOPERATIVE FINDINGS': 'DIAGNOSIS',
    'INDICATION': 'DIAGNOSIS',
    'INDICATIONS': 'DIAGNOSIS',
    'POSTOP DIAGNOSIS': 'DIAGNOSIS',
    'POSTOPERATIVE DIAGNOSES': 'DIAGNOSIS',
    'INDICATION': 'DIAGNOSIS',
    'INDICATION FOR SURGERY': 'DIAGNOSIS',
    'OTHER': 'OTHER',
    'BLOOD LOSS': 'OTHER',
    'ESTIMATED BLOOD LOSS': 'OTHER',
    'OD': 'OTHER',
    'RE': 'OTHER',
    'IOL': 'OTHER',
    'XYZ': 'OTHER',
    'OS': 'OTHER',
    'OU': 'OTHER',
    'SPECIMEN': 'OTHER',
    'SPECIMENS': 'OTHER',
    'PMH': 'OTHER',
    'IOP': 'OTHER',
    'REVIEW OF SYSTEMS': 'OTHER',
    'PATIENT INSTRUCTIONS': 'OTHER',
    'PHACOEMULSIFICATION TIME': 'OTHER',
    'INFORMED CONSENT': 'OTHER',
    'LENS IMPLANT USED': 'OTHER',
    'DISCHARGE': 'OTHER',
    'PHACO TIME': 'OTHER',
    'CONDITION': 'OTHER',
    'TEST RESULTS': 'OTHER',
    'INTRAOCULAR LENS': 'OTHER',
    'TO PREVENT THE SPREAD OF THE INFECTION': 'OTHER',
    'REFRACTION': 'OTHER',
    'ASSISTANT': 'OTHER',
    'NARRATIVE': 'OTHER',
    'PROS DEV IMPLANT': 'OTHER',
}


def parse_headings():

    headings = []

    df = pd.read_csv(SOURCE_PATH, index_col=0)

    # Retrieve all header in source data
    for row in df['transcription'].iloc[:].items():
        try:
            idx, text = row

            reg_headers = r'[A-Z][A-Z ]+:'

            headings += re.findall(reg_headers, text)
        except:
            print(row)

    print(Counter([i.strip(':') for i in headings]))
    return list(i.strip(':') for i in set(headings))


def main():
    labels = parse_headings()

    for label in labels:
        print(label)




    # df_stripped = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
	# opthamal_mask = df_stripped['medical_specialty'] == 'Ophthalmology'
	# opthamal_df = df[opthamal_mask]
    #
	# conditions = [
	# 	(opthamal_df['sample_name'].str.contains('Cataract')==True)
	# ]
    #
	# values = ['cataract']
    #
    #
	# opthamal_df['label'] = np.select(conditions,values)
    #
    #
    #
	# opthamal_df.to_csv('source_data/mtsamples_opthamal.csv')






if __name__ == '__main__':
    main()
