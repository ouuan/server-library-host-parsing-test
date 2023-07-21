# server library host parsing test

Some tests inspired by [Host of Troubles](https://hostoftroubles.com/).

You can use [Docker Compose](https://docs.docker.com/compose/) to run the tests and directly get the results: `sudo docker compose up --build`.

Servers:

-   Node.js [`http`](https://nodejs.org/api/http.html) (20.4.0)
-   Python [`http.server`](https://docs.python.org/3/library/http.server.html) (3.11.3)
-   Python [Django](https://www.djangoproject.com/) (4.2.3)
-   Rust (1.71.0) [hyper](https://hyper.rs/) (0.14.27)
-   Go [`net/http`](https://pkg.go.dev/net/http) (1.20.6)
-   Ruby (3.0.5) [Sinatra](https://sinatrarb.com/) (3.0.6) with [Webrick](https://github.com/ruby/webrick) (1.8.1)
-   PHP (8.2.8)

See [`test.py`](test.py) for the test cases:

-   Normal
-   No Host header
-   Multiple Host headers
-   Space-preceded Host as first header
-   Space-preceded Host header after another Host
-   Non-first space-preceded the only Host header
-   Space-after-colon Host header
-   Space-succeeded Host header
-   Empty Host header
-   Empty Host header with line-folding

See [`test-servers-result.txt`](results/test-servers-result.txt) for the raw results.

|                          | Node  |  Python   |  Django  |   hyper   |  Go   | Sinatra  |    PHP    |
| :----------------------: | :---: | :-------: | :------: | :-------: | :---: | :------: | :-------: |
|          normal          |   -   |     -     |    -     |     -     |   -   | no port  |     -     |
|         multiple         | first |   first   |   400    |   first   |  400  |  concat  |   first   |
|         no host          |  400  | undefined | fallback | undefined |  400  | fallback | undefined |
|     space-prec-first     |  400  | undefined | fallback |    400    |  400  |   400    | undefined |
|     space-prec-after     | fold  | multiline |   400    |    400    |  400  |   fold   |   first   |
|     space-prec-only      |  400  | undefined | fallback |    400    |  400  | fallback | undefined |
|    space-after-colon     | trim  |   trim    |   trim   |   trim    | trim  |   trim   |   trim    |
|     space-succeeded      | trim  | trailing  |   trim   |   trim    | trim  |   trim   | trailing  |
|          empty           | empty |   empty   |   400    |   empty   | empty |  empty   |   empty   |
|    empty-line-folding    |  400  | multiline |   400    |    400    | empty |  empty   |   empty   |

Here "fallback" means something like "127.0.0.1". Django provides `HttpRequest.get_host()` and Sinatra provides `request.host`, which are special properties of the request instead of just a header.
