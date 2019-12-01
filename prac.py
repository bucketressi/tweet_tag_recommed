#create table hashtag (id INT AUTO_INCREMENT PRIMARY KEY, hashtag1 varchar(255), hashtag2 varchar(255), hashtag3 varchar(255), hashtag4 varchar(255), hashtag5 varchar(255), follower_count INT);
#drop table hashtag;

# 뒤에서 20개만 받아오기
#select * from hashtag order by id desc limit 20;

# 중복된 열 제거
#DELETE n1 FROM hashtag n1, hashtag n2 WHERE n1.id < n2.id AND n1.hashtag1 = n2.hashtag1 and n1.hashtag2 = n2.hashtag2 and n1.hashtag3 = n2.hashtag3;

# 태그 2개 이상만 남겨두기
#delete from hashtag where hashtag2 = '';

# id 재정렬
#alter table hashtag auto_increment = 1; set @count =0; update hashtag set id = @count:=@count+1;

# 불순한 단어 제거
#DELETE FROM hashtag WHERE hashtag1 LIKE "%teen%";

# follower_count가 낮은 열(100이하) 제거
#DELETE FROM hashtag WHERE follower_count <100;


# 검색 결과
#select * from hashtag where hashtag1 like "%beautiful%" OR hashtag2 like "%beautiful%" OR hashtag3 like "%beautiful%" OR hashtag4 like "%beautiful%" OR hashtag5 like "%beautiful%";