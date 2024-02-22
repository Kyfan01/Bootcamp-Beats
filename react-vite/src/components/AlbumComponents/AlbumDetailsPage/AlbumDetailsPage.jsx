import { useEffect } from 'react'
import './AlbumDetailsPage.css'

import { useParams, useNavigate } from 'react-router-dom'
import { thunkFetchAlbumById, thunkDeleteAlbum } from '../../../redux/album'
import { useDispatch, useSelector } from 'react-redux'

export function AlbumDetailsPage() {
  const { albumId } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  // const user = useSelector(state => state.session.user)
  const album = useSelector(state => state.albums[albumId])

  // const isOwner = (parseInt(user?.id) === album?.artistId)

  useEffect(() => {
    dispatch(thunkFetchAlbumById(albumId))
  }, [dispatch, albumId])

  const handleDelete = (e) => {
    e.preventDefault()
    dispatch(thunkDeleteAlbum(albumId)).then(() => navigate('/albums'))
  }

  return (
    <div>
      <div className='album-details-img-container'>
        <p>{album?.albumCoverUrl}</p>
      </div>
      <p>Title: {album?.title}</p>
      <p>{album?.releaseDate.split(' ')[3]}</p>
      <p>{album?.genre}</p>
      <p>{album?.artistName}</p>
      <button onClick={handleDelete}>Delete Album</button>

    </div>
  )
}

export default AlbumDetailsPage
