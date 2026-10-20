from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _stage2_on_bench(ctx):
    return any(p.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value for p in ctx.my_bench())


card = PokemonCardDef(
    guid="93228f57-5824-5efa-9b01-f0cc92b805be",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Powerful Friends",
            game_text="If you have any Stage 2 Pok\u00e9mon on your Bench, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_stage2_on_bench, 70, base=10),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)