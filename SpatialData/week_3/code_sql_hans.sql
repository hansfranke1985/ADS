CREATE EXTENSION postgis;
CREATE EXTENSION pgrouting;

drop table roads_ams_2008 cascade

#testing loaded dataset#
select * from roads_ams_2008 limit 10
select * from obstacles limit 10

## create topology
ALTER TABLE roads_ams_2008 ADD COLUMN "source" integer;
ALTER TABLE roads_ams_2008 ADD COLUMN "target" integer;

SELECT pgr_createTopology('roads_ams_2008', 0.000001, 'geom', 'gid');


Alter table roads_ams_2008 add cost double precision;
update roads_ams_2008 set cost=st_length(ST_Transform(geom, 28992))

ALTER TABLE roads_ams_2008 ADD COLUMN reverse_cost double precision;
UPDATE roads_ams_2008 SET reverse_cost = cost;

Select * from roads_ams_2008 limit 10

SELECT roads_ams_2008_vertices_pgr.id FROM roads_ams_2008_vertices_pgr,
firestations_ams_2013 where firestations_ams_2013.OBJECTID=1014 ORDER BY
ST_Distance(ST_Transform(ST_SetSRID(firestations_ams_2013.geom, 4326),
28992), ST_Transform(roads_ams_2008_vertices_pgr.the_geom, 28992)) ASC
LIMIT 1;

SELECT roads_ams_2008_vertices_pgr.id FROM roads_ams_2008_vertices_pgr,
firestations_ams_2013 where firestations_ams_2013.OBJECTID=533 ORDER BY
ST_Distance(ST_Transform(ST_SetSRID(firestations_ams_2013.geom, 4326),
28992), ST_Transform(roads_ams_2008_vertices_pgr.the_geom, 28992)) ASC
LIMIT 1;

SELECT id FROM roads_ams_2008_vertices_pgr ORDER BY
ST_Distance(ST_GeomFromText('POINT(4.806462559
52.4438188114)',4326)::geography, the_geom::geography) ASC LIMIT 1;

Drop table if exists destinations;
Create table destinations (
id integer,
nn_id integer, -- nearest node id
geom geometry(point, 4326)
);

select * from destinations;

INSERT INTO destinations (id, nn_id, geom) values (1, 1300,
ST_GeomFromText('POINT(4.806462559 52.4438188114)',4326)); 

SELECT id FROM roads_ams_2008_vertices_pgr ORDER BY
ST_Distance(ST_GeomFromText('POINT(4.806462559 52.4438188114)',4326)::geography, the_geom::geography) ASC LIMIT 1;

--please change XXXX to the closet node ID for the destination POINT(4.816071043 52.3480865708), according to your network
INSERT INTO destinations (id, nn_id, geom) values (2, 5715,
ST_GeomFromText('POINT(4.816071043 52.3480865708)',4326));

SELECT id FROM roads_ams_2008_vertices_pgr ORDER BY
ST_Distance(ST_GeomFromText('POINT(4.923351096 52.4117317620)',4326)::geography, the_geom::geography) ASC LIMIT 1;

--please change XXXX to the closet node ID for the destination POINT(5.000307123 52.3539927035), according to your network
INSERT INTO destinations (id, nn_id, geom) values (3, 35768,
ST_GeomFromText('POINT(5.000307123 52.3539927035)',4326));

--please change XXXX to the closet node ID for the destination POINT(4.864906827 52.3127379258), according to your network
INSERT INTO destinations (id, nn_id, geom) values (4, 12215,
ST_GeomFromText('POINT(4.864906827 52.3127379258)',4326));

--please change XXXX to the closet node ID for the destination POINT(4.923351096 52.4117317620), according to your network
INSERT INTO destinations (id, nn_id, geom) values (5, 32485,
ST_GeomFromText('POINT(4.923351096 52.4117317620)',4326));

UPDATE roads_ams_2008 SET cost =999999, reverse_cost=999999 From obstacles
WHERE ST_Intersects(roads_ams_2008.geom, obstacles.geom) 



