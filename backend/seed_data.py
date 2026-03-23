from __future__ import annotations

from sqlalchemy.orm import Session
import models
from database import SessionLocal


def seed_rooms(db: Session) -> None:
    """Populate sample rooms into the database"""
    
    # Check if rooms already exist
    existing_rooms = db.query(models.Room).first()
    if existing_rooms:
        print("Rooms already exist in database, skipping room seeding...")
        return
    
    rooms_data = [
        {
            "room_title": "Deluxe Suite",
            "image": "/images/rooms/deluxe-suite.jpg",
            "description": "Spacious suite with premium furnishings, king-size bed, separate living area, and bathroom with modern amenities.",
            "price": "299",
            "wifi": "yes",
            "room_type": "Suite",
        },
        {
            "room_title": "Ocean View Room",
            "image": "/images/rooms/ocean-view.jpg",
            "description": "Beautiful room with panoramic ocean views, private balcony, queen-size bed, and luxury bathroom.",
            "price": "249",
            "wifi": "yes",
            "room_type": "Deluxe",
        },
        {
            "room_title": "Standard Room",
            "image": "/images/rooms/standard-room.jpg",
            "description": "Comfortable standard room with queen-size bed, modern furnishings, and en-suite bathroom.",
            "price": "149",
            "wifi": "yes",
            "room_type": "Standard",
        },
        {
            "room_title": "Family Room",
            "image": "/images/rooms/family-room.jpg",
            "description": "Large family room with two queen-size beds, separate living area, kitchenette, and bathroom.",
            "price": "349",
            "wifi": "yes",
            "room_type": "Family",
        },
        {
            "room_title": "Budget Room",
            "image": "/images/rooms/budget-room.jpg",
            "description": "Compact and affordable room with single or twin beds, essential amenities, and shared or private bathroom.",
            "price": "99",
            "wifi": "yes",
            "room_type": "Budget",
        },
        {
            "room_title": "Luxury Penthouse",
            "image": "/images/rooms/luxury-penthouse.jpg",
            "description": "Ultimate luxury experience with panoramic views, private hot tub, king-size bed, and personalized service.",
            "price": "499",
            "wifi": "yes",
            "room_type": "Penthouse",
        },
        {
            "room_title": "Garden View Room",
            "image": "/images/rooms/garden-view.jpg",
            "description": "Peaceful room overlooking landscaped gardens, queen-size bed, and modern bathroom.",
            "price": "179",
            "wifi": "yes",
            "room_type": "Standard",
        },
        {
            "room_title": "Business Room",
            "image": "/images/rooms/business-room.jpg",
            "description": "Perfect for business travelers with work desk, high-speed internet, comfortable bed, and meeting space.",
            "price": "199",
            "wifi": "yes",
            "room_type": "Business",
        },
    ]
    
    for room_data in rooms_data:
        room = models.Room(**room_data)
        db.add(room)
    
    db.commit()
    print(f"✓ Seeded {len(rooms_data)} rooms successfully!")


def seed_ratings(db: Session) -> None:
    """Populate sample room ratings"""
    
    # Check if ratings already exist
    existing_ratings = db.query(models.RoomRating).first()
    if existing_ratings:
        print("Ratings already exist in database, skipping ratings seeding...")
        return
    
    rooms = db.query(models.Room).all()
    if not rooms:
        print("No rooms found, cannot seed ratings...")
        return
    
    ratings_data = [
        {
            "room_id": rooms[0].id,
            "username": "John Smith",
            "email": "john@example.com",
            "comment": "Amazing suite! Best stay ever. Highly recommended!",
            "rating": 5.0,
            "status": 1,
        },
        {
            "room_id": rooms[1].id,
            "username": "Sarah Johnson",
            "email": "sarah@example.com",
            "comment": "Wonderful ocean view. Perfect for a romantic getaway.",
            "rating": 5.0,
            "status": 1,
        },
        {
            "room_id": rooms[2].id,
            "username": "Mike Davis",
            "email": "mike@example.com",
            "comment": "Good value for money. Clean and comfortable.",
            "rating": 4.0,
            "status": 1,
        },
        {
            "room_id": rooms[3].id,
            "username": "Emily Rodriguez",
            "email": "emily@example.com",
            "comment": "Perfect for family vacation! Spacious and well-equipped.",
            "rating": 5.0,
            "status": 1,
        },
        {
            "room_id": rooms[4].id,
            "username": "David Wilson",
            "email": "david@example.com",
            "comment": "Budget-friendly option. Basic but clean.",
            "rating": 4.0,
            "status": 1,
        },
        {
            "room_id": rooms[5].id,
            "username": "Linda Martinez",
            "email": "linda@example.com",
            "comment": "Luxury experience! Worth every penny. Unforgettable!",
            "rating": 5.0,
            "status": 1,
        },
    ]
    
    for rating_data in ratings_data:
        rating = models.RoomRating(**rating_data)
        db.add(rating)
    
    db.commit()
    print(f"✓ Seeded {len(ratings_data)} room ratings successfully!")


def seed_bookings(db: Session) -> None:
    """Populate sample bookings"""
    
    # Check if bookings already exist
    existing_bookings = db.query(models.Booking).first()
    if existing_bookings:
        print("Bookings already exist in database, skipping bookings seeding...")
        return
    
    rooms = db.query(models.Room).all()
    if not rooms:
        print("No rooms found, cannot seed bookings...")
        return
    
    bookings_data = [
        {
            "room_id": str(rooms[0].id),
            "name": "John Smith",
            "email": "john@example.com",
            "phone": "+1-555-0101",
            "total_price": 597.00,
            "status": "confirmed",
            "start_date": "2026-04-01",
            "end_date": "2026-04-03",
        },
        {
            "room_id": str(rooms[1].id),
            "name": "Sarah Johnson",
            "email": "sarah@example.com",
            "phone": "+1-555-0102",
            "total_price": 498.00,
            "status": "confirmed",
            "start_date": "2026-04-05",
            "end_date": "2026-04-07",
        },
        {
            "room_id": str(rooms[2].id),
            "name": "Mike Davis",
            "email": "mike@example.com",
            "phone": "+1-555-0103",
            "total_price": 447.00,
            "status": "waiting",
            "start_date": "2026-04-10",
            "end_date": "2026-04-13",
        },
        {
            "room_id": str(rooms[3].id),
            "name": "Emily Rodriguez",
            "email": "emily@example.com",
            "phone": "+1-555-0104",
            "total_price": 1396.00,
            "status": "confirmed",
            "start_date": "2026-04-15",
            "end_date": "2026-04-19",
        },
    ]
    
    for booking_data in bookings_data:
        booking = models.Booking(**booking_data)
        db.add(booking)
    
    db.commit()
    print(f"✓ Seeded {len(bookings_data)} bookings successfully!")


def seed_gallery(db: Session) -> None:
    """Populate sample gallery images"""
    
    # Check if gallery already exists
    existing_gallery = db.query(models.Gallary).first()
    if existing_gallery:
        print("Gallery already exists in database, skipping gallery seeding...")
        return
    
    gallery_data = [
        {
            "image": "/gallary/hotel-exterior.jpg",
        },
        {
            "image": "/gallary/lobby.jpg",
        },
        {
            "image": "/gallary/restaurant.jpg",
        },
        {
            "image": "/gallary/pool.jpg",
        },
        {
            "image": "/gallary/gym.jpg",
        },
        {
            "image": "/gallary/conference-room.jpg",
        },
        {
            "image": "/gallary/spa.jpg",
        },
        {
            "image": "/gallary/beach.jpg",
        },
    ]
    
    for image_data in gallery_data:
        gallery = models.Gallary(**image_data)
        db.add(gallery)
    
    db.commit()
    print(f"✓ Seeded {len(gallery_data)} gallery images successfully!")


def seed_contacts(db: Session) -> None:
    """Populate sample contact submissions"""
    
    # Check if contacts already exist
    existing_contacts = db.query(models.Contact).first()
    if existing_contacts:
        print("Contacts already exist in database, skipping contacts seeding...")
        return
    
    contacts_data = [
        {
            "name": "Robert Thompson",
            "email": "robert@example.com",
            "phone": "+1-555-0201",
            "message": "I'm interested in booking a suite for my honeymoon. Can you provide more information about special packages?",
        },
        {
            "name": "Jennifer Lee",
            "email": "jennifer@example.com",
            "phone": "+1-555-0202",
            "message": "Great service! Your staff was very helpful. Looking forward to staying again.",
        },
        {
            "name": "Christopher Brown",
            "email": "chris@example.com",
            "phone": "+1-555-0203",
            "message": "Do you have any corporate group rates available for 25-30 people?",
        },
        {
            "name": "Jessica White",
            "email": "jessica@example.com",
            "phone": "+1-555-0204",
            "message": "Excellent experience. The ocean view from my room was stunning!",
        },
    ]
    
    for contact_data in contacts_data:
        contact = models.Contact(**contact_data)
        db.add(contact)
    
    db.commit()
    print(f"✓ Seeded {len(contacts_data)} contact submissions successfully!")


def main() -> None:
    """Main function to seed all data"""
    db = SessionLocal()
    try:
        print("\n🌱 Starting database seeding...\n")
        seed_rooms(db)
        seed_ratings(db)
        seed_bookings(db)
        seed_gallery(db)
        seed_contacts(db)
        print("\n✅ Database seeding completed successfully!\n")
    except Exception as e:
        print(f"\n❌ Error during seeding: {e}\n")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
