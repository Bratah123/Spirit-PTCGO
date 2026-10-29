from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    grandiose_fangs,
)

card = PokemonCardDef(
    guid="b3f09071-ba2f-5cc1-888f-a0f8f395d987",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic", "Sandile"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=551,
    abilities=[
        Attack(
            title="Grandiose Fangs",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, this Pok\u00e9mon's attacks do 120 more damage to your opponent's Active Pok\u00e9mon during your next turn (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=grandiose_fangs
        ),
    ],
)