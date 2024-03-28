// action types
export const LOAD_PLAYING_TRACK = 'tracks/loadPlayingTrack'
export const SET_IS_PLAYING_TRACK = 'tracks/setIsPlayingTrack'

// action creators

export const loadPlayingTrack = track => ({
  type: LOAD_PLAYING_TRACK,
  track
})

export const setIsPlayingTrack = isPlaying => ({
  type: SET_IS_PLAYING_TRACK,
  isPlaying
})

export const thunkFetchPlayingTrack = trackId => async (dispatch, getState) => {
  const currentTrack = getState().playingTrack.selected;

  if (trackId === currentTrack?.id) {
    dispatch(setIsPlayingTrack(true))
    return currentTrack;
  }

  const res = await fetch(`/api/tracks/${trackId}`)
  if (res.ok) {
    const track = await res.json()
    dispatch(loadPlayingTrack(track))
    dispatch(setIsPlayingTrack(true))
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

    case SET_IS_PLAYING_TRACK: {
      const newPlayingTrackState = { ...state }
      newPlayingTrackState['isPlaying'] = action.isPlaying
      return newPlayingTrackState
    }

    default:
      return state
  }
}

export default playingTrackReducer