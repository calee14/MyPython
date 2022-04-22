import { Box, Input } from "@chakra-ui/react"
import { useMoralis } from "react-moralis"
import { useState } from "react";

export const Profile = () => {
    const { user } = useMoralis();
    
    const [username, setUsername] = useState(user.attributes.username);

    return (
    <Box>
        <Input value={username}/>
    </Box>
    );
}