-- list join --

SELECT t.title, tg.genre_id
FROM tv_shows t LEFT JOIN tv_show_genres tg
ON t.id = tg.show_id
WHERE tg.genre_id IS NULL
ORDER BY t.title, tg.genre_id ASC;