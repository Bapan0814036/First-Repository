package main
import "net/http"
import "time"
import "strings"
import "fmt"


func mlogic(w http.ResponseWriter,r *http.Request){
  fmt.Println(strings.Split(r.URL.Path,"/")[1])
  w.Write([]byte("Service1 Executed"))
  w.WriteHeader(http.StatusOK)
}

func main(){
  http.HandleFunc("/serv1",mlogic)
  serv:=&http.Server{
    Addr:":8000",
    ReadTimeout:10*time.Second,
    WriteTimeout:10*time.Second,
    MaxHeaderBytes:1<<20,
  }
  serv.ListenAndServe()
}