import { DateTime } from 'luxon';

export const processTransaction = (transaction) => {
    
    const processed = {
        ...transaction,
        hash: shortenString(transaction.hash),
        block_number: transaction.block_number,
        age: agoTime(transaction.block_timestamp.valueOf()),
        from_address: shortenString(transaction.from_address),
        to_address: shortenString(transaction.to_address),
        value: toEth(parseInt(transaction.value)),
        gas: toEth(parseInt(transaction.gas)),
    }
    return processed;
};

export const agoTime = (unixTimeStampMili) => {
    return DateTime.fromMillis(unixTimeStampMili).toRelative();
}


export const shortenString = (address) => {
    if (!(address?.length))
        return "";
    if (address.length <= 12)
        return address;
    return address.substring(0, 6) + "..." + address.substring(address.length - 6, address.length);
};

export const toEth = (gweiAmount) => {
    return (gweiAmount / Math.pow(10, 18) + " ETH");
};
