import { useEffect } from 'react';
import './TracksIndex.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkFetchTracks } from '../../../redux/track';
import { TrackCard } from '../TrackCard/TrackCard';
// import { Footer } from '../../Footer/Footer';

export function TracksIndex() {
    const dispatch = useDispatch();
    let numTrack = 0;

    // const [playingTrack, setPlayingTrack] = useState()


    const tracksObj = useSelector(state => state.tracks)
    const tracks = Object.values(tracksObj)

    useEffect(() => {
        dispatch(thunkFetchTracks())
    }, [dispatch])

    return (
        <div className='track-index-container'>
            <h1>Tracks</h1>

            <div>
                <div className='track-index-cards-container'>
                    {tracks.map(track => <TrackCard numTrack={numTrack += 1} track={track} key={track?.id} />)}
                </div>
                {/* <Footer playingTrack={playingTrack}/> */}
            </div>
        </div>
    )
}

export default TracksIndex;
