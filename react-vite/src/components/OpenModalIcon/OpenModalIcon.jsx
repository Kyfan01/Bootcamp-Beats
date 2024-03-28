import { useModal } from '../../context/Modal';

function OpenModalIcon({
  icon,
  modalComponent, // component to render inside the modal
}) {
  const { setModalContent } = useModal();

  const onClick = () => {
    setModalContent(modalComponent);
  };

  return <div onClick={onClick}>
    {icon}
    </div>;
}

export default OpenModalIcon;
