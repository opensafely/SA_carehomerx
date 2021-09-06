from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA

from codelists import *

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    index_date="2020-01-01",
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),

antipsychotics_prescribing = patients.with_these_medications(
    antipsychotics_sec_gen,
    returning = "binary_flag",
    find_first_match_in_period = True,
    between = ["index_date", "index_date - 3 months"],
    return_expectations = {"incidence": 0.2}
),

)

