import { useEffect } from 'react'
import './TrackDetailsPage.css'

import { useParams } from 'react-router-dom'
import { thunkFetchTrackById } from '../../../redux/track'
import { useDispatch, useSelector } from 'react-redux'

export function TrackDetailsPage() {
  const { trackId } = useParams()
  const dispatch = useDispatch()

  const user = useSelector(state => state.session.user)
  const track = useSelector(state => state.tracks[trackId])

  const isOwner = (parseInt(user?.id) === track?.artistId)
  
  useEffect(() => {
    dispatch(thunkFetchTrackById(trackId))
  }, [dispatch, trackId])

  return (
    <div>
      <p>{track?.title}</p>
      <p>{track?.albumId}</p>
      <p>{track?.artistId}</p>
      <p>{track?.artistName}</p>
      <p>{track?.duration}</p>
      <p>{track?.genre}</p>
      <p>{track?.trackNumber}</p>
      <p>{track?.trackLikes}</p>
      <p>{track?.liked}</p>
    </div>
  )
}

export default TrackDetailsPage