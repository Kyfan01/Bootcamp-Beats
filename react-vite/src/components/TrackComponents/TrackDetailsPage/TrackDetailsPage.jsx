import { useEffect } from 'react'
import './TrackDetailsPage.css'

import { useParams, useNavigate } from 'react-router-dom'
import { thunkDeleteTrack, thunkFetchTrackById } from '../../../redux/track'
import { useDispatch, useSelector } from 'react-redux'
import { thunkFetchPlayingTrack } from '../../../redux/playingTrack'

import { IoPlayCircle } from "react-icons/io5";
import { TbArrowsExchange2 } from "react-icons/tb";
import { MdDelete } from "react-icons/md";

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

  const handleTrackSelect = async (e) => {
    e.preventDefault()
    dispatch(thunkFetchPlayingTrack(track?.id))
  }

  return (
    <div>
      <div className='track-details-header-div'>
        <div className='track-details-header-image-div'>
          <img src={track?.previewImageUrl} alt="Track Preview Image" />
        </div>
        <div className='track-details-header-details-div'>
          <p className='track-details-track-word'>Track</p>
          <p className='track-details-track-title'>{track?.title}</p>
          <div className='track-details-artist-genre-div'>
            <p className='track-details-track-artist'>{track?.artistName}  •</p>
            <p className='track-details-track-genre'>{track?.genre}</p>
          </div>
        </div>
      </div>
      <div className='play-update-delete-div'>
        <IoPlayCircle className='track-details-header-playicon' onClick={handleTrackSelect} />
        {isOwner && <TbArrowsExchange2 className='album-details-update' onClick={handleUpdate}/>}
        {isOwner && <MdDelete className='album-details-delete' onClick={handleDelete}/>}       
      </div>






      {/* <h1>{track?.title} Track Details</h1>
      <div>
        <img src={track?.previewImageUrl} alt="Track Preview Image" />
      </div>
      <h1>{track?.title}</h1>
      <button type="button" onClick={handleTrackSelect}>Play</button>
      <p>Artist: {track?.artistName}</p>
      <p>Genre: {track?.genre}</p>
      <p>Track Number: {track?.trackNumber}</p>
      <p>Likes: {track?.trackLikes}</p>
      <p>Liked: {track?.liked ? 'true' : 'false'}</p>
      {isOwner && <button onClick={handleDelete}>Delete Track</button>}
      {isOwner && <button onClick={handleUpdate}>Update Track</button>} */}
    </div>
  )
}

export default TrackDetailsPage
