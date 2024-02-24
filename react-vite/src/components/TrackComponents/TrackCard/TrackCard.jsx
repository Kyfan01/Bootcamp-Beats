import './TrackCard.css'
import { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { thunkToggleLikeTrack } from '../../../redux/track'
import { useDispatch } from 'react-redux'
import { thunkFetchPlayingTrack } from '../../../redux/playingTrack'

import { IoPlay } from "react-icons/io5";
import { IoIosHeart } from "react-icons/io";
import { IoIosHeartEmpty } from "react-icons/io";



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
      <div className='id-image-title-artist-div'>
        <div className='track-id-div'>
          <p className='track-id'>{track?.id}</p>
          <div className='track-play-button'>
            <IoPlay className='track-hover-play-icon' onClick={handleTrackSelect} />
            {/* <button type="button" onClick={handleTrackSelect}>Play</button> */}
          </div>
        </div>
        <div className='preview-image-div'>
          <img className='preview-image' src={track?.previewImageUrl} alt="Track Preview Image" />
        </div>
        <div className='title-artist-div'>
          <NavLink to={`/tracks/${track?.id}`} className='track-card-link'>
            <p className='track-title'>{track?.title}</p>
          </NavLink>
          <NavLink to={`/users/${track?.artistId}`} className="track-card-link">
            <p className='track-artist'>{track?.artistName}</p>
          </NavLink>
        </div>
      </div>
      <div className='album-name-div'>
        <NavLink to={`/albums/${track?.albumId}`} className='track-card-link'>
          <p className='track-album'>{track?.albumTitle}</p>
        </NavLink>
      </div>
      <div className='likes-div'>
        {liked ? <IoIosHeart className='like-heart-icon' onClick={handleSubmit}/> : <IoIosHeartEmpty className='like-heart-icon' onClick={handleSubmit}/>}
        <p>{track?.trackLikes}</p>
      </div>

      {/* <div className='track-card-header-container'>
        <NavLink to={`/tracks/${track?.id}`} className='track-card-link'>
          <div className="track-card-image-container">
            <img className='preview-image' src={track?.previewImageUrl} alt="Track Preview Image" />
          </div>
          <h2>{track?.title}</h2>
        </NavLink>

        <NavLink to={`/users/${track?.artistId}`} className="track-card-link">
          <p>{track?.artistName}</p>
        </NavLink>
      </div>

      <NavLink to={`/albums/${track?.albumId}`} className='track-card-link'>
        <p>{track?.albumTitle}</p>
      </NavLink>
      <button type="button" onClick={handleTrackSelect}>Play</button> */}
      {/* <audio ref={trackRef} src={track?.url} />

      <div>
        <button onClick={handleSubmit}>{liked ? 'Unlike' : 'Like'}</button>
        <p>{track?.trackLikes}</p>
      </div> */}
    </div>
  )
}
