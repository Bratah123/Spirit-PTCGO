from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


def _lunatone_on_bench(ctx):
    return any(getattr(def_for(p.archetype_id), "display_name", None) == "Lunatone"
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="b5286690-9511-5749-805e-e60210ab82a0",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Attack(
            title="Cosmic Spin",
            game_text="If Lunatone is on your Bench, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_lunatone_on_bench, 30, base=10),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)