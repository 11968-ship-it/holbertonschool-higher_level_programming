-- A script that lists all TV shows with their genre IDs (shows without genres should show NULL)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- join tv_show_genres in a way that includes shows without genres
ON ...
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
