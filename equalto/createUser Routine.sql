CREATE DEFINER=`root`@`localhost` PROCEDURE `createUser`(
    IN p_email VARCHAR(200)
)
BEGIN
    if ( select exists (select 1 from HOD_equalto_users where email = p_email) ) THEN
     
        select submitted from HOD_equalto_users where email = p_email;
     
    ELSE
     
        insert into HOD_equalto_users
        (
            email,
            startTime,
            endTime
        )
        values
        (
            p_name,
            NOW(),
            NOW()+INTERVAL 30 MINUTE
        );
        
        select submitted from HOD_equalto_users where email = p_email;     
    END IF;
END