// action types
export const LOAD_TRACKS = 'tracks/loadTracks'
export const LOAD_TRACK_BY_ID = 'tracks/loadTrackById'
export const CREATE_TRACK = 'tracks/createTrack'
export const DELETE_TRACK = 'tracks/deleteTrack'
export const UPDATE_TRACK = 'tracks/updateTrack'
export const TOGGLE_LIKE_TRACK = 'tracks/toggleLikeTrack'

// action creators
export const loadTracks = tracks => ({
    type: LOAD_TRACKS,
    payload: tracks
})

export const loadTrackById = track => ({
    type: LOAD_TRACK_BY_ID,
    track
})

export const createTrack = track => ({
    type: CREATE_TRACK,
    track
})

export const updateTrack = track => ({
    type: UPDATE_TRACK,
    track
})

export const deleteTrack = trackId => ({
    type: DELETE_TRACK,
    trackId
})

export const toggleLikeTrack = trackId => ({
    type: TOGGLE_LIKE_TRACK,
    trackId
})


// thunk action creators
export const thunkFetchTracks = () => async dispatch => {
    const res = await fetch('/api/tracks')

    if (res.ok) {
        const tracks = await res.json()
        dispatch(loadTracks(tracks))
    } else return 'track get all thunks error'
}

export const thunkFetchTrackById = trackId => async dispatch => {
    const res = await fetch(`/api/tracks/${trackId}`)
    if (res.ok) {
        const track = await res.json()
        dispatch(loadTrackById(track))
        return track
    } else return 'fetch track by id thunk error'
}

export const thunkCreateTrack = track => async dispatch => {
    const res = await fetch('/api/tracks', {
        method: 'POST',
        // headers: {
        //     'Content-Type': 'application/json'
        // },
        body: track
    })

    if (res.ok) {
        const newTrack = await res.json()
        dispatch(createTrack(newTrack))
        return newTrack
    } else return 'track create thunk error'
}

export const thunkUpdateTrack = (trackId, track) => async dispatch => {
    const res = await fetch(`/api/tracks/${trackId}`, {
        method: 'PUT',
        body: track
    })

    if (res.ok) {
        const updatedTrack = await res.json()
        dispatch(updateTrack(updatedTrack))
        return updatedTrack
    } else return 'track update thunk error'
}

export const thunkDeleteTrack = trackId => async dispatch => {
    const res = await fetch(`/api/tracks/${trackId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })

    if (res.ok) {
        const deleteConfirm = await res.json()
        dispatch(deleteTrack(trackId))
        return deleteConfirm
    } else return 'track delete thunk error'
}

export const thunkToggleLikeTrack = trackId => async dispatch => {
    const res = await fetch(`/api/tracks/${trackId}/like`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    console.log('thunk response: ', res)
    if (res.ok) {
        const updatedTrack = await res.json()
        dispatch(toggleLikeTrack(trackId))
        return updatedTrack
    } else return 'track like thunk error'
}



const trackReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_TRACKS: {
            const newTrackState = { ...state }
            action.payload.tracks.forEach(track => { newTrackState[track.id] = track })
            return newTrackState
        }
        case LOAD_TRACK_BY_ID: {
            const newTrackState = { ...state }
            newTrackState[action.track.id] = action.track
            return newTrackState
        }

        case CREATE_TRACK: {
            const newTrackState = { ...state }
            newTrackState[action.track.id] = action.track
            return newTrackState
        }

        case UPDATE_TRACK: {
            const newTrackState = { ...state }
            newTrackState[action.track.id] = action.track
            return newTrackState
        }

        case DELETE_TRACK: {
            const newTrackState = { ...state }
            delete newTrackState[action.trackId]
            return newTrackState
        }

        case TOGGLE_LIKE_TRACK: {
            const newTrackState = { ...state }
            newTrackState[action.trackId] = action.track
            return newTrackState
        }


        default:
            return state
    }
}

export default trackReducer
