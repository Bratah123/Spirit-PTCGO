from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    self_destruct,
)

card = PokemonCardDef(
    guid="64fd77a7-b873-51bb-b307-99412f31c437",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    display_name="Alolan Geodude",
    searchable_by=["Alolan Geodude", "Basic", "AlolanGeodude"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=74,
    abilities=[
        Attack(
            title="Self-Destruct",
            game_text="This Pok\u00e9mon does 60 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=self_destruct,
        ),
    ],
)