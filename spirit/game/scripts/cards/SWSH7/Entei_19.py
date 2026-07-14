from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, recoil_attack


def _single_strike_bench_counters(ctx) -> int:
    total = 0
    for p in ctx.my_bench():
        if "Single Strike" in subtypes_for(p.archetype_id):
            total += max(0, (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10)
    return total

card = PokemonCardDef(
    guid="3a9f71bb-13e7-5436-ba45-d6fdbf7b0128",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Single Strike", "Entei"],
    subtypes=["Basic", "Single Strike"],
    collector_number=19,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Angry Fang",
            game_text="This attack does 10 damage for each damage counter on all of your Benched Single Strike Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(_single_strike_bench_counters, 10),
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)