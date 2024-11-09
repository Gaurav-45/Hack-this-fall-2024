import React from "react";
import { Route, Switch } from "react-router-dom";
import Detect from "./pages/Detect";
import NotFound from "./pages/NotFound";
import Database from "./pages/Database";
import Home from "./pages/Home";
import YPredictor from "./components/YieldPrediction/YPredictor";

const routing = ({ childProps }) => (
  <Switch>
    <Route path="/" exact component={Home} props={childProps} />
    <Route path="/detect" exact component={Detect} props={childProps} />
    <Route path="/database" exact component={Database} props={childProps} />
    <Route
      path="/yieldpredictor"
      exact
      component={YPredictor}
      props={childProps}
    />
    <Route component={NotFound} />
  </Switch>
);
export default routing;
