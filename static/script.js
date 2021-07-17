document
  .getElementsByClassName("app-form-button")[0]
  .addEventListener("click", prediction);
function prediction() {
  var text = document.getElementsByClassName("app-form-control")[0].value;
  console.log(text);
  const URL = "/predict";
  const data = {
    news_text: text,
  };
  var json_data;
  // Send a post request
  fetch(URL, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (data["prediction"] == 1) {
        alert("The news is unreliable");
      } else if (data["prediction"] == 0) {
        alert("The news is reliable");
      }
      console.log(data);
    })
    .catch((err) => {
      alert(err);
      console.log(err);
    });
}
