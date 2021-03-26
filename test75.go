package main
import "fmt"
import "net/http"


func mlogic(w http.ResponseWriter,r *http.Request){
     fmt.Println("Executing Request")
     w.Write([]byte("mlogic executed"))
     w.WriteHeader(http.StatusOK)
}

func main(){
   mux:=http.NewServeMux()
   mux.HandleFunc("/test",mlogic)
   http.ListenAndServe(":8000",mux)
}