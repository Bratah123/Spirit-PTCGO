"""STUB: effect not implemented — do not guess mechanics.
Armaldo ex (POP1 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import double_wing_attack
from spirit.game.card_effects.attacks_common import ignore_resistance_attack


card = PokemonCardDef(
    guid="65ce4f3b-c94e-5846-805f-cdc91de7afc3",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldoex.Name",
    display_name="Armaldo ex",
    searchable_by=["Armaldo ex", "Stage 2", "ex", "Armaldoex"],
    subtypes=["Stage 2", "ex"],
    collector_number=16,
    set_code="POP1",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=348,
    abilities=[
        Attack(
            title="Twin-blade",
            game_text="Does 30 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=double_wing_attack(),
        ),
        Attack(
            title="Supersonic Claws",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=ignore_resistance_attack(),
        ),
    ],
)