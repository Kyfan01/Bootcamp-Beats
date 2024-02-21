import './TrackCard.css'
import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import { thunkToggleLikeTrack } from '../../../redux/track'
import { useDispatch } from 'react-redux'

export function TrackCard({ track }) {
  const dispatch = useDispatch()

  const [liked, setLiked] = useState(false)

  return (
      <div title={track?.title} className='track-card-container'>

      <NavLink to={`/tracks/${track.id}`} className='track-card-link'>
        <div>
          <p>Preview Image URL: {track?.previewImageUrl}</p>
          <p>Title: {track?.title}</p>
          <p>Artist Name: {track?.artistName}</p>
        </div>
      </NavLink>
        <p>Album Title: {track?.albumTitle}</p>
        <p>Genre: {track?.genre}</p>
        <p>Track Number: {track?.trackNumber}</p>
        <p>URL: {track?.url}</p>
        <p>Liked: {track?.liked ? 'True' : 'False'}</p>
        <button onClick={() => {
          console.log('button pressed')
          console.log(track?.liked ? 'True' : 'False')
          dispatch(thunkToggleLikeTrack(track?.id))}}>{liked ? 'Unlike' : 'Like'}</button>
      </div>
  )
}
