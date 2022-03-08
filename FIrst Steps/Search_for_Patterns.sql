-- Quieres retornar filas que posean cierto patron.
-- Solution:  Use the LIKE operator whit the %

select ename, job
from emp
where deptno in (10,20)
and (ename like '%I%' or job like '%ER')


--Discusion: Tambien se provee el simbolo "_" para considir con un solo caracter. '%I%' : Encerrar una cadena de caracteres en las % hace que se encuentren resultados de cualquier cosa que contenga "I".
-- '%ER' : ESto devuelve las palabras terminadas en ER
-- 'ER%' : Esto devuelve las palabras que empeizan con ER
