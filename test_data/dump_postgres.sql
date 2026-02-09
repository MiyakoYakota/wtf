--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';

CREATE TABLE accounts (
    id serial PRIMARY KEY,
    email character varying(255) NOT NULL,
    username character varying(100),
    password character varying(255) NOT NULL,
    domain character varying(200)
);

COPY accounts (id, email, username, password, domain) FROM stdin;
1	alice@example.com	alice	hunter2	example.com
2	bob@example.com	bob_jones	p@ssw0rd	example.com
3	charlie@test.org	charlie	qwerty123	test.org
\.

INSERT INTO accounts (id, email, username, password, domain) VALUES (4, 'dave@corp.net', 'dave', 'letmein', 'corp.net');
