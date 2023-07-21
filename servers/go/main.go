package main

import (
	"fmt"
	"net/http"
)

func handleRequest(w http.ResponseWriter, r *http.Request) {
	host := r.Host
	w.Header().Set("Connection", "close")
	fmt.Fprintf(w, "[%s]", host)
}

func main() {
	port := 3004
	http.HandleFunc("/", handleRequest)
	fmt.Printf("Server listening on http://localhost:%d\n", port)
	err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
	if err != nil {
		fmt.Println("Error starting the server:", err)
	}
}
