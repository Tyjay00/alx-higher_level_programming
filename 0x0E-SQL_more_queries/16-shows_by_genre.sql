-- Lists all shows and all genres linked to those shows from the database hbtn_0d_tvshows

-- Selects the title of TV shows and the name of genres linked to those shows
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
