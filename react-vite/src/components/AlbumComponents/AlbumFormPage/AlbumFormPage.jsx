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

  const [hasSubmitted] = useState(false)
  const [errors] = useState({});

  const [isLoading, setIsLoading] = useState(false)

  const currentUser = useSelector(state => state.session.user)


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

    console.log('releaseDate: ', releaseDate)

    const formData = new FormData()
    formData.append('title', title)
    formData.append('releaseDate', releaseDate)
    formData.append('genre', genre)
    if (previewImage) {
      formData.append('albumCoverUrl', previewImage)
    }


    if (albumId) {
      setIsLoading(true)
      await dispatch(thunkUpdateAlbum(albumId, formData)).then(() => navigate(`/albums/${albumId}`)).then(() => setIsLoading(false))
    } else {
      await dispatch(thunkCreateAlbum(formData)).then(newAlbum => navigate(`/albums/${newAlbum.id}`)).then(() => setIsLoading(false))
    }


  };

  return (
    <div className="album-form-container">
      <h1>Album Form</h1>
      {errors.length > 0 && hasSubmitted == true &&
        errors.map((message) => <p key={message}>{message}</p>)}
      <form onSubmit={handleSubmit} encType="multipart/form-data">

        <div>

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
        </div>

        <div>
          <label>
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

        <div>
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

        </div>

        <div>
          <label>
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
    </div>
  );
}

export default AlbumFormPage;
