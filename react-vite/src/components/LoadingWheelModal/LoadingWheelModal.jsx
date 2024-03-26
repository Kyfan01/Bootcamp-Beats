// import { useModal } from "../../context/Modal";
import "./LoadingWheelModal.css";
import { Oval } from 'react-loader-spinner'


function LoadingWheelModal() {
  // const { closeModal } = useModal();



  return (
    <div className="loading-wheel-bg-div">
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
    </div>
  );
}

export default LoadingWheelModal;
