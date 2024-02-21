// action types
export const LOAD_TRACKS = 'tracks/loadTracks'
export const CREATE_TRACK = 'tracks/createTrack'
export const DELETE_TRACK = 'tracks/deleteTrack'

// action creators
export const loadTracks = tracks => ({
    type: LOAD_TRACKS,
    tracks
})

export const createTrack = track => ({
    type: CREATE_TRACK,
    track
})

export const deleteTrack = trackId => ({
    type: DELETE_TRACK,
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

export const thunkDeleteTrack = trackId => async dispatch => {
    const res = await fetch(`/api/tracks/${trackId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })

    if (res.ok) {
        const deleteComfirm = await res.json()
        dispatch(deleteTrack(trackId))
        return deleteComfirm
    } else return 'track delete thunk error'
}


const trackReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_TRACKS: {
            const newTrackState = { ...state }
            action.tracks.forEach(track => { newTrackState[track.id] = track })
            return newTrackState
        }

        case CREATE_TRACK: {
            const newTrackState = { ...state }
            newTrackState[action.track.id] = action.track
            return newTrackState
        }

        case DELETE_TRACK: {
            const newTrackState = { ...state }
            delete newTrackState[action.trackId]
            return newTrackState
        }

        default:
            return state
    }
}

export default trackReducer
