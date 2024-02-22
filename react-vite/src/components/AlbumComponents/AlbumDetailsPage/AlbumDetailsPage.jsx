import { useEffect } from 'react'
import './AlbumDetailsPage.css'

import { useParams } from 'react-router-dom'
import { thunkFetchAlbumById } from '../../../redux/album'
import { useDispatch, useSelector } from 'react-redux'

export function AlbumDetailsPage() {
  const { albumId } = useParams()
  const dispatch = useDispatch()

  // const user = useSelector(state => state.session.user)
  const album = useSelector(state => state.albums[albumId])

  // const isOwner = (parseInt(user?.id) === album?.artistId)
  
  useEffect(() => {
    dispatch(thunkFetchAlbumById(albumId))
  }, [dispatch, albumId])

  return (
    <div>
      <p>Title: {album?.title}</p>
    </div>
  )
}

export default AlbumDetailsPage