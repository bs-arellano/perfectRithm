/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     04/10/2021                         */
/*==============================================================*/

/*==============================================================*/
/* Table: CANCION                                                   */
/*==============================================================*/
create table CANCION (
   CANCION_ID           VARCHAR(15)          not null,
   CANCION_NAME         VARCHAR(30)          not null,
   ARTISTA              VARCHAR(30)          not null,
   GENERO               VARCHAR(30)          not null,
   URL_JSON             VARCHAR(50)          not null,
   URL_MEDIA            VARCHAR(50)          not null,
   constraint PK_CANCION primary key (CANCION_ID)
);

/*==============================================================*/
/* Index: CANCION_PK                                                */
/*==============================================================*/
create unique index CANCION_PK on CANCION (
CANCION_ID
);

/*==============================================================*/
/* Table: RECORD                                                */
/*==============================================================*/
create table RECORD (
   SERIAL               INT4                 not null,
   USER_ID              VARCHAR(15)          null,
   CANCION_ID               VARCHAR(15)          null,
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
/* Index: CANCIONRECORD_FK                                          */
/*==============================================================*/
create  index CANCIONRECORD_FK on RECORD (
CANCION_ID
);

/*==============================================================*/
/* Table: "USER"                                                */
/*==============================================================*/
create table USUARIO (
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
create unique index USER_PK on USUARIO (
UID
);

alter table RECORD
   add constraint FK_RECORD_CANCIONRECORD_CANCION foreign key (CANCION_ID)
      references CANCION (CANCION_ID)
      on delete restrict on update restrict;

alter table RECORD
   add constraint FK_RECORD_USERRECORD_USER foreign key (USER_ID)
      references USUARIO (UID)
      on delete restrict on update restrict;

