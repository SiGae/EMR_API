from models import Person, Concept, VisitOccurrence, ConditionOccurrence, Death, DrugExposure
from library import l_convert, l_translate
from sqlalchemy.orm import aliased


def get_person(param, db):
    person_gender = aliased(Concept)
    person_race = aliased(Concept)
    person_ethnicity = aliased(Concept)
    response_data = db.query(Person.person_id,
                             Person.gender_concept_id,
                             person_gender.concept_name.label('성별'),
                             Person.ethnicity_concept_id,
                             person_ethnicity.concept_name.label('민족'),
                             Person.race_concept_id,
                             person_race.concept_name.label('인종'),
                             Person.gender_source_value,
                             Person.birth_datetime,
                             Person.day_of_birth,
                             Person.month_of_birth,
                             Person.year_of_birth,
                             Person.care_site_id,
                             Person.ethnicity_source_concept_id,
                             Person.race_source_value,
                             Person.provider_id,
                             Person.location_id,
                             Person.person_source_value,
                             Person.gender_source_concept_id,
                             Person.race_source_concept_id,
                             Person.ethnicity_source_value
                             ) \
        .join(person_gender, person_gender.concept_id == Person.gender_concept_id, isouter=True) \
        .join(person_race, person_race.concept_id == Person.race_concept_id, isouter=True) \
        .join(person_ethnicity, person_ethnicity.concept_id == Person.ethnicity_concept_id, isouter=True)

    response_data = __filter_page__(response_data, param).all()
    response_data = l_convert.convert_dict(response_data)

    return {'검색 결과': response_data}


def get_visit_occurrence(param, db):
    visit_type = aliased(Concept)
    visit_discharge = aliased(Concept)

    response_data = db.query(VisitOccurrence.visit_occurrence_id,
                             VisitOccurrence.person_id,
                             VisitOccurrence.visit_concept_id,
                             VisitOccurrence.visit_start_date,
                             VisitOccurrence.visit_start_datetime,
                             VisitOccurrence.visit_end_date,
                             VisitOccurrence.visit_start_datetime,
                             VisitOccurrence.visit_type_concept_id,
                             VisitOccurrence.provider_id,
                             VisitOccurrence.care_site_id,
                             VisitOccurrence.visit_source_value,
                             VisitOccurrence.visit_source_concept_id,
                             VisitOccurrence.admitted_from_concept_id,
                             VisitOccurrence.admitted_from_source_value,
                             VisitOccurrence.discharge_to_source_value,
                             VisitOccurrence.discharge_to_concept_id,
                             VisitOccurrence.preceding_visit_occurrence_id,
                             visit_type.concept_name.label('방문 유형'),
                             visit_discharge.concept_name.label('visit_discharge_name'),

                             ) \
        .join(visit_type, visit_type.concept_id == VisitOccurrence.visit_concept_id, isouter=True) \
        .join(visit_discharge, visit_type.concept_id == VisitOccurrence.discharge_to_concept_id, isouter=True)

    response_data = __filter_page__(response_data, param).all()
    response_data = l_convert.convert_dict(response_data)
    for response in response_data:
        response['방문 유형'] = l_translate.visit_concept[response['방문 유형']]

    return {'검색 결과': response_data}


def get_condition_occurrence(param, db):
    condition_concept = aliased(Concept)
    condition_type = aliased(Concept)
    condition_status = aliased(Concept)

    response_data = db.query(ConditionOccurrence.condition_occurrence_id,
                             ConditionOccurrence.person_id,
                             ConditionOccurrence.condition_concept_id,
                             ConditionOccurrence.condition_start_date,
                             ConditionOccurrence.condition_start_datetime,
                             ConditionOccurrence.condition_end_date,
                             ConditionOccurrence.condition_end_datetime,
                             ConditionOccurrence.stop_reason,
                             ConditionOccurrence.provider_id,
                             ConditionOccurrence.visit_occurrence_id,
                             ConditionOccurrence.visit_detail_id,
                             ConditionOccurrence.condition_source_value,
                             ConditionOccurrence.condition_source_concept_id,
                             ConditionOccurrence.condition_status_status_source_value,
                             ConditionOccurrence.condition_type_concept_id,
                             ConditionOccurrence.condition_status_concept_id,
                             condition_concept.concept_name.label('condition_concept_name'),
                             condition_type.concept_name.label('condition_type_name'),
                             condition_status.concept_name.label('condition_status_name'))\
        .join(condition_type, condition_type.concept_id == ConditionOccurrence.condition_type_concept_id, isouter=True)\
        .join(condition_concept, condition_concept.concept_id == ConditionOccurrence.condition_concept_id, isouter=True)\
        .join(condition_status, condition_status.concept_id == ConditionOccurrence.condition_status_concept_id, isouter=True)

    response_data = __filter_page__(response_data, param).all()
    response_data = l_convert.convert_dict(response_data)

    return {'검색 결과': response_data}


def get_drug_exposure(param, db):
    drug_concept = aliased(Concept)
    drug_concept_source = aliased(Concept)
    drug_route_concept = aliased(Concept)
    drug_type = aliased(Concept)

    response_data = db.query(DrugExposure.drug_exposure_id,
                             DrugExposure.person_id,
                             DrugExposure.drug_concept_id,
                             DrugExposure.drug_exposure_start_date,
                             DrugExposure.drug_exposure_start_datetime,
                             DrugExposure.drug_exposure_end_date,
                             DrugExposure.drug_exposure_end_datetime,
                             DrugExposure.verbatim_end_date,
                             DrugExposure.drug_type_concept_id,
                             DrugExposure.stop_reason,
                             DrugExposure.refills,
                             DrugExposure.quantity,
                             DrugExposure.days_supply,
                             DrugExposure.sig,
                             DrugExposure.route_concept_id,
                             DrugExposure.lot_number,
                             DrugExposure.provider_id,
                             DrugExposure.visit_occurrence_id,
                             DrugExposure.visit_detail_id,
                             DrugExposure.drug_source_concept_id,
                             DrugExposure.route_source_value,
                             DrugExposure.dose_unit_source_value,
                             drug_concept.concept_name.label('drug_concept_name'),
                             drug_type.concept_name.label('drug_type_name'),
                             drug_concept_source.concept_name.label('drug_concept_source_name'),
                             drug_route_concept.concept_name.label('drug_route_name'))\
        .join(drug_concept_source, drug_concept_source.concept_id == DrugExposure.drug_source_concept_id, isouter=True)\
        .join(drug_concept, drug_concept.concept_id == DrugExposure.drug_concept_id, isouter=True)\
        .join(drug_route_concept, drug_route_concept.concept_id == DrugExposure.route_concept_id, isouter=True)\
        .join(drug_type, drug_type.concept_id == DrugExposure.drug_type_concept_id, isouter=True)

    response_data = __filter_page__(response_data, param).all()
    response_data = l_convert.convert_dict(response_data)

    return {'검색 결과': response_data}


def get_death(param, db):
    cause_concept = aliased(Concept)
    cause_source_concept = aliased(Concept)

    response_data = db.query(Death.person_id,
                             Death.death_date,
                             Death.death_datetime,
                             Death.death_type_concept_id,
                             Death.cause_concept_id,
                             Death.cause_source_value,
                             Death.cause_source_concept_id,
                             cause_concept.concept_name.label(''),
                             cause_source_concept.concept_name.label('')
                             ) \
        .join(cause_concept, cause_concept.concept_id == Death.cause_concept_id, isouter=True) \
        .join(cause_source_concept, cause_source_concept.concept_id == Death.cause_source_concept_id, isouter=True)

    response_data = __filter_page__(response_data, param).all()
    response_data = l_convert.convert_dict(response_data)

    return {'검색 결과': response_data}


def get_concept(param, db):
    response_data = db.query(Concept.concept_id,
                             Concept.concept_name,
                             Concept.concept_code,
                             Concept.concept_class_id,
                             Concept.domain_id,
                             Concept.vocabulary_id,
                             Concept.standard_concept,
                             Concept.valid_start_date,
                             Concept.valid_end_date,
                             Concept.invalid_reason
                             )

    response_data = __filter_page__(response_data, param).all()
    response_data = l_convert.convert_dict(response_data)

    return {'검색 결과': response_data}


def __filter_page__(response_data, param):
    if 'column' in param and 'keyword' in param:
        keyword = "%{}%".format(param['keyword'])
        response_data = response_data.filter(getattr(Death, param['column']).like(keyword))

    if not ('limit' in param):
        param['limit'] = 10

    if not ('offset' in param):
        param['offset'] = 0
    else:
        param['offset'] = int(param['offset'])
        param['offset'] *= int(param['limit'])

    return response_data.offset(param['offset']).limit(param['limit'])