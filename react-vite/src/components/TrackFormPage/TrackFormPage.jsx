import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
// import { useNavigate } from "react-router-dom";
import thunkCreateTrack from '../../redux/track'
import "./TrackForm.css";

function TrackFormPage() {
  // const navigate = useNavigate();
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [albumId, setAlbumId] = useState();
  const [genre, setGenre] = useState("");
  const [trackNumber, setTrackNumber] = useState();
  const [trackFile, setTrackFile] = useState();
  const [previewImage, setPreviewImage] = useState('')

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


  const handleSubmit = async (e) => {
    e.preventDefault();


    // setHasSubmitted(true)

    // let newTrack = {
    //   title,
    //   albumId,
    //   genre,
    //   trackFile,
    //   previewImage
    // }

    const formData = new FormData()
    formData.append('title', title)
    formData.append('albumId', albumId)
    formData.append('genre', genre)
    formData.append('trackNumber', trackNumber)
    formData.append('trackFile', trackFile)
    formData.append('previewImage', previewImage)
    formData.append('submit', true)
    // console.log(formData)
    await dispatch(thunkCreateTrack(formData))

    setTitle('')
    setAlbumId()
    setGenre()
    setTrackFile()
    setPreviewImage()
    setHasSubmitted(false)
    setErrors([])



    // .then((responseTrack) => navigate(`/api/tracks/${responseTrack.id}`))

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
          Track Number
          <input 
            type="number"
            value={trackNumber}
            onChange={(e) => setTrackNumber(e.target.value)}
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
            value={previewImage}
            onChange={(e) => setPreviewImage(e.target.value)}
            accept="image/*"
          />
        </label>


        <button type="submit">Submit</button>
      </form>
    </>
  );
}

export default TrackFormPage;
