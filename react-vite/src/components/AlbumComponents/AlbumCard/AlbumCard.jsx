import './AlbumCard.css'

export function AlbumCard({album}) {

  return (
    <div title={album?.title}>
      <p>Title: {album?.title}</p>
    </div>
  )
}