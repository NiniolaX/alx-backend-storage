-- Script creates a trigger that resets the attribute 'valid_email' only when the email has been changed
-- Query to create trigger
DELIMITER $$
CREATE TRIGGER validate_email
    BEFORE UPDATE ON users
    FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ;