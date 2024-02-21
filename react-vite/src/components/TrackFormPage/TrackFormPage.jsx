import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import {thunkCreateTrack, thunkFetchTrackById, thunkUpdateTrack} from '../../redux/track'
import "./TrackForm.css";
import { Navigate, useParams } from "react-router-dom";

function TrackFormPage() {
  const { trackId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [albumId, setAlbumId] = useState();
  const [genre, setGenre] = useState("");
  const [trackNumber, setTrackNumber] = useState();
  const [trackFile, setTrackFile] = useState();
  const [previewImage, setPreviewImage] = useState()

  const [hasSubmitted, setHasSubmitted] = useState(false)
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

  useEffect(() => {
    if (trackId) {
      dispatch(thunkFetchTrackById(trackId)).then((oldTrack) => {
        setTitle(oldTrack.title)
        setAlbumId(oldTrack.albumId)
        setGenre(oldTrack.genre)
        setTrackNumber(oldTrack.trackNumber)
      })
    }
  }, [trackId, dispatch])


  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const formData = new FormData()
    formData.append('title', title)
    formData.append('albumId', albumId)
    formData.append('genre', genre)
    formData.append('trackNumber', trackNumber)
    formData.append('trackFile', trackFile)
    formData.append('previewImage', previewImage)
    formData.append('submit', true)

    if(trackId) {
      dispatch(thunkUpdateTrack(formData)).then(() => navigate(`/api/tracks/${trackId}`))
    } else{
      dispatch(thunkCreateTrack(formData)).then(newTrack => navigate(`/api/tracks/${newTrack.id}`))
    }


    // setTitle('')
    // setAlbumId()
    // setGenre()
    // setTrackFile()
    // setPreviewImage()
    // setHasSubmitted(false)
    // setErrors([])
  };

  return (
    <>
      <h1>Track Form</h1>
      {errors.length > 0 && hasSubmitted == true &&
        errors.map((message) => <p key={message}>{message}</p>)}
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <label>
          Title
          <input 
            type="text"
            name="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            />
        </label>
        <label>
          Album
          <select
            name="album"
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
            name="genre"
            value={genre}
            onChange={(e) => setGenre(e.target.value)}
            required
          />
        </label>
        <label>
          Track Number
          <input 
            type="number"
            name="track_number"
            value={trackNumber}
            onChange={(e) => setTrackNumber(e.target.value)}
            required
          />
        </label>
        <label>
          Track File
          <input 
            type="file"
            name="track_file"
            onChange={(e) => setTrackFile(e.target.files[0])}
            accept="audio/*"
          />
        </label>
        <label>
          Album Cover
          <input
            type="file"
            name="album_cover"
            onChange={(e) => setPreviewImage(e.target.files[0])}
            accept="image/*"
          />
        </label>


        <button type="submit">Submit</button>
      </form>
    </>
  );
}

export default TrackFormPage;
