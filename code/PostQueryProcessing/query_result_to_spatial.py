#%% TAKE TRACT-LEVEL BEDDN DATA QUERIED FROM DB AND CREATED SPATIAL FILE WITH COLUMN FOR EACH CATEGORY-YEAR
# read in results file
beddn_results = pd.read_csv(r'path to db query results\file.csv', dtype={'Tract10':str})

# define new folder to house output by-year csv files
output_csv_path = r'new folder to output csvs by year'
# extract unique years from file and sort
years = beddn_results['Year'].unique()
years.sort()
# create new folder, if not exists
Path(output_csv_path).mkdir(parents=True, exist_ok=True)
# define schema ini file and path
schemafile = os.path.join(output_csv_path, 'schema.ini')
# define gdb to output by-year gdb tables
gdbtable_outpath = r'path to gdb to output tables.gdb'
# get list of category columns
cols = [col for col in beddn_results.columns if beddn_results.columns.startswith('t10_net')]

# loop through years, creat individual csv and gdb table files
for year in years:
    tempdf = beddn_results.loc[beddn_results['Year']==year]
    # create column rename schema and rename columns to include year
    rename_schema = {col:f'{col}{year}' for col in cols}
    tempdf = tempdf.rename(columns=rename_schema)
    # output csv
    out_filename = f't10_beddn_cnd_{year}.csv'
    out_filepath = os.path.join(output_csv_path, out_filename)
    tempdf.to_csv(out_filepath, index=False)
    # create/add to schema ini for csv
    schema = [f'[{filename}]\n', 'ColNameHeader=True\n', 'Format=CSVDelimited\n', 'Col1="Tract10" Text Width 11\n\n']
    with open(schemafile, "a") as file:
        file.writelines(schema)
    out_name_gdb = f't10_beddn_cnd_{year}'
    arcpy.conversion.TableToTable(out_filepath, gdbtable_outpath, out_name_gdb)

#%% LOAD TRACT SPATIAL FILE
# copy tract spatial file and drop columns
tract_spatial = r'Z:\UHC_Data\Census2010\Geodatabases\Census2010_US20230929.gdb\AlbersContUS_USGS\CT_2010_ContUSlandRepairAlbers'
tracts_out_name = 'name_output_fc'
tracts_out_fullpath = os.path.join(gdbtable_outpath, tracts_out_name)
arcpy.management.CopyFeatures(tract_spatial, tracts_out_fullpath)
arcpy.management.DeleteField(tracts_out_fullpath, ['GEOID10'], 'KEEP_FIELDS')

# JOIN FILES TO SPATIAL FILE 
# walk through files and join to tract boundary files
arcpy.env.workspace = gdbtable_outpath
files = arcpy.ListTables()

for file in files:
    print(f'joining {file}')
    # get year as string
    year = re.findall(r"(?<=cnd_)\d{4}", file)[0]
    # join file to spatial file (category cols only)
    join_field = 'Tract10'
    in_field = 'GEOID10'
    fields = arcpy.ListFields(file)
    fields = [field.name for field in fields if field.name.startswith('t10_net')]
    arcpy.management.JoinField(in_data=tracts_out)fullpath, in_field=in_field, join_table=file, join_field=join_field, fields=fields)
