// action types
export const LOAD_ARTIST = 'tracks/loadArtist'

// action creators

export const loadArtist = user => ({
    type: LOAD_ARTIST,
    user
})

export const thunkFetchArtist = userId => async dispatch => {
    const res = await fetch(`/api/users/${userId}`)
    if (res.ok) {
        const user = await res.json()
        dispatch(loadArtist(user))
        return user
    } else return 'fetch artist thunk error'
}

const artistReducer = (state = {}, action) => {
    switch (action.type) {

        case LOAD_ARTIST: {
            const newArtistState = { ...state }
            newArtistState['selected'] = action.user
            return newArtistState
        }
        default:
            return state
    }
}

export default artistReducer
