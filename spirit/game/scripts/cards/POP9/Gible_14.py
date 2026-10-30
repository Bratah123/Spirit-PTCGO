"""Gible (POP9 #14)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="998ff4b9-f984-5c04-9289-b2ed62c2f520",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic", "Gible"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=443,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=gust_attack(opponent_chooses=True)
        ),
    ]
)