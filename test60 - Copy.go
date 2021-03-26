package main
import "github.com/gorilla/handlers"
import "github.com/gorilla/mux"
import "log"
import "os"
import "net/http"

func mainLogic(w http.ResponseWriter,r *http.Request){
   log.Println("Process Request")
   w.Write([]byte("ok"))
   log.Println("Finished processing Request")
}

func main(){
  r:=mux.NewRouter()
  r.HandleFunc("/",mainLogic)
  loggedRouter:=handlers.LoggingHandler(os.Stdout,r)
  http.ListenAndServe(":8000",loggedRouter)
}