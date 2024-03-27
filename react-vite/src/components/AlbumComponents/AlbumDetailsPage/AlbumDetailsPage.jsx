import { useEffect } from 'react'
import './AlbumDetailsPage.css'
import default_upload_image from '../../../../../images/default_upload_image.jpg'

import { useParams, useNavigate, NavLink } from 'react-router-dom'
import { thunkFetchAlbumById, thunkDeleteAlbum, clearAlbums } from '../../../redux/album'
import { useDispatch, useSelector } from 'react-redux'
import { clearTracks, thunkFetchAlbumTracks } from '../../../redux/track'
import { TrackCard } from '../../TrackComponents/TrackCard/TrackCard'

import { IoPlayCircle } from "react-icons/io5";
import { IoPauseCircle } from "react-icons/io5";
import { TbArrowsExchange2 } from "react-icons/tb";
import { MdDelete } from "react-icons/md";


import { setIsPlayingTrack, thunkFetchPlayingTrack } from '../../../redux/playingTrack'
import OpenModalIcon from '../../OpenModalIcon'
import { DeleteConfirmationModal } from '../../DeleteConfirmationModal'

export function AlbumDetailsPage() {
  const { albumId } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const user = useSelector(state => state.session.user)
  const album = useSelector(state => state.albums[albumId])
  const albumTracks = useSelector(state => Object.values(state.tracks).filter(track => parseInt(albumId) === track.albumId))
  const sortedAlbumTracks = albumTracks.sort((a, b) => a.trackNumber - b.trackNumber)
  const playingTrack = useSelector(state => state.playingTrack.selected)
  const isPlaying = useSelector(state => state.playingTrack.isPlaying);

  const isOwner = (user?.id === album?.artistId)
  let numTrack = 0;

  useEffect(() => {
    dispatch(thunkFetchAlbumById(albumId))
    dispatch(thunkFetchAlbumTracks(albumId))
  }, [dispatch, albumId])

  const handleDelete = (e) => {
    e.preventDefault()
    dispatch(thunkDeleteAlbum(albumId)).then(() => {
      dispatch(clearAlbums())
      dispatch(clearTracks())
      navigate('/albums')
    })
  }

  const handleUpdate = (e) => {
    e.preventDefault()
    navigate(`/albums/${albumId}/update`)
  }

  const handleTrackSelect = async (e) => {
    e.preventDefault()
    dispatch(thunkFetchPlayingTrack(sortedAlbumTracks[0]?.id))
  }

  if (album && !(album.albumCoverUrl)) album.albumCoverUrl = default_upload_image

  if (!album) return

  return (
    <div id='album-details-body'>
      <div className='album-details-header-div'>
        <div className='album-details-header-image-div'>
          <img src={album?.albumCoverUrl} alt="Album Preview Image" />
        </div>
        <div className='album-details-header-details-div'>
          <p className='album-details-album-word'>Album</p>
          <p className='album-details-album-name'>{album?.title}</p>
          <div className='album-details-artist-year-length-div'>
            <p className='album-details-artist-year-length'><NavLink className="album-details-artist-navlink" to={`/users/${album.artistId}`}>{album?.artistName}</NavLink> • {album?.releaseDate.split(' ')[3]} • {sortedAlbumTracks.length} songs</p>
          </div>
        </div>
      </div>
      <div className='play-update-delete-div'>
        {isPlaying && playingTrack.albumId == albumId ? <IoPauseCircle onClick={() => dispatch(setIsPlayingTrack(false))}  className='album-details-header-playicon' title='Select for player' /> : <IoPlayCircle className='album-details-header-playicon' onClick={handleTrackSelect} title='Select for player' />}
        {/* <IoPlayCircle className='album-details-header-playicon' onClick={handleTrackSelect} title='Select first track' /> */}
        {isOwner && <TbArrowsExchange2 className='album-details-update' onClick={handleUpdate} title='Update' />}
        {isOwner && <OpenModalIcon icon={<MdDelete className='album-details-delete' />} modalComponent={<DeleteConfirmationModal deleteType={'album'} id={albumId} />} title='Delete'/>}
      </div>




      {/* {console.log('albumTracks', albumTracks)}
      {console.log('sortedAlbumTracks', sortedAlbumTracks)}
      <h1>{album?.title} Album Details</h1>
      <div className='album-details-img-container'>
        <img src={album?.albumCoverUrl} alt="Album Preview Image" />
      </div>
      <div>
        <h1>{album?.title}</h1>
        <p>{album?.releaseDate.split(' ')[3]}</p>
        <p>{album?.genre}</p>
        <p>{album?.artistName}</p>
        {isOwner && <button onClick={handleDelete}>Delete Album</button>}
        {isOwner && <button onClick={handleUpdate}>Update Album</button>}

      </div> */}
      <div>
        <p>{sortedAlbumTracks.length > 0 ? sortedAlbumTracks.map(track => <TrackCard numTrack={numTrack += 1} track={track} key={track?.id} />) : null}</p>
      </div>
    </div>
  )
}

export default AlbumDetailsPage
