
INPUT_FILE="../ex00/hh.json"
FILTER_FILE=filter.jq
OUTPUT_FILE=hh.csv

cat $INPUT_FILE | jq -rf $FILTER_FILE > $OUTPUT_FILE
