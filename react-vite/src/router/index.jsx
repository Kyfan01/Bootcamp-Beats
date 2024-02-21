import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import TrackFormPage from '../components/TrackComponents/TrackFormPage/TrackFormPage';

import Layout from './Layout';
import TracksIndex from '../components/TrackComponents/TracksIndex/TracksIndex';
import TrackDetailsPage from '../components/TrackComponents/TrackDetailsPage/TrackDetailsPage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "tracks/new",
        element: <TrackFormPage />,
      },
      {
        path: "tracks/:trackId/update",
        element: <TrackFormPage />,
      },
      {
        path: "/tracks",
        element: <TracksIndex />,
      },
      {
        path: "/tracks/:trackId",
        element: <TrackDetailsPage />,
      },
    ],
  },
]);