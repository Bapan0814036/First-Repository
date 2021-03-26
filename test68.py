package main
import "fmt"
import "net/http"
import "github.com/gorilla/mux"

func Qhandler(w http.ResponseWriter,r *http.Request){
  param:=r.URL.Query()
  w.WriteHeader(http.StatusOK)
  fmt.Fprintf(w,"The first query is %s",param["task1"])
  fmt.Fprintf(w,"The second query is %s",param["task2"])
  fmt.Fprintf(w,"The third query is %s",param["task3"])
}


func main(){
   m:=mux.NewRouter()
   m.HandleFunc("/task2",Qhandler)
   http.ListenAndServe(":9000",m)
}