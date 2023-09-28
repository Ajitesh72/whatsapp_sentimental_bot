const { create, Client } = require("@open-wa/wa-automate");
const { spawn } = require("child_process");

// Create a WhatsApp bot using wa-automate
create()
  .then((client) => {
    console.log("WhatsApp bot is now connected.");

    client.onMessage(async (message) => {
      console.log(`Received message from ${message.from}: ${message.body}`);

      // Send the message content to the Python NLP script for processing
      const message_extracted = message.body;
      console.log("mssg is", message_extracted);

      const pythonProcess = spawn("python", [
        "whatsapp_nlp.py",
        message_extracted,
      ]);

      pythonProcess.stdout.on("data", (data) => {
        try {
          const outputText_sentiment = data.toString("utf8");
          console.log("Data is:", outputText_sentiment); // Process the extracted information from Python


          // For demonstration purposes, let's send a response back to the user
          // const responseMessage = `Extracted Date: ${extractedInfo.dates.join(
          //   ", "
          // )}\nSentiment: ${outputText_sentiment}`;
          if (outputText_sentiment === positive) {
            client.sendText("thanks for your positive message");
          }
        } catch (error) {
          console.error("Error parsing JSON data from Python:", error);
        }
      });
    });
  })
  .catch((error) => {
    console.error("Error while connecting to WhatsApp:", error);
  });
