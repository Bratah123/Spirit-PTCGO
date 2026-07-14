from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if, damage_all_opponents


def _magmortar_bench_damaged(ctx) -> bool:
    for p in ctx.my_bench():
        if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Magmortar" \
                and p.get_attribute(AttrID.HP, ctx.max_hp(p)) < ctx.max_hp(p):
            return True
    return False

card = PokemonCardDef(
    guid="9dbb9c63-3178-59b6-8f77-653b43c1d4d2",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Explosive Bolt",
            game_text="If any of your Benched Magmortar have any damage counters on them, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_magmortar_bench_damaged, 90),
        ),
        Attack(
            title="High-Voltage Current",
            game_text="This attack does 50 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(50),
        ),
    ],
)