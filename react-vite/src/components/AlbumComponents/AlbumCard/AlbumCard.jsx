import './AlbumCard.css'
import { NavLink } from 'react-router-dom'

export function AlbumCard({ album }) {

  return (
    <div title={album?.title} className='album-card-container'>
      <NavLink to={`/albums/${album.id}`} className='album-card-link'>
        <div>
          <div className='album-card-img-container'>
            <img className='album-card-image' src={album?.albumCoverUrl} alt="Album Preview Image" />
          </div>
          <div>
            <p className='album-card-title'>{album?.title.length < 13 ? album?.title : album?.title.substring(0, 13) + '...'}</p>
            <p className='album-card-artist'>{album?.artistName}</p>
          </div>

        </div>
      </NavLink>
    </div>

  )
}
