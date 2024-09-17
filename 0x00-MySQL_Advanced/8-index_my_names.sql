-- Script creates an index on the table 'names' and the first letter of 'name'
-- Query that creates index
CREATE index idx_name_first
    ON names(name(1));