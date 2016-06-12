use stock

drop table stk_data;

create table stk_data
(
quote_date date,
symbol varchar(10),
name varchar(40),
open_price double (12,5),
close_price double (12,5),
high_52_wk double (12,5),
low_52_wk double (12,5),
ma_200_day double (12,2),
revenue varchar (40),
market_cap varchar (40),
PEG varchar (40),
yield varchar (40),
beta double (12,5)
);


