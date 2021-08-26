import { useState } from 'react'
import SignUpForm from "./SignUpForm";
import { Modal } from '../../context/Modal'
import LoginForm from '../loginModal'



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
                    {/* <LoginForm></LoginForm> */}
                </Modal>
            )}
        </>

    )
}

export default SignupFormModal
