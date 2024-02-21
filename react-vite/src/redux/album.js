// action types
export const LOAD_ALBUMS = 'albums/loadAlbums'
export const CREATE_ALBUM = 'albums/createAlbum'
export const DELETE_ALBUM = 'albums/deleteAlbum'

// action creators
export const loadAlbums = albums => ({
    type: LOAD_ALBUMS,
    albums
})

export const createAlbum = album => ({
    type: CREATE_ALBUM,
    album
})

export const deleteAlbum = albumId => ({
    type: DELETE_ALBUM,
    albumId
})

// thunk action creators
export const thunkFetchAlbums = () => async dispatch => {
    const res = await fetch('/api/albums')

    if (res.ok) {
        const albums = await res.json()
        dispatch(loadAlbums(albums))
    } else return 'album get all thunks error'
}

export const thunkCreateAlbum = album => async dispatch => {
    const res = await fetch('/api/album', {
        method: 'POST',
        // headers: {
        //     'Content-Type': 'application/json'
        // },
        body: album
    })

    if (res.ok) {
        const newAlbum = await res.json()
        dispatch(createAlbum(newAlbum))
        return newAlbum
    } else return 'album create thunk error'
}

export const thunkDeleteAlbum = albumId => async dispatch => {
    const res = await fetch(`/api/tracks/${albumId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    })

    if (res.ok) {
        const deleteComfirm = await res.json()
        dispatch(deleteAlbum(albumId))
        return deleteComfirm
    } else return 'album delete thunk error'
}


const albumReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_ALBUMS: {
            const newAlbumState = { ...state }
            action.albums.forEach(album => { newAlbumState[album.id] = album })
            return newAlbumState
        }

        case CREATE_ALBUM: {
            const newAlbumState = { ...state }
            newAlbumState[action.album.id] = action.album
            return newAlbumState
        }

        case DELETE_ALBUM: {
            const newAlbumState = { ...state }
            delete newAlbumState[action.albumId]
            return newAlbumState
        }

        default:
            return state
    }
}

export default albumReducer
