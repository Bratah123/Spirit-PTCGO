from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    zzzap_touch,
)

card = PokemonCardDef(
    guid="bcbe5ff3-489a-5e5c-8f8b-ecce0bb04940",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title="Zzzap Touch",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=zzzap_touch
        ),
    ],
)