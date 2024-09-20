-- Script lists all bands with 'Glam rock' as their main style ranked by longevity
-- Query to select bands with 'Glam rock' as their main style, ordered by longevity
SELECT band_name, IF(split IS NULL, 2022 - formed, split - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', style) > 0
    ORDER BY lifespan DESC;