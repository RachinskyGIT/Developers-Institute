const Car = (props) => {
    let { listCars } = props;

    //checking for duplicates
    let valueArr = listCars.map(function (item) { return item.id });
    let isDuplicate = valueArr.some(function (item, idx) {
        return valueArr.indexOf(item) != idx
    });

    //conditional rendering
    if (isDuplicate) {
        throw new Error('Duplicate Keys');
    }
    //else
    return (
        <div>
            {
                listCars.map(item => (
                    <ul key={item.id}>
                        <li>Brand : {item.brand}</li>
                        <li>Name : {item.name}</li>
                        <li>Year of creation : {item.year}</li>
                        <li>Origin : {item.origin}</li>
                    </ul>
                ))
            }
        </div>
    )
}

export default Car;