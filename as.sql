USE answering_system;
-- 题目表
CREATE TABLE IF NOT EXISTS `as_questions`
(
    `id`          BIGINT                             NOT NULL AUTO_INCREMENT COMMENT '主键,题号' PRIMARY KEY,
    `question`    VARCHAR(256)                       NOT NULL COMMENT '题目内容',
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT '创建时间',
    `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) COMMENT '题目表';


-- 答案表
CREATE TABLE IF NOT EXISTS `as_answers`
(
    `id`          BIGINT                             NOT NULL AUTO_INCREMENT COMMENT '主键，答案号' PRIMARY KEY,
    `answer`      VARCHAR(256)                       NOT NULL COMMENT '答案',
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT '创建时间',
    `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) COMMENT '答案表';

-- 数据导入实例
INSERT INTO `as_questions` (`question`)
VALUES ('1922年5月，在广州召开的第一次全国劳动大会是中国____第一次全国性的盛会'),
       ('1930年冬到1931年秋，中央根据地和红一方面军在____的指挥下，进行了三次胜利的反“围剿”斗争。'),
       ('1924年1月，四川的吴玉章、杨周公等20余人，秘密组织中国青年共产党，并创办____作为党的刊物。'),
       ('1922年，____宣言初步阐明了现阶段中国革命的性质、对象、动力、策略、任务和目标，指明了中国革命的前途。'),
       ('1931年11月25日，中华苏维埃共和国临时中央政府发布通令，成立以____为主席，王稼祥、彭德怀为副主席的中央革命军事委员会(简称中革军委)。'),
       ('1935年在赣粤边地区坚持艰苦的游击战争期间，____曾写下:“投身革命即为家，血雨腥风应有涯。取义成仁今日事，人间遍种自由花。'),
       ('上海党组织创办的____是一所培养干部的学校，吸收上海、湖南、浙江、安徽等地的青年入学，学习外语和马克思主义基本知识，同时参加一些革命活动。'),
       ('中国共产党第六次全国代表大会明确指出中国仍然是半殖民地半封建社会，中国革命现在阶段的性质是____。'),
       ('党最早提出关于统一战线的思想和主张是在____。'),
       ('党的二大依据《中国共产党章程》的规定，选举产生了____。');

INSERT INTO `as_answers`(answer)
VALUES ('工人阶级'),
       ('毛泽东、朱德'),
       ('《赤心评论》'),
       ('党的二大'),
       ('朱德'),
       ('陈毅'),
       ('外国语学社'),
       ('资产阶级民主革命'),
       ('党的二大'),
       ('中央执行委员会');
