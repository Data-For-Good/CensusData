import pandas as pd
import numpy as np

csv_path = 'C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA.csv'
census_2011_Toronto = pd.read_csv(csv_path, encoding="cp1252")

required_areas = ['Canada', 'Ontario', 'M1B', 'M1C', 'M1G', 'M1H', 'M1J', 'M1K',
                  'M1L', 'M1M', 'M1N', 'M1P', 'M1R', 'M1S', 'M1T', 'M1V', 'M1W', 'M1X',
                  'M2H', 'M2J', 'M2K', 'M2L', 'M2M', 'M2N', 'M2P', 'M2R',
                  'M3A', 'M3B', 'M3C', 'M3H', 'M3J', 'M3K', 'M3L', 'M3M', 'M3N',
                  'M4A', 'M4B', 'M4C', 'M4E', 'M4G', 'M4H', 'M4J', 'M4K', 'M4L', 'M4M', 'M4N', 'M4P', 'M4R',
                  'M4S', 'M4T', 'M4V', 'M4W', 'M4X', 'M4Y',
                  'M5A', 'M5B', 'M5C', 'M5E', 'M5G', 'M5H', 'M5J', 'M5M', 'M5N', 'M5P', 'M5R',
                  'M5S', 'M5T', 'M5V', 'M5W', 'M6A', 'M6B', 'M6C', 'M6E', 'M6G', 'M6H', 'M6J',
                  'M6K', 'M6L', 'M6M', 'M6N', 'M6P', 'M6R', 'M6S', 'M8V', 'M8W', 'M8X', 'M8Y', 'M8Z',
                  'M9A', 'M9B', 'M9C', 'M9L', 'M9M', 'M9N', 'M9P', 'M9R', 'M9V', 'M9W']

space_count = 0
space_charac = ' '
special_charac = '\xa0'
census_2011_Toronto = census_2011_Toronto[census_2011_Toronto['Geo Code'].isin(required_areas)]

census_2011_Toronto.reset_index(drop=True, inplace=True)
for index, row in census_2011_Toronto.iterrows():
    if index == 11:
        print(index)
    if ((row['Characteristic'].startswith((space_charac*0, special_charac*0))
            or (row['Characteristic'].startswith((space_charac*1, special_charac*1))))
            and not (row['Characteristic'].startswith((space_charac*3, special_charac*3)))
            and not row['Characteristic'].startswith((space_charac*6, special_charac*6))
            and not row['Characteristic'].startswith((space_charac*8, special_charac*8))
            and not row['Characteristic'].startswith((space_charac*12, special_charac*12))
            and not row['Characteristic'].startswith((space_charac*14, special_charac*14))
            and not row['Characteristic'].startswith((space_charac*16, special_charac*16))
            and not row['Characteristic'].startswith((space_charac*18, special_charac*18))):
        census_2011_Toronto.at[index, 'Category'] = row['Characteristic'].strip()
        if index > 0:
            try:
                if census_2011_Toronto.at[index, 'Characteristic'] == census_2011_Toronto.at[index-1, 'Category']:
                    census_2011_Toronto.at[index, 'Sub Category'] \
                        = census_2011_Toronto.at[index-1, 'Sub Category'].strip()
            except:
                print(index)
        # print(census_df.at[index, 'Category'])
    elif ((row['Characteristic'].startswith((space_charac*2, special_charac*2))
            or row['Characteristic'].startswith((space_charac*3, special_charac*3))
            or row['Characteristic'].startswith((space_charac*4, special_charac*4)))
            and not row['Characteristic'].startswith((space_charac*6, special_charac*6))
            and not row['Characteristic'].startswith((space_charac*8, special_charac*8))
            and not row['Characteristic'].startswith((space_charac*12, special_charac*12))
            and not row['Characteristic'].startswith((space_charac*14, special_charac*14))
            and not row['Characteristic'].startswith((space_charac*16, special_charac*16))
            and not row['Characteristic'].startswith((space_charac*18, special_charac*18))):
        census_2011_Toronto.at[index, 'Sub Category'] = row['Characteristic'].strip()
        census_2011_Toronto.at[index, 'Category'] = census_2011_Toronto.at[index-1, 'Category']
        # print(census_df.at[index, 'Sub Category'])
    elif (row['Characteristic'].startswith((space_charac*6, special_charac*6))
            and not row['Characteristic'].startswith((space_charac*8, special_charac*8))
            and not row['Characteristic'].startswith((space_charac*12, special_charac*12))
            and not row['Characteristic'].startswith((space_charac*14, special_charac*14))
            and not row['Characteristic'].startswith((space_charac*16, special_charac*16))
            and not row['Characteristic'].startswith((space_charac*18, special_charac*18))):
        census_2011_Toronto.at[index, 'Sub Category'] = census_2011_Toronto.at[index - 1, 'Sub Category']
        census_2011_Toronto.at[index, 'Category'] = census_2011_Toronto.at[index - 1, 'Category']
        census_2011_Toronto.at[index, 'Characteristic_level_1'] = row['Characteristic'].strip()
        # print(census_df.at[index, 'Characteristic_level_1'])
    elif (row['Characteristic'].startswith((space_charac*8, special_charac*8))
          and not row['Characteristic'].startswith((space_charac*12, special_charac*12))
          and not row['Characteristic'].startswith((space_charac*14, special_charac*14))
          and not row['Characteristic'].startswith((space_charac*16, special_charac*16))
          and not row['Characteristic'].startswith((space_charac*18, special_charac*18))):
        census_2011_Toronto.at[index, 'Sub Category'] = census_2011_Toronto.at[index - 1, 'Sub Category']
        census_2011_Toronto.at[index, 'Category'] = census_2011_Toronto.at[index - 1, 'Category']
        census_2011_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2011_Toronto.at[index-1, 'Characteristic_level_1']
        census_2011_Toronto.at[index, 'Characteristic_level_2'] = row['Characteristic'].strip()
        # print(census_df.at[index, 'Characteristic_level_2'])
    elif (row['Characteristic'].startswith((space_charac*12, special_charac*12))
          and not row['Characteristic'].startswith((space_charac*14, special_charac*14))
          and not row['Characteristic'].startswith((space_charac*16, special_charac*16))
          and not row['Characteristic'].startswith((space_charac*18, special_charac*18))):
        census_2011_Toronto.at[index, 'Sub Category'] = census_2011_Toronto.at[index - 1, 'Sub Category']
        census_2011_Toronto.at[index, 'Category'] = census_2011_Toronto.at[index - 1, 'Category']
        census_2011_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2011_Toronto.at[index-1, 'Characteristic_level_1']
        census_2011_Toronto.at[index, 'Characteristic_level_2'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_2']
        census_2011_Toronto.at[index, 'Characteristic_level_3'] = row['Characteristic'].strip()
        # print(census_df.at[index, 'Characteristic_level_3'])
    elif (row['Characteristic'].startswith((space_charac*14, special_charac*14))
          and not row['Characteristic'].startswith((space_charac*16, special_charac*16))
          and not row['Characteristic'].startswith((space_charac*18, special_charac*18))):
        census_2011_Toronto.at[index, 'Sub Category'] = census_2011_Toronto.at[index - 1, 'Sub Category']
        census_2011_Toronto.at[index, 'Category'] = census_2011_Toronto.at[index - 1, 'Category']
        census_2011_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_1']
        census_2011_Toronto.at[index, 'Characteristic_level_2'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_2']
        census_2011_Toronto.at[index, 'Characteristic_level_3'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_3']
        census_2011_Toronto.at[index, 'Characteristic_level_4'] = row['Characteristic'].strip()
        # print(census_df.at[index, 'Characteristic_level_4'])
    else:
        census_2011_Toronto.at[index, 'Characteristic_level_5'] = row['Characteristic'].strip()
        census_2011_Toronto.at[index, 'Sub Category'] = census_2011_Toronto.at[index - 1, 'Sub Category']
        census_2011_Toronto.at[index, 'Category'] = census_2011_Toronto.at[index - 1, 'Category']
        census_2011_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_1']
        census_2011_Toronto.at[index, 'Characteristic_level_2'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_2']
        census_2011_Toronto.at[index, 'Characteristic_level_3'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_3']
        census_2011_Toronto.at[index, 'Characteristic_level_4'] = \
            census_2011_Toronto.at[index - 1, 'Characteristic_level_4']
        # print(census_df.at[index, 'Characteristic_level_5'])

census_2011_Toronto['Category'] = census_2011_Toronto['Category'].replace('', np.nan).ffill()
census_2011_Toronto = census_2011_Toronto[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                           'Characteristic_level_1',
                                           'Characteristic_level_2', 'Characteristic_level_3',
                                           'Characteristic_level_4',
                                           'Total']]
# census_2011_Toronto.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_filtered.csv')

# Age & Gender
# age_characteristics = census_2011_Toronto[census_2011_Toronto['Topic'] == 'Age characteristics']
# age_characteristics.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_Age.csv')

# Marital Status
# marriage_status = census_2011_Toronto[census_2011_Toronto['Topic'] == 'Marital status']
# marriage_status.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_MaritalStatus.csv')

# Family Characteristics
# family_characteristics = census_2011_Toronto[census_2011_Toronto['Topic'] == 'Family characteristics']
# family_characteristics.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_FamilyStructure.csv')

# Dwelling & Household
# dwelling_household = census_2011_Toronto[census_2011_Toronto['Topic'] == 'Household and dwelling characteristics']
# dwelling_household.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_DwellingHousehold.csv')

# Detailed Language
detailed_language = census_2011_Toronto[(census_2011_Toronto['Topic'] == 'Detailed mother tongue')
                                        | (census_2011_Toronto['Topic'] == 'Knowledge of official languages')
                                        | (census_2011_Toronto['Topic'] == 'First official language spoken')
                                        | (census_2011_Toronto['Topic'] ==
                                           'Detailed language spoken most often at home')
                                        | (census_2011_Toronto['Topic'] ==
                                           'Detailed other language spoken regularly at home')]
detailed_language.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_DetailedLanguages.csv')

# Population Characteristics
# population = census_2011_Toronto[census_2011_Toronto['Topic'] == 'Population and dwelling counts']
# population.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2011_CensusDataFSA_Population.csv')

