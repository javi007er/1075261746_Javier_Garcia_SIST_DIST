DROP DATABASE IF EXISTS parcial1;

create database parcial1;

use parcial1;

create table usuario(
id int primary key auto_increment,
nombre varchar (50) not null,
tipo varchar (50) not null
);

create table libro(
id int primary key auto_increment,
titulo varchar (50) not null,
categoria varchar (50) not null,
sala_id int

);

create table prestamo(
id int primary key auto_increment,
usuario_id int,
libro_id int,
fecha_prestamo date,
fecha_devolucion date

);

create table sala(
id int primary key auto_increment,
nombre varchar (50) not null,
sala_id int

);



