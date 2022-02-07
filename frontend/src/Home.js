// Home component 

import BlogList from './BlogList';
import useFetch from './useFetch';

const a = "http://";
const b = "<yourIP>";
const c = ":8000/api/v1/";

// Home Page
const Home = () => {

 // const { data: drones, isPending, error } = useFetch('http://<yourIP>:8000/api/v1/')
  const { data: drones, isPending, error } = useFetch(a+b+c);
    return ( 
        <div className="home">
            { error && <div>{ error }</div>}
        { isPending && <div>Loading....</div>}
        {drones && <BlogList drones={drones} title="All Blogs!"/>} 
        </div> 
     );
}
 
export default Home;