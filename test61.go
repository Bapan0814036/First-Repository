package main
import "fmt"
import "net/http"

func middleware(handler http.Handler)http.Handler{
  return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
      fmt.Println("Executing Middleware before request")
      handler.ServeHTTP(w,r)
      fmt.Println("Executing Middleware after response")
  })
}

func mainLogic(w http.ResponseWriter,r *http.Request){
  fmt.Println("Executing mainhandler")
  w.Write([]byte("ok"))
}

func main(){
   lhandler:=http.HandlerFunc(mainLogic)
   http.Handle("/",middleware(lhandler))
   http.ListenAndServe(":8000",nil)
}