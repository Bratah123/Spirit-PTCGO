from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    delivery_dash,
)

card = PokemonCardDef(
    guid="58f360e3-44b7-5db3-bfc5-74d591461a37",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic", "Blitzle"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=522,
    abilities=[
        Attack(
            title="Delivery Dash",
            game_text="Search your deck for up to 2 Electropower cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=delivery_dash,
        ),
        Attack(
            title="Zap Kick",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)