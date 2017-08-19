import slacker
import sys
import os

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Please type your token.")
		sys.exit()
	
	my_token = sys.argv[1]
	
	my_slack = slacker.Slacker(my_token)

	try: 
		file_list = my_slack.files.list().body['files']
	except:
		print('Error connecting to slack.')
		sys.exit()

	if not os.path.exists('download'):
		os.mkdir('download')

	for f in file_list:
		file_to_download = f.get('url_private_download')
		if file_to_download:
			if file_to_download[-3:] == 'pdf':
				slack_file = slacker.requests.get(url=file_to_download,headers={'Authorization': 'Bearer '+my_token})
				file_name = file_to_download.split('/')[-1]
				
				print('Downloading {}'.format(file_name))

				with open('download/'+file_name,'wb') as file_save:
                			file_save.write(slack_file.content)


