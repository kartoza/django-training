Middleware
==========

As you are aware, middleware is evaluated when a request arrives at the
app and when a response leaves. Hence it is very important to make this
code as efficient as possible and only apply it when necessary. Adding
slow code here can really affect your app's performance.
