package main
import "net/http"
import "github.com/julienschmidt/httprouter"

func main(){
   router:=httprouter.New()
   router.ServeFiles("/static/*filepath",http.Dir("./"))
   http.ListenAndServe(":8000",router)
}