#!/bin/env python
# __author__ = 'wankun'
# -*- coding: utf-8 -*-

import os

src = open('data1.sql', 'r')
dest = open('data2.sql', 'w')

buf = []
for line in src:
    if len(buf) == 0:
        buf.append('BEGIN\n')
    if line.find("'\\0'") > 0:
        line = line.replace("'\\0'", "0")
    if line.find("'\\1'") > 0:
        line = line.replace("'\\1'", "1")
    if line.startswith('''INSERT INTO "TBLS" VALUES'''):
        line = line.replace(''',NULL);''', ''');''')
    elif line.startswith('''INSERT INTO "PARTITIONS" VALUES'''):
        line = line.replace(''',NULL);''', ''');''')
    elif line.startswith('''INSERT INTO "SDS" VALUES ('''):
        line = line.replace('''INSERT INTO "SDS" VALUES (''',
                            '''INSERT INTO "SDS"(SD_ID,CD_ID,INPUT_FORMAT,IS_COMPRESSED,IS_STOREDASSUBDIRECTORIES,LOCATION,NUM_BUCKETS,OUTPUT_FORMAT,SERDE_ID) VALUES (''')

    if line.startswith('INSERT INTO'):
        line = line.replace('INSERT INTO', 'INSERT /*+ append nologging */ INTO')

    if not line.startswith('INSERT /*+ append nologging */ INTO "VERSION"'):
        buf.append(line)

    if len(buf) == 2000:
        buf.append('END;\n')
        buf.append('/\n')
        dest.writelines(buf)
        buf = []

if len(buf) != 0:
    buf.append('END;\n')
    buf.append('/\n')
    dest.writelines(buf)
    buf = []

dest.close()
src.close()
