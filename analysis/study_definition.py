from cohortextractor import (StudyDefinition, patients, codelist, codelist_from_csv, Measure)  # NOQA

from codelists import *


study = StudyDefinition(

    default_expectations={
      "date": {"earliest": "1900-01-01", "latest": "today"},
      "rate": "uniform",
      "incidence": 0.5,
    },

    index_date="2019-01-01",
    
    population=patients.satisfying(
      """
        age>=60
        AND
        NOT has_died
        AND
        registered
        """
      ),

    # population=patients.all(),
    
    age=patients.age_as_of(
      "index_date",
      return_expectations={
        "rate": "universal",
        "int": {"distribution": "population_ages"}
      }
      ),

    has_died=patients.died_from_any_cause(
      on_or_before = "index_date",
      returning = "binary_flag",
    ),
    
    registered = patients.satisfying(
      "registered_at_start",
      registered_at_start = patients.registered_as_of("index_date"),
    ),

    antipsychotics_prescribing = patients.with_these_medications(
      antipsychotics_sec_gen,
      returning = "binary_flag",
      find_first_match_in_period = True,
      between = ["index_date - 3 months", "index_date"],
      return_expectations = {"incidence": 0.2}
      ),
)

measures = [

  Measure(

    id="antipsychotic_rx_rate",

    numerator="antipsychotics_prescribing",

    denominator="population",
    group_by="population"

  ),

]
