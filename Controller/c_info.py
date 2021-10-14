from sqlalchemy import func
from models import Person, Concept, VisitOccurrence, ConditionOccurrence, Death, DrugExposure
from library import l_translate, l_convert


def get_person(db):
    total_count = db.query(func.count(Person.person_id)
                           .label("전체 환자 수")) \
        .all()

    gender_count = db.query(Concept.concept_name,
                            func.count(Person.gender_concept_id)) \
        .join(Concept, Concept.concept_id == Person.gender_concept_id) \
        .group_by(Concept.concept_name) \
        .all()

    race_count = db.query(Concept.concept_name,
                          func.count(Person.race_concept_id)) \
        .join(Concept, Concept.concept_id == Person.race_concept_id) \
        .group_by(Concept.concept_name) \
        .all()

    ethnicity_count = db.query(Concept.concept_name,
                               func.count(Person.ethnicity_concept_id)) \
        .join(Concept, Concept.concept_id == Person.ethnicity_concept_id) \
        .group_by(Concept.concept_name) \
        .all()

    death_count = db.query(func.count(Person.person_id)) \
        .join(Death,
              Person.person_id == Death.person_id) \
        .all()

    response_data = {
        '전체 환자 수': [dict(total_count[0])],
        '성별 방문 수': l_convert.do(gender_count),
        '인종별 방문 수': l_convert.do(race_count),
        '민족별 방문 수': l_convert.do(ethnicity_count),
        '사망 환자 수': [dict(death_count[0])]
    }
    return response_data


def get_visit(db):
    visit_concept_data = db.query(Concept.concept_name,
                                  func.count(VisitOccurrence.visit_concept_id)) \
        .join(Concept, Concept.concept_id == VisitOccurrence.visit_concept_id) \
        .group_by(Concept.concept_name) \
        .all()

    visit_concept_data = l_convert.do(visit_concept_data)
    for visit_concept in visit_concept_data:
        key = list(visit_concept.keys())[0]
        visit_concept[l_translate.visit_concept[key]] = visit_concept.pop(key)

    gender_data = db.query(Concept.concept_name, func.count(Person.gender_concept_id)) \
        .join(Concept, Concept.concept_id == Person.gender_concept_id) \
        .join(VisitOccurrence, VisitOccurrence.person_id == Person.person_id) \
        .group_by(Concept.concept_name) \
        .all()

    race_data = db.query(Concept.concept_name,
                         func.count(Person.race_concept_id)) \
        .join(Concept, Concept.concept_id == Person.race_concept_id) \
        .join(VisitOccurrence, VisitOccurrence.person_id == Person.person_id) \
        .group_by(Concept.concept_name) \
        .all()

    ethnicity_data = db.query(Concept.concept_name,
                              func.count(Person.ethnicity_concept_id)) \
        .join(Concept, Concept.concept_id == Person.ethnicity_concept_id) \
        .join(VisitOccurrence, VisitOccurrence.person_id == Person.person_id) \
        .group_by(Concept.concept_name) \
        .all()

    query = """
    SELECT
        CASE
            WHEN (SELECT date_part('year', now())) - person.year_of_birth < 10
                THEN '10이하'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 10 AND 19
                THEN '10대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 20 AND 29
                THEN '20대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 30 AND 39
                THEN '30대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 40 AND 49
                THEN '40대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 50 AND 59
                THEN '50대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 60 AND 69
                THEN '60대'
            WHEN (SELECT date_part('year', now()))- person.year_of_birth BETWEEN 70 AND 79
                THEN '70대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 80 AND 89
                THEN '80대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth BETWEEN 90 AND 99
                THEN '90대'
            WHEN (SELECT date_part('year', now())) - person.year_of_birth > 99
                THEN '90대 이상'
            END AS age,
        COUNT(*)
    FROM de.visit_occurrence
        JOIN person ON ( de.visit_occurrence.person_id = de.person.person_id )
    GROUP BY
        age
    """
    age_data = db.execute(query).all()

    response_data = {
        '방문 유형별 방문 수': visit_concept_data,
        '성별 방문 수 ': l_convert.do(gender_data),
        '인종별 방문 수': l_convert.do(race_data),
        '민족별 방문 수': l_convert.do(ethnicity_data),
        '연령대 별 방문 수': l_convert.do(age_data)
    }
    return response_data
