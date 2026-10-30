"""STUB: effect not implemented — do not guess mechanics.
Lanturn (EX10 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import energy_stream
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="efe37608-2dbd-5850-8185-ba4d2e05c620",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Search your discard pile for a basic Energy card and attach it to Lanturn.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=energy_stream(),
        ),
        Attack(
            title="Take Down",
            game_text="Lanturn does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=recoil_attack(10),
        ),
    ],
)