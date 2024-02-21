import './AlbumCard.css'
import { NavLink } from 'react-router-dom'

export function AlbumCard({album}) {

  return (
    <NavLink to={`/albums/${album.id}`} className='album-card-link'>
      <div title={album?.title} className='album-card-container'>
        <p>Title: {album?.title}</p>
      </div>

    </NavLink>
  )
}
