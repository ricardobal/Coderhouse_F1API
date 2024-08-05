CREATE TABLE ricardobal_coderhouse.laps (
    date_start TIMESTAMP WITH TIME ZONE NOT NULL, -- Fecha y hora de inicio en UTC
    driver_number INTEGER NOT NULL,     -- Número único asignado al piloto
    duration_sector_1 DECIMAL(6, 3),    -- Tiempo en segundos para completar el primer sector
    duration_sector_2 DECIMAL(6, 3),    -- Tiempo en segundos para completar el segundo sector
    duration_sector_3 DECIMAL(6, 3),    -- Tiempo en segundos para completar el tercer sector
    i1_speed DECIMAL(6, 3),             -- Velocidad en km/h en el primer punto intermedio
    i2_speed DECIMAL(6, 3),             -- Velocidad en km/h en el segundo punto intermedio
    is_pit_out_lap BOOLEAN NOT NULL,    -- Valor booleano indicando si es una vuelta de salida del pit
    lap_duration DECIMAL(6, 3),         -- Tiempo total en segundos para completar la vuelta
    lap_number INTEGER NOT NULL,        -- Número secuencial de la vuelta dentro de la sesión
    meeting_key INTEGER,                -- Identificador único para la reunión
    segments_sector_1 varchar(200),           -- Lista de valores representando mini-sectores en el primer sector
    segments_sector_2 varchar(200),           -- Lista de valores representando mini-sectores en el segundo sector
    segments_sector_3 varchar(200),           -- Lista de valores representando mini-sectores en el tercer sector
    session_key INTEGER NOT NULL,       -- Identificador único para la sesión
    st_speed DECIMAL(6, 3)              -- Velocidad en km/h en el punto de control de velocidad
);
