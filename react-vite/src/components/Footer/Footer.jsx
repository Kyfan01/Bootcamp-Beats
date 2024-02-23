import { useSelector } from 'react-redux'
import './Footer.css'

export function Footer() {


  const playingTrack = useSelector(state => state.playingTrack['selected'])

  const src = playingTrack?.url
  const audio = new Audio(src)
  function togglePlay() {
    if (audio.paused) {
      audio.play()
    } else {
      audio.pause()
    }
  }

  return (
    <div className='track-player'>
      <p>{playingTrack ? playingTrack?.title : 'No track selected'}</p>
      <button onClick={togglePlay}>Toggle Play</button>
    </div>
  )
}
