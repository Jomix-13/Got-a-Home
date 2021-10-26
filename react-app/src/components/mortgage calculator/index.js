import { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import {fetchAllHomes} from '../../store/home'
import Map from '../googlemap'
import CurrencyFormat from 'react-currency-format';
import {fetchOneHome,fetchDeleteHome} from '../../store/home'




import './calc.css'

function Calculator(home) {
    // let homeId = home.home.id
    const dispatch = useDispatch()
    const id = home.home.id
    console.log(id,'CALC')
    console.log(home.home.price)
    console.log(home)

    useEffect(()=>{
        console.log(id)
        dispatch(fetchOneHome(id))
        
    },[dispatch,id])

    const term = ['30-yr fixed','20-yr fixed','15-yr fixed'
                // ,'10/1 arm','7/1 arm','5/1 arm','3/1 arm'
                ]
    const [homevalue , setHomevalue] = useState(home.home.price)
    const [downpayment , setDownpayment] = useState((home.home.price * 0.20))
    const [loanterm , setLoanterm] = useState(term[0])
    const [interestRate , setInterestRate] = useState(4)
    const [monthlypaymet , setMonthlypayment] = useState('')
    const [loanamount , setLoanamount] = useState(homevalue-downpayment)
    

    useEffect(()=>{
        setHomevalue(home.home.price)
        setLoanterm(term[0])
        setDownpayment(home.home.price * 0.20)
        
    },[dispatch,home])
    // useEffect(()=>{
    //     if(loanamount + downpayment > homevalue){
    //         setLoanamount(homevalue - downpayment)
    //     }
    // },[downpayment])
    // useEffect(()=>{
    //     if(loanamount + downpayment > homevalue){
    //         downpayment = homevalue - loanamount
    //     }
    // },[loanamount])

    const monthlyPaymet = ()=>{
        // e.preventDefault()
        // M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
        let M = monthlypaymet
        let P = homevalue - downpayment
        let i = interestRate/1200
        let n = 1
        if( loanterm === '30-yr fixed'){
            n = 360
            M = P * i * (Math.pow(1 + i, n)) / (Math.pow(1 + i, n) - 1);

            return M.toFixed(2)
        }
        if( loanterm === '20-yr fixed'){
            n = 240
            M = P * i * (Math.pow(1 + i, n)) / (Math.pow(1 + i, n) - 1);
            return M.toFixed(2)
        }
        if( loanterm === '15-yr fixed'){
            n = 180
            M = P * i * (Math.pow(1 + i, n)) / (Math.pow(1 + i, n) - 1);
            return M.toFixed(2)
        }
    }

    return (
        <div className='CalcContainer'>
            <div className='value'>
            <div> Home Value </div>
                {/* {homevalue} */}
            <CurrencyFormat value={homevalue} displayType={'text'} thousandSeparator={true} prefix={'$'} />
            </div>
            <div className='value'>
                <div> Loan Amount </div>
            <CurrencyFormat value={homevalue - downpayment} displayType={'text'} thousandSeparator={true} prefix={'$'} />

                {/* {homevalue - downpayment} */}
            </div>
            <div className='value'>

                <div> Down Payment </div>
                <div className='subvalue'>
                <div>$</div>
                <input
                    className=''
                    value={downpayment}
                    onChange={e=>setDownpayment(e.target.value)}
                >
                </input>
            </div>
            </div>
            <div className='value'>
                <div> loan Term </div>
                <select
                    className=''
                    value={loanterm}
                    onChange={e=>setLoanterm(e.target.value)}
                >
                {term.map(t => (
                <option
                key={t}
                >
                {t}
                </option>
                ))}
                </select>
            </div>
            <div className='value'>
                <div> Interest Rate </div>
                <div className='subvalue'>
                <input
                    className=''
                    value={interestRate}
                    onChange={e=>setInterestRate(e.target.value)}
                >
                </input>
                <div>%</div>
                </div>
            </div>
            <div className='value'>
                <div> monthly Paymet </div>
                <div className=''>
                <CurrencyFormat value={monthlyPaymet()} displayType={'text'} thousandSeparator={true} prefix={'$'} />
                    {/* {monthlyPaymet()} */}
                </div>
            </div>
            <div className='value'> ## Taxes and insurance are not included</div>
        </div>
    )
}

export default Calculator