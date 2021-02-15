import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Test from "./components/Test"
import Graph from "./components/Graph"



function App() {
  return (
    <div className="wrapper">
      <h1>Home page</h1>
      <Router>
        <nav>
          <ul>
            <li><Link to ="/graph">Graph</Link></li>
            <li><Link to="/test">Test</Link></li>
          </ul>
        </nav>
        <Switch>
          <Route path = "/test">
            <Test />
          </Route>  
          <Route path = "/graph" component={Graph}>
            <Graph />
          </Route>
        </Switch>
      </Router>
    </div>

  );
}

/*<Router>
      <Switch>
        <Route
          exact={true}
          path="/test"
          render={(props) => (
            <Test />
          )}
        />
      </Switch>
    </Router>*/
export default App;

/*
    
  */
