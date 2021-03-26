package main
import "fmt"
import "net/http"



func middleware(handler http.Handler)http.Handler{
   return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
         fmt.Println("Before Request")
         handler.ServeHTTP(w,r)
         fmt.Println("After Request")
   })
}

func mlogic(w http.ResponseWriter,r *http.Request){
   w.Write([]byte("This is main logic section"))
}

func main(){
  mhandler:=http.HandlerFunc(mlogic)
  http.Handle("/req",middleware(mhandler))
  http.ListenAndServe(":8000",nil)
}