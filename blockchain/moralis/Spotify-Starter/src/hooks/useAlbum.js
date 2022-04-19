import { useEffect, useState } from "react";
import { useMoralis, useMoralisWeb3Api } from "react-moralis"

export const useAlbum = (contract) => {
    const { token } = useMoralisWeb3Api();
    const { isInitialized } = useMoralis();

    const [albumDetails, setAlbumDetails] = useState();

    const fetchAlbum = async () => {
        return await token
            .getAllTokenIds({
                address: contract,
                chain: "mumbai"
            })
            .then((result) => result);
    };

    useEffect(() => {
        if (isInitialized) {
            fetchAlbum().then((songs) => {
                // console.log(songs.result);
                setAlbumDetails(songs.result)
            });
        }
    }, [isInitialized, contract])


    return { fetchAlbum, albumDetails };
}