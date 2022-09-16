# !/bin/sh

jq="/Users/eabradol/.brew/Cellar/jq/1.6/bin/jq"

OUTPUT_FILE="hh.json"
VACANCY_AMOUNT="20"

VACANCY_NAME="${1/ /+}"

curl -k -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$VACANCY_NAME&per_page=$VACANCY_AMOUNT" | jq > $OUTPUT_FILE

