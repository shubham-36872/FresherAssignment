package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"database/sql"
    _ "github.com/go-sql-driver/mysql"
	
	
)	

type Book struct{
	ID string `json:"Id"`
	Title string `json:"Title"`
	Desc string `json:"Desc"`
	Price string `json:"Price"`
}

type allBook []Book
var events = allBook{
	{
		ID:          "1",
		Title:       "Introduction to Golang",
		Desc: "Come join us for a chance to learn how golang works and get to eventually try it out",
		Price: "100",
	},
}
func allBooks(w http.ResponseWriter, r *http.Request) { 
	
	json.NewEncoder(w).Encode(events)
}

func main() {
   fmt.Println("Before connection of mysql ")
   db, err :=sql.Open("mysql","root:root@tcpl(127.0.0.1:3306)/mavenirdb") 
   if err != nil {
	   panic(err.Error())
   }

   defer db.Close()
   
	http.HandleFunc("/", allBooks)
	fmt.Println("Succesfully connected to database ")
	log.Fatal(http.ListenAndServe(":8080", nil))
}