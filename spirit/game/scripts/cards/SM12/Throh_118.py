from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _bench_has_damage(ctx) -> bool:
    return any(p.get_attribute(AttrID.HP, ctx.max_hp(p)) < ctx.max_hp(p)
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="ddcd5658-1aa7-58c2-998e-c21f725d3489",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic", "Throh"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Reverse Shoulder Throw",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_bench_has_damage, 90),
        ),
    ],
)