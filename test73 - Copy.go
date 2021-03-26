package main
import "fmt"
import "math/rand"
import "net/http"

type Cs struct{
}

func (c *Cs)ServeHTTP(w http.ResponseWriter,r *http.Request){
   if r.URL.Path=="/"{
      giveRandom(w,r)
      return
   }
   http.NotFound(w,r)
   return
}

func giveRandom(w http.ResponseWriter,r *http.Request){
   fmt.Fprintf(w,"Your random number is %f",rand.Float64())
}

func main(){
  mux:=&Cs{}
  http.ListenAndServe(":8000",mux)
}