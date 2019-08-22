drop table if exists users;
    create table users (
        id integer primary key autoincrement,
        email text not null,
        username text not null,
        password text not null
    );

drop table if exists tests;
    create table tests (
        -- testid integer,
        quesid integer PRIMARY KEY autoincrement,
        QUES text not null,
        optionA text not null,
        optionB text not null,
        optionC text not null,
        optionD text not null,
        ans text not null
    );    