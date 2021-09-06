from cohortextractor import (codelist, codelist_from_csv, combine_codelists)

antipsychotics_sec_gen = codelist_from_csv(
    "codelists/opensafely-second-generation-antipsychotics-excluding-long-acting-injections.csv",
    system="snomed",
    column="dmd_id",
    )