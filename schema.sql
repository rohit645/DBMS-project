drop table if exists admin;
drop table if exists student;
    create table student (
        ROLLNO integer primary key,
        EMAIL text not null,
        PASSWORD text not null
    );
    -- create table admin (
    --     EID integer primary key,
    --     EMAIL text not null,
    --     PASSWORD text not null
    -- );