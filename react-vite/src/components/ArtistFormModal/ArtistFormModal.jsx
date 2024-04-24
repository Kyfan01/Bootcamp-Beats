import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import "./ArtistFormModal.css";
import { thunkFetchUpdateArtistInfo, thunkFetchArtist } from "../../redux/artist";

function ArtistFormModal(artistId) {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [artistName, setArtistName] = useState("")
  const [fullName, setFullName] = useState("")
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const currentUser = useSelector(state => state.session['user'])

  useEffect(() => {
    setUsername(currentUser.username)
    setArtistName(currentUser.artistName)
    setEmail(currentUser.email)
    setFullName(currentUser.name)
  }, [currentUser])

  useEffect(() => {
    dispatch(thunkFetchArtist(artistId))
  }, [dispatch, artistId])

  const handleSubmit = async (e) => {
    e.preventDefault();


    

    const serverResponse = await dispatch(
      thunkFetchUpdateArtistInfo(currentUser.id, {
        email,
        username,
        name: fullName,
        artist_name: artistName
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
      window.location.reload(false);
    }
  };

  return (
    <>
      <div className="signup-header-div">
        <h1>Update Profile</h1>
      </div>
      {errors.server && <p className="modal-error">{errors.server}</p>}
      {errors.email && <p className="modal-error">{errors.email}</p>}
      <form className="signup-form" onSubmit={handleSubmit}>
        <label className="signup-form-input">
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>

        <label className="signup-form-input">
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>

        <label className="signup-form-input">
          Artist Name
          <input
            type="text"
            value={artistName}
            onChange={(e) => setArtistName(e.target.value)}
            required
          />
        </label>

        <label className="signup-form-input">
          Name
          <input
            type="text"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            required
          />
        </label>

        {errors.username && <p>{errors.username}</p>}
        

        
        <div className="signup-form-submit-button-div">

          <button type="submit" className="modal-button">Confirm</button>
        </div>
      </form>
    </>
  );
}

export default ArtistFormModal;
