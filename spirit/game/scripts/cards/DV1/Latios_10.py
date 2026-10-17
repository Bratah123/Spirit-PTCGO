from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _latias_on_bench(ctx):
    return any(
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Latias"
        for p in ctx.my_bench()
    )


card = PokemonCardDef(
    guid="c4f94ed4-0e9e-5089-b43f-91259841d0f4",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=381,
    abilities=[
        Attack(
            title="Sky Blade",
            game_text="If Latias is on your Bench, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_latias_on_bench, 20),
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
