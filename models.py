import database
from sqlalchemy import Column, Integer, TIMESTAMP, VARCHAR, DATETIME, BigInteger, Numeric, Date, Text


class Person(database.Base):
    __tablename__ = 'person'
    __table_args__ = {'schema': 'de'}

    person_id = Column(BigInteger, primary_key=True)
    gender_concept_id = Column(Integer)
    year_of_birth = Column(Integer)
    month_of_birth = Column(Integer)
    day_of_birth = Column(Integer)
    birth_datetime = Column(DATETIME)
    race_concept_id = Column(Integer)
    ethnicity_concept_id = Column(Integer)
    location_id = Column(BigInteger)
    provider_id = Column(BigInteger)
    care_site_id = Column(BigInteger)
    person_source_value = Column(VARCHAR(50))
    gender_source_value = Column(VARCHAR(50))
    gender_source_concept_id = Column(Integer)
    race_source_value = Column(VARCHAR(50))
    race_source_concept_id = Column(Integer)
    ethnicity_source_value = Column(VARCHAR(50))
    ethnicity_source_concept_id = Column(Integer)


class VisitOccurrence(database.Base):
    __tablename__ = 'visit_occurrence'
    __table_args__ = {'schema': 'de'}

    visit_occurrence_id = Column(BigInteger, primary_key=True)
    person_id = Column(BigInteger)
    visit_concept_id = Column(Integer)
    visit_start_datetime = Column(TIMESTAMP)
    visit_end_datetime = Column(TIMESTAMP)
    visit_start_date = Column(Date)
    visit_end_date = Column(Date)
    visit_type_concept_id = Column(Integer)
    provider_id = Column(BigInteger)
    care_site_id = Column(BigInteger)
    visit_source_value = Column(VARCHAR(50))
    visit_source_concept_id = Column(Integer)
    admitted_from_concept_id = Column(Integer)
    admitted_from_source_value = Column(VARCHAR(50))
    discharge_to_source_value = Column(VARCHAR(50))
    discharge_to_concept_id = Column(Integer)
    preceding_visit_occurrence_id = Column(BigInteger)


class ConditionOccurrence(database.Base):
    __tablename__ = 'condition_occurrence'
    __table_args__ = {'schema': 'de'}

    condition_occurrence_id = Column(BigInteger, primary_key=True)
    person_id = Column(BigInteger)
    condition_concept_id = Column(BigInteger)
    condition_start_datetime = Column(TIMESTAMP)
    condition_end_datetime = Column(TIMESTAMP)
    visit_occurrence_id = Column(BigInteger)
    condition_start_date = Column(Date)
    condition_end_date = Column(Date)
    stop_reason = Column(VARCHAR(20))
    provider_id = Column(BigInteger)
    visit_detail_id = Column(BigInteger)
    condition_source_value = Column(VARCHAR(50))
    condition_source_concept_id = Column(Integer)
    condition_status_status_source_value = Column(VARCHAR(50))
    condition_type_concept_id = Column(Integer)
    condition_status_concept_id = Column(Integer)


class DrugExposure(database.Base):
    __tablename__ = 'drug_exposure'
    __table_args__ = {'schema': 'de'}

    drug_exposure_id = Column(BigInteger, primary_key=True)
    person_id = Column(BigInteger)
    drug_concept_id = Column(Integer)
    drug_exposure_start_datetime = Column(TIMESTAMP)
    drug_exposure_start_date = Column(Date)
    drug_exposure_end_datetime = Column(TIMESTAMP)
    drug_exposure_end_date = Column(Date)
    verbatim_end_date = Column(Date)
    drug_type_concept_id = Column(Integer)
    stop_reason = Column(VARCHAR(20))
    refills = Column(Integer)
    quantity = Column(Numeric)
    days_supply = Column(Integer)
    sig = Column(Text)
    route_concept_id = Column(Integer)
    lot_number = Column(VARCHAR(50))
    provider_id = Column(BigInteger)
    visit_detail_id = Column(BigInteger)
    drug_source_value = Column(VARCHAR(50))
    drug_source_concept_id = Column(Integer)
    dose_unit_source_value = Column(VARCHAR(50))
    route_source_value = Column(VARCHAR(50))
    visit_occurrence_id = Column(BigInteger)


class Concept(database.Base):
    __tablename__ = 'concept'
    __table_args__ = {'schema': 'de'}

    concept_id = Column(Integer, primary_key=True)
    concept_name = Column(VARCHAR(255))
    domain_id = Column(VARCHAR(20))
    vocabulary_id = Column(VARCHAR(20))
    concept_class_id = Column(VARCHAR(20))
    concept_code = Column(VARCHAR(50))
    standard_concept = Column(VARCHAR(1))
    valid_start_date = Column(Date)
    valid_end_date = Column(Date)
    invalid_reason = Column(VARCHAR(1))



class Death(database.Base):
    __tablename__ = 'death'
    __table_args__ = {'schema': 'de'}

    person_id = Column(BigInteger, primary_key=True)
    death_date = Column(Date)
    death_datetime = Column(TIMESTAMP)
    death_type_concept_id = Column(Integer)
    cause_concept_id = Column(BigInteger)
    cause_source_value = Column(Integer)
    cause_source_concept_id = Column(BigInteger)
