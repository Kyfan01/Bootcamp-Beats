import './TrackCard.css'

export function TrackCard({track}) {

  return (
    <div title={track?.title}>
      <p>Title: {track?.title}</p>
      <p>AlbumId: {track?.albumId}</p>
      <p>Genre: {track?.genre}</p>
      <p>Track Number: {track?.trackNumber}</p>
      <p>URL: {track?.url}</p>
      <p>Preview Image URL: {track?.previewImageUrl}</p>
    </div>
  )
}