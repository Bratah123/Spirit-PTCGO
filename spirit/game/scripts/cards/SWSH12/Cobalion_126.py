from spirit.game.card_effects.passives_common import team_damage_boost_passive
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon


def _is_darkness(pokemon) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.DARKNESS.value in types


async def follow_up(ctx):
    """30 damage. Choose up to 2 Benched Pokémon; for each, search a basic
    Energy card and attach it to that Pokémon. Then, shuffle your deck."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    picks = await ctx.choose_cards(
        bench, 2, minimum=0, prompt="Choose up to 2 of your Benched Pokémon.",
    )
    if not picks:
        return
    for target in picks:
        found = await ctx.search_deck(
            is_basic_energy_card, count=1, minimum=0,
            prompt="Choose a basic Energy card to attach.",
        )
        if found:
            await ctx.attach_energy(found[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="e7302307-c6a3-5a2b-9054-3b3128f1fd6f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic", "Cobalion"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=638,
    abilities=[
        Ability(
            title="Justified Law",
            game_text="Your Basic Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Darkness Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(
                30, attacker_pred=is_basic_pokemon, target_pred=_is_darkness,
            ),
        ),
        Attack(
            title="Follow-Up",
            game_text="Choose up to 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a basic Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=follow_up,
        ),
    ],
)