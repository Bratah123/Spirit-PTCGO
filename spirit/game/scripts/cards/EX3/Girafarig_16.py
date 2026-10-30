"""STUB: effect not implemented — do not guess mechanics.
Girafarig (EX3 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import synchronized_search, breaking_impact

card = PokemonCardDef(
    guid="996f1f82-8b41-5892-a456-d7bb960e0310",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="EX3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Attack(
            title="Synchronized Search",
            game_text="If Girafarig and the Defending Pok\u00e9mon have the same amount of Energy attached to them, pick any 1 card from your deck and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=synchronized_search(),
        ),
        Attack(
            title="Breaking Impact",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage for each Colorless Energy in that Pok\u00e9mon's Retreat Cost to that Pok\u00e9mon (after applying effects to the Retreat Cost). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=breaking_impact(10),
        ),
    ],
)