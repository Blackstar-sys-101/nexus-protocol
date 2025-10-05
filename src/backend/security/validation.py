

"""
NEXUS PROTOCOL - COORDINATION SECURITY
Validating inputs for meta-coordination systems
"""

class NexusValidator:
    """
    Security validation specifically for coordination protocols
    """
    
    @staticmethod
    def validate_system_identifier(system_id: str) -> str:
        """
        Validate system identifiers in coordination protocols
        Why? We need to trust which systems are participating
        """
        if not isinstance(system_id, str):
            raise ValueError("System identifier must be a string")
            
        cleaned_id = system_id.strip()
        
        # System IDs should be specific format
        if len(cleaned_id) < 3 or len(cleaned_id) > 64:
            raise ValueError("System identifier must be 3-64 characters")
            
        # Only allow safe characters
        if not all(c.isalnum() or c in '.-_' for c in cleaned_id):
            raise ValueError("System identifier contains invalid characters")
            
        return cleaned_id
    
    @staticmethod
    def validate_coordination_message(message: str) -> str:
        """
        Validate messages between coordinating systems
        Why? Prevent injection in coordination logic
        """
        if not isinstance(message, str):
            raise ValueError("Coordination message must be a string")
            
        cleaned = message.strip()
        
        # Reasonable message size for coordination
        if len(cleaned) > 4096:  # 4KB max for coordination messages
            raise ValueError("Coordination message too large")
            
        if len(cleaned) == 0:
            raise ValueError("Coordination message cannot be empty")
            
        # Block common attack patterns
        dangerous_patterns = ["<script", "javascript:", "<?php", "exec("]
        for pattern in dangerous_patterns:
            if pattern in cleaned.lower():
                raise SecurityError(f"Dangerous pattern detected: {pattern}")
                
        return cleaned
    
    @staticmethod
    def validate_resource_allocation(amount: int) -> int:
        """
        Validate resource allocation amounts
        Why? Prevent resource exhaustion attacks
        """
        if not isinstance(amount, int):
            raise ValueError("Resource amount must be an integer")
            
        # Reasonable bounds for resource allocation
        if amount < 0:
            raise ValueError("Resource amount cannot be negative")
            
        if amount > 1000000:  # Prevent ridiculously large allocations
            raise ValueError("Resource amount too large")
            
        return amount


class SecurityError(Exception):
    """Nexus Protocol security violation"""
    pass


# Test with Nexus-specific scenarios
if __name__ == "__main__":
    print("🧪 NEXUS PROTOCOL SECURITY TESTING")
    print("=" * 50)
    
    validator = NexusValidator()
    
    # Test cases relevant to coordination protocols
    test_cases = [
        # (input, validator_method, description)
        ("auth-system-01", validator.validate_system_identifier, "Valid system ID"),
        ("invalid@system", validator.validate_system_identifier, "Invalid system ID"),
        ("coordination decision: allocate resources", validator.validate_coordination_message, "Valid coordination message"),
        ("<script>alert('xss')</script>", validator.validate_coordination_message, "Dangerous message"),
        (500, validator.validate_resource_allocation, "Valid resource allocation"),
        (-100, validator.validate_resource_allocation, "Negative resources"),
    ]
    
    for test_input, validator_method, description in test_cases:
        print(f"\n📝 {description}:")
        try:
            result = validator_method(test_input)
            print(f"   ✅ PASS: {result}")
        except (ValueError, SecurityError) as e:
            print(f"   🛡️ BLOCKED: {e}")