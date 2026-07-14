from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_in_play


def _is_rapid_strike(pokemon):
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


card = PokemonCardDef(
    guid="1dcd2998-5a26-54f6-9755-276cd53b7e23",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifu.Name",
    display_name="Rapid Strike Urshifu",
    searchable_by=["Rapid Strike Urshifu", "Stage 1", "Rapid Strike", "RapidStrikeUrshifu"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=44,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kubfu.Name",
    family_id=891,
    abilities=[
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Rapid-Fisted Rush",
            game_text="This attack does 30 damage for each of your Rapid Strike Pok\u00e9mon in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play(side="mine", pred=_is_rapid_strike), 30),
        ),
    ],
)