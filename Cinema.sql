SET autocommit = OFF;
use Cinema;
start transaction;

create table Genre(
id int primary key auto_increment,
Name varchar(30) NOT NULL unique
);

ALTER TABLE Genre ENGINE = MyISAM;

create table Movie(
id int primary key auto_increment,
Genre_id int NOT NULL, 
foreign key(Genre_id) references Genre(id),
Name varchar(50) NOT NULL unique,
Lenght int check(Lenght >0) NOT NULL,
Price decimal(10,2) check(Price >0) NOT NULL,
Premiere_date date
);

create table Hall(
id int primary key auto_increment,
Name varchar(30) unique NOT NULL,
Type varchar(30) check(Type in ('Standartní','VIP')) NOT NULL
);

create table Screening(
id int primary key auto_increment,
Movie_id int NOT NULL,
foreign key(Movie_id) references Movie(id),
Hall_id int NOT NULL,
foreign key(Hall_id) references Hall(id),
Date datetime NOT NULL
);

create table Customer(
id int primary key auto_increment,
Name varchar(30) NOT NULL,
Last_name varchar(30) NOT NULL,
Loyalty_program bit default(0),
Loyalty_points decimal(10,2) default(0) NOT NULL,
Registry_date date default (curdate()) NOT NULL
);

create table Rezervation(
id int primary key auto_increment,
Customer_id int NOT NULL,
foreign key(Customer_id) references Customer(id),
Screening_id int NOT NULL,
foreign key(Screening_id) references Screening(id),
Date date NOT NULL,
Ticket_ammount int check(Ticket_ammount >0) default(0) NOT NULL,
Total_price decimal(10,2) check(Total_price>=0) NOT NULL
);

create table Points(
id int primary key auto_increment,
Customer_id int,
foreign key(Customer_id) references Customer(id) ON DELETE CASCADE,
ammount decimal(10,2),
date date default (curdate()),
description varchar(50)
);

DELIMITER //
CREATE PROCEDURE InsertRezervation(IN _Customer_id int,IN _Screening_id int,IN _Date date,IN _Ticket_ammount int)
BEGIN
    DECLARE _Movie_id INT;
	Declare _price decimal(10,2);
    
    SELECT id INTO _Movie_id
    FROM Screening
    WHERE id = _Screening_id;
    
    select Price into _price
    from Movie
    where id = _Movie_id;
    
    set _price = _price*_Ticket_ammount;
    
    insert into Rezervation(Customer_id,Screening_id,Date,Ticket_ammount,Total_price) values(_Customer_id,_Screening_id,_Date,_Ticket_ammount,_price);
END //

DELIMITER //
CREATE PROCEDURE UpdateRezervation(IN _id int,IN _Customer_id int,IN _Screening_id int,IN _Date date,IN _Ticket_ammount int)
BEGIN
    DECLARE _Movie_id INT;
	Declare _price decimal(10,2);
    
    SELECT id INTO _Movie_id
    FROM Screening
    WHERE id = _Screening_id;
    
    select Price into _price
    from Movie
    where id = _Movie_id;
    
    set _price = _price*_Ticket_ammount;
    
    update Rezervation
    set Customer_id = _Customer_id,Screening_id = _Screening_id,Date = _Date,Ticket_ammount=_Ticket_ammount,Total_price=_price
    where id = _id;
END //

delimiter //
create view NextScreeningCustomers
as
select c.Name,c.Last_name,r.Date as Purchase_date,r.Ticket_ammount,r.Total_price
from Customer as c inner join Rezervation as r on r.Customer_id = c.id
					inner join Screening as s on r.Screening_id = s.id
where s.id =(
select id 
from Screening
where Date>current_time()
limit 1); //

delimiter //
create view TotalMovieTickets
as
select m.Name,sum(r.Ticket_ammount) as ammount
from Movie as m inner join Screening as s on s.Movie_id = m.id
				inner join Rezervation as r on r.Screening_id = s.id
group by m.Name; //

delimiter //
create view MovieSummary
as
SELECT m.Name AS Movie_Name,COUNT(r.id) AS Number_of_Reservations,SUM(r.Total_price) AS Total_Revenue,round(AVG(r.Ticket_ammount),2) as Average_ticket_ammount,round(AVG(r.Total_price),2) AS Average_Rezervation_Price
FROM Movie m JOIN Screening s ON m.id = s.Movie_id
			JOIN Rezervation r ON s.id = r.Screening_id
GROUP BY m.Name; //

DELIMITER //
CREATE PROCEDURE TransferPoints(IN _from_id int,IN _to_id int,IN _ammount int)
BEGIN
    UPDATE Customer 
    SET Loyalty_points = Loyalty_points-_ammount WHERE id = _from_id;
    
	insert into Points(Customer_id,ammount,description) values(_from_id,-_ammount,'Převod');
    
	UPDATE Customer 
    SET Loyalty_points = Loyalty_points+_ammount WHERE id = _to_id;
    
    insert into Points(Customer_id,ammount,description) values(_to_id,_ammount,'Převod');
END //

DELIMITER //
CREATE PROCEDURE CreateCustomer(IN _Name varchar(30), IN _Last_name varchar(30), In _Loyalty_program bit, In _Loyalty_points varchar(30))
BEGIN
    insert into Customer(Name, Last_name, Loyalty_program, Loyalty_points) values(_Name,_Last_name,_Loyalty_program,_Loyalty_points);
	insert into Points(Customer_id,ammount,description) values(LAST_INSERT_ID(),_Loyalty_points,'Založení účtu');
END //

delimiter //
create view All_rezervations
as
select c.Name,c.Last_name,r.date as Rezervation_date,r.Ticket_ammount,m.Name as Movie_name,h.name as Hall_name,h.type as Hall_type
from Customer as c inner join Rezervation as r on r.Customer_id = c.id
					inner join Screening as s on r.Screening_id = s.id
                    inner join Movie as m on s.Movie_id = m.id
					inner join Hall as h on s.Hall_id = h.id; //
                    
delimiter //
create view Hall_Type_Summary
as
select h.Type, g.Name,sum(r.Total_price) as Total_revenue
from Rezervation as r inner join Screening as s on r.Screening_id = s.id
                    inner join Movie as m on s.Movie_id = m.id
                    inner join Genre as g on m.Genre_id = g.id
					inner join Hall as h on s.Hall_id = h.id 
group by h.Type,g.Name; //

COMMIT