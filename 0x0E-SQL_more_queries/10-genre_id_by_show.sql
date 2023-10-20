-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

-- Selects the title of TV shows and their associated genre IDs
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
