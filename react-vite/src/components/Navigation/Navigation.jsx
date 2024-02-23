import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useSelector } from "react-redux";


function Navigation() {
  const user = useSelector(state => state.session.user)
  return (
    <ul>
      {console.log(user)}
      <li>
        <NavLink to="/">Home</NavLink>
      </li>

      <li>
        <NavLink to="/tracks">See Tracks</NavLink>
      </li>
      <li><NavLink to="/tracks/new">New Track</NavLink></li>
      <li><NavLink to="/albums">See Albums</NavLink></li>
      <li><NavLink to="/albums/new">New Album</NavLink></li>

      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}

export default Navigation;
