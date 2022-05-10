CREATE OR REPLACE TRIGGER TRG_INS_AUDITORIA
BEFORE UPDATE OF AUTHOR_LAST_NAME ON BOOKS
FOR EACH ROW 
BEGIN
	INSERT INTO TRACK_AUDITOR (
        usuario,
        valor_anterior,
        valor_nuevo,
        operacion,
        fecha
    ) VALUES (
        sys_context('userenv','current_user'),
        :old.author_last_name,
        :new.author_last_name,
        'UPDATE',
        SYSDATE
    );
END;