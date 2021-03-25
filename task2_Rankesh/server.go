package main

import (
    "encoding/json"
    "database/sql"
    "fmt"
    "log"
    "net/http"
    _ "github.com/go-sql-driver/mysql"
)


type Article struct {
    Title  string `json:"Title"`
    Author string `json:"author"`
    Link   string `json:"link"`
}
 
// Articles ...
var Articles []Article


func formHandler(w http.ResponseWriter, r *http.Request) {
    if err := r.ParseForm(); err != nil {
        fmt.Fprintf(w, "ParseForm() err: %v", err)
        return
    }
    fmt.Fprintf(w, "POST request successful")
    name := r.FormValue("name")
    address := r.FormValue("address")
    fmt.Fprintf(w, "Name = %s\n", name)
    fmt.Fprintf(w, "Address = %s\n", address)
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/hello" {
        http.Error(w, "404 not found.", http.StatusNotFound)
        return
    }

    if r.Method != "GET" {
        http.Error(w, "Method is not supported.", http.StatusNotFound)
        return
    }


    fmt.Fprintf(w, "Hello!")
}

func returnAllArticles(w http.ResponseWriter, r *http.Request) {
    fmt.Println("Endpoint Hit: returnAllArticles")
    json.NewEncoder(w).Encode(Articles)
}


func main() {


    Articles = []Article{
        Article{Title: "Python Intermediate and Advanced 101",
            Author: "Arkaprabha Majumdar",
            Link:   "https://www.amazon.com/dp/B089KVK23P"},
        Article{Title: "R programming Advanced",
            Author: "Arkaprabha Majumdar",
            Link:   "https://www.amazon.com/dp/B089WH12CR"},
        Article{Title: "R programming Fundamentals",
            Author: "Arkaprabha Majumdar",
            Link:   "https://www.amazon.com/dp/B089S58WWG"},
    }

    
    fmt.Println("Successfully connected to mysql database")

    db,err :=sql.Open("mysql", "root:root@tcp(127.0.0.1:3306)/testdb")
    
    if err != nil {
        panic(err.Error())
    }

    defer db.Close()


    fileServer := http.FileServer(http.Dir("./static")) // New code
    http.Handle("/", fileServer) // New code

    http.HandleFunc("/form", formHandler)
    http.HandleFunc("/articles", returnAllArticles)
    http.HandleFunc("/hello", helloHandler)

    fmt.Printf("Starting server at port 8080\n")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}