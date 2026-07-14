from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import bonus_if, condition_attack


def _defender_has_condition(ctx) -> bool:
    defender = ctx.defender
    return bool(defender and defender.get_attribute(AttrID.SPECIAL_CONDITIONS))


card = PokemonCardDef(
    guid="7a11ae33-16b6-5345-a421-7c8d72dd4a02",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Hex",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_defender_has_condition, 90, base=30),
        ),
        Attack(
            title="Flickering Flames",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)