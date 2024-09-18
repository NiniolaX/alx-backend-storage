-- Script ranks the country of origin of bands in 'metal_bands.sql', ordered by the number of (non-unique) fans
-- Group bands by country and sum of fans
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;