# Category-Year BEDDN Files for Rasters
### Summary
Peter James reached out to the MESA Neighborhood & Aging team about acquiring Business Establishment Data Derived from NETS (BEDDN) in April 2024. Intended use is for creating year-category rasters for the contiguous US.

### Files Sent
1. Folders for every year from 1990-2022 (n=33) containing files for each category (n=255), where every record has a unique establishment ID (created at Drexel) and address ID (created at Drexel) in order to link to lat/longs for spatial processing. File name format is: CCC_YYYY.csv, where CCC = category, such as 'AAL', and YYYY = year. These files can be linked to BEDDN_addressid_latlong.txt by the address ID.
2. A file containing the unique address ID and its corresponding latitude/longitude in WGS84 geographic coordinates.

### Codebooks
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
| AddressID                   | unique id for each address in BEDDN can be used to link to spatial dataset |
| DisplayX                    | longitude (WGS84)                                                          |
| DisplayY                    | latitude (WGS84)                                                           |
