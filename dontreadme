# Ready. Set. Fight!

_Swoosh, Swoosh!_ Did you hear that sound too?

As you may have noticed from our [website](https://bendingspoons.com/), we focus our work on mobile apps. In order to deliver great products, you must have great technologies behind them: here comes our beloved [Katana](https://github.com/BendingSpoons/katana-swift). Katana is a modern Swift framework for writing the business logic for iOS applications in a way that makes it easy to understand and highly testable.

## Uhm..!? 🤔
At this point, you should be asking yourself: "Why the heck are you introducing me to Katana?"

Well, fair question. What we didn't tell you is that we publicly released it to the open source community. We believe Katana to be one of the very best solutions out there for coding a mobile app and we would like other developers to adopt it and contribute to it to make it even better.

## The challenge
We're addicted to data, meaning that we measure everything we can and we evaluate our choices based on that. In this specific case, we would like to understand whether releasing Katana to the world 🌍 was a good choice or not in terms of external contributions.

To answer this question, our Data Science team asked for the list of commits on the `master` branch. Specifically, we would like to collect all of the commits that have been made until a certain date, label each of them as `Internal contribution` or `External contribution`, and finally store them in an SQLite database.

## How to proceed
To simplify your task we're not going to ask you to solve this test in no specific language. Pick the one you know best (yes, [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) is allowed too) and run with it.

You're required to perform a mini [ETL Process](https://en.wikipedia.org/wiki/Extract,_transform,_load):
 - Download all the commits until `June 27, 2018` by means of [GitHub API](https://developer.github.com/v3/).
 As far as the authentication is concerned, you need to have a GitHub account and create a [personal access token](https://github.com/settings/tokens)* to perform the request**.
 - Get the list of all the members of Bending Spoons. You want to look into `assets/members.json` for this 😉.
 - Classify the internal and the external commits based on the author's login username. An `Internal contribution` is one performed by a member of Bending Spoons. It may happen that some commits have their author username set to `null`: label them as `External contribution` instead.
 - Store the processed information in a database called `github.db`. We provide you with the database schema and the query to create the table. **FOLLOW THEM TO THE LETTER.**
```
CREATE TABLE commits (sha TEXT, date TEXT, author TEXT, message TEXT, is_external INTEGER)
```
 - Additional tips that might help you deliver a perfect solution:
   -  **sha** is the SHA for the commit. Example: `0370242fc8e8a461c69b472de067074d41487ac4`.
   -  **date** is the string the APIs return to represent dates. Example: `2018-02-28T13:10:12Z`.
   -  **author** represents the author's username. Example: `matteomartinelli`.
   -  **message** is the message attached to the commit.
   -  **is_external** is either `1` for `External contribution` or `0` for `Internal contribution`.

\* **DO NOT** include any credentials in the final solution you'll send to us.

** Github has a rate limit on the requests you can perform. More precisely, it accepts a maximum of 60 requests per hour. You shouldn't need that many requests, tough. Alternatively, you can rely on basic _username:password_ authentication.

## What, where, and how to delivery your work
Take your time to solve the exercise. Once you believe you're done, commit your script and the resulting database in the following repository:

```
.
├── assets
│   └── members.json
├── README.md
├── github.db
└── your_script_whatever_it_is.ext
```

Push your commit, and then let us know you're done by pasting your username in the text box you find at the end of the problem that brought you here. We can't wait to see your masterpiece!

## How we'll evaluate your work
We'll evaluate your work according to one key criterion only: robustness.

To evaluate how robust your code is, we'll run a set of tests making sure that your database is consistent with our expectations (do you see now why you need to follow the schema provided to the letter?). Check you've read this ReadMe thoroughly and that your code respects all the requirements.

Use this GitHub repository to develop and submit your script and the resulting database.

**Important**: At Bending Spoons we do everything we can to make sure we evaluate candidates objectively and remove any potential bias from the process. This includes anonymizing your tests before evaluating them. Please help us by **NOT** including any details in your code that could identify you, such as your name, nickname, or email address.

Have fun!
