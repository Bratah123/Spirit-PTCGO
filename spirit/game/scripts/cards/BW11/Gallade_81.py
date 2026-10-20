from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack, damage_per


def _damaged_bench(ctx):
    """Your Benched Pokemon that have any damage counters on them."""
    return sum(1 for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p))


card = PokemonCardDef(
    guid="695d73f7-1457-5965-b821-a8409ebe8bdc",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gallade.Name",
    display_name="Gallade",
    searchable_by=["Gallade", "Stage 2", "Gallade"],
    subtypes=["Stage 2"],
    collector_number=81,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Nerve Shot",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Pandemonium Blade",
            game_text="Does 20 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(_damaged_bench, 20, base=60),
        ),
    ],
)