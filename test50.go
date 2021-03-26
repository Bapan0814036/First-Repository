package main
import "fmt"
import "net/http"
import "github.com/gorilla/mux"


func QueryHandler(w http.ResponseWriter,r *http.Request){
   queryparam:=r.URL.Query()
   w.WriteHeader(http.StatusOK)
   fmt.Fprintf(w,"Got query parameter %s\n",queryparam["id"])
   fmt.Fprintf(w,"Got query parameter %s\n",queryparam["category"])
}

func main(){
  r:=mux.NewRouter()
  r.HandleFunc("/articles",QueryHandler).Queries("id","category")
  http.ListenAndServe(":7000",r)  
}