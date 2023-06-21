import {useState, useEffect} from 'react'
import { useSelector, useDispatch} from 'react-redux'
import {insert_trx, update_trx} from  '../redux/actions'

const TransactionForm = (props) => {

    //делает то же самое, что и функция handleInputChange (???)
    const [transaction, setTransaction] = useState({
        accountNumber: '',    //эта строка делает то же самое, что и эта строка: const [accountNumber, setAccountNumber] = useState('')
        FSC: '',
        name: '',
        amount: ''
    })

    const currentIndex = useSelector(state => state.currentIndex)
    const list = useSelector(state => state.list)

    const dispatch = useDispatch();

    const handleInputChange = (e) => {
        setTransaction({...transaction, [e.target.name]:e.target.value})
    }

    useEffect(()=>{
        if(currentIndex !=-1){
            const trx = list[currentIndex];
            setTransaction({
                accountNumber:trx.accountNumber|| '', 
                FSC:trx.FSC|| '',
                name:trx.name|| '',
                amount:trx.amount|| ''
            })
        }
    },[currentIndex])

    const handleSubmit = (e) => {
        e.preventDefault()
        if (
                transaction.accountNumber.trim() === '' ||
                transaction.FSC.trim() === '' ||
                transaction.name.trim() === '' ||
                transaction.amount.trim() === ''
          ) {
                // Один или несколько полей пустые, ничего не делаем
                return;
            }

        if(currentIndex === -1) {
            dispatch(insert_trx(transaction))
        }
        else{
            dispatch(update_trx(transaction))
        }

        setTransaction({
            accountNumber: '', 
            FSC: '',
            name: '',
            amount: ''
        })
    }

    
    return(
        <>
        <h2>Transaction Form</h2>
        <form onSubmit={handleSubmit}>
            <input name='accountNumber' 
                placeholder='Accoint Number'
                onChange={handleInputChange}
                value={transaction.accountNumber}
                /><br/>
            <input name='FSC' 
                placeholder='FSC'
                onChange={handleInputChange}
                value={transaction.FSC}
                /><br/>
            <input name='name' 
                placeholder='Name'
                onChange={handleInputChange}
                value={transaction.name}
                /><br/>
            <input name='amount' 
                placeholder='Amount'
                onChange={handleInputChange}
                value={transaction.amount}
                /><br/>
            <input type='submit'
                   value={currentIndex === -1 ? 'Submit' : 'Update'} />
        </form>
        </>
    )

}

export default TransactionForm