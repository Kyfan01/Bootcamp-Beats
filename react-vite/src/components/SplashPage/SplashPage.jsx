import './SplashPage.css'
import { TrackCard } from '../TrackComponents/TrackCard/TrackCard'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { thunkFetchTrackById } from '../../redux/track'

export function SplashPage() {
    const dispatch = useDispatch()
    const track = useSelector(state => state.tracks[14])

    useEffect(() => {
        dispatch(thunkFetchTrackById(14))
    }, [dispatch])

    return (
        <div className='splash-page-container'>
            <div>
                <h1>Welcome to Bootcamp Beats!</h1>
                <h3>A Spotify/Soundcloud clone created using React/Redux and Flask</h3>
            </div>

            <div>
                <h1>Meet the Developers</h1>

                <h2>Collin Ullmann</h2>
                <a href="https://github.com/CollinUllmann">Collin&apos;s Github</a>

                <h2>Kevin Fan</h2>
                <a href="https://github.com/Kyfan01">Kevin&apos;s Github</a>
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
