window.onload = function getData(){
    //用fetch連線並取得資料
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        
//Promotion Text

        let attractions = data["result"]["results"]
        for (let i = 0; i < 3; i++) {
            let promotionElement = document.querySelector(`#promotion-text${i + 1}`);
            promotionElement.textContent = '';
          
            let newPromotionElement = document.createElement('div');
            newPromotionElement.textContent = attractions[i].stitle;
            promotionElement.appendChild(newPromotionElement);
        }
        
        

//Image Text
        
        for (let i = 1; i <= 12; i++) {
            let titleElement = document.querySelector(`#title${i}`);
            titleElement.textContent = '';
          
            let newTitleElement = document.createElement('div');
            newTitleElement.textContent = attractions[i + 2].stitle;
            titleElement.appendChild(newTitleElement);
          }
          
//Promotion Image

        let image1 = document.querySelector("#image1");
        image1.src = attractions[0].file.match(/https:\/\/.*?(?:\.jpg|\.JPG)/)[0];

        let image2 = document.querySelector("#image2");
        image2.src = attractions[1].file.match(/https:\/\/.*?(?:\.jpg|\.JPG)/)[0];
        
        let image3 = document.querySelector("#image3");
        image3.src = attractions[2].file.match(/https:\/\/.*?(?:\.jpg|\.JPG)/)[0];


      



//Item Image

        for (let i = 3; i <= 14; i++) {
            let imageElement = document.querySelector(`#image${i+1}`);
            let newImageElement = document.createElement('img');
            newImageElement.src = attractions[i].file.match(/https:\/\/.*?(?:\.jpg|\.JPG)/)[0];
            newImageElement.className = 'content-image'; // 保留原本的 class
            imageElement.appendChild(newImageElement);
          }

    

       

            

    });
    

  }