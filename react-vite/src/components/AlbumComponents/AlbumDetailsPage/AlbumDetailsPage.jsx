import { useEffect } from 'react'
import './AlbumDetailsPage.css'

import { useParams, useNavigate } from 'react-router-dom'
import { thunkFetchAlbumById, thunkDeleteAlbum } from '../../../redux/album'
import { useDispatch, useSelector } from 'react-redux'
import { thunkFetchAlbumTracks } from '../../../redux/track'
import { TrackCard } from '../../TrackComponents/TrackCard/TrackCard'

export function AlbumDetailsPage() {
  const { albumId } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const user = useSelector(state => state.session.user)
  const album = useSelector(state => state.albums[albumId])
  const albumTracks = useSelector(state => Object.values(state.tracks).filter(track => parseInt(albumId) === track.albumId))

  const isOwner = (user?.id === album?.artistId)

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
    navigate(`/tracks/${albumId}/update`)
  }

  return (
    <div>
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

      </div>
      <div>
        <p>{albumTracks.length > 0 ? albumTracks.map(track => <TrackCard track={track} key={track?.id} />) : null}</p>
      </div>
    </div>
  )
}

export default AlbumDetailsPage
