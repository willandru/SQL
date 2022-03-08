-- Tienes filas que tienen valores NULL, y quieres devolver valores NO-NULOS

-- Solution: Use the function COALESCE to substitute with Real values

select coalesce(comm,0)
from emp

