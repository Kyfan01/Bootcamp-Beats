import './TrackCard.css'
import { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { thunkToggleLikeTrack } from '../../../redux/track'
import { useDispatch } from 'react-redux'
import { thunkFetchPlayingTrack } from '../../../redux/playingTrack'

export function TrackCard({ track }) {
  const dispatch = useDispatch()

  const [liked, setLiked] = useState('')

  // audio player stuff
  // const [play] = useState(false)
  // const trackRef = useRef < HTMLAudioElement > (null)
  //   // const MAX = 20

  // function toggleAudio() {
  //   if (play) {
  //     trackRef.current?.pause()
  //     setPlay(false)
  //   } else {
  //     trackRef.current?.play()
  //     setPlay(true)
  //   }
  // }

  useEffect(() => {
    setLiked(track?.liked)
  }, [track])

  const handleSubmit = async (e) => {
    e.preventDefault()

    dispatch(thunkToggleLikeTrack(track?.id))
  }

  const handleTrackSelect = async (e) => {
    e.preventDefault()
    dispatch(thunkFetchPlayingTrack(track?.id))
  }

  return (
    <div title={track?.title} className='track-card-container'>

      <div className='track-card-header-container'>
        <NavLink to={`/tracks/${track?.id}`} className='track-card-link'>
          <div className="track-card-image-container">
            <img src={track?.previewImageUrl} alt="Track Preview Image" />
          </div>
          <h2>{track?.title}</h2>
        </NavLink>

        <NavLink to={`/users/${track?.artistId}`}>
          <p>{track?.artistName}</p>
        </NavLink>
      </div>

      <NavLink to={`/albums/${track?.albumId}`} className='track-card-link'>
        <p>{track?.albumTitle}</p>
      </NavLink>
      <button type="button" onClick={handleTrackSelect}>Select</button>
      {/* <audio ref={trackRef} src={track?.url} /> */}

      <div>
        <button onClick={handleSubmit}>{liked ? 'Unlike' : 'Like'}</button>
        <p>{track?.trackLikes}</p>
      </div>
    </div>
  )
}
