import { useState } from 'react'
import EditQuestionForm from "./editquestionform";
import { Modal } from '../../context/Modal'


function EditQuestionFormModal({id}) {
    const [showModal, setShowModal] = useState(false)

    return (
        <>
            <button className='bb' id='login-btn' onClick={() => setShowModal(true)}>Edit</button>
            {showModal && (
                <Modal onClose={() => {
                    setShowModal(false)
                    }}>
                    <EditQuestionForm setShowModal={setShowModal} id={id}/>
                </Modal>
            )}
        </>

    )
}

export default EditQuestionFormModal
