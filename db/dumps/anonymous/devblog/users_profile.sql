create table users_profile
(
    id      bigint auto_increment
        primary key,
    image   varchar(100) not null,
    user_id int          not null,
    constraint user_id
        unique (user_id),
    constraint users_profile_user_id_2112e78d_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

