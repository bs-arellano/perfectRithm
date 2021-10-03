/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     02/10/2021 8:38:11                           */
/*==============================================================*/

/*==============================================================*/
/* Table: MAP                                                   */
/*==============================================================*/
create table MAP (
   MAP_ID               VARCHAR(15)          not null,
   MAP_NAME             VARCHAR(30)          not null,
   DIFFICULT            NUMERIC              not null,
   URL_JSON             VARCHAR(50)          not null,
   URL_MEDIA            VARCHAR(50)          not null,
   constraint PK_MAP primary key (MAP_ID)
);

/*==============================================================*/
/* Index: MAP_PK                                                */
/*==============================================================*/
create unique index MAP_PK on MAP (
MAP_ID
);

/*==============================================================*/
/* Table: RECORD                                                */
/*==============================================================*/
create table RECORD (
   SERIAL               INT4                 not null,
   USER_ID              VARCHAR(15)          null,
   MAP_ID               VARCHAR(15)          null,
   SCORE                INT4                 not null,
   ACCURACY             NUMERIC              not null,
   DATE                 DATE                 not null,
   constraint PK_RECORD primary key (SERIAL)
);

/*==============================================================*/
/* Index: RECORD_PK                                             */
/*==============================================================*/
create unique index RECORD_PK on RECORD (
SERIAL
);

/*==============================================================*/
/* Index: USERRECORD_FK                                         */
/*==============================================================*/
create  index USERRECORD_FK on RECORD (
USER_ID
);

/*==============================================================*/
/* Index: MAPRECORD_FK                                          */
/*==============================================================*/
create  index MAPRECORD_FK on RECORD (
MAP_ID
);

/*==============================================================*/
/* Table: "USER"                                                */
/*==============================================================*/
create table "USER" (
   UID                  VARCHAR(15)          not null,
   USERNAME             VARCHAR(16)          not null,
   EMAIL                VARCHAR(320)         not null,
   PASSWORD             VARCHAR(30)          not null,
   LEVEL                INT4                 not null,
   USER_SCORE           INT4                 not null,
   constraint PK_USER primary key (UID)
);

/*==============================================================*/
/* Index: USER_PK                                               */
/*==============================================================*/
create unique index USER_PK on "USER" (
UID
);

alter table RECORD
   add constraint FK_RECORD_MAPRECORD_MAP foreign key (MAP_ID)
      references MAP (MAP_ID)
      on delete restrict on update restrict;

alter table RECORD
   add constraint FK_RECORD_USERRECOR_USER foreign key (USER_ID)
      references "USER" (UID)
      on delete restrict on update restrict;

