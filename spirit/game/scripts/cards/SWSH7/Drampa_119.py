from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _bench_has_damage(ctx) -> bool:
    return any(p.get_attribute(AttrID.HP, ctx.max_hp(p)) < ctx.max_hp(p)
               for p in ctx.my_bench())

card = PokemonCardDef(
    guid="77f90310-be17-567d-89c3-bda9e52036b2",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=780,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Berserk",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_bench_has_damage, 90),
        ),
    ],
)