import './Footer.css'

export function Footer({playingTrack}) {

  const src = playingTrack?.url
  const audio = new Audio(src)
  function togglePlay() {
    if (audio.paused){
      audio.play()
    } else {
      audio.pause()
    }
  }

  return (
    <div>
      <button onClick={togglePlay}>Toggle Play</button>
    </div>
  )
}