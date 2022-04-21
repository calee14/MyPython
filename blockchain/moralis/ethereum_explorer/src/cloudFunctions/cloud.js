
//comment this out when saving changes
// import Moralis from "moralis";

Moralis.Cloud.define("searchEthAddress", async (request) => {
   //PLACEHOLDER
});

Moralis.Cloud.define("getEthTransactions", async(request) => {
  //PLACEHOLDER
  const query1 = new Moralis.Query("EthTransactions");

  query1.equalTo("from_address", request.params.address);

  const query2 = new Moralis.Query("EthTransactions");
  
  query2.equalTo("to_address", request.params.address);

  const combinedQuery = Moralis.Query.or(query1, query2);
  combinedQuery.descending("block_number");

  combinedQuery.withCount();

  const results = await combinedQuery.find();

  return results;
});