import { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import {fetchAllHomes} from '../../store/home'
import Map from '../googlemap'
import CurrencyFormat from 'react-currency-format';
import {fetchOneHome,fetchDeleteHome} from '../../store/home'



import './calc.css'

function Calculator(home,id) {
    // let homeId = home.home.id
    const dispatch = useDispatch()

    console.log(id)
    console.log(home.home.price)
    console.log()
    useEffect(()=>{
        dispatch(fetchOneHome(id))
    },[dispatch,id])

    const term = ['30-yr fixed','20-yr fixed','15-yr fixed'
                // ,'10/1 arm','7/1 arm','5/1 arm','3/1 arm'
                ]
    const [homevalue , setHomevalue] = useState(home.home.price)
    const [downpayment , setDownpayment] = useState((home.home.price * 0.20))
    // const [loanamount , setLoanamount] = useState(home.home.price - downpayment)
    const [loanterm , setLoanterm] = useState(term[0])
    const [interestRate , setInterestRate] = useState(4)
    const [monthlypaymet , setMonthlypayment] = useState('')

    // useEffect(()=>{
    //     if(loanamount + downpayment > homevalue){
    //         loanamount = homevalue - downpayment
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
            M = P * ( i * ((1 + i)^n) ) / ( (1 + i)^(n - 1))
            return M
        }
        if( loanterm === '15-yr fixed'){
            n = 180
            M = P * ( i * ((1 + i)^n) ) / ( (1 + i)^(n - 1))
            return M
        }
    }

    return (
        <div className='CalcContainer'>
            <div className='value'>
            <div> Home Value </div>
                {homevalue}
            </div>
            <div className='value'>
                <div> Loan Amount </div>

                {homevalue - downpayment}
            </div>
            <div className='value'>
                <div> Down Payment </div>
                <input
                    className=''
                    value={downpayment}
                    onChange={e=>setDownpayment(e.target.value)}
                >
                </input>
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
                    {monthlyPaymet()}
                </div>
            </div>
            <div className='value'> ## Taxes and insurance are not included</div>
        </div>
    )
}

export default Calculator