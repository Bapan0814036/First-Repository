package main
import "net/http"
import "fmt"
import "github.com/julienschmidt/httprouter"



func dowork1(work string,arguments ...string)string{
   var str1 string
   for i:=0;i<len(arguments);i++{
     str1+=arguments[i]+" "
   }
   return "doing "+work+" "+str1
}

func func1(w http.ResponseWriter,r *http.Request,params httprouter.Params){

   fmt.Fprintf(w,dowork1("gardening"))
}


func func2(w http.ResponseWriter,r *http.Request,params httprouter.Params){

   fmt.Fprintf(w,dowork1("gardening",params.ByName("name")))
}

func main(){
   router:=httprouter.New()
   router.GET("/work1",func1)
   router.GET("/work2/:name",func2)
   http.ListenAndServe(":8000",router)
}