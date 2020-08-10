    // Securing Node-RED
    // -----------------
    // To password protect the Node-RED editor and admin API, the following
    // property can be used. See http://nodered.org/docs/security.html for details.
    adminAuth: {
        type: "credentials",
        users: [{
            username: "admin",
            password: "$2a$08$eNu717MuUoucCgUAWKM9Qeymf94ps6qxaJHTzdA2hDOvy2pbrYH12",
            permissions: "*"
        }]
    },

    // To password protect the node-defined HTTP endpoints (httpNodeRoot), or
    // the static content (httpStatic), the following properties can be used.
    // The pass field is a bcrypt hash of the password.
    // See http://nodered.org/docs/security.html#generating-the-password-hash
    httpNodeAuth: {user:"user",pass:"$2a$08$eNu717MuUoucCgUAWKM9Qeymf94ps6qxaJHTzdA2hDOvy2pbrYH12"},
    httpStaticAuth: {user:"user",pass:"$2a$08$eNu717MuUoucCgUAWKM9Qeymf94ps6qxaJHTzdA2hDOvy2pbrYH12"},
