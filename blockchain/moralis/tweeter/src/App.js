import { Button, Container, Heading, Alert, AlertIcon, AlertTitle, Box, AlertDescription, CloseButton} from "@chakra-ui/react";
import { useMoralis } from "react-moralis";

function App() {
  const {authenticate, isAuthenticated, isAuthenticating, authError, logout } = useMoralis();
  if(isAuthenticated) {
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
      <Button isLoading={isAuthenticating} onClick={() => authenticate()}>Authenticate</Button>
    </Container>
  );
}

export default App;
