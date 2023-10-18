create table blog_post
(
    id          bigint auto_increment
        primary key,
    title       varchar(450) not null,
    content     longtext     not null,
    author_id   int          not null,
    date_posted datetime     null,
    constraint blog_post_author_id_dd7a8485_fk_auth_user_id
        foreign key (author_id) references auth_user (id)
);

