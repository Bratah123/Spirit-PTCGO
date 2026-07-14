from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_energy

_ENERGY_ON_SELF = count_energy("self")


def _has_extra_energy(ctx) -> bool:
    total_cost = sum(ctx.ability.cost.values())
    return _ENERGY_ON_SELF(ctx) > total_cost


card = PokemonCardDef(
    guid="1ac0697d-0170-5fc3-b035-8f31594901c1",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic", "Stonjourner"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Power Press",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached (in addition to this attack's cost), this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_has_extra_energy, 60),
        ),
    ],
)