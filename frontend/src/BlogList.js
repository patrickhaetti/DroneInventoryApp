// List Items in table

import './App.css';
import handleClickSort from './handleClickSort'
const BlogList = ({ drones}) => {

console.log(drones);
    return ( 
        <div className="App">
            <header className="App-header">

            <h1>Drones With Cameras</h1>
            <h3>Click on headers for sorting</h3>
            
            <table id="DroneTable">

                <thead>
                <tr>
                <th onClick={() => handleClickSort(0)}>Id</th>
                <th onClick={() => handleClickSort(1)}>Name</th>
                <th onClick={() => handleClickSort(2)}>Model</th>
                <th onClick={() => handleClickSort(3)}>Megapixel</th>
                <th onClick={() => handleClickSort(4)}>Brand</th>
                <th onClick={() => handleClickSort(5)}>Serial Number</th>
                <th onClick={() => handleClickSort(6)}>Supported Cameras</th>
                <th onClick={() => handleClickSort(7)}>Created at</th>
                </tr>
                </thead>

                <tbody>
            {drones.map((item) => (
                    <tr key={item.id}>
                    <td>{item.id}</td>
                    <td>{item.author}</td>
                    <td>{item.model}</td>
                    <td>{item.megapixel}</td>
                    <td>{item.brand}</td>
                    <td>{item.serialno}</td>
                    <td>{item.supported_cameras}</td>
                    <td>{item.created_at}</td>
                    </tr>
            ))}
                </tbody>
                </table>
                <h4>Amount of Items: {drones.length}</h4>
                </header>
        </div>
     );
}

export default BlogList;