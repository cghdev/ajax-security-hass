#!/usr/bin/env python3
"""Debug script to identify unknown device types in Ajax system.

This script will:
1. Connect to Ajax API
2. List all devices and their raw type strings
3. Identify which types are not mapped in the integration
"""
import asyncio
import json
import os
import sys
from collections import Counter

# Add parent directory to path to import custom_components
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from custom_components.ajax.api import AjaxApi
from custom_components.ajax.coordinator import AjaxDataCoordinator
from custom_components.ajax.models import DeviceType


async def main():
    """Main function to debug unknown devices."""
    email = os.environ.get("AJAX_EMAIL")
    password = os.environ.get("AJAX_PASSWORD")

    if not email or not password:
        print("Please set AJAX_EMAIL and AJAX_PASSWORD environment variables")
        print("Example: AJAX_EMAIL=your@email.com AJAX_PASSWORD=yourpass python3 debug_unknown_devices.py")
        sys.exit(1)

    print(f"Connecting to Ajax API as {email}...")

    api = AjaxApi(email, password)

    try:
        # Login
        print("Logging in...")
        await api.login()
        print("✓ Login successful\n")

        # Get account info
        print("Fetching account information...")
        account = await api.get_account()
        print(f"✓ Account: {account.name} ({account.email})")
        print(f"✓ Found {len(account.spaces)} space(s)\n")

        all_device_types = []
        unknown_device_types = []
        device_type_examples = {}

        for space_id, space in account.spaces.items():
            print(f"\n{'='*80}")
            print(f"Space: {space.name} (ID: {space_id})")
            print(f"{'='*80}")
            print(f"Total devices: {len(space.devices)}\n")

            for device_id, device in space.devices.items():
                # Get raw type from device attributes or states
                raw_type = "unknown"
                if "device_type" in device.attributes:
                    raw_type = device.attributes["device_type"]
                elif device.device_marketing_id:
                    raw_type = device.device_marketing_id

                all_device_types.append(raw_type)

                # Check if device is unknown
                if device.type == DeviceType.UNKNOWN:
                    unknown_device_types.append(raw_type)
                    if raw_type not in device_type_examples:
                        device_type_examples[raw_type] = {
                            "name": device.name,
                            "id": device.id,
                            "has_battery": device.has_battery,
                            "signal_strength": device.signal_strength is not None,
                            "attributes": list(device.attributes.keys()),
                            "states": device.states,
                        }

                    print(f"⚠️  UNKNOWN: {device.name}")
                    print(f"   Device ID: {device.id}")
                    print(f"   Raw type: {raw_type}")
                    print(f"   Marketing ID: {device.device_marketing_id}")
                    print(f"   Has battery: {device.has_battery}")
                    print(f"   Signal strength: {device.signal_strength is not None}")
                    print(f"   Attributes: {list(device.attributes.keys())}")
                    print(f"   States: {device.states}")
                    print()
                else:
                    print(f"✓  {device.type.value:20} - {device.name}")

        # Summary
        print(f"\n{'='*80}")
        print("SUMMARY")
        print(f"{'='*80}\n")

        print("All device type distribution:")
        type_counts = Counter(all_device_types)
        for device_type, count in type_counts.most_common():
            print(f"  {device_type:30} : {count}")

        print(f"\n{'='*80}")
        print(f"Unknown devices: {len(unknown_device_types)}")
        print(f"{'='*80}\n")

        if unknown_device_types:
            print("Unknown device type distribution:")
            unknown_counts = Counter(unknown_device_types)
            for device_type, count in unknown_counts.most_common():
                print(f"  {device_type:30} : {count}")

            print(f"\n{'='*80}")
            print("Example devices for each unknown type:")
            print(f"{'='*80}\n")

            print(json.dumps(device_type_examples, indent=2))

            # Save to file
            output_file = "ajax_unknown_devices.json"
            with open(output_file, "w") as f:
                json.dump(device_type_examples, f, indent=2)
            print(f"\n✓ Saved detailed information to {output_file}")
        else:
            print("✓ No unknown devices found!")

    except Exception as err:
        print(f"\n❌ Error: {err}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
