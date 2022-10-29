---
files: []
url: https://cdn.cs50.net/2022/fall/labs/7/songs/README.md
window: [terminal]
---

# Lab 7: Songs

{% alert warning %}

Labs are practice problems which, time permitting, may be started or completed in your {% if college %}lab{% else %}section{% endif %}, and are assessed on correctness only. You are encouraged to collaborate with classmates on this lab, though each member in a group collaborating is expected to contribute equally to the lab.

{% endalert %}

Write SQL queries to answer questions about a database of songs.

## Understanding

Provided to you is a file called `songs.db`, a SQLite database that stores data from [Spotify](https://developer.spotify.com/documentation/web-api/) about songs and their artists. This dataset contains the top 100 streamed songs on Spotify in 2018. In a terminal window, run `sqlite3 songs.db` so that you can begin executing queries on the database.

First, when `sqlite3` prompts you to provide a query, type `.schema` and press enter. This will output the `CREATE TABLE` statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.

Notice that every `artist` has an `id` and a `name`. Notice, too, that every song has a `name`, an `artist_id` (corresponding to the `id` of the artist of the song), as well as values for the danceability, energy, key, loudness, speechiness (presence of spoken words in a track), valence, tempo, and duration of the song (measured in milliseconds).

The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables. After you do so, you'll reflect on the ways Spotify might use this same data in their annual [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) campaign to characterize listeners' habits.

## Implementation Details

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You **should not** assume anything about the `id`s of any particular songs or artists: your queries should be accurate even if the `id` of any particular song or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of songs, for example, then your query should not also output each song's tempo.

1. In `1.sql`, write a SQL query to list the names of all songs in the database.
    * Your query should output a table with a single column for the name of each song.
1. In `2.sql`, write a SQL query to list the names of all songs in increasing order of tempo.
    * Your query should output a table with a single column for the name of each song.
1. In `3.sql`, write a SQL query to list the names of the top 5 longest songs, in descending order of length.
    * Your query should output a table with a single column for the name of each song.
1. In `4.sql`, write a SQL query that lists the names of any songs that have danceability, energy, and valence greater than 0.75.
    * Your query should output a table with a single column for the name of each song.
1. In `5.sql`, write a SQL query that returns the average energy of all the songs.
    * Your query should output a table with a single column and a single row containing the average energy.
1. In `6.sql`, write a SQL query that lists the names of songs that are by Post Malone.
    * Your query should output a table with a single column for the name of each song.
    * You should not make any assumptions about what Post Malone's `artist_id` is.
1. In `7.sql`, write a SQL query that returns the average energy of songs that are by Drake.
    * Your query should output a table with a single column and a single row containing the average energy.
    * You should not make any assumptions about what Drake's `artist_id` is.
1. In `8.sql`, write a SQL query that lists the names of the songs that feature other artists.
    * Songs that feature other artists will include "feat." in the name of the song.
    * Your query should output a table with a single column for the name of each song.

### Walkthrough

{% alert primary %}

This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!

{% endalert %}

{% video https://video.cs50.io/wgKPUd_95AA %}

### Hints

* See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!

{% spoiler "Not sure how to solve?" %}

{% video https://video.cs50.io/7hydPL9ZswE %}

{% endspoiler %}

### Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) is a feature presenting Spotify users' 100 most played songs from the past year. In 2021, Spotify Wrapped calculated an ["Audio Aura"](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) for each user, a "reading of \[their\] two most prominent moods as dictated by \[their\] top songs and artists of the year." Suppose Spotify determines an audio aura by looking at the average energy, valence, and danceability of a person's top 100 songs from the past year. In `answers.txt`, reflect on the following questions:

* If `songs.db` contains the top 100 songs of one listener from 2018, how would you characterize their audio aura? 
* Hypothesize about why the way you've calculated this aura might *not* be very representative of the listener. What better ways of calculating this aura would you propose?

Be sure to submit `answers.txt` along with each of your `.sql` files!

### Testing

Execute the below to evaluate the correctness of your code using `check50`.

```
check50 cs50/labs/2022/fall/songs
```

## How to Submit

1. Download each of your 8 `.sql` files (named `1.sql`, `2.sql`, ..., `8.sql`) and `answers.txt` by control-clicking or right-clicking on the files in your codespace's file browser and choosing **Download**.
1. Go to CS50's [Gradescope page](https://www.gradescope.com/courses/{{ gradescope_id }}).
1. Click "Lab 7: Songs".
1. Drag and drop your `.sql` files and `answers.txt` to the area that says "Drag & Drop". Be sure that each file is correctly named and that you submit all files in one bundle.
1. Click "Upload".

You should see a message that says "Lab 7: Songs submitted successfully!"

{% alert danger %}

Per Step 4 above, after you submit, be sure to check your autograder results. If you see `SUBMISSION ERROR: missing files (0.0/1.0)`, it means your file was either not named exactly as prescribed, you uploaded it to the wrong problem, or you did not include all files.

Correctness in submissions entails everything from reading the specification, writing code that is compliant with it, and submitting all files with the correct names. If you see this error, you should resubmit right away, making sure your submission is fully compliant with the specification. The staff will not adjust your filenames nor upload files for you after the fact!

{% endalert %}

{% spoiler "Want to see the staff's solution?" %}
```sql
-- 1.sql 
-- All songs in the database.
SELECT name
FROM songs;

-- 2.sql 
-- All songs in increasing order of tempo.
SELECT name
FROM songs
ORDER BY tempo;

-- 3.sql 
-- The names of the top 5 longest songs, in descending order of length.
SELECT name
FROM songs 
ORDER BY duration_ms
DESC LIMIT 5;

-- 4.sql
-- The names of any songs that have danceability, energy, and valence greater than 0.75.
SELECT name 
FROM songs 
WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;

-- 5.sql
-- The average energy of all the songs.
SELECT AVG(energy)
FROM songs

-- 6.sql
-- The names of songs that are by Post Malone.
-- Using nested SELECTs
SELECT name
FROM songs
WHERE artist_id =
(
    SELECT id
    FROM artists
    WHERE name = 'Post Malone'
);

-- Using JOIN
SELECT songs.name
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = 'Post Malone';

-- 7.sql
-- The average energy of songs that are by Drake
-- Using nested SELECTs
SELECT AVG(energy) 
FROM songs 
WHERE artist_id = 
(
    SELECT id 
    FROM artists 
    WHERE name = 'Drake'
);

-- Using JOIN
SELECT AVG(songs.energy)
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = 'Drake';

-- 8.sql
-- The names of songs that feature other artists.
SELECT name 
FROM songs 
WHERE name LIKE '%feat.%';
```
{% endspoiler %}

## Acknowledgements

Dataset from [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).