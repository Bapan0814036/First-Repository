package main
import "fmt"
import "net/http"

func mainlogic(w http.ResponseWriter,r *http.Request){
   fmt.Println("Mainlogic Executed")
   w.Write([]byte("main logic executed"))
}

func middleware(handler http.Handler)http.Handler{
   return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
     fmt.Println("Before running the request")
     handler.ServeHTTP(w,r)
     fmt.Println("After the request is completed")
   })
}

func main(){
   func1:=http.HandlerFunc(mainlogic)
   http.Handle("/",middleware(func1))
   http.ListenAndServe(":8000",nil)   
}

