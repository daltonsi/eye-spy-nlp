import pandas as pd 


SOURCE_PATH = 'source_data/mtsamples.csv'




def main():
"""preprocess source data to Opthamal speciality"""
	df = pd.read_csv(SOURCE_PATH)
	df_stripped = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
	opthamal_mask = df_stripped['medical_specialty'] == 'Ophthalmology'
	opthamal_df = df[opthamal_mask]
	opthamal_df.to_csv('source_data/mtsamples_opthamal.csv')


if __name__ == '__main__':
	main()