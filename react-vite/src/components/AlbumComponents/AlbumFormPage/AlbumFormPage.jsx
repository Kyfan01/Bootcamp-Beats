import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import {thunkCreateAlbum, thunkFetchAlbumById, thunkUpdateAlbum} from '../../../redux/album'
import "./AlbumForm.css";
import { useParams } from "react-router-dom";

function AlbumFormPage() {
  const { albumId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  

  const [hasSubmitted] = useState(false)
  const [errors] = useState({});
  


  useEffect( () => {
    if (albumId) {
      dispatch(thunkFetchAlbumById(albumId)).then((oldAlbum) => {
        setTitle(oldAlbum.title)
      })
    }
  }, [albumId, dispatch])


  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const formData = new FormData()
    formData.append('title', title)

    if(albumId) {
      dispatch(thunkUpdateAlbum(albumId, formData)).then(() => navigate(`/albums/${albumId}`))
    } else{
      dispatch(thunkCreateAlbum(formData)).then(newAlbum => navigate(`/albums/${newAlbum.id}`))
    }

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
        


        <button type="submit">Submit</button>
      </form>
    </>
  );
}

export default AlbumFormPage;
