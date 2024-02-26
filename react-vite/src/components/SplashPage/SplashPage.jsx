import './SplashPage.css'
import { TrackCard } from '../TrackComponents/TrackCard/TrackCard'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { thunkFetchTrackById } from '../../redux/track'

import { FaGithubSquare } from "react-icons/fa";
import { SiLinkedin } from "react-icons/si";

export function SplashPage() {
    const dispatch = useDispatch()
    const track = useSelector(state => state.tracks[21])

    useEffect(() => {
        dispatch(thunkFetchTrackById(21))
    }, [dispatch])

    return (
        <div className='splash-page-container'>
            <div className='splash-welcome-div'>
                <h1>Welcome to Bootcamp Beats!</h1>
                <h3>A Spotify clone created using React/Redux and Flask</h3>
            </div>

            <div>
                <h1>Meet the Developers</h1>
                <div className='splash-dev-name-icon-div'>
                    <h2>Collin Ullmann</h2>
                    <a href="https://github.com/CollinUllmann"><FaGithubSquare className='splash-icon'/></a>
                    <a href="https://www.linkedin.com/in/collin-ullmann-984115119/"><SiLinkedin className='splash-icon'/></a>

                </div>
                <div className='splash-dev-name-icon-div'>
                    <h2>Kevin Fan</h2>
                    <a href="https://github.com/Kyfan01"><FaGithubSquare className='splash-icon'/></a>
                    <a href="https://www.linkedin.com/in/kevin-fan-20475a162/"><SiLinkedin className='splash-icon'/></a>

                </div>

                
            </div>


            <div>
                <p>Here is a sample track. Try playing it and controlling it with our music player! You can find more tracks
                    on our track page.
                </p>
            </div>

            <div>
                <TrackCard track={track} />
            </div>
        </div>
    )
}
