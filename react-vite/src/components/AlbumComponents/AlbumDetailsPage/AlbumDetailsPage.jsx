import { useEffect } from 'react'
import './AlbumDetailsPage.css'

import { useParams, useNavigate } from 'react-router-dom'
import { thunkFetchAlbumById, thunkDeleteAlbum } from '../../../redux/album'
import { useDispatch, useSelector } from 'react-redux'
import { thunkFetchAlbumTracks } from '../../../redux/track'
import { TrackCard } from '../../TrackComponents/TrackCard/TrackCard'

import { IoPlayCircle } from "react-icons/io5";
import { TbArrowsExchange2 } from "react-icons/tb";
import { MdDelete } from "react-icons/md";

import { thunkFetchPlayingTrack } from '../../../redux/playingTrack'

export function AlbumDetailsPage() {
  const { albumId } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const user = useSelector(state => state.session.user)
  const album = useSelector(state => state.albums[albumId])
  const albumTracks = useSelector(state => Object.values(state.tracks).filter(track => parseInt(albumId) === track.albumId))
  const sortedAlbumTracks = albumTracks.sort((a, b) => a.trackNumber - b.trackNumber)

  const isOwner = (user?.id === album?.artistId)
  let numTrack = 0;

  useEffect(() => {
    dispatch(thunkFetchAlbumById(albumId))
    dispatch(thunkFetchAlbumTracks(albumId))
  }, [dispatch, albumId])

  const handleDelete = (e) => {
    e.preventDefault()
    dispatch(thunkDeleteAlbum(albumId)).then(() => navigate('/albums'))
  }

  const handleUpdate = (e) => {
    e.preventDefault()
    navigate(`/albums/${albumId}/update`)
  }

  const handleTrackSelect = async (e) => {
    e.preventDefault()
    dispatch(thunkFetchPlayingTrack(sortedAlbumTracks[0]?.id))
  }

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
            <p className='album-details-artist'>{album?.artistName} •</p>
            <p>{album?.releaseDate.split(' ')[3]} •</p>
            <p>{sortedAlbumTracks.length} songs</p>
          </div>
        </div>
      </div>
      <div className='play-update-delete-div'>
        <IoPlayCircle className='album-details-header-playicon' onClick={handleTrackSelect} title='Select first track' />
        {isOwner && <TbArrowsExchange2 className='album-details-update' onClick={handleUpdate} title='Update' />}
        {isOwner && <MdDelete className='album-details-delete' onClick={handleDelete} title='Delete' />}
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
