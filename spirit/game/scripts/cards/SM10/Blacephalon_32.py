from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    blazer,
    fireball_circus,
)

card = PokemonCardDef(
    guid="1402ef31-b7da-517d-a2c7-e8020c2e1d2a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blacephalon.Name",
    display_name="Blacephalon",
    searchable_by=["Blacephalon", "Basic", "Ultra Beast", "Blacephalon"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=32,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=806,
    abilities=[
        Attack(
            title="Blazer",
            game_text="Turn 1 of your face-down Prize cards face up. If it's a Fire Energy card, this attack does 50 more damage. (That Prize card remains face up for the rest of the game.)",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=blazer
        ),
        Attack(
            title="Fireball Circus",
            game_text="Discard any number of Fire Energy cards from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            damage_operator="x",
            effect=fireball_circus
        ),
    ],
)