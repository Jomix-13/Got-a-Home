import { useState } from 'react'
import EditHomeForm from "./EditHome";
import { Modal } from '../../context/Modal'


function EditHomeFormModal({id}) {
    const [showModal, setShowModal] = useState(false)

    return (
        <>
            <button className='button' id='login-btn' onClick={() => setShowModal(true)}>Update</button>
            {showModal && (
                <Modal onClose={() => {
                    setShowModal(false)
                    }}>
                    <EditHomeForm setShowModal={setShowModal} id={id}/>
                </Modal>
            )}
        </>

    )
}

export default EditHomeFormModal
