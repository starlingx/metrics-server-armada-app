
/* Copyright (c) 2021 Wind River Systems, Inc.

  SPDX-License-Identifier: Apache-2.0 */


const fetch = require('node-fetch');
const https = require('https');
const fs = require('fs');

const url = "https://kubernetes.default.svc/apis/metrics.k8s.io/v1beta1/pods"

const httpsAgent = new https.Agent({
  rejectUnauthorized: false,
});

if (process.env.TOKEN_PATH) {
  fs.readFile(process.env.TOKEN_PATH, 'utf8', (err, token) => {
    if (err) {
      console.error(`Error reading TOKEN_PATH: ${TOKEN_PATH}`, err)
      return
    }
    if (!token) {
      console.log("Miss the token, stopping the application!")
      process.exit(1)
    }
    setInterval(async () => {
      try {
        console.log(`Using the token ${token}`);
        const response = await fetch(url, {
          method: 'GET',
          headers: { "Authorization": `Bearer ${token}` },
          agent: httpsAgent
        });

        const body = await response.text();
        console.log(body);
      } catch (error) {
        console.log(`Error requesting ${url}` + error);
      }
    }, 1000)
  });
} else {
  console.error("Missing the TOKEN_PATH variable. Stopping the application");
  process.exit(1)
}






