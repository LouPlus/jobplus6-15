# jobplus6-15

LouPlus Team 15 https://www.shiyanlou.com/louplus/python

## Contributors

* [LouPlus](https://github.com/LouPlus)
* [CTCT](https://github.com/ctcodingstyle)
* [Joy818](https://github.com/joy818)

## Database

#### User 用户表
field name|type|desc|notes
:-:|:-:|:-:|:--
id|Integer|用户id|
email|String(128)|邮箱
role|Integer|用户身份| 普通用户0, 企业用户20, 管理员30
password|String(128)|密码
created_time|DateTime|创建时间
updated_time|DateTime|更新时间

#### Seeker 求职者表
field name|type|desc|notes
:-:|:-:|:-:|:--
id|Integer|求职者id
user_id|Integer|用户id
name|String(128)|用户名
phone|Integer|手机号
resume_uri|String(256)|简历链接
created_time|DateTime|创建时间
updated_time|DateTime|更新时间

#### Company 公司表
field name|type|desc|notes
:-:|:-:|:-:|:--
id|Integer|公司id
user_id|Integer|用户id
name|String(128)|公司名
website|String(256)|公司主页链接
logo_uri|String(256)|公司logo链接
introduction|String(256)|一句话简介
description|Text|公司介绍
domain|String(128)|领域
finance|Integer|融资
city|String(128)|所在城市
created_time|DateTime|创建时间
updated_time|DateTime|更新时间


#### Job 职位表
field name|type|desc|notes
:-:|:-:|:-:|:--
id|Integer|职位id
company_id|Integer|公司id
description|Text|
title|String(128)|
salary_max|Integer|
salary_min|Integer|
experience|Integer|
education|String(128)|
created_time|DateTime|创建时间
updated_time|DateTime|更新时间


#### Tag 标签表
field name|type|desc|notes
:-:|:-:|:-:|:--
id|Integer|标签id
job_id|Integer|职位id
name|String(128)|职位名称
created_time|DateTime|创建时间
updated_time|DateTime|更新时间

#### Delivery 简历投递表
field name|type|desc|notes
:-:|:-:|:-:|:--
id|Integer|简历投递id
job_id|Integer|职位id
seeker_id|Integer|求职者id
status|Integer|投递状态|0待审核，1审核中，2审核成功，3审核失败
created_time|DateTime|创建时间
updated_time|DateTime|更新时间
