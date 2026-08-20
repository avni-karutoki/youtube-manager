import json

def load_data():
    try:
        with open ('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []    

def save_data(videos):
    with open ('youtube.txt', 'w') as file:
        json.dump(videos , file)

def list_all(videos):
    print('\n')
    print ('*' * 70)
    for index, video in enumerate(videos, start =1):
        print (f"{index}. {video["name"]}, Duration: {video["time"]} ")
    print ('\n')
    print ("*" * 70)    

def add_video(videos):
    name = input ("Enter the video name: ")
    time = input ("Enter the video time: ")
    videos.append({'name': name, 'time':time})
    save_data(videos)

def update_video(videos):
    list_all(videos)
    num = int(input("Enter the video number which you want to update: "))
    if 1 <= num <= len(videos):
        name = input("Enter the new video name:")
        time = input("Enter the new video time:")
        videos [num-1] = {"name":name, "time": time}
        save_data(videos)
    else:
        print ("Invalid video number seleted.")   

def delete_video(videos):
    list_all(videos)
    num = int(input("Enter the video number which you want to delete: "))
    
    if 1 <= num <= len(videos):
        del videos[num-1]
        save_data(videos)
    else:
        print ("Invalid video number seleted.")
            
            
def main ():
    videos = load_data()
    while True:
        print ('\n Youtube Manager|Choose an option:')
        print ('1.List all Youtube Videos.')
        print ('2.Add a Youtube Video.')
        print ('3.Update a Youtube Video details.')
        print ('4.Delete a Youtube Video.')
        print ('5.Exit the app.')
        choice = input ("Enter your choice:")
        
        match choice:
            case '1':
                list_all(videos)
            case '2':
                add_video (videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print ("Invalid choice")
                                
if __name__ == '__main__':
    main()        
    
    