import { useEffect } from 'react'
import './TrackDetailsPage.css'

import { useParams, useNavigate } from 'react-router-dom'
import { thunkDeleteTrack, thunkFetchTrackById } from '../../../redux/track'
import { useDispatch, useSelector } from 'react-redux'

export function TrackDetailsPage() {
  const { trackId } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const user = useSelector(state => state.session.user)
  const track = useSelector(state => state.tracks[trackId])

  const isOwner = (parseInt(user?.id) === track?.artistId)

  useEffect(() => {
    dispatch(thunkFetchTrackById(trackId))
  }, [dispatch, trackId])

  const handleDelete = (e) => {
    e.preventDefault()
    dispatch(thunkDeleteTrack(trackId)).then(() => navigate('/tracks'))
  }

  const handleUpdate = (e) => {
    e.preventDefault()
    navigate(`/tracks/${trackId}/update`)
  }

  return (
    <div>
      <h1>{track?.title} Track Details</h1>
      <div>
        <img src={track?.previewImageUrl} alt="Track Preview Image" />
      </div>
      <h1>{track?.title}</h1>
      {/* <p>Album Id: {track?.albumId}</p>
      <p>Artist Id: {track?.artistId}</p> */}
      <p>Artist: {track?.artistName}</p>
      {/* <p>Duration: {track?.duration}</p> */}
      <p>Genre: {track?.genre}</p>
      <p>Track Number: {track?.trackNumber}</p>
      <p>Likes: {track?.trackLikes}</p>
      <p>Liked: {track?.liked ? 'true' : 'false'}</p>
      {/* <p>URL: {track?.url}</p>
      <p>Preview Image URL: {track?.previewImageUrl}</p> */}
      {isOwner && <button onClick={handleDelete}>Delete Track</button>}
      {isOwner && <button onClick={handleUpdate}>Update Track</button>}
    </div>
  )
}

export default TrackDetailsPage
