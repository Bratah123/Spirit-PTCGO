"""STUB: effect not implemented — do not guess mechanics.
Tyranitar (XY10 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="abc94f0b-1003-5b62-9167-a8be94fcf646",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Raging Roar",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may attach 1 Darkness Energy from your discard pile to this Pok\u00e9mon for each Prize card your opponent has taken.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Mountain",
            game_text="Discard the top 2 cards of your deck. This attack does 50 more damage for each Supporter card discarded in this way.",
            cost={PokemonTypes.DARKNESS: 5},
            damage=150,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)