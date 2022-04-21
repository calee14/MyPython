import { Button, Container, Heading, Alert, AlertIcon, AlertTitle, Box, AlertDescription, CloseButton, Input } from "@chakra-ui/react";
import { useState } from "react";
import { useMoralis } from "react-moralis";
import Login from "./components/Login";
import SignUp from "./components/SignUp"

function App() {
  const { authenticate, isAuthenticated, isAuthenticating, authError, logout } = useMoralis();

  if (isAuthenticated) {
    return (
      <Container>
        <Heading>Welcome to Tweeter</Heading>
        <Button onClick={() => logout()}>Logout</Button>
      </Container>
    )
  }

  return (
    <Container>
      Tweeter
      {authError &&
        <Alert status='error'>
          <AlertIcon />
          <Box>
            <AlertTitle>Authentication has failed</AlertTitle>
            <AlertDescription>
              {authError.message}
            </AlertDescription>
          </Box>
          <CloseButton
            alignSelf='flex-start'
            position='relative'
            right={-1}
            top={-1}
          />
        </Alert>
      }
      <SignUp/>
      <Login/>
      <Button isLoading={isAuthenticating} onClick={() => authenticate()}>Authenticate</Button>
    </Container>
  );
}

export default App;
