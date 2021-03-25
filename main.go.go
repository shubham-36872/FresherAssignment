package main
import (
    "fmt"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
)
func main() {
	//http.HandleFunc()
	//http.ListenAndServe(":8080", nil)
	fmt.Println("Welcome")
	db, err := sql.Open("mysql", "username:Mav$#2030@tcp(127.0.0.1:3306)/test")

    if err != nil {
        panic(err.Error())
	}
	
	defer db.Close()
	fmt.Println("DB connected")


}