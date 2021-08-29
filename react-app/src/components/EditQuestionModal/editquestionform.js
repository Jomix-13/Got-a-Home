import { useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAddQuestion, fetchEditQuestion } from "../../store/questions"
import Errors from "../errors"

import './editquestion.css'

const EditQuestionForm = ({ setShowModal }) => {

    const home = useSelector(state => state.homesReducer.home)
    const qu = useSelector(state => state.questionReducer.question)


    const [question,setQuestion] = useState(qu?.question)

    const dispatch = useDispatch()

    const onSubmit = async(e,id) =>{
        e.preventDefault()
        const payload = {
            question,
            homeId: home.id
        }
        const success = await dispatch(fetchEditQuestion(payload,id))
        if (success){
            setShowModal(false);
        }
        

    }

    return (
        <div className='form-div'>
            <form onSubmit={onSubmit}>
                <div className='form-content'>
                    <div className='form-all-inputs-container'>
                        <div className='form-h3-container'>
                            {/* <h3 className='form-h3'>Login</h3> */}
                        </div>
                        <div >
                            <Errors></Errors>
                            <div className='form-input-container'>
                                <label className='form-label' >Question</label>
                                <input
                                    className='form-input'
                                    type='text'
                                    value={question}
                                    onChange={e=>setQuestion(e.target.value)}
                                >
                                </input>
                            </div>
                            <div>
                                <button className='button' type="submit">Submit</button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
            

    )
}

export default EditQuestionForm