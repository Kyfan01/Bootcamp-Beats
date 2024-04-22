// action types
export const LOAD_ARTIST = 'artists/loadArtist'
export const UPDATE_ARTIST = 'artists/updateArtist'

// action creators

export const loadArtist = user => ({
    type: LOAD_ARTIST,
    user
})
export const updateArtist = artist => ({
    type: UPDATE_ARTIST,
    artist
})


export const thunkFetchArtist = userId => async dispatch => {
    const res = await fetch(`/api/users/${userId}`)
    if (res.ok) {
        const user = await res.json()
        dispatch(loadArtist(user))
        return user
    } else return 'fetch artist thunk error'
}

export const thunkFetchUpdateArtist = (artistId, artist) => async dispatch => {
    const res = await fetch(`api/users/${artistId}`, {
        method: 'PUT',
        body: artist
    })

    if (res.ok) {
        const updatedArtist = await res.json()
        dispatch(updateArtist(updatedArtist))
        return updatedArtist
    } else return 'artist update thunk error'
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
