from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.content.definitions import def_for


def _named(pokemon, name):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return getattr(d, "display_name", "") == name


card = PokemonCardDef(
    guid="32070912-a6b7-5962-b225-d10897c0f58b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=58,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Lovestrike",
            game_text="Does 40 more damage for each Nidoqueen on your Bench.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(lambda ctx: sum(1 for p in ctx.my_bench() if _named(p, "Nidoqueen")), 40, base=20),
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)