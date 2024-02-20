import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { Navigate, useNavigate } from "react-router-dom";
// import "./LoginForm.css";

function TrackFormPage() {
  // const navigate = useNavigate();
  const dispatch = useDispatch();
  // const sessionUser = useSelector((state) => state.session.user);
  const [title, setTitle] = useState("");
  const [albumId, setAlbumId] = useState("");
  const [genre, setGenre] = useState("");
  const [trackFile, setTrackFile] = useState();
  const [previewImageUrl, setPreviewImageUrl] = useState('')

  const [errors, setErrors] = useState({});
  
  const [albums, setAlbums] = useState([])

  useEffect(() => { //fetch the albums when the component mounts so that the dropdown has options
    const fetchAlbums = async () => {
      const response = await fetch('/api/albums');
      const data = await response.json();
      setAlbums(data.albums)
    }
    fetchAlbums()
  }, [])


  const handleSubmit = async (e) => {
    e.preventDefault();

    let newTrack = {
      title,
      albumId,
      genre,
      trackFile,
      previewImageUrl
    }

    dispatch(thunkCreateTrack)

    setErrors([])
  };

  return (
    <>
      <h1>Track Form</h1>
      {errors.length > 0 &&
        errors.map((message) => <p key={message}>{message}</p>)}
      <form onSubmit={handleSubmit}>
        <label>
          Title
          <input 
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            />
        </label>
        <label>
          Album
          <select
            value={albumId}
            onChange={(e) => setAlbumId(e.target.value)}  
          >
            {albums.map(album => (
              <option key={album.id} value={album.id}>
                {album.title}
              </option>
            ))}
          </select>
        </label>
        <label>
          Genre
          <input 
            type="text"
            value={genre}
            onChange={(e) => setGenre(e.target.value)}
            required
          />
        </label>
        <label>
          Track File
          <input 
            type="file"
            value={trackFile}
            onChange={(e) => setTrackFile(e.target.value)}
            accept="audio/*"
          />
        </label>
        <label>
          Album Cover
          <input
            type="file"
            value={previewImageUrl}
            onChange={(e) => setPreviewImageUrl(e.target.value)}
            accept="image/*"
          />
        </label>


        <button type="submit">Submit</button>
      </form>
    </>
  );
}

export default TrackFormPage;
