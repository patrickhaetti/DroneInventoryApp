// App to gather components. Now only Home is included but easily extendable 

import Home from './Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
    <div className="App">
      <div className="content">
      <Switch>
        <Route exact path="/">
        <Home />
        </Route>
      </Switch>
      </div>
    </div>
    </Router>
  );
}

export default App;
