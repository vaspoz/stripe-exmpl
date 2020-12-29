import './App.css';
import React from "react";

import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import { BrowserRouter } from "react-router-dom";

import ElementDemos from "./components/ElementDemos";
import IdealBankForm from "./components/IdealBankForm";

import "./styles.css";

const stripePromise = loadStripe("pk_test_51I3POiJJCaz63LZXNTUlBogJ7on1YYsLm2zIOQQvF8cUnDNcI59vFBU7i4km8S5IuX8AwrVIFhhadhsYw77nl9pf00pC7d6Y8b");

const demos = [
  {
    path: "/ideal-bank-element",
    label: "IdealBankElement",
    component: IdealBankForm
  }
];

const App = () => {
  return (
    <BrowserRouter>
      <Elements stripe={stripePromise}>
        <ElementDemos demos={demos} />
      </Elements>
    </BrowserRouter>
  );
};

export default App;