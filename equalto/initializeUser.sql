CREATE DEFINER=`root`@`localhost` PROCEDURE `initializeUser`(
    IN p_email VARCHAR(200), IN p_startTime bigint, IN p_endTime bigint
)
BEGIN
insert into `equalto`.`equalto_vision17_users`
        (
            email,
            startTime,
            endTime
        )
        values
        (
            p_email,
            p_startTime,
            p_endTime
        );

END