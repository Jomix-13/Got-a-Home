import { useState } from 'react'
import SignUpForm from "./SignUpForm";
import { Modal } from '../../context/Modal'



function SignupFormModal() {
    const [showModal, setShowModal] = useState(false)

    return (
        <>
            <button id='signup-btn' onClick={() => setShowModal(true)}>Sign up</button>
            {showModal && (
                <Modal onClose={() => {
                    setShowModal(false)
                    }}>
                    <SignUpForm />
                </Modal>
            )}
        </>

    )
}

export default SignupFormModal


