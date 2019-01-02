sudo apt-get update
echo 'sleeping for 60 seconds'
sleep 60
echo 'back online'

sudo apt-get -y install python3-requests
echo 'sleeping for 60 seconds'
sleep 60
echo 'back online'

# git clone https://github.com/138Ahmed/google_cloud_API_script
# echo 'sleeping for 45 seconds'
# sleep 45
# echo 'back online'

python3 api_script.py 
echo 'sleeping for 120 seconds'
sleep 120
echo 'back online'

gsutil cp api_output.* gs://api_json_data/api_output/