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

delimiter //
create view MovieJoin
as
select Movie.id,Movie.Name as Movie,Genre.Name as Genre,Lenght,Price,Premiere_date 
from Movie inner join Genre on Movie.Genre_id = Genre.id
//
COMMIT