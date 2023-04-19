import pandas as pd
import re

SOURCE_PATH = '/home/daltonsi/eye-spy-nlp/source_data/mtsamples.csv'



LABEL_MAPPINGS = {
    'SUBJECTIVE': 'SUBJECTIVE',
    'PROCEDURE':'PROCEDURE',
    'FINDINGS AND PROCEDURE':'PROCEDURE',
    'OPERATIVE PROCEDURE': 'PROCEDURE',
    'PROCEDURES': 'PROCEDURE',
    'PROCEDURE IN DETAIL': 'PROCEDURE',
    'INDICATION FOR OPERATION': 'PROCEDURE',
    'OPERATION': 'PROCEDURE',
    'INDICATION FOR PROCEDURE': 'PROCEDURE',
    'ALLERGIES':'ALLERGIES',
    'ASSESSMENT':'ASSESSMENT',
    'DESCRIPTION': 'ASSESSMENT',
    'PHYSICAL EXAMINATION': 'ASSESSMENT',
    'IMPRESSION': 'IMPRESSION',
    'HISTORY': 'HISTORY',
    'HISTORY OF PRESENT ILLNESS': 'HISTORY',
    'EATING HISTORY': 'HISTORY',
    'SOCIAL HISTORY': 'HISTORY',
    'PAST MEDICAL HISTORY': 'HISTORY',
    'FAMILY HISTORY': 'HISTORY',
    'PAST SURGICAL HISTORY': 'HISTORY',
    'DIAGNOSIS': 'DIAGNOSIS',
    'POSTOPERATIVE DIAGNOSIS': 'DIAGNOSIS',
    'PREOPERATIVE DIAGNOSES': 'DIAGNOSIS',
    'POSTOPERATIVE DIAGNOSES': 'DIAGNOSIS',
    'PREOPERATIVE DIAGNOSIS': 'DIAGNOSIS',
    'OBJECTIVE': 'OBJECTIVE',
    'PLAN': 'PLAN',
    'ANESTHESIA': 'ANESTHESIA',
    'CURRENT MEDICATIONS': 'MEDICATIONS',
    'MEDICATIONS': 'MEDICATIONS',
    'IMAGING': 'IMAGING',
    'DOPPLER': 'IMAGING',
    'OTHER': 'OTHER',
    'HEENT': 'OTHER',
    'REVIEW OF SYSTEMS': 'OTHER',
    'MODE': 'OTHER',
}


def parse_headings():

    headings = []

    df = pd.read_csv(SOURCE_PATH, index_col=0)

    # Retrieve all header in source data
    for row in df['transcription'].iloc[:10].items():
        idx, text = row

        reg_headers = r'[A-Z][A-Z ]+:'

        headings += re.findall(reg_headers, text)

    return list(i.strip(':') for i in set(headings))


def main():
    labels = parse_headings()
    print(labels)




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
