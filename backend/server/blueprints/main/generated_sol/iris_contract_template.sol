// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

// This a template file, the {% %} fields will be filled in at runtime
// because they vary from event to event

contract IrisTemplate is ChainlinkClient {
    using Chainlink for Chainlink.Request;
  
    {% main_fig_type %} public mainFigure;
    
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;
    string  private eventId;
    
    constructor() {
        setPublicChainlinkToken();
        oracle = TODO;
        jobId = "TODO";
        fee = 0.1 * 10 ** 18; // (Varies by network and job)
        eventId = "{% event_id %}"//TODO
    }
    
    // Main figure(s) is defined in the data policy on the chainlink iris event setup
    function requestMainFigure() public returns ({% main_fig_type %} requestId) 
    {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        
        // Set the URL to perform the GET request on
        request.add("get", concat("https://chainiris.io/data/",eventId));
        
        request.add("path", "DATA.FIGURES.1");
        
        // Multiply the result by 1000000000000000000 to remove decimals
        int timesAmount = {% decimal_handler %};
        request.addInt("times", timesAmount);
        
        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }
    
    function concat(string front, string back) internal pure returns (string) {
        return string(abi.encodePacked(a, b));
    }

    /**
     * Receive the response in the form of uint256
     */ 
    function fulfill(bytes32 _requestId, uint256 _mainFigure) public recordChainlinkFulfillment(_requestId)
    {
        mainFigure = _mainFigure;
    }

    // function withdrawLink() external {} - Implement a withdraw function to avoid locking your LINK in the contract
}
