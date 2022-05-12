import { useMoralis } from 'react-moralis';

export const Login = () => {
    const { authenticate, isAuthenticated } = useMoralis();

    return (
        <div className='flex w-screen h-screen justify-center items-center'>
            <button className="border-[1px] p-2 border-black" onClick={() => authenticate()}>Auth with MetaMask</button>
        </div>
    );
};