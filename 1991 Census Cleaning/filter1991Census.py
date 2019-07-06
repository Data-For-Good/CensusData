import pandas as pd
import numpy as np

csv_path = 'C:/Users/deepi/Desktop/DataForGood/SAS/1991 Census Cleaning/1991_CensusDataFSA.csv'

census_1991_Toronto = pd.read_csv(csv_path, encoding="cp1252")

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
census_1991_Toronto = census_1991_Toronto.melt(id_vars=['Profile of Forw'],
                                               var_name=['Geo Code'],
                                               value_name='Count')
census_1991_Toronto['Geo Code'] = census_1991_Toronto['Geo Code'].str.replace(r"\(.*\)", "")
census_1991_Toronto['Geo Code'] = census_1991_Toronto['Geo Code'].apply(lambda x: x.split(" ")[0])
census_1991_Toronto = census_1991_Toronto[census_1991_Toronto['Geo Code'].isin(required_areas)]

census_1991_Toronto.reset_index(drop=True, inplace=True)
for index, row in census_1991_Toronto.iterrows():
    print(index)
    if ((row['Profile of Forw'].startswith((space_charac*0, special_charac*0)))
            and not (row['Profile of Forw'].startswith((space_charac*1, special_charac*1)))
            and not (row['Profile of Forw'].startswith((space_charac * 2, special_charac * 2)))
            and not (row['Profile of Forw'].startswith((space_charac*3, special_charac*3)))
            and not row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
            and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))
            and not row['Profile of Forw'].startswith((space_charac*12, special_charac*12))
            and not row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
            and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
            and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_1991_Toronto.at[index, 'Category'] = row['Profile of Forw'].strip()
        if index > 0:
            try:
                if census_1991_Toronto.at[index, 'Profile of Forw'] == census_1991_Toronto.at[index-1, 'Category']:
                    census_1991_Toronto.at[index, 'Sub Category'] \
                        = census_1991_Toronto.at[index-1, 'Sub Category'].strip()
            except:
                print(index)
        # print(census_df.at[index, 'Category'])
    elif ((row['Profile of Forw'].startswith((space_charac*1, special_charac*1)))
            and not row['Profile of Forw'].startswith((space_charac*2, special_charac*2))
            and not row['Profile of Forw'].startswith((space_charac*3, special_charac*3))
            and not row['Profile of Forw'].startswith((space_charac*4, special_charac*4))
            and not row['Profile of Forw'].startswith((space_charac*5, special_charac*5))
            and not row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
            and not row['Profile of Forw'].startswith((space_charac*7, special_charac*7))
            and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))):
        census_1991_Toronto.at[index, 'Sub Category'] = row['Profile of Forw'].strip()
        census_1991_Toronto.at[index, 'Category'] = census_1991_Toronto.at[index-1, 'Category']
        # print(census_df.at[index, 'Sub Category'])
    elif ((row['Profile of Forw'].startswith((space_charac*2, special_charac*2))
          or row['Profile of Forw'].startswith((space_charac*3, special_charac*3)))
            and not row['Profile of Forw'].startswith((space_charac*4, special_charac*4))
            and not row['Profile of Forw'].startswith((space_charac*5, special_charac*5))
            and not row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
            and not row['Profile of Forw'].startswith((space_charac*7, special_charac*7))
            and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))):
        census_1991_Toronto.at[index, 'Sub Category'] = census_1991_Toronto.at[index - 1, 'Sub Category']
        census_1991_Toronto.at[index, 'Category'] = census_1991_Toronto.at[index - 1, 'Category']
        census_1991_Toronto.at[index, 'Characteristic_level_1'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_1'])
    elif ((row['Profile of Forw'].startswith((space_charac*4, special_charac*4))
          or row['Profile of Forw'].startswith((space_charac*5, special_charac*5)))
          and not row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
          and not row['Profile of Forw'].startswith((space_charac*7, special_charac*7))
          and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))):
        census_1991_Toronto.at[index, 'Sub Category'] = census_1991_Toronto.at[index - 1, 'Sub Category']
        census_1991_Toronto.at[index, 'Category'] = census_1991_Toronto.at[index - 1, 'Category']
        census_1991_Toronto.at[index, 'Characteristic_level_1'] = \
            census_1991_Toronto.at[index-1, 'Characteristic_level_1']
        census_1991_Toronto.at[index, 'Characteristic_level_2'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_2'])
    elif (row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
          and not row['Profile of Forw'].startswith((space_charac*7, special_charac*7))
          and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))):
        census_1991_Toronto.at[index, 'Sub Category'] = census_1991_Toronto.at[index - 1, 'Sub Category']
        census_1991_Toronto.at[index, 'Category'] = census_1991_Toronto.at[index - 1, 'Category']
        census_1991_Toronto.at[index, 'Characteristic_level_1'] = \
            census_1991_Toronto.at[index-1, 'Characteristic_level_1']
        census_1991_Toronto.at[index, 'Characteristic_level_2'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_2']
        census_1991_Toronto.at[index, 'Characteristic_level_3'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_3'])
    elif (row['Profile of Forw'].startswith((space_charac*7, special_charac*7))
          and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))):
        census_1991_Toronto.at[index, 'Sub Category'] = census_1991_Toronto.at[index - 1, 'Sub Category']
        census_1991_Toronto.at[index, 'Category'] = census_1991_Toronto.at[index - 1, 'Category']
        census_1991_Toronto.at[index, 'Characteristic_level_1'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_1']
        census_1991_Toronto.at[index, 'Characteristic_level_2'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_2']
        census_1991_Toronto.at[index, 'Characteristic_level_3'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_3']
        census_1991_Toronto.at[index, 'Characteristic_level_4'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_4'])
    else:
        census_1991_Toronto.at[index, 'Characteristic_level_5'] = row['Profile of Forw'].strip()
        census_1991_Toronto.at[index, 'Sub Category'] = census_1991_Toronto.at[index - 1, 'Sub Category']
        census_1991_Toronto.at[index, 'Category'] = census_1991_Toronto.at[index - 1, 'Category']
        census_1991_Toronto.at[index, 'Characteristic_level_1'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_1']
        census_1991_Toronto.at[index, 'Characteristic_level_2'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_2']
        census_1991_Toronto.at[index, 'Characteristic_level_3'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_3']
        census_1991_Toronto.at[index, 'Characteristic_level_4'] = \
            census_1991_Toronto.at[index - 1, 'Characteristic_level_4']
        # print(census_df.at[index, 'Characteristic_level_4'])

census_1991_Toronto['Category'] = census_1991_Toronto['Category'].replace('', np.nan).ffill()

# In case these 2 cols don't exist, add them
# We need these 2 columns in order to maintain consistency over all other census-year files
try:
    if census_1991_Toronto['Characteristic_level_4'].iloc[0] > 0:
        print('level_4 column exists')
except:
    census_1991_Toronto['Characteristic_level_4'] = np.nan

# Re-order column
census_1991_Toronto_final = census_1991_Toronto[['Geo Code', 'Category', 'Sub Category',
                                                 'Characteristic_level_1',
                                                 'Characteristic_level_2',
                                                 'Characteristic_level_3',
                                                 'Characteristic_level_4',
                                                 'Count']]
census_1991_Toronto_final.to_csv('C:/Users/deepi/Desktop/'
                                 'DataForGood/SAS/1991 Census Cleaning/1991_CensusDataFSA_filtered.csv')

final_df = pd.read_csv('C:/Users/deepi/Desktop/DataForGood/SAS/1991 Census Cleaning/1991_CensusDataFSA_filtered.csv')

# Divide categories into separate csv files
unique_categories = final_df['Category'].unique()

# Population Characteristics
temp = unique_categories[[0, 1, 2, 3, 4, 5, 6]]
pop_characteristics = temp.tolist()
pop_characteristics_final = final_df[final_df['Category'].isin(pop_characteristics)]
pop_characteristics_final.reset_index(drop=True)
pop_characteristics_final['Topic'] = 'Population Characteristics'
pop_characteristics_final = pop_characteristics_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                                       'Characteristic_level_1',
                                                       'Characteristic_level_2', 'Characteristic_level_3',
                                                       'Characteristic_level_4',
                                                       'Counts']]
pop_characteristics_final.to_csv('C:/Users/deepi/Desktop/DataForGood/'
                                 'SAS/1991 Census Cleaning/1991_CensusDataFSA_Population.csv')


# Age & Gender
temp = unique_categories[[7, 8, 9, 10]]
age_characteristics = temp.tolist()
age_characteristics_final = final_df[final_df['Category'].isin(age_characteristics)]
age_characteristics_final.reset_index(drop=True, inplace=True)
age_characteristics_final['Topic'] = 'Age Characteristics'
age_characteristics_final = age_characteristics_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                                       'Characteristic_level_1',
                                                       'Characteristic_level_2', 'Characteristic_level_3',
                                                       'Characteristic_level_4',
                                                       'Counts']]
age_characteristics_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                 '1991 Census Cleaning/1991_CensusDataFSA_Age.csv')

# Marital Status
temp = unique_categories[[15]]
marriage_status = temp.tolist()
marriage_status_final = final_df[final_df['Category'].isin(marriage_status)]
marriage_status_final.reset_index(drop=True, inplace=True)
marriage_status_final['Topic'] = 'Marriage Characteristics'
marriage_status_final = marriage_status_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
marriage_status_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                             '1991 Census Cleaning/1991_CensusDataFSA_MaritalStatus.csv')

# Household and dwelling characteristics
temp = unique_categories[[15]]
dwelling_household = temp.tolist()
dwelling_household_final = final_df[final_df['Category'].isin(dwelling_household)]
dwelling_household_final.reset_index(drop=True, inplace=True)
dwelling_household_final['Topic'] = 'Household and dwelling characteristics'
dwelling_household_final = dwelling_household_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
dwelling_household_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                '1991 Census Cleaning/1991_CensusDataFSA_DwellingHousehold.csv')


# Family Characteristics
temp = unique_categories[[11, 12, 13, 14, 16, 17, 18, 19, 20, 21]]
family_characteristic = temp.tolist()
family_characteristic_final = final_df[final_df['Category'].isin(family_characteristic)]
family_characteristic_final.reset_index(drop=True, inplace=True)
family_characteristic_final['Topic'] = 'Family characteristics'
family_characteristic_final = family_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
family_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                   '1991 Census Cleaning/1991_CensusDataFSA_FamilyStructure.csv')

# Household Type
temp = unique_categories[[22, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]]
household_characteristic = temp.tolist()
household_characteristic_final = final_df[final_df['Category'].isin(household_characteristic)]
household_characteristic_final.reset_index(drop=True, inplace=True)
household_characteristic_final['Topic'] = 'Household characteristics'
household_characteristic_final = household_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
household_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                   '1991 Census Cleaning/1991_CensusDataFSA_HouseholdStructure.csv')

# Detailed Language
temp = unique_categories[[23, 24, 25, 26, 27, 28, 29, 57]]
language_characteristic = temp.tolist()
language_characteristic_final = final_df[final_df['Category'].isin(language_characteristic)]
language_characteristic_final.reset_index(drop=True, inplace=True)
language_characteristic_final['Topic'] = 'Detailed Language characteristics'
language_characteristic_final = language_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
language_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                     '1991 Census Cleaning/1991_CensusDataFSA_DetailedLanguages.csv')

# Income Characteristics
temp = unique_categories[30:56]
income_characteristic = temp.tolist()
income_characteristic_final = final_df[final_df['Category'].isin(income_characteristic)]
income_characteristic_final.reset_index(drop=True, inplace=True)
income_characteristic_final['Topic'] = 'Income characteristics'
income_characteristic_final = income_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
income_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                     '1991 Census Cleaning/1991_CensusDataFSA_DetailedIncome.csv')

# Immigration Characteristics
temp = unique_categories[58:64]
immigration_characteristic = temp.tolist()
immigration_characteristic_final = final_df[final_df['Category'].isin(immigration_characteristic)]
immigration_characteristic_final.reset_index(drop=True, inplace=True)
immigration_characteristic_final['Topic'] = 'Immigration characteristics'
immigration_characteristic_final = immigration_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
immigration_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                     '1991 Census Cleaning/1991_CensusDataFSA_DetailedImmigration.csv')

# Visible Minority
temp = unique_categories[65:69]
visible_minority_characteristic = temp.tolist()
visible_minority_characteristic_final = final_df[final_df['Category'].isin(visible_minority_characteristic)]
visible_minority_characteristic_final.reset_index(drop=True, inplace=True)
visible_minority_characteristic_final['Topic'] = 'Visible Minority'
visible_minority_characteristic_final = visible_minority_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
visible_minority_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                     '1991 Census Cleaning/1991_CensusDataFSA_Visible_Minority.csv')

# Education
temp = unique_categories[84:89]
education_characteristic = temp.tolist()
education_characteristic_final = final_df[final_df['Category'].isin(education_characteristic)]
education_characteristic_final.reset_index(drop=True, inplace=True)
education_characteristic_final['Topic'] = 'Education'
education_characteristic_final = education_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
education_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                     '1991 Census Cleaning/1991_CensusDataFSA_Education.csv')

# Employment
temp = unique_categories[90:107]
employment_characteristic = temp.tolist()
employment_characteristic_final = final_df[final_df['Category'].isin(employment_characteristic)]
employment_characteristic_final.reset_index(drop=True, inplace=True)
employment_characteristic_final['Topic'] = 'Employment'
employment_characteristic_final = employment_characteristic_final[['Geo Code', 'Topic', 'Category', 'Sub Category',
                                               'Characteristic_level_1',
                                               'Characteristic_level_2', 'Characteristic_level_3',
                                               'Characteristic_level_4',
                                               'Counts']]
employment_characteristic_final.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/'
                                     '1991 Census Cleaning/1991_CensusDataFSA_Employment.csv')

