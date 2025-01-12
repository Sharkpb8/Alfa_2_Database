SET autocommit = OFF;
use Cinema;
start transaction;

create table Genre(
id int primary key auto_increment,
Name varchar(30) NOT NULL unique
);

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

COMMIT