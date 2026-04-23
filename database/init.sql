-- =====================================================
-- АИС БИБЛИОТЕКИ
-- Скрипт инициализации базы данных с тестовыми данными
-- =====================================================

-- 📚 КАТЕГОРИИ
INSERT INTO library_app_category (name) VALUES
('Русская литература'),
('Django'),
('Кибербезопасность'),
('История');

-- 👨‍🎓 АВТОРЫ
INSERT INTO library_app_author (full_name) VALUES
('Лев Толстой'),
('Фёдор Достоевский'),
('Александр Пушкин'),
('Иван Тургенев'),
('Николай Гоголь'),
('William S. Vincent'),
('Adrian Holovaty'),
('Jacob Kaplan-Moss'),
('Nigel George'),
('Antonio Melé'),
('Kevin Mitnick'),
('Bruce Schneier'),
('Jon Erickson'),
('Mark Stamp'),
('Charlie Miller'),
('Юваль Ной Харари'),
('Сергей Соловьёв'),
('Николай Карамзин'),
('Эрик Хобсбаум'),
('Антони Бивор');

-- 🏢 ИЗДАТЕЛИ
INSERT INTO library_app_publisher (name) VALUES
('Эксмо'),
('Питер'),
('O''Reilly'),
('Packt Publishing'),
('АСТ');

-- 📖 КНИГИ (Русская литература)
INSERT INTO library_app_book (isbn, title, author_id, publisher_id, category_id, year, copies, available) VALUES
('RUS1', 'Война и мир', 1, 1, 1, 1869, 5, 5),
('RUS2', 'Преступление и наказание', 2, 1, 1, 1866, 5, 5),
('RUS3', 'Евгений Онегин', 3, 5, 1, 1833, 5, 5),
('RUS4', 'Отцы и дети', 4, 5, 1, 1862, 5, 5),
('RUS5', 'Мёртвые души', 5, 5, 1, 1842, 5, 5);

-- 💻 КНИГИ (Django)
INSERT INTO library_app_book (isbn, title, author_id, publisher_id, category_id, year, copies, available) VALUES
('DJ1', 'Django for Beginners', 6, 3, 2, 2022, 3, 3),
('DJ2', 'The Django Book', 7, 3, 2, 2019, 3, 3),
('DJ3', 'Django Unleashed', 8, 4, 2, 2015, 3, 3),
('DJ4', 'Mastering Django', 9, 4, 2, 2020, 3, 3),
('DJ5', 'Django 3 By Example', 10, 4, 2, 2021, 3, 3);

-- 🔐 КНИГИ (Кибербезопасность)
INSERT INTO library_app_book (isbn, title, author_id, publisher_id, category_id, year, copies, available) VALUES
('SEC1', 'The Art of Deception', 11, 3, 3, 2002, 4, 4),
('SEC2', 'Applied Cryptography', 12, 3, 3, 1996, 4, 4),
('SEC3', 'Hacking: The Art of Exploitation', 13, 3, 3, 2008, 4, 4),
('SEC4', 'Information Security', 14, 4, 3, 2011, 4, 4),
('SEC5', 'The Hacker Playbook', 15, 4, 3, 2018, 4, 4);

-- 🏛 КНИГИ (История)
INSERT INTO library_app_book (isbn, title, author_id, publisher_id, category_id, year, copies, available) VALUES
('HIS1', 'Sapiens', 16, 5, 4, 2011, 4, 4),
('HIS2', 'История России', 17, 1, 4, 1851, 4, 4),
('HIS3', 'История государства Российского', 18, 1, 4, 1818, 4, 4),
('HIS4', 'Век революции', 19, 5, 4, 1962, 4, 4),
('HIS5', 'Сталинград', 20, 5, 4, 1998, 4, 4);