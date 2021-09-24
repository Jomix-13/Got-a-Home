import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useHistory, useParams } from "react-router-dom"
import {fetchOneHome,fetchDeleteHome} from '../../store/home'
import {fetchDeleteQuestion} from '../../store/questions'
import EditQuestionFormModal from '../EditQuestionModal'
import EditHomeFormModal from '../EditHome'
import AddQuestionForm from '../AddQuestion'
import CurrencyFormat from 'react-currency-format';


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
    
    const homes = useSelector(state => state.homesReducer.homes)
    const Next = (homes,id) => {
        for( let i=0; i < homes.length; i++) {
            let home = homes[i]
            if (id === home.id){
                console.log(home)
                if ( i+1 > homes.length-1){
                    i = -1
                }
                const nextHome = homes[i+1]
                console.log(nextHome)
                dispatch(fetchOneHome(nextHome.id))
                return history.push(`/homes/${nextHome.id}`)
            }
        }
    }
    const Previous = (homes,id) => {
        for( let i=0; i < homes.length; i++) {
            let home = homes[i]
            if (id === home.id){
                // console.log(home)
                if ( i-1 < 0){
                    i = homes.length
                }
                const nextHome = homes[i-1]
                
                // console.log(nextHome)
                dispatch(fetchOneHome(nextHome.id))
                return history.push(`/homes/${nextHome.id}`)
            }
        }
    }


    return (
        <div className='all'>
            {user?.id === home?.userId ?
            <div>
                <EditHomeFormModal/>
                <button className='button' onClick={e=>deleteHome(e,home.id)}>Sold</button>
            </div>
             : null }
            <div className='photos'>
                {home?.images?.map((image)=>(
                    <img key={image} src={image} alt=''></img>
                ))}
            </div>
            <div className='HomeData'>
            <div className='HomeData2'>
                <div>
                    <div className='price'>
                    <CurrencyFormat value={home.price} displayType={'text'} thousandSeparator={true} prefix={'$'} />
                        {/* $ {home.price} */}
                        </div>
                </div>
                <div>
                    <div className='status'>{home.status}</div>
                </div>
                <div className='descriptions'>
                    <div>
                        <div className='adress'>{home.stAddress},</div>
                    </div>
                    <div>
                        <div className='city'>{home.city}, {home.state} {home.zipCode}</div>
                    </div>
                    <div>
                        <div className='lotSize'>Lot Size : {home.lotSize} sq ft</div>
                    </div>
                    <div>
                        <div className='BB'>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                    </div>
                </div>
                </div>

                <div>
                <button className='button' onClick={()=>Previous(homes,home.id)}>&laquo; Previous</button>
                <button className='button' onClick={()=>Next(homes,home.id)}>Next &raquo;</button>

                </div>
            <div className='qupa'>
                {user ?
                <div>
                    <AddQuestionForm></AddQuestionForm>
                </div>
                : 
                <div className='Note'>*** Please log in to be able to post a question ***</div>}
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
        </div>

    )
}

export default OneHome