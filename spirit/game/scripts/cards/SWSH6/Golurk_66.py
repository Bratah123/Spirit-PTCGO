from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_tool, recoil_attack


def _has_own_tool(ctx):
    return has_tool(ctx.attacker)


card = PokemonCardDef(
    guid="da80fa47-56a8-5986-bc3a-8c23af8a9347",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Reinforced Punch",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_has_own_tool, 90),
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=recoil_attack(30),
        ),
    ],
)