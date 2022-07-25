def create_youtube_video(title, description):
	video_dict = {"title":title, "description":description, "likes": 0, 'dislikes':0, 'comments':{}}
	global video_list
	videos_dict[title] = video_dict

def like(dict):
	if "likes" in dict:
		dict['likes'] +=1
		return dict
def comment(youtubevideo, username, comment_text):
	youtubevideo['comments'][username] = comment_text
	return youtubevideo
def dislike(dict):
	if 'likes' in dict:
		dict['dislikes']+=1
		return dict

global video_list
videos_dict={}

x=3

while x<4:
	request = input('search/post/ exit: ')
	if request=='search':
		request = input('name of video: ')
		if request in videos_dict:
			video = videos_dict[request]
			print(request)
			print(video['description'])
			print(str(video['likes']) + ' likes')
			print(str(video['dislikes'])+ ' dislikes')
			while x==3:
				
				request = input('like/dislike/comment/see comments/cancel: ')
				if request=='like':
					video = like(video)
					print(str(video['likes'])+ ' likes')
				elif request=='dislike':
					video = dislike(video)
					print(str(video['dislikes']) + ' dislikes')
				elif request=='comment':
					comment(video, input('username: '), input('comment: '))
				elif request=='see comments':
					print(video['comments'])
				elif request=='cancel':
					x=2
	if request=='post':
		create_youtube_video(input('title: '), input('description: '))
	if request=='exit':
		print('done.')
		x=5
