#0x00 - MySQL Advanced
This repository contains the following SQL scripts:
1. 0-uniq_users.sql - Creates a table _users_ with the following attributes:
	- id, integer, never null, auto increment and primary key
	- email, string (255 characters), never null and unique
	- name, string (255 characters)
2. 1-country_users.sql - Creates a table _users_ with the following attributes:
	- id, integer, never null, auto increment and primary key
	- email, string (255 characters), never null and unique
	- name, string (255 characters)
	- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)

