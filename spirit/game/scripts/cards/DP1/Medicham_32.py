"""STUB: effect not implemented — do not guess mechanics.
Medicham (DP1 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import force_palm
from spirit.game.card_effects.dp import recoil_attack

card = PokemonCardDef(
    guid="acde35fa-74fb-5657-bd8d-ea7226687cdb",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Force Palm",
            game_text="Count the number of damage counters on Medicham. Put that many damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=force_palm(),
        ),
        Attack(
            title="Spinning Kick",
            game_text="Medicham does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=recoil_attack(20),
        ),
    ],
)