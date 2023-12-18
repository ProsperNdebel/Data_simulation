async function fetchData(serviceName) {
  try {
    const response = await fetch("http://localhost:5000/fetch_forex_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ apiInput: serviceName }),
    });

    const data = await response.json();
    alert(`Result: ${JSON.stringify(data.result)}`);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

function handleDropdownClick(option) {
  alert("fetching data now...");
  fetchData(option);
}

// Exporting the functions because I am  using ES6 modules
export { fetchData, handleDropdownClick };

// Test cases
async function runTests() {
  try {
    // Test case 1: Successful data fetch
    const result1 = await fetchData("TestService1");
    console.assert(result1 === "ExpectedResult1", "Test case 1 failed");

    // Test case 2: Handle fetch error
    const result2 = await fetchData("TestService2");
    console.assert(result2 === "ExpectedResult2", "Test case 2 failed");
  } catch (error) {
    console.error("Test execution failed:", error);
  }
}

// Run the tests
runTests();
