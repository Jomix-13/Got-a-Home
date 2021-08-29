import { useState } from 'react'
import EditQuestionForm from "./editquestionform";
import { Modal } from '../../context/Modal'


function EditQuestionFormModal() {
    const [showModal, setShowModal] = useState(false)

    return (
        <>
            <button id='login-btn' onClick={() => setShowModal(true)}>Edit</button>
            {showModal && (
                <Modal onClose={() => {
                    setShowModal(false)
                    }}>
                    <EditQuestionForm />
                </Modal>
            )}
        </>

    )
}

export default EditQuestionFormModal
