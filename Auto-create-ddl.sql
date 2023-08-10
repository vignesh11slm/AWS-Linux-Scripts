SELECT ddl
FROM (
    SELECT 'CREATE TABLE ' || table_schema || '.' || table_name || ' (' || listagg(column || ' ' || type, ', ') WITHIN GROUP (ORDER BY ordinal_position) || ');' AS ddl
    FROM information_schema.columns
    WHERE table_schema = 'public'  -- Adjust the schema name as needed
    GROUP BY table_schema, table_name
    
    UNION ALL
    
    SELECT 'CREATE OR REPLACE VIEW ' || table_schema || '.' || table_name || ' AS ' || view_definition || ';' AS ddl
    FROM information_schema.views
    WHERE table_schema = 'public'  -- Adjust the schema name as needed
) AS ddl_statements;
