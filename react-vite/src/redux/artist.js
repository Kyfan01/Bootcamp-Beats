// action types
export const LOAD_ARTIST = 'artists/loadArtist'
export const UPDATE_ARTIST = 'artists/updateArtist'
export const DELETE_ARTIST = 'artists/deleteArtist'

// action creators

export const loadArtist = user => ({
    type: LOAD_ARTIST,
    user
})
export const updateArtist = artist => ({
    type: UPDATE_ARTIST,
    artist
})
export const deleteArtist = artistId => ({
    type: DELETE_ARTIST,
    artistId
})


export const thunkFetchArtist = userId => async dispatch => {
    const res = await fetch(`/api/users/${userId}`)
    if (res.ok) {
        const user = await res.json()
        dispatch(loadArtist(user))
        return user
    } else return 'fetch artist thunk error'
}

export const thunkFetchUpdateArtistInfo = (artistId, artistInfo) => async dispatch => {
    const res = await fetch(`api/users/${artistId}`, {
        method: 'PUT',
        body: artistInfo
    })

    if (res.ok) {
        const updatedArtist = await res.json()
        dispatch(updateArtist(updatedArtist))
        return updatedArtist
    } else return 'artist update thunk error'
}

export const thunkDeleteArtist = (artistId) => async dispatch => {
    const res = await fetch(`api/users/${artistId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })

    if (res.ok) {
        const deleteConfirm = await res.json()
        dispatch(deleteArtist(artistId))
        return deleteConfirm
    } else return 'artist delete thunk error'
}


const artistReducer = (state = {}, action) => {
    switch (action.type) {

        case LOAD_ARTIST: {
            const newArtistState = { ...state }
            newArtistState['selected'] = action.user
            return newArtistState
        }
        case UPDATE_ARTIST: {
            const newArtistState = { ...state }
            newArtistState[action.artist.id] = action.artist
            return newArtistState
        }
        default:
            return state
    }
}

export default artistReducer
