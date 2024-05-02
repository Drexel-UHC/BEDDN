# Request: James_P 05/02/2024
**Via**: email on 04/17/2024 \
**Email subject**: RE: NETS Data \
**Output Dataset Name**: BEDDN_addressid_latlong.zip\
**Output Dataset Location**: Sharepoint: Sent by S. Melly via liquid files 05/02/2024 \
Additional files sent via email 05/02/2024: 
1. BEDDN_Catalogue.xlsx
2. BEDDN_InfoSheet.pdf
3. UHCMatchCodeRank20230822.xlsx


### Summary
Peter James reached out to the MESA Neighborhood & Aging team about acquiring Business Establishment Data Derived from NETS (BEDDN) in April 2024. Intended use is for creating year-category rasters for the contiguous US.

### Files Sent
1. Folders for every year from 1990-2022 (n=33) containing files for each category (n=255), where every record has a unique establishment ID (created at Drexel) and address ID (created at Drexel) in order to link to lat/longs for spatial processing. File name format is: CCC_YYYY.csv, where CCC = category, such as 'AAL', and YYYY = year. These files can be linked to BEDDN_addressid_latlong.txt by the address ID.
2. A file containing the unique address ID and its corresponding latitude/longitude in WGS84 geographic coordinates. The file also contains a geocoding accuracy measure, UHCMatchCodeRank, which was developed by the UHC using ESRI and other geocoding service accuracy measures as references. The UHC reccommends using lat/longs with UHCMatchCodeRank <= 6 (street intersection) for most situations.

### Codebook
#### CCC_YYYY.csv
File format: comma delimited
| Variable     | Description                                                |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DunsYearId   | Unique id for each establishment-year made up at Drexel to de-identify raw NETS data                                                                                                                                |
| AddressID    | Unique id for each address in BEDDN that can be used to link to spatial dataset (made up at Drexel to de-identify raw NETS data)                                                                                                                              |
| Year         |                                                                                                                                                                                                             |
| Category     | Category assigned to establishment-year. This variable name will read 'BaseGroup' or 'HighLevel' depending on whether the file contains establishments that are categorized as Base Groups or Combination Categories/Thematic Constructs.            |

#### BEDDN_addressid_latlong.txt
File format: tab delimited
| Variable                    | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| AddressID                   | Unique id for each address that can be used to link to spatial dataset |
| DisplayX                    | Longitude (WGS84)                                                          |
| DisplayY                    | Latitude (WGS84)                                                           |
| UHCMatchCodeRank            | Geocoding accuracy indicator (see UHCMatchCodeRank20230822.xlsx for details)                                       |
