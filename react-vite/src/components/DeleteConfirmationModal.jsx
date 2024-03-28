import { useDispatch } from "react-redux"
import { useModal } from "../context/Modal";
import { useNavigate } from "react-router-dom";
import { thunkDeleteAlbum } from "../redux/album";
import { thunkDeleteTrack } from "../redux/track";
import { clearAlbums } from "../redux/album";
import { clearTracks } from "../redux/track";



export function DeleteConfirmationModal({ deleteType, id }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { closeModal } = useModal();


  function handleDelete() {
    if (deleteType == 'album') {
      dispatch(thunkDeleteAlbum(id)).then(() => dispatch(clearTracks())).then(() => dispatch(clearAlbums())).then(() => navigate(`/albums`)).then(() => closeModal())
    } else if (deleteType == 'track') {
      dispatch(thunkDeleteTrack(id)).then(() => dispatch(clearTracks())).then(() => navigate(`/tracks`)).then(() => closeModal())
    }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '20px' }}>
      <h1>Deleting {deleteType == 'track' ? 'Track' : 'Album'}</h1>
      <p style={{ marginBottom: 40 }}>Are you sure?</p>
      <div style={{ display: 'flex', columnGap: '12px' }}>
        <button className="modal-button" onClick={handleDelete}>Yes</button>
        <button className="modal-button" onClick={closeModal}>Cancel</button>
      </div>
    </div>
  )
}
