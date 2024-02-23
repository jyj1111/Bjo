-- 코드를 입력하세요
with a as (select * from USER_INFO where year(JOINED)='2021')
,b as (select o.user_id,SALES_DATE from a join ONLINE_SALE o on a.USER_ID=o.USER_ID)
select year(SALES_DATE) AS YEAR,month(SALES_DATE) AS MONTH,count(distinct (user_id)) AS PUCHASED_USERS,
    round(count(distinct(user_id))/(select count(*) from a),1) AS PUCHASED_RATIO 
    from b group by YEAR,MONTH order by YEAR,MONTH