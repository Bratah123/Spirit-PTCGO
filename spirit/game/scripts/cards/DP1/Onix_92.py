"""STUB: effect not implemented — do not guess mechanics.
Onix (DP1 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import tunneling


card = PokemonCardDef(
    guid="cf643baa-5981-5b3d-a2b8-54acc3fc19fe",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Tunneling",
            game_text="Choose up to 2 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Onix can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=tunneling(),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)