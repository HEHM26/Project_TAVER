import boto3    # pip install boto3 or pip3 install boto3

def rasp_download():
    # s3에서 사진 빼오기 위해 IAM 아이디와 비밀번호 적기
    s3_client = boto3.client('s3', aws_access_key_id='AKIA3VLA64D5XFMG2WLQ',
                             aws_secret_access_key='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')

    # 사진들어있는 bucket이름
    bucket_name = 'bucketforjoljak'

    # 버킷의 사진들을 리스트 형식으로 만들기
    res = s3_client.list_objects(Bucket=bucket_name)

    # 가장 최근의 사진을 가져오고 저장할 변수
    recent_picture_name = ''

    # 가장 최근 사진을 가져오기 위해서 비교하는 for문
    for index, list_key in enumerate(res['Contents']):

        # 시간 비교를 위해 사진 이름에서 jpg를 떼는 작업
        list_key = list_key['Key']
        split_list = list_key.split('.')
        pop_value = split_list.pop()
        replace_value = list_key.replace('.' + pop_value, '')

        if index == 0:
            recent_picture_name = replace_value

        # 다음 사진이 가장 최근이라고 한 사진보다 최근일때 값 변경
        if recent_picture_name < replace_value:
            recent_picture_name = replace_value

    # 없앤 jpg 붙이기
    picture_name = recent_picture_name + '.jpg'
    # s3에서 가장 최근 사진 가져오기
    s3_client.download_file(bucket_name, picture_name, 'pictureFromPi.jpg')
    # 최근 사진 다운 받으면 s3안 사진 지우기(s3 용량확보 위해서)
    s3_client.delete_object(Bucket=bucket_name, Key=picture_name)