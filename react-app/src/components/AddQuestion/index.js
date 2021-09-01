import { useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAddQuestion } from "../../store/questions"
import Errors from "../errors"

import './questionform.css'

const AddQuestionForm = () => {

    const home = useSelector(state => state.homesReducer.home)

    const [question,setQuestion] = useState('')

    const dispatch = useDispatch()

    const onSubmit = async(e) =>{
        e.preventDefault()
        const payload = {
            question,
            homeId: home.id
        }
        console.log('COMP 1', payload)
        const success = await dispatch(fetchAddQuestion(payload))
        if (success){
        }
        setQuestion('')

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

export default AddQuestionForm