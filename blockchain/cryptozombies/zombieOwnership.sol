pragma solidity >=0.5.0 <0.6.0;

import "./zombieAttack.sol";
import "./erc721.sol";

contract ZombieOwnership is ZombieAttack, ERC721 {


  function balanceOf(address _owner) external view returns (uint256) {
    return ownerZombieCount[_owner];
  }

  function ownerOf(uint256 _tokenId) external view returns (address) {
    return zombieToOwner[_tokenId];
  }

  function _transfer(address _from, address _to, uint256 _tokenId) private {
    ownerZombieCount[_to]++;
    ownerZombieCount[_from]--;
    zombieToOwner[_tokenId] = _to;
    emit Transfer(_from, _to, _tokenId);
  }

  function transferFrom(address _from, address _to, uint256 _tokenId) external payable {
    // 2. Add the require statement here
    // 3. Call _transfer
  }

  function approve(address _approved, uint256 _tokenId) external payable {

  }

}
