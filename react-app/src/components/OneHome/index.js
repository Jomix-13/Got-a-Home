import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import {fetchOneHome,fetchDeleteHome} from '../../store/home'
import {fetchDeleteQuestion} from '../../store/questions'
import EditQuestionFormModal from '../EditQuestionModal'
import EditHomeFormModal from '../EditHome'
import AddQuestionForm from '../AddQuestion'

import './onehome.css'


const OneHome = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const history = useHistory()

    const home = useSelector(state => state.homesReducer.home)
    const user = useSelector(state => state.session.user)
    const questions = useSelector(state => state.questionReducer.questions)

    useEffect(()=>{
        dispatch(fetchOneHome(id))
        // dispatch(fetchAllQuestions())
    },[dispatch,id,questions])
    
    const deleteHome = async(e,id)=>{
        e.preventDefault()
        await dispatch(fetchDeleteHome(id)).then(history.push('/homes'))
        
    }
    const deleteQu = async(e,questionsid)=>{
        e.preventDefault()
        await dispatch(fetchDeleteQuestion(questionsid))    
    }


    return (
        <div className='all'>
            {user?.id === home?.userId ?
            <div>
                <EditHomeFormModal/>
                {/* <NavLink to={`/update/${home.id}`} alt="">
                    <button className='button'>
                        Modify
                    </button>
                </NavLink> */}
                <button className='button' onClick={e=>deleteHome(e,home.id)}>Sold</button>
            </div>
             : null }
            <div className='photos'>
                {home?.images?.map((image)=>(
                    <img key={image} src={image} alt=''></img>
                ))}
            </div>
            <div className='HomeData'>
                <div>
                    <div className='price'>$ {home.price}</div>
                </div>
                <div>
                    <div className='status'>{home.status}</div>
                </div>
                <div className='descriptions'>
                    <div>
                        <div className='adress'>{home.stAddress}</div>
                    </div>
                    <div>
                        <div className='city'>{home.city}, {home.state}. {home.zipCode}</div>
                    </div>
                    <div>
                        <div className='lotSize'>Lot Size : {home.lotSize} sq ft</div>
                    </div>
                    <div>
                        <div className='BB'>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                    </div>
                </div>
                </div>
            <div className='qupa'>
                {user ?
                <div>
                    <AddQuestionForm></AddQuestionForm>
                </div>
                : null}
                <div className='allqu'>
                {home?.questionswuserid?.map((qu)=>(
                    <div key={qu.id} className='qu'>
                        {qu.question}
                        {user?.id === qu.userId ?
                        <>
                            <button className='bb' onClick={e=>deleteQu(e,qu.id)}>delete</button>
                            <EditQuestionFormModal id={qu.id}/>
                        </>
                            :null
                        }
                    </div>
                    ))}
                </div>
            </div>
        </div>

    )
}

export default OneHome