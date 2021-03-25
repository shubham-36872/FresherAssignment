package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type User struct {
	ID         string `json:"id"`
	Age        string `json:"age"`
	First_name string `json:"first_name"`
	Last_name  string `json:"last_name"`
}

func userhandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/user" {
		http.Error(w, "404 not found.", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "Method is not supported.", http.StatusNotFound)
		return
	}

	fmt.Println("Go MySQL")

	db, err := sql.Open("mysql", "root:mavenir@tcp(127.0.0.1:3306)/test")
	// if there is an error opening the connection, handle it
	if err != nil {
		panic(err.Error())
	}
	// defer the close till after the main function has finished
	defer db.Close()

	result, err := db.Query("SELECT id, age, first_name, last_name FROM users")
	if err != nil {
		panic(err.Error())
	}

	for result.Next() {
		var user User

		err = result.Scan(&user.ID, &user.Age, &user.First_name, &user.Last_name)
		if err != nil {
			panic(err.Error())
		}
		//Output on console
		fmt.Println(user.ID, " ", user.Age, " ", user.First_name, " ", user.Last_name)
		//Output on Server
		fmt.Fprintf(w, "User ID : %v\n", user.ID)
		fmt.Fprintf(w, "User Age : %v\n", user.Age)
		fmt.Fprintf(w, "User First Name : %s\n", user.First_name)
		fmt.Fprintf(w, "User Last Nmae: %s\n", user.Last_name)

	}

}

func main() {

	http.HandleFunc("/user", userhandler)

	fmt.Printf("Starting server at port 8080\n")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}
