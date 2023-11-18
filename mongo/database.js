db.createCollection("video_games", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["title", "genre", "year_released", "platform", "ESRB_rating", "admin"],
            properties: {
                title: {
                    bsonType: "string",
                    description: "must be a string and is required"
                },
                genre: {
                    bsonType: ["array"],
                    items: {
                        bsonType: "string"
                    },
                    description: "must be an array of strings"
                },
                year_released: {
                    bsonType: "int",
                    description: "must be an integer and is required"
                },
                description: {
                    bsonType: "string",
                    description: "must be a string"
                },
                platform: {
                    bsonType: ["array"],
                    items: {
                        bsonType: "string"
                    },
                    description: "must be an array of strings"
                },
                ESRB_rating: {
                    bsonType: "string",
                    description: "must be a string"
                },
                admin: {
                    bsonType: "object",
                    required: ["admin_id", "username", "password"],
                    properties: {
                        admin_id: {
                            bsonType: "int",
                            description: "must be an int and is required"
                        },
                        username: {
                            bsonType: "string",
                            description: "must be a string and is required"
                        },
                        password: {
                            bsonType: "string",
                            description: "must be a string and is required"
                        }
                    }
                }
            }
        }
    }
});
