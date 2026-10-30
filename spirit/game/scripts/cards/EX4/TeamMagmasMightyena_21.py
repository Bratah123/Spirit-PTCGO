"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Mightyena (EX4 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import bonus_if_ex


card = PokemonCardDef(
    guid="cd8c2682-df42-51c8-8041-a5e316f4eaf2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasMightyena.Name",
    display_name="Team Magma's Mightyena",
    searchable_by=["Team Magma's Mightyena", "Stage 1", "TeamMagmasMightyena"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Overrun",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=snipe_attack(10, also_base=True),
        ),
        Attack(
            title="Bite Off",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 40 damage plus 40 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if_ex(40),
        ),
    ],
)