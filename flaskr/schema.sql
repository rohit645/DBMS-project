drop table if exists users;
    create table users (
        id integer primary key autoincrement,
        email text not null,
        username text not null,
        password text not null
    );

drop table if exists tests;
    create table tests (
        testid integer,
        quesid integer PRIMARY KEY autoincrement,
        QUES text not null,
        option1 text not null,
        option2 text not null,
        option3 text not null,
        option4 text not null,
        ans text not null
    );    