import { Button, Alert, AlertIcon, Box, AlertTitle, AlertDescription, CloseButton, Container } from "@chakra-ui/react";
import SignUp from "./SignUp";
import Login from "./Login";
import { useMoralis } from "react-moralis";

export const Auth = () => {

    const { authenticate, isAuthenticating, authError } = useMoralis();

    return (
        <>
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
            <SignUp />
            <Login />
            <Button isLoading={isAuthenticating} onClick={() => authenticate()}>Authenticate</Button>
        </Container>
        </>
    );
}