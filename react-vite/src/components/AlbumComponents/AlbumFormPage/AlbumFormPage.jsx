import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkCreateAlbum, thunkFetchAlbumById, thunkUpdateAlbum } from '../../../redux/album'
import "./AlbumForm.css";
import { useParams } from "react-router-dom";

import { Oval } from 'react-loader-spinner'


function AlbumFormPage() {
  const { albumId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [releaseDate, setReleaseDate] = useState("");
  const [genre, setGenre] = useState("");
  const [previewImage, setPreviewImage] = useState()

  const [hasSubmitted, setHasSubmitted] = useState(false)
  const [valErrors, setValErrors] = useState({});


  const [isLoading, setIsLoading] = useState(false)

  const currentUser = useSelector(state => state.session.user)

  useEffect(() => {
    if (!currentUser) navigate('/albums')
  }, [navigate, currentUser])

  useEffect(() => {
    function formatReleaseDate(date) {
      let months = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
      }
      let splitDate = date.split(' ')
      return `${splitDate[3]}-${months[splitDate[2]]}-${splitDate[1]}`
    }
    if (albumId) {
      dispatch(thunkFetchAlbumById(albumId)).then((oldAlbum) => {
        if (!(currentUser.id === oldAlbum.artistId)) navigate('/albums')
        setTitle(oldAlbum.title)
        setReleaseDate(formatReleaseDate(oldAlbum.releaseDate))
        setGenre(oldAlbum.genre)
      })
    }
  }, [albumId, dispatch, navigate, currentUser])

  useEffect(() => {
    if (!currentUser) navigate('/albums')
  })



  const handleSubmit = async (e) => {
    e.preventDefault();
    setHasSubmitted(true)


    const errObj = {}
    if (Date.parse(releaseDate) >= Date.parse(new Date())) errObj.releaseDate = "Release date cannot be in the future"
    if (title.length >= 50) errObj.title = "Title must be less than 50 characters"
    if (genre.length >= 50) errObj.genre = "Genre must be less than 50 characters"

    if (Object.values(errObj).length) {
      setValErrors(errObj)
    } else {
      setIsLoading(true)
      const formData = new FormData()
      formData.append('title', title)
      formData.append('releaseDate', releaseDate)
      formData.append('genre', genre)
      if (previewImage) {
        formData.append('albumCoverUrl', previewImage)
      }


      if (albumId) {

        await dispatch(thunkUpdateAlbum(albumId, formData)).then(() => navigate(`/albums/${albumId}`)).then(() => setIsLoading(false))
      } else {
        await dispatch(thunkCreateAlbum(formData)).then(newAlbum => navigate(`/albums/${newAlbum.id}`)).then(() => setIsLoading(false))
      }
    }
  };

  return (
    <div className="album-form-container">
      {isLoading &&
        <div className="loading-wheel-bg-div" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '84vh', width: '100%' }}>
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
        </div>}
      {!isLoading &&
        <>
          <h1>Album Form</h1>
          {Object.values(valErrors).length > 0 && hasSubmitted == true &&
            Object.values(valErrors).map((message) => <p key={message} className="validation-error">{message}</p>)}
          <form className="track-form" onSubmit={handleSubmit} encType="multipart/form-data">
            <div className="form-input title">
              <label className="track-form-input">
                Title
                <input
                  type="text"
                  placeholder="Title"
                  name="title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  required
                />
              </label>
            </div>

            <div className="form-input release-date">
              <label className="track-form-input">
                Release Date
                <input
                  type="date"
                  name="releaseDate"
                  value={releaseDate}
                  onChange={(e) => setReleaseDate(e.target.value)}
                  required
                />
              </label>
            </div>

            <div className="form-input genre">
              <label className="track-form-input">
                Genre
                <input
                  type="text"
                  placeholder="Genre"
                  name="genre"
                  value={genre}
                  onChange={(e) => setGenre(e.target.value)}
                  required
                />
              </label>

            </div>

            <div className="form-input">
              <label className="track-form-input-file">
                Preview Image
                <input
                  type="file"
                  name="previewImage"
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

export default AlbumFormPage;
