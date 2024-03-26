import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkCreateTrack, thunkFetchTrackById, thunkUpdateTrack } from '../../../redux/track'
import "./TrackForm.css";
import { useParams } from "react-router-dom";
import { thunkCreateAlbum, thunkFetchUserAlbums } from "../../../redux/album";

import { Oval } from 'react-loader-spinner'


function TrackFormPage() {
  const { trackId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [albumId, setAlbumId] = useState("");
  const [genre, setGenre] = useState("");
  const [trackNumber, setTrackNumber] = useState(1);
  const [trackFile, setTrackFile] = useState();
  const [previewImage, setPreviewImage] = useState()
  const [isUpdate, setIsUpdate] = useState(false)

  const [hasSubmitted, setHasSubmitted] = useState(false)
  const [valErrors, setValErrors] = useState({});

  const [albums, setAlbums] = useState([])

  const [isLoading, setIsLoading] = useState(false)

  const currentUser = useSelector(state => state.session['user'])
  useEffect(() => { //fetch the albums when the component mounts so that the dropdown has options
    if (currentUser) {
      dispatch(thunkFetchUserAlbums(currentUser.id)).then(userAlbums => {
        setAlbums(userAlbums.albums)
      })
    }
  }, [dispatch, currentUser])


  useEffect(() => {
    if (trackId) {
      setIsUpdate(true)
      dispatch(thunkFetchTrackById(trackId)).then((oldTrack) => {
        if (!(currentUser.id === oldTrack.artistId)) navigate('/tracks')
        setTitle(oldTrack.title)
        setAlbumId(oldTrack.albumId)
        setGenre(oldTrack.genre)
        setTrackNumber(oldTrack.trackNumber)
      })
    }
  }, [trackId, dispatch, navigate, currentUser])

  useEffect(() => {
    if (!currentUser) navigate('/tracks')
  }, [navigate, currentUser])


  const handleSubmit = async (e) => {
    e.preventDefault();
    setHasSubmitted(true)

    const errObj = {}
    if (title.length >= 50) errObj.title = "Title must be less than 50 characters"
    if (genre.length >= 50) errObj.genre = "Genre must be less than 50 characters"
    if (trackNumber >= 50) errObj.trackNumber = "Track Number must be less than 50"
    if (trackNumber < 1) errObj.trackNumber = "Track number must be a positive integer"
    if (!isUpdate && !trackFile) errObj.trackFile = "Need a file for track"

    if (Object.values(errObj).length) {

      setValErrors(errObj)
    } else {
      setIsLoading(true)
      let albumIdTemp = albumId;
      if (!albumId) {
        const albumFormData = new FormData()
        albumFormData.append('title', `${title} - Single`)
        albumFormData.append('releaseDate', new Date().toISOString().split('T')[0])
        albumFormData.append('genre', genre)
        if (previewImage) {
          albumFormData.append('albumCoverUrl', previewImage)
        }
        const responseAlbum = await dispatch(thunkCreateAlbum(albumFormData))
        setAlbumId(responseAlbum.id)
        albumIdTemp = responseAlbum.id
      }
      const formData = new FormData()
      formData.append('title', title)
      formData.append('albumId', albumIdTemp)
      formData.append('genre', genre)
      formData.append('trackNumber', trackNumber)
      formData.append('trackFile', trackFile)
      formData.append('previewImage', previewImage)

      if (trackId) {
        dispatch(thunkUpdateTrack(trackId, formData)).then(() => navigate(`/tracks/${trackId}`)).then(() => setIsLoading(false))
      } else {
        dispatch(thunkCreateTrack(formData)).then(newTrack => navigate(`/tracks/${newTrack.id}`)).then(() => setIsLoading(false))
      }
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
    <div className="track-form-container">
      {isLoading && 
        <div className="loading-wheel-bg-div" style={{display:'flex', justifyContent:'center', alignItems:'center', height: '84vh', width:'100%'}}>
        <div className="loading-wheel-div">
          <Oval
            visible={true}
            height="100%"
            width="100%"
            color="#4fa94d"
            ariaLabel="oval-loading"
            wrapperStyle={{}}
            wrapperClass=""
          />
          </div>
        </div> }
      {!isLoading && 
        <>
        <h1>Track Form</h1>
        {Object.values(valErrors).length > 0 && hasSubmitted == true &&
          Object.values(valErrors).map((message) => <p key={message} className="validation-error">{message}</p>)}
        <form className="track-form" onSubmit={handleSubmit} encType="multipart/form-data">
          <div className="form-input title">
            <label className="track-form-input">
              Title
              <input
                type="text"
                name="title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
              />
            </label>
          </div>

          <div className="form-input album">
            <label className="track-form-input-file">
              Album
              <select
                name="album"
                value={albumId}
                onChange={(e) => setAlbumId(e.target.value)}
              >
                <option value="">(Single)</option>
                {albums.map(album => (
                  <option key={album.id} value={album.id}>
                    {album.title}
                  </option>
                ))}
              </select>
            </label>
          </div>

          <div className="form-input genre">
            <label className="track-form-input">
              Genre
              <input
                type="text"
                name="genre"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
                required
              />
            </label>

          </div>

          <div className="form-input track-number">
            <label className="track-form-input">
              Track Number
              {/* {valErrors.trackNumber && hasSubmitted == true && <span className="validation-error">{valErrors.trackNumber}</span>} */}
              <input
                type="number"
                name="track_number"
                value={trackNumber}
                onChange={(e) => setTrackNumber(e.target.value)}
                required
              />
            </label>

          </div>

          <div className="form-input track-file">
            <label className="track-form-input-file">
              Track File
              {/* {valErrors.trackFile && hasSubmitted == true && <span className="validation-error">{valErrors.trackFile}</span>} */}
              <input
                type="file"
                name="track_file"
                onChange={(e) => setTrackFile(e.target.files[0])}
                accept="audio/*"
              />
            </label>

          </div>

          <div className="form-input album-cover">
            <label className="track-form-input-file">
              Album Cover
              <input
                type="file"
                name="album_cover"
                onChange={(e) => setPreviewImage(e.target.files[0])}
                accept="image/*"
              />
            </label>

          </div>


          <div className="submitButtonWithLoadingIcon">
            <button type="submit">Submit</button>

            {isLoading && <Oval
              visible={true}
              height="100%"
              width="100%"
              color="#4fa94d"
              ariaLabel="oval-loading"
              wrapperStyle={{}}
              wrapperClass=""
            />}
          </div>
        </form>
        </>
      
      }
    </div>
  );
}

export default TrackFormPage;
