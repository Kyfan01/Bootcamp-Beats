import './AlbumCard.css'
import { NavLink } from 'react-router-dom'

export function AlbumCard({ album }) {

  return (
    <div title={album?.title} className='album-card-container'>
      <NavLink to={`/albums/${album.id}`} className='album-card-link'>
        <div>
          <div className='album-card-img-container'>
            <p>{album?.albumCoverUrl}</p>
          </div>
          <div>
            <p>Title: {album?.title}</p>
            <p>{album?.releaseDate.split(' ')[3]}</p>
            <p>{album?.genre}</p>
            <p>{album?.artistName}</p>
          </div>

        </div>
      </NavLink>
    </div>

  )
}
