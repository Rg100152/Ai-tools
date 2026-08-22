#!/usr/bin/env python3
"""
Favorites Manager for AI Tools Launcher
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class FavoritesManager:
    def __init__(self, filepath="favorites.json"):
        self.filepath = filepath
        self.favorites_data = self.load_favorites()
    
    def load_favorites(self) -> Dict:
        """Load favorites from JSON file"""
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Create default structure
            default = {
                "version": "1.0.0",
                "last_updated": datetime.now().isoformat(),
                "total_favorites": 0,
                "favorites": [],
                "collections": {},
                "statistics": {},
                "sync": {},
                "backup": {}
            }
            self.save_favorites(default)
            return default
        except json.JSONDecodeError:
            print("Error: Invalid JSON in favorites file")
            return {}
    
    def save_favorites(self, data: Optional[Dict] = None) -> bool:
        """Save favorites to JSON file"""
        if data:
            self.favorites_data = data
        try:
            self.favorites_data["last_updated"] = datetime.now().isoformat()
            self.favorites_data["total_favorites"] = len(self.favorites_data.get("favorites", []))
            with open(self.filepath, 'w') as f:
                json.dump(self.favorites_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving favorites: {e}")
            return False
    
    def add_favorite(self, tool_data: Dict) -> bool:
        """Add a tool to favorites"""
        favorites = self.favorites_data.get("favorites", [])
        
        # Check if already exists
        if any(fav["id"] == tool_data["id"] for fav in favorites):
            print(f"Tool {tool_data['name']} already in favorites!")
            return False
        
        # Add metadata
        tool_data["date_added"] = datetime.now().isoformat()
        tool_data["last_used"] = None
        tool_data["use_count"] = 0
        tool_data["personal_rating"] = 0
        tool_data["notes"] = ""
        tool_data["custom_tags"] = []
        tool_data["is_pinned"] = False
        tool_data["pin_order"] = None
        
        favorites.append(tool_data)
        return self.save_favorites()
    
    def remove_favorite(self, tool_id: int) -> bool:
        """Remove a tool from favorites"""
        favorites = self.favorites_data.get("favorites", [])
        self.favorites_data["favorites"] = [fav for fav in favorites if fav["id"] != tool_id]
        return self.save_favorites()
    
    def toggle_favorite(self, tool_data: Dict) -> bool:
        """Toggle favorite status"""
        favorites = self.favorites_data.get("favorites", [])
        if any(fav["id"] == tool_data["id"] for fav in favorites):
            return self.remove_favorite(tool_data["id"])
        else:
            return self.add_favorite(tool_data)
    
    def get_favorite(self, tool_id: int) -> Optional[Dict]:
        """Get a specific favorite by ID"""
        for fav in self.favorites_data.get("favorites", []):
            if fav["id"] == tool_id:
                return fav
        return None
    
    def get_all_favorites(self) -> List[Dict]:
        """Get all favorites"""
        return self.favorites_data.get("favorites", [])
    
    def get_pinned_favorites(self) -> List[Dict]:
        """Get pinned favorites"""
        favorites = self.get_all_favorites()
        pinned = [fav for fav in favorites if fav.get("is_pinned", False)]
        return sorted(pinned, key=lambda x: x.get("pin_order", 999))
    
    def update_usage(self, tool_id: int) -> bool:
        """Update usage statistics"""
        fav = self.get_favorite(tool_id)
        if fav:
            fav["use_count"] = fav.get("use_count", 0) + 1
            fav["last_used"] = datetime.now().isoformat()
            return self.save_favorites()
        return False
    
    def set_rating(self, tool_id: int, rating: int) -> bool:
        """Set personal rating for a tool"""
        if 1 <= rating <= 5:
            fav = self.get_favorite(tool_id)
            if fav:
                fav["personal_rating"] = rating
                return self.save_favorites()
        return False
    
    def add_note(self, tool_id: int, note: str) -> bool:
        """Add note to a favorite"""
        fav = self.get_favorite(tool_id)
        if fav:
            fav["notes"] = note
            return self.save_favorites()
        return False
    
    def pin_favorite(self, tool_id: int) -> bool:
        """Pin a favorite to top"""
        fav = self.get_favorite(tool_id)
        if fav:
            fav["is_pinned"] = True
            # Set pin order
            pinned = self.get_pinned_favorites()
            fav["pin_order"] = len(pinned) + 1
            return self.save_favorites()
        return False
    
    def unpin_favorite(self, tool_id: int) -> bool:
        """Unpin a favorite"""
        fav = self.get_favorite(tool_id)
        if fav:
            fav["is_pinned"] = False
            fav["pin_order"] = None
            return self.save_favorites()
        return False
    
    def create_collection(self, name: str, description: str = "", icon: str = "📁") -> bool:
        """Create a new collection"""
        collections = self.favorites_data.get("collections", {})
        if name not in collections:
            collections[name] = {
                "name": name,
                "description": description,
                "icon": icon,
                "tool_ids": []
            }
            self.favorites_data["collections"] = collections
            return self.save_favorites()
        return False
    
    def add_to_collection(self, collection_name: str, tool_id: int) -> bool:
        """Add tool to collection"""
        collections = self.favorites_data.get("collections", {})
        if collection_name in collections:
            if tool_id not in collections[collection_name]["tool_ids"]:
                collections[collection_name]["tool_ids"].append(tool_id)
                self.favorites_data["collections"] = collections
                return self.save_favorites()
        return False
    
    def remove_from_collection(self, collection_name: str, tool_id: int) -> bool:
        """Remove tool from collection"""
        collections = self.favorites_data.get("collections", {})
        if collection_name in collections:
            if tool_id in collections[collection_name]["tool_ids"]:
                collections[collection_name]["tool_ids"].remove(tool_id)
                self.favorites_data["collections"] = collections
                return self.save_favorites()
        return False
    
    def search_favorites(self, query: str) -> List[Dict]:
        """Search through favorites"""
        query = query.lower()
        results = []
        for fav in self.get_all_favorites():
            if (query in fav["name"].lower() or 
                query in fav["type"].lower() or 
                query in fav.get("description", "").lower() or
                any(query in tag.lower() for tag in fav.get("tags", []))):
                results.append(fav)
        return results
    
    def get_statistics(self) -> Dict:
        """Get usage statistics"""
        favorites = self.get_all_favorites()
        total_use = sum(fav.get("use_count", 0) for fav in favorites)
        avg_rating = sum(fav.get("personal_rating", 0) for fav in favorites) / len(favorites) if favorites else 0
        
        stats = {
            "total_favorites": len(favorites),
            "total_use_count": total_use,
            "average_rating": round(avg_rating, 1),
            "pinned_count": len(self.get_pinned_favorites()),
            "collections_count": len(self.favorites_data.get("collections", {}))
        }
        
        self.favorites_data["statistics"] = stats
        self.save_favorites()
        return stats

# Usage Example
if __name__ == "__main__":
    fm = FavoritesManager()
    
    # Add favorite
    tool = {
        "id": 1,
        "name": "ChatGPT",
        "url": "https://chat.openai.com",
        "type": "Chat Assistant",
        "price": "Free/Paid",
        "description": "OpenAI's flagship AI chatbot"
    }
    fm.add_favorite(tool)
    
    # Get all favorites
    favorites = fm.get_all_favorites()
    print(f"Total favorites: {len(favorites)}")
    
    # Update usage
    fm.update_usage(1)
    
    # Set rating
    fm.set_rating(1, 5)
    
    # Pin favorite
    fm.pin_favorite(1)
    
    # Create collection
    fm.create_collection("daily_use", "Daily use tools", "⚡")
    
    # Add to collection
    fm.add_to_collection("daily_use", 1)
    
    # Get statistics
    stats = fm.get_statistics()
    print(f"Statistics: {stats}")
