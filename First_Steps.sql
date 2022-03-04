-- BASIC CONCEPTS

select *
from emp 
where deptno  = 10 
or comm is not null 
or sal < = 2000 
and deptno =20


select * from emp 
where (dptno =10 
or comm is not null 
or sal <= 2000
)
and deptno=20


select ename , dpto, sal
from emp

select sal as salary, comm as commision
from emp


select sal as salary, comm as commission
from emp
where salary < 5000    ----->FAILSSSSSSSS:: No se puede referenciar un alias en un where, ya que primero se evalua el where y al final de esto se creara el alias 

select * from (
select sal as salary, comm as commission
from emp
) x 
where salary <5000

-- WHERE se evalua antes que SELECT¡¡

-- CONCAT:: || ^ +  :: pARA CONCATENAR DOS O MAS COLUMNAS

select ename || 'WORK AS A' || job as msg
from emp
where deptno=10


-- Case expression to perfrom conditiona logic directlyy in your SELECT

select ename , sal, 
case when sal <= 2000 then 'UNDERPAID'
when sal >= 4000 then 'OVERPAID'
else 'OK'
end as status
from emp

-- TO lIMIT THE NUMBER OF ROWS RETURNED ::

rownum
select *    ,   select top 5 *
	from emp
limit 5  ,   where rownum <=5 , from emp

-- 










