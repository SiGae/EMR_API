from models import Person, Concept, VisitOccurrence, ConditionOccurrence, Death, DrugExposure
from sqlalchemy import or_
from library import l_convert


def get_concept(db, param):
    search = db.query(Concept.concept_id,
                      Concept.concept_name,
                      Concept.vocabulary_id,
                      Concept.domain_id,
                      Concept.concept_class_id,
                      Concept.concept_code)\
        .order_by(Concept.concept_id.asc())
    if 'keyword' in param:
        keyword = "%{}%".format(param['keyword'])
        search = search.filter(or_(Concept.concept_name.like(keyword),
                                   Concept.domain_id.like(keyword),
                                   Concept.vocabulary_id.like(keyword),
                                   Concept.concept_code.like(keyword))
                               )

    if 'id' in param:
        search = search.filter(Concept.concept_id == param['id'])

    if not('limit' in param):
        param['limit'] = 10

    if not('offset' in param):
        param['offset'] = 0
    else:
        param['offset'] = int(param['offset'])
        param['offset'] *= int(param['limit'])

    response_data = search.offset(param['offset']).limit(param['limit']).all()
    response_data = l_convert.convert_dict(response_data)

    return {'검색 결과': response_data}
