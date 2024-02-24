import { useSelector } from 'react-redux'
import './Footer.css'
// import { useState } from 'react'

import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';

export function Footer() {


  const playingTrack = useSelector(state => state.playingTrack['selected'])

  // const [isPlaying, setIsPlaying] = useState(false)

  const src = playingTrack?.url

  // useEffect(() => {
  //   if (playingTrack) togglePlay()
  // })

  // const audio = new Audio(src)
  // function togglePlay() {
  //   if (audio.paused) {
  //     setIsPlaying(true)
  //     audio.play()
  //   } else {
  //     setIsPlaying(false)
  //     audio.pause()
  //   }
  // }

  return (
    <div className='track-player'>
      <AudioPlayer
<<<<<<< HEAD
        autoPlay
        src={src}
      // onPlay={e => console.log("onPlay")}
=======
      autoPlay
      src={src}
      onPlay={}
>>>>>>> 1fcab427ae8e0b42d6fb22bd107a4c4151a56c9d
      // other props here
      />
    </div>


    // <div className='track-player'>
    //   <div>
    //     <h2>{playingTrack ? playingTrack?.title : 'No track selected'}</h2>
    //     {playingTrack && <p>{playingTrack?.artistName}</p>}
    //   </div>
    //   <button onClick={togglePlay}>{isPlaying ? 'Pause' : 'Play'}</button>
    // </div>
  )
}
