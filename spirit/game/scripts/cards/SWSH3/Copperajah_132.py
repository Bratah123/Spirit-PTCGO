from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import condition_immunity_passive


def _bench_damaged(ctx) -> bool:
    return any(
        p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p) for p in ctx.my_bench()
    )


card = PokemonCardDef(
    guid="5e272b8d-b1dd-52f8-ae29-9cb4afc5952d",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1", "Copperajah"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Ability(
            title="Antibacterial Skin",
            game_text="This Pok\u00e9mon can't be affected by any Special Conditions.",
            passive=condition_immunity_passive(),
        ),
        Attack(
            title="Vengeful Stomp",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_bench_damaged, 120),
        ),
    ],
)