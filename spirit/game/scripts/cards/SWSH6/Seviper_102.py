from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import bonus_if


def _played_single_strike_supporter(ctx) -> bool:
    def matches(record):
        archetype_id, _name, trainer_type = record
        return trainer_type == TrainerType.SUPPORTER.value \
            and "Single Strike" in subtypes_for(archetype_id)
    return ctx.played_trainer_this_turn(matches) > 0


card = PokemonCardDef(
    guid="168797c4-54f3-524c-b9f5-c3172bab5a4c",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic", "Single Strike", "Seviper"],
    subtypes=["Basic", "Single Strike"],
    collector_number=102,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=336,
    abilities=[
        Attack(
            title="Strong Tail",
            game_text="If you played a Single Strike Supporter card from your hand during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=bonus_if(_played_single_strike_supporter, 90),
        ),
    ],
)