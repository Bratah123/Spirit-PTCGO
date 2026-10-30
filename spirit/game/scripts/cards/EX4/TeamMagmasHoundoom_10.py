"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Houndoom (EX4 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import magma_spurt
from spirit.game.card_effects.attacks_common import bonus_if, defender_has_condition

card = PokemonCardDef(
    guid="34e6f5e2-679b-5143-9d81-3bcf8aec7f07",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundoom.Name",
    display_name="Team Magma's Houndoom",
    searchable_by=["Team Magma's Houndoom", "Stage 1", "TeamMagmasHoundoom"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If the Defending Pok\u00e9mon is Burned, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(defender_has_condition(SpecialConditions.BURNED), 20),
        ),
        Attack(
            title="Magma Spurt",
            game_text="Discard the top 5 cards from your deck. This attack does 30 damage times the number of Fire and Fighting basic Energy cards discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=magma_spurt(),
        ),
    ],
)