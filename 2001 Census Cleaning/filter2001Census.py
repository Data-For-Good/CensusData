import pandas as pd
import numpy as np

csv_path = 'C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/2001_CensusDataFSA.csv'

census_2001_Toronto = pd.read_csv(csv_path, encoding="cp1252")

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
census_2001_Toronto = census_2001_Toronto.melt(id_vars=['Profile of Forw'],
                                               var_name=['Geo Code'],
                                               value_name='Count')
census_2001_Toronto['Geo Code'] = census_2001_Toronto['Geo Code'].str.replace(r"\(.*\)", "")
census_2001_Toronto['Geo Code'] = census_2001_Toronto['Geo Code'].apply(lambda x: x.split(" ")[0])
census_2001_Toronto = census_2001_Toronto[census_2001_Toronto['Geo Code'].isin(required_areas)]

census_2001_Toronto.reset_index(drop=True, inplace=True)
for index, row in census_2001_Toronto.iterrows():
    # if index == 2:
    #     print(index)
    if ((row['Profile of Forw'].startswith((space_charac*0, special_charac*0))
            or (row['Profile of Forw'].startswith((space_charac*1, special_charac*1))))
            and not (row['Profile of Forw'].startswith((space_charac * 2, special_charac * 2)))
            and not (row['Profile of Forw'].startswith((space_charac*3, special_charac*3)))
            and not row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
            and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))
            and not row['Profile of Forw'].startswith((space_charac*12, special_charac*12))
            and not row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
            and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
            and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_2001_Toronto.at[index, 'Category'] = row['Profile of Forw'].strip()
        if index > 0:
            try:
                if census_2001_Toronto.at[index, 'Profile of Forw'] == census_2001_Toronto.at[index-1, 'Category']:
                    census_2001_Toronto.at[index, 'Sub Category'] \
                        = census_2001_Toronto.at[index-1, 'Sub Category'].strip()
            except:
                print(index)
        # print(census_df.at[index, 'Category'])
    elif ((row['Profile of Forw'].startswith((space_charac*2, special_charac*2))
            or row['Profile of Forw'].startswith((space_charac*3, special_charac*3)))
            and not row['Profile of Forw'].startswith((space_charac*4, special_charac*4))
            and not row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
            and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))
            and not row['Profile of Forw'].startswith((space_charac*12, special_charac*12))
            and not row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
            and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
            and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_2001_Toronto.at[index, 'Sub Category'] = row['Profile of Forw'].strip()
        census_2001_Toronto.at[index, 'Category'] = census_2001_Toronto.at[index-1, 'Category']
        # print(census_df.at[index, 'Sub Category'])
    elif (row['Profile of Forw'].startswith((space_charac*4, special_charac*4))
            and not row['Profile of Forw'].startswith((space_charac * 6, special_charac * 6))
            and not row['Profile of Forw'].startswith((space_charac*8, special_charac*8))
            and not row['Profile of Forw'].startswith((space_charac*12, special_charac*12))
            and not row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
            and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
            and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_2001_Toronto.at[index, 'Sub Category'] = census_2001_Toronto.at[index - 1, 'Sub Category']
        census_2001_Toronto.at[index, 'Category'] = census_2001_Toronto.at[index - 1, 'Category']
        census_2001_Toronto.at[index, 'Characteristic_level_1'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_1'])
    elif (row['Profile of Forw'].startswith((space_charac*6, special_charac*6))
          and not row['Profile of Forw'].startswith((space_charac * 8, special_charac * 8))
          and not row['Profile of Forw'].startswith((space_charac*12, special_charac*12))
          and not row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
          and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
          and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_2001_Toronto.at[index, 'Sub Category'] = census_2001_Toronto.at[index - 1, 'Sub Category']
        census_2001_Toronto.at[index, 'Category'] = census_2001_Toronto.at[index - 1, 'Category']
        census_2001_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2001_Toronto.at[index-1, 'Characteristic_level_1']
        census_2001_Toronto.at[index, 'Characteristic_level_2'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_2'])
    elif (row['Profile of Forw'].startswith((space_charac*8, special_charac*8))
          and not row['Profile of Forw'].startswith((space_charac * 12, special_charac * 12))
          and not row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
          and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
          and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_2001_Toronto.at[index, 'Sub Category'] = census_2001_Toronto.at[index - 1, 'Sub Category']
        census_2001_Toronto.at[index, 'Category'] = census_2001_Toronto.at[index - 1, 'Category']
        census_2001_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2001_Toronto.at[index-1, 'Characteristic_level_1']
        census_2001_Toronto.at[index, 'Characteristic_level_2'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_2']
        census_2001_Toronto.at[index, 'Characteristic_level_3'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_3'])
    elif (row['Profile of Forw'].startswith((space_charac*14, special_charac*14))
          and not row['Profile of Forw'].startswith((space_charac*16, special_charac*16))
          and not row['Profile of Forw'].startswith((space_charac*18, special_charac*18))):
        census_2001_Toronto.at[index, 'Sub Category'] = census_2001_Toronto.at[index - 1, 'Sub Category']
        census_2001_Toronto.at[index, 'Category'] = census_2001_Toronto.at[index - 1, 'Category']
        census_2001_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_1']
        census_2001_Toronto.at[index, 'Characteristic_level_2'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_2']
        census_2001_Toronto.at[index, 'Characteristic_level_3'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_3']
        census_2001_Toronto.at[index, 'Characteristic_level_4'] = row['Profile of Forw'].strip()
        # print(census_df.at[index, 'Characteristic_level_4'])
    else:
        census_2001_Toronto.at[index, 'Characteristic_level_5'] = row['Profile of Forw'].strip()
        census_2001_Toronto.at[index, 'Sub Category'] = census_2001_Toronto.at[index - 1, 'Sub Category']
        census_2001_Toronto.at[index, 'Category'] = census_2001_Toronto.at[index - 1, 'Category']
        census_2001_Toronto.at[index, 'Characteristic_level_1'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_1']
        census_2001_Toronto.at[index, 'Characteristic_level_2'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_2']
        census_2001_Toronto.at[index, 'Characteristic_level_3'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_3']
        census_2001_Toronto.at[index, 'Characteristic_level_4'] = \
            census_2001_Toronto.at[index - 1, 'Characteristic_level_4']
        # print(census_df.at[index, 'Characteristic_level_5'])

census_2001_Toronto['Category'] = census_2001_Toronto['Category'].replace('', np.nan).ffill()

# In case these 2 cols don't exist, add them
# We need these 2 columns in order to maintain consistency over all other census-year files
try:
    if census_2001_Toronto['Characteristic_level_4'].iloc[0] > 0:
        print('level_4 column exists')
except:
    census_2001_Toronto['Characteristic_level_4'] = np.nan
try:
    if census_2001_Toronto['Characteristic_level_5'].iloc[0] >0:
        print('level_5 column exists')
except:
    census_2001_Toronto['Characteristic_level_5'] = np.nan

# Re-order column
census_2001_Toronto_final = census_2001_Toronto[['Geo Code', 'Category', 'Sub Category',
                                                 'Characteristic_level_1',
                                                 'Characteristic_level_2',
                                                 'Characteristic_level_3',
                                                 'Characteristic_level_4',
                                                 'Characteristic_level_5',
                                                 'Count']]
census_2001_Toronto_final.to_csv('C:/Users/deepi/Desktop/'
                                 'DataForGood/SAS/2001 Census Cleaning/2001_CensusDataFSA_filtered.csv')

# Temporary file read
census_2001_Toronto = pd.read_csv('C:/Users/deepi/Desktop/'
                                  'DataForGood/SAS/2001 Census Cleaning/2001_CensusDataFSA_filtered.csv')

# Divide categories into separate csv files
unique_categories = census_2001_Toronto['Category'].unique()

# Age & Gender
age_characteristics = census_2001_Toronto[(census_2001_Toronto['Category'] == 'Population, 2001 - 100% Data')
                                          | (census_2001_Toronto['Category'] ==
                                             'Total population by sex and age groups - 100% Data')
                                          | (census_2001_Toronto['Category'] == 'Total population by '
                                                                                'sex and age groups - 100% Data')
                                          ]
age_characteristics.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/2001_CensusDataFSA_Age.csv')

# Marital Status
marriage_status = census_2001_Toronto[(census_2001_Toronto['Category']
                                      == 'Total population 15 years and over by legal marital status - 100% Data')
                                      | (census_2001_Toronto['Category']
                                      == 'Total population 15 years and over by common-law status - 100% Data')]
marriage_status.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                       '2001_CensusDataFSA_MaritalStatus.csv')

# Family Characteristics
family_characteristics = census_2001_Toronto[(census_2001_Toronto['Category'] ==
                                             'Total number of census families in private households - 20% Sample Data')
                                        | (census_2001_Toronto['Category'] ==
                                           'Average number of persons per census family')]
family_characteristics.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                              '2001_CensusDataFSA_FamilyStructure.csv')

# Dwelling & Household
dwelling_household = census_2001_Toronto[(census_2001_Toronto['Category'] == 'Household and dwelling characteristics')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of children at home - 20% Sample Data')
                                         | (census_2001_Toronto['Category'] ==
                                            'Average number of children at home per census family')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of persons in private households - 20% Sample Data')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of persons 65 years and over - 20% Sample Data')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of occupied private dwellings - 20% Sample Data')
                                         | (census_2001_Toronto['Category'] == 'Average number of rooms per dwelling')
                                         | (census_2001_Toronto['Category'] == 'Average number of bedrooms per dwelling')
                                         | (census_2001_Toronto['Category'] == 'Owned')
                                         | (census_2001_Toronto['Category'] == 'Rented')
                                         | (census_2001_Toronto['Category'] == 'Band Housing')
                                         | (census_2001_Toronto['Category'] == 'Regular maintenance only')
                                         | (census_2001_Toronto['Category'] == 'Minor Repairs')
                                         | (census_2001_Toronto['Category'] == 'Major Repairs')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, before 1946')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, 1946-1960')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, 1961-1970')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, 1971-1980')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, 1981-1990')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, 1991-1995')
                                         | (census_2001_Toronto['Category'] == 'Period of construction, 1996-2001')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of occupied private dwellings by structural '
                                            'type of dwelling - 100% Data')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of private households by household size - 100% Data')
                                         | (census_2001_Toronto['Category'] ==
                                            'Number of persons in private households')
                                         | (census_2001_Toronto['Category'] ==
                                            'Average number of persons in private households')
                                         | (census_2001_Toronto['Category'] ==
                                            'Total number of private households by household type - 20% Sample Data')
                                         | (census_2001_Toronto['Category'] == '')]
dwelling_household.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                          '2001_CensusDataFSA_DwellingHousehold.csv')

# Detailed Language
detailed_language = census_2001_Toronto[census_2001_Toronto['Category'].isin(unique_categories[46:230])]
detailed_language.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                         '2001_CensusDataFSA_DetailedLanguages.csv')

# Immigration / Citizenship Characteristics
citizenship_immigration = census_2001_Toronto[(census_2001_Toronto['Category'] ==
                                               'Total population by citizenship - 20% Sample Data')
                                              | (census_2001_Toronto['Category'] ==
                                                 'Total population by immigrant status '
                                                 'and place of birth - 20% Sample Data')
                                              | (census_2001_Toronto['Category'] ==
                                                 'Total recent immigrants by selected '
                                                 'places of birth - 20% Sample Data')
                                              | (census_2001_Toronto['Category'] ==
                                                 'Total immigrant population by period '
                                                 'of immigration - 20% Sample Data')
                                              | (census_2001_Toronto['Category'] ==
                                                 'Total immigrant population by age at immigration - 20% Sample Data')
                                              | (census_2001_Toronto['Category'] ==
                                                 'Total population 15 years and over by generation status '
                                                 '- 20% Sample Data')
                                              | (census_2001_Toronto['Category'] == 'Total '
                                                                                    'population by ethnic origin '
                                                                                    '(single and multiple responses) '
                                                                                    '- 20% Sample Data')]

citizenship_immigration.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                               '2001_CensusDataFSA_Citizenship_Immigration.csv')
# Mobility Status
mobility_status = census_2001_Toronto[(census_2001_Toronto['Category'] ==
                                       'Total population 5 years and over by '
                                       'mobility status 5 years ago - 20% Sample Data')
                                      | (census_2001_Toronto['Category'] ==
                                         'Total population 1 year and over '
                                         'by mobility status 1 year ago - 20% Sample Data')]
mobility_status.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                       '2001_CensusDataFSA_Mobility_Status.csv')

# Income Status
income_status = census_2001_Toronto[census_2001_Toronto['Category'].isin(unique_categories[280:312])]
income_status.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                     '2001_CensusDataFSA_IncomeStatus.csv')

# Visibile Minorities
visible_minorities = census_2001_Toronto[(census_2001_Toronto['Category'] ==
                                          'Total population by visible minority groups - 20% Sample Data')
                                          | (census_2001_Toronto['Category'] ==
                                             'Total population by Aboriginal and non-Aboriginal population - '
                                             '20% Sample Data')
                                          | (census_2001_Toronto['Category'] ==
                                             'Total population 15 years and over by labour force activity - '
                                             '20% Sample Data')]
visible_minorities.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                          '2001_CensusDataFSA_Visible_Minoritites.csv')

# Employment Status
employment_status = census_2001_Toronto[census_2001_Toronto['Category'].isin(unique_categories[237:275])]
employment_status.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                         '2001_CensusDataFSA_Employment_Status.csv')

# Education Status
education_status = census_2001_Toronto[census_2001_Toronto['Category'].isin(unique_categories[276:279])]
education_status.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                        '2001_CensusDataFSA_Education_Status.csv')

# Industry Divisions
industry_divisions = census_2001_Toronto[(census_2001_Toronto['Category'] == 'Total labour force 15 years and over '\
                                                                            'by occupation - 2001 National '
                                                                             'Occupational ' \
                                                                            'Classification for Statistics - ' \
                                                                            '20% Sample Data')
                                        | (census_2001_Toronto['Category'] == 'Male labour force 15 years and over '
                                                                              '- Occupation - 2001 National Occupational'
                                                                              ' Classification for Statistics')
                                        | (census_2001_Toronto['Category'] == 'Female labour force 15 years and over '
                                                                              '- Occupation - 2001 National Occupational'
                                                                              ' Classification for Statistics')
                                        | (census_2001_Toronto['Category'] == 'Female labour force 15 years and over '
                                                                                '- Occupation - 2001 National '
                                                                                'Occupational Classification for '
                                                                                'Statistics')]
industry_divisions.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                          '2001_CensusDataFSA_Industry_Divisions.csv')

# Religion Division
religion_divisions = census_2001_Toronto[(census_2001_Toronto['Category'] == 'Total population by selected religions '
                                                                             '- 20% Sample Data')]
religion_divisions.to_csv('C:/Users/deepi/Desktop/DataForGood/SAS/2001 Census Cleaning/'
                          '2001_CensusDataFSA_Religion_Division.csv')

