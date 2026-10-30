"""STUB: effect not implemented — do not guess mechanics.
Gyarados (EX3 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_resistance_attack
from spirit.game.card_effects.ex import dragon_crush


card = PokemonCardDef(
    guid="935bd8aa-42fa-5ace-b2b8-3d3f34479bcf",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Dragon Crush",
            game_text="Flip a coin. If heads, this attack does 10 damage to each Defending Pok\u00e9mon. Discard an Energy card from each Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=dragon_crush(10),
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=80,
            # STUB: attack effect not implemented
            effect=ignore_resistance_attack(),
        ),
    ],
)