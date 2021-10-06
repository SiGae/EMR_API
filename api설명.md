# API 설명

## 통계

/info/person - 환자 통계

`전체 환자 수`

`성별 환자 수`

`인종별 환자 수`

`민족별 환자 수`

`사망 환자 수`

/info/visit - 방문 통계

`방문 유형별 방문 수`

`성별 방문 수`

`인종별 방문 수`

`민족별 방문 수`

`방문시 연령대별 방문 수`

## Concept_id 정보

/concept

parameter

> key = 키워드 검색
> id = concept_id 검색
> limit = 출력할 데이터 양
> offset = 출력할 페이지 번호

## 테이블 row 조회

/search/person - 환자 테이블 조회

/search/visit_occurrence - 방문 테이블 조회

/search/condition_occurrence - 진단 정보 조회

/search/drug_exposure - 의약품 처방 정보 조회

/search/death - 사망 정보 조회

/search/concept - concept 정보 조회

parameter

> keyword = column과 함께 사용, column내 검색할 키워드
> column = 검색할 column지정
> limit = 출력할 데이터 양
> offset = 출력할 페이지 번호
