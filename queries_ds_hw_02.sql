-- 1st hw point--
select t.id as task_id, t.title, t.description as task_description, u.id as user_id, u.fullname
from tasks as t
inner join users as u on u.id = t.user_id
WHERE user_id = 10;


--2nd hw point--
select t.id as task_id, t.title, t.description, s.name as status
from tasks as t
inner join status as s on s.id = t.status_id
WHERE status_id in (select id
from status s 
where s.name = 'new');


--3rd hw point--
UPDATE tasks SET status_id = 2 WHERE id = 2;


--added new user who doesn't have any task--
INSERT INTO users (id, fullname, email)
VALUES (11, 'Izya Abramovych', 'abramovych@gmail.com');


--4th hw point--
select id, fullname, email
from users u 
where fullname not in(select u.fullname
from tasks as t
inner join users as u on u.id = t.user_id
group by u.fullname);


--5th hw point--
INSERT INTO tasks (id, title, description, status_id, user_id)
VALUES (101, 'task-1313', 'new task for fifth hw task', 1, 10);


--6th hw point--
select t.id, t.title, s.name 
from tasks as t
inner join status as s on s.id = t.status_id 
where s.name <> 'completed';


--7th hw point--
DELETE FROM tasks WHERE id = 99;


--8th hw point--
select id, fullname, email
from users u 
where email like '%@yahoo.com'
order by fullname;


--9th hw point--
UPDATE users SET fullname = 'Duke Dracula' WHERE id = 7;


--10th hw point--
select count(t.title) as task_q_ty, s.name
from tasks as t
inner join status as s on s.id = t.status_id
group by s.name
order by s.id;


--11th hw point--
select t.id, t.title, u.fullname, u.email 
from tasks as t
join users as u on u.id = t.user_id
WHERE u.email like '%@hotmail.com';


--12th hw point--
--first add a task without description--
INSERT INTO tasks (id, title, status_id, user_id)
VALUES (102, 'task-1314', 1, 9);
--the request for tasks without description--
select id, title
from tasks 
WHERE description is NULL;


--13th hw point--
select u.fullname, t.title, s.name
from tasks as t
inner join users as u on u.id = t.user_id
inner join status as s on s.id = t.status_id
WHERE s.name = 'in progress'
order by u.fullname;


--14th hw point--
select u.id, u.fullname, count(t.id)
from users as u 
left join tasks as t on t.user_id = u.id
group by u.fullname
order by u.id;








