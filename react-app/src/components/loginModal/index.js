import { useState } from 'react'
import LoginForm from "./LoginForm";
import { Modal } from '../../context/Modal'


function LoginFormModal() {
    const [showModal, setShowModal] = useState(false)

    return (
        <>
            <button className='d pointer' id='login-btn' onClick={() => setShowModal(true)}>
            <i class="fas fa-sign-in-alt"></i>

            {/* <i class="far fa-house-return"></i> */}
            </button>
            {showModal && (
                <Modal onClose={() => {
                    setShowModal(false)
                    }}>
                    <LoginForm />
                </Modal>
            )}
        </>

    )
}

export default LoginFormModal
