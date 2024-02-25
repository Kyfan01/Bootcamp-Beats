import { NavLink, useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useSelector } from "react-redux";
import { useEffect } from "react";

import { PiMusicNotesPlusFill } from "react-icons/pi";
import { PiMusicNotesFill } from "react-icons/pi";
import { MdLibraryMusic } from "react-icons/md";
import { MdLibraryAdd } from "react-icons/md";


function Navigation() {
  const navigate = useNavigate()
  const user = useSelector(state => state.session.user)
  return (
    <div className="navbar">
      <NavLink to='/' className='nav-logo'>
        <p>logo here</p>
      </NavLink>
      <div className="nav-buttons">
        <div className="nav-button-icons-div">
          <PiMusicNotesFill onClick={() => navigate('/tracks')} className="navigation-link"/>
          {user && <PiMusicNotesPlusFill onClick={() => navigate('/tracks/new')} className="navigation-link" />}
          <MdLibraryMusic onClick={() => navigate('/albums')} className="navigation-link"/>
          {user && <MdLibraryAdd onClick={() => navigate('/albums/new')} className="navigation-link"/>}
        </div>


        <ProfileButton className="profile-button" user={user} />

      </div>
    </div>


    //   <ul>
    //     {console.log(user)}
    //     <li>
    //       <NavLink to="/">Home</NavLink>
    //     </li>

    //     <li>
    //       <NavLink to="/tracks">See Tracks</NavLink>
    //     </li>
    //     <li><NavLink to="/tracks/new">New Track</NavLink></li>
    //     <li><NavLink to="/albums">See Albums</NavLink></li>
    //     <li><NavLink to="/albums/new">New Album</NavLink></li>

    //     <li>
    //       <ProfileButton />
    //     </li>
    //   </ul>
    // );
  )
}

export default Navigation;
