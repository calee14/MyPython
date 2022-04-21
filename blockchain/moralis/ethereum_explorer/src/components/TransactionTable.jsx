import { useState } from "react";
import { processTransaction } from "../utility/utils";
const cols = [
    { colName: "Txn Hash", key: "hash"},
    { colName: "Block", key: "block_number"},
    { colName: "Age", key: "age"},
    { colName: "From", key: "from_address"},
    { colName: "To", key: "to_address"},
    { colName: "Value", key: "value"},
    { colName: "Txn Fee", key: "gas"}
  ];
/*props should include:
transactions = array of transactions
 */
const TransactionTable = (props) => {

    if (props.loading)
        return(
          <div>
            <div>
              <table className="table">
                <thead className="thead-light">
                  <tr>
                    {cols.map((col) => (
                      <th scope="col" key={col.colName}>
                        {col.colName}
                      </th>
                    ))}
                  </tr>
                </thead>
              </table>
            </div>
            <div className="d-flex justify-content-center">
              <div className="spinner-border" style={{width: '6rem', height: '6rem'}}role="status">
                <span className="sr-only"></span>
              </div>
            </div>
          </div>
        );
    
    return (
    <div>
      <table className="table">
        <thead className="thead-light">
          <tr>
            {cols.map((col) => (
              <th scope="col" key={col.colName}>
                {col.colName}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {props.transactions.map((transaction, index) => (
            <tr key={index}>
              {cols.map((col) => {
                return(<td key = {col.colName}>{processTransaction(transaction)[col.key]}</td>)
})}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    );
}

export default TransactionTable;