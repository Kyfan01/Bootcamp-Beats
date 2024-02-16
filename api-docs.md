# Bootcamp Beats

## Database Schema Design
![bootcamp-beats-schema]

[bootcamp-beats-schema]: ./images/Bootcamp-Beats.png

## API Documentation

## USER AUTHENTICATION/AUTHORIZATION (WIP)

### All endpoints that require authentication (WIP)

## TRACKS

### Get all Tracks

Returns all the tracks.

* Require Authentication: False
* Request
  * Method: GET
  * URL: /api/tracks
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "tracks": [
            {
                "id": 1,
                "artist_id": 1,
                "album_id": 1,
                "title": "Dragon Night",
                "artist_name": "Sekai no Owari",
                "duration": 230,
                "album_title": "Tree",
                "total_likes": 20000,
                "liked": true,
                "url": "song url",
                "preview_image_url": "preview image url"
            }
        ]
    }
    ```

### Get all Tracks uploaded by the Current User

Returns all the tracks uploaded by the current user

* Require Authentication: True
* Request
  * Method: GET
  * URL: /api/tracks/current
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "tracks": [
            {
                "id": 1,
                "artist_id": 1,
                "album_id": 1,
                "track_num": 1,
                "title": "Dragon Night",
                "artist_name": "Sekai no Owari",
                "duration": 230,
                "album_title": "Tree",
                "total_likes": 20000,
                "liked": true,
                "url": "song url",
                "preview_image_url": "preview image url"
            }
        ]
    }
    ```

### Get details of a Track by id

Returns the details of a track specified by its id.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/tracks/:track_id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "id": 1,
        "artist_id": 1,
        "album_id": 1,
        "track_num": 1,
        "title": "Dragon Night",
        "artist_name": "Sekai no Owari",
        "duration": 230,
        "genre": "Pop",
        "total_likes": 20000,
        "liked": true,
        "url": "song url",
        "preview_image_url": "preview image url",
        "num_playlists": 3
    }

    ```

### Create a track

Creates and returns a new track.

* Require Authentication: True
* Request
  * Method: POST
  * URL: /api/tracks/
  * Body:

   ```json
    {
      "title": "Sweet Child o' Mine",
      "genre": "Rock",
      "url": "song url",
      "preview_image_url": "preview image url",
      "album_id": 1
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "id": 1,
        "artist_id": 1,
        "title": "Sweet Child o' Mine",
        "artist_name": "Guns n' Roses",
        "duration": 356,
        "genre": "Rock",
        "url": "song url",
        "preview_image_url": "preview image url",
        "album_id": 1,
        "track_num": 1
    }

    ```

* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "title": "Title must be 50 characters or less",
        "genre": "Genre must be 20 characters or less",
        "url": "Url must be a valid url",
        "preview_image_url": "Preview Image Url must be a valid url"
      }
    }
    ```

### Edit a Track

Updates and returns an existing track.

* Require Authentication: True
* Require proper authorization: Track must belong to the current user
* Request
  * Method: PUT
  * URL: /api/tracks/:trackId
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "title": "Sweet Child o' Mine",
      "genre": "Rock",
      "url": "song url",
      "preview_image_url": "preview image url",
      "album_id": 1
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "id": 1,
        "artist_id": 1,
        "title": "Sweet Child o' Mine",
        "artist_name": "Guns n' Roses",
        "duration": 356,
        "genre": "Rock",
        "url": "song url",
        "preview_image_url": "preview image url",
        "album_id": 1,
        "track_num": 1
    }
    ```

* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "title": "Title must be 50 characters or less",
        "genre": "Genre must be 20 characters or less",
        "url": "Url must be a valid url",
        "preview_image_url": "Preview Image Url must be a valid url"
      }
    }
    ```
* Error response: Couldn't find a track with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Track couldn't be found"
    }
    ```

### Delete a Track

Deletes an existing track.

* Require Authentication: True
* Require proper authorization: Track must belong to the current user
* Request
  * Method: DELETE
  * URL: /api/tracks/:track_Id
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

* Error response: Couldn't find a Track with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Track couldn't be found"
    }
    ```

## ALBUMS

### Get all Albums

Returns all the albums.

* Require Authentication: False
* Request
  * Method: GET
  * URL: /api/albums
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "Albums": [
            {
                "id": 1,
                "artist_id": 1,
                "title": "Tree",
                "release_date": "2021-11-19",
                "genre": "Pop",
                "album_cover_url": "album cover url",
                "single": false
            }
        ]
    }
    ```

### Get all Albums uploaded by the Current User

Returns all the albums uploaded by the current user

* Require Authentication: True
* Request
  * Method: GET
  * URL: /api/albums/current
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "Albums": [
            {
                "id": 1,
                "artist_id": 1,
                "title": "Tree",
                "release_date": "2021-11-19",
                "genre": "Pop",
                "album_cover_url": "album cover url",
                "single": false
            }
        ]
    }
    ```

### Get details of an Album by id

Returns the details of an album specified by its id.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/albums/:albumId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "artist_id": 1,
      "title": "Tree",
      "release_date": "2021-11-19",
      "genre": "Pop",
      "album_cover_url": "album cover url",
      "single": false,
      "num_tracks": 6,
      "duration": 1500
    }

    ```

### Create an Album

Creates and returns a new album.

* Require Authentication: True
* Request
  * Method: POST
  * URL: /api/albums/
  * Body:

   ```json
    {
      "title": "Tree",
      "release_date": "2021-11-19",
      "genre": "Pop",
      "album_cover_url": "album cover url",
      "single": false
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "artist_id": 1,
      "title": "Tree",
      "release_date": "2021-11-19",
      "genre": "Pop",
      "album_cover_url": "album cover url",
      "single": false
    }

    ```

* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "title": "Title must be 50 characters or less",
        "genre": "Genre must be 20 characters or less",
        "preview_image_url": "Preview Image Url must be a valid url",
        "release_date": "Release Date cannot be in the future"
      }
    }
    ```

### Edit an Album

Updates and returns an existing album.

* Require Authentication: True
* Require proper authorization: Album must belong to the current user
* Request
  * Method: PUT
  * URL: /api/albums/:albumId
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "title": "Tree",
      "release_date": "2021-11-19",
      "genre": "Pop",
      "album_cover_url": "album cover url",
      "single": false,
      "tracks": [
        {
          "id": 1,
          "artist_id": 1,
          "album_id": 1,
          "album_title": "Tree",
          "title": "Dragon Night",
          "artist_name": "Sekai no Owari",
          "duration": 230,
          "url": "song url",
          "preview_image_url": "preview image url"
        }
      ]
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "artist_id": 1,
      "title": "Tree",
      "release_date": "2021-11-19",
      "genre": "Pop",
      "album_cover_url": "album cover url",
      "single": false,
      "tracks": [
        {
          "id": 1,
          "artist_id": 1,
          "album_id": 1,
          "album_title": "Tree",
          "title": "Dragon Night",
          "artist_name": "Sekai no Owari",
          "duration": 230,
          "url": "song url",
          "preview_image_url": "preview image url"
        }
      ]
    }
    ```

* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "title": "Title must be 50 characters or less",
        "genre": "Genre must be 20 characters or less",
        "preview_image_url": "Preview Image Url must be a valid url",
        "release_date": "Release Date cannot be in the future"
      }
    }
    ```
* Error response: Couldn't find an album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Album couldn't be found"
    }
    ```

### Delete an Album

Deletes an existing album.

* Require Authentication: True
* Require proper authorization: Album must belong to the current user
* Request
  * Method: DELETE
  * URL: /api/albums/:albumId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

* Error response: Couldn't find an Album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Album couldn't be found"
    }
    ```

### PLAYLISTS

### Get all Playlists created by the Current User

Returns all the playlists created by the current user

* Require Authentication: True
* Request
  * Method: GET
  * URL: /api/playlists/current
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "Playlists": [
            {
                "name": "Awesome Mix",
                "preview_image": "preview image url"
            }
        ]
    }
    ```

### Get details of a Playlist by id

Returns the details of a playlist specified by its id.

* Require Authentication: True
* Request
  * Method: GET
  * URL: /api/playlists/:playlistId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "name": "Awesome Mix",
      "preview_image": "preview image url",
      "tracks": [
        {
            "id": 1,
            "artist_id": 1,
            "album_id": 1,
            "album_title": "Tree",
            "title": "Dragon Night",
            "artist_name": "Sekai no Owari",
            "duration": 230,
            "url": "song url",
            "preview_image_url": "preview image url"
        }
      ],
      "createdAt": "2021-11-19 20:39:36",
      "updatedAt": "2021-11-19 20:39:36",
    }

    ```

### Create a playlist

Creates and returns a new playlist.

* Require Authentication: True
* Request
  * Method: POST
  * URL: /api/playlists/
  * Body:

   ```json
    {
      "name": "Awesome Mix"
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "name": "Awesome Mix",
      "preview_image": "preview image url"
    }

    ```

* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "name": "Name must be less than 50 characters"
      }
    }
    ```

### Edit a Playlist

Updates and returns an existing playlist.

* Require Authentication: True
* Require proper authorization: Playlist must belong to the current user
* Request
  * Method: PUT
  * URL: /api/playlists/:playlistId
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "name": "Awesome Mix",
      "preview_image": "preview image url",
      "tracks": [
        {
          "id": 1,
          "artist_id": 1,
          "album_id": 1,
          "album_title": "Tree",
          "title": "Dragon Night",
          "artist_name": "Sekai no Owari",
          "duration": 230,
          "url": "song url",
          "preview_image_url": "preview image url"
        }
      ]
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "name": "Awesome Mix",
      "tracks": [
        {
          "id": 1,
          "artist_id": 1,
          "album_id": 1,
          "album_title": "Tree",
          "title": "Dragon Night",
          "artist_name": "Sekai no Owari",
          "duration": 230,
          "url": "song url",
          "preview_image_url": "preview image url"
        }
      ]
    }
    ```

* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "name": "Name is required"
      }
    }
    ```
* Error response: Couldn't find a playlist with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Playlist couldn't be found"
    }
    ```

### Delete a Playlist

Deletes an existing playlist.

* Require Authentication: True
* Require proper authorization: Playlist must belong to the current user
* Request
  * Method: DELETE
  * URL: /api/playlists/:playlistId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

* Error response: Couldn't find a Playlist with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Pllaylist couldn't be found"
    }
    ```

### LIKES

## Get likes by track id

Returns the number of likes by track id

* Require Authentication: False
* Request
  * Method: GET
  * URL: /api/tracks/:trackId/likes
  * Body:
    ```json
    {
      "track_id": 1
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

  ```json
  {
    "track_id": 1,
    "likes": 5
  }
  ```

## Like a Track

Likes a track by its id

* Require Authentication: True
* Request
  * Method: POST
  * URL: /api/tracks/:trackId/like
  * Body:
    ```json
    {
      "user_id": 1,
      "track_id": 1
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

  ```json
  {
    "message": "Successfully liked!"
  }
  ```

## Unlike a Track

Unlikes a track by its id

* Require Authentication: True
* Request
  * Method: DELETE
  * URL: /api/tracks/:trackId/unlike
  * Body:
    ```json
    {
      "user_id": 1,
      "track_id": 1
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

  ```json
  {
    "message": "Successfully deleted!"
  }
  ```
