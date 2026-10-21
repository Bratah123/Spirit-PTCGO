from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


def _named(card, *names):
    d = def_for(card.archetype_id)
    return getattr(d, "display_name", None) in names


card = PokemonCardDef(
    guid="b808a4cf-540f-528b-82ed-f44800402c15",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1", "Magmortar"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=126,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=search_attach_energy(predicate=_is_fire_energy, count=1, to_self=True),
        ),
        Attack(
            title="Twin Bursts",
            game_text="If Electivire is on your Bench, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(_named(p, "Electivire") for p in ctx.my_bench()), 80),
        ),
    ],
)