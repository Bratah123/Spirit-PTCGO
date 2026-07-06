from typing import Dict, List, Any, Optional

ZERO_GUID = "00000000-0000-0000-0000-000000000000"


def _card_guids():
    """Lowercase GUIDs of every loaded card (cached loader)."""
    try:
        from spirit.game.scripts.cards import loader as card_loader
        return {c.guid.lower() for c in card_loader.load_all()}
    except Exception:
        return set()


class Reward:
    """Represents a universal reward object (equivalent to client class A.N)."""
    def __init__(
        self, 
        name: str, 
        reward_type: str, 
        reward_amount: int, 
        reward_product_id: Optional[str] = None, 
        reward_currency: Optional[str] = None,
        reward_description: Optional[Dict[str, Any]] = None,
        reward_reason: Optional[str] = None
    ):
        self.name = name
        self.reward_type = reward_type
        self.reward_amount = reward_amount
        self.reward_product_id = reward_product_id
        self.reward_currency = reward_currency
        self.reward_description = reward_description
        self.reward_reason = reward_reason

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Reward':
        return cls(
            name=data.get("name", ""),
            reward_type=data.get("rewardType", "Tokens"),
            reward_amount=data.get("rewardAmount", 0),
            reward_product_id=data.get("rewardProductID"),
            reward_currency=data.get("rewardCurrency"),
            reward_description=data.get("rewardDescription"),
            reward_reason=data.get("rewardReason")
        )

    def to_dict(self, index: int = 0) -> Dict[str, Any]:
        # rewardProductID must be null when there is no product: the client
        # chevron renderers get_Item a non-null ArchetypeID (even Guid.Empty)
        # against the archetype cache unguarded — KeyNotFoundException.
        product_id = self.reward_product_id or ""
        return {
            "name": self.name,
            "rewardType": self.reward_type,
            "rewardAmount": self.reward_amount,
            "rewardProductID": product_id if product_id and product_id != ZERO_GUID else None,
            "rewardCurrency": self.reward_currency or "",
            "rewardDescription": self.reward_description or {"id": ""},
            "rewardReason": self.reward_reason or "",
            "index": index
        }


class VersusTier:
    """Represents a point tier within a Versus Season (client class V.u)."""
    def __init__(self, rewards: Dict[int, List[Reward]]):
        self.rewards = rewards

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'VersusTier':
        raw_rewards = data.get("rewards", {})
        rewards = {}
        for pts_str, reward_list in raw_rewards.items():
            try:
                pts = int(pts_str)
            except ValueError:
                pts = 0
            rewards[pts] = [Reward.from_dict(r) for r in reward_list]
        return cls(rewards=rewards)

    @staticmethod
    def _display_order(rewards: List[Reward]) -> List[Reward]:
        """Cards first, then products, tokens last — the client sorts by "index"
        and dereferences reward[0]'s archetype unguarded (cards get the fan render)."""
        cards = _card_guids()

        def rank(r: Reward) -> int:
            guid = (r.reward_product_id or "").lower()
            if not guid or guid == ZERO_GUID:
                return 2
            return 0 if guid in cards else 1

        return sorted(rewards, key=rank)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rewards": {
                str(pts): [r.to_dict(index=i)
                           for i, r in enumerate(self._display_order(r_list))]
                for pts, r_list in self.rewards.items()
            }
        }


class VersusSeason:
    """Represents a Versus Season configuration."""
    def __init__(
        self, 
        season_id: str, 
        start_time: int, 
        end_time: int, 
        description: Dict[str, Any], 
        tiers: List[VersusTier], 
        reset_reward_id: str = ""
    ):
        self.season_id = season_id
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.tiers = tiers
        self.reset_reward_id = reset_reward_id

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'VersusSeason':
        return cls(
            season_id=data.get("seasonID", ""),
            start_time=data.get("startTime", 0),
            end_time=data.get("endTime", 0),
            description=data.get("description", {"id": "SpiritPTCGO Season"}),
            tiers=[VersusTier.from_dict(t) for t in data.get("tiers", [])],
            reset_reward_id=data.get("resetRewardID", "")
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "seasonID": self.season_id,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "description": self.description,
            "tiers": [t.to_dict() for t in self.tiers],
            "resetRewardID": self.reset_reward_id
        }
