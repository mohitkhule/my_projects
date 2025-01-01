create database ola_db ;
use ola_db;
select * from booking;

# 1. Retrieve all successful bookings:
create view successful_bookings as
select * from bookings where booking_status = 'success';

#2. Find the average ride distance for each vehicle type:
 create view  average_ride_distance_for_each_vehicle as
 select  Vehicle_Type , avg(ride_distance) as avg_distance from bookings
group by Vehicle_Type;  # 14.2132
 
 
# 3. Get the total number of cancelled rides by customers:
create view total_number_of_cancelled_rides_by_customers as 
select count(Canceled_Rides_by_Customer)as number_of_rides_cancelled from bookings; # 9421


 #4. List the top 5 customers who booked the highest number of rides:
 create view booked_the_highest_number_of_rides as
 select Customer_ID , count(Booking_ID) as total_rides
 from bookings  group by Customer_ID order by total_rides desc limit 5 ;
 
 
 
 #5. Get the number of rides cancelled by drivers due to personal and car-related issues:
 create view cancelled_rides_by_rides as
 SELECT COUNT(*) FROM bookings WHERE Canceled_Rides_by_Driver = 'Personal & Car
 related issue';
 
 #6. Find the maximum and minimum driver ratings for Prime Sedan bookings:
 create view max_min_rating_for_primesedan as
 select max(Driver_Ratings) as max_rating , min(Driver_Ratings) as min_rating 
 from bookings where Vehicle_Type = "Prime Sedan";
 
 
 #7. Retrieve all rides where payment was made using UPI:

create view  rides_payment_by_upi as
 SELECT * FROM bookings WHERE Payment_Method = 'UPI';
 
 #8. Find the average customer rating per vehicle type:
 create view avg_cust_rating_by_vtype as
 select avg(Customer_Rating) as avg_customer_rating , Vehicle_Type from bookings group by  Vehicle_Type ;
 
# 9. Calculate the total booking value of rides completed successfully:
create view total_booking_value as
select sum(Booking_Value) as booking_value from bookings ;

 #10. List all incomplete rides along with the reason:
 create view list_ofincompletet_rides as 
 SELECT Booking_ID, Incomplete_Rides_Reason FROM bookings WHERE Incomplete_Rides ='Yes';

 
 