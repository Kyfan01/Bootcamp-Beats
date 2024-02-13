# Bootcamp Beats

## Database Schema Design

[bootcamp-beats-schema]: images/Bootcamp-Beats.png

## API Documentation

## USER AUTHENTICATION/AUTHORIZATION (WIP)

### All endpoints that require authentication (WIP)

## SONGS

### Get all Songs

Returns all the songs.

* Require Authentication: false
* Request
  * Method: GET
  * URL: /api/groups
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "Songs": [
            {
                "id": 1,
                "userId": 1,

            }
        ]
    }
    ```
