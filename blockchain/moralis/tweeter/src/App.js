import { Button, Container, Heading, Alert, AlertIcon, AlertTitle, Box, AlertDescription, CloseButton, Input } from "@chakra-ui/react";
import { useState } from "react";
import { useMoralis } from "react-moralis";
import Login from "./components/Login";
import SignUp from "./components/SignUp";
import { Routes, Route, Navigate } from "react-router-dom";
import { Home } from "./components/Home";
import { Profile } from "./components/Profile";
import { Auth } from "./components/Auth";

function App() {
  const { authenticate, isAuthenticated, isAuthUndefined, authError, logout, user } = useMoralis();


  return (
    <Container>
      <Header>
        
      </Header>
      {isAuthenticated ? 
      <Routes>
        <Route path="/" element={<Home/>} exact/>
        <Route path="/profile" element={<Profile/>} exact/>
      </Routes> : 
      <>
        {!isAuthUndefined && <Navigate replace to="/"/>}
        <Auth/>
      </>
      }
      
    </Container>
  );
}

export default App;
