import {useSelector} from 'react-redux'
import './errors.css'

const Errors = () =>{
    // const errors = useSelector((state) => state.errorsReducer.errors)
    const errors = useSelector((state) => state.errorsReducer);

    return(
        <div className='errors-div'>
            { errors?.map((errors,idx) => (
                <div className="errors" key={idx}>
                    {errors}
                </div>
            ))}
        </div>
    )
}

export default Errors
