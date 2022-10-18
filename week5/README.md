# Assignment - Week 5

## Install
This project uses MySQL. Go check them out if you don't have them locally installed.

`https://www.mysql.com/.`

## Content
###  Task 3
1. 

```
insert into member(id, name, username, password, follower_count, time)values (1, 'Amy', 'test', 'test', 100, '2008-08-08 22:10:40');
insert into member(id, name, username, password, follower_count, time)values (2, 'Ben', 'aaa', 'aaa', 150, '2011-02-11 11:18:20');
insert into member(id, name, username, password, follower_count, time)values (3, 'Charlie', 'bbb', 'bbb', 20, '2003-12-01 03:55:50');
insert into member(id, name, username, password, follower_count, time)values (4, 'Doris', 'ccc', 'ccc', 450, '2020-01-01 15:35:10');
insert into member(id, name, username, password, follower_count, time)values (5, 'Eric', 'ddd', 'ddd', 80, '2009-03-03 09:30:00');
```
![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_01.png)

2.

```select * from member;```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_02.png)

3.

```select * from member order by time desc;```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_03.png)

4.

```select * from member order by time desc limit 1,3;```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_04.png)

5.

```select * from member where username='test';```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_05.png)

6.

 ```select * from member where username='test' and password='test';```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_06.png)

7.

```update member set name='test2' where username='test';```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task3_07.png)

### Task 4

1.

`select count(*) from member;`

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task4_01.png)

2.

`select sum(follower_count) from member;`

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task4_02.png)

3.

`select avg(follower_count) from member;`

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task4_03.png)

### Task 5

1.

```
CREATE TABLE message(
id bigint primary key auto_increment, 
member_id bigint not null, 
content varchar(255) not null, 
like_count int unsigned not null default 0,
time datetime not null default current_timestamp
);
```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task5_00.png)

2.

```select member.name, message.content from member inner join message on member.id=message.member_id;```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task5_01.png)

3.

```select member.name, message.content from member inner join message on member.id=message.member_id where user name='test';```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task5_02.png)

4.

```select avg(like_count) from member inner join message on member.id=message.member_id where username='test';```

![](/Users/stephy/Desktop/Wehelp-Assignment-2022/week5/screenshots/Task5_04.png)
