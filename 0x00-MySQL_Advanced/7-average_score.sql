-- Script creates a stored procedure that computes and stores the average score for a student
-- Query to create stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(userid INT)
BEGIN 
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score)
        FROM corrections
        WHERE user_id = userid);
    UPDATE users
        SET average_score = avg_score
            WHERE id = userid;
END $$

DELIMITER ;