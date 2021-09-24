import { useState } from 'react'
import SignUpForm from "./SignUpForm";
import { Modal } from '../../context/Modal'
import LoginForm from '../loginModal'



function SignupFormModal() {
    const [showModal, setShowModal] = useState(false)

    return (
        <>
            <button className='ds pointer' id='signup-btn' onClick={() => setShowModal(true)}>
            <i class="fas fa-user-plus"></i>
            </button>
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


