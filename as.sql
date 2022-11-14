USE answering_system 
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
       ('1930年冬到1931年秋，中央根据地和红一方面军在____的指挥下，进行了三次胜利的反“围剿”斗争。');

INSERT INTO `as_answers`(answer)
VALUES ('工人阶级');

SELECT q.question, a.answer
FROM as_questions q
         JOIN as_answers a ON q.id = a.id;










