import pandas as pd 
import numpy as np

SOURCE_PATH = 'source_data/mtsamples.csv'




def main():
	"""preprocess source data to Opthamal speciality"""
	df = pd.read_csv(SOURCE_PATH, index_col=0)
	df_stripped = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
	opthamal_mask = df_stripped['medical_specialty'] == 'Ophthalmology'
	opthamal_df = df[opthamal_mask]

	conditions = [
		(opthamal_df['sample_name'].str.contains('Cataract')==True)
	]

	values = ['cataract']


	opthamal_df['label'] = np.select(conditions,values)



	opthamal_df.to_csv('source_data/mtsamples_opthamal.csv')


if __name__ == '__main__':
	main()