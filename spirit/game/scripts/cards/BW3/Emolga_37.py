from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _has_lightning_bench(ctx) -> bool:
    return any(
        PokemonTypes.LIGHTNING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
        for p in ctx.my_bench()
    )


card = PokemonCardDef(
    guid="9efc152e-f8a6-5014-a5f9-5b05c4d680b1",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga", "Basic", "Emolga"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=587,
    abilities=[
        Attack(
            title="Electrichain",
            game_text="Does 20 more damage if you have any Lightning Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_has_lightning_bench, 20),
        ),
    ],
)
