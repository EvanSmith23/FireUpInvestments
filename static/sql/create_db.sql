use FireUp;

create table houses (
	address varchar(75),
	city varchar(20),
	state varchar(2),
	zipcode varchar(10),
	description varchar(140),
	house_id int NOT NULL,
	PRIMARY KEY (house_id)
);

create table photos(
	picid varchar(40) NOT NULL,
	format char(3),
	house_id int NOT NULL,
	PRIMARY KEY (picid),
	FOREIGN KEY (house_id) references houses(house_id)
);
