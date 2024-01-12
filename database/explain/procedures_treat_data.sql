CREATE OR REPLACE PROCEDURE remove_seal_in_sequence()
AS
$$
DECLARE
  jutsus jutsu_have_seal.jutsu_id%TYPE;

  jutsu_title jutsu.title%TYPE;

  first_seal jutsu_have_seal.seal_id%TYPE;
  actual_seal jutsu_have_seal.seal_id%TYPE;

  position_seek jutsu_have_seal.position%TYPE;
BEGIN
  FOR jutsus IN SELECT DISTINCT(jutsu_id) FROM jutsu_have_seal
    LOOP

      SELECT title into jutsu_title FROM jutsu WHERE id = jutsus;

      SELECT seal_id INTO first_seal 
      FROM jutsu_have_seal
      WHERE jutsu_id = jutsus AND position = 1;

      position_seek := 2;

      SELECT seal_id INTO actual_seal 
      FROM jutsu_have_seal 
      WHERE jutsu_id = jutsus AND position = position_seek;

      WHILE actual_seal IS NOT NULL
        LOOP

          IF first_seal = actual_seal THEN
              DELETE FROM jutsu_have_seal WHERE jutsu_id = jutsus and position = position_seek;
              raise notice '(%): %',  jutsus, jutsu_title;
          ELSE
            first_seal = actual_seal;
          END IF;

          position_seek := position_seek + 1;
          SELECT seal_id INTO actual_seal FROM jutsu_have_seal WHERE jutsu_id = jutsus AND position = position_seek;
        END LOOP;
    END LOOP;

END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE fix_positions_after_remove_seal_in_sequence()
AS
$$
DECLARE
  jutsus jutsu_have_seal.jutsu_id%TYPE;

  jutsu_title jutsu.title%TYPE;

  line RECORD;

BEGIN
  FOR jutsus IN SELECT DISTINCT(jutsu_id) FROM jutsu_have_seal
    LOOP

      SELECT title into jutsu_title FROM jutsu WHERE id = jutsus;

      FOR line IN SELECT jutsu_id, seal_id, position, ROW_NUMBER() OVER (ORDER BY position) AS new_position FROM jutsu_have_seal  WHERE jutsu_id = jutsus ORDER BY position
        LOOP
          IF line.position != line.new_position THEN
            UPDATE jutsu_have_seal SET position = line.new_position WHERE jutsu_id = line.jutsu_id AND position = line.position;
            raise notice '%: (pos,new)|(%,%)', jutsu_title, line.position, line.new_position;
          END IF;
        END LOOP;
    END LOOP;

END;
$$
LANGUAGE plpgsql;

update jutsu_have_seal set seal_id = 1 where seal_id >= 14;
update seal set label = 'Desconhecido' where id = 1;
delete from seal where id >= 14;

CALL remove_seal_in_sequence();
CALL fix_positions_after_remove_seal_in_sequence();
