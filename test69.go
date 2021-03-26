package main
import "fmt"
import "log"
import "net/http"
import "time"
import "github.com/gorilla/mux"

func Qhandler(w http.ResponseWriter,r *http.Request){
  param:=r.URL.Query()
  w.WriteHeader(http.StatusOK)
  fmt.Fprintf(w,"The first query is %s",param["id"][0])
  fmt.Fprintf(w,"The second query is %s",param["test"][0])
}

func main(){
   r:=mux.NewRouter()
   r.HandleFunc("/article",Qhandler)
   r.Queries("id","category")
   srv:=&http.Server{
     Handler:r,
     Addr:"127.0.0.1:8000",
     WriteTimeout:15*time.Second,
     ReadTimeout:15*time.Second,
   }
   log.Fatal(srv.ListenAndServe())
}