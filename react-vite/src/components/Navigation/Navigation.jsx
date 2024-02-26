import { NavLink, useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useSelector } from "react-redux";

import { PiMusicNotesPlusFill } from "react-icons/pi";
import { PiMusicNotesFill } from "react-icons/pi";
import { MdLibraryMusic } from "react-icons/md";
import { MdLibraryAdd } from "react-icons/md";

import logo from '../../../../images/bootcamp_beats_logo.png'



function Navigation() {
  const navigate = useNavigate()
  const user = useSelector(state => state.session.user)
  return (
    <div className="navbar">
      <div className="nav-logo-div">
        <NavLink to='/' className='nav-logo' title="Splash Page">
          <img src={logo} alt="Bootcamp Beats Logo" />
        </NavLink>
      </div>
      <div className="nav-buttons">
        <div className="nav-button-icons-div">
          <PiMusicNotesFill onClick={() => navigate('/tracks')} className="navigation-link" title="All Tracks" />
          {user && <PiMusicNotesPlusFill onClick={() => navigate('/tracks/new')} className="navigation-link" title="New Track" />}
          <MdLibraryMusic onClick={() => navigate('/albums')} className="navigation-link" title="All Albums" />
          {user && <MdLibraryAdd onClick={() => navigate('/albums/new')} className="navigation-link" title="New Album" />}
        </div>


        <ProfileButton className="profile-button" user={user} title="User Options" />

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
