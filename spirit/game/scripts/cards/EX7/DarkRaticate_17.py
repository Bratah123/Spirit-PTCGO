from spirit.game.card_effects.ex import spread_poison, dark_seed
"""STUB: effect not implemented — do not guess mechanics.
Dark Raticate (EX7 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ec4f23d-8ff9-56a0-9d35-77691dc8e8bb",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkRaticate.Name",
    display_name="Dark Raticate",
    searchable_by=["Dark Raticate", "Stage 1", "DarkRaticate"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Dark Seed",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn. Put 5 damage counters on the Defending Pok\u00e9mon at the end of your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=dark_seed(),
        ),
        Attack(
            title="Spread Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned. This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            # STUB: attack effect not implemented
            effect=spread_poison(),
        ),
    ],
)