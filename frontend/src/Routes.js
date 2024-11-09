import React from "react";
import { Route, Switch } from "react-router-dom";
import Detect from "./pages/Detect";
import NotFound from "./pages/NotFound";
import Database from "./pages/Database";

const routing = ({ childProps }) => (
  <Switch>
    <Route path="/" exact component={Detect} props={childProps} />
    <Route path="/database" exact component={Database} props={childProps} />
    <Route component={NotFound} />
  </Switch>
);
export default routing;
