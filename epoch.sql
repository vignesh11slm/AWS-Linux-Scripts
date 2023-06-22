SELECT
  datehour,
  (DATE_PART('epoch', TIMESTAMP 'epoch' + (DATE_TRUNC('hour', TO_TIMESTAMP(datehour, 'YYYYMMDDHH')) - TIMESTAMP 'epoch')))::bigint AS epochtime
FROM
  your_table;
