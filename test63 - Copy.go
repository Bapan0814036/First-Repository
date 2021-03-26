package main
import "encoding/json"
import "fmt"
import "net/http"

type city struct{
  Name string
  Area uint64
}

func mainLogic(w http.ResponseWriter,r *http.Request){
  if r.Method=="POST"{
    var tempcity city
    decoder:=json.NewDecoder(r.Body)
    err:=decoder.Decode(&tempcity)
    if err!=nil{
      panic(err)
    }
    defer r.Body.Close()
    fmt.Printf("city is %s and  %d is area",tempcity.Name,tempcity.Area)
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("201-Created"))
  }else{
     w.WriteHeader(http.StatusMethodNotAllowed)
     w.Write([]byte("405-Method not alloweed"))
  }
}

func main(){
   http.HandleFunc("/city",mainLogic)
   http.ListenAndServe(":8000",nil)
}