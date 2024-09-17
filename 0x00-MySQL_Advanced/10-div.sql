-- Script creates a function that computes and returns the division of two numbers, but returns 0 if the second number is 0
-- Query that creates function
DELIMITER $$

CREATE FUNCTION SafeDiv (a INT, b INT)
    RETURNS FLOAT DETERMINISTIC
    BEGIN
        DECLARE result FLOAT;
        IF b = 0 THEN
            SET result = 0;
        ELSE
            SET result = a / b;
        END IF;
        RETURN result;
    END $$

DELIMITER ;