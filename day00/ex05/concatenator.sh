

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > concatenator.csv
cat 20*.csv | sed -En '/^"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"$/!p' >> concatenator.csv
