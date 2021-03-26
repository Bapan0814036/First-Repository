package main
import "net/http"
import "fmt"


func task(w http.ResponseWriter,r *http.Request){
  param:=r.URL.Query()
  w.Write([]byte("Hello Bapan"))
  w.WriteHeader(http.StatusOK)
  fmt.Fprintf(w,"The first query is %s",param["task1"])
}

func main(){
   http.HandleFunc("/task1",task)
   http.ListenAndServe(":9000",nil)
}