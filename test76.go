package main
import "fmt"
import "net/http"
import "github.com/julienschmidt/httprouter"

func getcommand(command string,arguments...string)string{
   var str1 string
   str1=command+" "
   for i:=0;i<len(arguments);i++{
      str1+=arguments[i]+" "
   }
   return str1
}

func gversion(w http.ResponseWriter,r *http.Request,params httprouter.Params){
   fmt.Fprintf(w,getcommand("command1","version1","version2"))
}

func gcontent(w http.ResponseWriter,r *http.Request,params httprouter.Params){
   fmt.Fprintf(w,getcommand("command2",params.ByName("name")))
}

func main(){
  router:=httprouter.New()
  router.GET("/test1",gversion)
  router.GET("/test2",gcontent)
  http.ListenAndServe(":8000",router)
}