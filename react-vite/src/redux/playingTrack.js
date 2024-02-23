// action types
export const LOAD_PLAYING_TRACK = 'tracks/loadPlayingTrack'

// action creators

export const loadPlayingTrack = track => ({
  type: LOAD_PLAYING_TRACK,
  track
})

export const thunkFetchPlayingTrack = trackId => async dispatch => {
  const res = await fetch(`/api/tracks/${trackId}`)
  if (res.ok) {
    const track = await res.json()
    dispatch(loadPlayingTrack(track))
    return track
  } else return 'fetch playing track thunk error'
}

const playingTrackReducer = (state = {}, action) => {
  switch (action.type) {

    case LOAD_PLAYING_TRACK: {
      const newPlayingTrackState = { ...state }
      newPlayingTrackState['selected'] = action.track
      return newPlayingTrackState
    }
    default:
      return state
  }
}

export default playingTrackReducer