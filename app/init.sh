#!/bin/sh

sqlite3 app.db << EOF
.mode csv
.import test.csv test_tbl
select GroupName,Groupcode from test_tbl limit 5;
EOF