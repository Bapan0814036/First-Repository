package main
import "encoding/json"
import "log"
import "net/http"
import "strconv"
import "time"
import "fmt"
import "github.com/justinas/alice"

type city struct{
  Name string
  Area uint64
}

func middleware1(handler http.Handler)http.Handler{
    return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
       fmt.Println("Before Request")
       if r.Header.Get("Content-type")!="application/json"{
          w.WriteHeader(http.StatusUnsupportedMediaType)
          w.Write([]byte("405-Unsupported Media Type"))
          return
       }
       handler.ServeHTTP(w,r)
       fmt.Println("After request")
    })
}

func mainlogic(w http.ResponseWriter,r *http.Request){
    if r.Method=="POST"{
       var tempcity city
       decoder:=json.NewDecoder(r.Body)
       err:=decoder.Decode(&tempcity)
       if err!=nil{
           panic(err)
       }
       defer r.Body.Close()
       fmt.Printf("City is %s and %d area",tempcity.Name,tempcity.Area)
       w.WriteHeader(http.StatusOK)
       w.Write([]byte("201-Created"))
    }else{
       w.WriteHeader(http.StatusMethodNotAllowed)
       w.Write([]byte("405-method not allowed"))
    }
}

func middleware2(handler http.Handler)http.Handler{
   return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
        handler.ServeHTTP(w,r)
        cookie:=http.Cookie{Name:"Server-Time(UTC)",Value:strconv.FormatInt(time.Now().Unix(),10)}
        http.SetCookie(w,&cookie)
        log.Println("Done")
   })
}

func main(){
  mhandle:=http.HandlerFunc(mainlogic)
  chain:=alice.New(middleware1,middleware2).Then(mhandle)
  http.Handle("/city",chain)
  http.ListenAndServe(":8000",nil)
}