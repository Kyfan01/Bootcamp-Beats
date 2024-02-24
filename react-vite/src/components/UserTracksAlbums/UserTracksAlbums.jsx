import { useDispatch, useSelector } from 'react-redux'
import './UserTracksAlbums.css'

export function UserTracksAlbums() {
    const dispatch = useDispatch()

    const tracks = useSelector(state => Object.values(state.tracks))
    const albums = useSelector(state => Object.values(state.albums))
    const user = useSelector(state => state.session.user)

}
