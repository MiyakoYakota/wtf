-- Oracle SQL Developer export

CREATE TABLE "WEBAPP"."USERS" (
    "ID" NUMBER(10,0) NOT NULL,
    "EMAIL" VARCHAR2(255) NOT NULL,
    "USERNAME" VARCHAR2(100),
    "PASSWORD" VARCHAR2(255) NOT NULL,
    "NAME" VARCHAR2(200)
);

INSERT INTO "WEBAPP"."USERS" ("ID", "EMAIL", "USERNAME", "PASSWORD", "NAME") VALUES (1, 'alice@example.com', 'alice', 'hunter2', 'Alice Smith');
INSERT INTO "WEBAPP"."USERS" ("ID", "EMAIL", "USERNAME", "PASSWORD", "NAME") VALUES (2, 'bob@example.com', 'bob_jones', 'p@ssw0rd', 'Bob Jones');
INSERT INTO "WEBAPP"."USERS" ("ID", "EMAIL", "USERNAME", "PASSWORD", "NAME") VALUES (3, 'charlie@test.org', 'charlie', 'qwerty123', 'Charlie Brown');

COMMIT;
