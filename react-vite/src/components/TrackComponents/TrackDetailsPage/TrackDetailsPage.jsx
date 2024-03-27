import { useEffect } from 'react'
import './TrackDetailsPage.css'
import default_upload_image from '../../../../../images/default_upload_image.jpg'

import { useParams, useNavigate } from 'react-router-dom'
import { clearTracks, thunkDeleteTrack, thunkFetchTrackById, thunkToggleLikeTrack } from '../../../redux/track'
import { useDispatch, useSelector } from 'react-redux'
import { setIsPlayingTrack, thunkFetchPlayingTrack } from '../../../redux/playingTrack'

import { IoPlayCircle } from "react-icons/io5";
import { TbArrowsExchange2 } from "react-icons/tb";
import { MdDelete } from "react-icons/md";
import { IoIosHeart } from "react-icons/io";
import { IoIosHeartEmpty } from "react-icons/io";
import { IoPauseCircle } from "react-icons/io5";
import OpenModalIcon from '../../OpenModalIcon'
import { DeleteConfirmationModal } from '../../DeleteConfirmationModal'

export function TrackDetailsPage() {
  const { trackId } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const user = useSelector(state => state.session.user)
  const track = useSelector(state => state.tracks[trackId])
  const isLiked = useSelector(state => state.tracks[trackId]?.liked)
  const playingTrack = useSelector(state => state.playingTrack.selected)
  const isPlaying = useSelector(state => state.playingTrack.isPlaying);

  const isOwner = (parseInt(user?.id) === track?.artistId)

  useEffect(() => {
    dispatch(thunkFetchTrackById(trackId))
  }, [dispatch, trackId])

  const handleDelete = (e) => {
    e.preventDefault()
    dispatch(thunkDeleteTrack(trackId)).then(() => {
      dispatch(clearTracks())
      navigate('/tracks')
    })
  }

  const handleUpdate = (e) => {
    e.preventDefault()
    navigate(`/tracks/${trackId}/update`)
  }

  const handleTrackSelect = async (e) => {
    e.preventDefault()
    dispatch(thunkFetchPlayingTrack(track?.id))
  }

  const toggleLike = e => {
    e.preventDefault()
    dispatch(thunkToggleLikeTrack(trackId))
  }


  if (track && !(track.previewImageUrl)) track.previewImageUrl = default_upload_image


  return (
    <div id='track-details-body'>
      <div className='track-details-header-div'>
        <div className='track-details-header-image-div'>
          <img src={track?.previewImageUrl} alt="Track Preview Image" />
        </div>
        <div className='track-details-header-details-div'>
          <p className='track-details-track-word'>Track</p>
          <p className='track-details-track-title'>{track?.title}</p>
          <div className='track-details-artist-genre-div'>
            <p>{track?.artistName} • {track?.genre}</p>
          </div>
        </div>
      </div>
      <div className='play-update-delete-div'>
        {isPlaying && trackId == playingTrack.id ? <IoPauseCircle onClick={() => dispatch(setIsPlayingTrack(false))}  className='track-details-header-playicon' title='Select for player' /> : <IoPlayCircle className='track-details-header-playicon' onClick={handleTrackSelect} title='Select for player' />}
        {isLiked ? <IoIosHeart onClick={toggleLike} className='track-details-button' /> : <IoIosHeartEmpty onClick={toggleLike} className='track-details-button' />}
        {isOwner && <TbArrowsExchange2 className='track-details-button' onClick={handleUpdate} title='Update' />}
        {isOwner && <OpenModalIcon icon={<MdDelete className='track-details-button' />} modalComponent={<DeleteConfirmationModal deleteType={'track'} id={trackId} />} title='Delete'/>}
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
