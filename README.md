# hw-17

MoviesView, DirectorsView, GenresView:
- get
- post

MovieView, DirectorView, GenreView:
- get
- put
- patch
- delete

- `/movies` — возвращает список всех фильмов,
- `/movies/<id>` — возвращает информацию о фильме.
- `/directors/` — возвращает всех режиссеров,
- `/directors/<id>` — возвращает информацию о режиссере,
- `/genres/` —  возвращает все жанры,
- `/genres/<id>` — возвращает информацию о жанре,
- `/movies/?director_id=2` — возвращает фильмы с определенным режиссером,
- `/movies/?genre_id=4` — возвращает фильмы с определенным жанром,
- `/movies/?director_id=2&genre_id=4` — возвращает фильмы с определенным режиссером и жанром,

- `POST /movies/` —  добавляет кино в фильмотеку,
- `PUT /movies/<id>` —  обновляет кино,
- `PATCH /movies/<id>` —  частично обновляет кино,
- `DELETE /movies/<id>` —  удаляет кино.
