import './AlbumCard.css'
import { NavLink } from 'react-router-dom'
import default_upload_image from '../../../../../images/default_upload_image.jpg'

export function AlbumCard({ album }) {


  if (album && !(album.albumCoverUrl)) album.albumCoverUrl = default_upload_image
  return (
    <div title={album?.title} className='album-card-container'>
      <NavLink to={`/albums/${album.id}`} className='album-card-link'>
        <div>
          <div className='album-card-img-container'>
            <img className='album-card-image' src={album?.albumCoverUrl} alt="Album Preview Image" />
          </div>
          <div>
            <span className='album-card-title'>{album?.title}</span>
            <NavLink to={`/users/${album.artistId}`} className="album-card-artist-navlink">
              <p className='album-card-artist'>{album?.artistName}</p>
            </NavLink>
          </div>

        </div>
      </NavLink >
    </div >

  )
}
