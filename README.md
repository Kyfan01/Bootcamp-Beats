# Bootcamp Beats

## Database Schema Design

[bootcamp-beats-schema]: images/Bootcamp-Beats.png

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
        "Tracks": [
            {
                "id": 1,
                "artist_id": 1,
                "album_id": 1,
                "title": "Dragon Night",
                "artist_name": "Sekai no Owari",
                "duration": 230,
                "album_name": "Tree",
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
        "Tracks": [
            {
                "id": 1,
                "artist_id": 1,
                "album_id": 1,
                "title": "Dragon Night",
                "artist_name": "Sekai no Owari",
                "duration": 230,
                "album_name": "Tree",
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
        "title": "Dragon Night",
        "artist_name": "Sekai no Owari",
        "duration": 230,
        "genre": "Pop",
        "url": "song url",
        "preview_image_url": "preview image url",
        "num_playlists": 3,
        "likes": 10000,
        "createdAt": "2021-11-19 20:39:36",
        "updatedAt": "2021-11-19 20:39:36",
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
      "preview_image_url": "preview image url"
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
        "createdAt": "2021-11-19 20:39:36",
        "updatedAt": "2021-11-19 20:39:36",
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
        "title": "Name must be 50 characters or less",
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
      "preview_image_url": "preview image url"
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
        "createdAt": "2021-11-19 20:39:36",
        "updatedAt": "2021-11-19 20:39:36",
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
        "title": "Name must be 50 characters or less",
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
  * URL: /api/tracks/:trackId
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
