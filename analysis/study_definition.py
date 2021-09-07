from cohortextractor import (StudyDefinition, patients, codelist, codelist_from_csv, Measure)  # NOQA

from codelists import *


study = StudyDefinition(

    default_expectations={
      "date": {"earliest": "1900-01-01", "latest": "today"},
      "rate": "uniform",
      "incidence": 0.5,
    },

    index_date="2020-01-01",
    # population=patients.satisfying(
      #age>="60"
      #),

    population=patients.all(),
    
    age=patients.age_as_of(
      "index_date",
      return_expectations={
        "rate": "universal",
        "int": {"distribution": "population_ages"}
      }
      ),

    
      
    antipsychotics_prescribing = patients.with_these_medications(
      antipsychotics_sec_gen,
      returning = "binary_flag",
      find_first_match_in_period = True,
      between = ["index_date", "index_date - 3 months"],
      return_expectations = {"incidence": 0.2}
      ),
)

measures = [

  Measure(

    id="antipsychotic_rx_rate",

    numerator="antipsychotics_prescribing",

    denominator="population",

  ),

]
